# coding:utf-8
from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet, _mtlObjPort, _mtlObjObject, _mtlObjDefinition


class Reference(mtlObjCore.Abc_MtlFileReference):
    CLS_raw_file = _mtlObjRaw.Raw_Reference

    VAR_mtlx_key_element = u'xi:include'

    def __init__(self, *args):
        self._initAbcMtlFileReference(*args)


class Look(mtlObjCore.Abc_MtlLook):
    CLS_raw_name = _mtlObjRaw.Raw_Name
    CLS_set_assign = _mtlObjSet.Set_Assign

    CLS_set_assign_shaderset = _mtlObjSet.Set_Assign
    ClS_set_assign_propertyset = _mtlObjSet.Set_Assign
    CLS_set_assign_visibility = _mtlObjSet.Set_Visibility

    VAR_mtlx_key_element = u'look'
    VAR_mtlx_key_attribute = u'look'

    def __init__(self, *args):
        self._initAbcMtlLook(*args)


class Material(mtlObjCore.Abc_MtlMaterial):
    CLS_raw_dag_path = _mtlObjRaw.ShadersetPath

    CLS_set_input = _mtlObjSet.Set_Input

    CLS_input = _mtlObjPort.ShadersetInput

    CLS_def_object = _mtlObjDefinition.Def_Node

    DEF_cls_value = _mtlObjObject.DEF_CLS_VALUE

    VAR_mtlx_key_element = u'material'
    VAR_mtlx_key_attribute = u'material'

    def __init__(self, *args):
        """
        * 1.maya: shading engine name
        :param args: str(shader set name)
        """
        self._initAbcMtlMaterial(*args)


class GeometryPortset(mtlObjCore.Abc_MtlPropertyset):
    CLS_raw_name = _mtlObjRaw.Raw_Name

    CLS_set_port = _mtlObjSet.Set_Port
    
    VAR_mtlx_key_element = u'propertyset'
    VAR_mtlx_key_attribute = u'propertyset'

    def __init__(self, *args):
        """
        :param args: str(geometry path)
        """
        self._initAbcMtlPropertyset(*args)


class NodeGraph(mtlObjCore.Abc_MtlNodeGraph):
    CLS_raw_name = _mtlObjRaw.Raw_Name

    CLS_set_dag = _mtlObjSet.Set_Dag
    CLS_set_input = _mtlObjSet.Set_Input

    CLS_node = _mtlObjObject.Node
    CLS_output = _mtlObjPort.NodeGraphOutput

    VAR_mtlx_key_element = u'nodegraph'
    VAR_mtlx_key_attribute = u'nodegraph'

    def __init__(self, *args):
        self._initAbcMtlNodeGraph(*args)


class Collection(mtlObjCore.Abc_MtlGeometryCollection):
    CLS_raw_name = _mtlObjRaw.Raw_Name

    CLS_set_geometry = _mtlObjSet.Set_Geometry
    CLS_set_collection = _mtlObjSet.Set_Collection

    DEF_geometry_separator = u','

    VAR_mtlx_key_element = u'collection'
    VAR_mtlx_key_attribute = u'collection'

    def __init__(self, *args):
        self._initAbcMtlGeometryCollection(*args)
