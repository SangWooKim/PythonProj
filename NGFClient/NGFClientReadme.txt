NGF Client �ڵ� ���带 ���� ��ȹ

 0. ������ ���� ����
 - �ڵ� ����� python-3.6.1-amd64 +  pycharm-community-2017.1.3 ȯ�濡�� �׽�Ʈ �Ǿ���
 - ��� ���� ������ svn�� commit �Ǿ� �ִ��� Ȯ���Ѵ�.
 - �����Ǿ� �ϴ� ����� �ݵ�� ���� ������ ���� �ν��緯�� �޶�� �Ѵ�.
 - ������ ���� ��� �߰��� svn�� �߰� �ؾ� ���������� �ν��緯�� ���Եȴ�.
 
 
 1. svn ����
	1.1 "trunk\OpenManager3.2x", "trunk\OpenManager 3.2 Installer" ������ REVERT �Ѵ�.
	1.2 "trunk\OpenManager3.2x", "trunk\OpenManager 3.2 Installer" ������ UPDATE �Ѵ�.
	
 2. Prject Clean
	2.1 Workspaces\MainFullVersion\MainFullVersion.dsw ������Ʈ�� Clean�Ѵ�.
	2.2 Workspaces\MainFullVersion\MainFullVersion.dsw ������Ʈ���� mesh build�� clean�Ѵ�.
	2.3 Workspaces\ModulesCommon\ModulesCommon.dsw ������Ʈ�� clean�Ѵ�.
 
 3. ������Ʈ ������
	3.1 Mesh �������� ����ϴ� icon�� �ٸ��� ������ �Ϲݹ��� �������� icon�� �������ش�.
		- omc_main.ico -> openmanager.ico, omc_NGF.ico -> NGF.ico
	3.2 Workspaces\MainFullVersion\MainFullVersion.dsw ������Ʈ�� ���� �Ѵ�.
	3.3 Workspaces\ModulesCommon\ModulesCommon.dsw ������Ʈ�� �����Ѵ�.
	
	3.4 Mesh �������� ����ϴ� icon�� �ٸ��� ������ Mesh ���� �������� icon�� �������ش�.
		- mesh_main.ico -> openmanager.ico, mesh_NGF.ico -> NGF.ico
	3.5 Workspaces\MainFullVersion\MainFullVersion.dsw ������Ʈ Mesh ���� �Ѵ�.
	
 4. ����� ���� 
	4.1 ���� �Ϸ�� ������ ���� ���� ���� ������ ���Ͽ� installer ������Ʈ�� patch ������ �������ش�.
	4.2.1 �Ϲ� ���� �ν��緯 ó��
		- trunk\OpenManager3.2x\OpenManager\Release\bin\*.*		-> trunk\OpenManager 3.2 Installer\SetupFile\Common\Bin\*.* �����Ѵ�.
		- trunk\OpenManager3.2x\OpenManager\Release\modules\*.* -> trunk\OpenManager 3.2 Installer\SetupFile\Common\Modules\*.* �����Ѵ�.
	4.2.2 �Ϲݹ��� Patch ó��
		- trunk\OpenManager3.2x\OpenManager\Release\bin\*.*		-> D:\Upload\OpenManager3\release\autobuild\3.4.YYYYMMDD_HHMM\patch\NGFClient.Auth\Bin\*.* �����Ѵ�.
		- trunk\OpenManager3.2x\OpenManager\Release\modules\*.* -> D:\Upload\OpenManager3\release\autobuild\3.4.YYYYMMDD_HHMM\patch\NGFClient.Auth\Modules\*.* �����Ѵ�.
	
	
	4.3.1 Mesh ���� �ν��緯 ó��
		- trunk\OpenManager3.2x\OpenManager\Release\bin\CloudMesh.exe	-> trunk\OpenManager 3.2 Installer\CustomSetupFile\MESH\bin\cloudmesh.exe ���� �Ѵ�.
		- trunk\OpenManager3.2x\OpenManager\Release\bin\OMUpdater.exe	-> trunk\OpenManager 3.2 Installer\CustomSetupFile\MESH\bin\OMUpdater.exe ���� �Ѵ�.
		- trunk\OpenManager3.2x\OpenManager\Release\modules\*.*			-> trunk\OpenManager 3.2 Installer\CustomSetupFile\MESH\modules*.* �����Ѵ�.
		# Mesh module ���
			* SendSMS.dll
			* ServerStatus.dll
			* VMCreate.dll
			* VMDataInfo.dll
			* VMManagement.dll
			* VMOperation.dll
			* VM_GuestResOp.dll
			* VM_StatusDlg.dll
			* VM_StatusDlg1.dll
			* VRInfoView.dll
	4.3.2 Mesh Patch ó��
		- trunk\OpenManager3.2x\OpenManager\Release\bin\CloudMesh.exe	-> D:\Upload\OpenManager3\release\autobuild\3.4.YYYYMMDD_HHMM\patch\MESH\bin\cloudmesh.exe ���� �Ѵ�.
		- trunk\OpenManager3.2x\OpenManager\Release\bin\OMUpdater.exe	-> D:\Upload\OpenManager3\release\autobuild\3.4.YYYYMMDD_HHMM\patch\MESH\bin\OMUpdater.exe ���� �Ѵ�.
		- trunk\OpenManager3.2x\OpenManager\Release\modules\*.*			-> D:\Upload\OpenManager3\release\autobuild\3.4.YYYYMMDD_HHMM\patch\MESH\modules*.* �����Ѵ�.
	
	
 5. �ν��緯 ����
	5.1 �Ʒ��� ISM ���Ͽ��� ����  <ProductVersion> node�� ã�Ƽ� ���� ��¥�� �������� ProductVersion�� �����Ѵ�.
		* "trunk\\OpenManager 3.2 Installer\\OpenManager 3.2.ism"
		* "trunk\\OpenManager 3.2 Installer\\CloudMesh_Lite.ism"
		* "trunk\\OpenManager 3.2 Installer\\OpenManager 3.2_IOMC.ism"
	4.2 trunk\autobuild\YYYYMMDD_HHMM\ ������ installer ������Ʈ�� export �Ѵ�.
	4.3 �ν��緯 ������Ʈ�� ���� �Ѵ�.
	4.4 ����� �ν��緯�� ���� ��¥�� �°� ���ϸ� ���� �� Upload ������ �����Ѵ�.
	
 6. FTP ���ε�
	6.1 Upload ������ ����� patch module(���� ������ ����Ǿ� 4�� �ܰ迡�� ����� ���)�� �ν��緯�� WinSCP�� �̿��� FTP�� �����Ѵ�.
		* OpenManager3/release/client/autobuild/3.4.YYYYMMDD_HHMM/ �� ���ε� �ȴ�.

 7. GIT ���� ���
    7.1 "D:\svn_backup\NGF" ��ο� svn fetch�� �̿��Ͽ� GIT ����� �Ѵ�.
	
 8. ���ε� �Ϸ� �� Slack ä�ο� �۾� �ϷḦ �˷��ش�.
 
 
	