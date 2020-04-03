# coding:utf-8
from LxData.datObjects import _datObjString

from .. import mtlObjAbs, mtlConfigure


class Name(mtlObjAbs.Abs_MtlRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_mtl_file_element_key = u'name'
    VAR_mtl_file_attribute_attach_key = u'name'

    def __init__(self, *args):
        self._initAbsMtlRaw(*args)


class Type(mtlObjAbs.Abs_MtlRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_mtl_file_element_key = u'string'
    VAR_mtl_file_attribute_attach_key = u'type'

    def __init__(self, *args):
        self._initAbsMtlRaw(*args)


class Porttype(mtlObjAbs.Abs_MtlRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_mtl_file_element_key = u'porttype'
    VAR_mtl_file_attribute_attach_key = u'type'

    def __init__(self, *args):
        self._initAbsMtlRaw(*args)


class VistypeString(mtlObjAbs.Abs_MtlRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_mtl_file_element_key = u'vistype'
    VAR_mtl_file_attribute_attach_key = u'vistype'

    def __init__(self, *args):
        self._initAbsMtlRaw(*args)


class Version(mtlObjAbs.Abs_MtlRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_mtl_file_element_key = u'version'
    VAR_mtl_file_attribute_attach_key = u'version'

    def __init__(self, *args):
        self._initAbsMtlRaw(*args)


class Datatype(mtlObjAbs.Abs_MtlRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_mtl_file_element_key = u'datatype'
    VAR_mtl_file_attribute_attach_key = u'type'

    def __init__(self, *args):
        self._initAbsMtlRaw(*args)


class Category(mtlObjAbs.Abs_MtlRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_mtl_file_element_key = u'category'
    VAR_mtl_file_attribute_attach_key = u'node'

    def __init__(self, *args):
        self._initAbsMtlRaw(*args)


class Nodename(mtlObjAbs.Abs_MtlNodename):
    CLS_dat_raw = unicode
    CLS_dat_namespace = Name
    CLS_dat_name = Name

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_namesep = mtlConfigure.Utility.DEF_mtl_nodename_namesep

    VAR_mtl_file_element_key = u'nodename'
    VAR_mtl_file_attribute_attach_key = u'name'

    def __init__(self, *args):
        self._initAbsMtlNodename(*args)


class Portpath(mtlObjAbs.Abs_MtlPath):
    CLS_dat_raw = unicode
    CLS_dat_dirname = Name
    CLS_dat_bscname = Name

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_pathsep = mtlConfigure.Utility.DEF_mtl_port_pathsep

    VAR_mtl_file_element_key = u'portpath'
    VAR_mtl_file_attribute_attach_key = u'name'

    def __init__(self, *args):
        self._initAbsMtlPath(*args)


class Nodepath(mtlObjAbs.Abs_MtlPath):
    CLS_dat_raw = unicode
    CLS_dat_dirname = Nodename
    CLS_dat_bscname = Nodename

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_pathsep = mtlConfigure.Utility.DEF_mtl_node_pathsep

    VAR_mtl_file_element_key = u'nodepath'
    VAR_mtl_file_attribute_attach_key = u'name'

    def __init__(self, *args):
        self._initAbsMtlPath(*args)


class Filepath(mtlObjAbs.Abs_MtlPath):
    CLS_dat_raw = unicode
    CLS_dat_dirname = _datObjString.Name
    CLS_dat_bscname = _datObjString.Filename

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_pathsep = mtlConfigure.Utility.DEF_mtl_file_pathsep

    VAR_mtl_file_element_key = u'filename'
    VAR_mtl_file_attribute_attach_key = u'filepath'

    def __init__(self, *args):
        self._initAbsMtlPath(*args)


class RefFilepath(mtlObjAbs.Abs_MtlPath):
    CLS_dat_raw = unicode
    CLS_dat_dirname = _datObjString.Name
    CLS_dat_bscname = _datObjString.Filename

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_pathsep = mtlConfigure.Utility.DEF_mtl_file_pathsep

    VAR_mtl_file_element_key = u'filename'
    VAR_mtl_file_attribute_attach_key = u'href'

    def __init__(self, *args):
        self._initAbsMtlPath(*args)
