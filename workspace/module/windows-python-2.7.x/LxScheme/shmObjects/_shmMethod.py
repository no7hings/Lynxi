# coding:utf-8
import sys

import os


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
        # copy list
        lis = [i.replace('\\', '/') for i in self._value.split(os.pathsep)]
        lis.sort()
        return '\r\n'.join(lis)


class Mtd_Environ(object):
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
    def isExist(key, value):
        value_ = os.environ.get(key)
        if value_ is not None:
            lowerLis = [i.lstrip().rstrip().lower() for i in value_.split(os.pathsep)]
            return value.lower() in lowerLis
        return False


class Mtd_SystemPath(object):
    def __init__(self):
        pass
    @staticmethod
    def isExist(pathString):
        pathLowerLis = [i.replace('\\', '/').lower() for i in sys.path]
        if pathString.lower() in pathLowerLis:
            return True
        return False

    @classmethod
    def add(cls, pathString):
        if cls.isExist(pathString) is False:
            sys.path.insert(0, pathString)

    @classmethod
    def remove(cls, pathString):
        if cls.isExist(pathString) is True:
            sys.path.remove(pathString)

    def __iadd__(self, other):
        if isinstance(other, tuple) or isinstance(other, list):
            [self.add(i) for i in other]
        elif isinstance(other, str) or isinstance(other, unicode):
            self.add(other)

        return self

    def __radd__(self, other):
        if isinstance(other, tuple) or isinstance(other, list):
            [self.remove(i) for i in other]
        elif isinstance(other, str) or isinstance(other, unicode):
            self.remove(other)

        return self

    def __str__(self):
        # copy list
        lis = [i.replace('\\', '/') for i in sys.path]
        lis.sort()
        return '\r\n'.join(lis)
