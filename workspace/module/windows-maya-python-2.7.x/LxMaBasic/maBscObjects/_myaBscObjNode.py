# coding:utf-8
from LxData.datObjects import _datObjString

from LxGraphic import grhCfg

from LxGraphic.grhObjects import _grhObjSet

from ..import myaBscObjAbs

from ..maBscObjects import _myaBscObjQuery, _myaBscObjRaw, _myaBscObjPort


class Node(myaBscObjAbs.Abs_MyaNode):
    CLS_grh_type = _datObjString.Type
    CLS_grh_category = _datObjString.Category

    CLS_grh_nodepath = _myaBscObjRaw.Nodepath

    CLS_grh_port_set = _grhObjSet.PortSet
    VAR_grh_port_cls_dict = {
        grhCfg.Utility.DEF_grh_keyword_inparm: _myaBscObjPort.Port,
        grhCfg.Utility.DEF_grh_keyword_otparm: _myaBscObjPort.Port,
        grhCfg.Utility.DEF_grh_keyword_param: _myaBscObjPort.Port
    }

    CLS_grh_connector = _myaBscObjPort.Connector

    VAR_grh_param_assign_keyword_list = grhCfg.Utility.DEF_grh_param_assign_keyword_list
    VAR_grh_inparm_assign_keyword_list = grhCfg.Utility.DEF_grh_inparm_assign_keyword_list
    VAR_grh_otparm_assign_keyword_list = grhCfg.Utility.DEF_grh_otparm_assign_keyword_list

    VAR_grh_channel_assign_keyword_list = [
        grhCfg.Utility.DEF_grh_keyword_inparm_channel,
        grhCfg.Utility.DEF_grh_keyword_otparm_channel
    ]

    OBJ_grh_query_cache = _myaBscObjQuery.GRH_QUERY_CACHE
    OBJ_grh_obj_cache = _myaBscObjQuery.GRH_OBJ_CACHE

    def __init__(self, *args):
        self._initAbsMyaNode(*args)


class Geometry(myaBscObjAbs.Abc_MyaGeometry):
    CLS_grh_type = _datObjString.Type
    CLS_grh_category = _datObjString.Category

    CLS_grh_nodepath = _myaBscObjRaw.Nodepath

    CLS_grh_port_set = _grhObjSet.PortSet
    VAR_grh_port_cls_dict = {
        grhCfg.Utility.DEF_grh_keyword_inparm: _myaBscObjPort.Port,
        grhCfg.Utility.DEF_grh_keyword_otparm: _myaBscObjPort.Port,
        grhCfg.Utility.DEF_grh_keyword_param: _myaBscObjPort.Port
    }

    CLS_grh_connector = _myaBscObjPort.Connector

    VAR_grh_param_assign_keyword_list = grhCfg.Utility.DEF_grh_param_assign_keyword_list
    VAR_grh_inparm_assign_keyword_list = grhCfg.Utility.DEF_grh_inparm_assign_keyword_list
    VAR_grh_otparm_assign_keyword_list = grhCfg.Utility.DEF_grh_otparm_assign_keyword_list

    VAR_grh_channel_assign_keyword_list = [
        grhCfg.Utility.DEF_grh_keyword_inparm_channel,
        grhCfg.Utility.DEF_grh_keyword_otparm_channel
    ]

    CLS_mya_node = Node

    OBJ_grh_query_cache = _myaBscObjQuery.GRH_QUERY_CACHE
    OBJ_grh_obj_cache = _myaBscObjQuery.GRH_OBJ_CACHE

    def __init__(self, nodepathString):
        self._initAbcMyaGeometry(nodepathString)


class GeometryRoot(myaBscObjAbs.Abc_MyaGeometryGroup):
    CLS_grh_type = _datObjString.Type
    CLS_grh_category = _datObjString.Category

    CLS_grh_nodepath = _myaBscObjRaw.Nodepath

    CLS_grh_port_set = _grhObjSet.PortSet
    VAR_grh_port_cls_dict = {
        grhCfg.Utility.DEF_grh_keyword_inparm: _myaBscObjPort.Port,
        grhCfg.Utility.DEF_grh_keyword_otparm: _myaBscObjPort.Port,
        grhCfg.Utility.DEF_grh_keyword_param: _myaBscObjPort.Port
    }

    CLS_grh_connector = _myaBscObjPort.Connector

    VAR_grh_param_assign_keyword_list = grhCfg.Utility.DEF_grh_param_assign_keyword_list
    VAR_grh_inparm_assign_keyword_list = grhCfg.Utility.DEF_grh_inparm_assign_keyword_list
    VAR_grh_otparm_assign_keyword_list = grhCfg.Utility.DEF_grh_otparm_assign_keyword_list

    VAR_grh_channel_assign_keyword_list = [
        grhCfg.Utility.DEF_grh_keyword_inparm_channel,
        grhCfg.Utility.DEF_grh_keyword_otparm_channel
    ]

    OBJ_grh_query_cache = _myaBscObjQuery.GRH_QUERY_CACHE
    OBJ_grh_obj_cache = _myaBscObjQuery.GRH_OBJ_CACHE

    CLS_grh_geometry = Geometry

    def __init__(self, groupString):
        self._initAbcMyaGeometryGroup(groupString)
