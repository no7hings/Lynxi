# coding:utf-8
from ..import bscCfg, bscMtdCore

from LxBasic.bscMethods import _bscMtdPython, _bscMtdSystem


class OsPath(bscMtdCore.Mtd_BscPath):
    separator_path = bscCfg.BscUtility.DEF_bsc__pathsep
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

    @classmethod
    def cleanupTo(cls, pathString):
        pathsep = cls.DEF_bsc__pathsep
        _ = pathString.replace('\\', pathsep)
        if _bscMtdSystem.LinuxPlatform.isActive():
            return pathsep + pathsep.join([i for i in _.split(pathsep) if i])
        return pathsep.join([i for i in _.split(pathsep) if i])


class OsDirectory(bscMtdCore.Mtd_BscUtility):
    @classmethod
    def allFileTimestampDict(cls, directoryStr):
        u"""
        :return: Key = child file's "relative name", Value = child file's "timestamp".
        """
        dic = {}
        for i in cls._getPathnameListByOsDirectory(
                directoryStr,
                extString=None,
                isFile=True,
                isFullpath=True,
                isAll=True
        ):
            relativeName = cls._osPathString2RelativeName(directoryStr, i)
            timestamp = cls.MOD_os.stat(i).st_mtime
            dic[relativeName] = timestamp

        return dic

    @classmethod
    def create(cls, directoryStr, trace=False):
        result = cls._bsc_mtd__os_path__set_directory_create_(directoryStr)
        if trace is True:
            if result is True:
                _bscMtdPython.PyMessage.traceResult(
                    u'create directory: "{}".'.format(directoryStr)
                )
            else:
                _bscMtdPython.PyMessage.traceWarning(
                    u'exist directory: "{}".'.format(directoryStr)
                )

    @classmethod
    def allFullpathnames(cls, directoryStr):
        """
        :param directoryStr: str
        :return: list([str, ...])
        """
        return cls._getPathnameListByOsDirectory(
            directoryStr,
            extString=None,
            isFile=False,
            isFullpath=True,
            isAll=True
        )

    @classmethod
    def allFileFullpathnames(cls, directoryStr, extString=None):
        return cls._getPathnameListByOsDirectory(
            directoryStr,
            extString=extString,
            isFile=True,
            isFullpath=True,
            isAll=True
        )

    @classmethod
    def fullpathnames(cls, directoryStr):
        return cls._getPathnameListByOsDirectory(
            directoryStr,
            extString=None,
            isFile=False,
            isFullpath=True,
            isAll=False
        )

    @classmethod
    def basenames(cls, directoryStr):
        return cls._getPathnameListByOsDirectory(
            directoryStr,
            extString=None,
            isFile=False,
            isFullpath=False,
            isAll=False
        )

    @classmethod
    def fileFullpathnames(cls, directoryStr):
        return cls._getPathnameListByOsDirectory(
            directoryStr,
            extString=None,
            isFile=True,
            isFullpath=True,
            isAll=False
        )

    @classmethod
    def fileBasenames(cls, directoryStr):
        return cls._getPathnameListByOsDirectory(
            directoryStr,
            extString=None,
            isFile=True,
            isFullpath=False,
            isAll=False
        )

    @classmethod
    def isExist(cls, directoryStr):
        """
        :param directoryStr: str
        :return: bool
        """
        return cls.MTD_os_path.isdir(directoryStr)

    @classmethod
    def setDirectoryCreate(cls, directoryStr):
        """
        :param directoryStr: str
        :return: None
        """
        cls._bsc_mtd__os_path__set_directory_create_(directoryStr)

    @classmethod
    def allRelativenames(cls, directoryStr, extString=None):
        return cls._getPathnameListByOsDirectory(
            rootString=directoryStr,
            extString=extString,
            isFile=False,
            isFullpath=False,
            isAll=True
        )

    @classmethod
    def allFileRelativenames(cls, directoryStr, extString=None):
        return cls._getPathnameListByOsDirectory(
            rootString=directoryStr,
            extString=extString,
            isFile=True,
            isFullpath=False,
            isAll=True
        )

    @classmethod
    def relativenames(cls, directoryStr, extString=None):
        return cls._getPathnameListByOsDirectory(
            rootString=directoryStr,
            extString=extString,
            isFile=False,
            isFullpath=False,
            isAll=False
        )

    @classmethod
    def fileRelativenames(cls, directoryStr, extString=None):
        return cls._getPathnameListByOsDirectory(
            rootString=directoryStr,
            extString=extString,
            isFile=True,
            isFullpath=False,
            isAll=False
        )

    @classmethod
    def remove(cls, directoryStr):
        children = cls.allFullpathnames(directoryStr)
        if children:
            children.reverse()
            for i in children:
                _bscMtdPython.PyMessage.traceResult(u'Remove: {}'.format(i.decode(u'gbk')))
                cls._setOsPathRemove(i)

        cls._setOsPathRemove(directoryStr)

    @classmethod
    def moveTo(cls, directoryStr, targetDirectoryString):
        filenameLis = cls.allFileFullpathnames(directoryStr)
        if filenameLis:
            for i in filenameLis:
                _bscMtdPython.PyMessage.traceResult(u'Move: {}'.format(i.decode(u'gbk')))
                cls._setOsFileMove_(i, targetDirectoryString)

        cls._setOsPathRemove(directoryStr)

    @classmethod
    def open(cls, directoryStr):
        cls._setOsDirectoryOpen(directoryStr)


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
    def namespace(cls, nodepathString):
        return cls._nodeString2namespace(
            nodepathString,
            nodesep=cls.VAR_bsc_node_separator,
            namespacesep=cls.VAR_bsc_namespace_separator
        )

    @classmethod
    def nodename(cls, nodepathString):
        return cls._nodepathString2nodenameString(
            nodepathString,
            nodesep=cls.VAR_bsc_node_separator,
            namespacesep=cls.VAR_bsc_namespace_separator
        )

    @classmethod
    def nodenameWithNamespace(cls, nodepathString):
        return cls._nodeString2nodenameWithNamespace(
            nodepathString,
            nodesep=cls.VAR_bsc_node_separator
        )

    @classmethod
    def namespaceTreeViewBuildDic(cls, nodepathString):
        return cls._getDagpathRemapDict(
            cls._toDagpathRemapList(nodepathString, cls.VAR_bsc_namespace_separator),
            cls.VAR_bsc_namespace_separator
        )

    @classmethod
    def nodeTreeViewBuildDic(cls, nodepathString):
        return cls._getDagpathRemapDict(
            cls._toDagpathRemapList(nodepathString, cls.VAR_bsc_node_separator),
            cls.VAR_bsc_node_separator
        )

    @classmethod
    def covertToPathCreateDic(cls, dic):
        return cls._setDicConvertToPathCreateDic(dic, cls.VAR_bsc_node_separator)


class MaAttrpath(bscMtdCore.Mtd_BscPath):
    VAR_bsc_port_separator = u'.'

    @classmethod
    def portsep(cls):
        return cls.VAR_bsc_port_separator

    @classmethod
    def nodepathString(cls, attrpathString):
        return cls._portString2nodeString(
            attrpathString,
            portsep=cls.VAR_bsc_port_separator
        )

    @classmethod
    def portpathString(cls, attrpathString):
        return cls._attrpathString2portpathString(
            attrpathString,
            portsep=cls.VAR_bsc_port_separator
        )

    @classmethod
    def name(cls, attrpathString):
        return cls._portString2portname(
            attrpathString,
            portsep=cls.VAR_bsc_port_separator
        )

    @classmethod
    def composeBy(cls, nodepathString, portpathString):
        return cls.VAR_bsc_port_separator.join([nodepathString, portpathString])
