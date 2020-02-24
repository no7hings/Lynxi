# coding:utf-8
DEF_mya_node_separator = u'|'
DEF_mya_namespace_separator = u':'


class Utility(object):
    DEF_separator_os = u'/'

    DEF_key_environ_path_develop = u'LYNXI_PATH_DEVELOP'
    VAR_path_default_develop = u'e:/myworkspace/td/lynxi'

    DEF_key_environ_path_product = u'LYNXI_PATH_PRODUCT'
    VAR_path_default_product = u'e:/myworkspace/td/lynxi'

    DEF_key_environ_path_local = u'LYNXI_PATH_LOCAL'

    DEF_key_environ_path_preset = u'LYNXI_PATH_PRESET'
    DEF_key_environ_path_toolkit = u'LYNXI_PATH_TOOLKIT'
    VAR_path_default_preset = u'e:/myworkspace/td/lynxi'

    DEF_key_environ_enable_develop = u'LYNXI_ENABLE_DEVELOP'
    DEF_key_environ_enable_trace = u'LYNXI_ENABLE_TRACE'

    DEF_key_environ_enable_usedef = u'LYNXI_ENABLE_USEDEF'

    DEF_path_temporary_local = u'd:/.lynxi.temporary'
    DEF_path_log_local = u'd:/.lynxi.log'

    DEF_key_environ_project = 'LYNXI_PROJECT'

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
    LynxiOsExt_Version = '.version.json'
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

    DEF_app_maya = u'maya'

    VAR_ui_time_tooltip_delay = 1000

    DEF_Value_Default = 'default'


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
