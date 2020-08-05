# coding:utf-8
import sys

import os

import socket

import getpass

import json

import time

import shutil

import pkgutil

import importlib

import types

import imp

import copy

import platform

import re

import datetime

import math

import hashlib

import collections

import locale

import glob

import gzip

import tarfile

import threading

import uuid

import subprocess

import fnmatch

DEF_mya_node_pathsep = u'|'
DEF_mya_node_namespace_pathsep = u':'

SYS_STDOUT = sys.stdout


class BscUtility(object):
    MOD_getpass = getpass
    MOD_socket = socket
    MOD_time = time
    MOD_datetime = datetime
    MOD_os = os
    MOD_shutil = shutil
    MOD_json = json
    MOD_pkgutil = pkgutil
    MOD_imp = imp
    MOD_sys = sys
    MOD_types = types
    MOD_importlib = importlib
    MOD_copy = copy
    MOD_platform = platform
    MOD_re = re
    MOD_math = math
    MOD_locale = locale
    MOD_hashlib = hashlib
    MOD_glob = glob
    MOD_gzip = gzip
    MOD_tarfile = tarfile
    MOD_threading = threading
    MOD_uuid = uuid
    MOD_subprocess = subprocess

    MTD_os_path = os.path

    MOD_fnmatch = fnmatch

    CLS_dic_order = collections.OrderedDict

    DEF_util__environ_key__path = u'LYNXI_PATH'
    DEF_util__root__default = u'e:/myworkspace/td/lynxi' if MOD_platform.system() == u'Windows' else u'/data/e/myworkspace/td/lynxi'

    DEF_util__environ_key__bin_python = u'LYNXI_BIN_PYTHON'

    DEF_util__environ_key__path_develop = u'LYNXI_PATH_DEVELOP'
    DEF_util__root__default_develop = u'e:/myworkspace/td/lynxi' if MOD_platform.system() == u'Windows' else u'/data/e/myworkspace/td/lynxi'

    DEF_util__environ_key__path_product = u'LYNXI_PATH_PRODUCT'
    DEF_util__root__default_product = u'e:/myworkspace/td/lynxi' if MOD_platform.system() == u'Windows' else u'/data/e/myworkspace/td/lynxi'

    DEF_util__environ_key__path_local = u'LYNXI_PATH_LOCAL'
    DEF_util__root__default_local = u'c:/.lynxi' if MOD_platform.system() == u'Windows' else u'/linux_home/{}'.format(MOD_getpass.getuser())

    DEF_util__environ_key__path_preset = u'LYNXI_PATH_PRESET'
    DEF_util__root__default_preset = DEF_util__root__default_product

    DEF_util__environ_key__path_toolkit = u'LYNXI_PATH_TOOLKIT'
    DEF_util__environ_key__path_appkit = u'LYNXI_PATH_APPKIT'

    DEF_util__environ_key__enable_develop = u'LYNXI_ENABLE_DEVELOP'
    DEF_util__environ_key__enable_trace = u'LYNXI_ENABLE_TRACE'

    DEF_util__environ_key__enable_usedef = u'LYNXI_ENABLE_USEDEF'

    DEF_path_temporary_local = u'{}/.temporary'.format(DEF_util__root__default_local)
    DEF_path_log_local = u'{}/.log'.format(DEF_util__root__default_local)

    DEF_util__environ_key__project = u'LYNXI_PROJECT'

    DEF_time_month = [
        (u'一月', 'January'),
        (u'二月', 'February'),
        (u'三月', 'March'),
        (u'四月', 'April'),
        (u'五月', 'May'),
        (u'六月', 'June'),
        (u'七月', 'July'),
        (u'八月', 'August'),
        (u'九月', 'September'),
        (u'十月', 'October'),
        (u'十一月', 'November'),
        (u'十二月', 'December')
    ]
    DEF_time_day = [
        (u'一日', '1st'),
        (u'二日', '2nd'),
        (u'三日', '3rd'),
        (u'四日', '4th'),
        (u'五日', '5th'),
        (u'六日', '6th'),
        (u'七日', '7th'),
        (u'八日', '8th'),
        (u'九日', '9th'),
        (u'十日', '10th'),
    ]
    DEF_time_week = [
        (u'周一', 'Monday'),
        (u'周二', 'Tuesday'),
        (u'周三', 'Wednesday'),
        (u'周四', 'Thursday'),
        (u'周五', 'Friday'),
        (u'周六', 'Saturday'),
        (u'周天', 'Sunday'),
    ]

    DEF_time_tag_format = u'%Y_%m%d_%H%M_%S'
    DEF_time_prettify_format = u'%Y-%m-%d %H:%M:%S'
    DEF_time_tag_search_string = u'[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9]'

    DEF_time_tag_default = u'0000_0000_0000_00'

    DEF_key_source = u'source'
    DEF_key_username = u'username'
    DEF_key_hostname = u'hostname'
    DEF_key_host = u'host'
    DEF_key_timestamp = u'timestamp'
    DEF_key_stage = u'stage'
    DEF_key_description = u'description'
    DEF_key_note = u'note'

    Folder_Basic = '.lynxi'
    LynxiOsFolder_Database = '.database'
    LynxiOsFolder_History = '.history'
    LynxiOsExtVAR_kit__window__version = '.version.json'
    #
    LynxiOsExt_Info = '.lxInfo'
    LynxiOsExt_Log = '.lxLog'
    LynxiOsExt_Record = '.lxRecord'
    #
    LynxiEnable_Log = False
    #
    LynxiLogType_Exception = 'exception'
    LynxiLogType_Function = 'function'
    LynxiLogType_OsFile = 'file'
    LynxiLogType_Database = 'database'
    #
    OsTimeTagFormat = '%Y_%m%d_%H%M%S'
    #
    DEF_value_preset_unspecified = 'Unspecified'
    #
    LynxiUiIndex_EnName = 0
    LynxiUiIndex_ChName = 1
    #
    LynxiUiIndex_Language = LynxiUiIndex_ChName
    #
    LynxiDatabaseKey_Index = '.index'
    LynxiDatabaseKey_Set = '.set'
    LynxiDatabaseKey_link = '.link'
    #
    LynxiUniqueId_Basic = '4908BDB4-911F-3DCE-904E-96E4792E75F1'
    #
    DEF_key_info_namespace = 'namespace'
    DEF_key_info_username = 'user'
    DEF_key_info_timestamp = 'time'
    DEF_key_info_hostname = 'hostname'
    DEF_key_info_host = 'host'
    DEF_key_info_sourcefile = 'sourcefile'
    DEF_key_info_description = 'description'
    DEF_key_info_note = 'note'
    DEF_key_info_stage = 'stage'
    DEF_key_info_version = 'version'
    #
    DEF_ui_name_toolkit = 'lynxiToolKitPanel'
    # ff0040
    LynxiUi_ErrorRgba = 255, 0, 63, 255
    # fdff42
    LynxiUi_WarningRgba = 255, 255, 64, 255
    # 40FD7F
    LynxiUi_OnRgba = 63, 255, 127, 255
    # 7f7f7f
    LynxiUi_LineRgba = 127, 127, 127, 255
    # dfdfdf
    LynxiUi_TextRgba = 191, 191, 191, 255
    # dfdfdf
    LynxiUi_TextHoverRgba = 223, 223, 223, 255
    # 00dfdf
    LynxiUi_TextHoverRgba_ = 63, 255, 255, 255

    DEF_bsc__platform_name__windows = u'windows'

    DEF_bsc__app_name__lynxi = u'lynxi'
    DEF_bsc__app_version__lynxi = u'0.0.0'

    DEF_bsc__app_name__maya = u'maya'
    DEF_bsc__app_name__houdini = u'houdini'

    VAR_ui_time_tooltip_delay = 1000

    DEF_Value_Default = 'default'

    DEF_bsc__linesep = MOD_os.linesep
    DEF_bsc__pathsep = MTD_os_path.sep
    DEF_bsc__extsep = MTD_os_path.extsep


class BscAppQuery(object):
    lynxi = BscUtility.DEF_bsc__app_name__lynxi
    maya = BscUtility.DEF_bsc__app_name__maya
    houdini = BscUtility.DEF_bsc__app_name__houdini


class Preset(object):
    pass


class Application(object):
    pass


class HtmlColor(object):
    def_color_html_lis = [
        u'#ff003f',  # 0 (255, 0, 63)
        u'#fffd3f',  # 1 (255, 255, 63)
        u'#ff7f3f',  # 2 (255, 127, 63)
        u'#3fff7f',  # 3 (64, 255, 127)
        u'#3f7fff',  # 4 (63, 127, 255)

        u'#dfdfdf',  # 5 (223, 223, 223)
        u'#dfdfdf',  # 6 (191, 191, 191)
        u'#7f7f7f',  # 7 (127, 127, 127)
        u'#3f3f3f',  # 8 (63, 63, 63)
        u'#1f1f1f'  # 9 (31, 31, 31)
    ]

    def_color_html_dic = {
        u'red': def_color_html_lis[0],
        u'yellow': def_color_html_lis[1],
        u'orange': def_color_html_lis[2],
        u'green': def_color_html_lis[3],
        u'blue': def_color_html_lis[4],

        u'white': def_color_html_lis[5],
        u'gray': def_color_html_lis[7],
        u'black': def_color_html_lis[9]
    }

    def __init__(self):
        pass

    @property
    def red(self):
        return self.def_color_html_lis[0]

    @property
    def yellow(self):
        return self.def_color_html_lis[1]

    @property
    def orange(self):
        return self.def_color_html_lis[2]

    @property
    def green(self):
        return self.def_color_html_lis[3]

    @property
    def blue(self):
        return self.def_color_html_lis[4]

    @property
    def white(self):
        return self.def_color_html_lis[5]

    @property
    def gray(self):
        return self.def_color_html_lis[7]

    @property
    def black(self):
        return self.def_color_html_lis[9]

    def raw(self):
        return self.def_color_html_lis


class HsvColor(object):
    def __init__(self):
        pass


class Ui(object):
    @property
    def families(self):
        """
        :return: list
        """
        return [
            u'Arial',
            u'Arial Unicode MS',
            u'Arial Black'
        ]

    @property
    def htmlColors(self):
        """
        * 0 ( 255, 0, 64 ), 1 (255, 255, 64), 2 (255, 127, 0), 3 (64, 255, 127), 4 (0, 223, 223),
        * 5 (191, 191, 191), 6 (223, 223, 223), 7 (127, 127, 127), 8 (0, 0, 0)
        :return: list
        """
        return HtmlColor.def_color_html_lis

    @property
    def htmlColorDict(self):
        return HtmlColor.def_color_html_dic
