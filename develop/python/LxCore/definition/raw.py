# coding:utf-8
from LxCore import lxBasic, lxConfigure

from LxCore.definition import abstract


class Raw_Object(abstract._AbcRaw):
    def __init__(self, raw=None):
        self._initRawObject(raw)

    def _initRawObject(self, raw):
        self._initAbcRaw()
        if raw is not None:
            self.create(raw)
        else:
            self.create(
                {
                    self.Key_Enable: True,
                    self.Key_Category: 'unspecific',
                    self.Key_Name: 'unspecific'
                }
            )

    def setEnable(self, boolean):
        self._raw[self.Key_Enable] = boolean

    def enable(self):
        return self._getValue(self.Key_Enable)

    def setName(self, string):
        self._raw[self.Key_Name] = string

    def name(self):
        return self._getValue(self.Key_Name)

    def setCategory(self, string):
        self._raw[self.Key_Category] = string

    def category(self):
        return self._getValue(self.Key_Category)


class Raw_Version(abstract._AbcRaw):
    def __init__(self, raw=None):
        self._initRawVersion(raw)

    def _initRawVersion(self, raw):
        self._initAbcRaw()

        if raw is not None:
            self.create(raw)
        else:
            self.create({})

    def addRecord(self, string):
        if not string in self.record():
            self.record().append(string)

    def record(self):
        return self._getValue(self.Key_Record)

    def setActive(self, string):
        self._raw[self.Key_Active] = string

    def active(self):
        return self._getValue(self.Key_Active)


class Raw_Environ(abstract._AbcRaw):
    def __init__(self, raw=None):
        self._initRawEnviron(raw)

    def _initRawEnviron(self, raw):
        self._initAbcRaw()

        if raw is not None:
            self.create(raw)
        else:
            self.create({})

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            for k, v in other._raw.items():
                value = v[self.Key_Value]
                operate = v[self.Key_Operate]
                self._add(k, value, operate)

        return self

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


class Raw_Dependent(abstract._AbcRaw):
    def __init__(self, raw=None):
        self._initRawDependent(raw)

    def _initRawDependent(self, raw):
        self._initAbcRaw()

        if raw is not None:
            self.create(raw)
        else:
            self.create({})


class Raw_ResourceConfig(lxConfigure.Basic):
    RAW_OBJECT_CLS = Raw_Object
    RAW_ENVIRON_CLS = Raw_Environ
    RAW_DEPENDENT_CLS = Raw_Dependent
    RAW_VERSION_CLS = Raw_Version

    def __init__(self, category, name, appObj):

        self._initRawResourceConfig(category, name, appObj)

    def _initRawResourceConfig(self, category, name, appObj):
        self._platform = appObj

        self._objectRaw = self.RAW_OBJECT_CLS(
            {
                self.Key_Enable: True,
                self.Key_Category: category,
                self.Key_Name: name
            }
        )
        self._versionRaw = self.RAW_VERSION_CLS(
            {
                self.Key_Record: [self.Version_Default],
                self.Key_Active: self.Version_Default
            }
        )
        self._environRaw = self.RAW_ENVIRON_CLS(
            {
                'PATH': {
                    self.Key_Value: '{sourcepath}',
                    self.Key_Operate: '+'
                }
            }
        )

        self._dependentRaw = self.RAW_DEPENDENT_CLS()

    def setEnable(self, boolean):
        self._objectRaw.setEnable(boolean)

    def enable(self):
        return self._objectRaw.enable()

    def setCategory(self, string):
        self._objectRaw.setCategory(string)

    def category(self):
        return self._objectRaw.category()

    def setName(self, string):
        self._objectRaw.setName(string)

    def name(self):
        return self._objectRaw.name()

    def platform(self):
        return self._platform

    def version(self):
        return self._versionRaw

    def environ(self):
        return self._environRaw

    def dependent(self):
        return self._dependentRaw

    def raw(self):
        return lxBasic.orderedDict(
            (
                (self.Key_Enable, self.enable()),
                (self.Key_Category, self.category()),
                (self.Key_Name, self.name()),
                (self.Key_Application, self.platform().raw()),
                (self.Key_Environ, self.environ().raw()),
                (self.Key_Dependent, self.dependent().raw()),
                (self.Key_Version, self.version().raw())
            )
        )
