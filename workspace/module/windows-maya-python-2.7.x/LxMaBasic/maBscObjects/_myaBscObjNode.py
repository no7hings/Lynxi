# coding:utf-8
from LxData.datObjects import _datObjRaw

from LxGraphic import grhCfg

from LxGraphic.grhObjects import _grhObjSet

from ..import myaBscObjAbs

from ..maBscObjects import _myaBscObjRaw, _myaBscObjQuery, _myaBscObjPort


class Node(myaBscObjAbs.Abs_MyaNode):
    CLS_grh_node_query = _myaBscObjQuery.NodeQuery

    CLS_grh_type = _datObjRaw.Type
    CLS_grh_category = _datObjRaw.Category

    CLS_grh_path = _myaBscObjRaw.Nodepath

    CLS_grh_port_set = _grhObjSet.PortSet
    VAR_grh_port_cls_dict = {
        grhCfg.Utility.DEF_grh_keyword_inparm: _myaBscObjPort.Parm,
        grhCfg.Utility.DEF_grh_keyword_otparm: _myaBscObjPort.Parm,
        grhCfg.Utility.DEF_grh_keyword_param: _myaBscObjPort.Parm
    }

    CLS_grh_connector = _myaBscObjPort.Connector

    VAR_grh_param_assign_keyword_list = grhCfg.Utility.DEF_grh_param_assign_keyword_list
    VAR_grh_inparm_assign_keyword_list = grhCfg.Utility.DEF_grh_inparm_assign_keyword_list
    VAR_grh_otparm_assign_keyword_list = grhCfg.Utility.DEF_grh_otparm_assign_keyword_list

    OBJ_grh_obj_cache = _myaBscObjQuery.GRH_OBJ_CACHE

    def __init__(self, *args):
        self._initAbsMyaNode(*args)


class Geometry(myaBscObjAbs.Abc_MyaGeometry):
    CLS_grh_node_query = _myaBscObjQuery.NodeQuery

    CLS_grh_type = _datObjRaw.Type
    CLS_grh_category = _datObjRaw.Category

    CLS_grh_path = _myaBscObjRaw.Nodepath

    CLS_grh_port_set = _grhObjSet.PortSet
    VAR_grh_port_cls_dict = {
        grhCfg.Utility.DEF_grh_keyword_inparm: _myaBscObjPort.Parm,
        grhCfg.Utility.DEF_grh_keyword_otparm: _myaBscObjPort.Parm,
        grhCfg.Utility.DEF_grh_keyword_param: _myaBscObjPort.Parm
    }

    CLS_grh_connector = _myaBscObjPort.Connector

    VAR_grh_param_assign_keyword_list = grhCfg.Utility.DEF_grh_param_assign_keyword_list
    VAR_grh_inparm_assign_keyword_list = grhCfg.Utility.DEF_grh_inparm_assign_keyword_list
    VAR_grh_otparm_assign_keyword_list = grhCfg.Utility.DEF_grh_otparm_assign_keyword_list

    CLS_mya_node = Node

    OBJ_grh_obj_cache = _myaBscObjQuery.GRH_OBJ_CACHE

    def __init__(self, nodepathString):
        self._initAbcMyaGeometry(nodepathString)


class GeometryRoot(myaBscObjAbs.Abc_MyaGeometryGroup):
    CLS_grh_node_query = _myaBscObjQuery.NodeQuery

    CLS_grh_type = _datObjRaw.Type
    CLS_grh_category = _datObjRaw.Category

    CLS_grh_path = _myaBscObjRaw.Nodepath

    CLS_grh_port_set = _grhObjSet.PortSet
    VAR_grh_port_cls_dict = {
        grhCfg.Utility.DEF_grh_keyword_inparm: _myaBscObjPort.Parm,
        grhCfg.Utility.DEF_grh_keyword_otparm: _myaBscObjPort.Parm,
        grhCfg.Utility.DEF_grh_keyword_param: _myaBscObjPort.Parm
    }

    CLS_grh_connector = _myaBscObjPort.Connector

    VAR_grh_param_assign_keyword_list = grhCfg.Utility.DEF_grh_param_assign_keyword_list
    VAR_grh_inparm_assign_keyword_list = grhCfg.Utility.DEF_grh_inparm_assign_keyword_list
    VAR_grh_otparm_assign_keyword_list = grhCfg.Utility.DEF_grh_otparm_assign_keyword_list

    OBJ_grh_obj_cache = _myaBscObjQuery.GRH_OBJ_CACHE

    CLS_grh_geometry = Geometry

    def __init__(self, groupString):
        self._initAbcMyaGeometryGroup(groupString)
