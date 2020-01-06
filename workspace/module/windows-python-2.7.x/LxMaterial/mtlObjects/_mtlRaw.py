# coding:utf-8
from LxMaterial import mtlAbstract, mtlConfigure


class Raw_Closure(mtlAbstract.Abc_Raw):
    def __init__(self, *args):
        self._initAbcRaw(*args)


class Raw_Name(mtlAbstract.Abc_Name):
    def __init__(self, *args):
        self._initAbcName(*args)


class Raw_Type(mtlAbstract.Abc_Type):
    def __init__(self, *args):
        self._initAbcType(*args)


class Raw_ValueType(mtlAbstract.Abc_Type):
    def __init__(self, *args):
        self._initAbcType()

        self.createByRaw(*args)

    def createByRaw(self, *args):
        self.setRaw(args[0])


class Raw_Category(mtlAbstract.Abc_Type):
    def __init__(self, *args):
        self._initAbcType()

        self.createByRaw(*args)

    def createByRaw(self, *args):
        self.setRaw(args[0])


class Raw_NamespacePath(mtlAbstract.Abc_Path):
    RAW_CLS = Raw_Name

    separator_path = ':'

    def __init__(self, *args):
        self._initAbcPath()


class FilePath(mtlAbstract.Abc_Path):
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


class GeometryPath(mtlAbstract.Abc_Path):
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

    def __init__(self, *args):
        self._initAbcDagpath(*args)

        self.createByRaw(*args)

    def createByRaw(self, *args):
        pass


class DagGeometryPath(mtlAbstract.Abc_Dagpath):
    RAW_PATH_NODE_CLS = Raw_Nodepath
    RAW_PATH_ATTRIBUTE_CLS = Raw_Attributepath

    def __init__(self, *args):
        self._initAbcDagpath(*args)

        self.createByRaw(*args)

    def createByRaw(self, *args):
        pass