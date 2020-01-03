# coding=utf-8
from LxCore import lxBasic, lxCore_
#
none = ''


#
def basicModuleConfig():
    lis = [
        lxCore_.LynxiProduct_Module_Asset,
        lxCore_.LynxiProduct_Module_Scenery,
        lxCore_.LynxiProduct_Module_Scene
    ]
    return lis


@lxBasic.getDicMethod
def basicModuleDic(*args):
    dic = lxBasic.orderedDict()
    dic[lxCore_.LynxiProduct_Module_Asset] = 'Asset', u'资产'
    dic[lxCore_.LynxiProduct_Module_Scenery] = 'Scenery', u'场景'
    dic[lxCore_.LynxiProduct_Module_Scene] = 'Scene', u'镜头'
    return dic


@lxBasic.getDicMethod
def basicPrioritiesDic(*args):
    dic = lxBasic.orderedDict()
    dic['major'] = 'Major', u'主要'
    dic['minor'] = 'Minor', u'次要'
    dic['util'] = 'Util', u'龙套'
    return dic


#
def basicVariantSetConfig(enabled=False, key=none, value=none):
    lis = [
        enabled,
        u'输入备注',
        [
            (lxCore_.LynxiVariantKey, key),
            (lxCore_.LynxiVariantValue, value)
        ]
    ]
    return lis


#
def defaultVariantConfig():
    lis = [
        (lxCore_.LynxiVariantKey, '', '', ''),
        (lxCore_.LynxiVariantValue, '', '', '')
    ]
    return lis


#
def basicPersonnelTeamConfig():
    lis = [
        lxCore_.LynxiValue_Unspecified,
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
        lxCore_.LynxiValue_Unspecified,
        'Artist',
        'Producer',
        'Team - Leader',
        'PM',
        'TD',
        'Rnd',
        lxCore_.LynxiPipelineTdPost
    ]
    return lis


#
def basicAppConfig():
    lis = [
        lxCore_.LynxiValue_Unspecified,
        lxCore_.LynxiMayaPresetKey
    ]
    return lis


#
def basicMayaVersionConfig():
    lis = [
        lxCore_.LynxiValue_Unspecified,
        lxCore_.LynxiGeneralValue,
        '2017',
        '2018',
        '2019'
    ]
    return lis


#
def basicMayaRendererConfig():
    lis = [
        lxCore_.LynxiValue_Unspecified,
        lxCore_.LynxiArnoldRendererValue,
        lxCore_.LynxiRedshiftRendererValue
    ]
    return lis


#
def basicAppShelfSchemeConfig():
    lis = [
        lxCore_.LynxiValue_Unspecified,
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
        lxCore_.LynxiValue_Unspecified,
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
        (lxCore_.LynxiAppNameKey, '<appNames>'),
        (lxCore_.LynxiAppVersionKey, '<appVersions>'),
        (lxCore_.LynxiShelfNameKey, '<shelfName>'),
        (lxCore_.LynxiUiNameKey, '<shelfName>'),
        (lxCore_.LynxiUiTipKey, '<shelfName>')
    ]
    return lis


#
def basicPresetToolSchemeConfig():
    lis = [
        lxCore_.LynxiValue_Unspecified,
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
        (lxCore_.LynxiAppNameKey, '<appNames>'),
        (lxCore_.LynxiAppVersionKey, '<appVersions>'),
        (lxCore_.LynxiToolNameKey, '<toolName>'),
        (lxCore_.LynxiUiNameKey, '<toolName>'),
        (lxCore_.LynxiUiTipKey, '<toolName>')
    ]
    return lis


#
def basicPresetScriptSchemeConfig():
    lis = [
        lxCore_.LynxiValue_Unspecified,
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
        (lxCore_.LynxiAppNameKey, '<appNames>'),
        (lxCore_.LynxiAppVersionKey, '<appVersions>'),
        (lxCore_.LynxiScriptNameKey, '<scriptName>'),
        (lxCore_.LynxiUiNameKey, '<scriptName>'),
        (lxCore_.LynxiUiTipKey, '<scriptName>')
    ]
    return lis


#
def basicAppPlugSchemeConfig():
    lis = [
        lxCore_.LynxiValue_Unspecified
    ]
    return lis


#
def basicAppPlugSetConfig():
    lis = [
        (lxCore_.LynxiAppNameKey, '<applicationName>'),
        (lxCore_.LynxiAppVersionKey, '<appVersions>'),
        (lxCore_.Key_Plug_Name, '<plugName>'),
        (lxCore_.Key_Plug_Version, '<plugVersions>'),
        (lxCore_.Lynxi_Key_Plug_Load_Names, '<plugLoadNames>'),
        (lxCore_.LynxiServerPathKey, '<serverBasicPath>/plug/<app>/<appVersion>/<plugName>/<plugVersion>'),
        (lxCore_.LynxiLocalPathKey, '<localBasicPath>/plug/<app>/<appVersion>/<plugName>/<plugVersion>')
    ]
    return lis


#
def basicMayaTimeUnitConfig():
    lis = [
        lxCore_.LynxiValue_Unspecified,
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
        lxCore_.LynxiValue_Unspecified,
        lxCore_.LynxiCgProjectValue,
        lxCore_.LynxiGameProjectValue
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
    dic = lxBasic.orderedDict()
    dic[0] = lxCore_.LynxiProduct_Stage_Pending, 'Pending', u'等待'
    dic[1] = lxCore_.LynxiProduct_Stage_Wip, 'WIP', u'制作'
    dic[2] = lxCore_.LynxiProduct_Stage_Delivery, 'Delivery', u'提交'
    dic[3] = lxCore_.LynxiProduct_Stage_Refine, 'Refine', u'返修'
    dic[4] = lxCore_.LynxiProduct_Stage_Validated, 'Validated', u'通过'
    return dic

