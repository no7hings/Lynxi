# coding:utf-8
from LxMaterial import mtlAbstract, mtlConfigure


class Raw_Closure(mtlAbstract.Abc_Raw):
    def __init__(self, *args):
        self._initAbcRaw(*args)


class Raw_String(mtlAbstract.Abc_RawString):
    STR_mtlx_key_attribute = u'string'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_Name(mtlAbstract.Abc_RawString):
    STR_mtlx_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_Type(mtlAbstract.Abc_RawString):
    STR_mtlx_key_attribute = u'type'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_Version(mtlAbstract.Abc_RawString):
    STR_mtlx_key_attribute = u'version'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_ValueType(mtlAbstract.Abc_RawString):
    STR_mtlx_key_attribute = u'type'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_ShaderCategory(mtlAbstract.Abc_RawString):
    STR_mtlx_key_attribute = u'node'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_NodeCategory(mtlAbstract.Abc_RawString):
    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_NamespacePath(mtlAbstract.Abc_Path):
    CLS_raw = Raw_String

    STR_separator = mtlConfigure.Separator_String_Namespace

    def __init__(self, *args):
        self._initAbcPath(*args)


class Raw_Reference(mtlAbstract.Abc_Path):
    CLS_raw = Raw_String

    STR_separator = mtlConfigure.Separator_String_File

    STR_mtlx_key_attribute = u'href'

    def __init__(self, *args):
        self._initAbcPath(*args)


class ShadersetPath(mtlAbstract.Abc_ShadersetPath):
    CLS_raw = Raw_Name

    STR_separator = mtlConfigure.Separator_String_Node

    STR_mtlx_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcPath(*args)


class Raw_NodePath(mtlAbstract.Abc_Path):
    CLS_raw = Raw_Name

    STR_separator = mtlConfigure.Separator_String_Node

    STR_mtlx_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcPath(*args)


class Raw_GeometryPath(mtlAbstract.Abc_Path):
    CLS_raw = Raw_Name

    STR_separator = mtlConfigure.Separator_String_Node

    STR_mtlx_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcPath(*args)


class Raw_PortPath(mtlAbstract.Abc_Path):
    CLS_raw = Raw_Name

    STR_separator = mtlConfigure.Separator_String_Attribute

    STR_mtlx_key_attribute = u'name'

    def __init__(self, *args):
        self._initAbcPath(*args)
