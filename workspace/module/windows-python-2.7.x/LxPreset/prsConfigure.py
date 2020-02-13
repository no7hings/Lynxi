# coding:utf-8
from LxBasic import bscCore

DIC_path_database = {
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

DIC_path_asset = {
    'basic': '{basicAssetFolder}/{basicUnitFolder}',
    'model': '{basicAssetFolder}/{basicUnitFolder}/{asset.variant}',
    'rig': '{basicAssetFolder}/{basicUnitFolder}',
    'groom': '{basicAssetFolder}/{basicUnitFolder}/{asset.variant}',
    'solver': '{basicAssetFolder}/{basicUnitFolder}/{asset.variant}/{astSolverFolder}',
    'light': '{basicAssetFolder}/{basicUnitFolder}/{asset.variant}/{astLightFolder}',
}


class PrsBasic(object):
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
    LynxiProduct_Module_ShowName_Dic = bscCore.orderedDict(
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
    LynxiProduct_Asset_Class_ShowName_Dic = bscCore.orderedDict(
        [
            (LynxiProduct_Asset_Class_Character, ('Character', u'角色')),
            (LynxiProduct_Asset_Class_Prop, ('Prop', u'道具'))
        ]
    )
    LynxiProduct_Asset_Class_UiDatumDic = bscCore.orderedDict(
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
    LynxiProduct_Scenery_Class_ShowName_Dic = bscCore.orderedDict(
        [
            (LynxiProduct_Scenery_Class_Scenery, ('Scenery', u'场景')),
            (LynxiProduct_Scenery_Class_Group, ('Group', u'组合')),
            (LynxiProduct_Scenery_Class_Assembly, ('Assembly', u'组装'))
        ]
    )
    LynxiProduct_Scenery_Class_UiDatumDic = bscCore.orderedDict(
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
    LynxiProduct_Scene_Class_ShowName_Dic = bscCore.orderedDict(
        [
            (LynxiProduct_Scene_Class_Scene, ('Scene', u'镜头')),
            (LynxiProduct_Scene_Class_Act, ('Act', u'动作'))
        ]
    )
    LynxiProduct_Scene_Class_UiDatumDic = bscCore.orderedDict(
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
    LynxiUnit_Priority_ShowName_Dic = bscCore.orderedDict(
        [
            (LynxiUnit_Priority_Major, ('Major', u'主要')),
            (LynxiUnit_Priority_Minor, ('Minor', u'次要')),
            (LynxiUnit_Priority_Util, ('Util', u'龙套'))
        ]
    )
    LynxiUnit_Priority_UiDatumDic = bscCore.orderedDict(
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
    LynxiProduct_Asset_Link_ShowName_Dic = bscCore.orderedDict(
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
    LynxiProduct_Scenery_Link_ShowName_Dic = bscCore.orderedDict(
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
    LynxiProduct_Scene_Link_ShowName_Dic = bscCore.orderedDict(
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

    LynxiAttrName_Object_Transparent = 'lxObjectTransparent'
    LynxiAttrName_Object_RenderVisible = 'lxObjectRenderVisible'


class PrsPipeline(object):
    pass