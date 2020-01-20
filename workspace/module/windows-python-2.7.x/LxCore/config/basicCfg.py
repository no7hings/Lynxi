# coding=utf-8
from LxBasic import bscModifiers, bscCommands

from LxCore import lxConfigure
#
none = ''


#
def defaultVariantConfig():
    lis = [
        (lxConfigure.LynxiVariantKey, '', '', ''),
        (lxConfigure.LynxiVariantValue, '', '', '')
    ]
    return lis


#
def basicPersonnelTeamConfig():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        'Model',
        'Rig',
        'CFX',
        'Layout',
        'Animation',
        'Simulation',
        'Light',
        'VFX',
        'TS'
    ]
    return lis


#
def basicPersonnelPostConfig():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        'Artist',
        'Producer',
        'Team - Leader',
        'PM',
        'TD',
        'Rnd',
        lxConfigure.LynxiPipelineTdPost
    ]
    return lis


#
def basicAppConfig():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        lxConfigure.Lynxi_Key_Preset_Maya
    ]
    return lis


#
def basicMayaVersionConfig():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        lxConfigure.LynxiGeneralValue,
        '2017',
        '2018',
        '2019'
    ]
    return lis


#
def basicMayaRendererConfig():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        lxConfigure.LynxiArnoldRendererValue,
        lxConfigure.LynxiRedshiftRendererValue
    ]
    return lis


#
def basicAppShelfSchemeConfig():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        'asset',
        'scenery',
        'animation',
        'light',
        'utils'
    ]
    return lis


#
def basicAppShelfToolSchemeConfig():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        'assetManager',
        'sceneryManager',
        'animationManager',
        'lightManager',
        'assetProduction',
        'sceneryProduction',
        'animationProduction',
        'lightProduction',
        'toolKit'
    ]
    return lis


#
def basicPresetShelfSetConfig():
    lis = [
        (lxConfigure.LynxiAppNameKey, '<appNames>'),
        (lxConfigure.LynxiAppVersionKey, '<appVersions>'),
        (lxConfigure.LynxiShelfNameKey, '<shelfName>'),
        (lxConfigure.LynxiUiNameKey, '<shelfName>'),
        (lxConfigure.LynxiUiTipKey, '<shelfName>')
    ]
    return lis


#
def basicPresetToolSchemeConfig():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        'model',
        'rig',
        'cfx',
        'scenery',
        'animation',
        'simulation',
        'light',
        'render',
        'td',
        'rd',
        'utils',
        'project'
    ]
    return lis


#
def basicPresetToolSetConfig():
    lis = [
        (lxConfigure.LynxiAppNameKey, '<appNames>'),
        (lxConfigure.LynxiAppVersionKey, '<appVersions>'),
        (lxConfigure.LynxiToolNameKey, '<toolName>'),
        (lxConfigure.LynxiUiNameKey, '<toolName>'),
        (lxConfigure.LynxiUiTipKey, '<toolName>')
    ]
    return lis


#
def basicPresetScriptSchemeConfig():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        'model',
        'rig',
        'cfx',
        'scenery',
        'animation',
        'simulation',
        'light',
        'render',
        'td',
        'rd',
        'utils',
        'project'
    ]
    return lis


#
def basicPresetScriptSetConfig():
    lis = [
        (lxConfigure.LynxiAppNameKey, '<appNames>'),
        (lxConfigure.LynxiAppVersionKey, '<appVersions>'),
        (lxConfigure.LynxiScriptNameKey, '<scriptName>'),
        (lxConfigure.LynxiUiNameKey, '<scriptName>'),
        (lxConfigure.LynxiUiTipKey, '<scriptName>')
    ]
    return lis


#
def basicAppPlugSchemeConfig():
    lis = [
        lxConfigure.LynxiValue_Unspecified
    ]
    return lis


#
def basicAppPlugSetConfig():
    lis = [
        (lxConfigure.LynxiAppNameKey, '<applicationName>'),
        (lxConfigure.LynxiAppVersionKey, '<appVersions>'),
        (lxConfigure.Key_Plug_Name, '<plugName>'),
        (lxConfigure.Key_Plug_Version, '<plugVersions>'),
        (lxConfigure.Lynxi_Key_Plug_Load_Names, '<plugLoadNames>'),
        (lxConfigure.LynxiServerPathKey, '<serverBasicPath>/plug/<app>/<appVersion>/<plugName>/<plugVersion>'),
        (lxConfigure.LynxiLocalPathKey, '<localBasicPath>/plug/<app>/<appVersion>/<plugName>/<plugVersion>')
    ]
    return lis


#
def basicMayaTimeUnitConfig():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        '15 fps',
        '24 fps',
        '25 fps',
        '30 fps',
        '48 fps',
        '50 fps',
        '60 fps'
    ]
    return lis


#
def basicMayaCommonPlugConfig():
    lis = (
        'gpuCache',
        'AbcExport',
        'AbcImport',
        'animImportExport',
        'animImportExport',
        'sceneAssembly',
        'gameFbxExporter'
    )
    return lis


#
def basicProjectClassificationConfig():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        lxConfigure.LynxiCgProjectValue,
        lxConfigure.LynxiGameProjectValue
    ]
    return lis


#
def basicProductionStages():
    lis = [
        'Validated',
        'Delivery',
        'Refine',
        'WIP',
        'Pending'
    ]
    return lis


#
def basicProductionStageDic():
    dic = bscCommands.orderedDict()
    dic[0] = lxConfigure.LynxiProduct_Stage_Pending, 'Pending', u'等待'
    dic[1] = lxConfigure.LynxiProduct_Stage_Wip, 'WIP', u'制作'
    dic[2] = lxConfigure.LynxiProduct_Stage_Delivery, 'Delivery', u'提交'
    dic[3] = lxConfigure.LynxiProduct_Stage_Refine, 'Refine', u'返修'
    dic[4] = lxConfigure.LynxiProduct_Stage_Validated, 'Validated', u'通过'
    return dic

