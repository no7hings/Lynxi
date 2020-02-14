# coding=utf-8
import collections
#
astHierarchyKey = 'hierarchy'
astGeometryKey = 'geometry'
astGeomShapeKey = 'geometryShape'
astMapKey = 'map'
astMapShapeKey = 'mapShape'
#
VAR_product_asset_category_character = 'character'
VAR_product_asset_category_prop = 'prop'
#
none = ''


# Model Check Config
def astModelCheckConfig():
    dic = collections.OrderedDict()
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
        'Mesh Nde_Geometry Check',
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
    dic = collections.OrderedDict()
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
    dic = collections.OrderedDict()
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
    dic = collections.OrderedDict()
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
    dic = collections.OrderedDict()
    dic['astRigControlCheck'] = [
        False,
        'Rig Control Check',
        u'''确认绑定不存在错误的 Control'''
    ]
    return dic


#
def astLightCheckConfig():
    dic = collections.OrderedDict()
    dic['astLightTransformCheck'] = [
        False,
        'Light Transform Check',
        u'''确认灯光不存在错误的 Transform'''
    ]
    return dic


#
def astShaderCheckConfig():
    dic = collections.OrderedDict()
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


# Nde_Geometry Data Config
def geometryDataConfig():
    # Dic { <Data Label>: <Data Label in UI> }
    dic = collections.OrderedDict()
    dic['hierarchyId'] = 'Hierarchy - ID'
    dic['geometryId'] = 'Nde_Geometry - ID'
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

