# coding:utf-8
from LxMaterial import mtlAbstract, mtlConfigure


class Raw_Xml(mtlAbstract.Abc_RawXml):
    def __init__(self, *args):
        self._initAbcRawXml(*args)


class Raw_Closure(mtlAbstract.Abc_Raw):
    def __init__(self, *args):
        self._initAbcRaw(*args)


class Raw_Name(mtlAbstract.Abc_RawString):
    xml_key_attribute = 'name'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_Type(mtlAbstract.Abc_RawString):
    xml_key_attribute = 'type'

    def __init__(self, *args):
        self._initAbcRawString(*args)


class Raw_ValueType(mtlAbstract.Abc_RawString):
    xml_key_attribute = 'type'

    def __init__(self, *args):
        self._initAbcRawString()

        self.createByRaw(*args)

    def createByRaw(self, *args):
        self.setRaw(args[0])


class Raw_ShaderCategory(mtlAbstract.Abc_RawString):
    xml_key_attribute = 'node'

    def __init__(self, *args):
        self._initAbcRawString()

        self.createByRaw(*args)

    def createByRaw(self, *args):
        self.setRaw(args[0])


class Raw_NodeCategory(mtlAbstract.Abc_RawString):
    def __init__(self, *args):
        self._initAbcRawString()

        self.createByRaw(*args)

    def createByRaw(self, *args):
        self.setRaw(args[0])


class Raw_NamespacePath(mtlAbstract.Abc_Path):
    RAW_CLS = Raw_Name

    separator_path = ':'

    def __init__(self, *args):
        self._initAbcPath()


class Raw_PthFile(mtlAbstract.Abc_Path):
    RAW_CLS = Raw_Name

    separator_path = mtlConfigure.Separator_String_File

    def __init__(self, *args):
        self._initAbcPath()


class Raw_Nodepath(mtlAbstract.Abc_Path):
    RAW_CLS = Raw_Name

    separator_path = mtlConfigure.Separator_String_Node

    def __init__(self, *args):
        self._initAbcPath(*args)

    def toString(self):
        return str(self._raw)


class Raw_PthGeometry(mtlAbstract.Abc_Path):
    RAW_CLS = Raw_Name

    separator_path = mtlConfigure.Separator_String_Node

    def __init__(self, *args):
        self._initAbcPath(*args)


class Raw_Attributepath(mtlAbstract.Abc_Path):
    RAW_CLS = Raw_Name

    separator_path = mtlConfigure.Separator_String_Attribute

    def __init__(self, *args):
        self._initAbcPath(*args)

    def toString(self):
        return str(self._raw)


class Raw_Dagpath(mtlAbstract.Abc_Dagpath):
    RAW_PATH_NODE_CLS = Raw_Nodepath
    RAW_PATH_ATTRIBUTE_CLS = Raw_Attributepath

    xml_key_attribute = 'name'

    def __init__(self, *args):
        self._initAbcDagpath(*args)

        self.createByRaw(*args)

    def createByRaw(self, *args):
        pass


class Raw_Geometrypath(mtlAbstract.Abc_Dagpath):
    RAW_PATH_NODE_CLS = Raw_Nodepath
    RAW_PATH_ATTRIBUTE_CLS = Raw_Attributepath

    xml_key_attribute = 'geom'

    def __init__(self, *args):
        self._initAbcDagpath(*args)

        self.createByRaw(*args)

    def createByRaw(self, *args):
        pass
