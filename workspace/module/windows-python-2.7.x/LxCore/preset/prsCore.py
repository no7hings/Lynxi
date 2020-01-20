# coding=utf-8
import types

from LxBasic import bscMethods, bscCommands
#
from LxCore import lxConfigure, lxScheme
#
from LxCore.config import basicCfg, assetCfg
#
STR_ROOT_PRESET = lxScheme.Root().preset.product
#
IsPresetVariantKey = True
#
presetPathsep = bscCommands.Ma_Separator_Node
guideExt = '.guide'
#
configExt = '.config'
#
none = ''


class Basic(object):
    Lynxi_Key_Preset = 'preset'
    Lynxi_Key_Pipeline = 'pipeline'
    Lynxi_Key_Preset_Variant = 'variant'
    Lynxi_Key_Preset_Personnel = 'personnel'
    Lynxi_Key_Preset_Software = 'software'
    Lynxi_Key_Preset_Maya = 'maya'
    Lynxi_Key_Preset_Project = 'project'
    Lynxi_Key_Preset_Basic = 'basic'
    Lynxi_Key_Preset_Deployment = 'deployment'
    Lynxi_Key_Preset_Environ = 'environ'
    Lynxi_Key_Preset_Set = 'set'
    Lynxi_Key_Preset_Episode = 'episode'
    Lynxi_Key_Preset_Production = 'production'
    Lynxi_Key_Preset_Inspection = 'Inspection'
    Lynxi_Key_Preset_Preference = 'preference'
    Lynxi_Key_Preset_Option = 'option'
    Lynxi_Key_Preset_Asset = 'asset'
    Lynxi_Key_Preset_Scenery = 'scenery'
    Lynxi_Key_Preset_Scene = 'scene'
    Lynxi_Key_Preset_Definition = 'definition'
    Lynxi_Key_Preset_Team = 'team'
    Lynxi_Key_Preset_Post = 'post'
    Lynxi_Key_Preset_User = 'user'
    Lynxi_Key_Preset_Storage = 'storage'
    Lynxi_Key_Preset_Root = 'root'
    Lynxi_Key_Preset_File = 'file'
    Lynxi_Key_Preset_Name = 'name'
    Lynxi_Key_Preset_Data = 'data'
    Lynxi_Key_Preset_Database = 'database'
    Lynxi_Key_Preset_Directory = 'directory'
    Lynxi_Key_Preset_Node = 'node'
    Lynxi_Key_Preset_Attribute = 'attribute'
    Lynxi_Key_Preset_Customization = 'customization'
    Lynxi_Key_Preset_Shelf = 'shelf'
    Lynxi_Key_Preset_Shelf_Tool = 'shelfTool'
    Lynxi_Key_Preset_Kit = 'kit'
    Lynxi_Key_Preset_App = 'app'
    Lynxi_Key_Preset_Plug = 'plug'
    Lynxi_Key_Preset_Renderer = 'renderer'
    Lynxi_Key_Preset_Version = 'version'
    Lynxi_Key_Preset_Script = 'script'
    Lynxi_Key_Preset_Td = 'td'