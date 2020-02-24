# coding:utf-8
from LxScheme import shmObjCore


class Raw_Version(shmObjCore.Abc_ShmRaw):
    def __init__(self, raw=None):
        self._initAbcRaw(
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


class Raw_Custom(shmObjCore.Abc_ShmRaw):
    def __init__(self, raw=None):
        self._initAbcRaw(
            raw,
            self.CLS_dic_order(
                [
                    (self.Key_Record, []),
                    (self.Key_Active, None)
                ]
            )
        )

    def addRecord(self, string):
        if string not in self.record:
            self.record.append(string)

    @property
    def record(self):
        return self.get(self.Key_Record) or []

    def setActive(self, string):
        self._raw[self.Key_Active] = string

    @property
    def active(self):
        return self.get(self.Key_Active)


class Raw_Environ(shmObjCore.Abc_ShmRaw):
    def __init__(self, raw=None):
        self._initAbcRaw(
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


class Raw_Dependent(shmObjCore.Abc_ShmRaw):
    def __init__(self, raw=None):
        self._initAbcRaw(
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


class Raw_Variant(shmObjCore.Abc_ShmRaw):
    def __init__(self, raw=None):
        self._initAbcRaw(
            raw,
            {}
        )

    def set(self, key, value):
        self._raw[key] = value


class Raw_Resource(shmObjCore.Abc_ShmConfigure):
    RAW_VERSION_CLS = Raw_Version
    RAW_ENVIRON_CLS = Raw_Environ
    RAW_DEPENDENT_CLS = Raw_Dependent

    def __init__(self, enable, category, name, appObj):
        self._initRawConfig(enable, category, name, appObj)

    def _initRawConfig(self, enable, category, name, appObj):
        self._initAbcConfigure(enable, category, name)
        # Version
        self._versionObj = self.RAW_VERSION_CLS(
            {
                self.Key_Record: [self.Version_Default],
                self.Key_Active: self.Version_Default
            }
        )
        self.addRaw(self.Key_Version, self._versionObj)
        # System
        self._systemObj = appObj
        self.addRaw(self.Key_System, self._systemObj)
        # Environ
        self._environObj = self.RAW_ENVIRON_CLS(
            {
                'SYSTEM_PATH': {
                    self.Key_Value: '{self.sourcepath}',
                    self.Key_Operate: '+'
                }
            }
        )
        self.addRaw(self.Key_Environ, self._environObj)
        # Dependent
        self._dependentObj = self.RAW_DEPENDENT_CLS()
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


class Raw_Preset(shmObjCore.Abc_ShmConfigure):
    RAW_CUSTOM_CLS = Raw_Custom
    RAW_VARIANT_CLS = Raw_Variant

    def __init__(self, enable, category, name):
        self._initRawConfig(enable, category, name)

    def _initRawConfig(self, enable, category, name):
        pass
