# coding:utf-8
from LxBasic import bscAbstract


class Pth_Directory(bscAbstract.Abc_Path):
    def __init__(self, directoryString):
        assert isinstance(directoryString, str) or isinstance(directoryString, unicode), u'Argument: "fileString" must be "str" or "unicode".'
        self._directoryString = self._osPathToPythonStyle(directoryString)

    @classmethod
    def _getChildMethod(cls, rootString, extString, isFile, isFullpath):
        def extFilterFnc_(fullpathName_):
            if filterExtStringLis is not None:
                for i in filterExtStringLis:
                    if fullpathName_.endswith(i):
                        return True
                return False
            return True

        def collectionFnc_(fullpathName_):
            if extFilterFnc_(fullpathName_) is True:
                if isFullpath is True:
                    lis.append(fullpathName_)
                else:
                    relativeName = cls._osPathString2RelativeName(rootString, fullpathName_)
                    lis.append(relativeName)

        def mainFnc_():
            for i in cls.MOD_os.listdir(rootString):
                fullpathName = cls._toOsFilename(rootString, i)
                if cls.MTD_os_path.isfile(fullpathName):
                    collectionFnc_(fullpathName)
                else:
                    if isFile is False:
                        collectionFnc_(fullpathName)
        
        lis = []

        if extString is not None:
            filterExtStringLis = cls.toStringList(extString)
        else:
            filterExtStringLis = None

        if cls.MTD_os_path.exists(rootString):
            mainFnc_()

        return lis

    def isExist(self):
        return self.MOD_os.path.exists(self._directoryString)

    def create(self):
        pass

    def childRelativeNames(self):
        u"""
        :return: List of child's "relative name".
        """
        return self._getChildMethod(
            self._directoryString,
            extString=None,
            isFile=False,
            isFullpath=False
        )

    def childFileRelativeNames(self):
        u"""
        :return: List of child file's "relative name".
        """
        return self._getChildMethod(
            self._directoryString,
            extString=None,
            isFile=True,
            isFullpath=False
        )

    def allChildRelativeNames(self):
        u"""
        :return: List of child's "relative name".
        """
        return self._getPathnameListByOsDirectory(
            self._directoryString,
            extString=None,
            isFile=False,
            isFullpath=False,
            isAll=True
        )

    def allChildFileRelativeNames(self):
        u"""
        :return: List of child file's "relative name".
        """
        return self._getPathnameListByOsDirectory(
            self._directoryString,
            extString=None,
            isFile=True,
            isFullpath=False,
            isAll=True
        )

    def allChildFileRelativeNamesWithExt(self, extString):
        u"""
        :return: List of child file's "relative name" with "ext".
        """
        return self._getPathnameListByOsDirectory(
            self._directoryString,
            extString=extString,
            isFile=True,
            isFullpath=False,
            isAll=True
        )

    def allChildFileTimestampDic(self):
        u"""
        :return: Key = child file's "relative name", Value = child file's "timestamp".
        """
        dic = {}
        for i in self.allChildFileFullpathNames():
            relativeName = self._osPathString2RelativeName(self._directoryString, i)
            timestamp = self.MOD_os.stat(i).st_mtime
            dic[relativeName] = timestamp

        return dic

    def childFullpathNames(self):
        pass

    def allChildFileFullpathNames(self):
        return self._getPathnameListByOsDirectory(
            self._directoryString,
            extString=None,
            isFile=True,
            isFullpath=True,
            isAll=True
        )

    def allChildFullpathNames(self):
        return self._getPathnameListByOsDirectory(
            self._directoryString,
            extString=None,
            isFile=False,
            isFullpath=True,
            isAll=True
        )

    def allChildFileFullpathNamesWithExt(self, extString):
        u"""
        :return: List of child file's "relative name" with "ext".
        """
        return self._getPathnameListByOsDirectory(
            self._directoryString,
            extString=extString,
            isFile=True,
            isFullpath=True,
            isAll=True
        )

    def __str__(self):
        return self._directoryString


class Pth_Maya(bscAbstract.Abc_DccPath):
    separator_namespace = ':'
    separator_node = '|'
    separator_attribute = '.'

    def __init__(self, pathString):
        self._initAbcDccPath(pathString)
