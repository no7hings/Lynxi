# coding:utf-8
from .. import datCfg, datObjAbs


class String(datObjAbs.AbsDatRaw):
    CLS_dat__raw = unicode

    VAR_dat__raw__rawtype_pattern = unicode, str
    VAR_dat__raw__default = u''

    def __init__(self, *args):
        self._initAbsDatRaw(*args)


class Name(datObjAbs.AbsDatName):
    def __init__(self, *args):
        self._initAbsDatName(*args)


class Typename(datObjAbs.AbsDatTypename):
    def __init__(self, *args):
        self._initAbsDatTypename(*args)


class Datatype(datObjAbs.AbsDatDatatype):
    CLS_dat__type__typename = Typename

    VAR_dat__type__category_dict = datCfg.DatUtility.DEF_dat__datatype__category_dict
    VAR_dat__type__role_dict = datCfg.DatUtility.DEF_dat__datatype__role_dict

    def __init__(self, *args):
        self._initAbsDatDatatype(*args)


class Porttype(datObjAbs.AbsDatPorttype):
    CLS_dat__type__typename = Typename

    def __init__(self, *args):
        self._initAbsDatPorttype(*args)


class ObjVariant(datObjAbs.AbsDatObjVariant):
    CLS_dat__obj_path__name = Name

    CLS_dat__obj_path__objsep = datCfg.DatUtility.DEF_dat__node_namespace_pathsep

    def __init__(self, *args):
        self._initAbsDatObjVariant(*args)


# object ************************************************************************************************************* #
class ObjNamespace(datObjAbs.AbsDatObjNamespace):
    CLS_dat__obj_path__name = Name

    CLS_dat__obj_path__objsep = datCfg.DatUtility.DEF_dat__node_namespace_pathsep

    def __init__(self, *args):
        self._initAbsDatObjNamespace(*args)


class ObjTypename(datObjAbs.AbsDatObjName):
    CLS_dat__obj_name__namespace = ObjNamespace
    CLS_dat__obj_name__name = Name

    def __init__(self, *args):
        self._initAbsDatObjName(*args)


class ObjName(datObjAbs.AbsDatObjName):
    CLS_dat__obj_name__namespace = ObjNamespace
    CLS_dat__obj_name__name = Name

    def __init__(self, *args):
        self._initAbsDatObjName(*args)


# file *************************************************************************************************************** #
class Filename(datObjAbs.AbsDatFilename):
    CLS_dat__filename__base = Name
    CLS_dat__filename__ext = Name

    VAR_dat__extsep = datCfg.DatUtility.DEF_dat__file_extsep

    def __init__(self, *args):
        self._initAbsDatFilename(*args)
