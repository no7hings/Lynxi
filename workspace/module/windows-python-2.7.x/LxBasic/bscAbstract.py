# coding:utf-8
from LxBasic import bscCore


class Abc_System(object):
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
        return self.platform_dic.get(bscCore.UtilityBasic.MOD_platform.system())

    @property
    def application(self):
        return self.application_dic.get(
            bscCore.UtilityBasic._getOsFileBasename(bscCore.UtilityBasic.MOD_sys.argv[0])
        )

    @property
    def isWindows(self):
        return self.platform == u'windows'

    @property
    def isMaya(self):
        return self.application == u'maya'

    @property
    def userName(self):
        return bscCore.UtilityBasic._getSystemUsername()

    @property
    def hostName(self):
        return bscCore.UtilityBasic._getSystemHostname()

    @property
    def host(self):
        return bscCore.UtilityBasic._getSystemHost()


class Abc_Time(bscCore.UtilityBasic):
    def _initAbcTime(self, timestamp):
        self._timestamp = timestamp

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def timetag(self):
        return self._timestamp2timetag(self._timestamp)

    @property
    def datetag(self):
        return self._timestampToDatetag(self._timestamp)

    @property
    def prettify(self):
        return self._timestampToPrettify(self._timestamp)


class Abc_Path(bscCore.UtilityBasic):
    pass


class Abc_File(Abc_Path):
    def _initAbcFile(self, fileString):
        assert isinstance(fileString, str) or isinstance(fileString, unicode), 'Argument: "fileString" must be "str" or "unicode"'
        self._fileString = self._osPathToPythonStyle(fileString)

    def createDirectory(self):
        self._setOsDirectoryCreate(self.dirname())

    def temporary(self):
        return self._getOsFileTemporaryName(self._fileString)

    def isExist(self):
        return self.MOD_os.path.isfile(self._fileString)

    def dirname(self):
        return self.MOD_os.path.dirname(self._fileString)

    def basename(self):
        return self.MOD_os.path.basename(self._fileString)

    def name(self):
        return self.MOD_os.path.splitext(self.basename())[0]

    def ext(self):
        return self.MOD_os.path.splitext(self.basename())[1]

    def read(self, *args):
        pass

    def write(self, *args):
        pass

    def copyTo(self, targetFileString):
        pass

    def __str__(self):
        return self._fileString


class Abc_DccPath(bscCore.UtilityBasic):
    separator_namespace = None
    separator_node = None
    separator_attribute = None

    def _initAbcDccPath(self, pathString):
        self._pathString = pathString

    @classmethod
    def _getNamespaceByPathString(cls, pathString, nodeSep, namespaceSep):
        if namespaceSep in pathString:
            return namespaceSep.join(pathString.split(nodeSep)[-1].split(namespaceSep)[:-1])
        return pathString

    @classmethod
    def _getNameByPathString(cls, pathString, nodeSep, namespaceSep):
        return pathString.split(nodeSep)[-1].split(namespaceSep)[-1]

    @classmethod
    def _getAttributeNameByPathString(cls, attrString, attributeSep):
        return attributeSep.join(attrString.split(attributeSep)[1:])

    @property
    def namespaceSep(self):
        return self.separator_namespace

    @property
    def nodeSep(self):
        return self.separator_node

    @property
    def attributeSep(self):
        return self.separator_attribute

    @property
    def namespace(self):
        return self._getNamespaceByPathString(self._pathString, self.separator_node, self.separator_namespace)

    def fullpathName(self):
        return self._pathString

    @property
    def name(self):
        return self._getNameByPathString(self._pathString, self.separator_node, self.separator_namespace)

    @property
    def attributeName(self):
        return self._getAttributeNameByPathString(self._pathString, self.separator_attribute)
