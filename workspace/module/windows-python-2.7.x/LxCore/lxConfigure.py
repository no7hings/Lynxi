# coding:utf-8
from LxBasic import bscMethods, bscCommands

Lynxi_Name_Td_Lis = [
    'dongchangbao',
    'changbao.dong'
]

LynxiPipelineTdPost = 'Pipeline - TD'
LynxiPipelineTdLevel = 3
pipelineTdBasicPaths = [
    'E:/myworkspace/td/lynxi'
]
# Environ Key
Lynxi_Environ_Key_Project = 'LYNXI_PROJECT'

LynxiUi_Value_TooltipDelayTime = 1000

Folder_Basic = '.lynxi'
Lynxi_App_Maya = 'maya'

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

LynxiGeneralValue = 'General'
LynxiValue_Unspecified = 'Unspecified'
LynxiDefaultPresetValue = 'Preset_2018'
Lynxi_Def_Value_Pipeline = 'Pipeline_2018'
LynxiDefaultVariantValue = 'Variant_2018'
LynxiDefaultPersonnelValue = 'Personnel_2018'
LynxiDefaultSoftwareValue = 'Software_2018'
LynxiDefaultMayaValue = 'Maya_2018'
Lynxi_Keyword_Project_Default = 'Default_Project'
LynxiDefaultProjectValue = 'Default_Project_2017'
LynxiDefaultSchemeValue = 'Default_Scheme'
LynxiPostLevelKey = 'postLevel'
LynxiUserEnNameKey = 'enName'
LynxiUserCnNameKey = 'cnName'
LynxiUserMailKey = 'mail'
LynxiUserSendMailEnabledKey = 'sendMail'
LynxiDefaultEpisodeKey = '001A'
LynxiMayaTimeUnitKey = 'mayaTimeUnit'
LynxiDefaultTimeUnitValue = '24 fps'
LynxiProjectClassificationKey = 'projectClassification'
LynxiFilmProjectValue = 'Film'
LynxiCgProjectValue = 'CG'
LynxiGameProjectValue = 'Game'
LynxiAppNameKey = 'applicationName'
LynxiAppNamesKey = 'appNames'
LynxiAppVersionKey = 'appVersion'
LynxiAppVersionsKey = 'appVersions'
LynxiShelfNameKey = 'shelfName'
LynxiToolNameKey = 'toolName'
LynxiScriptNameKey = 'scriptName'

Key_Plug_Name = 'plugName'
Key_Plug_Version = 'plugVersion'
Lynxi_Key_Plug_Versions = 'plugVersions'
Lynxi_Key_Plug_Load_Names = 'plugLoadNames'
Lynxi_Key_Plug_Load_Enable_Auto = 'autoLoad'
Lynxi_Key_Plug_Setup_Command = 'plugSetupCommand'
Lynxi_Key_Plug_Path = 'plugPath'
Lynxi_Key_Plug_Path_Deploy = 'plugDeployPath'
Lynxi_Key_Plug_Path_Module = 'plugModulePath'
Lynxi_Key_Plug_Path_Rlm = 'plugRlmPath'

LynxiVariantKey = 'key'
LynxiVariantValue = 'value'
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
LynxiMayaRendererKey = 'mayaRenderer'
LynxiMayaSoftwareRendererValue = 'Maya - Software'
LynxiMayaHardwareRendererValue = 'Maya - Hardware'
LynxiArnoldRendererValue = 'Arnold'
LynxiRedshiftRendererValue = 'Redshift'
LynxiMayaPlugPresetKey = 'mayaPlug'
LynxiSchemeExt = '.index'
LynxiSetExt = '.set'
LynxiUiPathsep = ' > '
LynxiRootIndex_Server = 0
LynxiRootIndex_Local = 1
LynxiRootIndex_Backup = 2
LynxiRootLabelDic = {
    0: 'serverRoot',
    1: 'localRoot',
    2: 'backupRoot'
}
# Module
LynxiProduct_Asset_Link_Model = 'model'
LynxiAstModelStages = [
    'model',
    'texture',
    'mdlShader'
]
LynxiProduct_Asset_Link_Rig = 'rig'
LynxiAstRigStages = [
    'rigLayout',
    'rigAnimation'
]
LynxiProduct_Asset_Link_Cfx = 'cfx'
LynxiAstCfxStages = [
    'groom',
    'cfxShader'
]
LynxiProduct_Asset_Link_Solver = 'solver'
LynxiAstRigSolStages = [
    'solverBind'
]
LynxiProduct_Asset_Link_Light = 'light'
LynxiAstLightStages = [
    'light',
    'lgtShader'
]
LynxiProduct_Asset_Link_Assembly = 'assembly'
LynxiAstAssemblyStages = [
    'assembly'
]
LynxiProduct_Scenery_Link_Scenery = 'scenery'
LynxiScnSceneryStages = [
    'scenery'
]
LynxiProduct_Scene_Link_layout = 'layout'
LynxiScLayoutStages = [
    'layout'
]
LynxiProduct_Scene_Link_Animation = 'animation'
LynxiScAnimationStages = [
    'blocking',
    'final',
    'polish'
]
LynxiProduct_Scene_Link_Solver = 'solver'
LynxiScSolverStages = [
    'solverSimulation'
]
LynxiProduct_Scene_Link_Simulation = 'simulation'
LynxiScSimulationStages = [
    'simulation'
]
LynxiProduct_Scene_Link_Light = 'light'
LynxiScLightStages = [
    'shader',
    'light',
    'render'
]
Lynxi_Key_Info_SourceFile = 'link'
LynxiCacheInfoKey = 'cache'
LynxiPoseCacheInfoKey = 'poseCache'
LynxiModelCacheInfoKey = 'modelCache'
LynxiSolverCacheInfoKey = 'solverCache'
LynxiExtraCacheInfoKey = 'extraCache'

Lynxi_Key_Info_Stage = 'stage'
Lynxi_Key_Info_Update = 'update'
Lynxi_Key_Info_Timestamp = 'timestamp'
Lynxi_Key_Info_Version = 'version'
Lynxi_Key_Info_User = 'user'
Lynxi_Key_Info_Artist = 'artist'
Lynxi_Key_Info_HostName = 'hostName'
Lynxi_Key_Info_Host = 'host'
Lynxi_Key_Info_Description = 'description'
Lynxi_Key_Info_Note = 'note'
Lynxi_Key_Info_Notes = 'notes'
Lynxi_Key_Info_Data = 'data'
Lynxi_Key_Info_StartFrame = 'startFrame'
Lynxi_Key_Info_EndFrame = 'endFrame'

Lynxi_Key_Info_Active = 'active'

LynxiSolverInfoKey = 'solver'
LynxiProjectInfoKey = 'project'
LynxiInfoKey_Index = 'index'
LynxiInfoKey_Class = 'classify'
LynxiInfoKey_Name = 'name'
LynxiInfoKey_Variant = 'variant'
LynxiAttributeDataKey = 'attribute'
LynxiAlembicAttrDataKey = 'alembicAttr'
LynxiConnectionDataKey = 'connection'
LynxiNhrConnectionDataKey = 'nhrConnection'
LynxiAssemblyReferenceDataKey = 'assemblyReference'
LynxiTransformationDataKey = 'transformation'
LynxiDatumKey_Extra_WorldMatrix = 'worldMatrix'
LynxiObjectShapeNameAttrName = 'lynxiShapeName'
LynxiTaskTimestampAttrName = 'lynxiTaskTimeStamp'
LynxiUpdateExt = '.update'
LynxiResultExt = '.result'
LynxiScCameraCacheType = 'cameraCache'
LynxiScAstModelCacheType = 'modelCache'
LynxiScAstCfxFurCacheType = 'cfxFurCache'
LynxiScAstExtraCacheType = 'extraCache'
# Ignore Send Message
if bscMethods.OsSystem.username() in Lynxi_Name_Td_Lis:
    LynxiIsSendMail = False
    LynxiIsSendDingTalk = False
else:
    LynxiIsSendMail = True
    LynxiIsSendDingTalk = True

LynxiCharacterClassKey = 'character'
LynxiPropClassKey = 'prop'
LynxiAssetClassLis = [
    LynxiCharacterClassKey,
    LynxiPropClassKey
]
LynxiSceneryClassKey = 'scenery'
LynxiMainTimeTag = '0000_0000_0000'
LynxiProduct_Stage_Pending = 'pending'
LynxiProduct_Stage_Wip = 'wip'
LynxiProduct_Stage_Delivery = 'delivery'
LynxiProduct_Stage_Refine = 'refine'
LynxiProduct_Stage_Validated = 'validated'
LynxiAttrName_Object_Transparent = 'lxObjectTransparent'
LynxiAttrName_Object_RenderVisible = 'lxObjectRenderVisible'

STR_Value_Default = 'default'

varDic = globals()


DIC_directory_database = {
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


def isLxPipelineTd():
    boolean = False
    user = bscMethods.OsSystem.username()
    if user in Lynxi_Name_Td_Lis:
        boolean = True
    return boolean


def getLxVariantValue(varName):
    if varName in varDic:
        return varDic[varName]


def setLxVariantValue(varName, value):
    varDic[varName] = value
