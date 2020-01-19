# coding:utf-8
from LxMaterial import mtlAbstract

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet, _mtlObjPort, _mtlObjDag, _mtlObjDefinition


class Reference(mtlAbstract.Abc_Reference):
    CLS_raw_file = _mtlObjRaw.Raw_Reference

    STR_mtlx_key_element = u'xi:include'

    def __init__(self, *args):
        self._initAbcInclude(*args)


class Look(mtlAbstract.Abc_Look):
    CLS_raw_name = _mtlObjRaw.Raw_Name
    CLS_set_assign = _mtlObjSet.Set_Assign

    CLS_set_assign_shaderset = _mtlObjSet.Set_Assign
    ClS_set_assign_propertyset = _mtlObjSet.Set_Assign
    CLS_set_assign_visibility = _mtlObjSet.Set_Visibility

    STR_mtlx_key_element = u'look'
    STR_mtlx_key_attribute = u'look'

    def __init__(self, *args):
        self._initAbcLook(*args)


class Shaderset(mtlAbstract.Abc_Shaderset):
    CLS_raw_dagpath = _mtlObjRaw.ShadersetPath

    CLS_set_input = _mtlObjSet.Set_Input

    CLS_input = _mtlObjPort.ShadersetInput

    CLS_def_dag = _mtlObjDefinition.Def_Node

    DIC_cls_value = _mtlObjDag.DIC_CLS_VALUE

    STR_mtlx_key_element = u'material'
    STR_mtlx_key_attribute = u'material'

    def __init__(self, *args):
        """
        * 1.maya: shading engine name
        :param args: str(shader set name)
        """
        self._initAbcShaderset(*args)


class GeometryPortset(mtlAbstract.Abc_Propertyset):
    CLS_raw_name = _mtlObjRaw.Raw_Name

    CLS_set_port = _mtlObjSet.Set_Port
    
    STR_mtlx_key_element = u'propertyset'
    STR_mtlx_key_attribute = u'propertyset'

    def __init__(self, *args):
        """
        :param args: str(geometry path)
        """
        self._initAbcPropertyset(*args)


class NodeGraph(mtlAbstract.Abc_NodeGraph):
    CLS_raw_name = _mtlObjRaw.Raw_Name

    CLS_set_dag = _mtlObjSet.Set_Dag
    CLS_set_input = _mtlObjSet.Set_Input

    CLS_node = _mtlObjDag.Node
    CLS_output = _mtlObjPort.NodeGraphOutput

    STR_mtlx_key_element = u'nodegraph'
    STR_mtlx_key_attribute = u'nodegraph'

    def __init__(self, *args):
        self._initAbcNodeGraph(*args)


class Collection(mtlAbstract.Abc_GeometryCollection):
    CLS_raw_name = _mtlObjRaw.Raw_Name

    CLS_set_geometry = _mtlObjSet.Set_Geometry
    CLS_set_collection = _mtlObjSet.Set_Collection

    STR_geometry_separator = u','

    STR_mtlx_key_element = u'collection'
    STR_mtlx_key_attribute = u'collection'

    def __init__(self, *args):
        self._initAbcGeometryCollection(*args)
