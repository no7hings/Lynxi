# coding:utf-8
from LxMaterial import mtlObjCore, mtlConfigure


class Raw_Closure(mtlObjCore.Abc_MtlRaw):
    def __init__(self, *args):
        self._initAbcMtlRaw(*args)


class Raw_string(mtlObjCore.Abc_MtlRawString):
    VAR_mtl_key_attribute = u'string'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_Name(mtlObjCore.Abc_MtlRawString):
    VAR_mtl_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_Type(mtlObjCore.Abc_MtlRawString):
    VAR_mtl_key_attribute = u'type'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_VisibilityType(mtlObjCore.Abc_MtlRawString):
    VAR_mtl_key_attribute = u'vistype'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_Version(mtlObjCore.Abc_MtlRawString):
    VAR_mtl_key_attribute = u'version'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_ValueType(mtlObjCore.Abc_MtlRawString):
    VAR_mtl_key_attribute = u'type'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_ShaderCategory(mtlObjCore.Abc_MtlRawString):
    VAR_mtl_key_attribute = u'node'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_NodeCategory(mtlObjCore.Abc_MtlRawString):
    VAR_mtl_key_attribute = u'category'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_NamespacePath(mtlObjCore.Abc_MtlDagPath):
    CLS_mtl_raw = Raw_string

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_namespace_separator

    def __init__(self, *args):
        self._initAbcMtlDagPath(*args)


class Raw_Reference(mtlObjCore.Abc_MtlDagPath):
    CLS_mtl_raw = Raw_string

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_file_separator

    VAR_mtl_key_attribute = u'href'

    def __init__(self, *args):
        self._initAbcMtlDagPath(*args)


class ShadersetPath(mtlObjCore.Abc_MtlMaterialPath):
    CLS_mtl_raw = Raw_Name

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_node_separator

    VAR_mtl_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcMtlDagPath(*args)


class Raw_DagPath(mtlObjCore.Abc_MtlDagPath):
    CLS_mtl_raw = Raw_Name

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_node_separator

    VAR_mtl_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcMtlDagPath(*args)


class Raw_GeometryPath(mtlObjCore.Abc_MtlDagPath):
    CLS_mtl_raw = Raw_Name

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_node_separator

    VAR_mtl_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcMtlDagPath(*args)


class Raw_PortPath(mtlObjCore.Abc_MtlDagPath):
    CLS_mtl_raw = Raw_Name

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_attribute_separator

    VAR_mtl_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcMtlDagPath(*args)
