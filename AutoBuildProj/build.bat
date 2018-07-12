@echo off
setlocal

@set project=EMPTY

:redo
echo.
echo =========================================
echo OpenManager Client Auto Build
echo =========================================
echo 0(exit)         : �����մϴ�.
echo 1(NGF Client )  : NGF�� ���� �մϴ�.
echo 2(DOF Client )  : DOF�� ���� �մϴ�.
echo 3(Agent)        : Agent Window ������ ���� �մϴ�.
echo 4(Agent-Module) : Agent�� ��� common ����� ���� �մϴ�.
echo 5(DOF Update)   : DOF�� ������Ʈ ��ġ�� ���� �մϴ�.
::echo 6(NGF Update)   : NGF�� ������Ʈ ��ġ�� ���� �մϴ�.
echo.
set /p type=����Ÿ���� �����ϼ���. : 

echo ������ ���� Ÿ���� : %type%

if %type%== 0 goto QUIT
if %type%== 1 goto ngf_build
if %type%== 2 goto dof_build
if %type%== 3 goto agent_build
if %type%== 4 goto agent_module_build
if %type%== 5 goto dof_update_build
if %type%== 6 goto ngf_update_build

echo �߸��� �����Դϴ�. 

goto redo


:ngf_build

echo.
echo =========================================
echo NGF Client ������Ʈ�� build �մϴ�. 
echo ���Ϲ����� ����� ��⸸ �ν��緯�� ���Ե˴ϴ�.
echo �Ϸ� �� FTP�� ������ �մϴ�.
echo �۾� �Ϸ� �� �������� �Ϸ� �޽����� �����ϴ�.
echo =========================================
call python NGFAutobuildMain.py
set project=NGF

goto confirm_commit

:dof_build

echo.
echo =========================================
echo DOF Client ������Ʈ�� build �մϴ�. 
echo ���Ϲ����� ����� ��⸸ �ν��緯�� ���Ե˴ϴ�.
echo �Ϸ� �� FTP�� ������ �մϴ�.
echo �۾� �Ϸ� �� �������� �Ϸ� �޽����� �����ϴ�.
echo =========================================
call python DOFAutobuildMain.py
set project=DOF

goto confirm_commit

:agent_build
echo.
echo =========================================
echo OMAGENT ������Ʈ�� build �մϴ�. 
echo �ҽ� ������ �߻��� ��⸸ ����Ǿ� �ν��緯�� �ۼ��ϰ�, FTP�� ���ε� �մϴ�.
echo �۾� �Ϸ� �� �������� �Ϸ� �޽����� �����ϴ�.
echo =========================================
call python AgentAutoBuildMain.py
set project=AGENT

goto confirm_commit

:agent_module_build
echo.
echo =========================================
echo Agent Module ������Ʈ�� build �մϴ�. 
echo �ҽ� ������ �߻��� ��⸸ ����Ǿ� �ν��緯�� �ۼ��ϰ�, FTP�� ���ε� �մϴ�.
echo �۾� �Ϸ� �� �������� �Ϸ� �޽����� �����ϴ�.
echo =========================================
call python AgentModuleAutoBuildMain.py
set project=AGENT

goto confirm_commit

:dof_update_build
echo.
echo =========================================
echo DOF Update ������Ʈ�� build �մϴ�. 
echo update ������ �ִ� ���θ� �ν��縦 ����ϴ�.
echo �۾� �Ϸ� �� �������� �Ϸ� �޽����� �����ϴ�.
echo =========================================
call python DOFUpdateBuildMain.py
set project=DOF_UPDATE

goto confirm_commit


:confirm_commit
echo.
echo =========================================
echo %project% ���尡 �Ϸ� �Ǿ����ϴ�. 
echo SVN�� Ŀ�� �Ͻðڽ��ϱ�?
echo =========================================
set /p commit= y(commit), n(continue)

if %commit%== y call python autocommit.py %project%

goto redo



:QUIT
PAUSE