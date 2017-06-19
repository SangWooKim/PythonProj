# -*- coding: utf-8 -*-
from Lib import SVNClientWrapper
from Lib import VSWrapper
from Lib import BasicFunctions
from Lib import InstallerWrapper

from slackclient import SlackClient

import shutil
import subprocess
import os
import logging
import logging.handlers
import configparser

basicfunction = BasicFunctions.BasicFunctions()
curTime = basicfunction.getCurrentTime()

# 로그를 남길 폴더를 만들고, 스트림 핸들러와 파일 핸들러를 붙여준다.
logdir = '{0}\\log\\{1}'.format(os.getcwd(), curTime)

if not os.path.exists(logdir):
    os.makedirs(logdir)

logger = logging.getLogger('dof_auto_build_logger')
fileHandler = logging.FileHandler('{0}/autobuild_{1}.log'.format(logdir, curTime))
streamHandler = logging.StreamHandler()

logger.addHandler(fileHandler)
logger.addHandler(streamHandler)
logger.setLevel(logging.DEBUG)

# 같은 경로에 있는 config.txt 파일을 읽어서 기본 root의 정보를 얻는다.
config = configparser.ConfigParser()

if os.path.exists('.\config.txt'):
    config.read('.\config.txt')
    config.set('DOF', 'autobuild', '{0}\\5.0.{1}'.format(config.get('DOF', 'autobuild'), curTime))
else:
    config.add_section('DOF')
    config.set('DOF', 'proj_root', 'D:\\DOF_FULL\\trunk')
    config.set('DOF', 'autobuild', 'D:\\Upload\\OpenManager5\\release\\autobuild\\5.0.{0}'.format(curTime))
    config.set('DOF', 'ftp_upload', '220.76.205.150:10021/OpenManager5/release/client/autobuild')
    config.add_section('slack')
    config.set('slack', 'channel', '#Chappie')

dof_proj_trunk = config.get('DOF', 'proj_root')
dof_autobuild = config.get('DOF', 'autobuild')
ftp_upload = config.get('DOF', 'ftp_upload')

# trunk에서 시작하는 경로는 변경 될 수 없다.
dof_installer_root = '{0}\\OpenManager 5.0 Installer'.format(dof_proj_trunk)
dof_source_root = '{0}\\OpenManager_DOF'.format(dof_proj_trunk)
dof_workspaces_path = '{0}\\OpenManager\\Workspaces'.format(dof_source_root)
dof_release_root = '{0}\\OpenManager\\Release'.format(dof_source_root)

# 로컬에서 저장된 svn의 경로
svnRepositoryList = [dof_source_root, dof_installer_root]

# vs6환경에서 clean하기 위한 프로젝트 파일명과 빌드 옵션을 map으로 만들어 준다.
OMCBuildProject = {'OpenManager - Win32 R_Auth': '{0}\\MainFullVersion\\MainFullVersion.dsw'.format(dof_workspaces_path)
    , 'About - Win32 Release': '{0}\\ModulesCommon\\ModulesCommon.dsw'.format(dof_workspaces_path)
    , 'OMUpdater - Win32 Release': '{0}\\Updater\\OMUpdater.dsw'.format(dof_workspaces_path)}

MeshBuildProject = {
    'OpenManager - Win32 R_Auth_Mesh': '{0}\\MainFullVersion\\MainFullVersion.dsw'.format(dof_workspaces_path)
    , 'OMUpdater - Win32 Release': '{0}\\Updater\\MeshUpdater.dsw'.format(dof_workspaces_path)}

IOMCBuildProject = {'OMUpdater - Win32 Release_IOMC': '{0}\\Updater\\OMUpdater.dsw'.format(dof_workspaces_path)}

# icon 복사 root
resRoot = '{0}\\OpenManager\\MainApplication\\FullVersion\\res'.format(dof_source_root)

if __name__ == "__main__":
    logger.info('=======================================')
    logger.info('DOF Client AutoBuild Start')
    logger.info('=======================================')

    basicfunction = BasicFunctions.BasicFunctions()
    curTime = basicfunction.getCurrentTime()

    # SVN 정리
    svnclient = SVNClientWrapper.SVNClient(svnRepositoryList)

    svnclient.svnRevert();
    svnclient.svnUpdate();

    # vs6 project clean
    vsclient = VSWrapper.VisualStudio(VSWrapper.VisualStudionVerionEnum.VS6, logdir)
    vsclient.CleanProject(OMCBuildProject)
    vsclient.CleanProject(MeshBuildProject)
    vsclient.CleanProject(IOMCBuildProject)

    ####################################################
    #########일반 OMC 처리하기
    shutil.copyfile('{0}\\omc_main.ico'.format(resRoot), '{0}\\openmanager.ico'.format(resRoot))
    shutil.copyfile('{0}\\omc_NGF.ico'.format(resRoot), '{0}\\NGF.ico'.format(resRoot))
    vsclient.BuildProject(OMCBuildProject)

    targetPathList = ['bin', 'modules']

    installerPath = '{0}\\SetupFile\\Common'.format(dof_installer_root)
    patchPath = '{0}\\patch\\NGFClient.Auth'.format(dof_autobuild)

    basicfunction.copyUpdateModules(targetPathList, dof_release_root, installerPath, patchPath)

    ####################################################
    #########  MESH 처리하기
    shutil.copyfile('{0}\\mesh_main.ico'.format(resRoot), '{0}\\openmanager.ico'.format(resRoot))
    shutil.copyfile('{0}\\mesh_NGF.ico'.format(resRoot), '{0}\\NGF.ico'.format(resRoot))
    vsclient.BuildProject(MeshBuildProject)

    installerPath = '{0}\\CustomSetupFile\\MESH'.format(dof_installer_root)
    patchPath = '{0}\\patch\\MESH'.format(dof_autobuild)

    basicfunction.copyUpdateModules(targetPathList, dof_release_root, installerPath, patchPath)

    ####################################################
    #########  IOMC 처리하기
    vsclient.BuildProject(IOMCBuildProject)
    installerPath = '{0}\\CustomSetupFile\\IOMC\\common'.format(dof_installer_root)
    patchPath = '{0}\\patch\\IOMC'.format(dof_autobuild)

    basicfunction.copyUpdateModules(targetPathList, dof_release_root, installerPath, patchPath)

    # install shield porductversion update

    ismList = []
    ismList.append("{0}\\OpenManager 3.2.ism".format(dof_installer_root))
    ismList.append("{0}\\CloudMesh_Lite.ism".format(dof_installer_root))
    ismList.append("{0}\\OpenManager 3.2_IOMC.ism".format(dof_installer_root))
    installshield = InstallerWrapper.Installer(ismList, '3.4')
    installshield.versioninfoUpdate()

    # svn export
    svnclient.svnExport(dof_installer_root, '{0}\\autobuild\\{1}'.format(dof_proj_trunk, curTime))

    # installer build
    del ismList[:]

    workdir = '{0}\\autobuild\\{1}'.format(dof_proj_trunk, curTime)
    omc_arg = [workdir, 'OpenManager 3.2.ism', 'Release_AUTHORITY']
    mesh_arg = [workdir, 'CloudMesh_Lite.ism', 'Release_Mesh_Authority']
    iomc_arg = [workdir, 'OpenManager 3.2_IOMC.ism', 'IOMC_Auth']

    ismList.append(omc_arg)
    ismList.append(mesh_arg)
    ismList.append(iomc_arg)
    installshield.buildISM(ismList)

    if not os.path.exists(dof_autobuild):
        os.makedirs(dof_autobuild)

    shutil.copyfile('{0}\\ReleaseInstaller\\OMCAuthority_3.4.exe'.format(workdir),
                    '{0}\\OMCAuthority_3.4.{1}.exe'.format(dof_autobuild, curTime))
    shutil.copyfile('{0}\\ReleaseInstaller\\CloudMeshAuthority_3.4.exe'.format(workdir),
                    '{0}\\CloudMeshAuthority_3.4.{1}.exe'.format(dof_autobuild, curTime))
    shutil.copyfile('{0}\\ReleaseInstaller\\IOMC_3.4.exe'.format(workdir),
                    '{0}\\IOMC_3.4.{1}.exe'.format(dof_autobuild, curTime))

    logger.info('ftp upload start')

    # win scp ftp upload
    subprocess.call(['C:\\Program Files (x86)\\WinSCP\\WinSCP.exe'
                        , '/command'
                        , 'option batch abort'
                        , 'option confirm off'
                        , 'option transfer binary'
                        , 'open ftp://ubicom:ubicom!23@{0}'.format(ftp_upload)
                        , 'put {0}'.format(dof_autobuild)
                        , 'close'
                        , 'exit'
                     ])
    logger.info('ftp upload END')

    # git backup
    logger.info('GIT Backup')
    subprocess.call(["c:\\Program Files (x86)\\Git\\bin\\git.exe"
                        , '-C'
                        , "D:\\svn_backup\\NGF"
                        , 'svn'
                        , 'fetch'
                     ])
    # slack noti
    logger.info('Slack notify')
    slack_client = SlackClient(config.get('slack', 'bot_token'))
    slack_client.api_call("chat.postMessage", channel=config.get('slack', 'channel'), text='NGF Build 완료', as_user=True)

    # end Main
    logger.info("NGF Client Auto Build END")