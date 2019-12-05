# coding:utf-8
from LxGraph import grhAbstract

from LxGraph.grhModel import grhRaw, grhObjectSet


class Node(grhAbstract.AbcNode):
    DAG_PATH_CLS = grhRaw.DagNodePath
    CATEGORY_CLS = grhRaw.Category
    CHILD_SET_CLS = grhObjectSet.NodeSet
    ATTRIBUTE_SET_CLS = grhObjectSet.AttributeSet

    def __init__(self, *args):
        pass


class Shader(grhAbstract.AbcShader):
    DAG_PATH_CLS = grhRaw.DagNodePath
    CATEGORY_CLS = grhRaw.Category
    CHILD_SET_CLS = grhObjectSet.NodeSet
    ATTRIBUTE_SET_CLS = grhObjectSet.AttributeSet

    def __init__(self, *args):
        pass


class Geometry(grhAbstract.AbcGeometry):
    DAG_PATH_CLS = grhRaw.DagGeometryPath
    CATEGORY_CLS = grhRaw.Category
    CHILD_SET_CLS = grhObjectSet.NodeSet
    ATTRIBUTE_SET_CLS = grhObjectSet.AttributeSet

    def __init__(self, *args):
        pass
