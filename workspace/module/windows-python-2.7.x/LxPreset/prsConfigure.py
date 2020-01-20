# coding:utf-8
import collections

from LxCore import lxConfigure


class Product(object):
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
    LynxiProduct_Module_UiSetDic = collections.OrderedDict(
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
    LynxiProduct_Asset_Class_UiSetDic = collections.OrderedDict(
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
    LynxiProduct_Scenery_Class_UiSetDic = collections.OrderedDict(
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
    LynxiProduct_Scene_Class_UiSetDic = collections.OrderedDict(
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
    LynxiUnit_Priority_UiSetDic = collections.OrderedDict(
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
    LynxiProduct_Asset_Link_Cfx = 'cfx'
    LynxiProduct_Asset_Link_Solver = 'solver'
    LynxiProduct_Asset_Link_Light = 'light'
    LynxiProduct_Asset_Link_Assembly = 'assembly'
    #
    LynxiProduct_Asset_Link_Lis = [
        LynxiProduct_Asset_Link_Model,
        LynxiProduct_Asset_Link_Rig,
        LynxiProduct_Asset_Link_Cfx,
        LynxiProduct_Asset_Link_Solver,
        LynxiProduct_Asset_Link_Light,
        LynxiProduct_Asset_Link_Assembly
    ]
    LynxiProduct_Asset_Link_UiSetDic = collections.OrderedDict(
        [
            (LynxiProduct_Asset_Link_Model, ('Model', u'模型')),
            (LynxiProduct_Asset_Link_Rig, ('Rig', u'绑定')),
            (LynxiProduct_Asset_Link_Cfx, ('Groom', u'毛发塑形')),
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
    #
    LynxiProduct_Scenery_Link_Lis = [
        LynxiProduct_Scenery_Link_Scenery,
        LynxiProduct_Scenery_Link_layout,
        LynxiProduct_Scenery_Link_Animation,
        LynxiProduct_Scenery_Link_Simulation,
        LynxiProduct_Scenery_Link_Solver,
        LynxiProduct_Scenery_Link_Light
    ]
    LynxiProduct_Scenery_Link_UiSetDic = collections.OrderedDict(
        [
            (LynxiProduct_Scenery_Link_Scenery, ('Scenery', u'场景布景')),
            (LynxiProduct_Scenery_Link_layout, ('Layout', u'场景预览')),
            (LynxiProduct_Scenery_Link_Animation, ('Animation', u'场景动画')),
            (LynxiProduct_Scenery_Link_Simulation, ('Simulation', u'场景解算')),
            (LynxiProduct_Scenery_Link_Solver, ('Solver', u'场景模拟')),
            (LynxiProduct_Scenery_Link_Light, ('Light', u'场景灯光'))
        ]
    )
    # Scene
    LynxiProduct_Scene_Link_layout = 'layout'
    LynxiProduct_Scene_Link_Animation = 'animation'
    LynxiProduct_Scene_Link_Simulation = 'simulation'
    LynxiProduct_Scene_Link_Solver = 'solver'
    LynxiProduct_Scene_Link_Light = 'light'
    #
    LynxiProduct_Scene_Link_Lis = [
        LynxiProduct_Scene_Link_layout,
        LynxiProduct_Scene_Link_Animation,
        LynxiProduct_Scene_Link_Simulation,
        LynxiProduct_Scene_Link_Solver,
        LynxiProduct_Scene_Link_Light
    ]
    LynxiProduct_Scene_Link_UiSetDic = collections.OrderedDict(
        [
            (LynxiProduct_Scene_Link_layout, ('Layout', u'镜头预览')),
            (LynxiProduct_Scene_Link_Animation, ('Animation', u'镜头动画')),
            (LynxiProduct_Scene_Link_Simulation, ('Simulation', u'镜头解算')),
            (LynxiProduct_Scene_Link_Solver, ('Solver', u'镜头模拟')),
            (LynxiProduct_Scene_Link_Light, ('Light', u'镜头灯光'))
        ]
    )
    #
    LynxiProduct_Module_Class_Dic = {
        LynxiProduct_Module_Asset: LynxiProduct_Asset_Class_Lis,
        LynxiProduct_Module_Scenery: LynxiProduct_Scenery_Class_Lis,
        LynxiProduct_Module_Scene: LynxiProduct_Scene_Class_Lis
    }
    #
    LynxiUnit_Label_Root = 'unitRoot'
    #
    LynxiUnit_AttrName_ID = 'index'
    LynxiUnit_AttrName_Class = 'classification'
    LynxiUnit_AttrName_Name = 'name'
    LynxiUnit_AttrName_Variant = 'variant'
    LynxiUnit_AttrName_Stage = 'stage'
    #
    LynxiProduct_Unit_AttrNameLis = [
        LynxiUnit_AttrName_ID,
        LynxiUnit_AttrName_Class,
        LynxiUnit_AttrName_Name,
        LynxiUnit_AttrName_Variant,
        LynxiUnit_AttrName_Stage
    ]
    #
    LynxiProduct_Unit_Key_Project = 'project'
    LynxiProduct_Unit_Key_Class = 'classify'
    LynxiProduct_Unit_Key_Priority = 'priority'
    LynxiProduct_Unit_Key_Name = 'name'
    LynxiProduct_Unit_Key_Variant = 'variant'
    #
    LynxiProduct_Stage_Pending = 'pending'
    LynxiProduct_Stage_Wip = 'wip'
    LynxiProduct_Stage_Delivery = 'delivery'
    LynxiProduct_Stage_Refine = 'refine'
    LynxiProduct_Stage_Validated = 'validated'
    LynxiProduct_Stage_UiSetDic = {
        LynxiProduct_Stage_Pending: ('Pending', u'等待'),
        LynxiProduct_Stage_Wip: ('WIP', u'制作'),
        LynxiProduct_Stage_Delivery: ('Delivery', u'提交'),
        LynxiProduct_Stage_Refine: ('Refine', u'返修'),
        LynxiProduct_Stage_Validated: ('Validated', u'通过')
    }

    @classmethod
    def modulenames(cls):
        return cls.LynxiProduct_ModuleLis

    @classmethod
    def moduleShowname(cls, moduleString):
        return cls.LynxiProduct_Module_UiSetDic[moduleString][1]

    @classmethod
    def modulePrefixname(cls, moduleString):
        return cls.LynxiProduct_Module_PrefixDic[moduleString]

    @classmethod
    def isModuleValid(cls, moduleString):
        return moduleString in cls.LynxiProduct_ModuleLis

    @staticmethod
    def _toProductUnitName(number):
        return 'ID{}'.format(str(number).zfill(6))

    @classmethod
    def isLxAssetClass(cls, unitClass):
        return unitClass in cls.LynxiProduct_Asset_Class_Lis

    @classmethod
    def isLxSceneryClass(cls, unitClass):
        return unitClass in cls.LynxiProduct_Scenery_Class_Lis

    @classmethod
    def isLxSceneClass(cls, unitClass):
        return unitClass in cls.LynxiProduct_Scene_Class_Lis

    @classmethod
    def getDbProductModule(cls, unitClass):
        if cls.isLxAssetClass(unitClass):
            return cls.LynxiProduct_Module_Asset
        elif cls.isLxSceneryClass(unitClass):
            return cls.LynxiProduct_Module_Scenery
        elif cls.isLxSceneClass(unitClass):
            return cls.LynxiProduct_Module_Scene

    @classmethod
    def moduleClassnames(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Asset_Class_Lis
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Scenery_Class_Lis
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Scene_Class_Lis

    @classmethod
    def moduleClassShownames(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Asset_Class_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Scenery_Class_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Scene_Class_UiSetDic

    @classmethod
    def _lxProductClassUiDatumDic(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Asset_Class_UiDatumDic
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Scenery_Class_UiDatumDic
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Scene_Class_UiDatumDic

    @classmethod
    def _lxProductPriorityUiDatum(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiUnit_Priority_UiDatumDic
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiUnit_Priority_UiDatumDic
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiUnit_Priority_UiDatumDic

    @classmethod
    def _lxProductLinkLis(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Asset_Link_Lis
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Scenery_Link_Lis
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Scene_Link_Lis

    @classmethod
    def _lxProductLinkUiSetDic(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Asset_Link_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Scenery_Link_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Scene_Link_UiSetDic

    @classmethod
    def _lxProductStageUiSetDic(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Stage_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Stage_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Stage_UiSetDic

    @classmethod
    def getLxPriorityKeyLisByProductModule(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiUnit_Priority_Lis
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiUnit_Priority_Lis
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiUnit_Priority_Lis

    @classmethod
    def _lxProductPriorityUiSetDic(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiUnit_Priority_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiUnit_Priority_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiUnit_Priority_UiSetDic

    @classmethod
    def lxDbProductUnitDefaultSetConfig(cls, projectName, productModule, number):
        def addLinkDatum():
            linkUiDic = cls._lxProductLinkUiSetDic(productModule)
            if linkUiDic:
                for k, v in linkUiDic.items():
                    lis.append(
                        [(k, u'{} [ {} ]'.format(v[1], v[0])), False]
                    )
        #
        lis = [
            [(cls.LynxiProduct_Unit_Key_Project, u'项目 [ Project(s) ]'), (projectName,)],
            [(cls.LynxiProduct_Unit_Key_Name, u'名字 [ Name ]'), cls._toProductUnitName(number)],
            [(cls.LynxiProduct_Unit_Key_Variant, u'变体 [ Variant(s) ]'), (lxConfigure.STR_Value_Default,)],
            [(cls.LynxiProduct_Unit_Key_Class, u'类型 [ Classify ]'), cls._lxProductClassUiDatumDic(productModule)],
            [(cls.LynxiProduct_Unit_Key_Priority, u'优先级 [ Priority ]'), cls._lxProductPriorityUiDatum(productModule)]
        ]
        addLinkDatum()
        return lis

    @classmethod
    def lxProductUnitViewInfoSet(cls, productModule, unitClass, unitViewName, extendString=None):
        unitViewClass = cls.moduleClassShownames(productModule)[unitClass]
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
    def prioritynames(cls):
        return cls.LynxiUnit_Priority_Lis
    
 
class Asset(Product):
    @classmethod
    def prefix(cls):
        return cls.LynxiProduct_Module_Prefix_Asset

    @classmethod
    def name(cls):
        return cls.LynxiProduct_Module_Asset

    @classmethod
    def showname(cls):
        return cls.moduleShowname(cls.LynxiProduct_Module_Asset)

    @classmethod
    def linknames(cls):
        return cls.LynxiProduct_Asset_Link_Lis
    
    @classmethod
    def isAstModelLink(cls, stageString):
        if stageString in lxConfigure.LynxiAstModelStages or stageString == cls.LynxiProduct_Asset_Link_Model:
            return True
        return False

    @classmethod
    def isAstRigLink(cls, stageString):
        if stageString in lxConfigure.LynxiAstRigStages or stageString == cls.LynxiProduct_Asset_Link_Rig:
            return True
        return False

    @classmethod
    def isAstCfxLink(cls, stageString):
        if stageString in lxConfigure.LynxiAstCfxStages or stageString == cls.LynxiProduct_Asset_Link_Cfx:
            return True
        return False

    @classmethod
    def isAstSolverLink(cls, stageString):
        if stageString in lxConfigure.LynxiAstRigSolStages or stageString == cls.LynxiProduct_Asset_Link_Solver:
            return True
        return False

    @classmethod
    def isAstLightLink(cls, stageString):
        if stageString in lxConfigure.LynxiScLightStages or stageString == cls.LynxiProduct_Asset_Link_Light:
            return True
        return False

    @classmethod
    def isAstAssemblyLink(cls, stageString):
        if stageString in lxConfigure.LynxiAstAssemblyStages or stageString == cls.LynxiProduct_Asset_Link_Assembly:
            return True
        return False
    
    @classmethod
    def stagename2linkname(cls, stageString):
        if cls.isAstModelLink(stageString):
            return cls.LynxiProduct_Asset_Link_Model
        elif cls.isAstRigLink(stageString):
            return cls.LynxiProduct_Asset_Link_Rig
        elif cls.isAstCfxLink(stageString):
            return cls.LynxiProduct_Asset_Link_Cfx
        elif cls.isAstSolverLink(stageString):
            return cls.LynxiProduct_Asset_Link_Solver
        elif cls.isAstLightLink(stageString):
            return cls.LynxiProduct_Asset_Link_Light
        return lxConfigure.LynxiProduct_Asset_Link_Model
    
    @classmethod
    def classShowname(cls, classString):
        return cls.LynxiProduct_Asset_Class_UiSetDic[classString][1]
    
    @classmethod
    def linkShowname(cls, linkString):
        return cls.LynxiProduct_Asset_Link_UiSetDic[linkString][1]
    
    @classmethod
    def linkShowname_(cls, stageString):
        return cls.linkShowname(cls.stagename2linkname(stageString))

    @classmethod
    def classShownameDic(cls):
        return cls.LynxiProduct_Asset_Class_UiDatumDic


class Scenery(Product):
    @classmethod
    def prefix(cls):
        return cls.LynxiProduct_Module_Prefix_Scenery

    @classmethod
    def name(cls):
        return cls.LynxiProduct_Module_Scenery

    @classmethod
    def showname(cls):
        return cls.moduleShowname(cls.LynxiProduct_Module_Scenery)

    @classmethod
    def linknames(cls):
        return cls.LynxiProduct_Scenery_Link_Lis
    
    @classmethod
    def classShowname(cls, classString):
        return cls.LynxiProduct_Scenery_Class_UiSetDic[classString][1]

    @classmethod
    def isScnSceneryLink(cls, stageString):
        if stageString in lxConfigure.LynxiScnSceneryStages or stageString == cls.LynxiProduct_Scenery_Link_Scenery:
            return True
        return False

    @classmethod
    def isScnLayoutLink(cls, stageString):
        if stageString in lxConfigure.LynxiScLayoutStages or stageString == cls.LynxiProduct_Scene_Link_layout:
            return True
        return False

    @classmethod
    def isScnAnimationLink(cls, stageString):
        if stageString in lxConfigure.LynxiScAnimationStages or stageString == cls.LynxiProduct_Scene_Link_Animation:
            return True
        return False

    @classmethod
    def isScnSimulationLink(cls, stageString):
        if stageString in lxConfigure.LynxiScSimulationStages or stageString == cls.LynxiProduct_Scene_Link_Simulation:
            return True
        return False

    @classmethod
    def isScnLightLink(cls, stageString):
        if stageString in lxConfigure.LynxiScLightStages or stageString == cls.LynxiProduct_Scene_Link_Light:
            return True
        return False

    @classmethod
    def stagename2linkname(cls, stageString):
        if cls.isScnSceneryLink(stageString):
            return cls.LynxiProduct_Scenery_Link_Scenery
        elif cls.isScnLayoutLink(stageString):
            return cls.LynxiProduct_Scene_Link_layout
        elif cls.isScnAnimationLink(stageString):
            return cls.LynxiProduct_Scene_Link_Animation
        elif cls.isScnSimulationLink(stageString):
            return cls.LynxiProduct_Scene_Link_Simulation
        elif cls.isScnLightLink(stageString):
            return cls.LynxiProduct_Scene_Link_Light
        return cls.LynxiProduct_Scenery_Link_Scenery
    
    @classmethod
    def linkShowname(cls, linkString):
        return cls.LynxiProduct_Scenery_Link_UiSetDic[linkString][1]
    
    @classmethod
    def linkShowname_(cls, stageString):
        return cls.linkShowname(cls.stagename2linkname(stageString))

    @classmethod
    def classShownameDic(cls):
        return cls.LynxiProduct_Scenery_Class_UiDatumDic
    

class Scene(Product):
    @classmethod
    def prefix(cls):
        return cls.LynxiProduct_Module_Prefix_Scene

    @classmethod
    def name(cls):
        return cls.LynxiProduct_Module_Scene

    @classmethod
    def showname(cls):
        return cls.moduleShowname(cls.LynxiProduct_Module_Scene)

    @classmethod
    def linknames(cls):
        return cls.LynxiProduct_Scene_Link_Lis
    
    @classmethod
    def classShowname(cls, classString):
        return cls.LynxiProduct_Scene_Class_UiSetDic[classString][1]

    @classmethod
    def isScLayoutLink(cls, sceneStage):
        boolean = False
        if sceneStage in lxConfigure.LynxiScLayoutStages or sceneStage == cls.LynxiProduct_Scene_Link_layout:
            boolean = True
        return boolean

    @classmethod
    def isScAnimationLink(cls, sceneStage):
        if sceneStage in lxConfigure.LynxiScAnimationStages or sceneStage == cls.LynxiProduct_Scene_Link_Animation:
            return True
        return False

    @classmethod
    def isScSolverLink(cls, sceneStage):
        if sceneStage in lxConfigure.LynxiScSolverStages or sceneStage == cls.LynxiProduct_Scene_Link_Solver:
            return True
        return False

    @classmethod
    def isScSimulationLink(cls, sceneStage):
        if sceneStage in lxConfigure.LynxiScSimulationStages or sceneStage == cls.LynxiProduct_Scene_Link_Simulation:
            return True
        return False

    @classmethod
    def isScLightLink(cls, sceneStage):
        if sceneStage in lxConfigure.LynxiScLightStages or sceneStage == cls.LynxiProduct_Scene_Link_Light:
            return True
        return False

    @classmethod
    def stagename2linkname(cls, sceneStage):
        if cls.isScLayoutLink(sceneStage):
            return lxConfigure.LynxiProduct_Scene_Link_layout
        elif cls.isScAnimationLink(sceneStage):
            return lxConfigure.LynxiProduct_Scene_Link_Animation
        elif cls.isScSolverLink(sceneStage):
            return lxConfigure.LynxiProduct_Scene_Link_Solver
        elif cls.isScSimulationLink(sceneStage):
            return lxConfigure.LynxiProduct_Scene_Link_Simulation
        elif cls.isScLightLink(sceneStage):
            return lxConfigure.LynxiProduct_Scene_Link_Light
        return lxConfigure.LynxiProduct_Scene_Link_layout

    @classmethod
    def linkShowname(cls, linkString):
        return cls.LynxiProduct_Scene_Link_UiSetDic[linkString][1]

    @classmethod
    def linkShowname_(cls, stageString):
        return cls.linkShowname(cls.stagename2linkname(stageString))

    @classmethod
    def classShownameDic(cls):
        return cls.LynxiProduct_Scene_Class_UiDatumDic
