# coding:utf-8
import collections

from LxBasic import bscMethods

from LxCore import lxConfigure


class Basic(object):
    # Module
    LynxiProduct_Module_Asset = 'asset'
    LynxiProduct_Module_Prefix_Asset = 'ast'
    LynxiProduct_Module_Scenery = 'scenery'
    LynxiProduct_Module_Prefix_Scenery = 'scn'
    LynxiProduct_Module_Scene = 'scene'
    LynxiProduct_Module_Prefix_Scene = 'sc'
    #
    LynxiProduct_ModuleLis = [
        LynxiProduct_Module_Asset,
        LynxiProduct_Module_Scenery,
        LynxiProduct_Module_Scene
    ]
    #
    LynxiProduct_Module_PrefixDic = {
        LynxiProduct_Module_Asset: LynxiProduct_Module_Prefix_Asset,
        LynxiProduct_Module_Scenery: LynxiProduct_Module_Prefix_Scenery,
        LynxiProduct_Module_Scene: LynxiProduct_Module_Prefix_Scene
    }
    LynxiProduct_Module_ShowName_Dic = collections.OrderedDict(
        [
            (LynxiProduct_Module_Asset, ('Asset', u'资产')),
            (LynxiProduct_Module_Scenery, ('Scenery', u'场景')),
            (LynxiProduct_Module_Scene, ('Scene', u'镜头'))
        ]
    )
    # Asset
    LynxiProduct_Asset_Class_Character = 'character'
    LynxiProduct_Asset_Class_Prop = 'prop'
    #
    LynxiProduct_Asset_Class_Lis = [
        LynxiProduct_Asset_Class_Character,
        LynxiProduct_Asset_Class_Prop
    ]
    LynxiProduct_Asset_Class_ShowName_Dic = collections.OrderedDict(
        [
            (LynxiProduct_Asset_Class_Character, ('Character', u'角色')),
            (LynxiProduct_Asset_Class_Prop, ('Prop', u'道具'))
        ]
    )
    LynxiProduct_Asset_Class_UiDatumDic = collections.OrderedDict(
        [
            ('ast0', (LynxiProduct_Asset_Class_Character, u'角色')),
            ('ast1', (LynxiProduct_Asset_Class_Prop, u'道具'))
        ]
    )
    # Scenery
    LynxiProduct_Scenery_Class_Scenery = 'scenery'
    LynxiProduct_Scenery_Class_Group = 'group'
    LynxiProduct_Scenery_Class_Assembly = 'assembly'
    #
    LynxiProduct_Scenery_Class_Lis = [
        LynxiProduct_Scenery_Class_Scenery,
        LynxiProduct_Scenery_Class_Group,
        LynxiProduct_Scenery_Class_Assembly
    ]
    LynxiProduct_Scenery_Class_ShowName_Dic = collections.OrderedDict(
        [
            (LynxiProduct_Scenery_Class_Scenery, ('Scenery', u'场景')),
            (LynxiProduct_Scenery_Class_Group, ('Group', u'组合')),
            (LynxiProduct_Scenery_Class_Assembly, ('Assembly', u'组装'))
        ]
    )
    LynxiProduct_Scenery_Class_UiDatumDic = collections.OrderedDict(
        [
            ('scn0', (LynxiProduct_Scenery_Class_Scenery, u'场景')),
            ('scn1', (LynxiProduct_Scenery_Class_Group, u'组合')),
            ('scn2', (LynxiProduct_Scenery_Class_Assembly, u'组装'))
        ]
    )
    # Scene
    LynxiProduct_Scene_Class_Scene = 'scene'
    LynxiProduct_Scene_Class_Act = 'act'
    #
    LynxiProduct_Scene_Class_Lis = [
        LynxiProduct_Scene_Class_Scene,
        LynxiProduct_Scene_Class_Act
    ]
    LynxiProduct_Scene_Class_ShowName_Dic = collections.OrderedDict(
        [
            (LynxiProduct_Scene_Class_Scene, ('Scene', u'镜头')),
            (LynxiProduct_Scene_Class_Act, ('Act', u'动作'))
        ]
    )
    LynxiProduct_Scene_Class_UiDatumDic = collections.OrderedDict(
        [
            ('sc0', (LynxiProduct_Scene_Class_Scene, u'镜头')),
            ('sc1', (LynxiProduct_Scene_Class_Act, u'动作'))
        ]
    )
    # Priority
    LynxiUnit_Priority_Major = 'major'
    LynxiUnit_Priority_Minor = 'minor'
    LynxiUnit_Priority_Util = 'util'
    #
    LynxiUnit_Priority_Lis = [
        LynxiUnit_Priority_Major,
        LynxiUnit_Priority_Minor,
        LynxiUnit_Priority_Util
    ]
    LynxiUnit_Priority_ShowName_Dic = collections.OrderedDict(
        [
            (LynxiUnit_Priority_Major, ('Major', u'主要')),
            (LynxiUnit_Priority_Minor, ('Minor', u'次要')),
            (LynxiUnit_Priority_Util, ('Util', u'龙套'))
        ]
    )
    LynxiUnit_Priority_UiDatumDic = collections.OrderedDict(
        [
            ('prt0', (LynxiUnit_Priority_Major, u'主要')),
            ('prt1', (LynxiUnit_Priority_Minor, u'次要')),
            ('prt2', (LynxiUnit_Priority_Util, u'龙套'))
        ]
    )
    # Asset
    LynxiProduct_Asset_Link_Model = 'model'
    LynxiProduct_Asset_Link_Rig = 'rig'
    LynxiProduct_Asset_Link_Groom = 'cfx'
    LynxiProduct_Asset_Link_Solver = 'solver'
    LynxiProduct_Asset_Link_Light = 'light'
    LynxiProduct_Asset_Link_Assembly = 'assembly'
    #
    LynxiProduct_Asset_Link_Lis = [
        LynxiProduct_Asset_Link_Model,
        LynxiProduct_Asset_Link_Rig,
        LynxiProduct_Asset_Link_Groom,
        LynxiProduct_Asset_Link_Solver,
        LynxiProduct_Asset_Link_Light,
        LynxiProduct_Asset_Link_Assembly
    ]
    LynxiProduct_Asset_Link_ShowName_Dic = collections.OrderedDict(
        [
            (LynxiProduct_Asset_Link_Model, ('Model', u'模型')),
            (LynxiProduct_Asset_Link_Rig, ('Rig', u'绑定')),
            (LynxiProduct_Asset_Link_Groom, ('Groom', u'毛发塑形')),
            (LynxiProduct_Asset_Link_Solver, ('Solver Rig', u'毛发绑定')),
            (LynxiProduct_Asset_Link_Light, ('Light', u'灯光')),
            (LynxiProduct_Asset_Link_Assembly, ('Assembly', u'组装'))
        ]
    )
    # Scenery
    LynxiProduct_Scenery_Link_Scenery = 'scenery'
    LynxiProduct_Scenery_Link_layout = 'layout'
    LynxiProduct_Scenery_Link_Animation = 'animation'
    LynxiProduct_Scenery_Link_Simulation = 'simulation'
    LynxiProduct_Scenery_Link_Solver = 'solver'
    LynxiProduct_Scenery_Link_Light = 'light'

    LynxiProduct_Scenery_Link_Lis = [
        LynxiProduct_Scenery_Link_Scenery,
        LynxiProduct_Scenery_Link_layout,
        LynxiProduct_Scenery_Link_Animation,
        LynxiProduct_Scenery_Link_Simulation,
        LynxiProduct_Scenery_Link_Solver,
        LynxiProduct_Scenery_Link_Light
    ]
    LynxiProduct_Scenery_Link_ShowName_Dic = collections.OrderedDict(
        [
            (LynxiProduct_Scenery_Link_Scenery, ('Scenery', u'场景布景')),
            (LynxiProduct_Scenery_Link_layout, ('Layout', u'场景预览')),
            (LynxiProduct_Scenery_Link_Animation, ('Animation', u'场景动画')),
            (LynxiProduct_Scenery_Link_Simulation, ('Simulation', u'场景解算')),
            (LynxiProduct_Scenery_Link_Solver, ('Solver', u'场景模拟')),
            (LynxiProduct_Scenery_Link_Light, ('Light', u'场景灯光'))
        ]
    )

    LynxiProduct_Scene_Link_layout = 'layout'
    LynxiProduct_Scene_Link_Animation = 'animation'
    LynxiProduct_Scene_Link_Simulation = 'simulation'
    LynxiProduct_Scene_Link_Solver = 'solver'
    LynxiProduct_Scene_Link_Light = 'light'

    LynxiProduct_Scene_Link_Lis = [
        LynxiProduct_Scene_Link_layout,
        LynxiProduct_Scene_Link_Animation,
        LynxiProduct_Scene_Link_Simulation,
        LynxiProduct_Scene_Link_Solver,
        LynxiProduct_Scene_Link_Light
    ]
    LynxiProduct_Scene_Link_ShowName_Dic = collections.OrderedDict(
        [
            (LynxiProduct_Scene_Link_layout, ('Layout', u'镜头预览')),
            (LynxiProduct_Scene_Link_Animation, ('Animation', u'镜头动画')),
            (LynxiProduct_Scene_Link_Simulation, ('Simulation', u'镜头解算')),
            (LynxiProduct_Scene_Link_Solver, ('Solver', u'镜头模拟')),
            (LynxiProduct_Scene_Link_Light, ('Light', u'镜头灯光'))
        ]
    )

    LynxiProduct_Module_Class_Dic = {
        LynxiProduct_Module_Asset: LynxiProduct_Asset_Class_Lis,
        LynxiProduct_Module_Scenery: LynxiProduct_Scenery_Class_Lis,
        LynxiProduct_Module_Scene: LynxiProduct_Scene_Class_Lis
    }

    LynxiUnit_Label_Root = 'unitRoot'

    LynxiUnit_AttrName_Id = 'index'
    LynxiUnit_AttrName_Class = 'classification'
    LynxiUnit_AttrName_Name = 'name'
    LynxiUnit_AttrName_Variant = 'variant'
    LynxiUnit_AttrName_Stage = 'stage'

    LynxiProduct_Unit_AttrNameLis = [
        LynxiUnit_AttrName_Id,
        LynxiUnit_AttrName_Class,
        LynxiUnit_AttrName_Name,
        LynxiUnit_AttrName_Variant,
        LynxiUnit_AttrName_Stage
    ]

    LynxiProduct_Unit_Key_Project = 'project'
    LynxiProduct_Unit_Key_Category = 'classify'
    LynxiProduct_Unit_Key_Module = 'module'
    LynxiProduct_Unit_Key_Link = 'link'
    LynxiProduct_Unit_Key_Stage = 'stage'

    LynxiProduct_Unit_Key_Priority = 'priority'
    LynxiProduct_Unit_Key_Name = 'name'
    LynxiProduct_Unit_Key_Variant = 'variant'

    LynxiProduct_Step_Pending = 'pending'
    LynxiProduct_Step_Wip = 'wip'
    LynxiProduct_Step_Delivery = 'delivery'
    LynxiProduct_Step_Refine = 'refine'
    LynxiProduct_Step_Validated = 'validated'

    LynxiProduct_Step_Lis = [
        LynxiProduct_Step_Pending,
        LynxiProduct_Step_Wip,
        LynxiProduct_Step_Delivery,
        LynxiProduct_Step_Refine,
        LynxiProduct_Step_Validated
    ]

    LynxiProduct_Step_ShowName_Dic = {
        LynxiProduct_Step_Pending: ('Pending', u'等待'),
        LynxiProduct_Step_Wip: ('WIP', u'制作'),
        LynxiProduct_Step_Delivery: ('Delivery', u'提交'),
        LynxiProduct_Step_Refine: ('Refine', u'返修'),
        LynxiProduct_Step_Validated: ('Validated', u'通过')
    }


class Product(Basic):
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
            [(cls.LynxiProduct_Unit_Key_Variant, u'变体 [ Variant(s) ]'), (lxConfigure.STR_Value_Default,)],
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
    
 
class Asset(Basic):
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
    def linknames(cls):
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
    def categoryNames(cls):
        return cls.LynxiProduct_Asset_Class_Lis
    
    @classmethod
    def isValidCategoryName(cls, categoryName):
        return categoryName in cls.categoryNames()

    @classmethod
    def isCharacterCategoryName(cls, categoryName):
        return categoryName == cls.LynxiProduct_Asset_Class_Character

    @classmethod
    def isPropCategoryName(cls, categoryName):
        return categoryName == cls.LynxiProduct_Asset_Class_Prop

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


class Scenery(Basic):
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
    def linknames(cls):
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
    def categoryNames(cls):
        return cls.LynxiProduct_Scenery_Class_Lis

    @classmethod
    def isValidCategoryName(cls, categoryName):
        return categoryName in cls.categoryNames()
    
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
    

class Scene(Basic):
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
    def linknames(cls):
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
    def categoryNames(cls):
        return cls.LynxiProduct_Scene_Class_Lis

    @classmethod
    def isValidCategoryName(cls, categoryName):
        return categoryName in cls.categoryNames()

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
