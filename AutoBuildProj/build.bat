@echo off
setlocal

@set project=EMPTY

:redo
echo.
echo =========================================
echo OpenManager Client Auto Build
echo =========================================
echo 0(exit)         : 종료합니다.
echo 1(NGF Client )  : NGF를 빌드 합니다.
echo 2(DOF Client )  : DOF를 빌드 합니다.
echo 3(Agent)        : Agent Window 버전을 빌드 합니다.
echo 4(Agent-Module) : Agent의 모든 common 모듈을 빌드 합니다.
echo 5(DOF Update)   : DOF의 업데이트 패치를 빌드 합니다.
::echo 6(NGF Update)   : NGF의 업데이트 패치를 빌드 합니다.
echo.
set /p type=빌드타입을 선택하세요. : 

echo 선택한 빌드 타입은 : %type%

if %type%== 0 goto QUIT
if %type%== 1 goto ngf_build
if %type%== 2 goto dof_build
if %type%== 3 goto agent_build
if %type%== 4 goto agent_module_build
if %type%== 5 goto dof_update_build
if %type%== 6 goto ngf_update_build

echo 잘못된 선택입니다. 

goto redo


:ngf_build

echo.
echo =========================================
echo NGF Client 프로젝트를 build 합니다. 
echo 파일버전이 변경된 모듈만 인스톨러에 포함됩니다.
echo 완료 후 FTP에 업르도 합니다.
echo 작업 완료 후 슬랙으로 완료 메시지가 나갑니다.
echo =========================================
call python NGFAutobuildMain.py
set project=NGF

goto confirm_commit

:dof_build

echo.
echo =========================================
echo DOF Client 프로젝트를 build 합니다. 
echo 파일버전이 변경된 모듈만 인스톨러에 포함됩니다.
echo 완료 후 FTP에 업르도 합니다.
echo 작업 완료 후 슬랙으로 완료 메시지가 나갑니다.
echo =========================================
call python DOFAutobuildMain.py
set project=DOF

goto confirm_commit

:agent_build
echo.
echo =========================================
echo OMAGENT 프로젝트를 build 합니다. 
echo 소스 수정이 발생한 모듈만 변경되어 인스톨러를 작성하고, FTP에 업로드 합니다.
echo 작업 완료 후 슬랙으로 완료 메시지가 나갑니다.
echo =========================================
call python AgentAutoBuildMain.py
set project=AGENT

goto confirm_commit

:agent_module_build
echo.
echo =========================================
echo Agent Module 프로젝트를 build 합니다. 
echo 소스 수정이 발생한 모듈만 변경되어 인스톨러를 작성하고, FTP에 업로드 합니다.
echo 작업 완료 후 슬랙으로 완료 메시지가 나갑니다.
echo =========================================
call python AgentModuleAutoBuildMain.py
set project=AGENT

goto confirm_commit

:dof_update_build
echo.
echo =========================================
echo DOF Update 프로젝트를 build 합니다. 
echo update 폴더에 있는 모듈로만 인스톨를 만듭니다.
echo 작업 완료 후 슬랙으로 완료 메시지가 나갑니다.
echo =========================================
call python DOFUpdateBuildMain.py
set project=DOF_UPDATE

goto confirm_commit


:confirm_commit
echo.
echo =========================================
echo %project% 빌드가 완료 되었습니다. 
echo SVN에 커밋 하시겠습니까?
echo =========================================
set /p commit= y(commit), n(continue)

if %commit%== y call python autocommit.py %project%

goto redo



:QUIT
PAUSE