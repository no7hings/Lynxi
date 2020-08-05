# coding:utf-8
import glob

import copy

import os

import collections

import commands


class AppUtility(object):
    MOD_glob = glob
    MOD_copy = copy
    MOD_commands = commands
    CLS_ordered_dict = collections.OrderedDict

    DEF_app__key__enable = 'enable'
    DEF_app__key__tag = 'tag'
    DEF_app__key__path = 'path'
    DEF_app__key__type = 'type'
    DEF_app__key__name = 'name'
    DEF_app__key__uiname = 'uiname'
    DEF_app__key__version = 'version'
    DEF_app__key__icon = 'icon'
    DEF_app__key__color = 'color'
    DEF_app__key__tip = 'tip'
    DEF_app__key__project = 'project'

    DEF_app__key__children = 'children'

    DEF_app__key__tag_config = 'tag_config'

    DEF_app__keyword__share = 'share'

    DEF_app__keyword__script = 'script'
    DEF_app__keyword__icon = 'icon'

    DEF_app__keyword__source = 'source'

    DEF_app__keyword__self = 'self'

    DEF_app__folder__kit = 'kit'
    DEF_app__folder__appkit = 'appkit'
    DEF_app__folder__toolkit = 'toolkit'

    DEF_app__config_file__appkit_tag = os.path.dirname(__file__) + u'/.data/appkit-tag.config.json'
    DEF_app__config_file__toolkit_tag = os.path.dirname(__file__) + u'/.data/toolkit-tag.config.json'

    DEF_app__tag__property_default_dict = {
        u'enable': False,
        u'uiname': '{self.name}',
        u'icon': 'svg_basic/tag',
        u'tip': 'to be edited.'
    }


class AppTag(object):
    pass
