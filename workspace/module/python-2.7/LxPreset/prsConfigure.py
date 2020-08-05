# coding:utf-8
from LxBasic import bscMtdCore, bscMethods

VAR_path_database = {
    'basic': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}',
    'assetIndexSub': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIndexSubKey}',
    'assetNurbscurveSub': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbNurbsCurveSubKey}',
    'assetGraphSub': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbGraphSubKey}',
    'assetMeshSub': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbMeshSubKey}',
    'assetProductSub': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIntegrationSubKey}',
    'assetGeometrySub': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbGeometrySubKey}',
    'assetMaterialSub': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbMaterialSubKey}',
    'assetFurSub': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbSubFurKey}',
    'assetAovSub': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbAovSubKey}',
    'assetRecordSub': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbRecordSubKey}',
    'assetPictureSub': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbPictureSubKey}',
    'assetGroomProduct': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIntegrationSubKey}/{dbCfxLinkUnitKey}',
    'assetRigProduct': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIntegrationSubKey}/{dbRigLinkUnitKey}',
    'sceneryHistory': '{dbAssetRoot}/{dbBasicFolderName}/{dbSceneryBasicKey}/{dbRecordSubKey}/{dbHistoryUnitKey}',
    'assetMaterialObjectSet': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbMaterialSubKey}/{dbObjectSetUnitKey}',
    'assetAssemblyIndex': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIndexSubKey}/{dbAssemblyUnitKey}',
    'assetVariantIndex': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIndexSubKey}/{dbVariantUnitKey}',
    'assetModelProduct': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIntegrationSubKey}/{dbModelLinkUnitKey}',
    'assetGeometryTransform': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbGeometrySubKey}/{dbTransformUnitKey}',
    'sceneryPreview': '{dbAssetRoot}/{dbBasicFolderName}/{dbSceneryBasicKey}/{dbPictureSubKey}/{dbPreviewUnitKey}',
    'assetHistory': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbRecordSubKey}/{dbHistoryUnitKey}',
    'sceneryBasic': '{dbAssetRoot}/{dbBasicFolderName}/{dbSceneryBasicKey}',
    'assetGeometryTopology': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbGeometrySubKey}/{dbGeomTopoUnitKey}',
    'assetGraphIndex': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIndexSubKey}/{dbGraphUnitKey}',
    'assetNurbsSurfaceIndex': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIndexSubKey}/{dbNurbsSurfaceUnitKey}',
    'assetMeshProduct': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIntegrationSubKey}/{dbMeshUnitKey}',
    'assetGeometryShape': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbGeometrySubKey}/{dbGeomShapeUnitKey}',
    'assetMaterialAttribute': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbMaterialSubKey}/{dbAttributeUnitKey}',
    'assetNurbsCurveTransform': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbNurbsCurveSubKey}/{dbTransformUnitKey}',
    'assetGeometryConstantIndex': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIndexSubKey}/{dbContrastUnitKey}',
    'assetNurbsCurveIndex': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIndexSubKey}/{dbNurbsCurveUnitKey}',
    'assetFilterIndex': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIndexSubKey}/{dbFilterUnitKey}',
    'assetGeometryIndex': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIndexSubKey}/{dbGeometryUnitKey}',
    'assetAovNode': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbAovSubKey}/{dbNodeUnitKey}',
    'assetNameIndex': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIndexSubKey}/{dbNameUnitKey}',
    'assetNurbsCurveTopology': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbNurbsCurveSubKey}/{dbGeomTopoUnitKey}',
    'assetMaterialNode': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbMaterialSubKey}/{dbNodeUnitKey}',
    'assetGraphGeometry': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbGraphSubKey}/{dbGeometryUnitKey}',
    'assetTextureIndex': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIndexSubKey}/{dbTextureUnitKey}',
    'assetNurbsCurveShape': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbNurbsCurveSubKey}/{dbGeomShapeUnitKey}',
    'assetPreview': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbPictureSubKey}/{dbPreviewUnitKey}',
    'assetGeometryEdgeSmooth': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbGeometrySubKey}/{dbEdgeSmoothUnitKey}',
    'assetFurProduct': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIntegrationSubKey}/{dbFurUnitKey}',
    'assetGeometryVertexNormal': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbGeometrySubKey}/{dbVertexNormalUnitKey}',
    'assetGraphNode': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbGraphSubKey}/{dbNodeUnitKey}',
    'assetAovRelation': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbAovSubKey}/{dbRelationUnitKey}',
    'assetSolverProduct': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIntegrationSubKey}/{dbSolverLinkUnitKey}',
    'assetFurPath': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbSubFurKey}/{dbPathUnitKey}',
    'assetMap': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbPictureSubKey}/{dbMapUnitKey}',
    'assetMaterialObject': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbMaterialSubKey}/{dbObjectUnitKey}',
    'assetGraphRelation': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbGraphSubKey}/{dbRelationUnitKey}',
    'assetAovIndex': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIndexSubKey}/{dbAovUnitKey}',
    'assetTexture': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbPictureSubKey}/{dbTextureUnitKey}',
    'assetGeometryMap': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbGeometrySubKey}/{dbMapUnitKey}',
    'assetFurIndex': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIndexSubKey}/{dbFurUnitKey}',
    'assetMaterialRelation': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbMaterialSubKey}/{dbRelationUnitKey}',
    'assetMaterialIndex': '{dbAssetRoot}/{dbBasicFolderName}/{dbAssetBasicKey}/{dbIndexSubKey}/{dbMaterialUnitKey}',

    'sceneryIndexSub': '{dbAssetRoot}/{dbBasicFolderName}/{dbSceneryBasicKey}/{dbIndexSubKey}',
    'sceneryRecordSub': '{dbAssetRoot}/{dbBasicFolderName}/{dbSceneryBasicKey}/{dbRecordSubKey}',
    'sceneryPictureSub': '{dbAssetRoot}/{dbBasicFolderName}/{dbSceneryBasicKey}/{dbPictureSubKey}'
}

VAR_path_asset = {
    'basic': '{basicAssetFolder}/{basicUnitFolder}',
    'model': '{basicAssetFolder}/{basicUnitFolder}/{asset.variant}',
    'rig': '{basicAssetFolder}/{basicUnitFolder}',
    'groom': '{basicAssetFolder}/{basicUnitFolder}/{asset.variant}',
    'solver': '{basicAssetFolder}/{basicUnitFolder}/{asset.variant}/{astSolverFolder}',
    'light': '{basicAssetFolder}/{basicUnitFolder}/{asset.variant}/{astLightFolder}',
}


class Utility(object):
    DEF_key_preset = 'preset'
    DEF_key_preset_pipeline = 'pipeline'
    DEF_key_preset_variant = 'variant'
    DEF_key_preset_personnel = 'personnel'
    DEF_key_preset_software = 'software'
    DEF_key_preset_maya = 'maya'
    DEF_key_preset_project = 'project'
    DEF_key_preset_basic = 'basic'
    DEF_key_preset_deployment = 'deployment'
    DEF_key_preset_environ = 'environ'
    DEF_key_preset_set = 'set'
    DEF_key_preset_production = 'production'
    DEF_key_preset_inspection = 'inspection'
    DEF_key_preset_preference = 'preference'
    DEF_key_preset_option = 'option'
    DEF_key_preset_asset = 'asset'
    DEF_key_preset_scenery = 'scenery'
    DEF_key_preset_scene = 'scene'
    DEF_key_preset_definition = 'definition'
    DEF_key_preset_team = 'team'
    DEF_key_preset_post = 'post'
    DEF_key_preset_user = 'user'
    DEF_key_preset_storage = 'storage'
    DEF_key_preset_root = 'root'
    DEF_key_preset_file = 'file'
    DEF_key_preset_name = 'name'
    DEF_key_preset_data = 'data'
    DEF_key_preset_database = 'database'
    DEF_key_preset_directory = 'directory'
    DEF_key_preset_node = 'node'
    DEF_key_preset_attribute = 'attribute'
    DEF_key_preset_customization = 'customization'
    DEF_key_preset_shelf = 'shelf'
    DEF_key_preset_shelftool = 'shelftool'
    DEF_key_preset_toolkit = 'toolkit'
    DEF_key_preset_application = 'application'
    DEF_key_preset_plug = 'plug'
    DEF_key_preset_renderer = 'renderer'
    DEF_key_preset_version = 'version'
    DEF_key_preset_script = 'script'
    DEF_key_preset_td = 'td'
    DEF_value_preset_unspecified = 'unspecified'

    VAR_value_preset_general = 'general'
    VAR_value_preset_default = 'default_preset'
    VAR_value_pipeline_default = 'default_pipeline'
    VAR_value_variant_default = 'default_variant'
    VAR_value_personnel_default = 'default_personnel'
    VAR_value_software_default = 'default_software'
    VAR_value_maya_default = 'default_maya'
    VAR_value_project_default = 'default_project'
    LynxiDefaultProjectValue = 'default_project_2017'
    VAR_value_scheme_default = 'default_scheme'

    DEF_key_info_team = 'team'
    DEF_key_info_post = 'post'
    DEF_key_info_level = 'level'
    DEF_key_info_engname = 'engname'
    DEF_key_info_chnname = 'chnname'
    DEF_key_info_mail = 'mail'
    DEF_key_info_sendmail = 'sendmail'

    DEF_key_preset_episode = 'episode'
    VAR_value_episode_default = '001A'
    DEF_key_timeunit = 'timeunit'
    VAR_value_timeunit_default = '24fps'
    DEF_key_category = 'category'
    DEF_key_category_project_film = 'film'
    DEF_key_category_project_cg = 'cg'
    DEF_key_category_project_game = 'game'

    DEF_key_application_name = 'appname'
    DEF_key_application_version = 'appversion'
    DEF_key_shelf_name = 'shelfname'
    DEF_key_tool_name = 'toolname'
    LynxiScriptNameKey = 'scriptName'

    DEF_key_plug_name = 'plugname'
    DEF_key_plug_version = 'plugversion'
    DEF_key_plug_loadname = 'loadname'
    DEF_key_plug_autoload = 'autoload'
    DEF_key_plug_setupcommand = 'setupcommand'
    Lynxi_Key_Plug_Path_Deploy = 'plugDeployPath'
    Lynxi_Key_Plug_Path_Module = 'plugModulePath'
    Lynxi_Key_Plug_Path_Rlm = 'plugRlmPath'

    DEF_key = 'key'
    DEF_value = 'value'
    LynxiUiNameKey = 'nameText'
    LynxiUiTipKey = 'uiTip'
    LynxiServerPathKey = 'serverDirectory'
    LynxiUtilitiesPathKey = 'utilitiesPath'
    LynxiLocalPathKey = 'localDirectory'
    LynxiServerRootKey = 'serverRoot'
    LynxiLocalRootKey = 'localRoot'
    LynxiBackupRootKey = 'backupRoot'
    LynxiMayaPackageKey = 'mayaPackage'
    LynxiMayaScriptKey = 'mayaScript'
    LynxiAssetUploadCommandKey = 'assetUploadCmd'
    LynxiAssetLoadCommandKey = 'assetLoadCmd'
    LynxiSceneUploadCommandKey = 'sceneUploadCmd'
    LynxiSceneLoadCommandKey = 'sceneLoadCmd'
    LynxiMayaVersionKey = 'mayaVersion'
    LynxiDefaultMayaVersion = '2017'
    LynxiMayaCommonPlugsKey = 'mayaCommonPlugs'

    DEF_key_renderer = 'renderer'
    DEF_value_renderer_software = 'software'
    DEF_value_renderer_hardware = 'hardware'
    DEF_value_renderer_arnold = 'arnold'
    DEF_value_renderer_redshift = 'redshift'
    LynxiMayaPlugPresetKey = 'mayaPlug'
    LynxiSchemeExt = '.index'
    LynxiSetExt = '.set'
    LynxiUiPathsep = ' > '
    DEF_value_root_server = 0
    DEF_value_root_local = 1
    DEF_value_root_backup = 2

    Lynxi_Name_Td_Lis = [
        'dongchangbao',
        'changbao.dong',
        'nothings'
    ]

    LynxiPipelineTdPost = 'Pipeline - TD'
    LynxiPipelineTdLevel = 3
    pipelineTdBasicPaths = [
        'E:/myworkspace/td/lynxi'
    ]

    astHierarchyKey = 'hierarchy'
    astGeometryKey = 'geometry'
    astGeomShapeKey = 'geometryShape'
    astMapKey = 'map'
    astMapShapeKey = 'mapShape'

    @classmethod
    def _defaultSchemeDatum(cls):
        lis = [
            True,
            u'请输入备注'
        ]
        return lis

    @classmethod
    def _defaultSetDatum(cls, setDatumLis=None):
        if setDatumLis is None:
            setDatumLis = []

        lis = [
            (True, u'请输入备注'),
            setDatumLis
        ]
        return lis

    @classmethod
    def _keyTreeDict(cls, guideKeyString):
        dic = bscMtdCore.orderedDict()
        # Variant
        dic[cls.DEF_key_preset_variant] = [
            (cls.DEF_key_preset_variant,),
            #
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_shelf),
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_shelf, cls.DEF_key_preset_definition),
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_shelftool),
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_shelftool, cls.DEF_key_preset_definition),
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_toolkit),
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_toolkit, cls.DEF_key_preset_definition),
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_script),
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_script, cls.DEF_key_preset_definition),
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_plug),
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_plug, cls.DEF_key_preset_definition),
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_plug, cls.DEF_key_preset_environ)
        ]
        # Pipeline
        dic[cls.DEF_key_preset_pipeline] = [
            (cls.DEF_key_preset_pipeline,),
            #
            (cls.DEF_key_preset_pipeline, cls.DEF_key_preset_basic),
            (cls.DEF_key_preset_pipeline, cls.DEF_key_preset_basic, cls.DEF_key_preset_deployment),
            (cls.DEF_key_preset_pipeline, cls.DEF_key_preset_basic, cls.DEF_key_preset_option),
            (cls.DEF_key_preset_pipeline, cls.DEF_key_preset_name),
            (cls.DEF_key_preset_pipeline, cls.DEF_key_preset_name, cls.DEF_key_preset_basic),
            (cls.DEF_key_preset_pipeline, cls.DEF_key_preset_name, cls.DEF_key_preset_data),
            (cls.DEF_key_preset_pipeline, cls.DEF_key_preset_name, cls.DEF_key_preset_database)
        ]
        # Software
        dic[cls.DEF_key_preset_software] = [
            (cls.DEF_key_preset_software,),
            #
            (cls.DEF_key_preset_software, cls.DEF_key_preset_application),
            (cls.DEF_key_preset_software, cls.DEF_key_preset_application, cls.DEF_key_preset_plug)
        ]
        # Maya
        dic[cls.DEF_key_preset_maya] = [
            (cls.DEF_key_preset_maya,),
            #
            (cls.DEF_key_preset_maya, cls.DEF_key_preset_version),
            (cls.DEF_key_preset_maya, cls.DEF_key_preset_renderer),
        ]
        # Project
        dic[cls.DEF_key_preset_project] = [
            # Project
            (cls.DEF_key_preset_project,),
            # Project > Basic
            (cls.DEF_key_preset_project, cls.DEF_key_preset_basic),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_basic, cls.DEF_key_preset_option),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_basic,
             cls.DEF_key_preset_definition),
            # Project > Production
            (cls.DEF_key_preset_project, cls.DEF_key_preset_production),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_production,
             cls.DEF_key_preset_asset),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_production,
             cls.DEF_key_preset_scene),
            # Project > Inspection
            (cls.DEF_key_preset_project, cls.DEF_key_preset_inspection),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_inspection,
             cls.DEF_key_preset_asset),
            #
            (cls.DEF_key_preset_project, cls.DEF_key_preset_name),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_name, cls.DEF_key_preset_directory),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_name, cls.DEF_key_preset_node),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_name, cls.DEF_key_preset_attribute),
            #
            (cls.DEF_key_preset_project, cls.DEF_key_preset_storage),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_storage, cls.DEF_key_preset_root),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_storage, cls.DEF_key_preset_file),
            #
            (cls.DEF_key_preset_project, cls.DEF_key_preset_maya),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_maya, cls.DEF_key_preset_shelf),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_maya, cls.DEF_key_preset_toolkit),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_maya, cls.DEF_key_preset_script),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_maya, cls.DEF_key_preset_td),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_maya, cls.DEF_key_preset_plug)
        ]
        # Personnel
        dic[cls.DEF_key_preset_personnel] = [
            (cls.DEF_key_preset_personnel,),
            #
            (cls.DEF_key_preset_personnel, cls.DEF_key_preset_team),
            (cls.DEF_key_preset_personnel, cls.DEF_key_preset_post),
            (cls.DEF_key_preset_personnel, cls.DEF_key_preset_user)
        ]

        key = guideKeyString
        if key in dic:
            return dic[key]

    @classmethod
    def _mainKeyPathList(cls):
        lis = [
            # Variant
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_shelf),
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_shelftool),
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_shelftool),
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_toolkit),
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_script),
            (cls.DEF_key_preset_variant, cls.DEF_key_preset_plug),
            # Pipeline
            (cls.DEF_key_preset_pipeline, cls.DEF_key_preset_basic),
            (cls.DEF_key_preset_pipeline, cls.DEF_key_preset_name),
            # Software
            (cls.DEF_key_preset_software, cls.DEF_key_preset_application),
            # Maya
            # Project > Basic
            (cls.DEF_key_preset_project, cls.DEF_key_preset_basic),
            # Project > Production
            (cls.DEF_key_preset_project, cls.DEF_key_preset_production),
            # Project > Inspection
            (cls.DEF_key_preset_project, cls.DEF_key_preset_inspection),
            # Project > Name
            (cls.DEF_key_preset_project, cls.DEF_key_preset_name),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_storage),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_maya)
        ]
        return lis

    @classmethod
    def _variantKeyPathList(cls):
        lis = [
            # Variant
            # Pipeline
            (cls.DEF_key_preset_pipeline, cls.DEF_key_preset_basic, cls.DEF_key_preset_deployment),
            (cls.DEF_key_preset_pipeline, cls.DEF_key_preset_basic, cls.DEF_key_preset_option),
            (cls.DEF_key_preset_pipeline, cls.DEF_key_preset_name, cls.DEF_key_preset_basic),
            (cls.DEF_key_preset_pipeline, cls.DEF_key_preset_name, cls.DEF_key_preset_data),
            (cls.DEF_key_preset_pipeline, cls.DEF_key_preset_name, cls.DEF_key_preset_database),
            # Maya
            # Project
            # Project > Basic > Option
            (cls.DEF_key_preset_project, cls.DEF_key_preset_basic, cls.DEF_key_preset_option),
            # Project > Production > Asset
            (cls.DEF_key_preset_project, cls.DEF_key_preset_production, cls.DEF_key_preset_asset),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_production, cls.DEF_key_preset_scene),
            # Project > Inspection > Asset
            (cls.DEF_key_preset_project, cls.DEF_key_preset_inspection, cls.DEF_key_preset_asset),
            #
            (cls.DEF_key_preset_project, cls.DEF_key_preset_name, cls.DEF_key_preset_directory),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_name, cls.DEF_key_preset_node),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_name, cls.DEF_key_preset_attribute),
            (cls.DEF_key_preset_project, cls.DEF_key_preset_storage, cls.DEF_key_preset_root)
        ]
        return lis

    @classmethod
    def _defaultVariantDatum(cls):
        lis = [
            (cls.DEF_key, '', '', ''),
            (cls.DEF_value, '', '', '')
        ]
        return lis

    @classmethod
    def _basicPersonnelTeamList(cls):
        lis = [
            cls.DEF_value_preset_unspecified,
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

    @classmethod
    def _basicPersonnelPostList(cls):
        lis = [
            cls.DEF_value_preset_unspecified,
            'Artist',
            'Producer',
            'Team - Leader',
            'PM',
            'TD',
            'Rnd',
            cls.LynxiPipelineTdPost
        ]
        return lis

    @classmethod
    def _basicSoftwareApplicationList(cls):
        lis = [
            cls.DEF_value_preset_unspecified,
            cls.DEF_key_preset_maya
        ]
        return lis

    @classmethod
    def _DEF_mya_version_list(cls):
        lis = [
            cls.DEF_value_preset_unspecified,
            cls.VAR_value_preset_general,
            '2017',
            '2018',
            '2019'
        ]
        return lis

    @classmethod
    def _DEF_mya_renderer_list(cls):
        lis = [
            cls.DEF_value_preset_unspecified,
            cls.DEF_value_renderer_arnold,
            cls.DEF_value_renderer_redshift
        ]
        return lis

    @classmethod
    def _basicVariantShelfList(cls):
        lis = [
            cls.DEF_value_preset_unspecified,
            'asset',
            'scenery',
            'animation',
            'light',
            'utils'
        ]
        return lis

    @classmethod
    def basicAppShelfToolSchemeConfig(cls):
        lis = [
            cls.DEF_value_preset_unspecified,
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

    @classmethod
    def basicPresetShelfSetConfig(cls):
        lis = [
            (cls.DEF_key_application_name, '<appNames>'),
            (cls.DEF_key_application_version, '<appVersions>'),
            (cls.DEF_key_shelf_name, '<shelfName>'),
            (cls.LynxiUiNameKey, '<shelfName>'),
            (cls.LynxiUiTipKey, '<shelfName>')
        ]
        return lis

    @classmethod
    def basicPresetToolSchemeConfig(cls):
        lis = [
            cls.DEF_value_preset_unspecified,
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

    @classmethod
    def basicPresetToolSetConfig(cls):
        lis = [
            (cls.DEF_key_application_name, '<appNames>'),
            (cls.DEF_key_application_version, '<appVersions>'),
            (cls.DEF_key_tool_name, '<toolName>'),
            (cls.LynxiUiNameKey, '<toolName>'),
            (cls.LynxiUiTipKey, '<toolName>')
        ]
        return lis

    @classmethod
    def basicPresetScriptSchemeConfig(cls):
        lis = [
            cls.DEF_value_preset_unspecified,
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

    @classmethod
    def basicPresetScriptSetConfig(cls):
        lis = [
            (cls.DEF_key_application_name, '<appNames>'),
            (cls.DEF_key_application_version, '<appVersions>'),
            (cls.LynxiScriptNameKey, '<scriptName>'),
            (cls.LynxiUiNameKey, '<scriptName>'),
            (cls.LynxiUiTipKey, '<scriptName>')
        ]
        return lis

    @classmethod
    def basicAppPlugSchemeConfig(cls):
        lis = [
            cls.DEF_value_preset_unspecified
        ]
        return lis

    @classmethod
    def basicAppPlugSetConfig(cls):
        lis = [
            (cls.DEF_key_application_name, '<applicationName>'),
            (cls.DEF_key_application_version, '<appVersions>'),
            (cls.DEF_key_plug_name, '<plugName>'),
            (cls.DEF_key_plug_version, '<plugVersions>'),
            (cls.DEF_key_plug_loadname, '<plugLoadNames>'),
            (cls.LynxiServerPathKey, '<serverBasicPath>/plug/<app>/<appVersion>/<plugName>/<plugVersion>'),
            (cls.LynxiLocalPathKey, '<localBasicPath>/plug/<app>/<appVersion>/<plugName>/<plugVersion>')
        ]
        return lis

    @classmethod
    def basicMayaTimeUnitConfig(cls):
        lis = [
            cls.DEF_value_preset_unspecified,
            '15 fps',
            '24 fps',
            '25 fps',
            '30 fps',
            '48 fps',
            '50 fps',
            '60 fps'
        ]
        return lis

    @classmethod
    def basicMayaCommonPlugConfig(cls):
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

    @classmethod
    def basicProjectClassificationConfig(cls):
        lis = [
            cls.DEF_value_preset_unspecified,
            cls.DEF_key_category_project_cg,
            cls.DEF_key_category_project_film,
            cls.DEF_key_category_project_game
        ]
        return lis

    @classmethod  # Model Check Config
    def _DEF_project_inspection_asset_model_dict(cls):
        dic = bscMtdCore.orderedDict()
        dic['meshInstanceCheck'] = [
            True,
            'Mesh Instance Check',
            u'''确认模型不存在关联复制'''
        ]
        dic['meshVertexNormalLockCheck'] = [
            True,
            'Mesh Normal Check',
            u'''确认模型不存在法线锁定'''
        ]
        dic['meshOverlapNameCheck'] = [
            True,
            'Mesh Overlapping Naming Check',
            u'''确认模型不存在物件重名'''
        ]
        dic['meshTransformCheck'] = [
            True,
            'Mesh Transform Check',
            u'''确认模型不存在错误的 Transform'''
        ]
        dic['meshMatrixNonDefaultCheck'] = [
            True,
            'Mesh Transformation Check',
            u'确认模型不存在错误的位移，旋转，缩放'
        ]
        dic['meshGeometryCheck'] = [
            True,
            'Mesh Nde_Geometry Check',
            u'''确认模型不存在错误的拓扑结构'''
        ]
        dic['meshHistoryCheck'] = [
            True,
            'Mesh History Check',
            u'''确认模型不存在多余的历史记录'''
        ]
        return dic

    @classmethod
    def _DEF_project_inspection_asset_model_mesh_dict(cls):
        dic = bscMtdCore.orderedDict()
        dic['meshFaceNSidedCheck'] = [
            True,
            'N - Sided Face Check',
            u'确认不存在超过四边的面'
        ]
        dic['meshFaceConcaveCheck'] = [
            False,
            'Concave Face Check',
            u'确认不存在凹形面'
        ]
        dic['meshFaceHoledCheck'] = [
            True,
            'Holed Face Check',
            u'确认不存在破损的面'
        ]
        dic['meshFaceNonPlanarCheck'] = [
            False,
            'Non - planar Face Check',
            u'确认不存在不平整的面'
        ]
        #
        dic['meshFaceLaminaCheck'] = [
            True,
            'Lamina Face Check',
            u'确认不存在重合的面'
        ]
        dic['meshFaceNonTriangulableCheck'] = [
            True,
            'Non - Triangulable Faces Check',
            u'确认不存在无法三角化的面'
        ]
        dic['meshFaceNonMappingCheck'] = [
            True,
            'Non - Mapping Face Check',
            u'确认不存在无UV的面'
        ]
        #
        dic['meshVertexNonManifoldCheck'] = [
            True,
            'Non - Manifold Vertex Check',
            u'确认不存在非流形的点'
        ]
        #
        dic['meshUvSharedCheck'] = [
            False,
            'Shared Uv Check',
            u'确认不存在共用UV'
        ]
        #
        dic['meshFaceZeroAreaCheck'] = [
            False,
            'Zero - Area Face Check',
            u'确认不存在无面积的面'
        ]
        dic['meshEdgeZeroLengthCheck'] = [
            False,
            'Zero - Length Edge Check',
            u'确认不存在无长度的线'
        ]
        dic['meshUvZeroAreaCheck'] = [
            False,
            'Zero - Area Uv Check',
            u'确认不存在无UV面积的面'
        ]
        return dic

    @classmethod
    def _DEF_project_inspection_asset_groom_dict(cls):
        dic = bscMtdCore.orderedDict()
        dic['astYetiCheck'] = [
            True,
            'Yeti Check',
            u'''确认不存在错误的 Yeti'''
        ]
        dic['astPfxHairCheck'] = [
            True,
            'Pfx - Hair Check',
            u'''确认不存在错误的 Pfx Hair'''
        ]
        dic['astNurbsHairCheck'] = [
            True,
            'Nurbs - Hair Check',
            u'''确认不存在错误的 Nurbs Hair'''
        ]
        dic['astGrowSourceCheck'] = [
            True,
            'Grow - Mesh ( Source ) Check',
            u'''确认不存在错误的 Grow - Mesh'''
        ]
        dic['astSolverGuideCheck'] = [
            False,
            'Solver - Guide Check',
            u'''确认不存在错误的 Solver - Guide'''
        ]
        return dic

    @classmethod
    def _DEF_project_inspection_asset_solver_dict(cls):
        dic = bscMtdCore.orderedDict()
        dic['astSolverGuideCheck'] = [
            True,
            'Solver - Guide Check',
            u'''确认不存在错误的 Solver - Guide'''
        ]
        dic['astGrowSourceCheck'] = [
            True,
            'Grow - Mesh ( Source ) Check',
            u'''确认不存在错误的 Grow - Mesh'''
        ]
        return dic

    @classmethod
    def _DEF_project_inspection_asset_rig_dict(cls):
        dic = bscMtdCore.orderedDict()
        dic['astRigControlCheck'] = [
            False,
            'Rig Control Check',
            u'''确认绑定不存在错误的 Control'''
        ]
        return dic

    @classmethod
    def _DEF_project_inspection_asset_light_dict(cls):
        dic = bscMtdCore.orderedDict()
        dic['astLightTransformCheck'] = [
            False,
            'Light Transform Check',
            u'''确认灯光不存在错误的 Transform'''
        ]
        return dic

    @classmethod
    def _DEF_project_inspection_asset_shader_dict(cls):
        dic = bscMtdCore.orderedDict()
        dic['arTextureFormatCheck'] = [
            False,
            'Arnold Texture Format Check',
            u'''确认贴图不存在错误的格式'''
        ]
        dic['arTextureTxCheck'] = [
            True,
            'Arnold TX Texture Check',
            u'''确认贴图不存在错误的".tx"'''
        ]
        dic['arTextureColorSpaceCheck'] = [
            True,
            'Arnold Texture Color Space Check',
            u'''确认贴图不存在错误的 "Color Space"'''
        ]
        return dic

    @classmethod
    def basicAssetMeshCheckKeys(cls):
        lis = [
            cls.astHierarchyKey,
            cls.astGeometryKey,
            cls.astGeomShapeKey,
            cls.astMapKey,
            cls.astMapShapeKey
        ]
        return lis

    @classmethod
    def isLxPipelineTd(cls):
        boolean = False
        user = bscMethods.OsPlatform.username()
        if user in cls.Lynxi_Name_Td_Lis:
            boolean = True
        return boolean


class Product(object):
    # Module
    VAR_product_module_asset = 'asset'
    VAR_product_module_prefix_asset = 'ast'
    VAR_product_module_scenery = 'scenery'
    VAR_product_module_prefix_scenery = 'scn'
    VAR_product_Module_scene = 'scene'
    VAR_product_module_prefix_scene = 'sc'
    #
    VAR_product_module_list = [
        VAR_product_module_asset,
        VAR_product_module_scenery,
        VAR_product_Module_scene
    ]
    #
    VAR_product_module_prefix_dict = {
        VAR_product_module_asset: VAR_product_module_prefix_asset,
        VAR_product_module_scenery: VAR_product_module_prefix_scenery,
        VAR_product_Module_scene: VAR_product_module_prefix_scene
    }
    VAR_product_module_showname_dict = bscMtdCore.orderedDict(
        [
            (VAR_product_module_asset, ('Asset', u'资产')),
            (VAR_product_module_scenery, ('Scenery', u'场景')),
            (VAR_product_Module_scene, ('Scene', u'镜头'))
        ]
    )
    # Asset
    VAR_product_asset_category_character = 'character'
    VAR_product_asset_category_prop = 'prop'
    #
    VAR_product_asset_category_list = [
        VAR_product_asset_category_character,
        VAR_product_asset_category_prop
    ]
    VAR_product_asset_category_showname_dict = bscMtdCore.orderedDict(
        [
            (VAR_product_asset_category_character, ('Character', u'角色')),
            (VAR_product_asset_category_prop, ('Prop', u'道具'))
        ]
    )
    VAR_product_asset_category_uidatum_dict = bscMtdCore.orderedDict(
        [
            ('ast0', (VAR_product_asset_category_character, u'角色')),
            ('ast1', (VAR_product_asset_category_prop, u'道具'))
        ]
    )
    # Scenery
    VAR_product_scenery_category_scenery = 'scenery'
    VAR_product_scenery_category_Group = 'group'
    VAR_product_scenery_category_Assembly = 'assembly'
    #
    VAR_product_scenery_category_Lis = [
        VAR_product_scenery_category_scenery,
        VAR_product_scenery_category_Group,
        VAR_product_scenery_category_Assembly
    ]
    VAR_product_scenery_category_showname_dict = bscMtdCore.orderedDict(
        [
            (VAR_product_scenery_category_scenery, ('Scenery', u'场景')),
            (VAR_product_scenery_category_Group, ('Group', u'组合')),
            (VAR_product_scenery_category_Assembly, ('Assembly', u'组装'))
        ]
    )
    VAR_product_scenery_category_uidatum_dict = bscMtdCore.orderedDict(
        [
            ('scn0', (VAR_product_scenery_category_scenery, u'场景')),
            ('scn1', (VAR_product_scenery_category_Group, u'组合')),
            ('scn2', (VAR_product_scenery_category_Assembly, u'组装'))
        ]
    )
    # Scene
    VAR_product_scene_category_scene = 'scene'
    VAR_product_scene_category_act = 'act'
    #
    VAR_product_scene_category_list = [
        VAR_product_scene_category_scene,
        VAR_product_scene_category_act
    ]
    VAR_product_scene_category_showname_dict = bscMtdCore.orderedDict(
        [
            (VAR_product_scene_category_scene, ('Scene', u'镜头')),
            (VAR_product_scene_category_act, ('Act', u'动作'))
        ]
    )
    VAR_product_scene_category_uidatum_dict = bscMtdCore.orderedDict(
        [
            ('sc0', (VAR_product_scene_category_scene, u'镜头')),
            ('sc1', (VAR_product_scene_category_act, u'动作'))
        ]
    )
    # Priority
    VAR_product_priority_major = 'major'
    VAR_product_priority_minor = 'minor'
    VAR_product_priority_util = 'util'
    #
    VAR_product_priority_list = [
        VAR_product_priority_major,
        VAR_product_priority_minor,
        VAR_product_priority_util
    ]
    VAR_product_priority_showname_dict = bscMtdCore.orderedDict(
        [
            (VAR_product_priority_major, ('Major', u'主要')),
            (VAR_product_priority_minor, ('Minor', u'次要')),
            (VAR_product_priority_util, ('Util', u'龙套'))
        ]
    )
    VAR_product_priority_uidatum_dict = bscMtdCore.orderedDict(
        [
            ('prt0', (VAR_product_priority_major, u'主要')),
            ('prt1', (VAR_product_priority_minor, u'次要')),
            ('prt2', (VAR_product_priority_util, u'龙套'))
        ]
    )
    # Asset
    VAR_product_asset_link_model = 'model'
    VAR_product_asset_link_rig = 'rig'
    VAR_product_asset_link_groom = 'cfx'
    VAR_product_asset_link_solver = 'solver'
    VAR_product_asset_link_light = 'light'
    VAR_product_asset_link_assembly = 'assembly'
    #
    VAR_product_asset_link_list = [
        VAR_product_asset_link_model,
        VAR_product_asset_link_rig,
        VAR_product_asset_link_groom,
        VAR_product_asset_link_solver,
        VAR_product_asset_link_light,
        VAR_product_asset_link_assembly
    ]
    VAR_product_asset_link_showname_dict = bscMtdCore.orderedDict(
        [
            (VAR_product_asset_link_model, ('Model', u'模型')),
            (VAR_product_asset_link_rig, ('Rig', u'绑定')),
            (VAR_product_asset_link_groom, ('Groom', u'毛发塑形')),
            (VAR_product_asset_link_solver, ('Solver Rig', u'毛发绑定')),
            (VAR_product_asset_link_light, ('Light', u'灯光')),
            (VAR_product_asset_link_assembly, ('Assembly', u'组装'))
        ]
    )
    # Scenery
    VAR_product_scenery_link_assembly = 'assembly'
    VAR_product_scenery_link_layout = 'layout'
    VAR_product_scenery_link_animation = 'animation'
    VAR_product_scenery_link_simulation = 'simulation'
    VAR_product_scenery_link_solver = 'solver'
    VAR_product_scenery_link_light = 'light'

    VAR_product_scenery_link_list = [
        VAR_product_scenery_link_assembly,
        VAR_product_scenery_link_layout,
        VAR_product_scenery_link_animation,
        VAR_product_scenery_link_simulation,
        VAR_product_scenery_link_solver,
        VAR_product_scenery_link_light
    ]
    VAR_product_scenery_link_showname_dict = bscMtdCore.orderedDict(
        [
            (VAR_product_scenery_link_assembly, ('Scenery', u'场景布景')),
            (VAR_product_scenery_link_layout, ('Layout', u'场景预览')),
            (VAR_product_scenery_link_animation, ('Animation', u'场景动画')),
            (VAR_product_scenery_link_simulation, ('Simulation', u'场景解算')),
            (VAR_product_scenery_link_solver, ('Solver', u'场景模拟')),
            (VAR_product_scenery_link_light, ('Light', u'场景灯光'))
        ]
    )

    VAR_product_scene_link_layout = 'layout'
    VAR_product_scene_link_animation = 'animation'
    VAR_product_scene_link_simulation = 'simulation'
    VAR_product_scene_link_solver = 'solver'
    VAR_product_scene_link_light = 'light'

    VAR_product_scene_link_list = [
        VAR_product_scene_link_layout,
        VAR_product_scene_link_animation,
        VAR_product_scene_link_simulation,
        VAR_product_scene_link_solver,
        VAR_product_scene_link_light
    ]
    VAR_product_scene_link_showname_dict = bscMtdCore.orderedDict(
        [
            (VAR_product_scene_link_layout, ('Layout', u'镜头预览')),
            (VAR_product_scene_link_animation, ('Animation', u'镜头动画')),
            (VAR_product_scene_link_simulation, ('Simulation', u'镜头解算')),
            (VAR_product_scene_link_solver, ('Solver', u'镜头模拟')),
            (VAR_product_scene_link_light, ('Light', u'镜头灯光'))
        ]
    )

    VAR_product_module_category_dict = {
        VAR_product_module_asset: VAR_product_asset_category_list,
        VAR_product_module_scenery: VAR_product_scenery_category_Lis,
        VAR_product_Module_scene: VAR_product_scene_category_list
    }

    VAR_product_key_priority = 'priority'
    VAR_product_key_Name = 'name'
    VAR_product_key_Variant = 'variant'

    VAR_product_step_pending = 'pending'
    VAR_product_step_wip = 'wip'
    VAR_product_step_delivery = 'delivery'
    VAR_product_step_refine = 'refine'
    VAR_product_step_validated = 'validated'

    VAR_product_step_list = [
        VAR_product_step_pending,
        VAR_product_step_wip,
        VAR_product_step_delivery,
        VAR_product_step_refine,
        VAR_product_step_validated
    ]

    VAR_product_step_showname_dict = {
        VAR_product_step_pending: ('Pending', u'等待'),
        VAR_product_step_wip: ('WIP', u'制作'),
        VAR_product_step_delivery: ('Delivery', u'提交'),
        VAR_product_step_refine: ('Refine', u'返修'),
        VAR_product_step_validated: ('Validated', u'通过')
    }

    VAR_product_label_root = 'unitRoot'

    VAR_product_key_project = 'project'
    VAR_product_key_category = 'classify'
    VAR_product_key_module = 'module'
    VAR_product_key_link = 'link'
    VAR_product_key_stage = 'stage'

    VAR_product_attribute_id = 'index'
    VAR_product_attribute_category = 'classification'
    VAR_product_attribute_name = 'name'
    VAR_product_attribute_variant = 'variant'
    VAR_product_attribute_stage = 'stage'

    VAR_product_attribute_camera = 'camera'
    VAR_product_separator_camera = ';'

    VAR_product_attribute_list = [
        VAR_product_attribute_id,
        VAR_product_attribute_category,
        VAR_product_attribute_name,
        VAR_product_attribute_variant,
        VAR_product_attribute_stage
    ]

    VAR_product_attribute_object_transparent = 'lxObjectTransparent'
    VAR_product_attribute_object_renderable = 'lxObjectRenderVisible'

    VAR_product_asset_model_stage_list = [
        'model',
        'texture',
        'shader'
    ]
    VAR_product_asset_rig_stage_list = [
        'layout',
        'animation'
    ]
    VAR_product_asset_groom_stage_list = [
        'groom',
        'shader'
    ]
    VAR_product_asset_solver_stage_list = [
        'solver'
    ]
    VAR_product_asset_light_stage_list = [
        'light',
        'shader'
    ]
    VAR_product_asset_assembly_stage_list = [
        'assembly'
    ]
    VAR_product_scenery_assembly_stage_list = [
        'scenery'
    ]
    VAR_product_scenery_layout_stage_list = [
        'layout'
    ]
    VAR_product_scene_animation_stage_list = [
        'blocking',
        'final',
        'polish'
    ]
    VAR_product_scene_solver_stage_list = [
        'solver'
    ]
    VAR_product_scene_simulation_stage_list = [
        'simulation'
    ]
    VAR_product_scene_light_stage_list = [
        'light',
        'render',
        'compose'
    ]

    DEF_key_cache = 'cache'
    DEF_key_posecache = 'posecache'
    DEF_key_modelcache = 'modelcache'
    DEF_key_solvercache = 'solvercache'
    DEF_key_rigcache = 'rigcache'

    DEF_key_info_startframe = 'startframe'
    DEF_key_info_endframe = 'endframe'

    DEF_key_info_project = 'project'
    DEF_key_info_index = 'index'
    DEF_key_info_category = 'classify'
    DEF_key_info_name = 'name'
    DEF_key_info_variant = 'variant'
    DEF_key_info_attribute = 'attribute'
    DEF_key_info_abcattribute = 'abcattribute'
    DEF_key_info_connection = 'connection'
    DEF_key_info_nhrconnection = 'nhrconnection'
    DEF_key_info_asbreference = 'asbreference'
    DEF_key_info_transformation = 'transformation'
    DEF_key_info_worldmatrix = 'worldMatrix'

    DEF_key_attribute_shapename = 'lynxiShapeName'

    DEF_key_type_cameracache = 'cameracache'
    DEF_key_type_modelcache = 'modelcache'
    DEF_key_type_furcache = 'furcache'
    DEF_key_type_rigcache = 'rigcache'
