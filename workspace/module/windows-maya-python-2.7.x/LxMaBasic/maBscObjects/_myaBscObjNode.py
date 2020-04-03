# coding:utf-8
from LxData.datObjects import _datObjString

from LxGraphic import grhConfigure

from LxGraphic.grhObjects import _grhObjSet

from .. import myaBscObjCore

from ..maBscObjects import _myaBscObjQuery, _myaBscObjRaw, _myaBscObjPort


class Node(myaBscObjCore.Abs_MyaNode):
    CLS_grh_type = _datObjString.Type
    CLS_grh_category = _datObjString.Category

    CLS_grh_nodepath = _myaBscObjRaw.Nodepath

    CLS_grh_port_set = _grhObjSet.PortSet

    VAR_grh_port_cls_dict = {
        grhConfigure.Utility.DEF_grh_keyword_input: _myaBscObjPort.Port,
        grhConfigure.Utility.DEF_grh_keyword_output: _myaBscObjPort.Port,
        grhConfigure.Utility.DEF_grh_keyword_parameter: _myaBscObjPort.Port
    }
    VAR_grh_input_assign_list = [
        grhConfigure.Utility.DEF_grh_keyword_input
    ]
    VAR_grh_output_assign_list = [
        grhConfigure.Utility.DEF_grh_keyword_output
    ]
    VAR_grh_parameter_assign_list = [
        grhConfigure.Utility.DEF_grh_keyword_parameter
    ]

    OBJ_grh_query_cache = _myaBscObjQuery.OBJ_grh_query_cache
    OBJ_grh_obj_cache = _myaBscObjQuery.OBJ_grh_obj_cache

    def __init__(self, *args):
        self._initAbsMyaNode(*args)


class Geometry(myaBscObjCore.Abc_MyaGeometry):
    CLS_grh_type = _datObjString.Type
    CLS_grh_category = _datObjString.Category

    CLS_grh_nodepath = _myaBscObjRaw.Nodepath

    CLS_grh_port_set = _grhObjSet.PortSet

    VAR_grh_port_cls_dict = {
        grhConfigure.Utility.DEF_grh_keyword_input: _myaBscObjPort.Port,
        grhConfigure.Utility.DEF_grh_keyword_output: _myaBscObjPort.Port,
        grhConfigure.Utility.DEF_grh_keyword_parameter: _myaBscObjPort.Port
    }
    VAR_grh_input_assign_list = [
        grhConfigure.Utility.DEF_grh_keyword_input
    ]
    VAR_grh_output_assign_list = [
        grhConfigure.Utility.DEF_grh_keyword_output
    ]
    VAR_grh_parameter_assign_list = [
        grhConfigure.Utility.DEF_grh_keyword_parameter
    ]

    CLS_mya_node = Node

    OBJ_grh_query_cache = _myaBscObjQuery.OBJ_grh_query_cache
    OBJ_grh_obj_cache = _myaBscObjQuery.OBJ_grh_obj_cache

    def __init__(self, nodepathString):
        self._initAbcMyaGeometry(nodepathString)


class GeometryRoot(myaBscObjCore.Abc_MyaGeometryGroup):
    CLS_grh_type = _datObjString.Type
    CLS_grh_category = _datObjString.Category

    CLS_grh_nodepath = _myaBscObjRaw.Nodepath

    CLS_grh_port_set = _grhObjSet.PortSet

    VAR_grh_port_cls_dict = {
        grhConfigure.Utility.DEF_grh_keyword_input: _myaBscObjPort.Port,
        grhConfigure.Utility.DEF_grh_keyword_output: _myaBscObjPort.Port,
        grhConfigure.Utility.DEF_grh_keyword_parameter: _myaBscObjPort.Port
    }
    VAR_grh_input_assign_list = [
        grhConfigure.Utility.DEF_grh_keyword_input
    ]
    VAR_grh_output_assign_list = [
        grhConfigure.Utility.DEF_grh_keyword_output
    ]
    VAR_grh_parameter_assign_list = [
        grhConfigure.Utility.DEF_grh_keyword_parameter
    ]

    OBJ_grh_query_cache = _myaBscObjQuery.OBJ_grh_query_cache
    OBJ_grh_obj_cache = _myaBscObjQuery.OBJ_grh_obj_cache

    CLS_grh_geometry = Geometry

    def __init__(self, groupString):
        self._initAbcMyaGeometryGroup(groupString)
