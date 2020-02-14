# coding:utf-8
from LxBasic import bscCore

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


class PrsBasic(object):
    pass


class PrsProduct(object):
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
    VAR_product_module_showname_dict = bscCore.orderedDict(
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
    VAR_product_asset_category_showname_dict = bscCore.orderedDict(
        [
            (VAR_product_asset_category_character, ('Character', u'角色')),
            (VAR_product_asset_category_prop, ('Prop', u'道具'))
        ]
    )
    VAR_product_asset_category_uidatum_dict = bscCore.orderedDict(
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
    VAR_product_scenery_category_showname_dict = bscCore.orderedDict(
        [
            (VAR_product_scenery_category_scenery, ('Scenery', u'场景')),
            (VAR_product_scenery_category_Group, ('Group', u'组合')),
            (VAR_product_scenery_category_Assembly, ('Assembly', u'组装'))
        ]
    )
    VAR_product_scenery_category_uidatum_dict = bscCore.orderedDict(
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
    VAR_product_scene_category_showname_dict = bscCore.orderedDict(
        [
            (VAR_product_scene_category_scene, ('Scene', u'镜头')),
            (VAR_product_scene_category_act, ('Act', u'动作'))
        ]
    )
    VAR_product_scene_category_uidatum_dict = bscCore.orderedDict(
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
    VAR_product_priority_showname_dict = bscCore.orderedDict(
        [
            (VAR_product_priority_major, ('Major', u'主要')),
            (VAR_product_priority_minor, ('Minor', u'次要')),
            (VAR_product_priority_util, ('Util', u'龙套'))
        ]
    )
    VAR_product_priority_uidatum_dict = bscCore.orderedDict(
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
    VAR_product_asset_link_showname_dict = bscCore.orderedDict(
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
    VAR_product_scenery_link_scenery = 'scenery'
    VAR_product_scenery_link_layout = 'layout'
    VAR_product_scenery_link_animation = 'animation'
    VAR_product_scenery_link_simulation = 'simulation'
    VAR_product_scenery_link_solver = 'solver'
    VAR_product_scenery_link_light = 'light'

    VAR_product_scenery_link_list = [
        VAR_product_scenery_link_scenery,
        VAR_product_scenery_link_layout,
        VAR_product_scenery_link_animation,
        VAR_product_scenery_link_simulation,
        VAR_product_scenery_link_solver,
        VAR_product_scenery_link_light
    ]
    VAR_product_scenery_link_showname_dict = bscCore.orderedDict(
        [
            (VAR_product_scenery_link_scenery, ('Scenery', u'场景布景')),
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
    VAR_product_scene_link_showname_dict = bscCore.orderedDict(
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

    VAR_product_attribute_list = [
        VAR_product_attribute_id,
        VAR_product_attribute_category,
        VAR_product_attribute_name,
        VAR_product_attribute_variant,
        VAR_product_attribute_stage
    ]

    VAR_product_attribute_object_transparent = 'lxObjectTransparent'
    VAR_product_attribute_object_renderable = 'lxObjectRenderVisible'
