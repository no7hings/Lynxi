# coding:utf-8
from LxMaBasic import maBscObjCore

from LxMaBasic.maBscObjects import _maBscObjRaw, _maBscObjUtility


class Node(maBscObjCore.Abc_MaDag):
    CLS_maya_string_node = _maBscObjRaw.NodeName
    CLS_maya_attribute = _maBscObjUtility.Attribute

    CLS_maya_set_attribute = _maBscObjRaw.ObjectSet

    def __init__(self, nodeString):
        self._initAbcMaDag(nodeString)


class NodeGraph(maBscObjCore.Abc_MaNodeGraph):
    CLS_maya_node = Node
    CLS_maya_connection = _maBscObjUtility.Connection

    def __init__(self, shaderObject):
        self._initAbcMaNodeGraph(shaderObject)


class Shader(maBscObjCore.Abc_MaShader):
    CLS_maya_string_node = _maBscObjRaw.NodeName
    CLS_maya_attribute = _maBscObjUtility.Attribute

    CLS_maya_set_attribute = _maBscObjRaw.ObjectSet

    CLS_maya_node_graph = NodeGraph

    def __init__(self, nodeString):
        self._initAbcMaShader(nodeString)


class Material(maBscObjCore.Abc_MaMaterial):
    CLS_maya_string_node = _maBscObjRaw.NodeName
    CLS_maya_attribute = _maBscObjUtility.Attribute

    CLS_maya_set_attribute = _maBscObjRaw.ObjectSet

    CLS_maya_shader = Shader

    def __init__(self, nodeString):
        self._initAbcMaMaterial(nodeString)


class Dag(maBscObjCore.Abc_MaDag):
    CLS_maya_string_node = _maBscObjRaw.NodeName
    CLS_maya_attribute = _maBscObjUtility.Attribute

    CLS_maya_set_attribute = _maBscObjRaw.ObjectSet

    def __init__(self, nodeString):
        self._initAbcMaDag(nodeString)


class Transform(maBscObjCore.Abc_MaTransform):
    CLS_maya_string_node = _maBscObjRaw.NodeName
    CLS_maya_attribute = _maBscObjUtility.Attribute

    CLS_maya_set_attribute = _maBscObjRaw.ObjectSet

    def __init__(self, nodeString):
        self._initAbcMaTransform(nodeString)


class Compose(maBscObjCore.Abc_MaCompose):
    CLS_maya_string_node = _maBscObjRaw.NodeName
    CLS_maya_attribute = _maBscObjUtility.Attribute

    CLS_maya_set_attribute = _maBscObjRaw.ObjectSet

    CLS_maya_transform = Transform
    CLS_maya_dag = Dag
    CLS_maya_node = Node

    def __init__(self, nodeString):
        self._initAbcMaCompose(nodeString)


class Geometry(maBscObjCore.Abc_MaGeometry):
    CLS_maya_string_node = _maBscObjRaw.NodeName
    CLS_maya_attribute = _maBscObjUtility.Attribute

    CLS_maya_set_attribute = _maBscObjRaw.ObjectSet

    CLS_maya_transform = Transform
    CLS_maya_dag = Dag
    CLS_maya_node = Node

    CLS_maya_material = Material

    def __init__(self, nodeString):
        self._initAbcMaGeometry(nodeString)


class Mesh(maBscObjCore.Abc_MaGeometry):
    CLS_maya_string_node = _maBscObjRaw.NodeName
    CLS_maya_attribute = _maBscObjUtility.Attribute

    CLS_maya_set_attribute = _maBscObjRaw.ObjectSet

    CLS_maya_transform = Transform
    CLS_maya_dag = Dag
    CLS_maya_node = Node

    CLS_maya_material = Material

    def __init__(self, nodeString):
        self._initAbcMaGeometry(nodeString)


class Group(maBscObjCore.Abc_MaGroup):
    CLS_maya_string_node = _maBscObjRaw.NodeName
    CLS_maya_attribute = _maBscObjUtility.Attribute

    CLS_maya_set_attribute = _maBscObjRaw.ObjectSet

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
