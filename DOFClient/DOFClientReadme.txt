DOF Client �ڵ� ���带 ���� ��ȹ

 0. ������ ���� ����
 - �ڵ� ����� python-3.6.1-amd64 +  pycharm-community-2017.1.3 ȯ�濡�� �׽�Ʈ �Ǿ���
 - ��� ���� ������ svn�� commit �Ǿ� �ִ��� Ȯ���Ѵ�.
 - �����Ǿ� �ϴ� ����� �ݵ�� ���� ������ ���� �ν��緯�� �޶�� �Ѵ�.
 - ������ ���� ��� �߰��� svn�� �߰� �ؾ� ���������� �ν��緯�� ���Եȴ�.
 
 
 1. svn ����
	1.1 "trunk\OpenManager_DOF", "trunk\OpenManager 5.0 Installer" ������ REVERT �Ѵ�.
	1.2 "trunk\OpenManager_DOF", "trunk\OpenManager 5.0 Installer" ������ UPDATE �Ѵ�.
  
 2. ������Ʈ ������
	2.1 ������Ʈ�� ������� Rebuild All �Ѵ�.
		* VS2008������ Rebuile �ɼ��� �ֱ� ������ NGF�� �ٸ��� Clean �ܰ谡 �ʿ� ����.
	2.2 Common version�� Release ���� ������ �Ѵ�.
		* trunk\OpenManager_DOF\OpenManager\Workspaces\MainFullVersion\MainFullVersion.sln
		* trunk\OpenManager_DOF\OpenManager\Workspaces\ModulesCommon\ModulesCommon.sln
	2.3 Anycatcher Version�� Release_AnyCatcher ���� ������ �Ѵ�.
		* trunk\OpenManager_DOF\OpenManager\Workspaces\MainFullVersion\AnyCatcher.sln
	2.4 BTV Version�� Release_BTV ���� ������ �Ѵ�.
		* trunk\OpenManager_DOF\OpenManager\Modules\Custom\BTV\BTV_full.sln
	
 3. ����� ���� 
	3.1 ���� �Ϸ�� ������ ���� ���� ���� ������ ���Ͽ� installer ������Ʈ�� patch ������ �������ش�.
	3.2.1 �Ϲ� ���� �ν��緯 ó��
		- trunk\OpenManager_DOF\OpenManager\Release\bin\*.exe | *.dll | *.ocx	-> trunk\OpenManager 5.0 Installer\SetupFile\Common\Bin\*.* �����Ѵ�.
		- trunk\OpenManager_DOF\OpenManager\Release\modules\*.dll				-> trunk\OpenManager 5.0 Installer\SetupFile\Common\Modules\*.* �����Ѵ�.
	3.2.2 �Ϲݹ��� Patch ó��
		- trunk\OpenManager_DOF\OpenManager\Release\bin\*.exe | *.dll | *.ocx	-> D:\Upload\OpenManager5\release\autobuild\5.0.YYYYMMDD_HHMM\Patch\DOFClient\bin
		- trunk\OpenManager_DOF\OpenManager\Release\modules\*.dll				-> D:\Upload\OpenManager5\release\autobuild\5.0.YYYYMMDD_HHMM\Patch\DOFClient\Modules
	
	3.3.1 Anycatcher ���� �ν��緯 ó��
		- trunk\OpenManager_DOF\OpenManager\ReleaseAnycatcher\bin\*.exe		-> trunk\OpenManager 5.0 Installer\CustomSetupFile\AnyCatcher\Common\Bin\*.* �����Ѵ�.
		- trunk\OpenManager_DOF\OpenManager\ReleaseAnycatcher\modules\*.* 	-> trunk\OpenManager 5.0 Installer\CustomSetupFile\AnyCatcher\Common\Modules\*.* �����Ѵ�.
	3.3.2 Anycatcher Patch ó��
		- trunk\OpenManager_DOF\OpenManager\ReleaseAnycatcher\bin\*.exe		-> D:\Upload\OpenManager5\release\autobuild\5.0.YYYYMMDD_HHMM\Patch\AnycatcherClient\bin
		- trunk\OpenManager_DOF\OpenManager\ReleaseAnycatcher\modules\*.*	-> D:\Upload\OpenManager5\release\autobuild\5.0.YYYYMMDD_HHMM\Patch\AnycatcherClient\modules
		
	3.4.1 BTV ���� �ν��緯 ó��
		- trunk\OpenManager_DOF\OpenManager\ReleaseBtv\modules\*.* -> trunk\OpenManager 5.0 Installer\CustomSetupFile\BTV\Common\Modules\*.* �����Ѵ�.
	3.4.2 BTV Patch ó��
		- trunk\OpenManager_DOF\OpenManager\ReleaseBtv\modules\*.* -> D:\Upload\OpenManager5\release\autobuild\5.0.YYYYMMDD_HHMM\Patch\btv\modules

4. �ν��緯 ����
	4.1 �Ʒ��� ISM ���Ͽ��� <ProductVersion> node�� ã�Ƽ� ���� ��¥�� �������� ProductVersion�� �����Ѵ�.
		* "trunk\\OpenManager 5.0 Installer\\AnyCatcher.ism"
		* "trunk\\OpenManager 5.0 Installer\\OpenManager 5.0_Lite.ism"		
	4.2 trunk\autobuild\YYYYMMDD_HHMM\ ������ installer ������Ʈ�� export �Ѵ�.
	4.3 �ν��緯 ������Ʈ�� ���� �Ѵ�.
	4.4 ����� �ν��緯�� ���� ��¥�� �°� ���ϸ� ���� �� Upload ������ �����Ѵ�.
	
5. FTP ���ε�
	6.1 Upload ������ ����� patch module(���� ������ ����Ǿ� 4�� �ܰ迡�� ����� ���)�� �ν��緯�� WinSCP�� �̿��� FTP�� �����Ѵ�.
		* OpenManager5/release/client/autobuild/5.0.YYYYMMDD_HHMM/ �� ���ε� �ȴ�.
	
6. ���ε� �Ϸ� �� Slack ä�ο� �۾� �ϷḦ �˷��ش�.