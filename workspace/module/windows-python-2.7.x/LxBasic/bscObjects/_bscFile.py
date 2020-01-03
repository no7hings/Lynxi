# coding:utf-8
from LxBasic import bscAbstract


class Fle_Data(bscAbstract.Abc_File):
    def __init__(self, fileString):
        self.__init__(fileString)

    def read(self, readLines=False):
        if self.isExist():
            with open(self._fileString, 'r') as f:
                if readLines is False:
                    data = f.read()
                else:
                    data = f.readlines()

                f.close()
                return data

    def write(self, raw):
        if raw is not None:
            self.createDirectory()
            with open(self._fileString, 'wb') as f:
                if isinstance(raw, str) or isinstance(raw, unicode):
                    f.write(raw)
                elif isinstance(raw, tuple) or isinstance(raw, list):
                    f.writelines(raw)

                f.close()


class Fle_Json(bscAbstract.Abc_File):
    def __init__(self, fileString):
        self._initAbcFile(fileString)

    def read(self, encoding=None):
        if self.isExist():
            with open(self._fileString) as j:
                data = self.json_method.load(j, encoding=encoding)
                return data

    def write(self, raw, indent=4, ensure_ascii=True):
        if raw is not None:
            with open(self.temporary(), 'w') as j:
                self.json_method.dump(raw, j, indent=indent, ensure_ascii=ensure_ascii)

            self._copyFileMethod(self.temporary(), self._fileString)
