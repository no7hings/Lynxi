# coding:utf-8
from LxBasic import bscCore

from LxCore.config import appConfig


#
class MaConfig(object):
    Ma_Separator_Node = '|'
    Ma_Separator_Set = '>'
    Ma_Separator_Namespace = ':'
    Ma_Separator_Attribute = '.'
    # Nde_Node Type
    MaNodeType_Transform = 'transform'
    MaNodeType_ShadingEngine = 'shadingEngine'
    MaNodeType_Mesh = 'mesh'
    MaNodeType_AssemblyReference = 'assemblyReference'
    MaNodeType_AssemblyDefinition = 'assemblyDefinition'
    #
    MaNodeType_GroupId = 'groupId'
    MaNodeType_Set = 'set'
    #
    MaNodeType_Light = 'light'
    #
    MaAttrName_Message = 'message'
    MaAttrName_ObjectGroup = 'instObjGroups'
    MaAttrName_SetMember = 'dagSetMembers'
    #
    MaCompName_Mesh_Vertex = 'vtx'
    MaCompName_Mesh_Edge = 'e'
    MaCompName_Mesh_Face = 'f'
    MaDefaultMatrix = [1.0, .0, .0, .0, .0, 1.0, .0, .0, .0, .0, 1.0, .0, .0, .0, .0, 1.0]


class Cfg_M2(object):
    pass


class MaAssemblyConfig(object):
    pass


class MaPlugConfig(object):
    MaPlugName_AlembicExport = 'AbcExport'
    MaPlugName_GpuCache = 'gpuCache'
    MaPlugName_Arnold = 'mtoa'
    MaPlugName_Yeti = 'pgYetiMaya'
    #
    MaNodeType_Plug_Yeti = 'pgYetiMaya'


class MaUnitConfig(appConfig.LxUnitConfig):
    # Key
    MaUnit_Key_Time = 'time'
    MaUnit_Key_Angle = 'angle'
    MaUnit_Key_Linear = 'linear'
    #
    MaUnit_DefaultValue_Time = 'film'
    MaUnit_DefaultValue_Angle = 'degree'
    MaUnit_DefaultValue_Linear = 'cm'
    #
    MaUnit_UiDic_Time = {
        '12fps': '12 Fps',
        'game': '15 Fps',
        '16fps': '16 Fps',
        'film': '24 Fps',
        'pal': '25 Fps',
        'ntsc': '30 Fps',
        'show': '48 Fps',
        'palf': '50 Fps',
        'ntscf': '60 Fps'
    }
    MaUnit_UiDic_Angle = {
        'deg': 'Degree',
        'rad': 'Radian'
    }
    MaUnit_UiDic_Linear = {
        'mm': 'Millimeter',
        'cm': 'Centimeter',
        'm': 'Meter',
        'km': 'Kilometer',
        'in': 'Inch',
        'ft': 'Foot',
        'yd': 'Yard',
        'mi': 'Mile'
    }
    @classmethod
    def _toViewTimeUnit(cls, unit):
        return cls.MaUnit_UiDic_Time.get(unit, 'N/a')
    @classmethod
    def _toViewAngleUnit(cls, unit):
        return cls.MaUnit_UiDic_Angle.get(unit, 'N/a')
    @classmethod
    def _toViewLinearUnit(cls, unit):
        return cls.MaUnit_UiDic_Linear.get(unit, 'N/a')


class MaRenderConfig(object):
    # Renderer
    MaRenderer_Arnold = 'arnold'
    MaRenderer_Software = 'mayaSoftware'
    MaRenderer_Hardware = 'mayaHardware'
    MaRenderer_Hardware2 = 'mayaHardware2'
    # Arnold
    MaArnold_DefaultRenderPass = 'beauty'
    # Software
    MaNode_DefaultRenderGlobals = 'defaultRenderGlobals'
    MaNode_DefaultResolution = 'defaultResolution'
    MaNode_DefaultRenderQuality = 'defaultRenderQuality'
    # Hardware
    MaNode_DefaultHardwareRenderGlobals = 'defaultHardwareRenderGlobals'
    MaNode_HardwareRenderGlobals = 'hardwareRenderGlobals'
    MaNode_HardwareRenderingGlobals = 'hardwareRenderingGlobals'
    # Arnold
    MaNode_DefaultArnoldRenderOptions = 'defaultArnoldRenderOptions'
    MaNode_DefaultArnoldDisplayDriver = 'defaultArnoldDisplayDriver'
    MaNode_DefaultArnoldFilter = 'defaultArnoldFilter'
    MaNode_DefaultArnoldDriver = 'defaultArnoldDriver'
    #
    MaRender_Software_Node_Lis = [
        MaNode_DefaultRenderGlobals,
        MaNode_DefaultResolution,
        #
        MaNode_DefaultRenderQuality
    ]
    MaRender_Hardware_Node_Lis = [
        MaNode_DefaultRenderGlobals,
        MaNode_DefaultResolution,
        #
        MaNode_DefaultHardwareRenderGlobals,
        MaNode_HardwareRenderGlobals
    ]
    MaRender_Hardware2_Node_Lis = [
        MaNode_DefaultRenderGlobals,
        MaNode_DefaultResolution,
        #
        MaNode_DefaultHardwareRenderGlobals,
        MaNode_HardwareRenderingGlobals
    ]
    MaRender_Arnold_Node_Lis = [
        MaNode_DefaultRenderGlobals,
        MaNode_DefaultResolution,
        #
        MaNode_DefaultArnoldRenderOptions,
        MaNode_DefaultArnoldDisplayDriver,
        MaNode_DefaultArnoldFilter,
        MaNode_DefaultArnoldDriver
    ]


class MaUiConfig(object):
    MaUiName_MainWindow = 'MayaWindow'
    #
    MaUiName_MainControl = 'MainPane'
    MaUiName_OutlinerControl = 'Outliner'
    MaUiName_AttributeControl = 'AttributeEditor'


class MaNodeAttributeConfig(appConfig.LxAttributeConfig):
    MaAttrNameLis_ShaderExcept = [
        'computedFileTextureNamePattern',
        'expression'
    ]
    MaAttrTypeLis_Readable = [
        'bool',
        'byte',
        'enum',
        'string',
        'short',
        'float',
        'double',
        'time',
        'doubleLinear',
        'doubleAngle',
        'matrix',
        'long',
        'lightData',
        'addr',
        'fltMatrix',
        'char',
        'floatAngle',
        'floatLinear'
    ]
    MaAttrTypeLis_NonDefaultValue = [
        'string'
    ]
    #
    MaAttrNameDic_Convert = {
        'internalExpression': 'expression'
    }
    MaAttrName_Visible = 'visibility'


class MaNodeConfig(appConfig.LxNodeConfig):
    pass


class MaLightNodeConfig(object):
    MaNodeTypeLis_LightDefaultSet_Except = [
        'aiLightDecay'
    ]
    MaNodeName_LightLink = 'lightLinker1'
    MaNodeName_DefaultLightSet = 'defaultLightSet'
    #
    MaAttrNameLis_LightLink = ['link', 'light', 'object']
    MaAttrNameLis_LightLink_Ignore = ['ignore', 'lightIgnored', 'objectIgnored']
    #
    MaAttrNameLis_ShadowLink = ['shadowLink', 'shadowLight', 'shadowObject']
    MaAttrNameLis_ShadowLink_Ignore = ['shadowIgnore', 'shadowLightIgnored', 'shadowObjectIgnored']
    #
    MaAttrNameDic_LightLink = {
        'link': ['light', 'object'],
        'shadowLink': ['shadowLight', 'shadowObject'],
        'ignore': ['lightIgnored', 'objectIgnored'],
        'shadowIgnore': ['shadowLightIgnored', 'shadowObjectIgnored']
    }
    #
    MaAttrPrevNameDic = {}
    @classmethod
    def maAttrPrettifyNameDic_lightLink(cls):
        return bscCore.orderedDict(
            [
                ('light', 'Light(s)'),
                ('object', 'Object(s)'),
                #
                ('defaultLightSet', 'Default Set(s)'),
                #
                ('link', 'Light Link(s)'),
                ('shadowLink', 'Shadow Link(s)'),
                ('ignore', 'Light Ignore(s)'),
                ('shadowIgnore', 'Shadow Ignore(s)')
            ]
        )


class MaNodeGraphConfig(appConfig.LxNodeGraphConfig):
    pass


class MaYetiPlugConfig(object):
    MaYetiImportType_Geometry = 'yetiGeometry'
    MaYetiImportType_Groom = 'yetiGroom'
    MaYetiImportType_Guide = 'yetiGuide'
    MaYetiImportType_Feather = 'yetiFeather'
    #
    MaYetiImportTypeLis = [
        MaYetiImportType_Geometry,
        MaYetiImportType_Groom,
        MaYetiImportType_Guide,
        MaYetiImportType_Feather
    ]


class MaArnoldPlugConfig(object):
    pass
