# coding=utf-8
from LxCore import lxBasic, lxConfigure
#
none = ''


#
def basicModuleConfig():
    lis = [
        lxConfigure.LynxiProduct_Module_Asset,
        lxConfigure.LynxiProduct_Module_Scenery,
        lxConfigure.LynxiProduct_Module_Scene
    ]
    return lis


@lxBasic.getDicMethod
def basicModuleDic(*args):
    dic = lxBasic.orderedDict()
    dic[lxConfigure.LynxiProduct_Module_Asset] = 'Asset', u'资产'
    dic[lxConfigure.LynxiProduct_Module_Scenery] = 'Scenery', u'场景'
    dic[lxConfigure.LynxiProduct_Module_Scene] = 'Scene', u'镜头'
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
            (lxConfigure.LynxiVariantKey, key),
            (lxConfigure.LynxiVariantValue, value)
        ]
    ]
    return lis


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
        lxConfigure.LynxiMayaPresetKey
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
        (lxConfigure.LynxiAppNameKey, '<appName>'),
        (lxConfigure.LynxiAppVersionKey, '<appVersions>'),
        (lxConfigure.LynxiPlugNameKey, '<plugName>'),
        (lxConfigure.LynxiPlugVersionKey, '<plugVersions>'),
        (lxConfigure.LynxiPlugLoadNamesKey, '<plugLoadNames>'),
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
    dic = lxBasic.orderedDict()
    dic[0] = lxConfigure.LynxiProduct_Stage_Pending, 'Pending', u'等待'
    dic[1] = lxConfigure.LynxiProduct_Stage_Wip, 'WIP', u'制作'
    dic[2] = lxConfigure.LynxiProduct_Stage_Delivery, 'Delivery', u'提交'
    dic[3] = lxConfigure.LynxiProduct_Stage_Refine, 'Refine', u'返修'
    dic[4] = lxConfigure.LynxiProduct_Stage_Validated, 'Validated', u'通过'
    return dic

