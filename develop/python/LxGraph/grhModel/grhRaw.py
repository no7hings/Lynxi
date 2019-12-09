# coding:utf-8
from LxGraph import grhAbstract, grhConfigure


class Name(grhAbstract.AbcName):
    def __init__(self, *args):
        self._initAbcName()

        self.create(*args)

    def create(self, *args):
        self.setRaw(args[0])


class Type(grhAbstract.AbcType):
    def __init__(self, *args):
        self._initAbcType()

        self.create(*args)

    def create(self, *args):
        self.setRaw(args[0])


class ValueType(grhAbstract.AbcType):
    def __init__(self, *args):
        self._initAbcType()

        self.create(*args)

    def create(self, *args):
        self.setRaw(args[0])


class Category(grhAbstract.AbcType):
    def __init__(self, *args):
        self._initAbcType()

        self.create(*args)

    def create(self, *args):
        self.setRaw(args[0])


class NamespacePath(grhAbstract.AbcPath):
    PathSeparator = ':'

    def __init__(self, *args):
        self._initAbcPath()


class FilePath(grhAbstract.AbcPath):
    PathSeparator = grhConfigure.Separator_String_File

    def __init__(self, *args):
        self._initAbcPath()


class NodePath(grhAbstract.AbcPath):
    PathSeparator = grhConfigure.Separator_String_Node

    def __init__(self, *args):
        self._initAbcPath()


class GeometryPath(grhAbstract.AbcPath):
    PathSeparator = grhConfigure.Separator_String_Node

    def __init__(self, *args):
        self._initAbcPath()


class AttributePath(grhAbstract.AbcPath):
    PathSeparator = grhConfigure.Separator_String_Attribute

    def __init__(self):
        self._initAbcPath()


class DagNodePath(grhAbstract.AbcDagPath):
    NODE_PATH_CLS = NodePath
    ATTRIBUTE_PATH_CLS = AttributePath

    def __init__(self, *args):
        self._initAbcDagPath()

        self.create(*args)

    def create(self, *args):
        pass


class DagAttributePath(grhAbstract.AbcDagPath):
    NODE_PATH_CLS = NodePath
    ATTRIBUTE_PATH_CLS = AttributePath

    def __init__(self, *args):
        self._initAbcDagPath()

        self.create(*args)

    def create(self, *args):
        pass


class DagGeometryPath(grhAbstract.AbcDagPath):
    NODE_PATH_CLS = NodePath
    ATTRIBUTE_PATH_CLS = AttributePath

    def __init__(self, *args):
        self._initAbcDagPath()

        self.create(*args)

    def create(self, *args):
        pass