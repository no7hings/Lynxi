# coding:utf-8
import os

import sys

import platform

from LxBasic import bscObjects

from LxCore import lxBasic

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
LynxiPresetKey = 'preset'
LynxiPipelinePresetKey = 'pipeline'
LynxiVariantPresetKey = 'variant'
LynxiPersonnelPresetKey = 'personnel'
LynxiSoftwarePresetKey = 'software'
LynxiMayaPresetKey = 'maya'
Lynxi_Key_Preset_Project = 'project'
LynxiBasicPresetKey = 'basic'
LynxiDeploymentPresetKey = 'deployment'
LynxiEnvironPresetKey = 'environ'
LynxiSetPresetKey = 'set'
LynxiEpisodePresetKey = 'episode'
LynxiProductionPresetKey = 'production'
LynxiInspectionPresetKey = 'Inspection'
LynxiPreferencePresetKey = 'preference'
LynxiOptionPresetKey = 'option'
LynxiAssetPresetKey = 'asset'
LynxiSceneryPresetKey = 'scenery'
LynxiScenePresetKey = 'scene'
LynxiAnimationPresetKey = 'animation'
LynxiDefinitionPresetKey = 'definition'
LynxiDevelopmentPresetKey = 'development'
LynxiTeamPresetKey = 'team'
LynxiPostPresetKey = 'post'
LynxiUserPresetKey = 'user'
LynxiStoragePresetKey = 'storage'
LynxiRootPresetKey = 'root'
LynxiFilePresetKey = 'file'
LynxiNamePresetKey = 'name'
LynxiDataPresetKey = 'data'
LynxiDatabasePresetKey = 'database'
LynxiDirectoryPresetKey = 'directory'
LynxiNodePresetKey = 'node'
LynxiAttributePresetKey = 'attribute'
LynxiCustomizationPresetKey = 'customization'
LynxiShelfPresetKey = 'shelf'
LynxiShelfToolPresetKey = 'shelfTool'
LynxiKitPresetKey = 'kit'
LynxiAppPresetKey = 'app'
Lynxi_Key_Plug_PresetKey = 'plug'
LynxiRendererPresetKey = 'renderer'
LynxiVersionPresetKey = 'version'
LynxiScriptPresetKey = 'script'
LynxiTdPresetKey = 'td'
LynxiGeneralValue = 'General'
LynxiValue_Unspecified = 'Unspecified'
LynxiDefaultPresetValue = 'Preset_2018'
LynxiDefaultPipelineValue = 'Pipeline_2018'
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
LynxiProduct_Module_Asset = 'asset'
LynxiProduct_Module_Scenery = 'scenery'
LynxiProduct_Module_Scene = 'scene'
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
if lxBasic.getOsUser() in Lynxi_Name_Td_Lis:
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
none = ''
Lynxi_Mode_Develop_Enable_Product = False

Lynxi_Mode_Plug_Enable_Local = True
Lynxi_Mode_Plug_Enable_Module = True
Lynxi_Mode_Plug_Enable_Environ = True

Lynxi_Mode_Package_Enable_Local = True
varDic = globals()


def isLxPipelineTd():
    boolean = False
    user = lxBasic.getOsUser()
    if user in Lynxi_Name_Td_Lis:
        boolean = True
    return boolean


def getLxVariantValue(varName):
    if varName in varDic:
        return varDic[varName]


def setLxVariantValue(varName, value):
    varDic[varName] = value


def lxProductRecordDatumDic(osFile, stage=None, description=None, notes=None):
    dic = lxBasic.orderedDict()
    dic[Lynxi_Key_Info_SourceFile] = osFile
    dic[Lynxi_Key_Info_Update] = lxBasic.getOsActiveTimestamp()
    dic[Lynxi_Key_Info_Artist] = lxBasic.getOsUser()
    dic[Lynxi_Key_Info_HostName] = lxBasic.getOsHostName()
    dic[Lynxi_Key_Info_Host] = lxBasic.getOsHost()
    dic[Lynxi_Key_Info_Stage] = stage
    dic[Lynxi_Key_Info_Description] = description
    dic[Lynxi_Key_Info_Note] = notes
    return dic


# Get Update File
def _toLxProductRecordFile(osFile):
    base = lxBasic.getOsFileBase(osFile)
    string = base + LynxiUpdateExt
    return string


# Get Update File
def _toLxProductResultFile(osFile):
    base = lxBasic.getOsFileBase(osFile)
    string = base + LynxiResultExt
    return string
