# coding:utf-8
from .. import datCfg, datObjAbs


class String(datObjAbs.Abs_DatRaw):
    CLS_dat__raw = unicode

    VAR_dat__raw__rawtype_pattern = unicode, str
    VAR_dat__raw__default = u''

    def __init__(self, *args):
        self._initAbsDatRaw(*args)


class Name(datObjAbs.Abs_DatName):
    def __init__(self, *args):
        self._initAbsDatName(*args)


class Typename(datObjAbs.Abs_DatTypename):
    def __init__(self, *args):
        self._initAbsDatTypename(*args)


class Datatype(datObjAbs.Abs_DatDatatype):
    CLS_dat__type__typename = Typename

    VAR_dat__type__category_dict = datCfg.DatUtility.DEF_dat__datatype__category_dict
    VAR_dat__type__role_dict = datCfg.DatUtility.DEF_dat__datatype__role_dict

    def __init__(self, *args):
        self._initAbsDatDatatype(*args)


class Porttype(datObjAbs.Abs_DatPorttype):
    CLS_dat__type__typename = Typename

    def __init__(self, *args):
        self._initAbsDatPorttype(*args)


class ObjVariant(datObjAbs.Abs_DatObjVariant):
    CLS_dat__obj_path__name = Name

    CLS_dat__obj_path__objsep = datCfg.DatUtility.DEF_dat__node_namespace_pathsep

    def __init__(self, *args):
        self._initAbsDatObjVariant(*args)


# object ************************************************************************************************************* #
class ObjNamespace(datObjAbs.Abs_DatObjNamespace):
    CLS_dat__obj_path__name = Name

    CLS_dat__obj_path__objsep = datCfg.DatUtility.DEF_dat__node_namespace_pathsep

    def __init__(self, *args):
        self._initAbsDatObjNamespace(*args)


class ObjTypename(datObjAbs.Abs_DatObjName):
    CLS_dat__obj_name__namespace = ObjNamespace
    CLS_dat__obj_name__name = Name

    def __init__(self, *args):
        self._initAbsDatObjName(*args)


class ObjName(datObjAbs.Abs_DatObjName):
    CLS_dat__obj_name__namespace = ObjNamespace
    CLS_dat__obj_name__name = Name

    def __init__(self, *args):
        self._initAbsDatObjName(*args)


# file *************************************************************************************************************** #
class Filename(datObjAbs.Abs_DatFilename):
    CLS_dat__filename__base = Name
    CLS_dat__filename__ext = Name

    VAR_dat__extsep = datCfg.DatUtility.DEF_dat__file_extsep

    def __init__(self, *args):
        self._initAbsDatFilename(*args)
