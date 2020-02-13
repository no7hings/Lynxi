# coding=utf-8
import os
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxBasic import bscCore, bscMethods
#
from LxMaya.command import maUtils, maAttr, maProxy
#
from random import choice
#
inBoxLabel = '_inBox'
inGpuLabel = '_inGpu'
inProxyLabel = '_inPrx'
inProxyMeshLabel = '_inPrxMsh'
#
definitionLabel = '_dfn'
#
asbProxyFileLabel = '_prx'
inAovLabel = '_inAov'
maskLabel = '_mask'
inContainerLabel = '_inContainer'
#
none = ''


#
def setOutAstProxy(fileString_, objectString, renderer):
    bscMethods.OsFile.createDirectory(fileString_)
    # Export
    cmds.select(objectString)
    maProxy.setOutProxy(fileString_, renderer, 0)
    cmds.select(clear=1)


#
def setProxyCreate(objectString, box, gpu, proxy, renderer):
    if renderer == 'Arnold':
        setArnoldProxyCreate(objectString, box, gpu, proxy)
    elif renderer == 'Redshift':
        setRedshiftProxyCreate(objectString, box, gpu, proxy)


#
def setCreateArnoldProxy(proxyObject, proxy):
    if not cmds.objExists('ArnoldStandInDefaultLightSet'):
        cmds.createNode('objectSet', name='ArnoldStandInDefaultLightSet', shared=1)
        cmds.lightlink(object='ArnoldStandInDefaultLightSet', light='defaultLightSet')
    #
    cmds.createNode('transform', name=proxyObject)
    # Proxy
    inProxyNode = proxyObject + inProxyLabel
    cmds.createNode('aiStandIn', name=inProxyNode, parent=proxyObject)
    cmds.setAttr(inProxyNode + '.mode', 1)
    cmds.setAttr(inProxyNode + '.visibleInReflections', 1)
    cmds.setAttr(inProxyNode + '.visibleInRefractions', 1)
    cmds.setAttr(inProxyNode + '.dso', proxy, type='string')


#
def setArnoldProxyCreate(objectString, box, gpu, proxy):
    def setRenderEnabled(node, enabled):
        if enabled is False:
            maAttr.setNodeUnrenderable(node)
    #
    proxyObject = objectString + asbProxyFileLabel
    if not cmds.objExists('ArnoldStandInDefaultLightSet'):
        cmds.createNode('objectSet', name='ArnoldStandInDefaultLightSet', shared=1)
        cmds.lightlink(object='ArnoldStandInDefaultLightSet', light='defaultLightSet')
    #
    cmds.createNode('transform', name=proxyObject)
    # Switch
    cmds.addAttr(proxyObject, longName='box', attributeType='bool', keyable=1)
    cmds.setAttr(proxyObject + '.box', 0)
    cmds.addAttr(proxyObject, longName='gpu', attributeType='bool', keyable=1)
    cmds.setAttr(proxyObject + '.gpu', 1)
    # Render
    cmds.addAttr(proxyObject, longName='used', niceName='Used', attributeType='enum', enumName='lod00:lod01:lod02:')
    cmds.addAttr(proxyObject, longName='override', niceName='Override', attributeType='bool')
    cmds.addAttr(proxyObject, longName='mask', niceName='Mask', attributeType='double3')
    cmds.addAttr(proxyObject, longName='colorR', attributeType='double', parent='mask')
    cmds.addAttr(proxyObject, longName='colorG', attributeType='double', parent='mask')
    cmds.addAttr(proxyObject, longName='colorB', attributeType='double', parent='mask')
    # Proxy
    inProxyNode = proxyObject + inProxyLabel
    cmds.createNode('aiStandIn', name=inProxyNode, parent=proxyObject)
    cmds.setAttr(inProxyNode + '.mode', 1)
    cmds.setAttr(inProxyNode + '.visibleInReflections', 1)
    cmds.setAttr(inProxyNode + '.visibleInRefractions', 1)
    cmds.setAttr(inProxyNode + '.dso', proxy, type='string')
    cmds.connectAttr(proxyObject + '.override', inProxyNode + '.overrideShaders', force=1)
    # Mask Nde_ShaderRef
    maskShader = proxyObject + maskLabel
    cmds.shadingNode('aiUtility', name=maskShader, asShader=1)
    cmds.setAttr(maskShader + '.shade_mode', 2)
    cmds.hyperShade(proxyObject, assign=maskShader)
    maskShadingEngine = proxyObject + maskLabel + 'SG'
    cmds.sets(inProxyNode, forceElement=maskShadingEngine)
    #
    cmds.connectAttr(proxyObject + '.mask.colorR', maskShader + '.color.colorR', force=1)
    cmds.connectAttr(proxyObject + '.mask.colorG', maskShader + '.color.colorG', force=1)
    cmds.connectAttr(proxyObject + '.mask.colorB', maskShader + '.color.colorB', force=1)
    # Box
    inBoxNode = proxyObject + inBoxLabel
    cmds.createNode('gpuCache', name=inBoxNode, parent=proxyObject)
    cmds.setAttr(inBoxNode + '.cacheFileName', box, type='string')
    cmds.connectAttr(proxyObject + '.box', inBoxNode + '.visibility')
    maUtils.setNodeTemplate(inBoxNode)
    # Gpu
    inGpuNode = proxyObject + inGpuLabel
    cmds.createNode('gpuCache', name=inGpuNode, parent=proxyObject)
    cmds.setAttr(inGpuNode + '.cacheFileName', gpu, type='string')
    cmds.connectAttr(proxyObject + '.gpu', inGpuNode + '.visibility')
    maUtils.setNodeTemplate(inGpuNode)
    # Container
    inContainerNode = proxyObject + inContainerLabel
    cmds.container(type='dagContainer', name=inContainerNode)
    cmds.setAttr(inContainerNode + '.blackBox', 1, lock=1)
    cmds.setAttr(inContainerNode + '.iconName', 'out_gpuCache.png', type='string')
    cmds.setAttr(inContainerNode + '.hiddenInOutliner', 1)
    cmds.container(inContainerNode, edit=1, force=1, addNode=[inBoxNode, inGpuNode])
    #
    cmds.parent(inContainerNode, proxyObject)
    maUtils.setObjectLockTransform(proxyObject, True)


#
def setRedshiftProxyCreate(objectString, box, gpu, proxy):
    def setRenderEnabled(node, enabled):
        if enabled is False:
            maAttr.setNodeUnrenderable(node)
    #
    proxyObject = objectString + asbProxyFileLabel
    #
    cmds.createNode('transform', name=proxyObject)
    # Switch
    cmds.addAttr(proxyObject, longName='box', attributeType='bool', keyable=1)
    cmds.setAttr(proxyObject + '.box', 0)
    cmds.addAttr(proxyObject, longName='gpu', attributeType='bool', keyable=1)
    cmds.setAttr(proxyObject + '.gpu', 1)
    # Render
    cmds.addAttr(proxyObject, longName='used', niceName='Used', attributeType='enum', enumName='lod00:lod01:lod02:')
    cmds.addAttr(proxyObject, longName='override', niceName='Override', attributeType='bool')
    cmds.addAttr(proxyObject, longName='mask', niceName='Mask', attributeType='double3')
    cmds.addAttr(proxyObject, longName='colorR', attributeType='double', parent='mask')
    cmds.addAttr(proxyObject, longName='colorG', attributeType='double', parent='mask')
    cmds.addAttr(proxyObject, longName='colorB', attributeType='double', parent='mask')
    # Proxy
    inProxyNode = proxyObject + inProxyLabel
    #
    cmds.createNode('RedshiftProxyMesh', name=inProxyNode)
    inProxyMesh = proxyObject + inProxyMeshLabel
    cmds.createNode('mesh', name=inProxyMesh, parent=proxyObject)
    cmds.connectAttr(inProxyNode + '.outMesh', inProxyMesh + '.inMesh')
    cmds.setAttr(inProxyNode + '.displayMode', 3)
    cmds.setAttr(inProxyNode + '.fileName', proxy, type='string')
    cmds.connectAttr(proxyObject + '.override', inProxyNode + '.objectIdMode', force=1)
    cmds.connectAttr(proxyObject + '.override', inProxyNode + '.visibilityMode', force=1)
    # Box
    inBoxNode = proxyObject + inBoxLabel
    cmds.createNode('gpuCache', name=inBoxNode, parent=proxyObject)
    cmds.setAttr(inBoxNode + '.cacheFileName', box, type='string')
    cmds.connectAttr(proxyObject + '.box', inBoxNode + '.visibility')
    maUtils.setNodeTemplate(inBoxNode)
    # Gpu
    inGpuNode = proxyObject + inGpuLabel
    cmds.createNode('gpuCache', name=inGpuNode, parent=proxyObject)
    cmds.setAttr(inGpuNode + '.cacheFileName', gpu, type='string')
    cmds.connectAttr(proxyObject + '.gpu', inGpuNode + '.visibility')
    maUtils.setNodeTemplate(inGpuNode)
    # Container
    inContainerNode = proxyObject + inContainerLabel
    cmds.container(type='dagContainer', name=inContainerNode)
    cmds.setAttr(inContainerNode + '.blackBox', 1, lock=1)
    cmds.setAttr(inContainerNode + '.iconName', 'out_gpuCache.png', type='string')
    cmds.setAttr(inContainerNode + '.hiddenInOutliner', 1)
    cmds.container(inContainerNode, edit=1, force=1, addNode=[inBoxNode, inGpuNode])
    #
    cmds.parent(inContainerNode, proxyObject)
    maUtils.setObjectLockTransform(proxyObject, True)


#
def setCreateProxyAov(aovData):
    for aovNode, aovName in aovData.items():
        if not maUtils.isAppExist(aovNode):
            inAovNode = aovNode + inAovLabel
            maUtils.setCreateNode('aiAOV', inAovNode)
            maUtils.setAttrStringDatumForce(inAovNode, 'name', aovName)


#
def getProxyAovData():
    dic = bscCore.orderedDict()
    aovNodes = cmds.ls(type='aiAOV')
    if aovNodes:
        for inAovNode in aovNodes:
            if inAovNode.endswith(inAovLabel):
                aovNode = inAovNode.split(':')[-1][:-len(inAovLabel)]
                aovName = maUtils.getAttrDatum(inAovNode, 'name')
                dic[aovNode] = aovName
    return dic


#
def setCreateAssemblyDefinition(objectString, box, gpu, proxy, asset, withLod=1):
    adObject = objectString + definitionLabel
    cmds.container(type='assemblyDefinition', name=adObject)
    # GPU
    cmds.assembly(
        adObject,
        edit=1,
        createRepresentation='Cache',
        repName='GPU',
        input=gpu)
    gpuExt = os.path.splitext(gpu)[1]
    if withLod:
        for level in range(2):
            gpuLod = gpu[:-len(gpuExt)] + '_lod%s' % str(level + 1).zfill(2) + gpuExt
            cmds.assembly(
                adObject,
                edit=1,
                createRepresentation='Cache',
                repName='GPU-LOD%s' % str(level + 1).zfill(2),
                input=gpuLod)
    # Proxy
    cmds.assembly(
        adObject,
        edit=1,
        createRepresentation='Scene',
        repName='Proxy',
        input=proxy)
    dsoExt = os.path.splitext(proxy)[1]
    if withLod:
        for level in range(2):
            dsoLod = proxy[:-len(dsoExt)] + '_lod%s' % str(level + 1).zfill(2) + dsoExt
            cmds.assembly(
                adObject,
                edit=1,
                createRepresentation='Scene',
                repName='Proxy-LOD%s' % str(level + 1).zfill(2),
                input=dsoLod)
    # BOX
    cmds.assembly(
        adObject,
        edit=1,
        createRepresentation='Cache',
        repName='Box',
        input=box)
    # Asset
    cmds.assembly(
        adObject,
        edit=1,
        createRepresentation='Scene',
        repName='Asset', input=asset)
    cmds.assembly(
        adObject, edit=1, active='Proxy')


#
def randColor(colorRand, mesh=none):
    if not mesh:
        mesh = cmds.ls(type='mesh')
    #
    sg = []
    n = [str(i).zfill(3) for i in range(0, colorRand)]
    for i in n:
        colorName = 'color_' + i
        sgName = 'color_' + i + 'SG'
        sg.append(sgName)
        c = [i / 100.0 for i in range(0, 100)]
        if not cmds.objExists(colorName):
            cmds.shadingNode('lambert', n=colorName, asShader=True)
            cmds.setAttr(colorName + '.color', choice(c), choice(c), choice(c))
            cmds.sets(renderable=1, noSurfaceShader=1, empty=1, n=sgName)
            cmds.connectAttr(colorName + '.color', sgName + '.surfaceShader')
    if mesh:
        for i in mesh:
            cmds.sets(i, forceElement=choice(sg))


#
def dynDso(overrideFrameRange, mode=2):
    objects = cmds.ls(type='aiStandIn')
    for objectString in objects:
        cmds.setAttr(objectString + '.mode', mode)
        transform = cmds.listRelatives(objectString, parent=1, fullPath=1)[0]
        if not cmds.objExists(transform + '.overrideFrameRange'):
            cmds.addAttr(transform, ln='overrideFrameRange', at='long')
        cmds.setAttr(transform + '.overrideFrameRange', overrideFrameRange)
        if not cmds.objExists(transform + '.overrideFrameOffset'):
            cmds.addAttr(transform, ln='overrideFrameOffset', at='long')
        cmds.setAttr(transform + '.overrideFrameOffset', choice(range(0, 86)))
        try:
            exp = '%s.frameNumber = 1 + ((frame - %s.overrideFrameOffset)/%s.overrideFrameRange - floor((frame - %s.overrideFrameOffset)/%s.overrideFrameRange))*%s.overrideFrameRange'\
                  % (objectString, transform, transform, transform, transform, transform)
            cmds.expression(o=objectString, s=exp)
        except:
            pass