#-*- coding: utf-8 -*-

import os
import time
import shutil
#pip install pypiwin32
from win32api import GetFileVersionInfo, LOWORD, HIWORD

class BasicFunctions(object):

    def __init__(self):
        return


    #주어진 경로에서 파일목록을 얻는다.
    def getfilenames(self, dirname):
        filenames = os.listdir(dirname)
        return  filenames



    def get_version_number(self, filename):
        try:
            info = GetFileVersionInfo(filename, "\\")
            ms = info['FileVersionMS']
            ls = info['FileVersionLS']
            return '{0}.{1}.{2}.{3}'.format( HIWORD(ms), LOWORD(ms), HIWORD(ls), LOWORD(ls) )
        except:
            return '0.0.0.0'

    #dfilepath가 존재하고, sfilepaht와 파일 버전 정보가 다른 경우 true를 리턴한다.
    def isCopyFile(self, sfilepath, dfilepath):

        if os.path.isfile(sfilepath) and os.path.isfile(dfilepath):
            sfileVer = self.get_version_number(sfilepath)
            dfileVer = self.get_version_number(dfilepath)
            if sfileVer != dfileVer:
                print(sfileVer + '    ' + dfileVer)
                return True

        return  False


    def getCurrentTiem(self):
        now = time.localtime()
        s = "%04d%02d%02d_%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
        return  s


    def copyUpdateModules(self, targetPathList, releasePath, installerPath, patchPath):
        for target in targetPathList:
            sourceFileList = self.getfilenames('{0}\\{1}'.format(releasePath, target))

            for fileName in sourceFileList:
                dFilePath = '{0}\\{1}\\{2}'.format(installerPath, target, fileName)
                sFilePath = '{0}\\{1}\\{2}'.format(releasePath, target, fileName)
                pFilePath = '{0}\\{1}\\{2}'.format(patchPath, target, fileName)

                print(sFilePath + " " + dFilePath + " " + pFilePath)

                if self.isCopyFile(sFilePath, dFilePath):
                    shutil.copyfile(sFilePath, dFilePath)
                    shutil.copyfile(sFilePath, pFilePath)
        return