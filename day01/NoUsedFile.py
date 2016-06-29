# -*- encoding: utf-8 -*-
import os
import glob
import fnmatch

class NoUsedFile:

    def readEachLineInFile(self,path,fileName):
        fp = open(path,'r')
        for eachLine in fp:
            if fileName in eachLine:
                print u"文件名:%s \t 路径:%s \n 引用的内容:%s \n" %(fileName,path,eachLine)

    def filesInDir(self,dir):
        headerFiles = []
        headerFilePaths = []
        for root, dirs, files in os.walk(dir):
            if '/Pods' in root:
                continue
            elif '/u3d' in root:
                continue
            elif '/.svn' in root:
                continue
            elif '.framework/' in root:
                continue
            elif 'Framework/' in root:
                continue

            for name in files:
                pattern = '*.h'
                if fnmatch.fnmatch(name,pattern):
                    headerFiles.append(name)
                    headerFilePaths.append(root+"/"+name)
                    # print root + "/" + name
        # print headerFiles,headerFilePaths
        return headerFiles,headerFilePaths

    def listDirNoHidden(self,path):
        return glob.glob(os.path.join(path,'*'))

noUsedFile = NoUsedFile()
# noUsedFile.eachLineInFile('/Users/lizhao/Desktop/UnityAppController.mm')
print noUsedFile.filesInDir('/Users/lizhao/Desktop/EnNew/EnNew1.0')
paths = noUsedFile.filesInDir('/Users/lizhao/Desktop/EnNew/EnNew1.0')[1]
fileNames = noUsedFile.filesInDir('/Users/lizhao/Desktop/EnNew/EnNew1.0')[0]
for path in paths:
    for fileName in fileNames:
        noUsedFile.readEachLineInFile(path,fileName)