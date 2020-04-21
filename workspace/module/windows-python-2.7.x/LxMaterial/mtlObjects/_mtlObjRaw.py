# coding:utf-8
from LxData.datObjects import _datObjString

from ..import mtlObjAbs, mtlCfg


class Name(mtlObjAbs.Abs_MtlRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_xml_file_element_tag = u'name'
    VAR_dat_xml_file_attribute_attach_tag = u'name'

    def __init__(self, *args):
        self._initAbsMtlRaw(*args)


class Type(mtlObjAbs.Abs_MtlRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_xml_file_element_tag = u'type'
    VAR_dat_xml_file_attribute_attach_tag = u'type'

    def __init__(self, *args):
        self._initAbsMtlRaw(*args)


class Porttype(mtlObjAbs.Abs_MtlRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_xml_file_element_tag = u'porttype'
    VAR_dat_xml_file_attribute_attach_tag = u'type'

    def __init__(self, *args):
        self._initAbsMtlRaw(*args)


class VistypeString(mtlObjAbs.Abs_MtlRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_xml_file_element_tag = u'vistype'
    VAR_dat_xml_file_attribute_attach_tag = u'vistype'

    def __init__(self, *args):
        self._initAbsMtlRaw(*args)


class Version(mtlObjAbs.Abs_MtlRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_xml_file_element_tag = u'version'
    VAR_dat_xml_file_attribute_attach_tag = u'version'

    def __init__(self, *args):
        self._initAbsMtlRaw(*args)


class Datatype(mtlObjAbs.Abs_MtlRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_xml_file_element_tag = u'datatype'
    VAR_dat_xml_file_attribute_attach_tag = u'type'

    def __init__(self, *args):
        self._initAbsMtlRaw(*args)


class Category(mtlObjAbs.Abs_MtlRaw):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_xml_file_element_tag = u'category'
    VAR_dat_xml_file_attribute_attach_tag = u'node'

    def __init__(self, *args):
        self._initAbsMtlRaw(*args)


class Portname(mtlObjAbs.Abs_MtlPortname):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    def __init__(self, *args):
        self._initAbsMtlPortname(*args)


class Nodename(mtlObjAbs.Abs_MtlNodename):
    CLS_dat_raw = unicode
    CLS_dat_namespace = Name

    CLS_dat_name = Name

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_namesep = mtlCfg.Utility.DEF_mtl_nodename_namesep

    VAR_dat_xml_file_element_tag = u'nodename'
    VAR_dat_xml_file_attribute_attach_tag = u'name'

    def __init__(self, *args):
        self._initAbsMtlNodename(*args)


class Portpath(mtlObjAbs.Abs_MtlPath):
    CLS_dat_name = Portname

    VAR_dat_pathsep = mtlCfg.Utility.DEF_mtl_port_pathsep

    VAR_dat_xml_file_element_tag = u'portpath'
    VAR_dat_xml_file_attribute_attach_tag = u'name'

    def __init__(self, *args):
        self._initAbsMtlPath(*args)


class Nodepath(mtlObjAbs.Abs_MtlPath):
    CLS_dat_name = Nodename

    VAR_dat_pathsep = mtlCfg.Utility.DEF_mtl_node_pathsep

    VAR_dat_xml_file_element_tag = u'nodepath'
    VAR_dat_xml_file_attribute_attach_tag = u'name'

    def __init__(self, *args):
        self._initAbsMtlPath(*args)


class Attrpath(mtlObjAbs.Abs_MtlAttrpath):
    CLS_dat_raw = unicode

    CLS_dat_nodepath = Nodepath
    CLS_dat_portpath = Portpath

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_xml_file_element_tag = u'portpath'
    VAR_dat_xml_file_attribute_attach_tag = u'name'

    def __init__(self, *args):
        self._initAbsMtlAttrpath(*args)


class Filepath(mtlObjAbs.Abs_MtlPath):
    CLS_dat_name = _datObjString.Filename

    VAR_dat_pathsep = mtlCfg.Utility.DEF_mtl_file_pathsep

    VAR_dat_xml_file_element_tag = u'filename'
    VAR_dat_xml_file_attribute_attach_tag = u'filepath'

    def __init__(self, *args):
        self._initAbsMtlPath(*args)


class RefFilepath(mtlObjAbs.Abs_MtlPath):
    CLS_dat_name = _datObjString.Filename

    VAR_dat_pathsep = mtlCfg.Utility.DEF_mtl_file_pathsep

    VAR_dat_xml_file_element_tag = u'filename'
    VAR_dat_xml_file_attribute_attach_tag = u'href'

    def __init__(self, *args):
        self._initAbsMtlPath(*args)
