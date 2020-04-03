# coding:utf-8
from .. import datCfg, datObjAbs


class Type(datObjAbs.Abs_DatRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    def __init__(self, *args):
        self._initAbsDatRaw(*args)


class Name(datObjAbs.Abs_DatRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    def __init__(self, *args):
        self._initAbsDatRaw(*args)


class Category(datObjAbs.Abs_DatRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    def __init__(self, *args):
        self._initAbsDatRaw(*args)


class Datatype(datObjAbs.Abs_DatRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    def __init__(self, *args):
        self._initAbsDatRaw(*args)


class Porttype(datObjAbs.Abs_DatRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    def __init__(self, *args):
        self._initAbsDatRaw(*args)


class Nodename(datObjAbs.Abs_DatNodename):
    CLS_dat_raw = unicode

    CLS_dat_namespace = Name
    CLS_dat_name = Name

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_namesep = datCfg.Utility.DEF_dat_node_namesep

    def __init__(self, *args):
        self._initAbsDatNodename(*args)


class Filename(datObjAbs.Abs_DatFilename):
    CLS_dat_raw = unicode

    CLS_dat_base = Name
    CLS_dat_ext = Name

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_extsep = datCfg.Utility.DEF_dat_file_extsep

    def __init__(self, *args):
        self._initAbsDatFilename(*args)
