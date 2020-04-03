# coding:utf-8
import sys
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.OpenMaya as OpenMaya
# noinspection PyUnresolvedReferences
import maya.OpenMayaMPx as OpenMayaMPx
# noinspection PyUnresolvedReferences
import maya.api.OpenMayaRender as OpenMayaRender


class asTransformCmd(object):
    def __init__(self, *args):
        nodeName, lod, proxyCacheFile, gpuCacheFile = args
        print nodeName, lod, proxyCacheFile, gpuCacheFile


#
class asbTransformMatrix(OpenMayaMPx.MPxTransformationMatrix):
    TypeId = OpenMaya.MTypeId(0x8700E)
    @classmethod
    def create(cls):
        return OpenMayaMPx.asMPxPtr(asbTransformMatrix())


#
class asbTransform(OpenMayaMPx.MPxTransform):
    Nodename = 'asbTransform'
    # noinspection PyArgumentList
    TypeId = OpenMaya.MTypeId(0x8700D)
    NodeClass = 'lynxi/assembly'
    #
    NamespaceAttr = OpenMaya.MObject()
    #
    LodAttr = OpenMaya.MObject()
    #
    ProxyCacheFileAttr = OpenMaya.MObject()
    GpuCacheFileAttr = OpenMaya.MObject()
    AssetFileAttr = OpenMaya.MObject()
    #
    CompAttr = OpenMaya.MFnCompoundAttribute()
    NumAttr = OpenMaya.MFnNumericAttribute()
    EnumAttr = OpenMaya.MFnEnumAttribute()
    TypeAttr = OpenMaya.MFnTypedAttribute()
    StringData = OpenMaya.MFnStringData()
    @classmethod
    def _addCompAttr(cls, longName, shortName):
        attr = cls.CompAttr.create(longName, shortName)
        #
        positionAttr = cls.NumAttr.create(
            longName + '_Position', shortName + 'p',
            OpenMaya.MFnNumericData.kFloat
        )
        #
        valueAttr = cls.NumAttr.create(
            longName + '_FloatValue', shortName + 'v',
            OpenMaya.MFnNumericData.kFloat
        )
        #
        interpAttr = cls.EnumAttr.create(
            longName + '_Interp', shortName + 'i'
        )
        cls.EnumAttr.addField('None', 0)
        cls.EnumAttr.addField('Linear', 1)
        cls.EnumAttr.addField('Smooth', 2)
        cls.EnumAttr.addField('Spline', 3)
        cls.EnumAttr.default = 3
        cls.CompAttr.addChild(positionAttr)
        cls.CompAttr.addChild(valueAttr)
        cls.CompAttr.addChild(interpAttr)
        #
        cls.CompAttr.setStorable(True)
        cls.CompAttr.array = True
        cls.CompAttr.usesArrayDataBuilder = True
        cls.addAttribute(attr)
        return attr
    @classmethod
    def _addIntNumAttr(cls, longName, shortName, value, maximum=None, minimum=None, softMax=None, softMin=None, keyable=True):
        attr = cls.NumAttr.create(longName, shortName, OpenMaya.MFnNumericData.kInt, int(value))
        cls.NumAttr.setWritable(True)
        cls.NumAttr.setKeyable(keyable)
        cls.NumAttr.setStorable(True)
        cls.NumAttr.setChannelBox(True)
        if maximum is not None:
            cls.NumAttr.setMax(int(maximum))
        if minimum is not None:
            cls.NumAttr.setMin(int(minimum))
        if softMax is not None:
            cls.NumAttr.setSoftMax(softMax)
        if softMin is not None:
            cls.NumAttr.setSoftMin(softMin)
        cls.addAttribute(attr)
        return attr
    @classmethod
    def _addFloatNumAttr(cls, longName, shortName, value, maximum=None, minimum=None, softMax=None, softMin=None, keyable=True):
        attr = cls.NumAttr.create(longName, shortName, OpenMaya.MFnNumericData.kFloat, float(value))
        cls.NumAttr.setWritable(True)
        cls.NumAttr.setKeyable(keyable)
        cls.NumAttr.setStorable(True)
        cls.NumAttr.setChannelBox(True)
        if maximum is not None:
            cls.NumAttr.setMax(float(maximum))
        if minimum is not None:
            cls.NumAttr.setMin(float(minimum))
        if softMax is not None:
            cls.NumAttr.setSoftMax(float(softMax))
        if softMin is not None:
            cls.NumAttr.setSoftMin(float(softMin))
        cls.addAttribute(attr)
        return attr
    @classmethod
    def _addBooleanNumAttr(cls, longName, shortName, value, keyable=True):
        attr = cls.NumAttr.create(longName, shortName, OpenMaya.MFnNumericData.kBoolean, value)
        cls.NumAttr.setWritable(True)
        cls.NumAttr.setKeyable(keyable)
        cls.NumAttr.setStorable(True)
        cls.NumAttr.setChannelBox(True)
        cls.addAttribute(attr)
        return attr
    @classmethod
    def _addEnumAttr(cls, longName, shortName, value, keyable=True):
        attr = cls.EnumAttr.create(longName, shortName)
        cls.EnumAttr.setWritable(True)
        cls.EnumAttr.setKeyable(keyable)
        cls.EnumAttr.setStorable(True)
        cls.EnumAttr.setChannelBox(True)
        [cls.EnumAttr.addField(i, seq) for seq, i in enumerate(value)]
        cls.addAttribute(attr)
        return attr
    @classmethod
    def _addStringAttr(cls, longName, shortName, keyable=False):
        attr = cls.TypeAttr.create(longName, shortName, OpenMaya.MFnData.kString)
        cls.TypeAttr.setWritable(True)
        cls.TypeAttr.setKeyable(keyable)
        cls.TypeAttr.setStorable(True)
        cls.addAttribute(attr)
        return attr
    @classmethod
    def _addFileNameAttr(cls, longName, shortName, keyable=False):
        attr = cls.TypeAttr.create(longName, shortName, OpenMaya.MFnData.kString)
        cls.TypeAttr.setWritable(True)
        cls.TypeAttr.setKeyable(keyable)
        cls.TypeAttr.setStorable(True)
        cls.TypeAttr.setUsedAsFilename(True)
        cls.addAttribute(attr)
        return attr
    @classmethod
    def initializer(cls):
        cls.NamespaceAttr = cls._addStringAttr(
            'namespace', 'ns'
        )
        cls.LodAttr = cls._addEnumAttr(
            'lod', 'lod', value=['{}'.format(i) for i in range(3)]
        )
        cls.ProxyCacheFileAttr = cls._addFileNameAttr(
            'proxyCacheFile', 'prxFile'
        )
        cls.GpuCacheFileAttr = cls._addFileNameAttr(
            'gpuCacheFile', 'gpuFile'
        )
        cls.AssetFileAttr = cls._addFileNameAttr(
            'assetFile', 'astFile'
        )
    @classmethod
    def create(cls):
        return OpenMayaMPx.asMPxPtr(asbTransform())
    @staticmethod
    def setOsCommandRun_(*args):
        asTransformCmd(*args)
    # noinspection PyMethodOverriding
    def compute(self, plug, dataBlock):
        return OpenMayaMPx.MPxTransform.compute(self, plug, dataBlock)


# Initialize
def initializePlugin(obj):
    # noinspection PyArgumentList
    plug = OpenMayaMPx.MFnPlugin(obj, 'ChangBao.Dong', '1.0.0', 'Any')
    # Register Nde_Node
    try:
        plug.registerTransform(
            asbTransform.Nodename,
            asbTransform.TypeId,
            asbTransform.create,
            asbTransform.initializer,
            asbTransformMatrix.create,
            asbTransformMatrix.TypeId
        )
    except:
        sys.stderr.write('Failed to Register Nde_Node: %s' % asbTransform.Nodename)
        raise


# Uninitialize
def uninitializePlugin(obj):
    # noinspection PyArgumentList
    plug = OpenMayaMPx.MFnPlugin(obj)
    # Deregister Nde_Node
    try:
        plug.deregisterNode(
            asbTransform.TypeId
        )
    except:
        sys.stderr.write('Failed to Deregister Nde_Node: %s' % asbTransform.Nodename)
        raise
