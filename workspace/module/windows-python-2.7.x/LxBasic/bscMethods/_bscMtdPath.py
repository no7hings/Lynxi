# coding:utf-8
from LxBasic import bscMtdCore

from LxBasic.bscMethods import _bscMtdPython


class OsPath(bscMtdCore.Mtd_BscPath):
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
        return cls._getDagpathRemapDict(
            cls._toDagpathRemapList(pathStrings, cls.separator_path),
            cls.separator_path
        )

    @classmethod
    def isExist(cls, pathString):
        """
        :param pathString: str
        :return: bool
        """
        return cls.MTD_os_path.exists(pathString)


class OsDirectory(bscMtdCore.Mtd_BscUtility):
    @classmethod
    def allFileTimestampDict(cls, directoryString):
        u"""
        :return: Key = child file's "relative name", Value = child file's "timestamp".
        """
        dic = {}
        for i in cls._getPathnameListByOsDirectory(
                directoryString,
                extString=None,
                isFile=True,
                isFullpath=True,
                isAll=True
        ):
            relativeName = cls._osPathString2RelativeName(directoryString, i)
            timestamp = cls.MOD_os.stat(i).st_mtime
            dic[relativeName] = timestamp

        return dic

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


class AppPath(bscMtdCore.Mtd_BscPath):
    pass


class MaNodeString(bscMtdCore.Mtd_BscPath):
    VAR_bsc_namespace_separator = u':'
    VAR_bsc_node_separator = u'|'

    @classmethod
    def namespacesep(cls):
        return cls.VAR_bsc_namespace_separator

    @classmethod
    def nodesep(cls):
        return cls.VAR_bsc_node_separator

    @classmethod
    def namespace(cls, nodeString):
        return cls._nodeString2namespace(
            nodeString,
            nodesep=cls.VAR_bsc_node_separator,
            namespacesep=cls.VAR_bsc_namespace_separator
        )

    @classmethod
    def nodename(cls, nodeString):
        return cls._nodeString2nodename(
            nodeString,
            nodesep=cls.VAR_bsc_node_separator,
            namespacesep=cls.VAR_bsc_namespace_separator
        )

    @classmethod
    def nodenameWithNamespace(cls, nodeString):
        return cls._nodeString2nodenameWithNamespace(
            nodeString,
            nodesep=cls.VAR_bsc_node_separator
        )

    @classmethod
    def namespaceTreeViewBuildDic(cls, nodeString):
        return cls._getDagpathRemapDict(
            cls._toDagpathRemapList(nodeString, cls.VAR_bsc_namespace_separator),
            cls.VAR_bsc_namespace_separator
        )

    @classmethod
    def nodeTreeViewBuildDic(cls, nodeString):
        return cls._getDagpathRemapDict(
            cls._toDagpathRemapList(nodeString, cls.VAR_bsc_node_separator),
            cls.VAR_bsc_node_separator
        )

    @classmethod
    def covertToPathCreateDic(cls, dic):
        return cls._setDicConvertToPathCreateDic(dic, cls.VAR_bsc_node_separator)


class MaAttributeString(bscMtdCore.Mtd_BscPath):
    VAR_bsc_port_separator = u'.'

    @classmethod
    def portsep(cls):
        return cls.VAR_bsc_port_separator

    @classmethod
    def nodeString(cls, attributeString):
        return cls._portString2nodeString(
            attributeString,
            portsep=cls.VAR_bsc_port_separator
        )

    @classmethod
    def fullpathPortname(cls, attributeString):
        return cls._portString2fullpathPortname(
            attributeString,
            portsep=cls.VAR_bsc_port_separator
        )

    @classmethod
    def name(cls, attributeString):
        return cls._portString2portname(
            attributeString,
            portsep=cls.VAR_bsc_port_separator
        )

    @classmethod
    def composeBy(cls, nodeString, portString):
        return cls.VAR_bsc_port_separator.join([nodeString, portString])
