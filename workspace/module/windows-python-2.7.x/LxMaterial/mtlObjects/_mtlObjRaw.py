# coding:utf-8
from LxMaterial import mtlObjAbstract, mtlConfigure


class Raw_Closure(mtlObjAbstract.Abc_Raw):
    def __init__(self, *args):
        self._initAbcRaw(*args)


class Raw_String(mtlObjAbstract.Abc_RawString):
    STR_mtlx_key_attribute = u'string'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_Name(mtlObjAbstract.Abc_RawString):
    STR_mtlx_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_Type(mtlObjAbstract.Abc_RawString):
    STR_mtlx_key_attribute = u'type'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_VisibilityType(mtlObjAbstract.Abc_RawString):
    STR_mtlx_key_attribute = u'vistype'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_Version(mtlObjAbstract.Abc_RawString):
    STR_mtlx_key_attribute = u'version'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_ValueType(mtlObjAbstract.Abc_RawString):
    STR_mtlx_key_attribute = u'type'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_ShaderCategory(mtlObjAbstract.Abc_RawString):
    STR_mtlx_key_attribute = u'node'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_NodeCategory(mtlObjAbstract.Abc_RawString):
    STR_mtlx_key_attribute = u'category'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_NamespacePath(mtlObjAbstract.Abc_Path):
    CLS_raw = Raw_String

    STR_separator = mtlConfigure.Separator_String_Namespace

    def __init__(self, *args):
        self._initAbcPath(*args)


class Raw_Reference(mtlObjAbstract.Abc_Path):
    CLS_raw = Raw_String

    STR_separator = mtlConfigure.Separator_String_File

    STR_mtlx_key_attribute = u'href'

    def __init__(self, *args):
        self._initAbcPath(*args)


class ShadersetPath(mtlObjAbstract.Abc_ShadersetPath):
    CLS_raw = Raw_Name

    STR_separator = mtlConfigure.Separator_String_Node

    STR_mtlx_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcPath(*args)


class Raw_NodePath(mtlObjAbstract.Abc_Path):
    CLS_raw = Raw_Name

    STR_separator = mtlConfigure.Separator_String_Node

    STR_mtlx_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcPath(*args)


class Raw_GeometryPath(mtlObjAbstract.Abc_Path):
    CLS_raw = Raw_Name

    STR_separator = mtlConfigure.Separator_String_Node

    STR_mtlx_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcPath(*args)


class Raw_PortPath(mtlObjAbstract.Abc_Path):
    CLS_raw = Raw_Name

    STR_separator = mtlConfigure.Separator_String_Attribute

    STR_mtlx_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcPath(*args)
