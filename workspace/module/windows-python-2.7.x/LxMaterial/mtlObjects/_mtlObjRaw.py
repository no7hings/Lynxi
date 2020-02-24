# coding:utf-8
from LxMaterial import mtlObjCore, mtlConfigure


class Raw_Closure(mtlObjCore.Abc_MtlRaw):
    def __init__(self, *args):
        self._initAbcMtlRaw(*args)


class Raw_String(mtlObjCore.Abc_MtlRawString):
    VAR_mtlx_key_attribute = u'string'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_Name(mtlObjCore.Abc_MtlRawString):
    VAR_mtlx_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_Type(mtlObjCore.Abc_MtlRawString):
    VAR_mtlx_key_attribute = u'type'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_VisibilityType(mtlObjCore.Abc_MtlRawString):
    VAR_mtlx_key_attribute = u'vistype'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_Version(mtlObjCore.Abc_MtlRawString):
    VAR_mtlx_key_attribute = u'version'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_ValueType(mtlObjCore.Abc_MtlRawString):
    VAR_mtlx_key_attribute = u'type'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_ShaderCategory(mtlObjCore.Abc_MtlRawString):
    VAR_mtlx_key_attribute = u'node'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_NodeCategory(mtlObjCore.Abc_MtlRawString):
    VAR_mtlx_key_attribute = u'category'

    def __init__(self, *args):
        self._initAbcMtlRawString(*args)


class Raw_NamespacePath(mtlObjCore.Abc_MtlDagPath):
    CLS_raw = Raw_String

    DEF_separator = mtlConfigure.Separator_String_Namespace

    def __init__(self, *args):
        self._initAbcMtlDagPath(*args)


class Raw_Reference(mtlObjCore.Abc_MtlDagPath):
    CLS_raw = Raw_String

    DEF_separator = mtlConfigure.Utility.DEF_separator_file

    VAR_mtlx_key_attribute = u'href'

    def __init__(self, *args):
        self._initAbcMtlDagPath(*args)


class ShadersetPath(mtlObjCore.Abc_MtlMaterialPath):
    CLS_raw = Raw_Name

    DEF_separator = mtlConfigure.Utility.DEF_separator_node

    VAR_mtlx_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcMtlDagPath(*args)


class Raw_DagPath(mtlObjCore.Abc_MtlDagPath):
    CLS_raw = Raw_Name

    DEF_separator = mtlConfigure.Utility.DEF_separator_node

    VAR_mtlx_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcMtlDagPath(*args)


class Raw_GeometryPath(mtlObjCore.Abc_MtlDagPath):
    CLS_raw = Raw_Name

    DEF_separator = mtlConfigure.Utility.DEF_separator_node

    VAR_mtlx_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcMtlDagPath(*args)


class Raw_PortPath(mtlObjCore.Abc_MtlDagPath):
    CLS_raw = Raw_Name

    DEF_separator = mtlConfigure.Utility.DEF_separator_attribute

    VAR_mtlx_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcMtlDagPath(*args)
