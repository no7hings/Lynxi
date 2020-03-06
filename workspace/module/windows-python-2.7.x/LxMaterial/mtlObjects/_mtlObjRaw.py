# coding:utf-8
from LxMaterial import mtlObjCore, mtlConfigure


class Raw_Closure(mtlObjCore.Abc_MtlRaw):
    def __init__(self, *args):
        self._initAbcMtlRaw(*args)


class NameString(mtlObjCore.Abc_MtlRawString):
    VAR_mtl_file_element_key = u'string'
    VAR_mtl_file_attribute_key = u'name'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class TypeString(mtlObjCore.Abc_MtlRawString):
    VAR_mtl_file_element_key = u'string'
    VAR_mtl_file_attribute_key = u'type'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class VistypeString(mtlObjCore.Abc_MtlRawString):
    VAR_mtl_file_element_key = u'string'
    VAR_mtl_file_attribute_key = u'vistype'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class VersionString(mtlObjCore.Abc_MtlRawString):
    VAR_mtl_file_element_key = u'string'
    VAR_mtl_file_attribute_key = u'version'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class DatatypeString(mtlObjCore.Abc_MtlRawString):
    VAR_mtl_file_element_key = u'datatype'
    VAR_mtl_file_attribute_key = u'type'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class ShaderCategoryString(mtlObjCore.Abc_MtlRawString):
    VAR_mtl_file_element_key = u'string'
    VAR_mtl_file_attribute_key = u'node'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class NodeCategoryString(mtlObjCore.Abc_MtlRawString):
    VAR_mtl_file_element_key = u'string'
    VAR_mtl_file_attribute_key = u'category'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_NamespacePath(mtlObjCore.Abc_MtlDagpath):
    CLS_mtl_raw = NameString

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_namespace_separator

    def __init__(self, *args):
        self._initAbcMtlDagpath(*args)


class Raw_Reference(mtlObjCore.Abc_MtlDagpath):
    CLS_mtl_raw = NameString

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_file_separator

    VAR_mtl_file_attribute_key = u'href'

    def __init__(self, *args):
        self._initAbcMtlDagpath(*args)


class Raw_MaterialDagpath(mtlObjCore.Abc_MtlMaterialDagpath):
    CLS_mtl_raw = NameString

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_node_separator

    VAR_mtl_file_attribute_key = u'name'

    def __init__(self, *args):
        self._initAbcMtlDagpath(*args)


class Raw_NodeDagpath(mtlObjCore.Abc_MtlDagpath):
    CLS_mtl_raw = NameString

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_node_separator

    VAR_mtl_file_attribute_key = u'name'

    def __init__(self, *args):
        self._initAbcMtlDagpath(*args)


class Raw_GeometryDagpath(mtlObjCore.Abc_MtlDagpath):
    CLS_mtl_raw = NameString

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_node_separator

    VAR_mtl_file_attribute_key = u'name'

    def __init__(self, *args):
        self._initAbcMtlDagpath(*args)


class PortPath(mtlObjCore.Abc_MtlDagpath):
    CLS_mtl_raw = NameString

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_port_separator

    VAR_mtl_file_attribute_key = u'name'

    def __init__(self, *args):
        self._initAbcMtlDagpath(*args)
