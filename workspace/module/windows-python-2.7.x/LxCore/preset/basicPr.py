# coding=utf-8
import types
#
from LxCore import lxBasic, lxCore_, lxScheme
#
from LxCore.config import basicCfg, assetCfg
#
basicPresetPath = lxScheme.Root().basic.product
#
IsPresetVariantKey = True
#
presetPathsep = lxBasic.Ma_Separator_Node
guideExt = '.guide'
#
configExt = '.config'
#
none = ''


#
def basicPresetConfig(guidePresetKey):
    dic = lxBasic.orderedDict()
    # Variant
    dic[lxCore_.LynxiVariantPresetKey] = [
        (lxCore_.LynxiVariantPresetKey,),
        #
        (lxCore_.LynxiVariantPresetKey, lxCore_.LynxiShelfPresetKey),
        (lxCore_.LynxiVariantPresetKey, lxCore_.LynxiShelfPresetKey, lxCore_.LynxiDefinitionPresetKey),
        (lxCore_.LynxiVariantPresetKey, lxCore_.LynxiShelfToolPresetKey),
        (lxCore_.LynxiVariantPresetKey, lxCore_.LynxiShelfToolPresetKey, lxCore_.LynxiDefinitionPresetKey),
        (lxCore_.LynxiVariantPresetKey, lxCore_.LynxiKitPresetKey),
        (lxCore_.LynxiVariantPresetKey, lxCore_.LynxiKitPresetKey, lxCore_.LynxiDefinitionPresetKey),
        (lxCore_.LynxiVariantPresetKey, lxCore_.LynxiScriptPresetKey),
        (lxCore_.LynxiVariantPresetKey, lxCore_.LynxiScriptPresetKey, lxCore_.LynxiDefinitionPresetKey),
        (lxCore_.LynxiVariantPresetKey, lxCore_.Lynxi_Key_Plug_PresetKey),
        (lxCore_.LynxiVariantPresetKey, lxCore_.Lynxi_Key_Plug_PresetKey, lxCore_.LynxiDefinitionPresetKey),
        (lxCore_.LynxiVariantPresetKey, lxCore_.Lynxi_Key_Plug_PresetKey, lxCore_.LynxiEnvironPresetKey)
    ]
    # Pipeline
    dic[lxCore_.LynxiPipelinePresetKey] = [
        (lxCore_.LynxiPipelinePresetKey,),
        #
        (lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiBasicPresetKey),
        (lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiBasicPresetKey, lxCore_.LynxiDeploymentPresetKey),
        (lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiBasicPresetKey, lxCore_.LynxiOptionPresetKey),
        (lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiNamePresetKey),
        (lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiNamePresetKey, lxCore_.LynxiBasicPresetKey),
        (lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiNamePresetKey, lxCore_.LynxiDataPresetKey),
        (lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiNamePresetKey, lxCore_.LynxiDatabasePresetKey)
    ]
    # Software
    dic[lxCore_.LynxiSoftwarePresetKey] = [
        (lxCore_.LynxiSoftwarePresetKey,),
        #
        (lxCore_.LynxiSoftwarePresetKey, lxCore_.LynxiAppPresetKey),
        (lxCore_.LynxiSoftwarePresetKey, lxCore_.LynxiAppPresetKey, lxCore_.Lynxi_Key_Plug_PresetKey)
    ]
    # Maya
    dic[lxCore_.LynxiMayaPresetKey] = [
        (lxCore_.LynxiMayaPresetKey,),
        #
        (lxCore_.LynxiMayaPresetKey, lxCore_.LynxiVersionPresetKey),
        (lxCore_.LynxiMayaPresetKey, lxCore_.LynxiRendererPresetKey),
    ]
    # Project
    dic[lxCore_.Lynxi_Key_Preset_Project] = [
        # Project
        (lxCore_.Lynxi_Key_Preset_Project,),
        # Project > Basic
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiBasicPresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiBasicPresetKey, lxCore_.LynxiOptionPresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiBasicPresetKey, lxCore_.LynxiDefinitionPresetKey),
        # Project > Production
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiProductionPresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiProductionPresetKey, lxCore_.LynxiAssetPresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiProductionPresetKey, lxCore_.LynxiScenePresetKey),
        # Project > Inspection
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiInspectionPresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiInspectionPresetKey, lxCore_.LynxiAssetPresetKey),
        #
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiNamePresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiNamePresetKey, lxCore_.LynxiDirectoryPresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiNamePresetKey, lxCore_.LynxiNodePresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiNamePresetKey, lxCore_.LynxiAttributePresetKey),
        #
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiStoragePresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiStoragePresetKey, lxCore_.LynxiRootPresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiStoragePresetKey, lxCore_.LynxiFilePresetKey),
        #
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiMayaPresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiMayaPresetKey, lxCore_.LynxiShelfPresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiMayaPresetKey, lxCore_.LynxiKitPresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiMayaPresetKey, lxCore_.LynxiScriptPresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiMayaPresetKey, lxCore_.LynxiTdPresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiMayaPresetKey, lxCore_.Lynxi_Key_Plug_PresetKey)
    ]
    # Personnel
    dic[lxCore_.LynxiPersonnelPresetKey] = [
        (lxCore_.LynxiPersonnelPresetKey,),
        #
        (lxCore_.LynxiPersonnelPresetKey, lxCore_.LynxiTeamPresetKey),
        (lxCore_.LynxiPersonnelPresetKey, lxCore_.LynxiPostPresetKey),
        (lxCore_.LynxiPersonnelPresetKey, lxCore_.LynxiUserPresetKey)
    ]
    key = guidePresetKey
    if key in dic:
        return dic[key]


#
def basicMainPresetKeySchemeConfig():
    lis = [
        # Variant
        (lxCore_.LynxiVariantPresetKey, lxCore_.LynxiShelfPresetKey),
        (lxCore_.LynxiVariantPresetKey, lxCore_.LynxiShelfToolPresetKey),
        (lxCore_.LynxiVariantPresetKey, lxCore_.LynxiShelfToolPresetKey),
        (lxCore_.LynxiVariantPresetKey, lxCore_.LynxiKitPresetKey),
        (lxCore_.LynxiVariantPresetKey, lxCore_.LynxiScriptPresetKey),
        (lxCore_.LynxiVariantPresetKey, lxCore_.Lynxi_Key_Plug_PresetKey),
        # Pipeline
        (lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiBasicPresetKey),
        (lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiNamePresetKey),
        # Software
        (lxCore_.LynxiSoftwarePresetKey, lxCore_.LynxiAppPresetKey),
        # Maya
        # Project > Basic
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiBasicPresetKey),
        # Project > Production
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiProductionPresetKey),
        # Project > Inspection
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiInspectionPresetKey),
        # Project > Name
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiNamePresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiStoragePresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiMayaPresetKey)
    ]
    return lis


#
def basicVariantPresetKeys():
    lis = [
        # Variant
        # Pipeline
        (lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiBasicPresetKey, lxCore_.LynxiDeploymentPresetKey),
        (lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiBasicPresetKey, lxCore_.LynxiOptionPresetKey),
        (lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiNamePresetKey, lxCore_.LynxiBasicPresetKey),
        (lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiNamePresetKey, lxCore_.LynxiDataPresetKey),
        (lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiNamePresetKey, lxCore_.LynxiDatabasePresetKey),
        # Maya
        # Project
        # Project > Basic > Option
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiBasicPresetKey, lxCore_.LynxiOptionPresetKey),
        # Project > Production > Asset
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiProductionPresetKey, lxCore_.LynxiAssetPresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiProductionPresetKey, lxCore_.LynxiScenePresetKey),
        # Project > Inspection > Asset
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiInspectionPresetKey, lxCore_.LynxiAssetPresetKey),
        #
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiNamePresetKey, lxCore_.LynxiDirectoryPresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiNamePresetKey, lxCore_.LynxiNodePresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiNamePresetKey, lxCore_.LynxiAttributePresetKey),
        (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiStoragePresetKey, lxCore_.LynxiRootPresetKey)
    ]
    return lis


#
def defaultSchemeConfig():
    lis = [
        True,
        u'请输入备注'
    ]
    return lis


#
def defaultSetConfig(setDatumLis=None):
    if setDatumLis is None:
        setDatumLis = []
    lis = [
        (True, u'请输入备注'),
        setDatumLis
    ]
    return lis


#
def presetPath(basicPath):
    string = '{0}/{1}'.format(basicPath, '.preset')
    return string


#
def defaultPresetSchemeLis():
    lis = [
        [
            lxCore_.LynxiDefaultPresetValue,
            None,
            u'默认预设配置'
        ]
    ]
    return lis


#
def defaultPipelineSchemeLis():
    lis = [
        [
            lxCore_.LynxiDefaultPipelineValue,
            None,
            u'默认流程配置'
        ]
    ]
    return lis


#
def defaultVariantSchemeLis():
    lis = [
        [
            lxCore_.LynxiDefaultVariantValue,
            None,
            u'默认变量配置'
        ]
    ]
    return lis


#
def defaultPipelineSetConfig():
    lis = [
        [lxCore_.LynxiBasicPresetKey, getPresetSchemes((lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiBasicPresetKey))],
        [lxCore_.LynxiNamePresetKey, getPresetSchemes((lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiNamePresetKey))]
    ]
    return lis


#
def defaultPipelineDeploymentSetConfig():
    dic = lxBasic.orderedDict()
    dic['pipeStructure'] = [
        None,
        u'流程架构预设',
        [
            [('pipeBasicPresetFolder', 'Preset Folder'), '.preset'],
            [('pipeBasicLogFolder', 'Log Folder'), '.log'],
            [('pipeBasicIconFolder', 'Icon Folder'), 'icon'],
            [('pipeBasicDocumentFolder', 'Document Folder'), 'doc'],
            [('pipeBasicKitFolder', 'Kit Folder'), 'kit'],
            [('pipeBasicScriptFolder', 'Script Folder'), 'script'],
            [('pipeBasicPlugFolder', 'Plug Folder'), 'plug'],
            [('pipeBasicPackageFolder', 'Package Folder'), 'package']
        ]
    ]
    dic['pipePython'] = [
        None,
        u'流程Python预设',
        [
            ['pipePythonSharePackage', '<serverBasicPath>/<pipeBasicPackageFolder>/python/share/<languageVersion>'],
            ['pipeMayaPythonPackage', '<serverBasicPath>/<pipeBasicPackageFolder>/python/maya/<mayaVersion>']
        ]
    ]
    return dic


#
def defaultPipelineOptionSetConfig():
    dic = lxBasic.orderedDict()
    dic['pipelineOption'] = [
        None,
        u'权限设置',
        [
            ['pipeAdministrators', ('dongchangbao',)]
        ]
    ]
    dic['deadlineOption'] = [
        None,
        u'Deadline设置',
        [
            ['pipeDeadlineWebServiceName', '192.168.0.33'],
            ['pipeDeadlineServerPath', '//192.168.0.33/DeadlineRepository10'],
            ['pipeDeadlineLocalPath', 'C:/Program Files/Thinkbox/Deadline7/bin']
        ]
    ]
    dic['mailOption'] = [
        None,
        u'邮件设置',
        [
            [('pipeMailEnabled', u'Enabled'), False],
            [('pipeMailPort', u'Port'), ''],
            [('pipeMailServer', u'Server'), ''],
            [('pipeMailAddress', u'Address'), ''],
            [('pipeMailPassword', u'Password'), '']
        ]
    ]
    dic['assetOption'] = [
        None,
        u'资产设置',
        [
            ['astOperations', ('unused', 'create', 'load')],
            ['astBasicClassifications', ('character', 'prop')],
            ['astCharacterClass', 'character'],
            ['astPropClass', 'prop'],
            ['astSceneryClass', 'scenery'],
            ['astBasicPriorities', ('major', 'minor', 'util')],
            ['astDefaultVariant', 'default'],
            ['astDefaultVersion', 'default'],
            ['sceneryTags', ('building', 'plant', 'furniture')]
        ]
    ]
    dic['sceneryOption'] = [
        None,
        u'资产设置',
        [
            ['scnLayoutLink', 'layout'],
            ['scnLightLink', 'light'],
            ['scnBasicLinks', ('layout', 'light')],
            ['scnSceneryStages', ('scenery', )],
            ['scnAssemblyStages', ('assemblyGroup', )],
            ['scnBasicClassifications', ('scene', 'group')],
            ['scnSceneryClass', 'scenery'],
            ['scnBasicPriorities', ('major', 'minor', 'util')],
            ['scnDefaultVariant', 'default']
        ]
    ]
    dic['sceneOption'] = [
        None,
        u'资产设置',
        [
            ['scDefaultCustomizeLabel', 'A01']
        ]
    ]
    return dic


#
def defaultBasicNameSetConfig():
    dic = lxBasic.orderedDict()
    dic['basicNode'] = [
        None,
        u'数据库预设',
        [
            ['lxPreviewLight', 'lxPreviewLight']
        ]
    ]
    dic['mayaNode'] = [
        None,
        u'数据库预设',
        [
            ['maYetiNode', 'pgYetiMaya'],
            ['maPfxHairNode', 'pfxHair'],
            ['maHairSystemNode', 'hairSystem'],
            ['maNurbsHairNode', 'nurbsHair'],
            ['maNurbsHairInGuideCurvesNode', 'nurbsHairOp_InGuideCurves'],
        ]
    ]
    return dic


#
def defaultDataNameSetConfig():
    dic = lxBasic.orderedDict()
    dic['informationLabel'] = [
        None,
        u'数据库预设',
        [
            ['infoIndexLabel', 'index'],
            ['infoNameLabel', 'name'],
            ['infoEnableLabel', 'enable'],
            ['infoUpdateLabel', 'update'],
            ['infoUpdaterLabel', 'updater'],
            ['infoSourceLabel', 'source'],
            ['descriptionLabel', 'description'],
            ['keyLabel', 'key'],
            ['unlockKeySet', 'unlock'],
            ['lockKeySet', 'lock'],
            ['uploadKeySet', 'uploading'],
            ['linkFileLabel', 'link'],
            ['stageLabel', 'stage'],
            ['updateLabel', 'update'],
            ['artistLabel', 'artist'],
            ['hostNameLabel', 'hostName'],
            ['hostLabel', 'host'],
            ['noteLabel', 'notes'],
            ['tipLabel', 'tips'],
            ['progressLabel', 'progress'],
            ['maxProgressLabel', 'maxProgress'],
            ['activeProjectLabel', 'project'],
            ['infoNonExistsLabel', 'Non - Exists']
        ]
    ]
    return dic


#
def defaultDatabaseNameSetConfig():
    dic = lxBasic.orderedDict()
    dic['databaseFolder'] = [
        None,
        u'数据库预设',
        [
            ['dbAssetBasicKey', 'asset'],
            ['dbSceneryBasicKey', 'scenery'],
            ['dbSceneBasicKey', 'scene'],
            #
            ['dbIndexSubKey', 'index'],
            #
            ['dbModelSubKey', 'model'],
            ['dbRigSubKey', 'rig'],
            ['dbCfxSubKey', 'cfx'],
            #
            ['dbGeometrySubKey', 'geometry'],
            ['dbMeshSubKey', 'mesh'],
            ['dbNurbsSurfaceSubKey', 'nurbsSurface'],
            ['dbNurbsCurveSubKey', 'nurbsCurve'],
            #
            ['dbMaterialSubKey', 'material'],
            ['dbAovSubKey', 'aov'],
            ['dbSubFurKey', 'fur'],
            ['dbGraphSubKey', 'graph'],
            #
            ['dbPictureSubKey', 'picture'],
            ['dbRecordSubKey', 'record'],
            ['dbIntegrationSubKey', 'integration']
        ]
    ]
    dic['databaseExtensionLabel'] = [
        None,
        u'数据库预设',
        [
            ['dbNameUnitKey', '.name'],
            ['dbFilterUnitKey', '.filter'],
            ['dbVariantUnitKey', '.variant'],
            ['dbAssemblyUnitKey', '.assembly'],
            ['dbLockUnitKey', '.lock'],
            #
            ['dbTypeUnitKey', '.type'],
            ['dbGeometryUnitKey', '.geometry'],
            ['dbMeshUnitKey', '.mesh'],
            ['dbNurbsSurfaceUnitKey', '.nurbsSurface'],
            ['dbNurbsCurveUnitKey', '.nurbsCurve'],
            ['dbFurUnitKey', '.fur'],
            #
            ['dbMaterialUnitKey', '.material'],
            ['dbAovUnitKey', '.aov'],
            ['dbGraphUnitKey', '.graph'],
            #
            ['dbTransformUnitKey', '.transform'],
            ['dbGeomTopoUnitKey', '.topology'],
            ['dbGeomShapeUnitKey', '.shape'],
            ['dbVertexNormalUnitKey', '.vertexNormal'],
            ['dbEdgeSmoothUnitKey', '.edgeSmooth'],
            ['dbMapUnitKey', '.map'],
            ['dbAttributeUnitKey', '.attribute'],
            #
            ['dbContrastUnitKey', '.contrast'],
            #
            ['dbNodeUnitKey', '.node'],
            ['dbObjectUnitKey', '.object'],
            ['dbRelationUnitKey', '.relation'],
            ['dbObjectSetUnitKey', '.objectSet'],
            ['dbVertexColorUnitKey', '.colorSet'],
            #
            ['dbPathUnitKey', '.path'],
            #
            ['dbModelLinkUnitKey', '.model'],
            ['dbRigLinkUnitKey', '.rig'],
            ['dbSolverLinkUnitKey', '.solver'],
            ['dbCfxLinkUnitKey', '.cfx'],
            #
            ['dbTextureUnitKey', '.texture'],
            ['dbExtraUnitKey', '.extra'],
            #
            ['dbHistoryUnitKey', '.history'],
            ['dbPreviewUnitKey', '.preview']
        ]
    ]
    return dic


#
def defaultPersonnelSchemeConfig():
    lis = [
        [
            lxCore_.LynxiDefaultPersonnelValue,
            None,
            u'默认人员配置'
        ]
    ]
    return lis


#
def defaultPersonnelTeamSchemeConfig():
    lis = []
    for team in basicCfg.basicPersonnelTeamConfig():
        schemeData = [
            team,
            None,
            u'人员分组'
        ]
        lis.append(schemeData)
    return lis


#
def defaultPersonnelPostSchemeConfig():
    lis = []
    for i in basicCfg.basicPersonnelPostConfig():
        schemeData = [
            i,
            None,
            u'人员职务',
        ]
        lis.append(schemeData)
    return lis


#
def defaultPersonnelPostSetConfig():
    lis = [
        [lxCore_.LynxiPostLevelKey, 0]
    ]
    return lis


#
def defaultPersonnelUserSetConfig():
    lis = [
        [lxCore_.LynxiTeamPresetKey, getPersonnelTeamLis()],
        [lxCore_.LynxiPostPresetKey, getPersonnelPosts()],
        [lxCore_.LynxiUserCnNameKey, ''],
        [lxCore_.LynxiUserEnNameKey, ''],
        [lxCore_.LynxiUserMailKey, ''],
        [lxCore_.LynxiUserSendMailEnabledKey, False]
    ]
    return lis


#
def defaultSoftwareSchemeConfig():
    lis = [
        [
            lxCore_.LynxiDefaultSoftwareValue,
            None,
            u'默认软件配置'
        ]
    ]
    return lis


#
def defaultAppSchemeConfig():
    lis = []
    for i in basicCfg.basicAppConfig():
        schemeData = [
            i,
            None,
            u'软件名称',
        ]
        lis.append(schemeData)
    return lis


#
def defaultAppShelfSchemeConfig():
    lis = []
    for i in basicCfg.basicAppShelfSchemeConfig():
        schemeData = [
            i,
            None,
            u'工具架预设',
        ]
        lis.append(schemeData)
    return lis


#
def defaultAppShelfSetConfig():
    lis = [
        ('nameText', '<shelfName>'),
        ('uiTip', '')
    ]
    return lis


#
def defaultAppShelfToolSchemeConfig():
    lis = []
    for i in basicCfg.basicAppShelfToolSchemeConfig():
        schemeData = [
            i,
            None,
            u'工具架预设',
        ]
        lis.append(schemeData)
    return lis


#
def defaultAppShelfToolSetConfig():
    lis = [
        ('shelf', getShelfNames()),
        ('toolName', '<toolName>'),
        ('nameText', '<toolName>'),
        ('toolIcon', '<serverBasicPath>/<pipeBasicIconFolder>/shelf/manager.png'),
        ('toolIconHover', '<serverBasicPath>/<pipeBasicIconFolder>/shelf/managerOn.png'),
        ('toolTip', ''),
        ('toolCommand', ''),
        #
        ('helpName', ''),
        ('helpIcon', '<serverBasicPath>/<pipeBasicIconFolder>/shelf/shelf/help.png'),
        ('helpIconHover', '<serverBasicPath>/<pipeBasicIconFolder>/shelf/helpOn.png'),
        ('helpTip', ''),
        ('helpCommand', '')
    ]
    return lis


#
def defaultAppKitSchemeConfig():
    lis = []
    for i in basicCfg.basicPresetToolSchemeConfig():
        schemeData = [
            i,
            None,
            u'工具预设',
        ]
        lis.append(schemeData)
    return lis


#
def defaultAppKitSetConfig():
    lis = [
        ('nameText', ''),
        ('uiTip', ''),
        (lxCore_.LynxiServerPathKey, '<serverBasicPath>/<pipeBasicKitFolder>/<app>/<appVersion>/main/<toolName>'),
        (lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/<pipeBasicKitFolder>/<app>/<appVersion>/sub/<toolName>'),
        (lxCore_.LynxiLocalPathKey, '<localBasicPath>/<pipeBasicKitFolder>/<app>/<appVersion>/<toolName>')
    ]
    return lis


#
def defaultAppScriptSchemeConfig():
    lis = []
    for i in basicCfg.basicPresetScriptSchemeConfig():
        schemeData = [
            i,
            None,
            u'脚本预设',
        ]
        lis.append(schemeData)
    return lis


#
def defaultAppScriptSetConfig():
    lis = [
        (lxCore_.LynxiServerPathKey, '<serverBasicPath>/<pipeBasicScriptFolder>/<app>/<appVersion>/main/<scriptName>'),
        (lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/<pipeBasicScriptFolder>/<app>/<appVersion>/sub/<scriptName>'),
        (lxCore_.LynxiLocalPathKey, '<localBasicPath>/<pipeBasicScriptFolder>/<app>/<appVersion>/<scriptName>')
    ]
    return lis


#
def defaultAppPublishSetConfig():
    pass


#
def defaultPresetPlugSchemeConfig():
    lis = []
    for i in basicCfg.basicAppPlugSchemeConfig():
        schemeData = [
            i,
            None,
            u'软件名称',
        ]
        lis.append(schemeData)
    return lis


#
def defaultAppPlugSetConfig():
    lis = [
        (lxCore_.Lynxi_Key_Plug_Load_Names, ()),
        (lxCore_.LynxiServerPathKey, '<serverBasicPath>/<pipeBasicPlugFolder>/<app>/<appVersion>/<plugName>/<plugVersion>'),
        (lxCore_.LynxiLocalPathKey, '<localBasicPath>/<pipeBasicPlugFolder>/<app>/<appVersion>/<plugName>/<plugVersion>'),
        (lxCore_.Lynxi_Key_Plug_Path_Deploy, '<localDirectory>/deploy'),
        (lxCore_.Lynxi_Key_Plug_Path_Module, '<localDirectory>/module'),
        (lxCore_.Lynxi_Key_Plug_Path_Rlm, '<localDirectory>/rlm')
    ]
    return lis


#
def defaultMayaSchemeConfig():
    lis = [
        [
            lxCore_.LynxiDefaultMayaValue,
            None,
            u'默认软件配置'
        ]
    ]
    return lis


#
def defaultMayaVersionSchemeConfig():
    lis = []
    for i in basicCfg.basicMayaVersionConfig():
        schemeData = [
            i,
            None,
            u'Maya版本',
        ]
        lis.append(schemeData)
    return lis


#
def defaultMayaRendererSchemeConfig():
    lis = []
    for i in basicCfg.basicMayaRendererConfig():
        schemeData = [
            i,
            None,
            u'渲染器',
        ]
        lis.append(schemeData)
    return lis


# Project Scheme
def defaultProjectSchemeConfig():
    if lxBasic.isMayaApp():
        mayaVersion = lxBasic.getMayaAppVersion()
        defaultValue = '{}_{}'.format(lxCore_.Lynxi_Keyword_Project_Default, mayaVersion)
    else:
        defaultValue = lxCore_.LynxiDefaultProjectValue
    #
    lis = [
        [
            defaultValue,
            None,
            u'默认项目'
        ]
    ]
    return lis


# Project Set
def defaultProjectSetConfig():
    lis = [
        [
            lxCore_.LynxiBasicPresetKey,
            getPresetSchemes((lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiBasicPresetKey))
        ],
        [
            lxCore_.LynxiProductionPresetKey,
            getPresetSchemes((lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiProductionPresetKey))
        ],
        [
            lxCore_.LynxiInspectionPresetKey,
            getPresetSchemes((lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiInspectionPresetKey))
        ],
        [
            lxCore_.LynxiNamePresetKey,
            getPresetSchemes((lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiNamePresetKey))
        ],
        [
            lxCore_.LynxiStoragePresetKey,
            getPresetSchemes((lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiStoragePresetKey))
        ],
        [
            lxCore_.LynxiMayaPresetKey,
            getPresetSchemes((lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiMayaPresetKey))
        ]
    ]
    return lis


#
def defaultProjectBasicSetConfig():
    lis = [
        [lxCore_.LynxiProjectClassificationKey, basicCfg.basicProjectClassificationConfig()],
        [lxCore_.LynxiMayaRendererKey, getMayaRenderer()],
        [lxCore_.LynxiMayaTimeUnitKey, basicCfg.basicMayaTimeUnitConfig()],
        [lxCore_.LynxiEpisodePresetKey, (lxCore_.LynxiDefaultEpisodeKey,)]
    ]
    return lis


#
def defaultProjectOptionSetConfig():
    dic = lxBasic.orderedDict()
    dic['animationOption'] = [
        None,
        u'动画设置',
        [
            ['animStages', ('scenery', 'layout', 'blocking', 'final', 'polish', 'simulation')],
            ['animOperations', ('unused', 'create', 'load')],
            ['animStartFrame', 100],
            ['animKeyFrameOffset', 5],
            ['animAlembicStep', 0.5]
        ]
    ]
    dic['renderOption'] = [
        None,
        u'渲染设置',
        [
            ['rndrImageWidth', 1920],
            ['rndrImageHeight', 1080],
            ['rndrImageDpi', 72],
            ['rndrImageDeviceAspectRatio', 1],
            ['rndrImagePixelAspect', 1],
            ['rndrImageOutFormat', ['exr', 'tif', 'jpg', 'png']],
            ['rndrImageDeviceAspectRatio', 1],
            ['rndrImageExtensionPadding', 4],
            ['rndrUseReference', True]
        ]
    ]
    return dic


#
def defaultAssetProductionSetConfig():
    dic = lxBasic.orderedDict()
    dic['modelProduction'] = [
        None,
        u'模型生产设置',
        [
            [('isPushModelTextureToDatabase', 'Push Texture to Database'), True],
            [('isPushModelProductToDatabase', 'Push Product to Database'), True]
        ]
    ]
    dic['cfxProduction'] = [
        None,
        u'角色特效生产设置',
        [
            [('isPushCfxTextureToDatabase', 'Push Texture to Database'), True],
            [('isPushCfxMapToDatabase', 'Push Map to Database'), True],
            [('isPushCfxProductToDatabase', 'Push Product to Database'), True]
        ]
    ]
    return dic


#
def defaultSceneProductionSetConfig():
    dic = lxBasic.orderedDict()
    dic['layoutProduction'] = [
        None,
        u'镜头 - 预览 - 生产设置',
        [
            [('isScLayoutAstModelCacheUploadEnable', 'Model Cache Upload Enable'), True],
            [('isScLayoutAstSolverCacheUploadEnable', 'Solver Cache Upload Enable'), True],
            [('isScLayoutAstRigExtraCacheUploadEnable', 'Rig Extra Cache Upload Enable'), True]
        ]
    ]
    dic['animationProduction'] = [
        None,
        u'镜头 - 动画 - 生产设置',
        [
            [('isScAnimationAstModelCacheUploadEnable', 'Model Cache Upload Enable'), True],
            [('isScAnimationAstSolverCacheUploadEnable', 'Solver Cache Upload Enable'), True],
            [('isScAnimationAstRigExtraCacheUploadEnable', 'Rig Extra Cache Upload Enable'), True]
        ]
    ]
    dic['simulationProduction'] = [
        None,
        u'镜头 - 解算 - 生产设置',
        [
            [('isScSimulationAstModelCacheUploadEnable', 'Model Cache Upload Enable'), True],
            [('isScSimulationAstSolverCacheUploadEnable', 'Solver Cache Upload Enable'), False],
            [('isScSimulationAstRigExtraCacheUploadEnable', 'Rig Extra Cache Upload Enable'), False]
        ]
    ]
    dic['solverProduction'] = [
        None,
        u'镜头 - 模拟 - 生产设置',
        [
            [('isScSolverAstModelCacheUploadEnable', 'Model Cache Upload Enable'), False],
            [('isScSolverAstSolverCacheUploadEnable', 'Solver Cache Upload Enable'), False],
            [('isScSolverAstRigExtraCacheUploadEnable', 'Rig Extra Cache Upload Enable'), False]
        ]
    ]
    dic['lightProduction'] = [
        None,
        u'镜头 - 灯光 - 生产设置',
        [
            [('isScLightAstModelCacheUploadEnable', 'Model Cache Upload Enable'), False],
            [('isScLightAstSolverCacheUploadEnable', 'Solver Cache Upload Enable'), False],
            [('isScLightAstRigExtraCacheUploadEnable', 'Rig Extra Cache Upload Enable'), False]
        ]
    ]
    return dic


#
def defaultAssetInspectionSetConfig():
    dic = lxBasic.orderedDict()
    dic['astModelInspection'] = [
        None,
        u'资产 - 模型 - 检查设置',
        [
            [(k, v[1]), v[0]] for k, v in assetCfg.astModelCheckConfig().items()
        ]
    ]
    dic['astMeshGeometryInspection'] = [
        None,
        u'资产 - 模型 - 几何 - 检查设置',
        [
            [(k, v[1]), v[0]] for k, v in assetCfg.astMeshGeomCheckConfig().items()
        ]
    ]
    dic['astRigInspection'] = [
        None,
        u'资产 - 绑定 - 检查设置',
        [
            [(k, v[1]), v[0]] for k, v in assetCfg.astRigCheckConfig().items()
        ]
    ]
    dic['astShaderInspection'] = [
        None,
        u'资产 - 材质 - 检查设置',
        [
            [(k, v[1]), v[0]] for k, v in assetCfg.astShaderCheckConfig().items()
        ]
    ]
    dic['cfxGroomInspection'] = [
        None,
        u'资产 - 角色特效 - 塑形 - 检查设置',
        [
            [(k, v[1]), v[0]] for k, v in assetCfg.astCfxGroomCheckConfig().items()
        ]
    ]
    return dic


#
def defaultDirectoryNameConfig():
    dic = lxBasic.orderedDict()
    dic['basicFolder'] = [
        None,
        u'文件夹名预设',
        [
            ['basicAssetFolder', 'asset'],
            ['basicAssemblyFolder', 'assembly'],
            ['basicSceneryFolder', 'scenery'],
            ['basicSceneFolder', 'scene'],
            ['basicActFolder', 'act'],
            ['basicAnimationFolder', 'animation'],
            ['basicCacheFolder', 'cache'],
            ['basicLightFolder', 'light'],
            ['basicRenderFolder', 'render'],
            ['basicOutputFolder', 'output'],
            ['basicFxFolder', 'fx'],
            ['basicComposeFolder', 'compose'],
            ['dbBasicFolderName', '.database'],
            ['basicMayaFolder', 'maya'],
            ['basicDeadlineFolder', 'deadline'],
            #
            ['basicUnitFolder', 'unit'],
            ['basicComposeFolder', 'compose'],
        ]
    ]
    dic['basicLabel'] = [
        None,
        u'文件标签名预设',
        [
            ['basicModelLinkLabel', '_mdl'],
            ['basicRigLinkLabel', '_rig'],
            ['basicCharacterFxLinkLabel', '_cfx'],
            ['basicSolverLinkLabel', '_sol'],
            ['basicAssemblyLinkLabel', '_asb'],
            #
            ['basicSceneryLinkLabel', '_scn'],
            ['basicLayoutLinkLabel', '_lay'],
            ['basicAnimationLinkLabel', '_anim'],
            ['basicSimulationLinkLabel', '_sim'],
            ['basicLightLinkLabel', '_lgt']
        ]
    ]
    dic['basicSubLabel'] = [
        None,
        u'文件副标签名预设',
        [
            ['basicMeshSubLabel', 'msh'],
            ['basicFurSubLabel', 'fur'],
            ['basicMaterialSubLabel', 'matl'],
            #
            ['basicTextureSubLabel', 'txtr'],
            ['basicMapSubLabel', 'map'],
            ['basicCacheSubLabel', 'cache'],
            #
            ['basicSourceSubLabel', 'src'],
            ['basicProductSubLabel', 'prod'],
            ['basicPreviewSubLabel', 'prv'],
            ['basicSolverSubLabel', 'sol'],
            ['basicAssemblySubLabel', 'asb'],
            #
            ['basicAssemblyDefinitionSubLabel', 'dfn'],
            ['basicAssemblyReferenceSubLabel', 'rfn'],
            #
            ['basicFieldLabel', 'field']
        ]
    ]
    #
    dic['assetFolder'] = [
        None,
        u'文件夹名预设',
        [
            ['astModelLinkFolder', 'model'],
            ['astModelFolderEnabled', True],
            ['astRigLinkFolder', 'rig'],
            ['astRigFolderEnabled', True],
            ['astCfxLinkFolder', 'cfx'],
            ['astCfxFolderEnabled', True],
            ['astRigSolFolder', 'solver'],
            ['astSolverFolderEnabled', True],
            ['astLightLinkFolder', 'light'],
            ['astLightFolderEnabled', True],
            ['astAssemblyLinkFolder', 'assembly'],
            ['astAssemblyFolderEnabled', True]
        ]
    ]
    dic['assetSubFolder'] = [
        None,
        u'文件夹名预设',
        [
            ['astModelTextureFolder', 'texture'],
            ['astRigTextureFolder', 'rigTexture'],
            ['astCfxTextureFolder', 'cfxTexture'],
            ['astSolverTextureFolder', 'solverTexture'],
            ['astLightTextureFolder', 'lightTexture'],
            ['astAssemblyTextureFolder', 'assemblyTexture'],
            #
            ['astModelMapFolder', 'modelMap'],
            ['astRigMapFolder', 'rigMap'],
            ['astCfxMapFolder', 'cfxMap'],
            ['astSolverMapFolder', 'solverMap'],
            ['astLightMapFolder', 'lightMap'],
            #
            ['astModelCacheFolder', 'modelCache'],
            ['astRigCacheFolder', 'rigCache'],
            ['astCfxCacheFolder', 'cfxCache'],
            ['astSolverCacheFolder', 'solverCache'],
            ['astLightCacheFolder', 'lightCache']
        ]
    ]
    dic['assemblyFolder'] = [
        None,
        u'文件夹名预设',
        [
            ['asbUnitFolder', 'unit'],
            ['asbComposeFolder', 'compose']
        ]
    ]
    dic['sceneryFolder'] = [
        None,
        u'文件夹名预设',
        [
            ['scnUnitFolder', 'unit'],
            ['scnSequenceSceneryFolder', 'sequenceScenery'],
            ['scnShotSceneryFolder', 'shotScenery'],
            #
            ['scnSceneryFolder', 'scenery'],
            ['scnLayoutFolder', 'layout'],
            ['scnAnimationFolder', 'animation'],
            ['scnSimulationFolder', 'simulation'],
            ['scnLightFolder', 'light'],
        ]
    ]
    dic['sceneFolder'] = [
        None,
        u'文件夹名预设',
        [
            ['scUnitFolder', 'unit'],
            #
            ['scLayoutFolder', 'layout'],
            ['scSolverFolder', 'solver'],
            ['scAnimationFolder', 'animation'],
            ['scSimulationFolder', 'simulation'],
            ['scLightFolder', 'light'],
            ['scRecordFolder', 'record']
        ]
    ]
    dic['animationFolder'] = [
        None,
        u'文件夹名预设',
        [
            ['animCameraFolder', 'camera'],
            ['animPreviewFolder', 'preview'],
        ]
    ]
    dic['cacheFolder'] = [
        None,
        u'文件夹名预设',
        [
            ['cacheCameraFolder', 'cameraCache'],
            ['cacheAssetFolder', 'assetCache'],
            ['cacheSimulationFolder', 'simulationCache'],
            #
            ['cacheAlembicFolder', 'abcCache'],
            ['cacheGpuFolder', 'gpuCache'],
            ['cacheFurFolder', 'furCache'],
            ['cacheYetiFolder', 'yetiCache'],
            ['cacheGeometryFolder', 'geomCache'],
            ['cacheProxyFolder', 'proxyCache']
        ]
    ]
    dic['renderFolder'] = [
        None,
        u'文件夹名预设',
        [
            ['rndrLightFolder', 'light'],
            ['rndrAssetFolder', 'asset'],
            ['rndrSceneFolder', 'scene'],
        ]
    ]
    dic['outputFolder'] = [
        None,
        u'文件夹名预设',
        [
            ['outImageFolder', 'outImage'],
            ['outComposeFolder', 'outCompose'],
        ]
    ]
    dic['utilitiesFolder'] = [
        None,
        u'文件夹名预设',
        [
            ['utilSourceFolder', 'source'],
            ['utilPreviewFolder', 'preview'],
            ['utilReferenceFolder', 'reference'],
            ['utilsMayaFolder', 'maya'],
            ['utilsArnoldFolder', 'arnold'],
            ['utilsYetiFolder', 'yeti'],
            ['utilsTransferFolder', 'transfer'],
            ['utilsPackageFolder', 'package'],
            ['utilsTemporaryFolder', 'temporary']
        ]
    ]
    #
    dic['assetFileLabel'] = [
        None,
        u'文件标签名预设',
        [
            ['astModelSourceFileLabel', '_mdlSrc'],
            ['astShaderSourceFileLabel', '_shdrSrc'],
            ['astRigSourceFileLabel', '_rigSrc'],
            ['astCfxSourceFileLabel', '_cfxSrc'],
            ['astSolverSourceFileLabel', '_solSrc'],
            ['astLightSourceFileLabel', '_lgtSrc'],
            ['astAssemblySourceFileLabel', '_asbSrc'],
            #
            ['astModelProductFileLabel', '_mdlProd'],
            ['astShaderProductFileLabel', '_shdrProd'],
            ['astRigProductFileLabel', '_rigProd'],
            ['astCfxProductFileLabel', '_cfxProd'],
            ['astSolverProductFileLabel', '_solProd'],
            ['astLightProductFileLabel', '_lgtProd'],
            ['astAssemblyProductFileLabel', '_asbProd'],
            #
            ['astModelPreviewFileLabel', '_mdlPrv'],
            ['astModelPreviewFileLabel', '_shdrPrv'],
            ['astRigPreviewFileLabel', '_rigPrv'],
            ['astCfxPreviewFileLabel', '_cfxPrv'],
            ['astLightPreviewFileLabel', '_lgtPrv'],
            ['astSolverPreviewFileLabel', '_solPrv'],
            ['astAssemblyPreviewFileLabel', '_asbPrv'],
            #
            ['astLayoutRigFileLabel', '_layRig'],
            ['astAnimationRigFileLabel', '_animRig'],
            ['astSimulationRigFileLabel', '_simRig'],
            #
            ['astMeshFileLabel', '_msh'],
            ['astModelMaterialFileLabel', '_mdlMatl'],

            ['astFurFileLabel', '_fur'],
            ['astFurMaterialFileLabel', '_furMatl'],
            #
            ['astAssemblyDefinitionLabel', '_astDfn'],
            ['astAssemblyReferenceLabel', '_astRfn']
        ]
    ]
    dic['sceneryFileLabel'] = [
        None,
        u'文件标签名预设',
        [
            ['sceneryLabel', '_scn'],
            ['scnScenerySourceLabel', '_scnSrc'],
            ['scnSceneryProductLabel', '_scnProd'],
            ['scnSceneryPreviewLabel', '_scnPrv'],
            ['scnSceneryDefinitionLabel', '_scnDfn'],
            ['scnSceneryReferenceLabel', '_scnRfn'],
            ['scnSceneryAssemblyLabel', '_scnAsb'],
            #
            ['scnLayoutLabel', '_lay'],
            ['scnLayoutSourceLabel', '_laySrc'],
            ['scnLayoutProductLabel', '_layProd'],
            ['scnLayoutPreviewLabel', '_layPrv'],
            ['scnDefLayoutinitionLabel', '_layDfn'],
            ['scnLayoutReferenceLabel', '_layRfn'],
            #
            ['scnAnimationLabel', '_anim'],
            ['scnAnimationSourceLabel', '_animSrc'],
            ['scnAnimationProductLabel', '_animProd'],
            ['scnAnimationPreviewLabel', '_animPrv'],
            ['scnAnimationDefinitionLabel', '_animDfn'],
            ['scnAnimationReferenceLabel', '_animRfn'],
            #
            ['scnSimulationLabel', '_sim'],
            ['scnSimulationSourceLabel', '_simSrc'],
            ['scnSimulationProductLabel', '_simProd'],
            ['scnSimulationPreviewLabel', '_simPrv'],
            ['scnSimulationDefinitionLabel', '_simDfn'],
            ['scnSimulationReferenceLabel', '_simRfn'],
            #
            ['scnLightLabel', '_lgt'],
            ['scnLightSourceLabel', '_lgtSrc'],
            ['scnLightProductLabel', '_lgtProd'],
            ['scnLightPreviewLabel', '_lgtPrv'],
            ['scnLightDefinitionLabel', '_lgtDfn'],
            ['scnLightReferenceLabel', '_lgtRfn'],
        ]
    ]
    dic['sceneFileLabel'] = [
        None,
        u'文件标签名预设',
        [
            ['scSoundLabel', 'sud'],
            #
            ['scLayoutLabel', '_lay'],
            ['scLayoutSourceLabel', '_laySrc'],
            ['scLayoutProductLabel', '_layProd'],
            ['scLayoutPreviewLabel', '_layPrv'],
            ['scLayoutCameraLabel', '_layCam'],
            ['scLayoutAssetLabel', '_layAst'],
            ['scLayoutSceneryLabel', '_layScn'],
            ['scLayoutExtraLabel', '_layExtra'],
            ['scLayoutRenderLabel', '_layRndr'],
            #
            ['scAnimationLabel', '_anim'],
            ['scAnimationSourceLabel', '_animSrc'],
            ['scAnimationProductLabel', '_animProd'],
            ['scAnimationPreviewLabel', '_animPrv'],
            ['scAnimationCameraLabel', '_animCam'],
            ['scAnimationAssetLabel', '_animAst'],
            ['scAnimationSceneryLabel', '_animScn'],
            ['scAnimationExtraLabel', '_animExtra'],
            ['scAnimationRenderLabel', '_animRndr'],
            #
            ['scSolverLabel', '_sol'],
            ['scSolverSourceLabel', '_solSrc'],
            ['scSolverProductLabel', '_solProd'],
            ['scSolverPreviewLabel', '_solPrv'],
            ['scSolverCameraLabel', '_solCam'],
            ['scSolverAssetLabel', '_solAst'],
            ['scSolverSceneryLabel', '_solScn'],
            ['scSolverExtraLabel', '_solExtra'],
            ['scSolverRenderLabel', '_solRndr'],
            #
            ['scSimulationLabel', '_sim'],
            ['scSimulationSourceLabel', '_simSrc'],
            ['scSimulationProductLabel', '_simProd'],
            ['scSimulationPreviewLabel', '_simPrv'],
            ['scSimulationCameraLabel', '_simCam'],
            ['scSimulationAssetLabel', '_simAst'],
            ['scSimulationSceneryLabel', 'simScn'],
            ['scSimulationExtraLabel', 'simExtra'],
            ['scSimulationRenderLabel', '_simRndr'],
            #
            ['scLightLabel', '_lgt'],
            ['scLightSourceLabel', '_lgtSrc'],
            ['scLightProductLabel', '_lgtProd'],
            ['scLightPreviewLabel', '_lgtPrv'],
            ['scLightCameraLabel', '_lgtCam'],
            ['scLightAssetLabel', '_lgtAst'],
            ['scLightSceneryLabel', 'lgtScn'],
            ['scLightExtraLabel', 'lgtExtra'],
            ['scLightRenderLabel', '_lgtRndr'],
            #
            ['scAstRigExtraLabel', '_rigExtra'],
            ['scAstModelPoseLabel', '_mdlPose'],
            ['scAstModelSolverLabel', 'Solver']
        ]
    ]
    dic['assemblyFileLabel'] = [
        None,
        u'文件标签名预设',
        [
            ['asbGpuFileLabel', '_gpu'],
            ['asbBoxFileLabel', '_box'],
            ['asbProxyFileLabel', '_prx'],
            ['asbFileLabel', '_asb'],
            ['asbDefinitionFileLabel', '_asbDfn'],
            ['asbReferenceFileLabel', '_asbRfn'],
            ['asbProductFileLabel', '_asbProd']
        ]
    ]
    dic['animationFilePrefix'] = [
        None,
        u'文件标签名预设',
        [
            ['episodeFilePrefix', 'ep'],
            ['sequenceFilePrefix', 'seq'],
            ['sceneFilePrefix', 'sc']
        ]
    ]
    dic['animationFileLabel'] = [
        None,
        u'文件标签名预设',
        [
            ['animationLabel', '_anim'],
            ['layoutLabel', '_lay'],
            ['layoutSourceLabel', '_laySrc'],
            ['blockingLabel', '_blk'],
            ['blockingSourceLabel', '_blkSrc'],
            ['finalLabel', '_fnl'],
            ['finalSourceLabel', '_fnlSrc'],
            ['polishLabel', '_pls'],
            ['polishSourceLabel', '_plsSrc'],
            ['simulationLabel', '_sim'],
            ['simulationSourceLabel', '_simSrc'],
            ['animLayoutCameraLabel', '_layCam'],
            ['animFinalCameraLabel', '_fnlCam'],
            ['simulationCameraLabel', '_simCam'],
            ['animationPreviewLabel', '_animPrv']
        ]
    ]
    dic['utilitiesFileLabel'] = [
        None,
        u'文件标签名预设',
        [
            ['actLabel', '_act'],
            ['actDefinitionLabel', '_actDfn'],
            ['lightLabel', '_lgt'],
            ['sceneLightLabel', '_scLgt'],
            ['renderLabel', '_rndr']
        ]
    ]
    dic['assetExtensionLabel'] = [
        None,
        u'资产扩展名预设',
        [
            ['astAssemblyIndexExt', '.asbIndex'],
        ]
    ]
    dic['sceneryExtensionLabel'] = [
        None,
        u'资产扩展名预设',
        [
            ['assemblyComposeExt', '.compose'],
        ]
    ]
    dic['sceneExtensionLabel'] = [
        None,
        u'镜头扩展名预设',
        [
            ['scSceneIndexExt', '.scIndex'],
            ['scPreviewIndexExt', '.prvIndex'],
            ['scGeomCacheIndexExt', '.geomIndex'],
            ['scFurCacheIndexExt', '.furIndex'],
            ['scRenderIndexExt', '.rndrIndex'],
            #
            ['scDeadlineInfoExt', '.info'],
            ['scDeadlineJobExt', '.job'],
            ['scDeadlineResultExt', '.result']
        ]
    ]
    dic['extensionLabel'] = [
        None,
        u'扩展名预设',
        [
            ['updateExt', '.update'],
            ['mayaAsciiExt', '.ma'],
            ['mayaBinaryExt', '.mb'],
            ['gpuCacheExt', '.abc'],
            ['fbxExt', '.fbx'],
            ['alembicCacheExt', '.abc'],
            ['meshDataExt', '.mshData'],
            ['assetDataExt', '.assData'],
            ['materialDataExt', '.matlData'],
            ['materialLinkExt', '.matlLink'],
            ['textureDataExt', '.txtrData'],
            ['textureLinkExt', '.txtrLink'],
            ['aovDataExt', '.aovData'],
            ['aovLinExt', '.aovLink'],
            ['furDataExt', '.furData'],
            ['furMapDataExt', '.furMapData'],
            ['furMaterialDataExt', '.furMatData'],
            ['furMaterialLinkExt', '.furMatLink'],
            ['furTextureDataExt', '.furTxtrData'],
            ['furTextureLinkExt', '.furTxtrLink'],
            ['assemblyRelationExt', '.asbRlt'],
            ['sceneryLinkExt', '.scnLink'],
            ['sceneryDataExt', '.scn'],
            ['jpgExt', '.jpg'],
            ['pngExt', '.png'],
            ['exrExt', '.exr'],
            ['actDataExt', '.act'],
            ['animationSceneryDataExt', '.scnData'],
            ['animationKeysExt', '.key'],
            ['animationCacheDataExt', '.cache'],
            ['animationFurDataExt', '.furData'],
            ['actProxyDataExt', '.dsoData'],
            ['actProxyLinkExt', '.dsoLink'],
            ['animationCameraCacheIndexExt', '.camCacheLink'],
            ['aviExt', '.avi'],
            ['movExt', '.mov'],
            ['exrExt', '.exr'],
            ['logExt', '.log'],
            ['noteExt', '.note'],
            ['configExt', '.config'],
            ['renderDataExt', '.rndrData'],
            #
            ['infoExt', '.info'],
            ['gzipExt', '.gz']
        ]
    ]
    return dic


#
def lxSet_name_node_dic(*args):
    dic = lxBasic.orderedDict()
    dic['Lynxi_Prefix'] = [
        None,
        u'节点前缀标签预设',
        [
            [('Lynxi_Prefix_Product_Asset', 'Asset Prefix'), 'ast'],
            [('Lynxi_Prefix_Product_Scenery', 'Scenery Prefix'), 'scn'],
            [('Lynxi_Prefix_Product_Scene', 'Scene Prefix'), 'sc']
        ]
    ]
    dic['basicGroupLabel'] = [
        None,
        u'节点组标签预设',
        [
            ['basicGroupLabel', '_grp'],
            #
            ['basicUnitRootGroupLabel', '_unitRoot'],
            ['basicComposeRootGroupLabel', '_compRoot'],
            # Root
            ['basicModelRootGroupLabel', '_modelRoot'],
            ['basicRigRootGroupLabel', '_rigRoot'],
            ['basicCfxRootGroupLabel', '_cfxRoot'],
            #
            ['basicModelLinkGroupLabel', '_model'],
            ['basicRigLinkGroupLabel', '_rig'],
            ['basicCfxLinkGroupLabel', '_cfx'],
            ['basicRigSolLinkGroupLabel', '_rigSol'],
            ['basicLightLinkGroupLabel', '_light'],
            #
            ['basicGeometryGroupLabel', '_geometry'],
            ['basicSolverGeometrySubGroupLabel', '_solver'],
            ['basicSolverClothFieldGroupLabel', '_solClothField'],
            ['basicSolverHairFieldGroupLabel', '_solHairField'],
            ['basicSolverCurveFieldGroupLabel', '_solCurveField'],
            #
            ['basicModelReferenceGroupLabel', '_mdlReference'],
            #
            ['basicModelBridgeGroupLabel', '_mdlBridge'],
            ['basicRigBridgeGroupLabel', '_rigBridge'],
            ['basicSolverBridgeGroupLabel', '_solBridge'],
            #
            ['basicSolverFieldGroupLabel', '_solField'],
            ['basicCollisionFieldGroupLabel', '_collisionField'],
            #
            ['basicAssemblyLabel', '_assembly'],
            ['basicGpuLabel', '_gpu'],
            ['basicProxyLabel', '_proxy'],
            ['basicAssetLabel', '_asset'],
            ['basicControlLabel', '_control'],
            #
            ['basicScCameraGroupLabel', '_camera'],
            ['basicScAstGroupLabel', '_asset'],
            ['basicScSceneryGroupLabel', '_scenery'],
            ['basicScSceneGroupLabel', '_scene'],
            #
            ['basicLayoutLinkGroupLabel', '_lay'],
            ['basicAnimationLinkGroupLabel', '_anim'],
            ['basicSolverLinkGroupLabel', '_solver'],
            ['basicSimulationLinkGroupLabel', '_sim']
        ]
    ]
    dic['assetGroupLabel'] = [
        None,
        u'节点组标签预设',
        [
            ['astFurYetiGroupLabel', '_furYeti'],
            ['astFurMayaGroupLabel', '_furMaya'],
            ['astFurNurbsGroupLabel', '_furNurbs'],
            ['astFurSolverGroupLabel', '_furSol'],
            #
            ['astYetiNodeGroupLabel', '_yetiNode'],
            ['astYetiGroomGroupLabel', '_yetiGroom'],
            ['astYetiGrowGroupLabel', '_yetiGrow'],
            ['astYetiReferenceGroupLabel', '_yetiRef'],
            ['astYetiGuideGroupLabel', '_yetiGuide'],
            ['astYetiGuideFollicleGroupLabel', '_guideFollicle'],
            ['astYetiGuideCurveGroupLabel', '_guideCurve'],
            ['astYetiGuideSolverNodeGroupLabel', '_guideSolver'],
            #
            ['astPfxHairGroupLabel', '_pfxHair'],
            ['astPfxHairGrowGroupLabel', '_pfxGrow'],
            ['astPfxHairFollicleGroupLabel', '_pfxFollicle'],
            ['astPfxHairCurveGroupLabel', '_pfxCurve'],
            ['astPfxHairSolverNodeGroupLabel', '_pfxSolver'],
            #
            ['astCfxFurNhrFieldGroupLabel', '_nurbsField'],
            ['astCfxFurNhrObjectGroupLabel', '_nurbsNode'],
            ['astCfxFurNhrGrowGroupLabel', '_nurbsGrow'],
            ['astCfxFurNhrGuideGroupLabel', '_nurbsGuide'],
            #
            ['astCfxGrowFieldSubGroupLabel', '_growField'],
            ['astCfxGrowSourceGroupLabel', '_growSource'],
            ['astCfxFurGrowTargetGroupLabel', '_growTarget'],
            ['astCfxGrowDeformGroupLabel', '_growDeform'],
            ['astCfxFurCollisionSubGroupLabel', '_furCollision'],
            ['astFurGrowPublicGroupLabel', '_growPublic'],
            #
            ['astRigSolNhrSubGroupLabel', '_solNurbs'],
            ['astRigSolFurFieldGroupLabel', '_furSolField'],
            ['astRigSolNhrFieldGroupLabel', '_nurbsSolField'],
            ['astRigSolNhrSolGuideGroupLabel', '_nurbsSolGuide'],
            ['astRigSolNhrSolCurveGroupLabel', '_nurbsSolCurve'],
            ['astSolverGrowFieldSubGroupLabel', '_solGrowField'],
            ['astSolverGrowSourceGroupLabel', '_solGrowSource'],
            ['astRigSolGrowTargetGroupLabel', '_solGrowTarget'],
            ['astSolverGrowDeformGroupLabel', '_solGrowDeform'],
            ['astRigSolCollisionSubGroupLabel', '_solCollision'],
            #
            ['astRigSolFurCollisionFieldGroupLabel', '_furSolCollisionField']
        ]
    ]
    dic['lightGroupLabel'] = [
        None,
        u'节点组标签预设',
        [
            ['lgtFieldLabel', '_lightField']
        ]
    ]
    dic['basicNodeLabel'] = [
        None,
        u'节点组标签预设',
        [
            ['displayLayerLabel', '_layer']
        ]
    ]
    dic['basicSetLabel'] = [
        None,
        u'节点集合标签预设',
        [
            ['basicSetLabel', '_set']
        ]
    ]
    dic['assetNodeLabel'] = [
        None,
        u'资产节点标签预设',
        [
            ['astRigNodeLabel', '_rig'],
            ['astSolverNodeLabel', '_solver'],
            ['astRigMeshNodeLabel', '_rigMsh'],
            ['astCfxMeshNodeLabel', '_cfxMsh'],
            ['astYetiGuideFollicleNodeLabel', '_guideFollicle'],
            ['astYetiGuideLocalCurveNodeLabel', '_guideLocCurve'],
            ['astYetiGuideOutputCurveNodeLabel', '_guideOutCurve'],
            ['astYetiGuideSystemNodeLabel', '_guideSystem'],
            ['astYetiGuideNucleusNodeLabel', '_guideNucleus'],
            ['astYetiGuideSetNodeLabel', '_guideSet'],
            ['astPfxHairFollicleNodeLabel', '_pfxFollicle'],
            ['astPfxHairLocalCurveNodeLabel', '_pfxLocCurve'],
            ['astPfxHairOutputCurveNodeLabel', '_pfxOutCurve'],
            ['astPfxHairSystemNodeLabel', '_pfxSystem'],
            ['astPfxHairNucleusNodeLabel', '_pfxNucleus'],
            ['astPfxHairShaderNodeLabel', '_pfxShader'],
            ['astPfxHairTextureNodeLabel', '_pfxTexture'],
            ['astPfxHairMapNodeLabel', '_pfxMap'],
            ['astContainerNodeLabel', '_container']
        ]
    ]
    dic['sceneryNodeLabel'] = [
        None,
        u'场景节点标签预设',
        [
            ['scnAssemblyPrefix', 'asb']
        ]
    ]
    dic['sceneNodeLabel'] = [
        None,
        u'镜头节点标签预设',
        [
            ['scCameraNodeLabel', '_cam'],
            ['scOutputCameraNodeLabel', '_outCam'],
            ['scCameraLocatorNodeLabel', '_camLoc'],
            ['scCameraSubLocatorNodeLabel', '_camSubLoc'],
            #
            ['scSoundNodeLabel', '_sud'],
            #
            ['scCacheNodeLabel', '_cache'],
            ['scModelNodeLabel', '_model'],
            ['scRigNodeLabel', '_rig'],
            ['scCfxNodeLabel', '_cfx'],
            ['scSolverNodeLabel', '_solver'],
            ['scExtraNodeLabel', '_extra'],
            ['scSolverCacheNodeLabel', '_solCache'],
            ['scExtraCacheNodeLabel', '_extCache'],
        ]
    ]
    dic['animationNodeLabel'] = [
        None,
        u'动画节点标签预设',
        [
            ['animActLocatorNodeLabel', '_actLoc'],
            ['animSceneLocatorLabel', '_scLoc'],
            ['animLayoutCameraLabel', '_layCam'],
            ['animBlockingCameraLabel', '_blkCam'],
            ['animFinalCameraLabel', '_animCam'],
            ['scnSceneryLocatorLabel', '_scnLoc'],
            ['cameraNodeLabel', ['layout', '_layCam', 'blocking', '_blkCam', 'animation', '_animCam']],
            ['inShapeLabel', '_inShape'],
            ['inContainerLabel', '_inContainer']
        ]
    ]
    dic['lightNodeLabel'] = [
        None,
        u'动画节点标签预设',
        [
            ['lightLocatorLabel', '_lgtLoc'],
            ['sceneryRangeLabel', '_scnRng'],
            ['sceneCameraLabel', '_scCam'],
            ['outLightLabel', '_outLgt']
        ]
    ]
    return dic


#
def defaultAttributeNameSetConfig():
    dic = lxBasic.orderedDict()
    dic['basicAttributeLabel'] = [
        None,
        u'节点组标签预设',
        [
            ['basicHierarchyAttrLabel', 'hierarchy'],
            #
            ['basicArtistAttrLabel', 'lynxiArtist'],
            ['basicUpdateAttrLabel', 'lynxiUpdate'],
            ['basicTagAttrLabel', 'tag'],
            #
            ['basicProjectAttrLabel', 'project'],
            #
            ['basicIndexAttrLabel', 'index'],
            ['basicClassAttrLabel', 'classification'],
            ['basicNameAttrLabel', 'name'],
            ['basicVariantAttrLabel', 'variant'],
            ['basicStageAttrLabel', 'stage'],
            ['basicStartFrameAttrLabel', 'startFrame'],
            ['basicEndFrameAttrLabel', 'endFrame'],
            ['basicWidthAttrLabel', 'width'],
            ['basicHeightAttrLabel', 'height'],
            #
            ['basicCameraAttrLabel', 'camera'],
            ['basicAssetAttrLabel', 'asset'],
            ['basicSceneryAttrLabel', 'scenery'],
            #
            ['basicNumberAttrLabel', 'number'],
            ['basicCustomizeAttrLabel', 'customize'],
            ['basicRootIndexAttrLabel', 'rootIndex'],
            #
            ['basicCacheArtistAttrLabel', 'lynxiCacheArtist'],
            ['basicCacheUpdateAttrLabel', 'lynxiCacheUpdate'],
            ['basicCacheTagAttrLabel', 'cacheTag']
        ]
    ]
    dic['assetAttributeLabel'] = [
        None,
        u'节点组标签预设',
        [
            ['astCfxGrowSourceAttrLabel', 'growSource'],
            ['astRigSolGuideSourceAttrLabel', 'guideSource'],
            ['astUniqueIdAttrLabel', 'assetUniqueID']
        ]
    ]
    dic['assemblyAttributeLabel'] = [
        None,
        u'节点组标签预设',
        [
            ['asbLodLevelAttrLabel', 'lodLevel'],
        ]
    ]
    dic['animationAttributeLabel'] = [
        None,
        u'节点组标签预设',
        [
            ['animEpisodeAttrLabel', 'episode'],
            ['animSequenceAttrLabel', 'sequence'],
            ['animShotAttrLabel', 'shot'],
            ['adFileAttrLabel', 'adFile'],
            ['inGpuAttrLabel', 'inGpu'],
            ['showGpuAttrLabel', 'showGpu'],
            ['cacheAttrLabel', '.cacheFile'],
            ['cacheUpdateAttrLabel', '.cacheUpdate'],
            ['assetAttrLabel', '.assetFile'],
            ['assetUpdateAttrLabel', '.assetUpdate']
        ]
    ]
    return dic


#
def defaultRootStorageSetConfig():
    dic = lxBasic.orderedDict()
    dic['databaseRoot'] = [
        None,
        u'数据库根目录预设',
        [
            ['dbAssetRoot', 'l:/project'],
            ['dbSceneryRoot', 'l:/project'],
            ['dbSceneRoot', 'l:/project'],
            ['dbAnimationRoot', 'l:/project'],
            ['dbLightRoot', 'l:/project'],
            ['dbRenderRoot', 'l:/project'],
            ['dbGeoCacheRoot', 'l:/project'],
            ['dbCfxCacheRoot', 'l:/project'],
            ['dbVfxCacheRoot', 'l:/project'],
            ['dbTemporaryRoot', 'l:/project']
        ]
    ]
    dic[lxCore_.LynxiServerRootKey] = [
        None,
        u'服务器根目录预设',
        [
            ['serverAssetRoot', 'l:/project'],
            ['serverSceneryRoot', 'l:/project'],
            ['serverSceneRoot', 'l:/project'],
            ['serverAnimationRoot', 'l:/project'],
            ['serverLightRoot', 'l:/project'],
            ['serverRenderRoot', 'l:/project'],
            ['serverGeomCacheRoot', 'l:/project'],
            ['serverCfxCacheRoot', 'l:/project'],
            ['serverVfxCacheRoot', 'l:/project'],
            ['serverTemporaryRoot', 'l:/project']
        ]
    ]
    dic[lxCore_.LynxiLocalRootKey] = [
        None,
        u'本地根目录预设',
        [
            ['localAssetRoot', 'd:/project'],
            ['localSceneryRoot', 'd:/project'],
            ['localSceneRoot', 'd:/project'],
            ['localAnimationRoot', 'd:/project'],
            ['localLightRoot', 'd:/project'],
            ['localRenderRoot', 'd:/project'],
            ['localGeomCacheRoot', 'd:/project'],
            ['localCfxCacheRoot', 'd:/project'],
            ['localVfxCacheRoot', 'd:/project'],
            ['localTemporaryRoot', 'd:/project']
        ]
    ]
    dic[lxCore_.LynxiBackupRootKey] = [
        None,
        u'备份根目录预设',
        [
            ['backupAssetRoot', 'l:/projectBackup'],
            ['backupSceneryRoot', 'l:/projectBackup'],
            ['backupSceneRoot', 'l:/projectBackup'],
            ['backupAnimationRoot', 'l:/projectBackup'],
            ['backupLightRoot', 'l:/projectBackup'],
            ['backupRenderRoot', 'l:/projectBackup'],
            ['backupGeomCacheRoot', 'l:/projectBackup'],
            ['backupCfxCacheRoot', 'l:/projectBackup'],
            ['backupVfxCacheRoot', 'l:/projectBackup'],
            ['backupTemporaryRoot', 'l:/projectBackup']
        ]
    ]
    return dic


#
def defaultFileStorageSetConfig():
    dic = lxBasic.orderedDict()
    dic['assetModelFile'] = [
        None,
        u'资产预设',
        [
            ['filePath', '<projectName>/<basicAssetFolder>/<assetName>/<assetVariant>'],
            ['fileName', '<assetName><basicModelLinkLabel>'],
            ['fileExt', '<mayaAsciiExt>']
        ]
    ]
    dic['assetRigFile'] = [
        None,
        u'资产预设',
        [
            ['filePath', '<projectName>/<basicAssetFolder>/<assetName>'],
            ['fileName', '<assetName><basicRigLinkLabel>'],
            ['fileExt', '<mayaAsciiExt>']
        ]
    ]
    dic['assetCfxFile'] = [
        None,
        u'资产预设',
        [
            ['filePath', '<projectName>/<basicAssetFolder>/<assetName>/<assetVariant>'],
            ['fileName', '<assetName><basicCharacterFxLinkLabel>'],
            ['fileExt', '<mayaAsciiExt>']
        ]
    ]
    return dic


#
def defaultMayaProjectSetConfig():
    lis = [
        [lxCore_.LynxiMayaVersionKey, getMayaVersions()],
        [lxCore_.LynxiMayaCommonPlugsKey, basicCfg.basicMayaCommonPlugConfig()]
    ]
    return lis


#
def defaultProjectMayaShelfSetDic():
    dic = lxBasic.orderedDict()
    # Asset
    dic['assetShelf'] = [
        None,
        u'资产工具架预设',
        [
            ['shelfName', 'Model / Rig / CFX'],
            ['shelfIcon', 'svg_basic@svg#asset'],
            ['shelfTip', u'''点击显示资产模块工具架''']
        ]
    ]
    dic['assetManagerTool'] = [
        False,
        u'资产管理工具预设',
        [
            ['shelf', 'assetShelf'],
            ['toolName', 'Asset Manager'],
            ['toolIcon', 'manager.png'],
            ['toolIcon_', 'window#managerTool'],
            ['toolIconHover', '/shelf/managerOn.png'],
            ['toolTip', u'''提示：点击显示资产管理面板'''],
            ['toolCommand', 'from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.If_QtAssetManagerWindow();w.windowShow()'],
            #
            ['helpName', 'Asset Manager Tool Help'],
            ['helpIcon', '/shelf/help.png'],
            ['helpIcon_', 'svg_basic@svg#help'],
            ['helpIconHover', '/shelf/helpOn.png'],
            ['helpTip', u'''提示：点击显示资产管理帮助'''],
            ['helpCommand', 'from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.If_QtAssetManagerWindow();w.helpShow()']
        ]
    ]
    dic['assetProductionTool'] = [
        False,
        u'资产生产工具预设',
        [
            ['shelf', 'assetShelf'],
            ['toolName', 'Asset Production'],
            ['toolIcon', '/shelf/production.png'],
            ['toolIcon_', 'window#ProductionTool'],
            ['toolIconHover', '/shelf/productionOn.png'],
            ['toolTip', u'''提示：点击显示资产生产面板'''],
            ['toolCommand', 'import LxMaya.interface.ifMaAssetProductWindow as uiPanel;uiPanel.tableShow()'],
            #
            ['helpName', 'Asset Production Tool Help'],
            ['helpIcon', '/shelf/help.png'],
            ['helpIcon_', 'svg_basic@svg#help'],
            ['helpIconHover', '/shelf/helpOn.png'],
            ['helpTip', u'''提示：点击显示资产生产帮助'''],
            ['helpCommand', 'import LxMaya.interface.ifMaAssetProductWindow as uiPanel;uiPanel.helpShow()']
        ]
    ]
    dic['assetUtilitiesTool'] = [
        None,
        u'资产通用工具预设',
        [
            ['shelf', 'assetShelf'],
            ['toolName', 'Asset Utilities Tool'],
            ['toolIcon', '/shelf/tool.png'],
            ['toolIcon_', 'svg_basic@svg#toolkit'],
            ['toolIconHover', '/shelf/toolOn.png'],
            ['toolTip', u'''提示：点击显示资产通用工具面板'''],
            ['toolCommand', 'from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.If_QtToolkitWindow();w.windowShow()'],
            #
            ['helpName', 'Asset Utilities Tool Help'],
            ['helpIcon', '/shelf/help.png'],
            ['helpIcon_', 'svg_basic@svg#help'],
            ['helpIconHover', '/shelf/helpOn.png'],
            ['helpTip', u'''提示：点击显示资产通用工具帮助'''],
            ['helpCommand', 'from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.If_QtToolkitWindow();w.helpShow()']
        ]
    ]
    dic['assetPresetTool'] = [
        None,
        u'资产预设工具预设',
        [
            ['shelf', 'assetShelf'],
            ['toolName', 'Asset Preset Tool'],
            ['toolIcon', '/shelf/preset.png'],
            ['toolIcon_', 'svg_basic@svg#setting'],
            ['toolIconHover', '/shelf/presetOn.png'],
            ['toolTip', u'''提示：点击显示资产预设工具面板'''],
            ['toolCommand', 'import LxInterface.qt.ifPresetWindow as w;w.tableShow()'],
            #
            ['helpName', 'Asset Preset Tool'],
            ['helpIcon', '/shelf/help.png'],
            ['helpIcon_', 'svg_basic@svg#help'],
            ['helpIconHover', '/shelf/helpOn.png'],
            ['helpTip', u'''提示：点击显示资产预设工具帮助'''],
            ['helpCommand', 'import LxInterface.qt.ifPresetWindow as w;w.helpShow()']
        ]
    ]
    # Scenery
    dic['sceneryShelf'] = [
        False,
        u'资产工具架预设',
        [
            ['shelfName', 'Assembly / Sce...'],
            ['shelfIcon', 'window#sceneryUnit'],
            ['shelfTip', u'''点击显示场景模块工具架''']
        ]
    ]
    dic['sceneryManagerTool'] = [
        False,
        u'场景管理工具预设',
        [
            ['shelf', 'sceneryShelf'],
            ['toolName', 'Scenery Manager Tool'],
            ['toolIcon', '/shelf/manager.png'],
            ['toolIcon_', 'window#managerTool'],
            ['toolIconHover', '/shelf/managerOn.png'],
            ['toolTip', u'''提示：点击显示场景管理面板'''],
            ['toolCommand', 'from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.If_QtSceneryManagerWindow();w.windowShow()'],
            #
            ['helpName', 'Scenery Manager Tool Help'],
            ['helpIcon', '/shelf/help.png'],
            ['helpIcon_', 'svg_basic@svg#help'],
            ['helpIconHover', '/shelf/helpOn.png'],
            ['helpTip', u'''提示：点击显示场景管理帮助'''],
            ['helpCommand', 'from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.If_QtSceneryManagerWindow();w.helpShow()']
        ]
    ]
    dic['sceneryProductionTool'] = [
        False,
        u'场景生产工具预设',
        [
            ['shelf', 'sceneryShelf'],
            ['toolName', 'Scenery Production Tool'],
            ['toolIcon', '/shelf/production.png'],
            ['toolIcon_', 'window#productionTool'],
            ['toolIconHover', '/shelf/productionOn.png'],
            ['toolTip', u'''提示：点击显示场景生产面板'''],
            ['toolCommand', 'import LxMaya.interface.ifMaSceneryProductWindow as uiPanel;uiPanel.tableShow()'],
            #
            ['helpName', 'Scenery Production Tool Help'],
            ['helpIcon', '/shelf/help.png'],
            ['helpIcon_', 'svg_basic@svg#help'],
            ['helpIconHover', '/shelf/helpOn.png'],
            ['helpTip', u'''提示：点击显示场景生产帮助'''],
            ['helpCommand', 'import LxMaya.interface.ifMaSceneryProductWindow as uiPanel;uiPanel.helpShow()']
        ]
    ]
    dic['sceneryUtilitiesTool'] = [
        False,
        u'场景通用工具预设',
        [
            ['shelf', 'sceneryShelf'],
            ['toolName', 'Scenery Utilities Tool'],
            ['toolIcon', '/shelf/tool.png'],
            ['toolIcon_', 'svg_basic@svg#toolkit'],
            ['toolIconHover', '/shelf/toolOn.png'],
            ['toolTip', u'''提示：点击显示场景通用工具面板'''],
            ['toolCommand', 'from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.If_QtToolkitWindow();w.windowShow()'],
            #
            ['helpName', 'Scenery Utilities Tool Help'],
            ['helpIcon', '/shelf/help.png'],
            ['helpIcon_', 'svg_basic@svg#help'],
            ['helpIconHover', '/shelf/helpOn.png'],
            ['helpTip', u'''提示：点击显示场景通用工具帮助'''],
            ['helpCommand', 'from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.If_QtToolkitWindow();w.helpShow()']
        ]
    ]
    dic['sceneryPresetTool'] = [
        False,
        u'场景预设工具预设',
        [
            ['shelf', 'sceneryShelf'],
            ['toolName', 'Scenery Preset Tool'],
            ['toolIcon', '/shelf/preset.png'],
            ['toolIcon_', 'svg_basic@svg#setting'],
            ['toolIconHover', '/shelf/presetOn.png'],
            ['toolTip', u'''提示：点击显示场景预设工具面板'''],
            ['toolCommand', 'import LxInterface.qt.ifPresetWindow as w;w.tableShow()'],
            #
            ['helpName', 'Scenery Preset Tool Help'],
            ['helpIcon', '/shelf/help.png'],
            ['helpIcon_', 'svg_basic@svg#help'],
            ['helpIconHover', '/shelf/helpOn.png'],
            ['helpTip', u'''提示：点击显示场景预设工具帮助'''],
            ['helpCommand', 'import LxInterface.qt.ifPresetWindow as w;w.helpShow()']
        ]
    ]
    # Scene
    dic['sceneShelf'] = [
        False,
        u'镜头工具架预设',
        [
            ['shelfName', 'Animation / Sim...'],
            ['shelfIcon', 'window#sceneUnit'],
            ['shelfTip', u'''点击显示镜头模块工具架''']
        ]
    ]
    dic['sceneManagerTool'] = [
        False,
        u'镜头管理工具预设',
        [
            ['shelf', 'sceneShelf'],
            ['toolName', 'Animation Manager Tool'],
            ['toolIcon', '/shelf/manager.png'],
            ['toolIcon_', 'window#managerTool'],
            ['toolIconHover', '/shelf/managerOn.png'],
            ['toolTip', u'''提示：点击显示镜头管理面板'''],
            ['toolCommand', 'from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.If_QtSceneManagerWindow();w.windowShow()'],
            #
            ['helpName', 'Animation Manager Tool Help'],
            ['helpIcon', '/shelf/help.png'],
            ['helpIcon_', 'svg_basic@svg#help'],
            ['helpIconHover', '/shelf/helpOn.png'],
            ['helpTip', u'''提示：点击显示镜头管理帮助'''],
            ['helpCommand', 'from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.If_QtSceneManagerWindow();w.helpShow()']
        ]
    ]
    dic['sceneProductionTool'] = [
        False,
        u'镜头生产工具预设',
        [
            ['shelf', 'sceneShelf'],
            ['toolName', 'Animation Production Tool'],
            ['toolIcon', '/shelf/production.png'],
            ['toolIcon_', 'window#productionTool'],
            ['toolIconHover', '/shelf/productionOn.png'],
            ['toolTip', u'''提示：点击显示镜头生产面板'''],
            ['toolCommand', 'import LxMaya.interface.ifMaSceneProductWindow as table;reload(table);table.tableShow()'],
            #
            ['helpName', 'Animation Production Tool Help'],
            ['helpIcon', '/shelf/help.png'],
            ['helpIcon_', 'svg_basic@svg#help'],
            ['helpIconHover', '/shelf/helpOn.png'],
            ['helpTip', u'''提示：点击显示镜头生产帮助'''],
            ['helpCommand', 'import LxMaya.interface.ifMaSceneProductWindow as table;table.helpShow()']
        ]
    ]
    dic['sceneUtilitiesTool'] = [
        False,
        u'镜头通用工具预设',
        [
            ['shelf', 'sceneShelf'],
            ['toolName', 'Animation Utilities Tool'],
            ['toolIcon', '/shelf/tool.png'],
            ['toolIcon_', 'svg_basic@svg#toolkit'],
            ['toolIconHover', '/shelf/toolOn.png'],
            ['toolTip', u'''提示：点击显示镜头通用工具面板'''],
            ['toolCommand', 'from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.If_QtToolkitWindow();w.windowShow()'],
            #
            ['helpName', 'Animation Utilities Tool Help'],
            ['helpIcon', '/shelf/help.png'],
            ['helpIcon_', 'svg_basic@svg#help'],
            ['helpIconHover', '/shelf/helpOn.png'],
            ['helpTip', u'''提示：点击显示镜头通用工具帮助'''],
            ['helpCommand', 'from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.If_QtToolkitWindow();w.helpShow()']
        ]
    ]
    dic['scenePresetTool'] = [
        False,
        u'镜头预设工具预设',
        [
            ['shelf', 'sceneShelf'],
            ['toolName', 'Animation Preset Tool'],
            ['toolIcon', '/shelf/preset.png'],
            ['toolIcon_', 'svg_basic@svg#setting'],
            ['toolIconHover', '/shelf/presetOn.png'],
            ['toolTip', u'''提示：点击显示镜头预设工具面板'''],
            ['toolCommand', 'import LxInterface.qt.ifPresetWindow as w;w.tableShow()'],
            #
            ['helpName', 'Animation Preset Tool Help'],
            ['helpIcon', '/shelf/help.png'],
            ['helpIcon_', 'svg_basic@svg#help'],
            ['helpIconHover', '/shelf/helpOn.png'],
            ['helpTip', u'''提示：点击显示镜头预设工具帮助'''],
            ['helpCommand', 'import LxInterface.qt.ifPresetWindow as w;w.helpShow()']
        ]
    ]
    return dic


#
def defaultProjectMayaToolKitSetDic():
    dic = lxBasic.orderedDict()
    dic['model'] = [
        True,
        u'模型工具',
        [
            ['nameText', 'Model'],
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/model'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/model'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/tool/maya/model']
        ]
    ]
    dic['rig'] = [
        True,
        u'绑定工具',
        [
            ['nameText', 'Rig'],
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/rig'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/rig'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/tool/maya/rig'],
        ]
    ]
    dic['cfx'] = [
        True,
        u'角色特效工具',
        [
            ['nameText', 'Character FX'],
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/cfx'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/cfx'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/tool/maya/cfx']
        ]
    ]
    dic['scenery'] = [
        True,
        u'场景工具',
        [
            ['nameText', 'Scenery'],
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/scenery'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/scenery'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/tool/maya/scenery']
        ]
    ]
    dic['animation'] = [
        True,
        u'动画工具',
        [
            ['nameText', 'Animation'],
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/animation'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/animation'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/tool/maya/animation']
        ]
    ]
    dic['simulation'] = [
        True,
        u'解算工具',
        [
            ['nameText', 'Simulation'],
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/simulation'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/simulation'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/tool/maya/simulation']
        ]
    ]
    dic['light'] = [
        True,
        u'灯光工具',
        [
            ['nameText', 'Light'],
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/light'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/light'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/tool/maya/light']
        ]
    ]
    dic['utilities'] = [
        True,
        u'公用工具',
        [
            ['nameText', 'Utilities'],
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/utilities'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/utilities'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/tool/maya/utilities']
        ]
    ]
    dic['td'] = [
        None,
        u'TD工具',
        [
            ['nameText', 'TD'],
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/td'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/td'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/tool/maya/td']
        ]
    ]
    dic['rd'] = [
        None,
        u'RnD工具',
        [
            ['nameText', 'RnD'],
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/rd'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/rd'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/tool/maya/rd']
        ]
    ]
    dic['project'] = [
        False,
        u'项目工具',
        [
            ['nameText', 'Project'],
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/<projectName>'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/<projectName>'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/tool/maya/<projectName>']
        ]
    ]
    return dic


#
def defaultProjectMayaScriptSetConfig():
    dic = lxBasic.orderedDict()
    dic['model'] = [
        False,
        u'模型脚本',
        [
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/model'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/model'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/script/maya/model']
        ]
    ]
    dic['rig'] = [
        False,
        u'绑定脚本',
        [
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/rig'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/rig'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/script/maya/rig'],
        ]
    ]
    dic['cfx'] = [
        False,
        u'角色特效脚本',
        [
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/cfx'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/cfx'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/script/maya/cfx']
        ]
    ]
    dic['scenery'] = [
        False,
        u'场景脚本',
        [
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/scenery'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/scenery'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/script/maya/scenery']
        ]
    ]
    dic['animation'] = [
        False,
        u'动画脚本',
        [
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/animation'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/animation'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/script/maya/animation']
        ]
    ]
    dic['simulation'] = [
        False,
        u'解算脚本',
        [
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/simulation'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/simulation'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/script/maya/simulation']
        ]
    ]
    dic['light'] = [
        False,
        u'灯光脚本',
        [
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/light'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/light'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/script/maya/light']
        ]
    ]
    dic['utilities'] = [
        False,
        u'公用脚本',
        [
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/utilities'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/utilities'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/script/maya/utilities']
        ]
    ]
    dic['td'] = [
        False,
        u'TD脚本',
        [
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/td'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/td'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/script/maya/td']
        ]
    ]
    dic['rd'] = [
        False,
        u'RnD脚本',
        [
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/rd'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/rd'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/script/maya/rd']
        ]
    ]
    dic['project'] = [
        False,
        u'项目脚本',
        [
            [lxCore_.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/<projectName>'],
            [lxCore_.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/<projectName>'],
            [lxCore_.LynxiLocalPathKey, '<localBasicPath>/script/maya/<projectName>']
        ]
    ]
    return dic


#
def defaultProjectMayaTdSetConfig():
    dic = lxBasic.orderedDict()
    dic['model'] = [
        False,
        u'模型脚本',
        [
            [lxCore_.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/model'],
            [lxCore_.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/model']
        ]
    ]
    dic['rig'] = [
        False,
        u'绑定脚本',
        [
            [lxCore_.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/rig'],
            [lxCore_.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/rig']
        ]
    ]
    dic['cfx'] = [
        False,
        u'角色特效脚本',
        [
            [lxCore_.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/cfx'],
            [lxCore_.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/cfx']
        ]
    ]
    dic['solver'] = [
        False,
        u'模拟脚本',
        [
            [lxCore_.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/solver'],
            [lxCore_.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/solver']
        ]
    ]
    dic['scenery'] = [
        False,
        u'场景脚本',
        [
            [lxCore_.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/scenery'],
            [lxCore_.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/scenery']
        ]
    ]
    dic['animation'] = [
        False,
        u'动画脚本',
        [
            [lxCore_.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/animation'],
            [lxCore_.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/animation']
        ]
    ]
    dic['simulation'] = [
        False,
        u'解算脚本',
        [
            [lxCore_.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/simulation'],
            [lxCore_.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/simulation']
        ]
    ]
    dic['light'] = [
        False,
        u'灯光脚本',
        [
            [lxCore_.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/light'],
            [lxCore_.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/light']
        ]
    ]
    return dic


#
def defaultProjectPythonPackage():
    pass


#
def presetKeyPathMethod(*args):
    return presetPathsep.join(args)


#
def presetKeysMethod(presetKeyPath):
    return presetKeyPath.split(presetPathsep)


#
def presetIndexFileMethod(presetKeys, mainSchemeKey=none):
    string = '{0}/{1}/.{2}'.format(presetPath(basicPresetPath), lxCore_.LynxiSchemeExt, '.'.join(presetKeys))
    if mainSchemeKey:
        string = '{0}/{1}/{3}@.{2}'.format(presetPath(basicPresetPath), lxCore_.LynxiSchemeExt, '.'.join(presetKeys), mainSchemeKey)
    return lxBasic.getOsUniqueFile(string)


#
def presetSetFileMethod(presetKeys, mainSchemeKey=none):
    string = '{0}/{1}/.{2}'.format(presetPath(basicPresetPath), lxCore_.LynxiSetExt, '.'.join(presetKeys))
    if mainSchemeKey:
        string = '{0}/{1}/{3}@.{2}'.format(presetPath(basicPresetPath), lxCore_.LynxiSetExt, '.'.join(presetKeys), mainSchemeKey)
    return lxBasic.getOsUniqueFile(string)


#
def presetDicMethod(fn):
    def subMethod(*args):
        inputFn = fn(*args)
        if len(args) == 1:
            args = args[0]
        if args in inputFn:
            return inputFn[args]
    return subMethod


#
def basicPresetSchemeConfig(presetKeys, mainSchemeKey=none):
    dic = lxBasic.orderedDict()
    # Preset 01
    dic[(lxCore_.LynxiVariantPresetKey,)] = defaultPresetSchemeLis
    # Pipeline 01
    dic[(lxCore_.LynxiPipelinePresetKey,)] = defaultPipelineSchemeLis
    # Personnel 01
    dic[(lxCore_.LynxiPersonnelPresetKey,)] = defaultPersonnelSchemeConfig
    # Software 01
    dic[(lxCore_.LynxiSoftwarePresetKey,)] = defaultSoftwareSchemeConfig
    # Maya 01
    dic[(lxCore_.LynxiMayaPresetKey,)] = defaultMayaSchemeConfig
    # Project 01
    dic[(lxCore_.Lynxi_Key_Preset_Project,)] = defaultProjectSchemeConfig
    # Preset 02
    dic[(lxCore_.LynxiVariantPresetKey, lxCore_.LynxiShelfPresetKey)] = defaultAppShelfSchemeConfig
    dic[(lxCore_.LynxiVariantPresetKey, lxCore_.LynxiShelfToolPresetKey)] = defaultAppShelfToolSchemeConfig
    dic[(lxCore_.LynxiVariantPresetKey, lxCore_.LynxiKitPresetKey)] = defaultAppKitSchemeConfig
    dic[(lxCore_.LynxiVariantPresetKey, lxCore_.LynxiScriptPresetKey)] = defaultAppScriptSchemeConfig
    dic[(lxCore_.LynxiVariantPresetKey, lxCore_.Lynxi_Key_Plug_PresetKey)] = defaultPresetPlugSchemeConfig
    # Pipeline 02
    dic[(lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiBasicPresetKey)] = [
        [
            lxCore_.LynxiDefaultSchemeValue,
            None,
            u'默认流程基础配置'
        ]
    ]
    dic[(lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiNamePresetKey)] = [
        [
            lxCore_.LynxiDefaultSchemeValue,
            None,
            u'默认流程命名配置'
        ]
    ]
    # Personnel 02
    dic[(lxCore_.LynxiPersonnelPresetKey, lxCore_.LynxiTeamPresetKey)] = defaultPersonnelTeamSchemeConfig
    dic[(lxCore_.LynxiPersonnelPresetKey, lxCore_.LynxiPostPresetKey)] = defaultPersonnelPostSchemeConfig
    # Software 02
    dic[(lxCore_.LynxiSoftwarePresetKey, lxCore_.LynxiAppPresetKey)] = defaultAppSchemeConfig
    # Maya 02
    dic[(lxCore_.LynxiMayaPresetKey, lxCore_.LynxiRendererPresetKey)] = defaultMayaRendererSchemeConfig
    dic[(lxCore_.LynxiMayaPresetKey, lxCore_.LynxiVersionPresetKey)] = defaultMayaVersionSchemeConfig
    # Project 02
    dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiBasicPresetKey)] = [
        [
            lxCore_.LynxiDefaultSchemeValue,
            None,
            u'默认项目基础配置'
        ]
    ]
    # Project 02
    dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiProductionPresetKey)] = [
        [
            lxCore_.LynxiDefaultSchemeValue,
            None,
            u'默认项目制作配置'
        ]
    ]
    dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiInspectionPresetKey)] = [
        [
            lxCore_.LynxiDefaultSchemeValue,
            None,
            u'默认项目检查配置'
        ]
    ]
    dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiStoragePresetKey)] = [
        [
            lxCore_.LynxiDefaultSchemeValue,
            None,
            u'默认项目存储配置'
        ]
    ]
    dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiNamePresetKey)] = [
        [
            lxCore_.LynxiDefaultSchemeValue,
            None,
            u'默认项目命名配置'
        ]
    ]
    dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiMayaPresetKey)] = [
        [
            lxCore_.LynxiDefaultSchemeValue,
            None,
            u'默认项目Maya配置'
        ]
    ]
    key = presetKeys
    if key in dic:
        data = dic[key]
        if isinstance(data, tuple) or isinstance(data, list):
            return data
        elif isinstance(data, types.FunctionType) or isinstance(data, types.ClassType):
            # noinspection PyCallingNonCallable
            return data()


#
def basicPresetSetConfig(presetKeys, mainSchemeKey=none):
    dic = lxBasic.orderedDict()
    if len(presetKeys) == 1:
        # Pipeline 01
        dic[(lxCore_.LynxiPipelinePresetKey,)] = \
            defaultPipelineSetConfig
        # Project 01
        dic[(lxCore_.Lynxi_Key_Preset_Project,)] = \
            defaultProjectSetConfig
    elif len(presetKeys) == 2:
        # Variant 02
        dic[(lxCore_.LynxiVariantPresetKey, lxCore_.LynxiShelfPresetKey)] = \
            defaultAppShelfSetConfig
        dic[(lxCore_.LynxiVariantPresetKey, lxCore_.LynxiShelfToolPresetKey)] = \
            defaultAppShelfToolSetConfig
        dic[(lxCore_.LynxiVariantPresetKey, lxCore_.LynxiKitPresetKey)] = \
            defaultAppKitSetConfig
        dic[(lxCore_.LynxiVariantPresetKey, lxCore_.LynxiScriptPresetKey)] = \
            defaultAppScriptSetConfig
        dic[(lxCore_.LynxiVariantPresetKey, lxCore_.Lynxi_Key_Plug_PresetKey)] = \
            defaultAppPlugSetConfig
        # Personnel 02
        dic[(lxCore_.LynxiPersonnelPresetKey, lxCore_.LynxiPostPresetKey)] = \
            defaultPersonnelPostSetConfig
        dic[(lxCore_.LynxiPersonnelPresetKey, lxCore_.LynxiUserPresetKey)] = \
            defaultPersonnelUserSetConfig
        # Software 02
        # Maya 02
        # Project 02
        dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiBasicPresetKey)] = \
            defaultProjectBasicSetConfig
        dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiMayaPresetKey)] = defaultMayaProjectSetConfig
    elif len(presetKeys) == 3:
        # Preset 03
        # Pipeline 03
        dic[(lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiBasicPresetKey, lxCore_.LynxiDeploymentPresetKey)] = \
            defaultPipelineDeploymentSetConfig
        dic[(lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiBasicPresetKey, lxCore_.LynxiOptionPresetKey)] = \
            defaultPipelineOptionSetConfig
        dic[(lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiNamePresetKey, lxCore_.LynxiBasicPresetKey)] = \
            defaultBasicNameSetConfig
        dic[(lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiNamePresetKey, lxCore_.LynxiDatabasePresetKey)] = \
            defaultDatabaseNameSetConfig
        dic[(lxCore_.LynxiPipelinePresetKey, lxCore_.LynxiNamePresetKey, lxCore_.LynxiDataPresetKey)] = \
            defaultDataNameSetConfig
        # Software 03
        # Maya 03
        # Project 03
        dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiBasicPresetKey, lxCore_.LynxiOptionPresetKey)] = defaultProjectOptionSetConfig
        dic[(
            lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiProductionPresetKey, lxCore_.LynxiAssetPresetKey)] = defaultAssetProductionSetConfig
        dic[(
            lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiProductionPresetKey, lxCore_.LynxiScenePresetKey)] = defaultSceneProductionSetConfig
        dic[(
            lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiInspectionPresetKey, lxCore_.LynxiAssetPresetKey)] = defaultAssetInspectionSetConfig
        dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiNamePresetKey, lxCore_.LynxiDirectoryPresetKey)] = defaultDirectoryNameConfig
        dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiNamePresetKey, lxCore_.LynxiNodePresetKey)] = lxSet_name_node_dic
        dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiNamePresetKey, lxCore_.LynxiAttributePresetKey)] = defaultAttributeNameSetConfig
        dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiStoragePresetKey, lxCore_.LynxiRootPresetKey)] = defaultRootStorageSetConfig
        dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiStoragePresetKey, lxCore_.LynxiFilePresetKey)] = defaultFileStorageSetConfig
        dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiMayaPresetKey, lxCore_.LynxiShelfPresetKey)] = defaultProjectMayaShelfSetDic
        dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiMayaPresetKey, lxCore_.LynxiKitPresetKey)] = defaultProjectMayaToolKitSetDic
        dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiMayaPresetKey, lxCore_.LynxiScriptPresetKey)] = defaultProjectMayaScriptSetConfig
        dic[(lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiMayaPresetKey, lxCore_.LynxiTdPresetKey)] = defaultProjectMayaTdSetConfig
    #
    key = presetKeys
    if key in dic:
        data = dic[key]
        if isinstance(data, list):
            return data
        elif isinstance(data, types.FunctionType) or isinstance(data, types.ClassType):
            # noinspection PyCallingNonCallable
            return data()
    else:
        if key == (lxCore_.Lynxi_Key_Preset_Project, lxCore_.LynxiMayaPresetKey, lxCore_.Lynxi_Key_Plug_PresetKey):
            return {}


#
def basicSubPresetSchemeConfig(presetKeys, mainSchemeKey=none):
    dic = lxBasic.orderedDict()
    #
    dic[(lxCore_.LynxiVariantPresetKey, lxCore_.Lynxi_Key_Plug_PresetKey, lxCore_.LynxiEnvironPresetKey)] = basicCfg.defaultVariantConfig
    key = presetKeys
    if key in dic:
        data = dic[key]
        if isinstance(data, tuple) or isinstance(data, list):
            return data
        elif isinstance(data, types.FunctionType) or isinstance(data, types.ClassType):
            # noinspection PyCallingNonCallable
            return data()
    elif not key in dic:
        if key == (
                lxCore_.LynxiSoftwarePresetKey, lxCore_.LynxiAppPresetKey, lxCore_.Lynxi_Key_Plug_PresetKey):
            return getPlugVariantLis(lxCore_.LynxiMayaPresetKey, getMayaVersions(), '')


# Schemes
def getPresetSchemes(presetKeys, mainSchemeKey=none):
    def getDefaultData():
        return basicPresetSchemeConfig(presetKeys)
    #
    def getCustomData():
        osFile = presetIndexFileMethod(presetKeys, mainSchemeKey)
        return lxBasic.readOsJson(osFile)
    #
    def getSubLis(data):
        lis = []
        if data:
            for i in data:
                schemeKey, enabled, description = i
                if enabled is True or enabled is None:
                    lis.append(schemeKey)
        return lis
    #
    def _toStringList(defaultLis, customLis):
        lis = defaultLis
        [lis.append(i) for i in customLis if i not in lis]
        return lis
    #
    return _toStringList(getSubLis(getDefaultData()), getSubLis(getCustomData()))


# Scheme Data
def getUiPresetSchemeDataDic(presetKeys, mainSchemeKey=none):
    def getDefaultData():
        return basicPresetSchemeConfig(presetKeys)
    #
    def getCustomData():
        osFile = presetIndexFileMethod(presetKeys, mainSchemeKey)
        return lxBasic.readOsJson(osFile)
    #
    def getSubDic(data):
        dic = lxBasic.orderedDict()
        if data:
            for i in data:
                scheme, enabled, description = i
                dic[scheme] = enabled, description
        return dic
    #
    def getDic(defaultDic, customDic):
        dic = lxBasic.orderedDict()
        if defaultDic:
            for k, v in defaultDic.items():
                enabled, description = v
                if k in customDic:
                    customEnabled, customDescription = customDic[k]
                    if enabled is not None:
                        enabled = customEnabled
                    description = customDescription
                dic[k] = enabled, description
        if customDic:
            for k, v in customDic.items():
                if not k in dic:
                    dic[k] = v
        elif not defaultDic:
            if customDic:
                dic = customDic
        return dic
    #
    return getDic(getSubDic(getDefaultData()), getSubDic(getCustomData()))


#
def getUiPresetSetDataLis(presetKeys, mainSchemeKey=none):
    def getDefaultData():
        return basicPresetSetConfig(presetKeys)
    #
    def getCustomData():
        osFile = presetSetFileMethod(presetKeys, mainSchemeKey)
        return lxBasic.readOsJson(osFile)
    #
    def getDic(defaultLis, customDic):
        lis = []
        if defaultLis:
            for i in defaultLis:
                setKey, uiData = i
                setUiKey = none
                if isinstance(setKey, str) or isinstance(setKey, unicode):
                    setUiKey = lxBasic.str_camelcase2prettify(setKey)
                if isinstance(setKey, tuple):
                    setKey, setUiKey = setKey
                defValue = uiData
                setValue = uiData
                if isinstance(uiData, list):
                    defValue = uiData[0]
                    setValue = uiData[0]
                if customDic:
                    if setKey in customDic:
                        setValue = customDic[setKey]
                lis.append(
                    (setKey, setUiKey, setValue, defValue, uiData)
                )
        return lis
    #
    return getDic(getDefaultData(), getCustomData())


#
def getUiSubPresetSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey):
    def getDefaultData():
        return basicPresetSetConfig((guidePresetKey, mainPresetKey, subPresetKey), mainSchemeKey)
    #
    def getCustomIndexData():
        osFile = presetIndexFileMethod((guidePresetKey, mainPresetKey, subPresetKey), mainSchemeKey)
        return lxBasic.readOsJson(osFile)
    #
    def getCustomSetData():
        osFile = presetSetFileMethod((guidePresetKey, mainPresetKey, subPresetKey), mainSchemeKey)
        return lxBasic.readOsJson(osFile)
    #
    def getDefaultIndexDic(data):
        dic = lxBasic.orderedDict()
        if data:
            for k, v in data.items():
                enabled, description, subSetDatas = v
                dic[k] = enabled, description
        return dic
    #
    def getCustomIndexDic(data):
        indexDic = lxBasic.orderedDict()
        if data:
            for i in data:
                subScheme, enabled, description = i
                indexDic[subScheme] = enabled, description
        return indexDic
    #
    def getDefaultSetDic(data):
        dic = lxBasic.orderedDict()
        if data:
            for k, v in data.items():
                subDic = lxBasic.orderedDict()
                enabled, description, subSetDatas = v
                for subSetData in subSetDatas:
                    subSetKey, subSetValue = subSetData
                    subSetUiKey = none
                    if isinstance(subSetKey, str) or isinstance(subSetKey, unicode):
                        subSetUiKey = lxBasic.str_camelcase2prettify(subSetKey)
                    if isinstance(subSetKey, tuple) or isinstance(subSetKey, list):
                        subSetKey, subSetUiKey = subSetKey
                    #
                    subDic[subSetKey] = subSetUiKey, subSetValue
                dic[k] = subDic
        return dic
    #
    def getCustomSetDic(data):
        dic = lxBasic.orderedDict()
        if data:
            for k, v in data.items():
                subDic = lxBasic.orderedDict()
                for ik, iv in v.items():
                    subDic[ik] = iv
                dic[k] = subDic
        return dic
    #
    def getUtilsIndexDic(defaultIndexDic, customIndexDic):
        dic = lxBasic.orderedDict()
        if defaultIndexDic:
            for k, v in defaultIndexDic.items():
                enabled, description = defaultIndexDic[k]
                if customIndexDic:
                    if k in customIndexDic:
                        customEnabled, customDescription = customIndexDic[k]
                        if enabled is not None:
                            enabled = customEnabled
                        description = customDescription
                dic[k] = enabled, description
        if customIndexDic:
            for k, v in customIndexDic.items():
                if not k in dic:
                    dic[k] = v
        return dic
    #
    def getSubUtilsSetLis(subDefaultSetDic, subCustomSetDic):
        lis = []
        if subDefaultSetDic:
            for k, v in subDefaultSetDic.items():
                setKey = k
                setUiKey, uiData = v
                setValue = uiData
                defValue = uiData
                if isinstance(uiData, list):
                    defValue = uiData[0]
                    setValue = uiData[0]
                if subCustomSetDic:
                    if k in subCustomSetDic:
                        setValue = subCustomSetDic[k]
                lis.append(
                    (setKey, setUiKey, setValue, defValue, uiData)
                )
        #
        elif not subDefaultSetDic:
            if subCustomSetDic:
                for k, v in subCustomSetDic.items():
                    setKey = k
                    setUiKey = lxBasic.str_camelcase2prettify(k)
                    setValue = v
                    defValue = v
                    uiData = v
                    lis.append(
                        (setKey, setUiKey, setValue, defValue, uiData)
                    )
        return lis
    #
    def getUiSetDataDic(defaultSetData, customIndexData, customSetData):
        dic = lxBasic.orderedDict()
        #
        defaultIndexDic = getDefaultIndexDic(defaultSetData)
        defaultSetDic = getDefaultSetDic(defaultSetData)
        customIndexDic = getCustomIndexDic(customIndexData)
        customSetDic = getCustomSetDic(customSetData)
        utilsIndexes = getUtilsIndexDic(defaultIndexDic, customIndexDic)
        if utilsIndexes:
            for k, v in utilsIndexes.items():
                enabled, description = v
                #
                subDefaultSetDic = lxBasic.orderedDict()
                subCustomSetDic = lxBasic.orderedDict()
                if k in defaultSetDic:
                    subDefaultSetDic = defaultSetDic[k]
                if k in customSetDic:
                    subCustomSetDic = customSetDic[k]
                #
                setLis = getSubUtilsSetLis(subDefaultSetDic, subCustomSetDic)
                dic[k] = (enabled, description), setLis
        return dic
    #
    return getUiSetDataDic(getDefaultData(), getCustomIndexData(), getCustomSetData())


#
def getPresetSetDic(presetKeys, mainSchemeKey):
    def getDefaultData():
        return basicPresetSetConfig(presetKeys)
    #
    def getCustomData():
        osFile = presetSetFileMethod(presetKeys, mainSchemeKey)
        return lxBasic.readOsJson(osFile)
    #
    def getDic(defaultLis, customDic):
        dic = lxBasic.orderedDict()
        if defaultLis:
            for i in defaultLis:
                setKey, setData = i
                if isinstance(setKey, tuple):
                    setKey, setUiKey = setKey
                setValue = setData
                if isinstance(setData, list):
                    setValue = setData[0]
                if customDic:
                    if setKey in customDic:
                        setValue = customDic[setKey]
                dic[setKey] = setValue
        return dic
    #
    return getDic(getDefaultData(), getCustomData())


#
def getGuidePresetSetValue(guidePresetKey, mainPresetKey, schemeKey):
    def getDefaultData():
        dic = lxBasic.orderedDict()
        data = basicPresetSetConfig((guidePresetKey, ))
        if data:
            for i in data:
                setKey, setData = i
                if isinstance(setKey, tuple):
                    setKey, setUiKey = setKey
                setValue = setData
                if isinstance(setData, list):
                    setValue = setData[0]
                dic[setKey] = setValue
        return dic
    #
    def getCustomData():
        osFile = presetSetFileMethod((guidePresetKey, ), schemeKey)
        return lxBasic.readOsJson(osFile)
    #
    def getValue(defaultDic, customDic):
        value = None
        if customDic:
            if mainPresetKey in defaultDic:
                if mainPresetKey in customDic:
                    value = customDic[mainPresetKey]
        elif defaultDic:
            if mainPresetKey in defaultDic:
                if mainPresetKey in defaultDic:
                    value = defaultDic[mainPresetKey]
        return value
    #
    return getValue(getDefaultData(), getCustomData())


#
def getMainPresetSetValue(guidePresetKey, mainPresetKey, schemeKey, mainSetKey):
    def getDefaultData():
        dic = lxBasic.orderedDict()
        data = basicPresetSetConfig((guidePresetKey, mainPresetKey))
        if data:
            for i in data:
                setKey, setData = i
                if isinstance(setKey, tuple):
                    setKey, setUiKey = setKey
                setValue = setData
                if isinstance(setData, list):
                    setValue = setData[0]
                dic[setKey] = setValue
        return dic
    #
    def getCustomData():
        osFile = presetSetFileMethod((guidePresetKey, mainPresetKey), schemeKey)
        return lxBasic.readOsJson(osFile)
    #
    def getValue(defaultDic, customDic):
        value = None
        if customDic:
            if mainSetKey in customDic:
                value = customDic[mainSetKey]
        elif defaultDic:
            if mainSetKey in defaultDic:
                value = defaultDic[mainSetKey]
        return value
    #
    return getValue(getDefaultData(), getCustomData())


#
def getSubPresetSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey):
    def getDefaultData():
        return basicPresetSetConfig((guidePresetKey, mainPresetKey, subPresetKey), mainSchemeKey)
    #
    def getCustomSetData():
        osFile = presetSetFileMethod((guidePresetKey, mainPresetKey, subPresetKey), mainSchemeKey)
        return lxBasic.readOsJson(osFile)
    #
    dic = lxBasic.orderedDict()
    defaultSetData = getDefaultData()
    customSetData = getCustomSetData()
    if defaultSetData:
        for setClassification, (enabled, description, setDatumLis) in defaultSetData.items():
            subCustomSetsDic = lxBasic.orderedDict()
            if customSetData:
                if setClassification in customSetData:
                    subCustomSetsDic = customSetData[setClassification]
            #
            subDic = lxBasic.orderedDict()
            for setDatum in setDatumLis:
                subSetKey, subSetValue = setDatum
                if isinstance(subSetKey, tuple):
                    subSetKey, variantUiKey = subSetKey
                #
                variantValue = subSetValue
                if not subCustomSetsDic:
                    if isinstance(subSetValue, list):
                        variantValue = subSetValue[0]
                elif subCustomSetsDic:
                    if subSetKey in subCustomSetsDic:
                        variantValue = subCustomSetsDic[subSetKey]
                subDic[subSetKey] = variantValue
            #
            dic[setClassification] = subDic
    return dic


#
def getSubPresetEnabledSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey):
    def getDefaultData():
        return basicPresetSetConfig((guidePresetKey, mainPresetKey, subPresetKey), mainSchemeKey)
    #
    def getCustomIndexData():
        osFile = presetIndexFileMethod((guidePresetKey, mainPresetKey, subPresetKey), mainSchemeKey)
        return lxBasic.readOsJson(osFile)
    #
    def getCustomSetData():
        osFile = presetSetFileMethod((guidePresetKey, mainPresetKey, subPresetKey), mainSchemeKey)
        return lxBasic.readOsJson(osFile)
    #
    def getDefaultIndexDic(data):
        dic = lxBasic.orderedDict()
        if data:
            for k, v in data.items():
                enabled, description, subSetDatas = v
                dic[k] = enabled, description
        return dic
    #
    def getCustomIndexDic(data):
        indexDic = lxBasic.orderedDict()
        if data:
            for i in data:
                subScheme, enabled, description = i
                indexDic[subScheme] = enabled, description
        return indexDic
    #
    def getUtilsIndexDic(defaultIndexDic, customIndexDic):
        dic = lxBasic.orderedDict()
        if defaultIndexDic:
            for k, v in defaultIndexDic.items():
                enabled, description = defaultIndexDic[k]
                if customIndexDic:
                    if k in customIndexDic:
                        customEnabled, customDescription = customIndexDic[k]
                        if enabled is not None:
                            enabled = customEnabled
                        description = customDescription
                dic[k] = enabled, description
        if customIndexDic:
            for k, v in customIndexDic.items():
                if not k in dic:
                    dic[k] = v
        return dic
    #
    def getSubUtilsSetLis(subDefaultSetDic, subCustomSetDic):
        dic = lxBasic.orderedDict()
        if subDefaultSetDic:
            for k, v in subDefaultSetDic.items():
                setValue = v
                if isinstance(v, list):
                    setValue = v[0]
                if subCustomSetDic:
                    if k in subCustomSetDic:
                        setValue = subCustomSetDic[k]
                dic[k] = setValue
        elif not subDefaultSetDic:
            if subCustomSetDic:
                for k, v in subCustomSetDic.items():
                    dic[k] = v
        return dic
    #
    def getDefaultSetDic(data):
        dic = lxBasic.orderedDict()
        if data:
            for k, v in data.items():
                subDic = lxBasic.orderedDict()
                enabled, description, subSetDatas = v
                for subSetData in subSetDatas:
                    subSetKey, subSetValue = subSetData
                    if isinstance(subSetKey, tuple):
                        subSetKey, subSetUiKey = subSetKey
                    subDic[subSetKey] = subSetValue
                dic[k] = subDic
        return dic
    #
    def getCustomSetDic(data):
        dic = lxBasic.orderedDict()
        if data:
            for k, v in data.items():
                subDic = lxBasic.orderedDict()
                for ik, iv in v.items():
                    subDic[ik] = iv
                dic[k] = subDic
        return dic
    #
    def getUiSetDataDic(defaultSetData, customIndexData, customSetData):
        dic = lxBasic.orderedDict()
        #
        defaultIndexDic = getDefaultIndexDic(defaultSetData)
        defaultSetDic = getDefaultSetDic(defaultSetData)
        customIndexDic = getCustomIndexDic(customIndexData)
        customSetDic = getCustomSetDic(customSetData)
        utilsIndexes = getUtilsIndexDic(defaultIndexDic, customIndexDic)
        if utilsIndexes:
            for k, v in utilsIndexes.items():
                enabled, description = v
                #
                subDefaultSetDic = lxBasic.orderedDict()
                subCustomSetDic = lxBasic.orderedDict()
                if k in defaultSetDic:
                    subDefaultSetDic = defaultSetDic[k]
                if k in customSetDic:
                    subCustomSetDic = customSetDic[k]
                #
                if enabled is True or enabled is None:
                    setDic = getSubUtilsSetLis(subDefaultSetDic, subCustomSetDic)
                    dic[k] = setDic
        return dic
    #
    return getUiSetDataDic(getDefaultData(), getCustomIndexData(), getCustomSetData())


#
def getSubPresetEnabledMainSetKeys(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey):
    def getDefaultData():
        return basicPresetSetConfig((guidePresetKey, mainPresetKey, subPresetKey), mainSchemeKey)
    #
    def getCustomIndexData():
        indexDic = lxBasic.orderedDict()
        osFile = presetIndexFileMethod((guidePresetKey, mainPresetKey, subPresetKey), mainSchemeKey)
        data = lxBasic.readOsJson(osFile)
        if data:
            for i in data:
                indexDic[i[0]] = i[1]
        return indexDic
    #
    lis = []
    defaultSetData = getDefaultData()
    customIndexData = getCustomIndexData()
    if defaultSetData:
        for mainSetKey, (enabled, description, setDatumLis) in defaultSetData.items():
            if customIndexData:
                if mainSetKey in customIndexData:
                    enabled = customIndexData[mainSetKey]
            #
            if enabled is True or enabled is None:
                lis.append(mainSetKey)
    return lis


#
def getGuidePresetVariantDic(guidePresetKey, guideSchemeKey):
    def getBranch(key):
        if key in basicVariantPresetKeys():
            mainPresetKey, subPresetKey = key[1:]
            mainPresetSchemeData = getPresetSetDic((guidePresetKey, ), guideSchemeKey)
            if mainPresetKey in mainPresetSchemeData:
                mainSchemeKey = mainPresetSchemeData[mainPresetKey]
                setData = getSubPresetSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey)
                if setData:
                    for mainSetKey, data in setData.items():
                        subDic = data
                        dic[mainSetKey] = subDic
    #
    dic = lxBasic.orderedDict()
    #
    basicData = basicPresetConfig(guidePresetKey)
    if basicData:
        [getBranch(i) for i in basicData]
    return dic


#
def setBuildBasicPresetVariants(presetVariantDic):
    lis = []
    moduleName = __name__.split('.')[-1]
    #
    for k, v in presetVariantDic.items():
        for varKey, varValue in v.items():
            command = '''global {0};{0} = {1}'''.format(varKey, varValue)
            if isinstance(varValue, str) or isinstance(varValue, unicode):
                command = '''global {0};{0} = "{1}"'''.format(varKey, varValue)
            #
            exec command
            #
            lis.append(varKey)
    return moduleName, lis


#
def getPersonnelTeamLis():
    guidePresetKey = lxCore_.LynxiPersonnelPresetKey
    mainPresetKey = lxCore_.LynxiTeamPresetKey
    return getPresetSchemes((guidePresetKey, mainPresetKey))


#
def getPersonnelPosts():
    guidePresetKey = lxCore_.LynxiPersonnelPresetKey
    mainPresetKey = lxCore_.LynxiPostPresetKey
    return getPresetSchemes((guidePresetKey, mainPresetKey))


#
def getAppNames():
    guidePresetKey = lxCore_.LynxiSoftwarePresetKey
    mainPresetKey = lxCore_.LynxiAppPresetKey
    return getPresetSchemes((guidePresetKey, mainPresetKey))


#
def getShelfNames():
    guidePresetKey = lxCore_.LynxiVariantPresetKey
    mainPresetKey = lxCore_.LynxiShelfPresetKey
    return getPresetSchemes((guidePresetKey, mainPresetKey))


#
def getToolNames():
    guidePresetKey = lxCore_.LynxiVariantPresetKey
    mainPresetKey = lxCore_.LynxiKitPresetKey
    return getPresetSchemes((guidePresetKey, mainPresetKey))


#
def getPlugNames():
    guidePresetKey = lxCore_.LynxiVariantPresetKey
    mainPresetKey = lxCore_.Lynxi_Key_Plug_PresetKey
    return getPresetSchemes((guidePresetKey, mainPresetKey))


#
def getPlugVariantLis(applicationName, appVersions, plugName):
    lis = []
    guidePresetKey = lxCore_.LynxiVariantPresetKey
    mainPresetKey = lxCore_.Lynxi_Key_Plug_PresetKey
    mainSchemeKey = plugName
    subPresetKey = lxCore_.LynxiDefinitionPresetKey
    data = getSubPresetEnabledSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey)
    if data:
        for k, v in data.items():
            if v:
                key = v[lxCore_.LynxiVariantKey]
                value = v[lxCore_.LynxiVariantValue]
                if key == lxCore_.LynxiAppNameKey:
                    value = applicationName
                if key == lxCore_.LynxiAppVersionKey:
                    value = appVersions
                if key == lxCore_.Key_Plug_Name:
                    value = getPlugNames()
                setValue = value
                defValue = value
                if isinstance(value, list):
                    setValue = value[0]
                    defValue = value[0]
                lis.append((key, setValue, defValue, value))
    return lis


#
def getMayaVersions():
    return getPresetSchemes((lxCore_.LynxiMayaPresetKey, lxCore_.LynxiVersionPresetKey))


#
def getMayaRenderer():
    guidePresetKey = lxCore_.LynxiMayaPresetKey
    mainPresetKey = lxCore_.LynxiRendererPresetKey
    return getPresetSchemes((guidePresetKey, mainPresetKey))
