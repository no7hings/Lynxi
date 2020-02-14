# coding:utf-8
from LxBasic import bscMethods

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

Lynxi_Key_Preset = 'preset'
Lynxi_Key_Pipeline = 'pipeline'
DEF_preset_key_variant = 'variant'
DEF_preset_key_personnel = 'personnel'
DEF_preset_key_Software = 'software'
DEF_preset_key_Maya = 'maya'
DEF_preset_key_Project = 'project'
DEF_preset_key_Basic = 'basic'
DEF_preset_key_Deployment = 'deployment'
DEF_preset_key_Environ = 'environ'
DEF_preset_key_Set = 'set'
DEF_preset_key_Episode = 'episode'
DEF_preset_key_Production = 'production'
DEF_preset_key_Inspection = 'Inspection'
DEF_preset_key_Preference = 'preference'
DEF_preset_key_Option = 'option'
DEF_preset_key_Asset = 'asset'
DEF_preset_key_scenery = 'scenery'
DEF_preset_key_scene = 'scene'
DEF_preset_key_Definition = 'definition'
DEF_preset_key_Team = 'team'
DEF_preset_key_Post = 'post'
DEF_preset_key_User = 'user'
DEF_preset_key_Storage = 'storage'
DEF_preset_key_Root = 'root'
DEF_preset_key_File = 'file'
DEF_preset_key_Name = 'name'
DEF_preset_key_Data = 'data'
DEF_preset_key_Database = 'database'
DEF_preset_key_Directory = 'directory'
DEF_preset_key_Node = 'node'
DEF_preset_key_Attribute = 'attribute'
DEF_preset_key_Customization = 'customization'
DEF_preset_key_Shelf = 'shelf'
DEF_preset_key_Shelf_Tool = 'shelfTool'
DEF_preset_key_Kit = 'kit'
DEF_preset_key_App = 'app'
DEF_preset_key_Plug = 'plug'
DEF_preset_key_Renderer = 'renderer'
DEF_preset_key_Version = 'version'
DEF_preset_key_Script = 'script'
DEF_preset_key_Td = 'td'

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
VAR_product_asset_link_model = 'model'
LynxiAstModelStages = [
    'model',
    'texture',
    'mdlShader'
]
VAR_product_asset_link_rig = 'rig'
LynxiAstRigStages = [
    'rigLayout',
    'rigAnimation'
]
VAR_product_asset_link_groom = 'cfx'
LynxiAstCfxStages = [
    'groom',
    'cfxShader'
]
VAR_product_asset_link_solver = 'solver'
LynxiAstRigSolStages = [
    'solverBind'
]
VAR_product_asset_link_light = 'light'
LynxiAstLightStages = [
    'light',
    'lgtShader'
]
VAR_product_asset_link_assembly = 'assembly'
LynxiAstAssemblyStages = [
    'assembly'
]
VAR_product_scenery_link_scenery = 'scenery'
LynxiScnSceneryStages = [
    'scenery'
]
VAR_product_scene_link_layout = 'layout'
LynxiScLayoutStages = [
    'layout'
]
VAR_product_scene_link_animation = 'animation'
LynxiScAnimationStages = [
    'blocking',
    'final',
    'polish'
]
VAR_product_scene_link_solver = 'solver'
LynxiScSolverStages = [
    'solverSimulation'
]
VAR_product_scene_link_simulation = 'simulation'
LynxiScSimulationStages = [
    'simulation'
]
VAR_product_scene_link_light = 'light'
LynxiScLightStages = [
    'shader',
    'light',
    'render'
]
DEF_key_info_sourcefile = 'link'
LynxiCacheInfoKey = 'cache'
LynxiPoseCacheInfoKey = 'poseCache'
LynxiModelCacheInfoKey = 'modelCache'
LynxiSolverCacheInfoKey = 'solverCache'
LynxiExtraCacheInfoKey = 'extraCache'

Lynxi_Key_Info_Stage = 'stage'
DEF_key_info_time = 'update'
Lynxi_Key_Info_Timestamp = 'timestamp'
Lynxi_Key_Info_Version = 'version'
Lynxi_Key_Info_User = 'user'
DEF_key_info_username = 'artist'
DEF_key_info_hostname = 'hostName'
DEF_key_info_host = 'host'
DEF_key_info_description = 'description'
DEF_key_info_note = 'note'
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

varDic = globals()


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
