# coding:utf-8
import os

import json

from LxCore import lxBasic


class _EnvironString(str):
    def __init__(self, value):
        self._value = value

        self._key = ''
        self._parent = None

    def _add(self, value):
        if self._value:
            lis = [i.lstrip().rstrip() for i in self._value.split(os.pathsep)]
            lowerLis = [i.lstrip().rstrip().lower() for i in self._value.lower().split(os.pathsep)]
            if value.lower() not in lowerLis:
                lis.append(value)
                self._value = os.pathsep.join(lis)
        else:
            self._value = value

    def _sub(self, value):
        if self._value:
            lis = [i.lstrip().rstrip() for i in self._value.split(os.pathsep)]
            lowerLis = [i.lstrip().rstrip().lower() for i in self._value.lower().split(os.pathsep)]
            if value.lower() in lowerLis:
                i = lowerLis.index(value.lower())
                lis.remove(lis[i])
                self._value = os.pathsep.join(lis)

    def _update(self):
        os.environ[self._key] = self._value

        str_ = _EnvironString(self._value)
        str_.key = self._key
        str_.parent = self._parent

        self.parent.__dict__[self._key] = str_
        return str_

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

        os.environ[self._key] = self._value

    def __iadd__(self, value):
        if isinstance(value, list) or isinstance(value, tuple):
            [self._add(i) for i in list(value)]
        else:
            self._add(value)

        return self._update()

    def __isub__(self, value):
        if isinstance(value, list) or isinstance(value, tuple):
            [self._sub(i) for i in list(value)]
        else:
            self._sub(value)

        return self._update()

    def append(self, value):
        self._add(value)

    def remove(self, value):
        self._sub(value)

    def __str__(self):
        return self._value.replace(os.pathsep, os.pathsep + '\r\n')


class Environ(object):
    def __getattr__(self, key):
        key = key.upper()

        value = os.environ.get(key, '')
        if not key in self.__dict__:
            str_ = _EnvironString(value)
            str_.key = key
            str_.parent = self

            self.__dict__[key] = str_
            return str_

    def __setattr__(self, key, value):
        key = key.upper()

        str_ = _EnvironString(value)
        str_.key = key
        str_.parent = self

        self.__dict__[key] = str_

    @staticmethod
    def exist(key, value):
        value_ = os.environ.get(key)
        if value_ is not None:
            lowerLis = [i.lstrip().rstrip().lower() for i in value_.split(os.pathsep)]
            return value.lower() in lowerLis
        return False


class _Abc_File(object):
    def _initAbcFile(self, fileString):
        self._fileString = fileString

    def exist(self):
        return self.isOsExist(self.fileString())

    def createDirectory(self):
        self.createOsDirectory(self.fileString())

    @classmethod
    def createOsDirectory(cls, fileString):
        osPath = os.path.dirname(fileString)
        if not cls.isOsExist(osPath):
            os.makedirs(osPath)

    @staticmethod
    def isOsExist(pathString):
        if pathString:
            return os.path.exists(pathString)
        return False

    def fileString(self):
        return self._fileString

    def read(self, *args):
        pass

    def write(self, *args):
        pass


class File(_Abc_File):
    def __init__(self, fileString):
        self._initAbcFile(fileString)

    def read(self, osFile, readLines=False):
        if self.exist():
            with open(self.fileString(), 'r') as f:
                if readLines is False:
                    data = f.read()
                else:
                    data = f.readlines()
                f.close()
                return data

    def write(self, raw):
        if raw is not None:
            self.createDirectory()
            with open(self.fileString(), 'wb') as f:
                if isinstance(raw, str) or isinstance(raw, unicode):
                    f.write(raw)
                elif isinstance(raw, tuple) or isinstance(raw, list):
                    f.writelines(raw)

                f.close()


class JsonFile(_Abc_File):
    def __init__(self, fileString):
        self._initAbcFile(fileString)

    def read(self, encoding=None):
        if self.exist():
            with open(self.fileString()) as j:
                data = json.load(j, encoding=encoding)
                return data

    def write(self, raw, ensure_ascii=True, indent=4):
        if raw is not None:
            tempFile = lxBasic.getOsTemporaryFile(self.fileString())

            with open(tempFile, 'w') as j:
                json.dump(raw, j, ensure_ascii=ensure_ascii, indent=indent)

            lxBasic.setOsFileCopy(tempFile, self.fileString())
