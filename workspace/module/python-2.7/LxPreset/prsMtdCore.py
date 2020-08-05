# coding:utf-8
import types

from LxBasic import bscCfg, bscMtdCore, bscMethods

from LxScheme import shmOutput

from LxPreset import prsConfigure


class Mtd_PrsUtility(prsConfigure.Utility):

    @classmethod
    def root(cls):
        return u'{0}/{1}'.format(shmOutput.Root().preset.product, '.preset')

    @classmethod
    def indexFile(cls, keypath, mainSchemeKey=None):
        string = '{0}/{1}/.{2}'.format(cls.root(), cls.LynxiSchemeExt, '.'.join(keypath))
        if mainSchemeKey is not None:
            string = '{0}/{1}/{3}@.{2}'.format(cls.root(), cls.LynxiSchemeExt, '.'.join(keypath),
                                               mainSchemeKey)
        return bscMethods.OsFile.uniqueName(string)

    @classmethod
    def setFile(cls, keypath, mainSchemeKey=None):
        string = '{0}/{1}/.{2}'.format(cls.root(), cls.LynxiSetExt, '.'.join(keypath))
        if mainSchemeKey:
            string = '{0}/{1}/{3}@.{2}'.format(cls.root(), cls.LynxiSetExt, '.'.join(keypath), mainSchemeKey)
        return bscMethods.OsFile.uniqueName(string)

    @classmethod
    def _VAR_datum_scheme_project(cls):
        if bscMethods.MayaApp.isActive():
            mayaVersion = bscMethods.MayaApp.version()
            defaultValue = '{}_{}'.format(cls.VAR_value_project_default, mayaVersion)
        else:
            defaultValue = cls.VAR_value_project_default
        #
        lis = [
            [
                defaultValue,
                None,
                u'默认项目'
            ]
        ]
        return lis

    @classmethod
    def _VAR_datum_scheme_project_basic(cls):
        return [
            [
                cls.VAR_value_scheme_default,
                None,
                u'默认项目基础配置'
            ]
        ]

    @classmethod
    def _VAR_datum_scheme_project_production(cls):
        return [
            [
                cls.VAR_value_scheme_default,
                None,
                u'默认项目制作配置'
            ]
        ]

    @classmethod
    def _VAR_datum_scheme_project_inspection(cls):
        return [
            [
                cls.VAR_value_scheme_default,
                None,
                u'默认项目检查配置'
            ]
        ]

    @classmethod
    def _VAR_datum_scheme_project_storage(cls):
        return [
            [
                cls.VAR_value_scheme_default,
                None,
                u'默认项目存储配置'
            ]
        ]

    @classmethod
    def _VAR_datum_scheme_project_name(cls):
        return [
            [
                cls.VAR_value_scheme_default,
                None,
                u'默认项目命名配置'
            ]
        ]

    @classmethod
    def _VAR_datum_scheme_project_maya(cls):
        return [
            [
                cls.VAR_value_scheme_default,
                None,
                u'默认项目Maya配置'
            ]
        ]

    @classmethod
    def _VAR_datum_scheme_maya_renderer(cls):
        lis = []
        for i in cls._DEF_mya_renderer_list():
            schemeData = [
                i,
                None,
                u'渲染器',
            ]
            lis.append(schemeData)
        return lis

    @classmethod
    def _VAR_datum_scheme_maya_version(cls):
        lis = []
        for i in cls._DEF_mya_version_list():
            schemeData = [
                i,
                None,
                u'Maya版本',
            ]
            lis.append(schemeData)
        return lis

    @classmethod
    def _VAR_datum_scheme_pipeline(cls):
        return [
            [
                cls.VAR_value_pipeline_default,
                None,
                u'默认流程配置'
            ]
        ]

    @classmethod
    def _VAR_datum_scheme_pipeline_basic(cls):
        return [
            [
                cls.VAR_value_scheme_default,
                None,
                u'默认流程基础配置'
            ]
        ]

    @classmethod
    def _VAR_datum_scheme_pipeline_name(cls):
        return [
            [
                cls.VAR_value_scheme_default,
                None,
                u'默认流程命名配置'
            ]
        ]

    @classmethod
    def _VAR_datum_scheme_personnel(cls):
        lis = [
            [
                cls.VAR_value_personnel_default,
                None,
                u'默认人员配置'
            ]
        ]
        return lis

    @classmethod
    def _VAR_datum_scheme_personnel_team(cls):
        lis = []
        for team in cls._basicPersonnelTeamList():
            schemeData = [
                team,
                None,
                u'人员分组'
            ]
            lis.append(schemeData)
        return lis

    @classmethod
    def _VAR_datum_scheme_personnel_post(cls):
        lis = []
        for i in cls._basicPersonnelPostList():
            schemeData = [
                i,
                None,
                u'人员职务',
            ]
            lis.append(schemeData)
        return lis

    @classmethod
    def _VAR_datum_scheme_software(cls):
        lis = [
            [
                cls.VAR_value_software_default,
                None,
                u'默认软件配置'
            ]
        ]
        return lis

    @classmethod
    def _VAR_datum_scheme_software_application(cls):
        lis = []
        for i in cls._basicSoftwareApplicationList():
            schemeData = [
                i,
                None,
                u'软件名称',
            ]
            lis.append(schemeData)
        return lis

    @classmethod
    def _VAR_datum_scheme_maya(cls):
        lis = [
            [
                cls.VAR_value_maya_default,
                None,
                u'默认软件配置'
            ]
        ]
        return lis

    @classmethod
    def _VAR_datum_scheme_variant(cls):
        lis = [
            [
                cls.VAR_value_preset_default,
                None,
                u'默认预设配置'
            ]
        ]
        return lis

    @classmethod
    def _VAR_datum_scheme_variant_shelf(cls):
        lis = []
        for i in cls._basicVariantShelfList():
            schemeData = [
                i,
                None,
                u'工具架预设',
            ]
            lis.append(schemeData)
        return lis

    @classmethod
    def _VAR_datum_scheme_variant_shelftool(cls):
        lis = []
        for i in cls.basicAppShelfToolSchemeConfig():
            schemeData = [
                i,
                None,
                u'工具架预设',
            ]
            lis.append(schemeData)
        return lis

    @classmethod
    def _VAR_datum_scheme_variant_toolkit(cls):
        lis = []
        for i in cls.basicPresetToolSchemeConfig():
            schemeData = [
                i,
                None,
                u'工具预设',
            ]
            lis.append(schemeData)
        return lis

    @classmethod
    def _VAR_datum_scheme_variant_script(cls):
        lis = []
        for i in cls.basicPresetScriptSchemeConfig():
            schemeData = [
                i,
                None,
                u'脚本预设',
            ]
            lis.append(schemeData)
        return lis

    @classmethod
    def _VAR_datum_scheme_variant_plug(cls):
        lis = []
        for i in cls.basicAppPlugSchemeConfig():
            schemeData = [
                i,
                None,
                u'软件名称',
            ]
            lis.append(schemeData)
        return lis

    @classmethod
    def defaultVariantSchemeLis(cls):
        lis = [
            [
                cls.VAR_value_variant_default,
                None,
                u'默认变量配置'
            ]
        ]
        return lis

    # Set: Pipeline
    @classmethod
    def _VAR_datum_set_pipeline(cls):
        lis = [
            [
                cls.DEF_key_preset_basic,
                cls._getEnabledSchemes((cls.DEF_key_preset_pipeline, cls.DEF_key_preset_basic))
            ],
            [
                cls.DEF_key_preset_name,
                cls._getEnabledSchemes((cls.DEF_key_preset_pipeline, cls.DEF_key_preset_name))
            ]
        ]
        return lis

    @classmethod
    def _VAR_datum_set_pipeline_basic_development(cls):
        dic = bscMtdCore.orderedDict()
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

    @classmethod
    def _VAR_datum_set_pipeline_basic_option(cls):
        dic = bscMtdCore.orderedDict()
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
                ['scnSceneryStages', ('scenery',)],
                ['scnAssemblyStages', ('assemblyGroup',)],
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

    @classmethod
    def _VAR_datum_set_pipeline_name_basic(cls):
        dic = bscMtdCore.orderedDict()
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

    @classmethod
    def _VAR_datum_set_pipeline_name_data(cls):
        dic = bscMtdCore.orderedDict()
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

    @classmethod
    def _VAR_datum_set_pipeline_name_database(cls):
        dic = bscMtdCore.orderedDict()
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

    # Set:  Personnel
    @classmethod
    def _VAR_datum_set_personnel_post(cls):
        lis = [
            [cls.DEF_key_info_level, 0]
        ]
        return lis

    @classmethod
    def _VAR_datum_set_personnel_user(cls):
        lis = [
            [cls.DEF_key_preset_team, cls._getPersonnelTeamLis()],
            [cls.DEF_key_preset_post, cls._getPersonnelPostLis()],
            [cls.DEF_key_info_chnname, ''],
            [cls.DEF_key_info_engname, ''],
            [cls.DEF_key_info_mail, ''],
            [cls.DEF_key_info_sendmail, False]
        ]
        return lis

    @classmethod
    def _VAR_datum_set_project(cls):
        lis = [
            [
                cls.DEF_key_preset_basic,
                cls._getEnabledSchemes((cls.DEF_key_preset_project, cls.DEF_key_preset_basic))
            ],
            [
                cls.DEF_key_preset_production,
                cls._getEnabledSchemes((cls.DEF_key_preset_project, cls.DEF_key_preset_production))
            ],
            [
                cls.DEF_key_preset_inspection,
                cls._getEnabledSchemes((cls.DEF_key_preset_project, cls.DEF_key_preset_inspection))
            ],
            [
                cls.DEF_key_preset_name,
                cls._getEnabledSchemes((cls.DEF_key_preset_project, cls.DEF_key_preset_name))
            ],
            [
                cls.DEF_key_preset_storage,
                cls._getEnabledSchemes((cls.DEF_key_preset_project, cls.DEF_key_preset_storage))
            ],
            [
                cls.DEF_key_preset_maya,
                cls._getEnabledSchemes((cls.DEF_key_preset_project, cls.DEF_key_preset_maya))
            ]
        ]
        return lis

    # Set:  Variant
    @classmethod
    def _VAR_datum_set_variant_shelf(cls):
        lis = [
            ('nameText', '<shelfName>'),
            ('uiTip', '')
        ]
        return lis

    @classmethod
    def _VAR_datum_set_variant_shelftool(cls):
        lis = [
            ('shelf', cls._getVariantShelfLis()),
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

    @classmethod
    def _VAR_datum_set_variant_toolkit(cls):
        lis = [
            ('nameText', ''),
            ('uiTip', ''),
            (cls.LynxiServerPathKey,
             '<serverBasicPath>/<pipeBasicKitFolder>/<app>/<appVersion>/main/<toolName>'),
            (cls.LynxiUtilitiesPathKey,
             '<serverBasicPath>/<pipeBasicKitFolder>/<app>/<appVersion>/sub/<toolName>'),
            (cls.LynxiLocalPathKey, '<localBasicPath>/<pipeBasicKitFolder>/<app>/<appVersion>/<toolName>')
        ]
        return lis

    @classmethod
    def _VAR_datum_set_variant_script(cls):
        lis = [
            (cls.LynxiServerPathKey,
             '<serverBasicPath>/<pipeBasicScriptFolder>/<app>/<appVersion>/main/<scriptName>'),
            (cls.LynxiUtilitiesPathKey,
             '<serverBasicPath>/<pipeBasicScriptFolder>/<app>/<appVersion>/sub/<scriptName>'),
            (cls.LynxiLocalPathKey, '<localBasicPath>/<pipeBasicScriptFolder>/<app>/<appVersion>/<scriptName>')
        ]
        return lis

    @classmethod
    def _VAR_datum_set_variant_plug(cls):
        lis = [
            (cls.DEF_key_plug_loadname, ()),
            (cls.LynxiServerPathKey, '<serverBasicPath>/<pipeBasicPlugFolder>/<app>/<appVersion>/<plugName>/<plugVersion>'),
            (cls.LynxiLocalPathKey, '<localBasicPath>/<pipeBasicPlugFolder>/<app>/<appVersion>/<plugName>/<plugVersion>'),
            (cls.Lynxi_Key_Plug_Path_Deploy, '<localDirectory>/deploy'),
            (cls.Lynxi_Key_Plug_Path_Module, '<localDirectory>/module'),
            (cls.Lynxi_Key_Plug_Path_Rlm, '<localDirectory>/rlm')
        ]
        return lis

    # Set: Project
    @classmethod
    def _VAR_datum_set_project_basic(cls):
        lis = [
            [cls.DEF_key_category, cls.basicProjectClassificationConfig()],
            [cls.DEF_key_renderer, cls._getMayaRendererLis()],
            [cls.DEF_key_timeunit, cls.basicMayaTimeUnitConfig()],
            [cls.DEF_key_preset_episode, (cls.VAR_value_episode_default,)]
        ]
        return lis

    @classmethod
    def _VAR_datum_set_project_basic_option(cls):
        dic = bscMtdCore.orderedDict()
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

    @classmethod
    def _VAR_datum_set_project_production_asset(cls):
        dic = bscMtdCore.orderedDict()
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

    @classmethod
    def _VAR_datum_set_project_production_scene(cls):
        dic = bscMtdCore.orderedDict()
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

    @classmethod
    def _VAR_datum_set_project_inspection_asset(cls):
        dic = bscMtdCore.orderedDict()
        dic['astModelInspection'] = [
            None,
            u'资产 - 模型 - 检查设置',
            [
                [(k, v[1]), v[0]] for k, v in cls._DEF_project_inspection_asset_model_dict().items()
            ]
        ]
        dic['astMeshGeometryInspection'] = [
            None,
            u'资产 - 模型 - 几何 - 检查设置',
            [
                [(k, v[1]), v[0]] for k, v in cls._DEF_project_inspection_asset_model_mesh_dict().items()
            ]
        ]
        dic['astRigInspection'] = [
            None,
            u'资产 - 绑定 - 检查设置',
            [
                [(k, v[1]), v[0]] for k, v in cls._DEF_project_inspection_asset_rig_dict().items()
            ]
        ]
        dic['astShaderInspection'] = [
            None,
            u'资产 - 材质 - 检查设置',
            [
                [(k, v[1]), v[0]] for k, v in cls._DEF_project_inspection_asset_shader_dict().items()
            ]
        ]
        dic['cfxGroomInspection'] = [
            None,
            u'资产 - 角色特效 - 塑形 - 检查设置',
            [
                [(k, v[1]), v[0]] for k, v in cls._DEF_project_inspection_asset_groom_dict().items()
            ]
        ]
        return dic

    @classmethod
    def _VAR_datum_set_project_name_directory(cls):
        dic = bscMtdCore.orderedDict()
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
                ['astSolverFolder', 'solver'],
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

    @classmethod
    def _VAR_datum_set_project_name_node(cls):
        dic = bscMtdCore.orderedDict()
        dic['prefix'] = [
            None,
            u'节点前缀标签预设',
            [
                [('Lynxi_Prefix_Product_Asset', 'Asset Prefix'), 'ast'],
                [('Lynxi_Prefix_Product_scenery', 'Scenery Prefix'), 'scn'],
                [('Lynxi_Prefix_Product_scene', 'Scene Prefix'), 'sc']
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

    @classmethod
    def _VAR_datum_set_project_name_attribute(cls):
        dic = bscMtdCore.orderedDict()
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

    @classmethod
    def _VAR_datum_set_project_storage_root(cls):
        dic = bscMtdCore.orderedDict()
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
        dic[cls.LynxiServerRootKey] = [
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
        dic[cls.LynxiLocalRootKey] = [
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
        dic[cls.LynxiBackupRootKey] = [
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

    @classmethod
    def _VAR_datum_set_project_storage_file(cls):
        dic = bscMtdCore.orderedDict()
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

    @classmethod
    def _VAR_datum_set_project_maya(cls):
        lis = [
            [cls.LynxiMayaVersionKey, cls._getMayaVersionLis()],
            [cls.LynxiMayaCommonPlugsKey, cls.basicMayaCommonPlugConfig()]
        ]
        return lis

    @classmethod
    def _VAR_datum_set_project_maya_shelf(cls):
        dic = bscMtdCore.orderedDict()
        # Asset
        dic['assetShelf'] = [
            None,
            u'资产工具架预设',
            [
                ['shelfName', 'Model / Rig / CFX'],
                ['shelfIcon', 'svg_basic/asset'],
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
                ['toolIcon_', 'window/managerTool'],
                ['toolIconHover', '/shelf/managerOn.png'],
                ['toolTip', u'''提示：点击显示资产管理面板'''],
                ['toolCommand',
                 'from LxKit.qt.kitQtWidgets import ifProductWindow;w=ifProductWindow.If_QtAssetManagerWindow();w.windowShow()'],
                #
                ['helpName', 'Asset Manager Tool Help'],
                ['helpIcon', '/shelf/help.png'],
                ['helpIcon_', 'svg_basic/help'],
                ['helpIconHover', '/shelf/helpOn.png'],
                ['helpTip', u'''提示：点击显示资产管理帮助'''],
                ['helpCommand',
                 'from LxKit.qt.kitQtWidgets import ifProductWindow;w=ifProductWindow.If_QtAssetManagerWindow();w.helpShow()']
            ]
        ]
        dic['assetProductionTool'] = [
            False,
            u'资产生产工具预设',
            [
                ['shelf', 'assetShelf'],
                ['toolName', 'Asset Production'],
                ['toolIcon', '/shelf/production.png'],
                ['toolIcon_', 'window/ProductionTool'],
                ['toolIconHover', '/shelf/productionOn.png'],
                ['toolTip', u'''提示：点击显示资产生产面板'''],
                ['toolCommand', 'import LxMaya.interface.ifMaAssetProductWindow as uiPanel;uiPanel.tableShow()'],
                #
                ['helpName', 'Asset Production Tool Help'],
                ['helpIcon', '/shelf/help.png'],
                ['helpIcon_', 'svg_basic/help'],
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
                ['toolIcon_', 'svg_basic/toolkit'],
                ['toolIconHover', '/shelf/toolOn.png'],
                ['toolTip', u'''提示：点击显示资产通用工具面板'''],
                ['toolCommand',
                 'from LxKit.qt.kitQtWidgets import ifProductWindow;w=ifProductWindow.KitQtToolkitWindow();w.windowShow()'],
                #
                ['helpName', 'Asset Utilities Tool Help'],
                ['helpIcon', '/shelf/help.png'],
                ['helpIcon_', 'svg_basic/help'],
                ['helpIconHover', '/shelf/helpOn.png'],
                ['helpTip', u'''提示：点击显示资产通用工具帮助'''],
                ['helpCommand',
                 'from LxKit.qt.kitQtWidgets import ifProductWindow;w=ifProductWindow.KitQtToolkitWindow();w.helpShow()']
            ]
        ]
        dic['assetPresetTool'] = [
            None,
            u'资产预设工具预设',
            [
                ['shelf', 'assetShelf'],
                ['toolName', 'Asset Preset Tool'],
                ['toolIcon', '/shelf/preset.png'],
                ['toolIcon_', 'svg_basic/setting'],
                ['toolIconHover', '/shelf/presetOn.png'],
                ['toolTip', u'''提示：点击显示资产预设工具面板'''],
                ['toolCommand', 'import LxKit.qt.ifPresetWindow as w;w.tableShow()'],
                #
                ['helpName', 'Asset Preset Tool'],
                ['helpIcon', '/shelf/help.png'],
                ['helpIcon_', 'svg_basic/help'],
                ['helpIconHover', '/shelf/helpOn.png'],
                ['helpTip', u'''提示：点击显示资产预设工具帮助'''],
                ['helpCommand', 'import LxKit.qt.ifPresetWindow as w;w.helpShow()']
            ]
        ]
        # Scenery
        dic['sceneryShelf'] = [
            False,
            u'资产工具架预设',
            [
                ['shelfName', 'Assembly / Sce...'],
                ['shelfIcon', 'window/sceneryUnit'],
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
                ['toolIcon_', 'window/managerTool'],
                ['toolIconHover', '/shelf/managerOn.png'],
                ['toolTip', u'''提示：点击显示场景管理面板'''],
                ['toolCommand',
                 'from LxKit.qt.kitQtWidgets import ifProductWindow;w=ifProductWindow.If_QtSceneryManagerWindow();w.windowShow()'],
                #
                ['helpName', 'Scenery Manager Tool Help'],
                ['helpIcon', '/shelf/help.png'],
                ['helpIcon_', 'svg_basic/help'],
                ['helpIconHover', '/shelf/helpOn.png'],
                ['helpTip', u'''提示：点击显示场景管理帮助'''],
                ['helpCommand',
                 'from LxKit.qt.kitQtWidgets import ifProductWindow;w=ifProductWindow.If_QtSceneryManagerWindow();w.helpShow()']
            ]
        ]
        dic['sceneryProductionTool'] = [
            False,
            u'场景生产工具预设',
            [
                ['shelf', 'sceneryShelf'],
                ['toolName', 'Scenery Production Tool'],
                ['toolIcon', '/shelf/production.png'],
                ['toolIcon_', 'window/productionTool'],
                ['toolIconHover', '/shelf/productionOn.png'],
                ['toolTip', u'''提示：点击显示场景生产面板'''],
                ['toolCommand', 'import LxMaya.interface.ifMaSceneryProductWindow as uiPanel;uiPanel.tableShow()'],
                #
                ['helpName', 'Scenery Production Tool Help'],
                ['helpIcon', '/shelf/help.png'],
                ['helpIcon_', 'svg_basic/help'],
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
                ['toolIcon_', 'svg_basic/toolkit'],
                ['toolIconHover', '/shelf/toolOn.png'],
                ['toolTip', u'''提示：点击显示场景通用工具面板'''],
                ['toolCommand',
                 'from LxKit.qt.kitQtWidgets import ifProductWindow;w=ifProductWindow.KitQtToolkitWindow();w.windowShow()'],
                #
                ['helpName', 'Scenery Utilities Tool Help'],
                ['helpIcon', '/shelf/help.png'],
                ['helpIcon_', 'svg_basic/help'],
                ['helpIconHover', '/shelf/helpOn.png'],
                ['helpTip', u'''提示：点击显示场景通用工具帮助'''],
                ['helpCommand',
                 'from LxKit.qt.kitQtWidgets import ifProductWindow;w=ifProductWindow.KitQtToolkitWindow();w.helpShow()']
            ]
        ]
        dic['sceneryPresetTool'] = [
            False,
            u'场景预设工具预设',
            [
                ['shelf', 'sceneryShelf'],
                ['toolName', 'Scenery Preset Tool'],
                ['toolIcon', '/shelf/preset.png'],
                ['toolIcon_', 'svg_basic/setting'],
                ['toolIconHover', '/shelf/presetOn.png'],
                ['toolTip', u'''提示：点击显示场景预设工具面板'''],
                ['toolCommand', 'import LxKit.qt.ifPresetWindow as w;w.tableShow()'],
                #
                ['helpName', 'Scenery Preset Tool Help'],
                ['helpIcon', '/shelf/help.png'],
                ['helpIcon_', 'svg_basic/help'],
                ['helpIconHover', '/shelf/helpOn.png'],
                ['helpTip', u'''提示：点击显示场景预设工具帮助'''],
                ['helpCommand', 'import LxKit.qt.ifPresetWindow as w;w.helpShow()']
            ]
        ]
        # Scene
        dic['sceneShelf'] = [
            False,
            u'镜头工具架预设',
            [
                ['shelfName', 'Animation / Sim...'],
                ['shelfIcon', 'window/sceneUnit'],
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
                ['toolIcon_', 'window/managerTool'],
                ['toolIconHover', '/shelf/managerOn.png'],
                ['toolTip', u'''提示：点击显示镜头管理面板'''],
                ['toolCommand',
                 'from LxKit.qt.kitQtWidgets import ifProductWindow;w=ifProductWindow.If_QtSceneManagerWindow();w.windowShow()'],
                #
                ['helpName', 'Animation Manager Tool Help'],
                ['helpIcon', '/shelf/help.png'],
                ['helpIcon_', 'svg_basic/help'],
                ['helpIconHover', '/shelf/helpOn.png'],
                ['helpTip', u'''提示：点击显示镜头管理帮助'''],
                ['helpCommand',
                 'from LxKit.qt.kitQtWidgets import ifProductWindow;w=ifProductWindow.If_QtSceneManagerWindow();w.helpShow()']
            ]
        ]
        dic['sceneProductionTool'] = [
            False,
            u'镜头生产工具预设',
            [
                ['shelf', 'sceneShelf'],
                ['toolName', 'Animation Production Tool'],
                ['toolIcon', '/shelf/production.png'],
                ['toolIcon_', 'window/productionTool'],
                ['toolIconHover', '/shelf/productionOn.png'],
                ['toolTip', u'''提示：点击显示镜头生产面板'''],
                ['toolCommand',
                 'import LxMaya.interface.ifMaSceneProductWindow as table;reload(table);table.tableShow()'],
                #
                ['helpName', 'Animation Production Tool Help'],
                ['helpIcon', '/shelf/help.png'],
                ['helpIcon_', 'svg_basic/help'],
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
                ['toolIcon_', 'svg_basic/toolkit'],
                ['toolIconHover', '/shelf/toolOn.png'],
                ['toolTip', u'''提示：点击显示镜头通用工具面板'''],
                ['toolCommand',
                 'from LxKit.qt.kitQtWidgets import ifProductWindow;w=ifProductWindow.KitQtToolkitWindow();w.windowShow()'],
                #
                ['helpName', 'Animation Utilities Tool Help'],
                ['helpIcon', '/shelf/help.png'],
                ['helpIcon_', 'svg_basic/help'],
                ['helpIconHover', '/shelf/helpOn.png'],
                ['helpTip', u'''提示：点击显示镜头通用工具帮助'''],
                ['helpCommand',
                 'from LxKit.qt.kitQtWidgets import ifProductWindow;w=ifProductWindow.KitQtToolkitWindow();w.helpShow()']
            ]
        ]
        dic['scenePresetTool'] = [
            False,
            u'镜头预设工具预设',
            [
                ['shelf', 'sceneShelf'],
                ['toolName', 'Animation Preset Tool'],
                ['toolIcon', '/shelf/preset.png'],
                ['toolIcon_', 'svg_basic/setting'],
                ['toolIconHover', '/shelf/presetOn.png'],
                ['toolTip', u'''提示：点击显示镜头预设工具面板'''],
                ['toolCommand', 'import LxKit.qt.ifPresetWindow as w;w.tableShow()'],
                #
                ['helpName', 'Animation Preset Tool Help'],
                ['helpIcon', '/shelf/help.png'],
                ['helpIcon_', 'svg_basic/help'],
                ['helpIconHover', '/shelf/helpOn.png'],
                ['helpTip', u'''提示：点击显示镜头预设工具帮助'''],
                ['helpCommand', 'import LxKit.qt.ifPresetWindow as w;w.helpShow()']
            ]
        ]
        return dic

    @classmethod
    def _VAR_datum_set_project_maya_toolkit(cls):
        dic = bscMtdCore.orderedDict()
        dic['model'] = [
            True,
            u'模型工具',
            [
                ['nameText', 'Model'],
                [cls.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/model'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/model'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/tool/maya/model']
            ]
        ]
        dic['rig'] = [
            True,
            u'绑定工具',
            [
                ['nameText', 'Rig'],
                [cls.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/rig'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/rig'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/tool/maya/rig'],
            ]
        ]
        dic['cfx'] = [
            True,
            u'角色特效工具',
            [
                ['nameText', 'Character FX'],
                [cls.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/cfx'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/cfx'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/tool/maya/cfx']
            ]
        ]
        dic['scenery'] = [
            True,
            u'场景工具',
            [
                ['nameText', 'Scenery'],
                [cls.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/scenery'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/scenery'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/tool/maya/scenery']
            ]
        ]
        dic['animation'] = [
            True,
            u'动画工具',
            [
                ['nameText', 'Animation'],
                [cls.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/animation'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/animation'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/tool/maya/animation']
            ]
        ]
        dic['simulation'] = [
            True,
            u'解算工具',
            [
                ['nameText', 'Simulation'],
                [cls.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/simulation'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/simulation'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/tool/maya/simulation']
            ]
        ]
        dic['light'] = [
            True,
            u'灯光工具',
            [
                ['nameText', 'Light'],
                [cls.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/light'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/light'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/tool/maya/light']
            ]
        ]
        dic['utilities'] = [
            True,
            u'公用工具',
            [
                ['nameText', 'Utilities'],
                [cls.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/utilities'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/utilities'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/tool/maya/utilities']
            ]
        ]
        dic['td'] = [
            None,
            u'TD工具',
            [
                ['nameText', 'TD'],
                [cls.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/td'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/td'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/tool/maya/td']
            ]
        ]
        dic['rd'] = [
            None,
            u'RnD工具',
            [
                ['nameText', 'RnD'],
                [cls.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/rd'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/rd'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/tool/maya/rd']
            ]
        ]
        dic['project'] = [
            False,
            u'项目工具',
            [
                ['nameText', 'Project'],
                [cls.LynxiServerPathKey, '<serverBasicPath>/tool/maya/pipeline/<projectName>'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/tool/maya/<projectName>'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/tool/maya/<projectName>']
            ]
        ]
        return dic

    @classmethod
    def _VAR_datum_set_project_maya_script(cls):
        dic = bscMtdCore.orderedDict()
        dic['model'] = [
            False,
            u'模型脚本',
            [
                [cls.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/model'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/model'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/script/maya/model']
            ]
        ]
        dic['rig'] = [
            False,
            u'绑定脚本',
            [
                [cls.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/rig'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/rig'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/script/maya/rig'],
            ]
        ]
        dic['cfx'] = [
            False,
            u'角色特效脚本',
            [
                [cls.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/cfx'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/cfx'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/script/maya/cfx']
            ]
        ]
        dic['scenery'] = [
            False,
            u'场景脚本',
            [
                [cls.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/scenery'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/scenery'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/script/maya/scenery']
            ]
        ]
        dic['animation'] = [
            False,
            u'动画脚本',
            [
                [cls.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/animation'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/animation'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/script/maya/animation']
            ]
        ]
        dic['simulation'] = [
            False,
            u'解算脚本',
            [
                [cls.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/simulation'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/simulation'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/script/maya/simulation']
            ]
        ]
        dic['light'] = [
            False,
            u'灯光脚本',
            [
                [cls.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/light'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/light'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/script/maya/light']
            ]
        ]
        dic['utilities'] = [
            False,
            u'公用脚本',
            [
                [cls.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/utilities'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/utilities'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/script/maya/utilities']
            ]
        ]
        dic['td'] = [
            False,
            u'TD脚本',
            [
                [cls.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/td'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/td'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/script/maya/td']
            ]
        ]
        dic['rd'] = [
            False,
            u'RnD脚本',
            [
                [cls.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/rd'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/rd'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/script/maya/rd']
            ]
        ]
        dic['project'] = [
            False,
            u'项目脚本',
            [
                [cls.LynxiServerPathKey, '<serverBasicPath>/script/maya/pipeline/<projectName>'],
                [cls.LynxiUtilitiesPathKey, '<serverBasicPath>/script/maya/<projectName>'],
                [cls.LynxiLocalPathKey, '<localBasicPath>/script/maya/<projectName>']
            ]
        ]
        return dic

    @classmethod
    def _VAR_datum_set_project_maya_td(cls):
        dic = bscMtdCore.orderedDict()
        dic['model'] = [
            False,
            u'模型脚本',
            [
                [cls.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/model'],
                [cls.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/model']
            ]
        ]
        dic['rig'] = [
            False,
            u'绑定脚本',
            [
                [cls.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/rig'],
                [cls.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/rig']
            ]
        ]
        dic['cfx'] = [
            False,
            u'角色特效脚本',
            [
                [cls.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/cfx'],
                [cls.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/cfx']
            ]
        ]
        dic['solver'] = [
            False,
            u'模拟脚本',
            [
                [cls.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/solver'],
                [cls.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/solver']
            ]
        ]
        dic['scenery'] = [
            False,
            u'场景脚本',
            [
                [cls.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/scenery'],
                [cls.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/scenery']
            ]
        ]
        dic['animation'] = [
            False,
            u'动画脚本',
            [
                [cls.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/animation'],
                [cls.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/animation']
            ]
        ]
        dic['simulation'] = [
            False,
            u'解算脚本',
            [
                [cls.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/simulation'],
                [cls.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/simulation']
            ]
        ]
        dic['light'] = [
            False,
            u'灯光脚本',
            [
                [cls.LynxiMayaPackageKey, '<serverBasicPath>/td/mayaPackage/light'],
                [cls.LynxiMayaScriptKey, '<serverBasicPath>/td/mayaScript/light']
            ]
        ]
        return dic

    @classmethod
    def defaultProjectPythonPackage(cls):
        pass

    # noinspection PyUnusedLocal
    @classmethod
    def _getSchemeDatum(cls, keypath, mainSchemeKey=None):
        dic = {}
        if len(keypath) == 1:
            # Variant 01
            dic[(cls.DEF_key_preset_variant,)] = cls._VAR_datum_scheme_variant
            # Pipeline 01
            dic[(cls.DEF_key_preset_pipeline,)] = cls._VAR_datum_scheme_pipeline
            # Personnel 01
            dic[(cls.DEF_key_preset_personnel,)] = cls._VAR_datum_scheme_personnel
            # Software 01
            dic[(cls.DEF_key_preset_software,)] = cls._VAR_datum_scheme_software
            # Maya 01
            dic[(cls.DEF_key_preset_maya,)] = cls._VAR_datum_scheme_maya
            # Project 01
            dic[(cls.DEF_key_preset_project,)] = cls._VAR_datum_scheme_project
        elif len(keypath) == 2:
            # Variant 02
            dic[(cls.DEF_key_preset_variant, cls.DEF_key_preset_shelf)] = cls._VAR_datum_scheme_variant_shelf
            dic[(cls.DEF_key_preset_variant, cls.DEF_key_preset_shelftool)] = cls._VAR_datum_scheme_variant_shelftool
            dic[(cls.DEF_key_preset_variant, cls.DEF_key_preset_toolkit)] = cls._VAR_datum_scheme_variant_toolkit
            dic[(cls.DEF_key_preset_variant, cls.DEF_key_preset_script)] = cls._VAR_datum_scheme_variant_script
            dic[(cls.DEF_key_preset_variant, cls.DEF_key_preset_plug)] = cls._VAR_datum_scheme_variant_plug
            # Pipeline 02
            dic[(cls.DEF_key_preset_pipeline, cls.DEF_key_preset_basic)] = cls._VAR_datum_scheme_pipeline_basic
            dic[(cls.DEF_key_preset_pipeline, cls.DEF_key_preset_name)] = cls._VAR_datum_scheme_pipeline_name
            # Personnel 02
            dic[(cls.DEF_key_preset_personnel, cls.DEF_key_preset_team)] = cls._VAR_datum_scheme_personnel_team
            dic[(cls.DEF_key_preset_personnel, cls.DEF_key_preset_post)] = cls._VAR_datum_scheme_personnel_post
            # Software 02
            dic[(cls.DEF_key_preset_software, cls.DEF_key_preset_application)] = cls._VAR_datum_scheme_software_application
            # Maya 02
            dic[(cls.DEF_key_preset_maya, cls.DEF_key_preset_renderer)] = cls._VAR_datum_scheme_maya_renderer
            dic[(cls.DEF_key_preset_maya, cls.DEF_key_preset_version)] = cls._VAR_datum_scheme_maya_version
            # Project 02
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_basic)] = cls._VAR_datum_scheme_project_basic
            # Project 02
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_production)] = cls._VAR_datum_scheme_project_production
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_inspection)] = cls._VAR_datum_scheme_project_inspection
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_storage)] = cls._VAR_datum_scheme_project_storage
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_name)] = cls._VAR_datum_scheme_project_name
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_maya)] = cls._VAR_datum_scheme_project_maya
        key = keypath
        if key in dic:
            data = dic[key]
            if isinstance(data, tuple) or isinstance(data, list):
                return data
            elif isinstance(data, types.MethodType) or isinstance(data, types.FunctionType):
                # noinspection PyCallingNonCallable
                return data()

    # noinspection PyUnusedLocal
    @classmethod
    def _getSetDatum(cls, keypath, mainSchemeKey=None):
        dic = {}
        if len(keypath) == 1:
            # Pipeline 01
            dic[(cls.DEF_key_preset_pipeline,)] = cls._VAR_datum_set_pipeline
            # Project 01
            dic[(cls.DEF_key_preset_project,)] = cls._VAR_datum_set_project
        elif len(keypath) == 2:
            # Variant 02
            dic[(cls.DEF_key_preset_variant, cls.DEF_key_preset_shelf)] = cls._VAR_datum_set_variant_shelf
            dic[(cls.DEF_key_preset_variant, cls.DEF_key_preset_shelftool)] = cls._VAR_datum_set_variant_shelftool
            dic[(cls.DEF_key_preset_variant, cls.DEF_key_preset_toolkit)] = cls._VAR_datum_set_variant_toolkit
            dic[(cls.DEF_key_preset_variant, cls.DEF_key_preset_script)] = cls._VAR_datum_set_variant_script
            dic[(cls.DEF_key_preset_variant, cls.DEF_key_preset_plug)] = cls._VAR_datum_set_variant_plug
            # Personnel 02
            dic[(cls.DEF_key_preset_personnel, cls.DEF_key_preset_post)] = cls._VAR_datum_set_personnel_post
            dic[(cls.DEF_key_preset_personnel, cls.DEF_key_preset_user)] = cls._VAR_datum_set_personnel_user
            # Software 02
            # Maya 02
            # Project 02
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_basic)] = cls._VAR_datum_set_project_basic
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_maya)] = cls._VAR_datum_set_project_maya
        elif len(keypath) == 3:
            # Preset 03
            # Pipeline 03
            dic[(cls.DEF_key_preset_pipeline, cls.DEF_key_preset_basic, cls.DEF_key_preset_deployment)] = cls._VAR_datum_set_pipeline_basic_development
            dic[(cls.DEF_key_preset_pipeline, cls.DEF_key_preset_basic, cls.DEF_key_preset_option)] = cls._VAR_datum_set_pipeline_basic_option
            dic[(cls.DEF_key_preset_pipeline, cls.DEF_key_preset_name, cls.DEF_key_preset_basic)] = cls._VAR_datum_set_pipeline_name_basic
            dic[(cls.DEF_key_preset_pipeline, cls.DEF_key_preset_name, cls.DEF_key_preset_database)] = cls._VAR_datum_set_pipeline_name_database
            dic[(cls.DEF_key_preset_pipeline, cls.DEF_key_preset_name, cls.DEF_key_preset_data)] = cls._VAR_datum_set_pipeline_name_data
            # Software 03
            # Maya 03
            # Project 03
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_basic, cls.DEF_key_preset_option)] = cls._VAR_datum_set_project_basic_option
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_production, cls.DEF_key_preset_asset)] = cls._VAR_datum_set_project_production_asset
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_production, cls.DEF_key_preset_scene)] = cls._VAR_datum_set_project_production_scene
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_inspection, cls.DEF_key_preset_asset)] = cls._VAR_datum_set_project_inspection_asset
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_name, cls.DEF_key_preset_directory)] = cls._VAR_datum_set_project_name_directory
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_name, cls.DEF_key_preset_node)] = cls._VAR_datum_set_project_name_node
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_name, cls.DEF_key_preset_attribute)] = cls._VAR_datum_set_project_name_attribute
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_storage, cls.DEF_key_preset_root)] = cls._VAR_datum_set_project_storage_root
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_storage, cls.DEF_key_preset_file)] = cls._VAR_datum_set_project_storage_file
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_maya, cls.DEF_key_preset_shelf)] = cls._VAR_datum_set_project_maya_shelf
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_maya, cls.DEF_key_preset_toolkit)] = cls._VAR_datum_set_project_maya_toolkit
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_maya, cls.DEF_key_preset_script)] = cls._VAR_datum_set_project_maya_script
            dic[(cls.DEF_key_preset_project, cls.DEF_key_preset_maya, cls.DEF_key_preset_td)] = cls._VAR_datum_set_project_maya_td
        #
        key = keypath
        if key in dic:
            data = dic[key]
            if isinstance(data, list):
                return data
            elif isinstance(data, types.MethodType) or isinstance(data, types.FunctionType):
                # noinspection PyCallingNonCallable
                return data()
        else:
            if key == (cls.DEF_key_preset_project, cls.DEF_key_preset_maya, cls.DEF_key_preset_plug):
                return {}

    # noinspection PyUnusedLocal
    @classmethod
    def basicSubPresetSchemeConfig(cls, keypath, mainSchemeKey=None):
        dic = bscMtdCore.orderedDict()
        #
        dic[(cls.DEF_key_preset_variant, cls.DEF_key_preset_plug, cls.DEF_key_preset_environ)] = cls._defaultVariantDatum
        key = keypath
        if key in dic:
            data = dic[key]
            if isinstance(data, tuple) or isinstance(data, list):
                return data
            elif isinstance(data, types.MethodType) or isinstance(data, types.FunctionType):
                # noinspection PyCallingNonCallable
                return data()
        elif not key in dic:
            if key == (cls.DEF_key_preset_software, cls.DEF_key_preset_application, cls.DEF_key_preset_plug):
                return cls.getPlugVariantLis(cls.DEF_key_preset_maya, cls._getMayaVersionLis(), '')

    @classmethod
    def _getEnabledSchemes(cls, keypath, mainSchemeKey=None):
        def getDefFnc_():
            return cls._getSchemeDatum(keypath)

        def getVarFnc_():
            fileString_ = cls.indexFile(keypath, mainSchemeKey)
            return bscMethods.OsJsonFile.read(fileString_)

        def getSubFnc_(data):
            lis = []
            if data:
                for i in data:
                    schemeString, enable, description = i
                    if enable is True or enable is None:
                        lis.append(schemeString)
            return lis

        def reduceFnc_(defaultLis, customLis):
            lis = defaultLis
            [lis.append(i) for i in customLis if i not in lis]
            return lis

        return reduceFnc_(getSubFnc_(getDefFnc_()), getSubFnc_(getVarFnc_()))

    @classmethod
    def _getSchemeUiDatumDic(cls, keypath, mainSchemeKey=None):
        def getDefFnc_():
            return cls._getSchemeDatum(keypath)

        def getVarFnc_():
            fileString_ = cls.indexFile(keypath, mainSchemeKey)
            return bscMethods.OsJsonFile.read(fileString_)

        def getSubFnc_(data):
            dic = bscMtdCore.orderedDict()
            if data:
                for i in data:
                    schemeString, enable, description = i
                    dic[schemeString] = enable, description
            return dic

        def reduceFnc_(defDict, varDict):
            dic = bscMtdCore.orderedDict()
            if defDict:
                for k, v in defDict.items():
                    enable, description = v
                    if k in varDict:
                        varEnable, customDescription = varDict[k]
                        if enable is not None:
                            enable = varEnable
                        description = customDescription
                    dic[k] = enable, description
            if varDict:
                for k, v in varDict.items():
                    if not k in dic:
                        dic[k] = v
            elif not defDict:
                if varDict:
                    dic = varDict
            return dic

        return reduceFnc_(getSubFnc_(getDefFnc_()), getSubFnc_(getVarFnc_()))

    @classmethod
    def _getSetUiDatumList(cls, keypath, mainSchemeKey=None):
        def getDefFnc_():
            return cls._getSetDatum(keypath)

        def getVarFnc_():
            fileString_ = cls.setFile(keypath, mainSchemeKey)
            return bscMethods.OsJsonFile.read(fileString_)

        def reduceFnc_(defList, varDict):
            lis = []
            if defList:
                for i in defList:
                    keyname, datum = i
                    showname = None

                    if isinstance(keyname, str) or isinstance(keyname, unicode):
                        showname = bscMethods.StrCamelcase.toPrettify(keyname)
                    elif isinstance(keyname, tuple):
                        keyname, showname = keyname

                    defValue, varValue = datum, datum
                    if isinstance(datum, list):
                        if datum:
                            defValue, varValue = datum[0], datum[0]

                    if varDict:
                        if keyname in varDict:
                            varValue = varDict[keyname]

                    lis.append(
                        (keyname, showname, varValue, defValue, datum)
                    )
            return lis

        return reduceFnc_(getDefFnc_(), getVarFnc_())

    @classmethod
    def getUiSubPresetSetDataDic(cls, guideKeyString, mainPresetKey, subPresetKey, mainSchemeKey):
        def getDefFnc_():
            return cls._getSetDatum((guideKeyString, mainPresetKey, subPresetKey), mainSchemeKey)

        def getCustomIndexData():
            fileString_ = cls.indexFile((guideKeyString, mainPresetKey, subPresetKey), mainSchemeKey)
            return bscMethods.OsJsonFile.read(fileString_)

        def getCustomSetData():
            fileString_ = cls.setFile((guideKeyString, mainPresetKey, subPresetKey), mainSchemeKey)
            return bscMethods.OsJsonFile.read(fileString_)

        def getDefaultIndexDic(data):
            dic = bscMtdCore.orderedDict()
            if data:
                for k, v in data.items():
                    enable, description, subSetDatas = v
                    dic[k] = enable, description
            return dic

        def getCustomIndexDic(data):
            indexDic = bscMtdCore.orderedDict()
            if data:
                for i in data:
                    subScheme, enable, description = i
                    indexDic[subScheme] = enable, description
            return indexDic

        def getDefaultSetDic(data):
            dic = bscMtdCore.orderedDict()
            if data:
                for k, v in data.items():
                    subDic = bscMtdCore.orderedDict()
                    enable, description, subSetDatas = v
                    for subSetData in subSetDatas:
                        subSetKey, subSetValue = subSetData
                        subSetUiKey = None
                        if isinstance(subSetKey, str) or isinstance(subSetKey, unicode):
                            subSetUiKey = bscMethods.StrCamelcase.toPrettify(subSetKey)
                        if isinstance(subSetKey, tuple) or isinstance(subSetKey, list):
                            subSetKey, subSetUiKey = subSetKey
                        #
                        subDic[subSetKey] = subSetUiKey, subSetValue
                    dic[k] = subDic
            return dic

        def getCustomSetDic(data):
            dic = bscMtdCore.orderedDict()
            if data:
                for k, v in data.items():
                    subDic = bscMtdCore.orderedDict()
                    for ik, iv in v.items():
                        subDic[ik] = iv
                    dic[k] = subDic
            return dic

        def getUtilsIndexDic(defaultIndexDic, customIndexDic):
            dic = bscMtdCore.orderedDict()
            if defaultIndexDic:
                for k, v in defaultIndexDic.items():
                    enable, description = defaultIndexDic[k]
                    if customIndexDic:
                        if k in customIndexDic:
                            varEnable, varDescription = customIndexDic[k]
                            if enable is not None:
                                enable = varEnable
                            description = varDescription
                    dic[k] = enable, description
            if customIndexDic:
                for k, v in customIndexDic.items():
                    if not k in dic:
                        dic[k] = v
            return dic

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
                        setUiKey = bscMethods.StrCamelcase.toPrettify(k)
                        setValue = v
                        defValue = v
                        uiData = v
                        lis.append(
                            (setKey, setUiKey, setValue, defValue, uiData)
                        )
            return lis

        def getUiSetDataDic(defaultSetData, customIndexData, customSetData):
            dic = bscMtdCore.orderedDict()
            #
            defaultIndexDic = getDefaultIndexDic(defaultSetData)
            defaultSetDic = getDefaultSetDic(defaultSetData)
            customIndexDic = getCustomIndexDic(customIndexData)
            customSetDic = getCustomSetDic(customSetData)
            utilsIndexes = getUtilsIndexDic(defaultIndexDic, customIndexDic)
            if utilsIndexes:
                for k, v in utilsIndexes.items():
                    enable, description = v
                    #
                    subDefaultSetDic = bscMtdCore.orderedDict()
                    subCustomSetDic = bscMtdCore.orderedDict()
                    if k in defaultSetDic:
                        subDefaultSetDic = defaultSetDic[k]
                    if k in customSetDic:
                        subCustomSetDic = customSetDic[k]
                    #
                    setLis = getSubUtilsSetLis(subDefaultSetDic, subCustomSetDic)
                    dic[k] = (enable, description), setLis
            return dic

        return getUiSetDataDic(getDefFnc_(), getCustomIndexData(), getCustomSetData())

    @classmethod
    def getPresetSetDic(cls, keypath, mainSchemeKey):
        def getDefFnc_():
            return cls._getSetDatum(keypath)

        def getVarFnc_():
            fileString_ = cls.setFile(keypath, mainSchemeKey)
            return bscMethods.OsJsonFile.read(fileString_)

        def reduceFnc_(defList, varDict):
            dic = bscMtdCore.orderedDict()
            if defList:
                for i in defList:
                    setKey, setData = i
                    if isinstance(setKey, tuple):
                        setKey, setUiKey = setKey
                    setValue = setData
                    if isinstance(setData, list):
                        setValue = setData[0]
                    if varDict:
                        if setKey in varDict:
                            setValue = varDict[setKey]
                    dic[setKey] = setValue
            return dic

        return reduceFnc_(getDefFnc_(), getVarFnc_())

    @classmethod
    def getGuidePresetSetValue(cls, guideKeyString, mainPresetKey, schemeKey):
        def getDefFnc_():
            dic = bscMtdCore.orderedDict()
            data = cls._getSetDatum((guideKeyString,))
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
        def getVarFnc_():
            fileString_ = cls.setFile((guideKeyString,), schemeKey)
            return bscMethods.OsJsonFile.read(fileString_)
        #
        def getValue(defDict, varDict):
            value = None
            if varDict:
                if mainPresetKey in defDict:
                    if mainPresetKey in varDict:
                        value = varDict[mainPresetKey]
            elif defDict:
                if mainPresetKey in defDict:
                    if mainPresetKey in defDict:
                        value = defDict[mainPresetKey]
            return value
        #
        return getValue(getDefFnc_(), getVarFnc_())

    @classmethod
    def getMainPresetSetValue(cls, guideKeyString, mainPresetKey, schemeKey, mainSetKey):
        def getDefFnc_():
            dic = bscMtdCore.orderedDict()
            data = cls._getSetDatum((guideKeyString, mainPresetKey))
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
        def getVarFnc_():
            fileString_ = cls.setFile((guideKeyString, mainPresetKey), schemeKey)
            return bscMethods.OsJsonFile.read(fileString_)

        #
        def getValue(defDict, varDict):
            value = None
            if varDict:
                if mainSetKey in varDict:
                    value = varDict[mainSetKey]
            elif defDict:
                if mainSetKey in defDict:
                    value = defDict[mainSetKey]
            return value

        #
        return getValue(getDefFnc_(), getVarFnc_())

    @classmethod
    def getSubPresetSetDataDic(cls, guideKeyString, mainPresetKey, subPresetKey, mainSchemeKey):
        def getDefFnc_():
            return cls._getSetDatum((guideKeyString, mainPresetKey, subPresetKey), mainSchemeKey)

        #
        def getCustomSetData():
            fileString_ = cls.setFile((guideKeyString, mainPresetKey, subPresetKey), mainSchemeKey)
            return bscMethods.OsJsonFile.read(fileString_)

        #
        dic = bscMtdCore.orderedDict()
        defaultSetData = getDefFnc_()
        customSetData = getCustomSetData()
        if defaultSetData:
            for setClassification, (enable, description, setDatumLis) in defaultSetData.items():
                subCustomSetsDic = bscMtdCore.orderedDict()
                if customSetData:
                    if setClassification in customSetData:
                        subCustomSetsDic = customSetData[setClassification]
                #
                subDic = bscMtdCore.orderedDict()
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

    @classmethod
    def getSubPresetEnabledSetDataDic(cls, guideKeyString, mainPresetKey, subPresetKey, mainSchemeKey):
        def getDefFnc_():
            return cls._getSetDatum((guideKeyString, mainPresetKey, subPresetKey), mainSchemeKey)

        def getCustomIndexData():
            fileString_ = cls.indexFile((guideKeyString, mainPresetKey, subPresetKey), mainSchemeKey)
            return bscMethods.OsJsonFile.read(fileString_)

        def getCustomSetData():
            fileString_ = cls.setFile((guideKeyString, mainPresetKey, subPresetKey), mainSchemeKey)
            return bscMethods.OsJsonFile.read(fileString_)

        def getDefaultIndexDic(data):
            dic = bscMtdCore.orderedDict()
            if data:
                for k, v in data.items():
                    enable, description, subSetDatas = v
                    dic[k] = enable, description
            return dic

        def getCustomIndexDic(data):
            indexDic = bscMtdCore.orderedDict()
            if data:
                for i in data:
                    subScheme, enable, description = i
                    indexDic[subScheme] = enable, description
            return indexDic

        def getUtilsIndexDic(defaultIndexDic, customIndexDic):
            dic = bscMtdCore.orderedDict()
            if defaultIndexDic:
                for k, v in defaultIndexDic.items():
                    enable, description = defaultIndexDic[k]
                    if customIndexDic:
                        if k in customIndexDic:
                            varEnable, varDescription = customIndexDic[k]
                            if enable is not None:
                                enable = varEnable
                            description = varDescription
                    dic[k] = enable, description
            if customIndexDic:
                for k, v in customIndexDic.items():
                    if not k in dic:
                        dic[k] = v
            return dic

        def getSubUtilsSetLis(subDefaultSetDic, subCustomSetDic):
            dic = bscMtdCore.orderedDict()
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

        def getDefaultSetDic(data):
            dic = bscMtdCore.orderedDict()
            if data:
                for k, v in data.items():
                    subDic = bscMtdCore.orderedDict()
                    enable, description, subSetDatas = v
                    for subSetData in subSetDatas:
                        subSetKey, subSetValue = subSetData
                        if isinstance(subSetKey, tuple):
                            subSetKey, subSetUiKey = subSetKey
                        subDic[subSetKey] = subSetValue
                    dic[k] = subDic
            return dic

        def getCustomSetDic(data):
            dic = bscMtdCore.orderedDict()
            if data:
                for k, v in data.items():
                    subDic = bscMtdCore.orderedDict()
                    for ik, iv in v.items():
                        subDic[ik] = iv
                    dic[k] = subDic
            return dic

        def getUiSetDataDic(defaultSetData, customIndexData, customSetData):
            dic = bscMtdCore.orderedDict()
            #
            defaultIndexDic = getDefaultIndexDic(defaultSetData)
            defaultSetDic = getDefaultSetDic(defaultSetData)
            customIndexDic = getCustomIndexDic(customIndexData)
            customSetDic = getCustomSetDic(customSetData)
            utilsIndexes = getUtilsIndexDic(defaultIndexDic, customIndexDic)
            if utilsIndexes:
                for k, v in utilsIndexes.items():
                    enable, description = v
                    #
                    subDefaultSetDic = bscMtdCore.orderedDict()
                    subCustomSetDic = bscMtdCore.orderedDict()
                    if k in defaultSetDic:
                        subDefaultSetDic = defaultSetDic[k]
                    if k in customSetDic:
                        subCustomSetDic = customSetDic[k]
                    #
                    if enable is True or enable is None:
                        setDic = getSubUtilsSetLis(subDefaultSetDic, subCustomSetDic)
                        dic[k] = setDic
            return dic

        return getUiSetDataDic(getDefFnc_(), getCustomIndexData(), getCustomSetData())

    @classmethod
    def getGuidePresetVariantDic(cls, guideKeyString, guideSchemeKey):
        def getBranch(key):
            if key in cls._variantKeyPathList():
                mainPresetKey, subPresetKey = key[1:]
                mainPresetSchemeData = cls.getPresetSetDic((guideKeyString,), guideSchemeKey)
                if mainPresetKey in mainPresetSchemeData:
                    mainSchemeKey = mainPresetSchemeData[mainPresetKey]
                    setData = cls.getSubPresetSetDataDic(guideKeyString, mainPresetKey, subPresetKey, mainSchemeKey)
                    if setData:
                        for mainSetKey, data in setData.items():
                            subDic = data
                            dic[mainSetKey] = subDic

        #
        dic = bscMtdCore.orderedDict()
        #
        basicData = cls._keyTreeDict(guideKeyString)
        if basicData:
            [getBranch(i) for i in basicData]
        return dic

    @classmethod
    def getPlugVariantLis(cls, applicationName, appVersions, plugName):
        lis = []
        guideKeyString = cls.DEF_key_preset_variant
        mainPresetKey = cls.DEF_key_preset_plug
        mainSchemeKey = plugName
        subPresetKey = cls.DEF_key_preset_definition
        data = cls.getSubPresetEnabledSetDataDic(guideKeyString, mainPresetKey, subPresetKey, mainSchemeKey)
        if data:
            for k, v in data.items():
                if v:
                    key = v[cls.DEF_key]
                    value = v[cls.DEF_value]
                    if key == cls.DEF_key_application_name:
                        value = applicationName
                    if key == cls.DEF_key_application_version:
                        value = appVersions
                    if key == cls.DEF_key_plug_name:
                        value = cls._getVariantPlugLis()
                    setValue = value
                    defValue = value
                    if isinstance(value, list):
                        setValue = value[0]
                        defValue = value[0]
                    lis.append((key, setValue, defValue, value))
        return lis

    @classmethod
    def _getPersonnelTeamLis(cls):
        guideKeyString = cls.DEF_key_preset_personnel
        mainPresetKey = cls.DEF_key_preset_team
        return cls._getEnabledSchemes((guideKeyString, mainPresetKey))

    @classmethod
    def _getPersonnelPostLis(cls):
        guideKeyString = cls.DEF_key_preset_personnel
        mainPresetKey = cls.DEF_key_preset_post
        return cls._getEnabledSchemes((guideKeyString, mainPresetKey))

    @classmethod
    def _getSoftwareApplicationLis(cls):
        guideKeyString = cls.DEF_key_preset_software
        mainPresetKey = cls.DEF_key_preset_application
        return cls._getEnabledSchemes((guideKeyString, mainPresetKey))

    @classmethod
    def _getVariantShelfLis(cls):
        guideKeyString = cls.DEF_key_preset_variant
        mainPresetKey = cls.DEF_key_preset_shelf
        return cls._getEnabledSchemes((guideKeyString, mainPresetKey))

    @classmethod
    def _getVariantKitLis(cls):
        guideKeyString = cls.DEF_key_preset_variant
        mainPresetKey = cls.DEF_key_preset_toolkit
        return cls._getEnabledSchemes((guideKeyString, mainPresetKey))

    @classmethod
    def _getVariantPlugLis(cls):
        guideKeyString = cls.DEF_key_preset_variant
        mainPresetKey = cls.DEF_key_preset_plug
        return cls._getEnabledSchemes((guideKeyString, mainPresetKey))

    @classmethod
    def _getMayaVersionLis(cls):
        return cls._getEnabledSchemes((cls.DEF_key_preset_maya, cls.DEF_key_preset_version))

    @classmethod
    def _getMayaRendererLis(cls):
        guideKeyString = cls.DEF_key_preset_maya
        mainPresetKey = cls.DEF_key_preset_renderer
        return cls._getEnabledSchemes((guideKeyString, mainPresetKey))


class Mtd_PrsProduct(prsConfigure.Product):
    @classmethod
    def moduleNames(cls):
        return cls.VAR_product_module_list

    @classmethod
    def moduleShowname(cls, moduleString):
        return cls.VAR_product_module_showname_dict[moduleString][1]

    @classmethod
    def modulePrefixname(cls, moduleString):
        return cls.VAR_product_module_prefix_dict[moduleString]

    @classmethod
    def isValidModuleName(cls, moduleString):
        return moduleString in cls.VAR_product_module_list

    @classmethod
    def stepNames(cls):
        return cls.VAR_product_step_list

    @classmethod
    def stepShownamesDic(cls):
        return cls.VAR_product_step_showname_dict

    @staticmethod
    def _toProductUnitName(number):
        return 'ID{}'.format(str(number).zfill(6))

    @classmethod
    def isValidAssetCategoryName(cls, typepathString):
        return typepathString in cls.VAR_product_asset_category_list

    @classmethod
    def isValidSceneryCategoryName(cls, typepathString):
        return typepathString in cls.VAR_product_scenery_category_Lis

    @classmethod
    def isValidSceneCategoryName(cls, typepathString):
        return typepathString in cls.VAR_product_scene_category_list

    @classmethod
    def moduleCategoryNames(cls, moduleString):
        if moduleString == cls.VAR_product_module_asset:
            return cls.VAR_product_asset_category_list
        elif moduleString == cls.VAR_product_module_scenery:
            return cls.VAR_product_scenery_category_Lis
        elif moduleString == cls.VAR_product_Module_scene:
            return cls.VAR_product_scene_category_list

    @classmethod
    def moduleClassShownames(cls, moduleString):
        if moduleString == cls.VAR_product_module_asset:
            return cls.VAR_product_asset_category_showname_dict
        elif moduleString == cls.VAR_product_module_scenery:
            return cls.VAR_product_scenery_category_showname_dict
        elif moduleString == cls.VAR_product_Module_scene:
            return cls.VAR_product_scene_category_showname_dict

    @classmethod
    def _lxProductClassUiDatumDic(cls, moduleString):
        if moduleString == cls.VAR_product_module_asset:
            return cls.VAR_product_asset_category_uidatum_dict
        elif moduleString == cls.VAR_product_module_scenery:
            return cls.VAR_product_scenery_category_uidatum_dict
        elif moduleString == cls.VAR_product_Module_scene:
            return cls.VAR_product_scene_category_uidatum_dict

    @classmethod
    def _lxProductPriorityUiDatum(cls, moduleString):
        if moduleString == cls.VAR_product_module_asset:
            return cls.VAR_product_priority_uidatum_dict
        elif moduleString == cls.VAR_product_module_scenery:
            return cls.VAR_product_priority_uidatum_dict
        elif moduleString == cls.VAR_product_Module_scene:
            return cls.VAR_product_priority_uidatum_dict

    @classmethod
    def _lxProductLinkLis(cls, moduleString):
        if moduleString == cls.VAR_product_module_asset:
            return cls.VAR_product_asset_link_list
        elif moduleString == cls.VAR_product_module_scenery:
            return cls.VAR_product_scenery_link_list
        elif moduleString == cls.VAR_product_Module_scene:
            return cls.VAR_product_scene_link_list

    @classmethod
    def moduleLinkShownameDic(cls, moduleString):
        if moduleString == cls.VAR_product_module_asset:
            return cls.VAR_product_asset_link_showname_dict
        elif moduleString == cls.VAR_product_module_scenery:
            return cls.VAR_product_scenery_link_showname_dict
        elif moduleString == cls.VAR_product_Module_scene:
            return cls.VAR_product_scene_link_showname_dict

    @classmethod
    def moduleStepShownameDic(cls, moduleString):
        if moduleString == cls.VAR_product_module_asset:
            return cls.VAR_product_step_showname_dict
        elif moduleString == cls.VAR_product_module_scenery:
            return cls.VAR_product_step_showname_dict
        elif moduleString == cls.VAR_product_Module_scene:
            return cls.VAR_product_step_showname_dict

    @classmethod
    def modulePriorityShownameDic(cls, moduleString):
        if moduleString == cls.VAR_product_module_asset:
            return cls.VAR_product_priority_showname_dict
        elif moduleString == cls.VAR_product_module_scenery:
            return cls.VAR_product_priority_showname_dict
        elif moduleString == cls.VAR_product_Module_scene:
            return cls.VAR_product_priority_showname_dict

    @classmethod
    def lxDbProductUnitDefaultSetConfig(cls, projectString, moduleString, number):
        def addLinkDatum():
            linkUiDic = cls.moduleLinkShownameDic(moduleString)
            if linkUiDic:
                for k, v in linkUiDic.items():
                    lis.append(
                        [(k, u'{} [ {} ]'.format(v[1], v[0])), False]
                    )
        #
        lis = [
            [(cls.VAR_product_key_project, u'项目 [ Project(s) ]'), (projectString,)],
            [(cls.VAR_product_key_Name, u'名字 [ Name ]'), cls._toProductUnitName(number)],
            [(cls.VAR_product_key_Variant, u'变体 [ Variant(s) ]'), (bscCfg.BscUtility.DEF_Value_Default,)],
            [(cls.VAR_product_key_category, u'类型 [ Category ]'), cls._lxProductClassUiDatumDic(moduleString)],
            [(cls.VAR_product_key_priority, u'优先级 [ Priority ]'), cls._lxProductPriorityUiDatum(moduleString)]
        ]
        addLinkDatum()
        return lis

    @classmethod
    def lxProductUnitViewInfoSet(cls, moduleString, typepathString, unitViewName, extendString=None):
        unitViewClass = cls.moduleClassShownames(moduleString)[typepathString]
        if extendString is None:
            string = u'{} {}'.format(
                unitViewClass,
                unitViewName
            )
        else:
            string = u'{} {} ( {} )'.format(
                unitViewClass,
                unitViewName,
                extendString
            )
        return string

    @classmethod
    def attributeNames(cls):
        return cls.VAR_product_attribute_list

    @classmethod
    def isValidAttributeName(cls, attributeName):
        return attributeName in cls.attributeNames()

    @classmethod
    def rootLabel(cls):
        return cls.VAR_product_label_root
    
 
class Mtd_PrsAsset(prsConfigure.Product):
    @classmethod
    def prefix(cls):
        return cls.VAR_product_module_prefix_asset

    @classmethod
    def moduleName(cls):
        return cls.VAR_product_module_asset

    @classmethod
    def moduleShowname(cls):
        return cls.VAR_product_module_showname_dict[cls.VAR_product_module_asset][1]

    @classmethod
    def linkNames(cls):
        return cls.VAR_product_asset_link_list

    @classmethod
    def modelLinkName(cls):
        return cls.VAR_product_asset_link_model

    @classmethod
    def rigLinkName(cls):
        return cls.VAR_product_asset_link_rig

    @classmethod
    def groomLinkName(cls):
        return cls.VAR_product_asset_link_groom

    @classmethod
    def solverLinkName(cls):
        return cls.VAR_product_asset_link_solver

    @classmethod
    def lightLinkName(cls):
        return cls.VAR_product_asset_link_light

    @classmethod
    def assemblyLinkName(cls):
        return cls.VAR_product_asset_link_assembly
    
    @classmethod
    def isModelStageName(cls, stageString):
        if stageString in cls.VAR_product_asset_model_stage_list or stageString == cls.VAR_product_asset_link_model:
            return True
        return False

    @classmethod
    def isRigStageName(cls, stageString):
        if stageString in cls.VAR_product_asset_rig_stage_list or stageString == cls.VAR_product_asset_link_rig:
            return True
        return False

    @classmethod
    def isGroomStageName(cls, stageString):
        if stageString in cls.VAR_product_asset_groom_stage_list or stageString == cls.VAR_product_asset_link_groom:
            return True
        return False

    @classmethod
    def isSolverStageName(cls, stageString):
        if stageString in cls.VAR_product_asset_solver_stage_list or stageString == cls.VAR_product_asset_link_solver:
            return True
        return False

    @classmethod
    def isLightStageName(cls, stageString):
        if stageString in cls.VAR_product_scene_light_stage_list or stageString == cls.VAR_product_asset_link_light:
            return True
        return False

    @classmethod
    def isAssemblyStageName(cls, stageString):
        if stageString in cls.VAR_product_asset_assembly_stage_list or stageString == cls.VAR_product_asset_link_assembly:
            return True
        return False

    @classmethod
    def isValidStageName(cls, stageString):
        if cls.isModelStageName(stageString):
            return True
        elif cls.isRigStageName(stageString):
            return True
        elif cls.isGroomStageName(stageString):
            return True
        elif cls.isSolverStageName(stageString):
            return True
        elif cls.isLightStageName(stageString):
            return True
        return False
    
    @classmethod
    def stageName2linkName(cls, stageString):
        if cls.isModelStageName(stageString):
            return cls.VAR_product_asset_link_model
        elif cls.isRigStageName(stageString):
            return cls.VAR_product_asset_link_rig
        elif cls.isGroomStageName(stageString):
            return cls.VAR_product_asset_link_groom
        elif cls.isSolverStageName(stageString):
            return cls.VAR_product_asset_link_solver
        elif cls.isLightStageName(stageString):
            return cls.VAR_product_asset_link_light
        return cls.VAR_product_asset_link_model
    
    @classmethod
    def categories(cls):
        return cls.VAR_product_asset_category_list
    
    @classmethod
    def isValidCategory(cls, categoryName):
        return categoryName in cls.categories()

    @classmethod
    def isCharacterCategory(cls, categoryName):
        return categoryName == cls.VAR_product_asset_category_character

    @classmethod
    def characterCategory(cls):
        return cls.VAR_product_asset_category_character

    @classmethod
    def isPropCategory(cls, categoryName):
        return categoryName == cls.VAR_product_asset_category_prop

    @classmethod
    def propCategory(cls):
        return cls.VAR_product_asset_category_prop

    @classmethod
    def assemblyCategoryName(cls):
        return cls.VAR_product_scenery_category_Assembly
    
    @classmethod
    def categoryShowname(cls, typepathString):
        return cls.VAR_product_asset_category_showname_dict[typepathString][1]
    
    @classmethod
    def linkShowname(cls, linkString):
        return cls.VAR_product_asset_link_showname_dict[linkString][1]
    
    @classmethod
    def linkShowname_(cls, stageString):
        return cls.linkShowname(cls.stageName2linkName(stageString))

    @classmethod
    def classShownameDic(cls):
        return cls.VAR_product_asset_category_uidatum_dict

    @classmethod
    def priorityNames(cls):
        return cls.VAR_product_priority_list


class Mtd_PrsScenery(prsConfigure.Product):
    @classmethod
    def prefix(cls):
        return cls.VAR_product_module_prefix_scenery

    @classmethod
    def moduleName(cls):
        return cls.VAR_product_module_scenery

    @classmethod
    def moduleShowname(cls):
        return cls.VAR_product_module_showname_dict[cls.VAR_product_module_scenery][1]

    @classmethod
    def linkNames(cls):
        return cls.VAR_product_scenery_link_list

    @classmethod
    def assemblyLinkName(cls):
        return cls.VAR_product_scenery_link_assembly

    @classmethod
    def layoutLinkName(cls):
        return cls.VAR_product_scenery_link_layout

    @classmethod
    def animationLinkName(cls):
        return cls.VAR_product_scenery_link_animation

    @classmethod
    def solverLinkName(cls):
        return cls.VAR_product_scenery_link_solver

    @classmethod
    def simulationLinkName(cls):
        return cls.VAR_product_scenery_link_simulation

    @classmethod
    def lightLinkName(cls):
        return cls.VAR_product_scenery_link_light

    @classmethod
    def categoryShowname(cls, typepathString):
        return cls.VAR_product_scenery_category_showname_dict[typepathString][1]

    @classmethod
    def isSceneryLinkName(cls, stageString):
        if stageString in cls.VAR_product_scenery_assembly_stage_list or stageString == cls.VAR_product_scenery_link_assembly:
            return True
        return False

    @classmethod
    def isLayoutLinkName(cls, stageString):
        if stageString in cls.VAR_product_scenery_layout_stage_list or stageString == cls.VAR_product_scene_link_layout:
            return True
        return False

    @classmethod
    def isAnimationLinkName(cls, stageString):
        if stageString in cls.VAR_product_scene_animation_stage_list or stageString == cls.VAR_product_scene_link_animation:
            return True
        return False

    @classmethod
    def isSolverLinkName(cls, stageString):
        if stageString in cls.VAR_product_scene_solver_stage_list or stageString == cls.VAR_product_scene_link_solver:
            return True
        return False

    @classmethod
    def isSimulationLinkName(cls, stageString):
        if stageString in cls.VAR_product_scene_simulation_stage_list or stageString == cls.VAR_product_scene_link_simulation:
            return True
        return False

    @classmethod
    def isLightLinkName(cls, stageString):
        if stageString in cls.VAR_product_scene_light_stage_list or stageString == cls.VAR_product_scene_link_light:
            return True
        return False

    @classmethod
    def stageName2linkName(cls, stageString):
        if cls.isSceneryLinkName(stageString):
            return cls.VAR_product_scenery_link_assembly
        elif cls.isLayoutLinkName(stageString):
            return cls.VAR_product_scenery_link_layout
        elif cls.isAnimationLinkName(stageString):
            return cls.VAR_product_scenery_link_animation
        elif cls.isSolverLinkName(stageString):
            return cls.VAR_product_scenery_link_solver
        elif cls.isSimulationLinkName(stageString):
            return cls.VAR_product_scenery_link_simulation
        elif cls.isLightLinkName(stageString):
            return cls.VAR_product_scenery_link_light
        return cls.VAR_product_scenery_link_assembly

    @classmethod
    def categories(cls):
        return cls.VAR_product_scenery_category_Lis

    @classmethod
    def isValidCategory(cls, categoryName):
        return categoryName in cls.categories()
    
    @classmethod
    def linkShowname(cls, linkString):
        return cls.VAR_product_scenery_link_showname_dict[linkString][1]
    
    @classmethod
    def linkShowname_(cls, stageString):
        return cls.linkShowname(cls.stageName2linkName(stageString))

    @classmethod
    def classShownameDic(cls):
        return cls.VAR_product_scenery_category_uidatum_dict

    @classmethod
    def priorityNames(cls):
        return cls.VAR_product_priority_list
    

class Mtd_PrsScene(prsConfigure.Product):
    @classmethod
    def prefix(cls):
        return cls.VAR_product_module_prefix_scene

    @classmethod
    def moduleName(cls):
        return cls.VAR_product_Module_scene

    @classmethod
    def moduleShowname(cls):
        return cls.VAR_product_module_showname_dict[cls.VAR_product_Module_scene][1]

    @classmethod
    def linkNames(cls):
        return cls.VAR_product_scene_link_list

    @classmethod
    def layoutLinkName(cls):
        return cls.VAR_product_scene_link_layout

    @classmethod
    def animationLinkName(cls):
        return cls.VAR_product_scene_link_animation

    @classmethod
    def solverLinkName(cls):
        return cls.VAR_product_scene_link_solver

    @classmethod
    def simulationLinkName(cls):
        return cls.VAR_product_scene_link_simulation

    @classmethod
    def lightLinkName(cls):
        return cls.VAR_product_scene_link_light
    
    @classmethod
    def categoryShowname(cls, typepathString):
        return cls.VAR_product_scene_category_showname_dict[typepathString][1]

    @classmethod
    def isLayoutLinkName(cls, sceneStage):
        if sceneStage in cls.VAR_product_scenery_layout_stage_list or sceneStage == cls.VAR_product_scene_link_layout:
            return True
        return False

    @classmethod
    def isAnimationLinkName(cls, sceneStage):
        if sceneStage in cls.VAR_product_scene_animation_stage_list or sceneStage == cls.VAR_product_scene_link_animation:
            return True
        return False

    @classmethod
    def isSolverLinkName(cls, sceneStage):
        if sceneStage in cls.VAR_product_scene_solver_stage_list or sceneStage == cls.VAR_product_scene_link_solver:
            return True
        return False

    @classmethod
    def isSimulationLinkName(cls, sceneStage):
        if sceneStage in cls.VAR_product_scene_simulation_stage_list or sceneStage == cls.VAR_product_scene_link_simulation:
            return True
        return False

    @classmethod
    def isLightLinkName(cls, sceneStage):
        if sceneStage in cls.VAR_product_scene_light_stage_list or sceneStage == cls.VAR_product_scene_link_light:
            return True
        return False

    @classmethod
    def stageName2linkName(cls, sceneStage):
        if cls.isLayoutLinkName(sceneStage):
            return cls.VAR_product_scene_link_layout
        elif cls.isAnimationLinkName(sceneStage):
            return cls.VAR_product_scene_link_animation
        elif cls.isSolverLinkName(sceneStage):
            return cls.VAR_product_scene_link_solver
        elif cls.isSimulationLinkName(sceneStage):
            return cls.VAR_product_scene_link_simulation
        elif cls.isLightLinkName(sceneStage):
            return cls.VAR_product_scene_link_light
        return cls.VAR_product_scene_link_layout
    
    @classmethod
    def categories(cls):
        return cls.VAR_product_scene_category_list

    @classmethod
    def isValidCategory(cls, categoryName):
        return categoryName in cls.categories()

    @classmethod
    def linkShowname(cls, linkString):
        return cls.VAR_product_scene_link_showname_dict[linkString][1]

    @classmethod
    def linkShowname_(cls, stageString):
        return cls.linkShowname(cls.stageName2linkName(stageString))

    @classmethod
    def classShownameDic(cls):
        return cls.VAR_product_scene_category_uidatum_dict

    @classmethod
    def priorityNames(cls):
        return cls.VAR_product_priority_list
