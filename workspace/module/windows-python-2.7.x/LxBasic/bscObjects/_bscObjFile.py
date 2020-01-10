# coding:utf-8
from LxBasic import bscAbstract


class File(bscAbstract.Abc_File):
    def __init__(self, fileString):
        self._initAbcFile(fileString)

    def read(self, readLines=False):
        if self.isExist():
            with open(self._fileString, u'r') as f:
                if readLines is False:
                    data = f.read()
                else:
                    data = f.readlines()

                f.close()
                return data

    def write(self, raw):
        if raw is not None:
            self.createDirectory()
            with open(self._fileString, u'w') as f:
                if isinstance(raw, str) or isinstance(raw, unicode):
                    f.write(raw)
                elif isinstance(raw, tuple) or isinstance(raw, list):
                    f.writelines(raw)

                f.close()


class JsonFile(bscAbstract.Abc_File):
    def __init__(self, fileString):
        self._initAbcFile(fileString)

    def read(self, encoding=None):
        if self.isExist():
            with open(self._fileString) as j:
                data = self.method_json.load(j, encoding=encoding)
                return data

    def write(self, raw, indent=4, ensure_ascii=True):
        if raw is not None:
            with open(self.temporary(), u'w') as j:
                self.method_json.dump(raw, j, indent=indent, ensure_ascii=ensure_ascii)

            self._setOsFileCopy(self.temporary(), self._fileString)
