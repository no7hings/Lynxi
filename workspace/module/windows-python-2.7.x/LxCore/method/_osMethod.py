# coding:utf-8
import yaml
#
from LxCore.method.basic import _methodBasic


#
class OsFileMethod(_methodBasic.Mtd_PlfFile):
    pass


#
class OsMultFileMethod(_methodBasic.Mtd_PlfFile):
    OsMultiFileKeywordLis = [
        '<udim>',
        '%04d',
        '####',
        '<f>'
    ]
    @classmethod
    def isOsExistsMultiFile(cls, osMultiFile):
        boolean = False
        multiFileLis = cls.getOsMultiFileSubFileLis(osMultiFile)
        if multiFileLis:
            boolean = True
        return boolean
    @classmethod
    def getOsMultiFileSubFileLis(cls, osMultiFile, useMode=0):
        lis = []
        # Single File
        if cls.isOsExistsFile(osMultiFile):
            lis = [osMultiFile]
        else:
            for keyword in cls.OsMultiFileKeywordLis:
                if keyword.lower() in osMultiFile.lower():
                    lis = cls.getOsMultiFileLisSub(osMultiFile, keyword)
                    break
        #
        if useMode == 1:
            if lis:
                lis = [[lis[0]], lis[1:]][len(lis) > 1]
        return lis
    @classmethod
    def setOsMultiFileCollection(cls, osMultiFile, targetOsPath, ignoreMtimeChanged=False, ignoreExists=False, backupExists=False):
        subOsFileLis = cls.getOsMultiFileSubFileLis(osMultiFile)
        if subOsFileLis:
            cls.setOsFileCollection(subOsFileLis, targetOsPath, ignoreMtimeChanged, ignoreExists, backupExists)
    @classmethod
    def getOsUdimFileSubFileLis(cls, osMultiFile, useMode=0):
        if cls.isOsExistsFile(osMultiFile):
            lis = [osMultiFile]
        # Mult File
        else:
            lis = cls.getOsMultiFileLisSub(osMultiFile, '<udim>')
        #
        if useMode == 1:
            if lis:
                lis = [[lis[0]], lis[1:]][len(lis) > 1]
        return lis


#
class OsYamlFileMethod(_methodBasic.Mtd_PlfFile):
    @classmethod
    def writeOsYaml(cls, data, osYamlFile):
        cls.setOsFileDirectoryCreate(osYamlFile)
        #
        with open(osYamlFile, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)
    @classmethod
    def readOsYaml(cls, osYamlFile):
        if cls.isOsExistsFile(osYamlFile):
            with open(osYamlFile) as f:
                data = yaml.load(f)
                return data
