# coding:utf-8
from .. import shmObjAbs


class RscVersionRaw(shmObjAbs.AbsShmRaw):
    def __init__(self, raw=None):
        self._initAbsShmRaw(
            raw,
            self.CLS_dic_order(
                [
                    (self.Key_Record, []),
                    (self.Key_Active, None)
                ]
            )
        )

    def addRecord(self, string):
        if not string in self.record:
            self.record.append(string)

    @property
    def record(self):
        return self.get(self.Key_Record) or []

    def setActive(self, string):
        self._raw[self.Key_Active] = string

    @property
    def active(self):
        return self.get(self.Key_Active)

    def _add(self, versionString):
        if versionString not in self.record:
            self.record.append(versionString)

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            pass
        elif isinstance(other, str) or isinstance(other, unicode):
            self._add(other)

        return self


class RscEnvironRaw(shmObjAbs.AbsShmRaw):
    def __init__(self, raw=None):
        self._initAbsShmRaw(
            raw,
            {}
        )

    def _add(self, key, value, operate):
        if key in self._raw:
            value_ = self._raw[key][self.Key_Value]
            value_lower = [i.lower() for i in value_]
            if isinstance(value_, list):
                if value.lower() not in value_lower:
                    value_.append(value)
                    value_.sort()
            else:
                if not value.lower() == value_.lower():
                    self._raw[key][self.Key_Value] = [value_, value]
        else:
            self._raw[key] = {
                self.Key_Value: value,
                self.Key_Operate: operate
            }

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            for k, v in other.raw().items():
                value = v[self.Key_Value]
                operate = v[self.Key_Operate]
                if isinstance(value, list):
                    [self._add(k, i, operate) for i in value]
                else:
                    self._add(k, value, operate)

        return self

    def toEnvironCommand(self):
        lis = []

        raw_ = self.raw()
        if raw_:
            for k, v in raw_.items():
                value = v[self.Key_Value]
                operate = v[self.Key_Operate]
                if operate == '+':
                    operate = '+='

                if isinstance(value, tuple) or isinstance(value, list):
                    value = [u'"{}"'.format(i) for i in value]
                    command = u'env.{} {} [{}]'.format(k, operate, ', '.join(value))
                else:
                    value = u'"{}"'.format(value)
                    command = u'env.{} {} {}'.format(k, operate, value)

                lis.append(command)

        return lis


class RscDependentRaw(shmObjAbs.AbsShmRaw):
    def __init__(self, raw=None):
        self._initAbsShmRaw(
            raw,
            {}
        )

    def _add(self, key, value):
        if not key in self._raw:
            self._raw[key] = value

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            for k, v in other.raw().items():
                self._add(k, v)

        return self


class RscResourceConfigure(shmObjAbs.AbsShmConfigure):
    CLS_shm__resource__version = RscVersionRaw
    CLS_shm__resource__environ = RscEnvironRaw
    CLS_shm__resource__dependent = RscDependentRaw

    def __init__(self, enable, category, name, systemObj):
        self._shm__rsc_raw__set_build_(enable, category, name, systemObj)

    def _shm__rsc_raw__set_build_(self, enable, category, name, systemObj):
        self._initAbsShmConfigure(enable, category, name)
        # Version
        self._versionObj = self.CLS_shm__resource__version(
            {
                self.Key_Record: [self.Version_Default],
                self.Key_Active: self.Version_Default
            }
        )
        self.addRaw(self.DEF_shm__key__version, self._versionObj)
        # System
        self._systemObj = systemObj
        self.addRaw(self.DEF_shm__key__system, self._systemObj)
        # Environ
        self._environObj = self.CLS_shm__resource__environ(
            {
                u'LYNXI_PYTHONPATH': {
                    self.Key_Value: u'{self.sourcepath}',
                    self.Key_Operate: u'+'
                }
            }
        )
        self.addRaw(self.Key_Environ, self._environObj)
        # Dependent
        self._dependentObj = self.CLS_shm__resource__dependent()
        self.addRaw(self.Key_Dependent, self._dependentObj)

    @property
    def system(self):
        return self._systemObj

    @property
    def version(self):
        return self._versionObj

    @property
    def environ(self):
        return self._environObj

    @property
    def dependent(self):
        return self._dependentObj
