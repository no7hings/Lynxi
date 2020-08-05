# coding:utf-8
from LxGraphic import grhCfg

from LxGraphic.grhObjects import _grhObjSet

from ..import mtlObjAbs

from ..mtlObjects import _mtlObjRaw, _mtlObjPort, _mtlObjQuery


class Node(mtlObjAbs.Abs_MtlNode):
    CLS_grh_node_query = _mtlObjQuery.NodeQuery

    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_category = _mtlObjRaw.Category
    CLS_grh_path = _mtlObjRaw.Nodepath

    CLS_grh_port_set = _grhObjSet.PortSet
    VAR_grh_port_cls_dict = {
        grhCfg.Utility.DEF_grh_keyword_param: _mtlObjPort.Param,

        grhCfg.Utility.DEF_grh_keyword_inparm: _mtlObjPort.Inparm,
        grhCfg.Utility.DEF_grh_keyword_inparm_channel: _mtlObjPort.InparmChannel,

        grhCfg.Utility.DEF_grh_keyword_otparm: _mtlObjPort.Otparm,
        grhCfg.Utility.DEF_grh_keyword_otparm_channel: _mtlObjPort.OtparmChannel,

        grhCfg.Utility.DEF_grh_keyword_property: _mtlObjPort.Param,
        grhCfg.Utility.DEF_grh_keyword_visibility: _mtlObjPort.Param
    }

    CLS_grh_connector = _mtlObjPort.Connector

    VAR_grh_param_assign_keyword_list = grhCfg.Utility.DEF_grh_param_assign_keyword_list
    VAR_grh_inparm_assign_keyword_list = grhCfg.Utility.DEF_grh_inparm_assign_keyword_list
    VAR_grh_otparm_assign_keyword_list = grhCfg.Utility.DEF_grh_otparm_assign_keyword_list

    OBJ_grh_obj_cache = _mtlObjQuery.GRH_OBJ_CACHE

    # xml ************************************************************************************************************ #
    VAR_dat_xml_file_attribute_attach_tag = u'nodename'

    def __init__(self, *args):
        self._initAbsMtlNode(*args)


class NodeGraph(mtlObjAbs.Abc_MtlNodeGraph):
    CLS_grh_name = _mtlObjRaw.Name

    CLS_grh_node_set = _grhObjSet.NodeSet

    CLS_grh_node_graph_output_set = _grhObjSet.PortProxySet
    CLS_grh_node_graph_output = _mtlObjPort.NodeGraphOutput

    VAR_dat_xml_file_element_tag = u'nodegraph'
    VAR_dat_xml_file_attribute_attach_tag = u'nodegraph'

    def __init__(self, *args):
        self._initAbcMtlNodeGraph(*args)


class ShaderProxy(mtlObjAbs.Abc_MtlShaderProxy):
    CLS_grh_name = _mtlObjRaw.Name
    CLS_grh_node = Node

    CLS_grh_node_graph_set = _grhObjSet.ObjSet
    CLS_grh_node_graph = NodeGraph

    CLS_grh_port_proxy_set = _grhObjSet.PortProxySet
    VAR_grh_port_proxy_cls_dict = {
        grhCfg.Utility.DEF_grh_keyword_param: _mtlObjPort.BindParm,

        grhCfg.Utility.DEF_grh_keyword_inparm: _mtlObjPort.BindInparm,
        grhCfg.Utility.DEF_grh_keyword_inparm_channel: _mtlObjPort.BindInparm,

        grhCfg.Utility.DEF_grh_keyword_otparm: _mtlObjPort.BindOtparm,
        grhCfg.Utility.DEF_grh_keyword_otparm_channel: _mtlObjPort.BindOtparm,

        grhCfg.Utility.DEF_grh_keyword_property: _mtlObjPort.Property,
        grhCfg.Utility.DEF_grh_keyword_visibility: _mtlObjPort.Visibility
    }

    VAR_dat_xml_file_element_tag = u'shaderref'

    def __init__(self, *args):
        self._initAbcMtlShaderProxy(*args)


class MaterialProxy(mtlObjAbs.Abc_MtlMaterialProxy):
    CLS_grh_name = _mtlObjRaw.Name
    CLS_grh_node = Node

    CLS_grh_node_graph_set = _grhObjSet.ObjSet
    CLS_grh_node_graph = NodeGraph

    CLS_grh_port_proxy_set = _grhObjSet.PortProxySet
    VAR_grh_port_proxy_cls_dict = {
        grhCfg.Utility.DEF_grh_keyword_param: _mtlObjPort.BindParm,

        grhCfg.Utility.DEF_grh_keyword_inparm: _mtlObjPort.BindInparm,
        grhCfg.Utility.DEF_grh_keyword_inparm_channel: _mtlObjPort.BindInparm,

        grhCfg.Utility.DEF_grh_keyword_otparm: _mtlObjPort.BindOtparm,
        grhCfg.Utility.DEF_grh_keyword_otparm_channel: _mtlObjPort.BindOtparm,

        grhCfg.Utility.DEF_grh_keyword_property: _mtlObjPort.Property,
        grhCfg.Utility.DEF_grh_keyword_visibility: _mtlObjPort.Visibility
    }

    VAR_dat_xml_file_element_tag = u'material'
    VAR_dat_xml_file_attribute_attach_tag = u'material'

    def __init__(self, *args):
        self._initAbcMtlMaterialProxy(*args)


class GeometryProxy(mtlObjAbs.Abc_MtlGeometryProxy):
    CLS_grh_name = _mtlObjRaw.Name
    CLS_grh_node = Node

    CLS_grh_node_graph_set = _grhObjSet.ObjSet
    CLS_grh_node_graph = NodeGraph

    CLS_grh_port_proxy_set = _grhObjSet.PortProxySet
    VAR_grh_port_proxy_cls_dict = {
        grhCfg.Utility.DEF_grh_keyword_param: _mtlObjPort.BindParm,

        grhCfg.Utility.DEF_grh_keyword_inparm: _mtlObjPort.BindInparm,
        grhCfg.Utility.DEF_grh_keyword_inparm_channel: _mtlObjPort.BindInparm,

        grhCfg.Utility.DEF_grh_keyword_otparm: _mtlObjPort.BindOtparm,
        grhCfg.Utility.DEF_grh_keyword_otparm_channel: _mtlObjPort.BindOtparm,

        grhCfg.Utility.DEF_grh_keyword_property: _mtlObjPort.Property,
        grhCfg.Utility.DEF_grh_keyword_visibility: _mtlObjPort.Visibility
    }

    CLS_mtl_property = _mtlObjPort.Property
    CLS_mtl_visibility_assign = _mtlObjPort.Visibility

    CLS_mtl_propertyset = _mtlObjPort.Propertyset

    VAR_dat_xml_file_element_tag = u'geometry'

    def __init__(self, *args):
        self._initAbcMtlGeometryProxy(*args)
