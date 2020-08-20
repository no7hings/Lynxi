# coding:utf-8
from LxData import datCfg

from LxData.datObjects import _datObjRaw

from .. import mtxObjAbs, mtxCfg


class Name(mtxObjAbs.AbsMtxName):
    VAR_dat__xml_obj__element_prefix_str = u'name'
    VAR_dat__xml_obj__attribute_attach_str = u'name'

    def __init__(self, *args):
        self._initAbsMtxName(*args)


class Porttype(mtxObjAbs.AbsMtxRaw):
    CLS_dat__raw = unicode

    VAR_dat__raw__rawtype_pattern = unicode, str
    VAR_dat__raw__default = u''

    VAR_dat__xml_obj__element_prefix_str = u'porttype'
    VAR_dat__xml_obj__attribute_attach_str = u'type'

    def __init__(self, *args):
        self._initAbsMtxRaw(*args)


class VistypeString(mtxObjAbs.AbsMtxRaw):
    CLS_dat__raw = unicode

    VAR_dat__raw__rawtype_pattern = unicode, str
    VAR_dat__raw__default = u''

    VAR_dat__xml_obj__element_prefix_str = u'vistype'
    VAR_dat__xml_obj__attribute_attach_str = u'vistype'

    def __init__(self, *args):
        self._initAbsMtxRaw(*args)


class Version(mtxObjAbs.AbsMtxRaw):
    CLS_dat__raw = unicode

    VAR_dat__raw__rawtype_pattern = unicode, str
    VAR_dat__raw__default = u''

    VAR_dat__xml_obj__element_prefix_str = u'version'
    VAR_dat__xml_obj__attribute_attach_str = u'version'

    def __init__(self, *args):
        self._initAbsMtxRaw(*args)


class Datatype(mtxObjAbs.AbsMtxDatatype):
    CLS_dat__type__typename = _datObjRaw.Typename

    VAR_dat__type__category_dict = datCfg.DatUtility.DEF_dat__datatype__category_dict
    VAR_dat__type__role_dict = datCfg.DatUtility.DEF_dat__datatype__role_dict

    VAR_dat__xml_obj__element_prefix_str = u'datatype'
    VAR_dat__xml_obj__attribute_attach_str = u'type'

    def __init__(self, *args):
        self._initAbsMtxDatatype(*args)


class ObjProxyNamespace(mtxObjAbs.AbsMtxObjProxyNamespace):
    CLS_dat__obj_path__name = Name

    CLS_dat__obj_path__objsep = datCfg.DatUtility.DEF_dat__node_namespace_pathsep

    VAR_dat__xml_obj__element_prefix_str = u'name'
    VAR_dat__xml_obj__attribute_attach_str = u'name'

    def __init__(self, *args):
        self._initAbsDatObjNamespace(*args)


class ObjTypename(mtxObjAbs.AbsMtxObjName):
    CLS_dat__obj_name__namespace = _datObjRaw.ObjNamespace
    CLS_dat__obj_name__name = Name

    VAR_dat__xml_obj__element_prefix_str = u'node'
    VAR_dat__xml_obj__attribute_attach_str = u'node'

    def __init__(self, *args):
        self._initAbsMtxObjName(*args)


class Typepath(mtxObjAbs.AbsMtxPath):
    CLS_dat__obj_path__name = ObjTypename

    CLS_dat__obj_path__objsep = mtxCfg.MtxUtility.DEF_mtx__node_pathsep

    VAR_dat__xml_obj__element_prefix_str = u'node'
    VAR_dat__xml_obj__attribute_attach_str = u'node'

    def __init__(self, *args):
        self._initAbsMtxPath(*args)


class ObjName(mtxObjAbs.AbsMtxObjName):
    CLS_dat__obj_name__namespace = _datObjRaw.ObjNamespace
    CLS_dat__obj_name__name = Name

    VAR_dat__xml_obj__element_prefix_str = u'name'
    VAR_dat__xml_obj__attribute_attach_str = u'name'

    def __init__(self, *args):
        self._initAbsMtxObjName(*args)


class Portpath(mtxObjAbs.AbsMtxPath):
    CLS_dat__obj_path__name = ObjName

    CLS_dat__obj_path__objsep = mtxCfg.MtxUtility.DEF_mtx__node_port_pathsep

    VAR_dat__xml_obj__element_prefix_str = u'portpath'
    VAR_dat__xml_obj__attribute_attach_str = u'name'

    def __init__(self, *args):
        self._initAbsMtxPath(*args)


class Nodepath(mtxObjAbs.AbsMtxPath):
    CLS_dat__obj_path__name = ObjName

    CLS_dat__obj_path__objsep = mtxCfg.MtxUtility.DEF_mtx__node_pathsep

    VAR_dat__xml_obj__element_prefix_str = u'name'
    VAR_dat__xml_obj__attribute_attach_str = u'name'

    def __init__(self, *args):
        self._initAbsMtxPath(*args)


class Attrpath(mtxObjAbs.AbsMtxAttrpath):
    CLS_dat__comppath__nodepath = Nodepath
    CLS_dat__comppath__portpath = Portpath

    VAR_dat__xml_obj__element_prefix_str = u'name'
    VAR_dat__xml_obj__attribute_attach_str = u'name'

    def __init__(self, *args):
        self._initAbsMtxAttrpath(*args)


class Filepath(mtxObjAbs.AbsMtxPath):
    CLS_dat__obj_path__name = _datObjRaw.Filename

    CLS_dat__obj_path__objsep = mtxCfg.MtxUtility.DEF_mtx__file_pathsep

    VAR_dat__xml_obj__element_prefix_str = u'filename'
    VAR_dat__xml_obj__attribute_attach_str = u'filepath'

    def __init__(self, *args):
        self._initAbsMtxPath(*args)


class RefFilepath(mtxObjAbs.AbsMtxPath):
    CLS_dat__obj_path__name = _datObjRaw.Filename

    CLS_dat__obj_path__objsep = mtxCfg.MtxUtility.DEF_mtx__file_pathsep

    VAR_dat__xml_obj__element_prefix_str = u'filename'
    VAR_dat__xml_obj__attribute_attach_str = u'href'

    def __init__(self, *args):
        self._initAbsMtxPath(*args)
