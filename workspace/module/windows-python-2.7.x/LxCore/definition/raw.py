# coding:utf-8
from LxCore import lxBasic

from LxCore.definition import abstract


class Raw_Version(abstract.Abc_Raw):
    def __init__(self, raw=None):
        self._initAbcRaw(
            raw,
            lxBasic.orderedDict(
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


class Raw_Environ(abstract.Abc_Raw):
    def __init__(self, raw=None):
        self._initAbcRaw(
            raw,
            {}
        )

    def _add(self, key, value, operate):
        if key in self._raw:
            value_ = self._raw[key][self.Key_Value]
            if isinstance(value_, list):
                if value not in value_:
                    value_.append(value)
            else:
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
                self._add(k, value, operate)

        return self


class Raw_Dependent(abstract.Abc_Raw):
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


class Raw_Configure(abstract.Abc_RawConfigure):
    VERSION_CLS = Raw_Version
    ENVIRON_CLS = Raw_Environ
    DEPENDENT_CLS = Raw_Dependent

    def __init__(self, enable, category, name, appObj):
        self._initRawConfig(enable, category, name, appObj)

    def _initRawConfig(self, enable, category, name, appObj):
        self._initAbcRawConfigure(enable, category, name)
        # Application
        self._systemObj = appObj
        self.addRaw(self.Key_System, self._systemObj)
        # Version
        self._versionObj = self.VERSION_CLS(
            {
                self.Key_Record: [self.Version_Default],
                self.Key_Active: self.Version_Default
            }
        )
        self.addRaw(self.Key_Version, self._versionObj)
        # Environ
        self._environObj = self.ENVIRON_CLS(
            {
                'PATH': {
                    self.Key_Value: '{self.sourcepath}',
                    self.Key_Operate: '+'
                }
            }
        )
        self.addRaw(self.Key_Environ, self._environObj)
        # Dependent
        self._dependentObj = self.DEPENDENT_CLS()
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
