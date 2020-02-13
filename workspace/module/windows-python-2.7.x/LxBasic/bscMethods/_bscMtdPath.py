# coding:utf-8
from LxBasic import bscCore

from LxBasic.bscMethods import _bscMtdPython


class OsPath(bscCore.BscMtdPathBasic):
    separator_path = u'/'
    @classmethod
    def composeBy(cls, *args):
        return cls._toOsPathString(*args)

    @classmethod
    def isDirectory(cls, pathString):
        return cls._isOsDirectory(pathString)

    @classmethod
    def isFile(cls, pathString):
        return cls._isOsFile(pathString)

    @classmethod
    def treeViewBuildDic(cls, pathStrings):
        return cls._getTreeViewBuildDic(
            cls._toTreeViewPathLis(pathStrings, cls.separator_path),
            cls.separator_path
        )

    @classmethod
    def isExist(cls, pathString):
        """
        :param pathString: str
        :return: bool
        """
        return cls.MTD_os_path.exists(pathString)


class OsDirectory(bscCore.BscMtdBasic):
    @classmethod
    def create(cls, directoryString):
        cls._setOsDirectoryCreate(directoryString)

    @classmethod
    def allFullpathnames(cls, directoryString):
        """
        :param directoryString: str
        :return: list([str, ...])
        """
        return cls._getPathnameListByOsDirectory(
            directoryString,
            extString=None,
            isFile=False,
            isFullpath=True,
            isAll=True
        )

    @classmethod
    def allFileFullpathnames(cls, directoryString):
        return cls._getPathnameListByOsDirectory(
            directoryString,
            extString=None,
            isFile=True,
            isFullpath=True,
            isAll=True
        )

    @classmethod
    def fullpathnames(cls, directoryString):
        return cls._getPathnameListByOsDirectory(
            directoryString,
            extString=None,
            isFile=False,
            isFullpath=True,
            isAll=False
        )

    @classmethod
    def basenames(cls, directoryString):
        return cls._getPathnameListByOsDirectory(
            directoryString,
            extString=None,
            isFile=False,
            isFullpath=False,
            isAll=False
        )

    @classmethod
    def fileFullpathnames(cls, directoryString):
        return cls._getPathnameListByOsDirectory(
            directoryString,
            extString=None,
            isFile=True,
            isFullpath=True,
            isAll=False
        )

    @classmethod
    def fileBasenames(cls, directoryString):
        return cls._getPathnameListByOsDirectory(
            directoryString,
            extString=None,
            isFile=True,
            isFullpath=False,
            isAll=False
        )

    @classmethod
    def isExist(cls, directoryString):
        """
        :param directoryString: str
        :return: bool
        """
        return cls.MTD_os_path.isdir(directoryString)

    @classmethod
    def setDirectoryCreate(cls, directoryString):
        """
        :param directoryString: str
        :return: None
        """
        cls._setOsDirectoryCreate(directoryString)

    @classmethod
    def allRelativenames(cls, directoryString, extString=None):
        return cls._getPathnameListByOsDirectory(
            rootString=directoryString,
            extString=extString,
            isFile=False,
            isFullpath=False,
            isAll=True
        )

    @classmethod
    def allFileRelativenames(cls, directoryString, extString=None):
        return cls._getPathnameListByOsDirectory(
            rootString=directoryString,
            extString=extString,
            isFile=True,
            isFullpath=False,
            isAll=True
        )

    @classmethod
    def relativenames(cls, directoryString, extString=None):
        return cls._getPathnameListByOsDirectory(
            rootString=directoryString,
            extString=extString,
            isFile=False,
            isFullpath=False,
            isAll=False
        )

    @classmethod
    def fileRelativenames(cls, directoryString, extString=None):
        return cls._getPathnameListByOsDirectory(
            rootString=directoryString,
            extString=extString,
            isFile=True,
            isFullpath=False,
            isAll=False
        )

    @classmethod
    def remove(cls, directoryString):
        children = cls.allFullpathnames(directoryString)
        if children:
            children.reverse()
            for i in children:
                _bscMtdPython.PyMessage.traceResult(u'Remove: {}'.format(i.decode(u'gbk')))
                cls._setOsPathRemove(i)

        cls._setOsPathRemove(directoryString)

    @classmethod
    def moveTo(cls, directoryString, targetDirectoryString):
        filenameLis = cls.allFileFullpathnames(directoryString)
        if filenameLis:
            for i in filenameLis:
                _bscMtdPython.PyMessage.traceResult(u'Move: {}'.format(i.decode(u'gbk')))
                cls._setOsFileMove_(i, targetDirectoryString)

        cls._setOsPathRemove(directoryString)

    @classmethod
    def open(cls, directoryString):
        cls._setOsDirectoryOpen(directoryString)


class AppPath(bscCore.BscMtdPathBasic):
    pass


class MayaPath(bscCore.BscMtdPathBasic):
    separator_namespace = u':'
    separator_node = u'|'
    separator_attribute = u'.'

    @classmethod
    def namespaceSep(cls):
        return cls.separator_namespace

    @classmethod
    def nodeSep(cls):
        return cls.separator_node

    @classmethod
    def attributeSep(cls):
        return cls.separator_attribute

    @classmethod
    def namespace(cls, pathString):
        return cls._getNamespaceByPathString(
            pathString,
            nodeSep=cls.separator_node,
            namespaceSep=cls.separator_namespace
        )

    @classmethod
    def name(cls, pathString):
        return cls._getNameByPathString(
            pathString,
            nodeSep=cls.separator_node,
            namespaceSep=cls.separator_namespace
        )

    @classmethod
    def nameWithNamespace(cls, pathString):
        return cls._getNameWithNamespaceByPathString(
            pathString,
            nodeSep=cls.separator_node
        )

    @classmethod
    def attributeName(cls, pathString):
        return cls._getAttributeNameByPathString(
            pathString,
            attributeSep=cls.separator_attribute
        )

    @classmethod
    def namespaceTreeViewBuildDic(cls, pathString):
        return cls._getTreeViewBuildDic(
            cls._toTreeViewPathLis(pathString, cls.separator_namespace),
            cls.separator_namespace
        )

    @classmethod
    def nodeTreeViewBuildDic(cls, pathString):
        return cls._getTreeViewBuildDic(
            cls._toTreeViewPathLis(pathString, cls.separator_node),
            cls.separator_node
        )

    @classmethod
    def covertToPathCreateDic(cls, dic):
        return cls._setDicConvertToPathCreateDic(dic, cls.separator_node)
