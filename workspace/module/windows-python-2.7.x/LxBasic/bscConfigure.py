# coding:utf-8
Ma_Separator_Node = u'|'
Ma_Separator_Namespace = u':'


class MtdBasic(object):
    STR_separator_os = u'/'

    STR_key_environ_path_develop = u'LYNXI_PATH_DEVELOP'
    path_default_develop = u'e:/myworkspace/td/lynxi'

    STR_key_environ_path_product = u'LYNXI_PATH_PRODUCT'
    path_default_product = u'e:/myworkspace/td/lynxi'

    STR_key_environ_path_local = u'LYNXI_PATH_LOCAL'

    environ_key_path_preset = u'LYNXI_PATH_PRESET'
    environ_key_path_toolkit = u'LYNXI_PATH_TOOLKIT'
    path_default_preset = u'e:/myworkspace/td/lynxi'

    STR_key_environ_enable_develop = u'LYNXI_ENABLE_DEVELOP'
    environ_key_enable_trace = u'LYNXI_ENABLE_TRACE'

    STR_key_environ_enable_usedef = u'LYNXI_ENABLE_USEDEF'

    STR_path_temporary_local = u'd:/.lynxi.temporary'
    STR_path_log_local = u'd:/.lynxi.log'

    STR_key_environ_project = 'LYNXI_PROJECT'

    LIS_time_month = [
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
    LIS_time_day = [
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
    LIS_time_week = [
        (u'周一', 'Monday'),
        (u'周二', 'Tuesday'),
        (u'周三', 'Wednesday'),
        (u'周四', 'Thursday'),
        (u'周五', 'Friday'),
        (u'周六', 'Saturday'),
        (u'周天', 'Sunday'),
    ]

    STR_time_tag_format = u'%Y_%m%d_%H%M_%S'
    STR_time_prettify_format = u'%Y-%m-%d %H:%M:%S'
    def_time_tag_search_string = u'[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9]'

    STR_time_tag_default = u'0000_0000_0000_00'

    STR_key_source = u'source'
    STR_key_username = u'username'
    STR_key_hostname = u'hostname'
    STR_key_host = u'host'
    STR_key_timestamp = u'timestamp'
    STR_key_stage = u'stage'
    STR_key_description = u'description'
    STR_key_note = u'note'

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
    LynxiValue_Unspecified = 'Unspecified'
    #
    LynxiUiIndex_EnName = 0
    LynxiUiIndex_ChName = 1
    #
    LynxiUiIndex_Language = LynxiUiIndex_ChName
    #
    LynxiDatabaseKey_Index = '.index'
    LynxiDatabaseKey_Set = '.set'
    LynxiDatabaseKey_Link = '.link'
    #
    LynxiUniqueId_Basic = '4908BDB4-911F-3DCE-904E-96E4792E75F1'
    #
    STR_key_info_namespace = 'namespace'
    #
    STR_key_info_username = 'user'
    STR_key_info_time = 'time'
    #
    STR_key_info_hostname = 'hostname'
    STR_key_info_host = 'host'
    #
    STR_key_info_sourcefile = 'sourcefile'
    #
    STR_key_info_description = 'description'
    STR_key_info_note = 'note'
    #
    STR_ui_name_toolkit = 'lynxiToolKitPanel'
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

    STR_app_maya = u'maya'

    INT_ui_time_tooltip_delay = 1000

    STR_Value_Default = 'default'


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
