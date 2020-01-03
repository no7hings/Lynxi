# coding:utf-8
from LxBasic import bscAbstract


class Pth_Directory(bscAbstract.Abc_Path):
    def __init__(self, directoryString):
        assert isinstance(directoryString, str) or isinstance(directoryString, unicode), u'Argument: "fileString" must be "str" or "unicode".'
        self._directoryString = self._toPythonPath(directoryString)

    @classmethod
    def _toRelativeNameMethod(cls, rootString, fullpathName):
        return fullpathName[len(rootString) + 1:]

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
                    relativeName = cls._toRelativeNameMethod(rootString, fullpathName_)
                    lis.append(relativeName)

        def mainFnc_():
            for i in cls.os_method.listdir(rootString):
                fullpathName = cls._toFileString(rootString, i)
                if cls.path_method.isfile(fullpathName):
                    collectionFnc_(fullpathName)
                else:
                    if isFile is False:
                        collectionFnc_(fullpathName)
        
        lis = []

        if extString is not None:
            filterExtStringLis = cls._toStringList(extString)
        else:
            filterExtStringLis = None

        if cls.path_method.exists(rootString):
            mainFnc_()

        return lis

    @classmethod
    def _getAllChildMethod(cls, rootString, extString, isFile, isFullpath):
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
                    relativeName = cls._toRelativeNameMethod(rootString, fullpathName_)
                    lis.append(relativeName)

        def mainFnc_():
            for root, _, fileRelativeNames in cls.os_method.walk(rootString, topdown=0):
                for i in fileRelativeNames:
                    fullpathName = cls._toFileString(root, i)
                    if cls.path_method.isfile(fullpathName):
                        collectionFnc_(fullpathName)
                    else:
                        if isFile is False:
                            collectionFnc_(fullpathName)

        lis = []

        if extString is not None:
            filterExtStringLis = cls._toStringList(extString)
        else:
            filterExtStringLis = None

        if cls.path_method.exists(rootString):
            mainFnc_()

        return lis

    def isExist(self):
        return self.os_method.path.exists(self._directoryString)

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
        return self._getAllChildMethod(
            self._directoryString,
            extString=None,
            isFile=False,
            isFullpath=False
        )

    def allChildFileRelativeNames(self):
        u"""
        :return: List of child file's "relative name".
        """
        return self._getAllChildMethod(
            self._directoryString,
            extString=None,
            isFile=True,
            isFullpath=False
        )

    def allChildFileRelativeNamesWithExt(self, extString):
        u"""
        :return: List of child file's "relative name" with "ext".
        """
        return self._getAllChildMethod(
            self._directoryString,
            extString=extString,
            isFile=True,
            isFullpath=False
        )

    def allChildFileTimestampDic(self):
        u"""
        :return: Key = child file's "relative name", Value = child file's "timestamp".
        """
        dic = {}
        for i in self.allChildFileFullpathNames():
            relativeName = self._toRelativeNameMethod(self._directoryString, i)
            timestamp = self.os_method.stat(i).st_mtime
            dic[relativeName] = timestamp

        return dic

    def childFullpathNames(self):
        pass

    def allChildFileFullpathNames(self):
        return self._getAllChildMethod(
            self._directoryString,
            extString=None,
            isFile=True,
            isFullpath=True
        )

    def allChildFullpathNames(self):
        return self._getAllChildMethod(
            self._directoryString,
            extString=None,
            isFile=False,
            isFullpath=True
        )

    def allChildFileFullpathNamesWithExt(self, extString):
        u"""
        :return: List of child file's "relative name" with "ext".
        """
        return self._getAllChildMethod(
            self._directoryString,
            extString=extString,
            isFile=True,
            isFullpath=True
        )

    def __str__(self):
        return self._directoryString