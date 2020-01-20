# coding:utf-8
from LxBasic import bscCore

from LxBasic.bscMethods import _bscMtdPython


class OsPath(bscCore.PathBasic):
    separator_path = u'/'
    @classmethod
    def composeBy(cls, *args):
        if isinstance(args[0], (list, tuple)):
            pathStringLis = args[0]
        else:
            pathStringLis = list(args)

        string = ''
        index = 0
        for i in pathStringLis:
            if i not in ['', None]:
                if index is 0:
                    string = i
                else:
                    string += u'{}{}'.format(cls.separator_path, i)
                index += 1
        return string

    @classmethod
    def treeViewBuildDic(cls, pathStrings):
        return cls._getTreeViewBuildDic(
            cls._toTreeViewPathLis(pathStrings, cls.separator_path),
            cls.separator_path
        )


class OsDirectory(bscCore.Basic):
    @classmethod
    def allPathnames(cls, directoryString):
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
    def allFilenames(cls, directoryString):
        return cls._getPathnameListByOsDirectory(
            directoryString,
            extString=None,
            isFile=True,
            isFullpath=True,
            isAll=True
        )

    @classmethod
    def pathnames(cls, directoryString):
        return cls._getPathnameListByOsDirectory(
            directoryString,
            extString=None,
            isFile=False,
            isFullpath=True,
            isAll=False
        )

    @classmethod
    def pathbasenames(cls, directoryString):
        return cls._getPathnameListByOsDirectory(
            directoryString,
            extString=None,
            isFile=False,
            isFullpath=False,
            isAll=False
        )

    @classmethod
    def filenames(cls, directoryString):
        return cls._getPathnameListByOsDirectory(
            directoryString,
            extString=None,
            isFile=True,
            isFullpath=True,
            isAll=False
        )

    @classmethod
    def filebasenames(cls, directoryString):
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
        return cls.MTD_os_path.exists(directoryString)

    @classmethod
    def setDirectoryCreate(cls, directoryString):
        """
        :param directoryString: str
        :return: None
        """
        cls._setOsDirectoryCreate(directoryString)

    @classmethod
    def getAllChildFileRelativeNames(cls, directoryString, extString):
        return cls._getPathnameListByOsDirectory(
            rootString=directoryString,
            extString=extString,
            isFile=True,
            isFullpath=False,
            isAll=True
        )

    @classmethod
    def remove(cls, directoryString):
        children = cls.allPathnames(directoryString)
        if children:
            children.reverse()
            for i in children:
                _bscMtdPython.PyMessage.traceResult(u'Remove: {}'.format(i.decode(u'gbk')))
                cls._setOsPathRemove(i)

        cls._setOsPathRemove(directoryString)

    @classmethod
    def moveTo(cls, directoryString, targetDirectoryString):
        filenameLis = cls.allFilenames(directoryString)
        if filenameLis:
            for i in filenameLis:
                _bscMtdPython.PyMessage.traceResult(u'Move: {}'.format(i.decode(u'gbk')))
                cls._setOsFileMove_(i, targetDirectoryString)

        cls._setOsPathRemove(directoryString)

    @classmethod
    def open(cls, directoryString):
        cls._setOsDirectoryOpen(directoryString)


class MayaPath(bscCore.PathBasic):
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
        return cls._getNamespace(
            pathString,
            nodeSep=cls.separator_node,
            namespaceSep=cls.separator_namespace
        )

    @classmethod
    def name(cls, pathString):
        return cls._getName(
            pathString,
            nodeSep=cls.separator_node,
            namespaceSep=cls.separator_namespace
        )

    @classmethod
    def nameWithNamespace(cls, pathString):
        return cls._getNameWithNamespace(
            pathString,
            nodeSep=cls.separator_node
        )

    @classmethod
    def attributeName(cls, pathString):
        return cls._getAttributeName(
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
