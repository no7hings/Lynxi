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

    STR_mtlx_key_element = u'look'
    STR_mtlx_key_attribute = u'look'

    def __init__(self, *args):
        self._initAbcLook(*args)


class Shaderset(mtlAbstract.Abc_Shaderset):
    CLS_raw_dagpath = _mtlObjRaw.ShadersetPath

    CLS_set_input = _mtlObjSet.Set_Port

    CLS_input = _mtlObjPort.ShadersetInput

    CLS_definition = _mtlObjDefinition.Def_Node

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
    CLS_set_input = _mtlObjSet.Set_Port

    CLS_node = _mtlObjDag.Node
    CLS_output = _mtlObjPort.NodeGraphOutput

    STR_mtlx_key_element = u'nodegraph'
    STR_mtlx_key_attribute = u'nodegraph'

    def __init__(self, *args):
        self._initAbcNodeGraph(*args)