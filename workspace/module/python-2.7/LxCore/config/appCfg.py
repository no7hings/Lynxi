# coding=utf-8
OsFilePathSep = '/'
#
MaKeyword_ShapeOrig = 'Orig'
MaKeyword_ShapeDeformed = 'Deformed'
MaKeyword_Shape = 'Shape'
#
M2TransformType = 'kTransform'
M2MeshType = 'kMesh'
M2NurbsSurfaceType = 'kNurbsSurface'
M2NurbsCurveType = 'kNurbsCurve'
#
DEF_mya_type_transform = 'transform'
DEF_mya_type_mesh = 'mesh'
DEF_mya_type_nurbs_surface = 'nurbsSurface'
DEF_mya_type_nurbs_curve = 'nurbsCurve'
#
MaCameraType = 'camera'
#
MaNodeType_Plug_Yeti = 'pgYetiMaya'
MaNodeType_YetiGroom = 'pgYetiGroom'
MaYetiFeatherType = 'pgYetiMayaFeather'
MaPfxHairType = 'pfxHair'
#
MaFollicleType = 'follicle'
MaHairSystemType = 'hairSystem'
MaNucleusType = 'nucleus'
MaNodeType_Plug_NurbsHair = 'nurbsHair'
MaNurbsHairScatterType = 'nurbsHairScatter'
MaNurbsHairInGuideCurvesType = 'nurbsHairOp_InGuideCurves'
MaNurbsHairCacheType = 'nurbsHairOp_Cache'
#
MaNurbsHairCacheModeAttrName = 'cacheMode'
MaNurbsHairCacheFileAttrName = 'cacheFile'
#
MaNodeType_CacheFile = 'cacheFile'
MaNodeType_AiVolume = 'aiVolume'
#
DEF_mya_type_alembic = 'AlembicNode'
MaGpuCache = 'gpuCache'
#
MaReferenceType = 'reference'
MaRN = 'RN'
#
DEF_mya_type_assembly_reference = 'assemblyReference'
#
DEF_mya_node_pathsep = '|'
DEF_mya_node_namespace_pathsep = ':'
DEF_mya_node_port_pathsep = '.'
#
MaNodeType_AiStandIn = 'aiStandIn'
MaArnoldTxExt = '.tx'
#
MaTextureNodeType = 'file'
#
MaReferenceNodeTypes = [
    MaReferenceType
]
# Texture
MaTexture_NodeTypeLis = [
    'file',
    'aiImage',
    'RedshiftNormalMap',
    'RedshiftCameraMap'
]
# Fur
MaFurMapNodeTypes = [
    MaNodeType_Plug_Yeti,
    MaPfxHairType,
    MaNodeType_Plug_NurbsHair
]
#
MaFurMapAttrDic = {
    MaNurbsHairCacheType: MaNurbsHairCacheFileAttrName
}
#
MaFurCacheNodeTypes = [
    MaNodeType_Plug_Yeti,
    MaNodeType_Plug_NurbsHair
]
#
MaYetiSolverModeLis = [
    'Off',
    'On'
]
#
MaHairSystemSolverModeLis = [
    'Off',
    'Static',
    'Dynamic Follicle Only',
    'All Follicle'
]
#
MaHairSystemNeedUploadModeLis = [
    'Dynamic Follicle Only',
    'All Follicle'
]
#
MaNurbsHairSolverModeLis = [
    'Off',
    'Write',
    'Read'
]
#
MaHairSystemSolverModeIndexDic = {
    'Off': 0,
    'Static': 1,
    'Dynamic Follicle Only': 2,
    'All Follicle': 3
}
MaNurbsHairSolverModeIndexDic = {
    'Off': 0,
    'Write': 1,
    'Read': 2
}
MaUnit_UiDic_Time = {
    '12 fps': '12fps',
    '15 fps': 'game',
    '16 fps': '16fps',
    '24 fps': 'film',
    '25 fps': 'pal',
    '30 fps': 'ntsc',
    '48 fps': 'show',
    '50 fps': 'palf',
    '60 fps': 'ntscf'
}
#
DEF_mya_type_shading_engine = 'shadingEngine'
#
MaRenderPartition = 'renderPartition'
MaNodeName_LightLink = 'lightLinker1'
MaNodeName_DefaultLightSet = 'defaultLightSet'
#
DEF_mya_type_light = 'light'
#
DdlMaBatchJob = 'MayaBatch'
DdlMaCmdJob = 'MayaCmd'
#
DdlJobs = [
    DdlMaBatchJob,
    DdlMaCmdJob
]
#
MaTransformationAttrLis = [
    'translate',
    'rotate',
    'scale'
]
