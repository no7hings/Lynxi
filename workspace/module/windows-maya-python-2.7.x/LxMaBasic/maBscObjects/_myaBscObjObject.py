# coding:utf-8
from LxGraphic.grhObjects import _grhObjRaw

from LxMaBasic import myaBscObjCore

from LxMaBasic.maBscObjects import _myaBscObjCache, _myaBscObjRaw, _myaBscObjPort


class Node(myaBscObjCore.Abc_MyaNode):
    CLS_mya_node_string = _myaBscObjRaw.NodeName
    CLS_mya_port = _myaBscObjPort.Port

    CLS_mya_port_set = _myaBscObjRaw.PortSet

    OBJ_mya_query_cache = _myaBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodepathString):
        self._initAbcMyaNode(nodepathString)


class Dag(myaBscObjCore.Abc_MyaDag):
    CLS_mya_node_string = _myaBscObjRaw.NodeName
    CLS_mya_port = _myaBscObjPort.Port

    CLS_mya_port_set = _myaBscObjRaw.PortSet

    OBJ_mya_query_cache = _myaBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodepathString):
        self._initAbcMyaDag(nodepathString)


class Transform(myaBscObjCore.Abc_MyaTransform):
    CLS_mya_node_string = _myaBscObjRaw.NodeName
    CLS_mya_port = _myaBscObjPort.Port

    CLS_mya_port_set = _myaBscObjRaw.PortSet

    OBJ_mya_query_cache = _myaBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodepathString):
        self._initAbcMyaTransform(nodepathString)


class Compose(myaBscObjCore.Abc_MyaCompDag):
    CLS_mya_node_string = _myaBscObjRaw.NodeName
    CLS_mya_port = _myaBscObjPort.Port

    CLS_mya_port_set = _myaBscObjRaw.PortSet

    CLS_mya_transform = Transform
    CLS_mya_dag = Dag
    CLS_mya_node = Node

    OBJ_mya_query_cache = _myaBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodepathString):
        self._initAbcMyaCompDag(nodepathString)


class Geometry(myaBscObjCore.Abc_MyaGeometry):
    CLS_mya_node_string = _myaBscObjRaw.NodeName
    CLS_mya_port = _myaBscObjPort.Port

    CLS_mya_port_set = _myaBscObjRaw.PortSet

    CLS_mya_transform = Transform
    CLS_mya_dag = Dag
    CLS_mya_node = Node

    OBJ_mya_query_cache = _myaBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodepathString):
        self._initAbcMyaGeometry(nodepathString)


class Mesh(myaBscObjCore.Abc_MyaGeometry):
    CLS_mya_node_string = _myaBscObjRaw.NodeName
    CLS_mya_port = _myaBscObjPort.Port

    CLS_mya_port_set = _myaBscObjRaw.PortSet

    CLS_mya_transform = Transform
    CLS_mya_dag = Dag
    CLS_mya_node = Node

    OBJ_mya_query_cache = _myaBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodepathString):
        self._initAbcMyaGeometry(nodepathString)


class Group(myaBscObjCore.Abc_MyaGroup):
    CLS_mya_node_string = _myaBscObjRaw.NodeName
    CLS_mya_port = _myaBscObjPort.Port

    CLS_mya_port_set = _myaBscObjRaw.PortSet

    OBJ_mya_query_cache = _myaBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodepathString):
        self._initAbcMyaGroup(nodepathString)


class NodeRoot(myaBscObjCore.Abc_MyaNodeRoot):
    CLS_group = Group
    CLS_node = Node

    def __init__(self, groupString):
        self._initAbcMyaNodeRoot(groupString)


class GeometryRoot(myaBscObjCore.Abc_MyaGeometryRoot):
    CLS_group = Group
    CLS_node = Node

    CLS_geometry = Geometry

    def __init__(self, groupString):
        self._initAbcMyaGeometryRoot(groupString)


# ******************************************************************************************************************** #
class Node_(myaBscObjCore.Abs_MyaNode):
    CLS_grh_type = _grhObjRaw.Type
    CLS_grh_category = _grhObjRaw.Category

    CLS_grh_nodepath = _myaBscObjRaw.Nodepath

    CLS_grh_port_set = _myaBscObjRaw.PortSet
    CLS_grh_port = _myaBscObjPort.Port_

    OBJ_grh_query_cache = _myaBscObjCache.OBJ_mya_query_cache

    def __init__(self, *args):
        self._initAbsMyaNode(*args)
