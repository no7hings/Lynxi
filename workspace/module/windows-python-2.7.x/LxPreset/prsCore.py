# coding:utf-8
from LxBasic import bscConfigure

from LxPreset import prsConfigure

from LxCore import lxConfigure


class PrsProductBasic(prsConfigure.PrsBasic):
    @classmethod
    def moduleNames(cls):
        return cls.LynxiProduct_ModuleLis

    @classmethod
    def moduleShowname(cls, moduleString):
        return cls.LynxiProduct_Module_ShowName_Dic[moduleString][1]

    @classmethod
    def modulePrefixname(cls, moduleString):
        return cls.LynxiProduct_Module_PrefixDic[moduleString]

    @classmethod
    def isValidModuleName(cls, moduleString):
        return moduleString in cls.LynxiProduct_ModuleLis

    @classmethod
    def stepNames(cls):
        return cls.LynxiProduct_Step_Lis

    @classmethod
    def stepShownamesDic(cls):
        return cls.LynxiProduct_Step_ShowName_Dic

    @staticmethod
    def _toProductUnitName(number):
        return 'ID{}'.format(str(number).zfill(6))

    @classmethod
    def isValidAssetCategoryName(cls, categoryString):
        return categoryString in cls.LynxiProduct_Asset_Class_Lis

    @classmethod
    def isValidSceneryCategoryName(cls, categoryString):
        return categoryString in cls.LynxiProduct_Scenery_Class_Lis

    @classmethod
    def isValidSceneCategoryName(cls, categoryString):
        return categoryString in cls.LynxiProduct_Scene_Class_Lis

    @classmethod
    def moduleCategoryNames(cls, moduleString):
        if moduleString == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Asset_Class_Lis
        elif moduleString == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Scenery_Class_Lis
        elif moduleString == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Scene_Class_Lis

    @classmethod
    def moduleClassShownames(cls, moduleString):
        if moduleString == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Asset_Class_ShowName_Dic
        elif moduleString == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Scenery_Class_ShowName_Dic
        elif moduleString == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Scene_Class_ShowName_Dic

    @classmethod
    def _lxProductClassUiDatumDic(cls, moduleString):
        if moduleString == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Asset_Class_UiDatumDic
        elif moduleString == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Scenery_Class_UiDatumDic
        elif moduleString == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Scene_Class_UiDatumDic

    @classmethod
    def _lxProductPriorityUiDatum(cls, moduleString):
        if moduleString == cls.LynxiProduct_Module_Asset:
            return cls.LynxiUnit_Priority_UiDatumDic
        elif moduleString == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiUnit_Priority_UiDatumDic
        elif moduleString == cls.LynxiProduct_Module_Scene:
            return cls.LynxiUnit_Priority_UiDatumDic

    @classmethod
    def _lxProductLinkLis(cls, moduleString):
        if moduleString == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Asset_Link_Lis
        elif moduleString == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Scenery_Link_Lis
        elif moduleString == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Scene_Link_Lis

    @classmethod
    def moduleLinkShownameDic(cls, moduleString):
        if moduleString == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Asset_Link_ShowName_Dic
        elif moduleString == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Scenery_Link_ShowName_Dic
        elif moduleString == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Scene_Link_ShowName_Dic

    @classmethod
    def moduleStepShownameDic(cls, moduleString):
        if moduleString == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Step_ShowName_Dic
        elif moduleString == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Step_ShowName_Dic
        elif moduleString == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Step_ShowName_Dic

    @classmethod
    def modulePriorityShownameDic(cls, moduleString):
        if moduleString == cls.LynxiProduct_Module_Asset:
            return cls.LynxiUnit_Priority_ShowName_Dic
        elif moduleString == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiUnit_Priority_ShowName_Dic
        elif moduleString == cls.LynxiProduct_Module_Scene:
            return cls.LynxiUnit_Priority_ShowName_Dic

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
            [(cls.LynxiProduct_Unit_Key_Project, u'项目 [ Project(s) ]'), (projectString,)],
            [(cls.LynxiProduct_Unit_Key_Name, u'名字 [ Name ]'), cls._toProductUnitName(number)],
            [(cls.LynxiProduct_Unit_Key_Variant, u'变体 [ Variant(s) ]'), (bscConfigure.MtdBasic.STR_Value_Default,)],
            [(cls.LynxiProduct_Unit_Key_Category, u'类型 [ Classify ]'), cls._lxProductClassUiDatumDic(moduleString)],
            [(cls.LynxiProduct_Unit_Key_Priority, u'优先级 [ Priority ]'), cls._lxProductPriorityUiDatum(moduleString)]
        ]
        addLinkDatum()
        return lis

    @classmethod
    def lxProductUnitViewInfoSet(cls, moduleString, categoryString, unitViewName, extendString=None):
        unitViewClass = cls.moduleClassShownames(moduleString)[categoryString]
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
        return cls.LynxiProduct_Unit_AttrNameLis

    @classmethod
    def isValidAttributeName(cls, attributeName):
        return attributeName in cls.attributeNames()

    @classmethod
    def rootLabel(cls):
        return cls.LynxiUnit_Label_Root
    
 
class PrsAssetBasic(prsConfigure.PrsBasic):
    @classmethod
    def prefix(cls):
        return cls.LynxiProduct_Module_Prefix_Asset

    @classmethod
    def moduleName(cls):
        return cls.LynxiProduct_Module_Asset

    @classmethod
    def moduleShowname(cls):
        return cls.LynxiProduct_Module_ShowName_Dic[cls.LynxiProduct_Module_Asset][1]

    @classmethod
    def linkNames(cls):
        return cls.LynxiProduct_Asset_Link_Lis

    @classmethod
    def modelLinkName(cls):
        return cls.LynxiProduct_Asset_Link_Model

    @classmethod
    def rigLinkName(cls):
        return cls.LynxiProduct_Asset_Link_Rig

    @classmethod
    def groomLinkName(cls):
        return cls.LynxiProduct_Asset_Link_Groom

    @classmethod
    def solverLinkName(cls):
        return cls.LynxiProduct_Asset_Link_Solver

    @classmethod
    def lightLinkName(cls):
        return cls.LynxiProduct_Asset_Link_Light
    
    @classmethod
    def isModelStageName(cls, stageString):
        if stageString in lxConfigure.LynxiAstModelStages or stageString == cls.LynxiProduct_Asset_Link_Model:
            return True
        return False

    @classmethod
    def isRigStageName(cls, stageString):
        if stageString in lxConfigure.LynxiAstRigStages or stageString == cls.LynxiProduct_Asset_Link_Rig:
            return True
        return False

    @classmethod
    def isGroomStageName(cls, stageString):
        if stageString in lxConfigure.LynxiAstCfxStages or stageString == cls.LynxiProduct_Asset_Link_Groom:
            return True
        return False

    @classmethod
    def isSolverStageName(cls, stageString):
        if stageString in lxConfigure.LynxiAstRigSolStages or stageString == cls.LynxiProduct_Asset_Link_Solver:
            return True
        return False

    @classmethod
    def isLightStageName(cls, stageString):
        if stageString in lxConfigure.LynxiScLightStages or stageString == cls.LynxiProduct_Asset_Link_Light:
            return True
        return False

    @classmethod
    def isAssemblyStageName(cls, stageString):
        if stageString in lxConfigure.LynxiAstAssemblyStages or stageString == cls.LynxiProduct_Asset_Link_Assembly:
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
            return cls.LynxiProduct_Asset_Link_Model
        elif cls.isRigStageName(stageString):
            return cls.LynxiProduct_Asset_Link_Rig
        elif cls.isGroomStageName(stageString):
            return cls.LynxiProduct_Asset_Link_Groom
        elif cls.isSolverStageName(stageString):
            return cls.LynxiProduct_Asset_Link_Solver
        elif cls.isLightStageName(stageString):
            return cls.LynxiProduct_Asset_Link_Light
        return cls.LynxiProduct_Asset_Link_Model
    
    @classmethod
    def categories(cls):
        return cls.LynxiProduct_Asset_Class_Lis
    
    @classmethod
    def isValidCategory(cls, categoryName):
        return categoryName in cls.categories()

    @classmethod
    def isCharacterCategory(cls, categoryName):
        return categoryName == cls.LynxiProduct_Asset_Class_Character

    @classmethod
    def characterCategory(cls):
        return cls.LynxiProduct_Asset_Class_Character

    @classmethod
    def isPropCategory(cls, categoryName):
        return categoryName == cls.LynxiProduct_Asset_Class_Prop

    @classmethod
    def propCategory(cls):
        return cls.LynxiProduct_Asset_Class_Prop

    @classmethod
    def assemblyCategoryName(cls):
        return cls.LynxiProduct_Scenery_Class_Assembly
    
    @classmethod
    def classShowname(cls, categoryString):
        return cls.LynxiProduct_Asset_Class_ShowName_Dic[categoryString][1]
    
    @classmethod
    def linkShowname(cls, linkString):
        return cls.LynxiProduct_Asset_Link_ShowName_Dic[linkString][1]
    
    @classmethod
    def linkShowname_(cls, stageString):
        return cls.linkShowname(cls.stageName2linkName(stageString))

    @classmethod
    def classShownameDic(cls):
        return cls.LynxiProduct_Asset_Class_UiDatumDic

    @classmethod
    def priorityNames(cls):
        return cls.LynxiUnit_Priority_Lis


class PrsSceneryBasic(prsConfigure.PrsBasic):
    @classmethod
    def prefix(cls):
        return cls.LynxiProduct_Module_Prefix_Scenery

    @classmethod
    def moduleName(cls):
        return cls.LynxiProduct_Module_Scenery

    @classmethod
    def moduleShowname(cls):
        return cls.LynxiProduct_Module_ShowName_Dic[cls.LynxiProduct_Module_Scenery][1]

    @classmethod
    def linkNames(cls):
        return cls.LynxiProduct_Scenery_Link_Lis

    @classmethod
    def sceneryLinkName(cls):
        return cls.LynxiProduct_Scenery_Link_Scenery

    @classmethod
    def layoutLinkName(cls):
        return cls.LynxiProduct_Scenery_Link_layout

    @classmethod
    def animationLinkName(cls):
        return cls.LynxiProduct_Scenery_Link_Animation

    @classmethod
    def solverLinkName(cls):
        return cls.LynxiProduct_Scenery_Link_Solver

    @classmethod
    def simulationLinkName(cls):
        return cls.LynxiProduct_Scenery_Link_Simulation

    @classmethod
    def lightLinkName(cls):
        return cls.LynxiProduct_Scenery_Link_Light

    @classmethod
    def classShowname(cls, categoryString):
        return cls.LynxiProduct_Scenery_Class_ShowName_Dic[categoryString][1]

    @classmethod
    def isSceneryLinkName(cls, stageString):
        if stageString in lxConfigure.LynxiScnSceneryStages or stageString == cls.LynxiProduct_Scenery_Link_Scenery:
            return True
        return False

    @classmethod
    def isLayoutLinkName(cls, stageString):
        if stageString in lxConfigure.LynxiScLayoutStages or stageString == cls.LynxiProduct_Scene_Link_layout:
            return True
        return False

    @classmethod
    def isAnimationLinkName(cls, stageString):
        if stageString in lxConfigure.LynxiScAnimationStages or stageString == cls.LynxiProduct_Scene_Link_Animation:
            return True
        return False

    @classmethod
    def isSolverLinkName(cls, stageString):
        if stageString in lxConfigure.LynxiScSolverStages or stageString == cls.LynxiProduct_Scene_Link_Solver:
            return True
        return False

    @classmethod
    def isSimulationLinkName(cls, stageString):
        if stageString in lxConfigure.LynxiScSimulationStages or stageString == cls.LynxiProduct_Scene_Link_Simulation:
            return True
        return False

    @classmethod
    def isLightLinkName(cls, stageString):
        if stageString in lxConfigure.LynxiScLightStages or stageString == cls.LynxiProduct_Scene_Link_Light:
            return True
        return False

    @classmethod
    def stageName2linkName(cls, stageString):
        if cls.isSceneryLinkName(stageString):
            return cls.LynxiProduct_Scenery_Link_Scenery
        elif cls.isLayoutLinkName(stageString):
            return cls.LynxiProduct_Scenery_Link_layout
        elif cls.isAnimationLinkName(stageString):
            return cls.LynxiProduct_Scenery_Link_Animation
        elif cls.isSolverLinkName(stageString):
            return cls.LynxiProduct_Scenery_Link_Solver
        elif cls.isSimulationLinkName(stageString):
            return cls.LynxiProduct_Scenery_Link_Simulation
        elif cls.isLightLinkName(stageString):
            return cls.LynxiProduct_Scenery_Link_Light
        return cls.LynxiProduct_Scenery_Link_Scenery

    @classmethod
    def categories(cls):
        return cls.LynxiProduct_Scenery_Class_Lis

    @classmethod
    def isValidCategory(cls, categoryName):
        return categoryName in cls.categories()
    
    @classmethod
    def linkShowname(cls, linkString):
        return cls.LynxiProduct_Scenery_Link_ShowName_Dic[linkString][1]
    
    @classmethod
    def linkShowname_(cls, stageString):
        return cls.linkShowname(cls.stageName2linkName(stageString))

    @classmethod
    def classShownameDic(cls):
        return cls.LynxiProduct_Scenery_Class_UiDatumDic

    @classmethod
    def priorityNames(cls):
        return cls.LynxiUnit_Priority_Lis
    

class PrsSceneBasic(prsConfigure.PrsBasic):
    @classmethod
    def prefix(cls):
        return cls.LynxiProduct_Module_Prefix_Scene

    @classmethod
    def moduleName(cls):
        return cls.LynxiProduct_Module_Scene

    @classmethod
    def moduleShowname(cls):
        return cls.LynxiProduct_Module_ShowName_Dic[cls.LynxiProduct_Module_Scene][1]

    @classmethod
    def linkNames(cls):
        return cls.LynxiProduct_Scene_Link_Lis

    @classmethod
    def layoutLinkName(cls):
        return cls.LynxiProduct_Scene_Link_layout

    @classmethod
    def animationLinkName(cls):
        return cls.LynxiProduct_Scene_Link_Animation

    @classmethod
    def solverLinkName(cls):
        return cls.LynxiProduct_Scene_Link_Solver

    @classmethod
    def simulationLinkName(cls):
        return cls.LynxiProduct_Scene_Link_Simulation

    @classmethod
    def lightLinkName(cls):
        return cls.LynxiProduct_Scene_Link_Light
    
    @classmethod
    def classShowname(cls, categoryString):
        return cls.LynxiProduct_Scene_Class_ShowName_Dic[categoryString][1]

    @classmethod
    def isLayoutLinkName(cls, sceneStage):
        if sceneStage in lxConfigure.LynxiScLayoutStages or sceneStage == cls.LynxiProduct_Scene_Link_layout:
            return True
        return False

    @classmethod
    def isAnimationLinkName(cls, sceneStage):
        if sceneStage in lxConfigure.LynxiScAnimationStages or sceneStage == cls.LynxiProduct_Scene_Link_Animation:
            return True
        return False

    @classmethod
    def isSolverLinkName(cls, sceneStage):
        if sceneStage in lxConfigure.LynxiScSolverStages or sceneStage == cls.LynxiProduct_Scene_Link_Solver:
            return True
        return False

    @classmethod
    def isSimulationLinkName(cls, sceneStage):
        if sceneStage in lxConfigure.LynxiScSimulationStages or sceneStage == cls.LynxiProduct_Scene_Link_Simulation:
            return True
        return False

    @classmethod
    def isLightLinkName(cls, sceneStage):
        if sceneStage in lxConfigure.LynxiScLightStages or sceneStage == cls.LynxiProduct_Scene_Link_Light:
            return True
        return False

    @classmethod
    def stageName2linkName(cls, sceneStage):
        if cls.isLayoutLinkName(sceneStage):
            return cls.LynxiProduct_Scene_Link_layout
        elif cls.isAnimationLinkName(sceneStage):
            return cls.LynxiProduct_Scene_Link_Animation
        elif cls.isSolverLinkName(sceneStage):
            return cls.LynxiProduct_Scene_Link_Solver
        elif cls.isSimulationLinkName(sceneStage):
            return cls.LynxiProduct_Scene_Link_Simulation
        elif cls.isLightLinkName(sceneStage):
            return cls.LynxiProduct_Scene_Link_Light
        return cls.LynxiProduct_Scene_Link_layout
    
    @classmethod
    def categories(cls):
        return cls.LynxiProduct_Scene_Class_Lis

    @classmethod
    def isValidCategory(cls, categoryName):
        return categoryName in cls.categories()

    @classmethod
    def linkShowname(cls, linkString):
        return cls.LynxiProduct_Scene_Link_ShowName_Dic[linkString][1]

    @classmethod
    def linkShowname_(cls, stageString):
        return cls.linkShowname(cls.stageName2linkName(stageString))

    @classmethod
    def classShownameDic(cls):
        return cls.LynxiProduct_Scene_Class_UiDatumDic

    @classmethod
    def priorityNames(cls):
        return cls.LynxiUnit_Priority_Lis
