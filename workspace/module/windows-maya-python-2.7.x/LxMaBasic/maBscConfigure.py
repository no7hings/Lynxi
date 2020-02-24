# coding:utf-8


class Utility(object):
    DEF_separator_node = '|'
    DEF_separator_set = '>'
    DEF_separator_namespace = ':'
    DEF_separator_port = '.'
    # Nde_Node Type
    DEF_type_transform = 'transform'
    DEF_type_shading_engine = 'shadingEngine'
    DEF_type_mesh = 'mesh'
    DEF_type_nurbs_surface = 'nurbsSurface'
    DEF_type_nurbs_curve = 'nurbsCurve'
    DEF_type_geometry_list = [
        DEF_type_mesh,
        DEF_type_nurbs_surface,
        DEF_type_nurbs_curve
    ]
    DEF_type_assembly_reference = 'assemblyReference'
    DEF_type_assembly_definition = 'assemblyDefinition'
    #
    DEF_type_group_id = 'groupId'
    DEF_type_set = 'set'
    #
    DEF_type_light = 'light'
    #
    DEF_attribute_message = 'message'
    DEF_attribute_inst_obj_groups = 'instObjGroups'
    DEF_attribute_dag_set_members = 'dagSetMembers'
    #
    DEF_key_mesh_vertex = 'vtx'
    DEF_key_mesh_edge = 'e'
    DEF_key_mesh_face = 'f'
    DEF_matrix_default = [1.0, .0, .0, .0, .0, 1.0, .0, .0, .0, .0, 1.0, .0, .0, .0, .0, 1.0]

    DEF_camera_default_list = ['persp', 'top', 'front', 'side']

    DEF_shading_engine_default_list = ['initialShadingGroup', 'initialParticleSE', 'defaultLightSet', 'defaultObjectSet']

    DEF_porttype_multichannel_list = [
        'long2',
        'long3',
        'short2',
        'short3',
        'float2',
        'float3',
        'double2',
        'double3'
    ]

    DEF_porttype_list = [
        'bool',
        'long',
        'short',
        'byte',
        'char',
        'enum',
        'float',
        'double',
        'doubleAngle',
        'doubleLinear',
        'string',
        'stringArray',
        'compound',
        'message',
        'time',
        'matrix',
        'fltMatrix',
        'reflectanceRGB',
        'reflectance',
        'spectrumRGB',
        'spectrum',
        'float2',
        'float3',
        'double2',
        'double3',
        'long2',
        'long3',
        'short2',
        'short3',
        'doubleArray',
        'floatArray',
        'Int32Array',
        'vectorArray',
        'nurbsCurve',
        'nurbsSurface',
        'mesh',
        'lattice',
        'pointArray',
    ]

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
    DEF_type_alembic = 'AlembicNode'
    MaGpuCache = 'gpuCache'
    #
    MaReferenceType = 'reference'
    MaRN = 'RN'
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
    #
    MaRenderPartition = 'renderPartition'
    MaNodeName_LightLink = 'lightLinker1'
    MaNodeName_DefaultLightSet = 'defaultLightSet'
    #
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

    MaPlugName_AlembicExport = 'AbcExport'
    MaPlugName_GpuCache = 'gpuCache'
    MaPlugName_Arnold = 'mtoa'
    MaPlugName_Yeti = 'pgYetiMaya'
    #
    MaNodeType_Plug_Yeti = 'pgYetiMaya'

