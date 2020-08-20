# coding:utf-8
from . import bscCfg, bscMtdCore, bscObjItf


class AbsBscPort(bscObjItf.ItfBscPort):
    def _initAbsBscPort(self, *args, **kwargs):
        self._initItfBscPort(*args, **kwargs)


class AbsBscNode(bscObjItf.ItfBscNode):
    def _initAbsBscNode(self, *args, **kwargs):
        self._initItfBscNode(*args, **kwargs)


class AbsBscObjStack(bscObjItf.ItfBscObjStack):
    def _initAbsBscObjStack(self, *args):
        self._initItfBscObjStack(*args)


class AbsBscDagTree(bscObjItf.ItfBscDagTree):
    def _initAbsBscDagTree(self, *args):
        self._initItfBscDagTree(*args)


# ******************************************************************************************************************** #
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
        return self.platform_dic.get(
            bscCfg.BscUtility.MOD_platform.system()
        )

    @property
    def application(self):
        return self.application_dic.get(
            bscMtdCore.Mtd_BscUtility._getOsFileBasename(bscMtdCore.Mtd_BscUtility.MOD_sys.argv[0])
        )

    @property
    def isWindows(self):
        return self.platform == u'windows'

    @property
    def isLinux(self):
        return self.platform == u'linux'

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
        assert isinstance(fileString, (str, unicode)), 'Argument: "fileString" must be "str" or "unicode"'
        self._fileString = bscMtdCore.Mtd_BscUtility._osPathToPythonStyle(fileString)

    def createDirectory(self):
        bscMtdCore.Mtd_BscUtility._bsc_mtd__os_path__set_directory_create_(self.dirname())

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
