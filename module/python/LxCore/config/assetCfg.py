# coding=utf-8
from LxCore import lxBasic, lxConfigure
#
astHierarchyKey = 'hierarchy'
astGeometryKey = 'geometry'
astGeomShapeKey = 'geometryShape'
astMapKey = 'map'
astMapShapeKey = 'mapShape'
#
LynxiProduct_Asset_Class_Character = 'character'
LynxiProduct_Asset_Class_Prop = 'prop'
#
none = ''


#
def astBasicClass():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        LynxiProduct_Asset_Class_Character,
        LynxiProduct_Asset_Class_Prop
    ]
    return lis


@lxBasic.getDicMethod
def astBasicViewLinkDic(*args):
    dic = lxBasic.orderedDict()
    dic[lxConfigure.LynxiProduct_Asset_Link_Model] = 'Model', u'模型'
    dic[lxConfigure.LynxiProduct_Asset_Link_Rig] = 'Rig', u'绑定'
    dic[lxConfigure.LynxiProduct_Asset_Link_Cfx] = 'Groom', u'毛发塑形'
    dic[lxConfigure.LynxiProduct_Asset_Link_Solver] = 'Solver Rig', u'毛发绑定'
    dic[lxConfigure.LynxiProduct_Asset_Link_Light] = 'Light', u'灯光'
    dic[lxConfigure.LynxiProduct_Asset_Link_Assembly] = 'Assembly', u'组装'
    return dic


@lxBasic.getDicMethod
def astBasicViewClassDic(*args):
    dic = lxBasic.orderedDict()
    dic[LynxiProduct_Asset_Class_Character] = 'Character', u'角色'
    dic[LynxiProduct_Asset_Class_Prop] = 'Prop', u'道具'
    return dic


#
def astBasicClassDatumDic():
    return lxBasic.orderedDict(
        [
            ('ast0', (lxConfigure.LynxiValue_Unspecified, u'待定')),
            ('ast1', (LynxiProduct_Asset_Class_Character, u'角色')),
            ('ast2', (LynxiProduct_Asset_Class_Prop, u'道具')),
        ]

    )


#
def basicAssetPriorityLis():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        'major',
        'minor',
        'util'
    ]
    return lis


#
def basicModelProcess():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        'Model > Texture > Shader'
    ]
    return lis


#
def basicRigProcess():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        'Low - Quality > High - Quality'
    ]
    return lis


#
def basicCfxProcess():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        'Fur - Groom > Fur - Shader'
    ]
    return lis


# Model Check Config
def astModelCheckConfig():
    dic = lxBasic.orderedDict()
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
        'Mesh Geometry Check',
        u'''确认模型不存在错误的拓扑结构'''
    ]
    dic['meshHistoryCheck'] = [
        True,
        'Mesh History Check',
        u'''确认模型不存在多余的历史记录'''
    ]
    return dic


#
def astMeshGeomCheckConfig():
    dic = lxBasic.orderedDict()
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


#
def astCfxGroomCheckConfig():
    dic = lxBasic.orderedDict()
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


#
def astSolverCheckConfig():
    dic = lxBasic.orderedDict()
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


#
def astRigCheckConfig():
    dic = lxBasic.orderedDict()
    dic['astRigControlCheck'] = [
        False,
        'Rig Control Check',
        u'''确认绑定不存在错误的 Control'''
    ]
    return dic


#
def astLightCheckConfig():
    dic = lxBasic.orderedDict()
    dic['astLightTransformCheck'] = [
        False,
        'Light Transform Check',
        u'''确认灯光不存在错误的 Transform'''
    ]
    return dic


#
def astShaderCheckConfig():
    dic = lxBasic.orderedDict()
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


# Geometry Data Config
def geometryDataConfig():
    # Dic { <Data Label>: <Data Label in UI> }
    dic = lxBasic.orderedDict()
    dic['hierarchyId'] = 'Hierarchy - ID'
    dic['geometryId'] = 'Geometry - ID'
    dic['uvCoordId'] = 'UVs - ID'
    dic['geometrys'] = 'Geometries'
    dic['vertex'] = 'Vertexs'
    dic['edge'] = 'Edges'
    dic['face'] = 'Faces'
    dic['triangle'] = 'Triangles'
    dic['uvcoord'] = 'Uvs'
    dic['area'] = 'Areas ( loc )'
    dic['worldArea'] = 'Areas ( wrd )'
    dic['shell'] = 'Shell'
    dic['axisX'] = 'Axis ( X )'
    dic['horz'] = 'Horz'
    return dic


# File Box Config
def fileBoxConfig():
    # Dic { <Data Label>: <Data Label in UI> }
    dic = lxBasic.orderedDict()
    modelDic = lxBasic.orderedDict()
    modelDic['mesh'] = 'Mesh'
    modelDic['material'] = 'Material'
    dic['model'] = ['Model', modelDic]
    cfxDic = lxBasic.orderedDict()
    cfxDic['fur'] = 'Fur'
    cfxDic['furMaterial'] = 'Fur - Material'
    dic['cfx'] = ['CFX', cfxDic]
    rigDic = lxBasic.orderedDict()
    rigDic['layoutRig'] = 'Low - Quality'
    rigDic['animationRig'] = 'High - Quality'
    dic['rig'] = ['Rig', rigDic]
    return dic


#
def basicAssetLinks():
    lis = [
        lxConfigure.LynxiProduct_Asset_Link_Model,
        lxConfigure.LynxiProduct_Asset_Link_Rig,
        lxConfigure.LynxiProduct_Asset_Link_Cfx,
        lxConfigure.LynxiProduct_Asset_Link_Solver,
        lxConfigure.LynxiProduct_Asset_Link_Light,
        lxConfigure.LynxiProduct_Asset_Link_Assembly
    ]
    return lis


#
def basicAssetMeshCheckKeys():
    lis = [
        astHierarchyKey,
        astGeometryKey,
        astGeomShapeKey,
        astMapKey,
        astMapShapeKey
    ]
    return lis

