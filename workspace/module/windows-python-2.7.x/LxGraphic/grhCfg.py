# coding:utf-8
import collections

import re


class Utility(object):
    CLS_ordered_dict = collections.OrderedDict

    MOD_re = re

    DEF_grh_port_pathsep = u'.'

    DEF_grh_key_category = u'category'
    DEF_grh_key_source_category = u'source_category'
    DEF_grh_key_target_category = u'target_category'

    DEF_grh_key_type = u'type'
    DEF_grh_key_source_type = u'source_type'
    DEF_grh_key_target_type = u'target_type'

    DEF_grh_key_port = u'port'
    DEF_grh_key_source_port = u'source_port'
    DEF_grh_key_target_port = u'target_port'

    DEF_grh_key_otparm = u'otparm'
    DEF_grh_key_source_otparm = u'source_otparm'
    DEF_grh_key_target_otparm = u'target_otparm'

    DEF_grh_key_porttype = u'porttype'
    DEF_grh_key_source_porttype = u'source_porttype'
    DEF_grh_key_target_porttype = u'target_porttype'

    DEF_grh_key_portpath = u'portpath'
    DEF_grh_key_source_portpath = u'source_portpath'
    DEF_grh_key_target_portpath = u'target_portpath'

    DEF_grh_key_portkey = u'portkey'
    DEF_grh_key_source_portkey = u'source_portkey'
    DEF_grh_key_target_portkey = u'target_portkey'

    DEF_grh_key_portraw = u'portraw'
    DEF_grh_key_source_portraw = u'source_portraw'
    DEF_grh_key_target_portraw = u'target_portraw'

    DEF_grh_key_assign = u'assign'
    DEF_grh_key_target_assign = u'target_assign'

    DEF_grh_key_parent = u'parent'
    DEF_grh_key_target_parent = u'target_parent'

    DEF_grh_key_children = u'children'
    DEF_grh_key_target_children = u'target_children'

    DEF_grh_keyword_format = u'format'

    DEF_grh_keyword_param = u'param'
    DEF_grh_keyword_param_channel = u'param_channel'
    DEF_grh_keyword_inparm = u'inparm'
    DEF_grh_keyword_inparm_channel = u'input_channel'
    DEF_grh_keyword_otparm = u'otparm'
    DEF_grh_keyword_otparm_channel = u'output_channel'

    DEF_grh_keyword_property = u'property'
    DEF_grh_keyword_visibility = u'visibility'

    DEF_grh_param_assign_keyword_list = [
        DEF_grh_keyword_param,
        DEF_grh_keyword_inparm,
        DEF_grh_keyword_otparm,
        # geometry
        DEF_grh_keyword_property,
        DEF_grh_keyword_visibility,
    ]
    DEF_grh_inparm_assign_keyword_list = [
        DEF_grh_keyword_inparm,
        DEF_grh_keyword_inparm_channel
    ]
    DEF_grh_otparm_assign_keyword_list = [
        DEF_grh_keyword_otparm,
        DEF_grh_keyword_otparm_channel
    ]

    DEF_grh_keyword_default = u'default'

    DEF_grh_keyword_porttype_uv_0 = u'uv_0'
    DEF_grh_keyword_porttype_uv_1 = u'uv_1'

    DEF_grh_keyword_custom_node = u'custom_node'
    DEF_grh_keyword_create_expression = u'create_expression'
    DEF_grh_keyword_after_expression = u'after_expression'
    DEF_grh_keyword_command = u'command'
