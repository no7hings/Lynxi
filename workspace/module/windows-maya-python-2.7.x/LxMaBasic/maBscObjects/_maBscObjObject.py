# coding:utf-8
from LxMaBasic import maBscObjCore

from LxMaBasic.maBscObjects import _maBscObjRaw, _maBscObjAttribute


class Node(maBscObjCore.Abc_MaNode):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_attribute = _maBscObjAttribute.Attribute

    CLS_mya_set_attribute = _maBscObjRaw.ObjectSet

    def __init__(self, nodeString):
        self._initAbcMaNode(nodeString)


class NodeGraph(maBscObjCore.Abc_MaNodeGraph):
    CLS_mya_node = Node
    CLS_mya_connection = _maBscObjAttribute.Connection

    def __init__(self, shaderObject):
        self._initAbcMaNodeGraph(shaderObject)


class Shader(maBscObjCore.Abc_MaShader):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_attribute = _maBscObjAttribute.Attribute

    CLS_mya_set_attribute = _maBscObjRaw.ObjectSet

    CLS_mya_node_graph = NodeGraph

    def __init__(self, nodeString):
        self._initAbcMaShader(nodeString)


class Material(maBscObjCore.Abc_MaMaterial):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_attribute = _maBscObjAttribute.Attribute

    CLS_mya_set_attribute = _maBscObjRaw.ObjectSet

    CLS_mya_shader = Shader

    def __init__(self, nodeString):
        self._initAbcMaMaterial(nodeString)


class Dag(maBscObjCore.Abc_MaDag):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_attribute = _maBscObjAttribute.Attribute

    CLS_mya_set_attribute = _maBscObjRaw.ObjectSet

    def __init__(self, nodeString):
        self._initAbcMaDag(nodeString)


class Transform(maBscObjCore.Abc_MaTransform):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_attribute = _maBscObjAttribute.Attribute

    CLS_mya_set_attribute = _maBscObjRaw.ObjectSet

    def __init__(self, nodeString):
        self._initAbcMaTransform(nodeString)


class Compose(maBscObjCore.Abc_MaCompoundDag):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_attribute = _maBscObjAttribute.Attribute

    CLS_mya_set_attribute = _maBscObjRaw.ObjectSet

    CLS_mya_transform = Transform
    CLS_mya_dag = Dag
    CLS_mya_node = Node

    def __init__(self, nodeString):
        self._initAbcMaCompoundDag(nodeString)


class Geometry(maBscObjCore.Abc_MaGeometry):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_attribute = _maBscObjAttribute.Attribute

    CLS_mya_set_attribute = _maBscObjRaw.ObjectSet

    CLS_mya_transform = Transform
    CLS_mya_dag = Dag
    CLS_mya_node = Node

    CLS_mya_material = Material

    def __init__(self, nodeString):
        self._initAbcMaGeometry(nodeString)


class Mesh(maBscObjCore.Abc_MaGeometry):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_attribute = _maBscObjAttribute.Attribute

    CLS_mya_set_attribute = _maBscObjRaw.ObjectSet

    CLS_mya_transform = Transform
    CLS_mya_dag = Dag
    CLS_mya_node = Node

    CLS_mya_material = Material

    def __init__(self, nodeString):
        self._initAbcMaGeometry(nodeString)


class Group(maBscObjCore.Abc_MaGroup):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_attribute = _maBscObjAttribute.Attribute

    CLS_mya_set_attribute = _maBscObjRaw.ObjectSet

    def __init__(self, nodeString):
        self._initAbcMaGroup(nodeString)


class NodeRoot(maBscObjCore.Abc_MaNodeRoot):
    CLS_group = Group
    CLS_node = Node

    def __init__(self, groupString):
        self._initAbcMaNodeRoot(groupString)


class GeometryRoot(maBscObjCore.Abc_MaGeometryRoot):
    CLS_group = Group
    CLS_node = Node

    CLS_geometry = Geometry

    def __init__(self, groupString):
        self._initAbcMaGeometryRoot(groupString)
