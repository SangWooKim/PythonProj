@echo off
setlocal

@set project=EMPTY

:redo
echo.
echo =========================================
echo NGF Client Auto Build
echo =========================================
set /p type= 0(exit), 1(NGF Build ), 2(DOF Build ), 3(Agent Build)

echo ������ ���� Ÿ���� : %type%

if %type%== 0 goto QUIT
if %type%== 1 goto ngf_build
if %type%== 2 goto dof_build
if %type%== 3 goto agent_build

echo �߸��� �����Դϴ�. 

goto redo


:ngf_build

echo.
echo =========================================
echo NGF Client ������Ʈ�� build �մϴ�. 
echo �ҽ� ������ �߻��� ��⸸ ����Ǿ� �ν��緯�� �ۼ��ϰ�, FTP�� ���ε� �մϴ�.
echo �۾� �Ϸ� �� �������� �Ϸ� �޽����� �����ϴ�.
echo =========================================
call python NGFAutobuildMain.py
set project=NGF

goto confirm_commit

:dof_build

echo.
echo =========================================
echo DOF Client ������Ʈ�� build �մϴ�. 
echo �ҽ� ������ �߻��� ��⸸ ����Ǿ� �ν��緯�� �ۼ��ϰ�, FTP�� ���ε� �մϴ�.
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

:confirm_commit
echo.
echo =========================================
echo ���尡 �Ϸ� �Ǿ����ϴ�. SVN�� Ŀ�� �Ͻðڽ��ϱ�?
echo =========================================
set /p commit= y(commit), n(continue)

if %commit%== y call python autocommit.py %project%

goto redo



:QUIT
PAUSE
