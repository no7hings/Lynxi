# coding:utf-8
import collections

import re

import copy

import fnmatch

import traceback


class GrhUtility(object):
    MOD_re = re
    MOD_copy = copy
    MOD_fnmatch = fnmatch
    MOD_traceback = traceback

    CLS_ordered_dict = collections.OrderedDict

    DEF_grh__key_source = u'source'
    DEF_grh__key_target = u'target'

    DEF_grh__node_port_pathsep = u'.'

    DEF_grh__key_node_typepath = u'typepath'
    DEF_grh__key_source_typepath = u'source_typepath'
    DEF_grh__key_target_typepath = u'target_typepath'

    DEF_grh__key_port = u'port'
    DEF_grh__key_source_port = u'source_port'
    DEF_grh__key_target_port = u'target_port'

    DEF_grh__key_porttype = u'porttype'
    DEF_grh__key_source_porttype = u'source_porttype'
    DEF_grh__key_target_porttype = u'target_porttype'

    DEF_grh__key_node_datatype = u'datatype'
    DEF_grh__key_node_source_datatype = u'source_datatype'
    DEF_grh__key_node_target_datatype = u'target_datatype'

    DEF_grh__key_port_datatype = u'datatype'
    DEF_grh__key_port_source_datatype = u'source_datatype'
    DEF_grh__key_port_target_datatype = u'target_datatype'

    DEF_grh__key_portsize = u'portsize'

    DEF_grh__key_portpath = u'portpath'
    DEF_grh__key_source_portpath = u'source_portpath'
    DEF_grh__key_target_portpath = u'target_portpath'

    DEF_grh__key_index = u'index'

    DEF_grh__key_portraw = u'portraw'
    DEF_grh__key_source_portraw = u'source_portraw'
    DEF_grh__key_target_portraw = u'target_portraw'

    DEF_grh__keyword_porttype_enumerate = u'enumerate'
    DEF_grh__keyword_datatype_convert = u'datatype_convert'
    DEF_grh__keyword_portraw_convert = u'portraw_convert'

    DEF_grh__key_assign = u'assign'

    DEF_grh__key_parent = u'parent'
    DEF_grh__key_target_parent = u'target_parent'

    DEF_grh__key_children = u'children'
    DEF_grh__key_target_children = u'target_children'

    DEF_grh__key_format = u'format'

    DEF_grh__keyword__gnport = u'gnport'
    DEF_grh__keyword__gnport_channel = u'gnport_channel'

    DEF_grh__keyword__inport = u'inport'
    DEF_grh__keyword__inport_channel = u'input_channel'
    DEF_grh__keyword__otport = u'otport'
    DEF_grh__keyword__otport_channel = u'output_channel'

    DEF_grh__keyword__asport = u'asport'
    DEF_grh__keyword__property = u'property'
    DEF_grh__keyword__visibility = u'visibility'

    DEF_grh__inport_assign_keyword_list = [
        DEF_grh__keyword__inport,
        DEF_grh__keyword__inport_channel,
        # general
        DEF_grh__keyword__gnport,
        DEF_grh__keyword__gnport_channel,
        # geometry
        DEF_grh__keyword__property,
        DEF_grh__keyword__visibility
    ]
    DEF_grh__otport_assign_keyword_list = [
        DEF_grh__keyword__otport,
        DEF_grh__keyword__otport_channel,
        # general
        DEF_grh__keyword__gnport,
        DEF_grh__keyword__gnport_channel,
    ]
    DEF_grh__asport_assign_keyword_list = [
        DEF_grh__keyword__asport
    ]
    DEF_grh__channel_assign_keyword_list = [
        DEF_grh__keyword__inport_channel,
        DEF_grh__keyword__otport_channel,
        DEF_grh__keyword__gnport_channel
    ]
    DEF_grh__inchannel_assign_keyword_list = [
        DEF_grh__keyword__inport_channel,
        DEF_grh__keyword__gnport_channel
    ]
    DEF_grh__otchannel_assign_keyword_list = [
        DEF_grh__keyword__otport_channel,
        DEF_grh__keyword__gnport_channel
    ]

    DEF_grh__keyword__default = u'default'

    DEF_grh__keyword__porttype_texturecoord2_0 = u'texturecoord2_0'
    DEF_grh__keyword__porttype_texturecoord2_1 = u'texturecoord2_1'

    DEF_grh__keyword__custom_node = u'custom_node'
    DEF_grh__keyword__create_expression = u'create_expression'
    DEF_grh__keyword__after_expression = u'after_expression'
    DEF_grh__keyword__command = u'command'


class GrhNodeQuery(object):
    typepath = GrhUtility.DEF_grh__key_node_typepath
    datatype = GrhUtility.DEF_grh__key_node_datatype
    port = GrhUtility.DEF_grh__key_port


class GrhPortQuery(object):
    portpath = GrhUtility.DEF_grh__key_portpath
    porttype = GrhUtility.DEF_grh__key_porttype
    assign = GrhUtility.DEF_grh__key_assign
    children = GrhUtility.DEF_grh__key_children
    parent = GrhUtility.DEF_grh__key_parent
    portraw = GrhUtility.DEF_grh__key_portraw
    format = GrhUtility.DEF_grh__key_format
    @classmethod
    def getPortRaw(cls, **kwargs):
        _portRaw = GrhUtility.CLS_ordered_dict()
        for i in [
            GrhUtility.DEF_grh__key_portpath,
            GrhUtility.DEF_grh__key_porttype,
            GrhUtility.DEF_grh__key_port_datatype,
            GrhUtility.DEF_grh__key_portraw,
            GrhUtility.DEF_grh__key_assign,
            GrhUtility.DEF_grh__key_format,
            GrhUtility.DEF_grh__key_parent,
            GrhUtility.DEF_grh__key_children
        ]:
            if i in kwargs:
                _portRaw[i] = kwargs[i]
            else:
                _portRaw[i] = None
        return _portRaw


class GrhPortAssignQuery(object):
    gnport = GrhUtility.DEF_grh__keyword__gnport
    gnport_channel = GrhUtility.DEF_grh__keyword__gnport_channel

    inport = GrhUtility.DEF_grh__keyword__inport
    inport_channel = GrhUtility.DEF_grh__keyword__inport_channel
    otport = GrhUtility.DEF_grh__keyword__otport
    otport_channel = GrhUtility.DEF_grh__keyword__otport_channel

    asport = GrhUtility.DEF_grh__keyword__asport

    property = GrhUtility.DEF_grh__keyword__property
    visibility = GrhUtility.DEF_grh__keyword__visibility

    @classmethod
    def isInport(cls, *args):
        assignStr = args[0]
        return assignStr in GrhUtility.DEF_grh__inport_assign_keyword_list

    @classmethod
    def isOtport(cls, *args):
        assignStr = args[0]
        return assignStr in GrhUtility.DEF_grh__otport_assign_keyword_list

    @classmethod
    def isAsport(cls, *args):
        assignStr = args[0]
        return assignStr in GrhUtility.DEF_grh__asport_assign_keyword_list

    @classmethod
    def isInchannel(cls, *args):
        assignStr = args[0]
        return assignStr in GrhUtility.DEF_grh__inchannel_assign_keyword_list
    @classmethod
    def isOtchannel(cls, *args):
        assignStr = args[0]
        return assignStr in GrhUtility.DEF_grh__otchannel_assign_keyword_list

    @classmethod
    def isChannel(cls, *args):
        assignStr = args[0]
        return assignStr in GrhUtility.DEF_grh__channel_assign_keyword_list
