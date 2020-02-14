# coding:utf-8
from LxBasic import bscConfigure

from LxPreset import prsConfigure

from LxCore import lxConfigure


class Mtd_PrsBasic(prsConfigure.PrsBasic):
    pass


class Mtd_PrsProductBasic(prsConfigure.PrsProduct):
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
    def isValidAssetCategoryName(cls, categoryString):
        return categoryString in cls.VAR_product_asset_category_list

    @classmethod
    def isValidSceneryCategoryName(cls, categoryString):
        return categoryString in cls.VAR_product_scenery_category_Lis

    @classmethod
    def isValidSceneCategoryName(cls, categoryString):
        return categoryString in cls.VAR_product_scene_category_list

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
            [(cls.VAR_product_key_Variant, u'变体 [ Variant(s) ]'), (bscConfigure.MtdBasic.DEF_Value_Default,)],
            [(cls.VAR_product_key_category, u'类型 [ Category ]'), cls._lxProductClassUiDatumDic(moduleString)],
            [(cls.VAR_product_key_priority, u'优先级 [ Priority ]'), cls._lxProductPriorityUiDatum(moduleString)]
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
        return cls.VAR_product_attribute_list

    @classmethod
    def isValidAttributeName(cls, attributeName):
        return attributeName in cls.attributeNames()

    @classmethod
    def rootLabel(cls):
        return cls.VAR_product_label_root
    
 
class Mtd_PrsAssetBasic(prsConfigure.PrsProduct):
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
    def isModelStageName(cls, stageString):
        if stageString in lxConfigure.LynxiAstModelStages or stageString == cls.VAR_product_asset_link_model:
            return True
        return False

    @classmethod
    def isRigStageName(cls, stageString):
        if stageString in lxConfigure.LynxiAstRigStages or stageString == cls.VAR_product_asset_link_rig:
            return True
        return False

    @classmethod
    def isGroomStageName(cls, stageString):
        if stageString in lxConfigure.LynxiAstCfxStages or stageString == cls.VAR_product_asset_link_groom:
            return True
        return False

    @classmethod
    def isSolverStageName(cls, stageString):
        if stageString in lxConfigure.LynxiAstRigSolStages or stageString == cls.VAR_product_asset_link_solver:
            return True
        return False

    @classmethod
    def isLightStageName(cls, stageString):
        if stageString in lxConfigure.LynxiScLightStages or stageString == cls.VAR_product_asset_link_light:
            return True
        return False

    @classmethod
    def isAssemblyStageName(cls, stageString):
        if stageString in lxConfigure.LynxiAstAssemblyStages or stageString == cls.VAR_product_asset_link_assembly:
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
    def classShowname(cls, categoryString):
        return cls.VAR_product_asset_category_showname_dict[categoryString][1]
    
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


class Mtd_PrsSceneryBasic(prsConfigure.PrsProduct):
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
    def sceneryLinkName(cls):
        return cls.VAR_product_scenery_link_scenery

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
    def classShowname(cls, categoryString):
        return cls.VAR_product_scenery_category_showname_dict[categoryString][1]

    @classmethod
    def isSceneryLinkName(cls, stageString):
        if stageString in lxConfigure.LynxiScnSceneryStages or stageString == cls.VAR_product_scenery_link_scenery:
            return True
        return False

    @classmethod
    def isLayoutLinkName(cls, stageString):
        if stageString in lxConfigure.LynxiScLayoutStages or stageString == cls.VAR_product_scene_link_layout:
            return True
        return False

    @classmethod
    def isAnimationLinkName(cls, stageString):
        if stageString in lxConfigure.LynxiScAnimationStages or stageString == cls.VAR_product_scene_link_animation:
            return True
        return False

    @classmethod
    def isSolverLinkName(cls, stageString):
        if stageString in lxConfigure.LynxiScSolverStages or stageString == cls.VAR_product_scene_link_solver:
            return True
        return False

    @classmethod
    def isSimulationLinkName(cls, stageString):
        if stageString in lxConfigure.LynxiScSimulationStages or stageString == cls.VAR_product_scene_link_simulation:
            return True
        return False

    @classmethod
    def isLightLinkName(cls, stageString):
        if stageString in lxConfigure.LynxiScLightStages or stageString == cls.VAR_product_scene_link_light:
            return True
        return False

    @classmethod
    def stageName2linkName(cls, stageString):
        if cls.isSceneryLinkName(stageString):
            return cls.VAR_product_scenery_link_scenery
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
        return cls.VAR_product_scenery_link_scenery

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
    

class Mtd_PrsSceneBasic(prsConfigure.PrsProduct):
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
    def classShowname(cls, categoryString):
        return cls.VAR_product_scene_category_showname_dict[categoryString][1]

    @classmethod
    def isLayoutLinkName(cls, sceneStage):
        if sceneStage in lxConfigure.LynxiScLayoutStages or sceneStage == cls.VAR_product_scene_link_layout:
            return True
        return False

    @classmethod
    def isAnimationLinkName(cls, sceneStage):
        if sceneStage in lxConfigure.LynxiScAnimationStages or sceneStage == cls.VAR_product_scene_link_animation:
            return True
        return False

    @classmethod
    def isSolverLinkName(cls, sceneStage):
        if sceneStage in lxConfigure.LynxiScSolverStages or sceneStage == cls.VAR_product_scene_link_solver:
            return True
        return False

    @classmethod
    def isSimulationLinkName(cls, sceneStage):
        if sceneStage in lxConfigure.LynxiScSimulationStages or sceneStage == cls.VAR_product_scene_link_simulation:
            return True
        return False

    @classmethod
    def isLightLinkName(cls, sceneStage):
        if sceneStage in lxConfigure.LynxiScLightStages or sceneStage == cls.VAR_product_scene_link_light:
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
