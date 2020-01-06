# coding:utf-8
from LxBasic import bscCore


class Abc_String(bscCore.Basic):
    pass


class Abc_System(bscCore.Basic):
    def _initAbcSys(self):
        pass


class Abc_Time(bscCore.Basic):
    def _initAbcTime(self, timestamp):
        self._timestamp = timestamp

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def timetag(self):
        return self._toTimetag(self._timestamp)

    @property
    def datetag(self):
        return self._toDatetag(self._timestamp)

    @property
    def prettify(self):
        return self._toPrettify(self._timestamp)


class Abc_Path(bscCore.Basic):
    @classmethod
    def _toTemporaryFileMethod(cls, fileString):
        datetag = Abc_Time()._getActiveDatetag()
        temporaryDirectory = 'D:/.lynxi.temporary/' + datetag
        temporaryFileString = cls._toFileString(temporaryDirectory, cls.os_path_method.basename(fileString))
        cls._setCreateDirectory(temporaryDirectory)
        return temporaryFileString

    @classmethod
    def _copyFileMethod(cls, sourceFileString, targetFileString, force=True):
        if cls.os_path_method.exists(sourceFileString):
            cls._setCreateFileDirectory(targetFileString)
            # Check Same File
            if not cls.os_path_method.normpath(sourceFileString) == cls.os_path_method.normpath(targetFileString):
                if force is True:
                    cls.copy_method.copy2(sourceFileString, targetFileString)
                elif force is False:
                    try:
                        cls.copy_method.copy2(sourceFileString, targetFileString)
                    except IOError:
                        print sourceFileString, targetFileString

    @staticmethod
    def _toPythonPath(pathString):
        return pathString.replace('\\', '/')

    @classmethod
    def _toFileString(cls, osPath, osFileBasename):
        return cls.os_path_method.join(osPath, osFileBasename).replace('\\', '/')


class Abc_File(Abc_Path):
    def _initAbcFile(self, fileString):
        assert isinstance(fileString, str) or isinstance(fileString, unicode), 'Argument: "fileString" must be "str" or "unicode"'
        self._fileString = self._toPythonPath(fileString)

    def createDirectory(self):
        self._setCreateDirectory(self.dirname())

    def temporary(self):
        return self._toTemporaryFileMethod(self._fileString)

    def isExist(self):
        return self.os_method.path.isfile(self._fileString)

    def dirname(self):
        return self.os_method.path.dirname(self._fileString)

    def basename(self):
        return self.os_method.path.basename(self._fileString)

    def name(self):
        return self.os_method.path.splitext(self.basename())[0]

    def ext(self):
        return self.os_method.path.splitext(self.basename())[1]

    def read(self, *args):
        pass

    def write(self, *args):
        pass

    def copyTo(self, targetFileString):
        pass

    def __str__(self):
        return self._fileString


class Abc_DccPath(bscCore.Basic):
    separator_namespace = None
    separator_node = None
    separator_attribute = None

    def _initAbcDccPath(self, pathString):
        self._pathString = pathString

    @classmethod
    def _getNamespace(cls, pathString, nodeSep, namespaceSep):
        if namespaceSep in pathString:
            return namespaceSep.join(pathString.split(nodeSep)[-1].split(namespaceSep)[:-1])
        return pathString

    @classmethod
    def _getName(cls, pathString, nodeSep, namespaceSep):
        return pathString.split(nodeSep)[-1].split(namespaceSep)[-1]

    @classmethod
    def _getAttributeName(cls, attrString, attributeSep):
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
        return self._getNamespace(self._pathString, self.separator_node, self.separator_namespace)

    @property
    def name(self):
        return self._getName(self._pathString, self.separator_node, self.separator_namespace)

    @property
    def attributeName(self):
        return self._getAttributeName(self._pathString, self.separator_attribute)
