# coding:utf-8
from . import bscObjDef, bscMtdCore


class Abc_BscSystem(object):
    platform_dic = {
        u'Windows': u'windows',
        u'Linux': u'linux'
    }

    application_dic = {
        u'maya.exe': u'maya',
        u'maya': u'maya'
    }

    @property
    def platform(self):
        return self.platform_dic.get(bscMtdCore.Mtd_BscUtility.MOD_platform.system())

    @property
    def application(self):
        return self.application_dic.get(
            bscMtdCore.Mtd_BscUtility._getOsFileBasename(bscMtdCore.Mtd_BscUtility.MOD_sys.argv[0])
        )

    @property
    def isWindows(self):
        return self.platform == u'windows'

    @property
    def isMaya(self):
        return self.application == u'maya'

    @property
    def userName(self):
        return bscMtdCore.Mtd_BscUtility._getSystemUsername()

    @property
    def hostName(self):
        return bscMtdCore.Mtd_BscUtility._getSystemHostname()

    @property
    def host(self):
        return bscMtdCore.Mtd_BscUtility._getSystemHost()


class Abc_BscTime(object):
    def _initAbcBscTime(self, timestamp):
        self._timestamp = timestamp

    def timestamp(self):
        return self._timestamp

    def timetag(self):
        return bscMtdCore.Mtd_BscUtility._timestamp2timetag(self._timestamp)

    def datetag(self):
        return bscMtdCore.Mtd_BscUtility._timestampToDatetag(self._timestamp)

    def prettify(self):
        return bscMtdCore.Mtd_BscUtility._timestampToPrettify(self._timestamp)


class Abc_BscPath(bscMtdCore.Mtd_BscUtility):
    pass


class Abc_BscFile(object):
    def _initAbcBscFile(self, fileString):
        assert isinstance(fileString, str) or isinstance(fileString, unicode), 'Argument: "fileString" must be "str" or "unicode"'
        self._fileString = bscMtdCore.Mtd_BscUtility._osPathToPythonStyle(fileString)

    def createDirectory(self):
        bscMtdCore.Mtd_BscUtility._setOsDirectoryCreate(self.dirname())

    def temporary(self):
        return bscMtdCore.Mtd_BscUtility._getOsFileTemporaryName(self._fileString)

    def isExist(self):
        return bscMtdCore.Mtd_BscUtility._isOsFileExist(self._fileString)

    def dirname(self):
        return bscMtdCore.Mtd_BscUtility._getOsFileDirname(self._fileString)

    def basename(self):
        return bscMtdCore.Mtd_BscUtility._getOsFileBasename(self._fileString)

    def name(self):
        return bscMtdCore.Mtd_BscUtility._getOsFileName(self._fileString)

    def ext(self):
        return bscMtdCore.Mtd_BscUtility._getOsFileExt(self._fileString)

    def read(self, *args):
        pass

    def write(self, *args):
        pass

    def copyTo(self, targetFileString):
        pass

    def __str__(self):
        return self._fileString


class Abc_BscDccNodeString(object):
    VAR_bsc_namespace_separator = None
    VAR_bsc_node_separator = None

    def _initAbcBscDccNodeString(self, nodepathString):
        self._nodeString = nodepathString

    def namespacesep(self):
        return self.VAR_bsc_namespace_separator

    def nodesep(self):
        return self.VAR_bsc_node_separator

    def namespace(self):
        return bscMtdCore.Mtd_BscPath._nodeString2namespace(
            self._nodeString,
            self.VAR_bsc_node_separator,
            self.VAR_bsc_namespace_separator
        )

    def nodepathString(self):
        return self._nodeString

    def name(self):
        return bscMtdCore.Mtd_BscPath._nodepathString2nodenameString(
            self._nodeString,
            self.VAR_bsc_node_separator,
            self.VAR_bsc_namespace_separator
        )

    def __str__(self):
        return self.nodepathString()


class Abc_BscDccPortString(object):
    VAR_bsc_port_separator = None

    def _initAbcBscDccPortString(self, portpathString):
        self._portString = portpathString

    def portsep(self):
        return self.VAR_bsc_port_separator

    def portpathString(self):
        return self._portString

    def portname(self):
        return bscMtdCore.Mtd_BscPath._portString2portname(
            self._portString,
            self.VAR_bsc_port_separator
        )

    def __str__(self):
        return self.portpathString()
