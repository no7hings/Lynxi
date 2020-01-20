# coding=utf-8
import os
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from random import choice
#
from LxBasic import bscMethods, bscCommands
#
from LxMaya.command import maUtils, maAttr, maProxy
#
inBoxLabel = '_inBox'
inGpuLabel = '_inGpu'
inProxyLabel = '_inPrx'
inProxyMeshLabel = '_inPrxMsh'
inAovLabel = '_inAov'
maskLabel = '_mask'
inContainerLabel = '_inContainer'
inExpressionLabel = '_inExpression'
#
none = ''


#
def setOutActProxy(osFile, frame, renderer):
    bscMethods.OsFile.createDirectory(osFile)
    # Set Frame
    cmds.currentTime(frame)
    maProxy.setOutProxy(osFile, renderer, 1)


#
def setGpu(maObj, box, gpu, frameCount, inNodes):
    def setRenderEnabled(node, enabled):
        if enabled is False:
            maAttr.setNodeUnrenderable(node)
    for seq in range(frameCount):
        currentTime = seq + 1
        subBox = ('_' + str(currentTime).zfill(4)).join(os.path.splitext(box))
        inBox = maObj + inBoxLabel + str(seq)
        cmds.createNode('gpuCache', name=inBox, parent=maObj)
        cmds.setAttr(inBox + '.cacheFileName', subBox, type='string')
        cmds.setAttr(inBox + '.visibility', keyable=1)
        inNodes.append(inBox)
        setRenderEnabled(inBox, False)
        #
        subGpu = ('_' + str(currentTime).zfill(4)).join(os.path.splitext(gpu))
        inGpu = maObj + inGpuLabel + str(seq)
        cmds.createNode('gpuCache', name=inGpu, parent=maObj)
        cmds.setAttr(inGpu + '.cacheFileName', subGpu, type='string')
        cmds.setAttr(inGpu + '.visibility', keyable=1)
        inNodes.append(inGpu)
        setRenderEnabled(inGpu, False)
        #
        inMult = maObj + '_inMult' + str(seq)
        cmds.createNode('multiplyDivide', name=inMult)
        cmds.connectAttr(maObj + '.box', inMult + '.input1X')
        cmds.connectAttr(maObj + '.gpu', inMult + '.input1Y')
        cmds.connectAttr(inMult + '.outputX', inBox + '.visibility')
        cmds.connectAttr(inMult + '.outputY', inGpu + '.visibility')
        inNodes.append(inMult)
        #
        inFrame = maObj + '_inFrame' + str(seq)
        cmds.createNode('animCurveUU', name=inFrame)
        cmds.connectAttr(maObj + '.frame', inFrame + '.input')
        cmds.connectAttr(inFrame + '.output', inMult + '.input2X')
        cmds.connectAttr(inFrame + '.output', inMult + '.input2Y')
        cmds.setAttr(inFrame + '.preInfinity', 3)
        cmds.setAttr(inFrame + '.postInfinity', 3)
        inNodes.append(inFrame)
        #
        timeRange = range(currentTime, currentTime + 2)
        #
        boolean = currentTime == frameCount
        #
        for time in timeRange:
            value = 0
            if time == currentTime:
                value = 1
            cmds.setDrivenKeyframe(
                inMult + '.input2X', currentDriver=maObj + '.frame', value=value,
                driverValue=time, outTangentType='step')
        cmds.setDrivenKeyframe(
            inMult + '.input2X', currentDriver=maObj + '.frame',
            driverValue=0, value=0, outTangentType='step')
        cmds.setDrivenKeyframe(
            inMult + '.input2X', currentDriver=maObj + '.frame',
            driverValue=frameCount, value=0, outTangentType='step')
        if boolean:
            cmds.setDrivenKeyframe(
                inMult + '.input2X', currentDriver=maObj + '.frame',
                driverValue=0, value=1, outTangentType='step')
            cmds.setDrivenKeyframe(
                inMult + '.input2X', currentDriver=maObj + '.frame',
                driverValue=1, value=0, outTangentType='step')
            cmds.setDrivenKeyframe(
                inMult + '.input2X', currentDriver=maObj + '.frame',
                driverValue=frameCount, value=1, outTangentType='step')


#
def setActProxy(maObj, box, gpu, proxy, startFrame, endFrame, renderer):
    if renderer == 'Arnold':
        setArnoldActProxy(maObj, box, gpu, proxy, startFrame, endFrame)
    if renderer == 'Redshift':
        setRedshiftActProxy(maObj, box, gpu, proxy, startFrame, endFrame)


#
def setArnoldActProxy(maObj, box, gpu, proxy, startFrame, endFrame):
    proxyFrameAttrName = 'frameNumber'
    #
    frameCount = endFrame - startFrame + 1
    cmds.createNode('transform', name=maObj)
    # Add Attr
    cmds.addAttr(maObj, longName='startFrame', attributeType='long', keyable=1)
    cmds.setAttr(maObj + '.startFrame', 1, lock=1)
    cmds.addAttr(maObj, longName='endFrame', attributeType='long', keyable=1)
    cmds.setAttr(maObj + '.endFrame', frameCount, lock=1)
    cmds.addAttr(maObj, longName='frame', attributeType='long', keyable=1)
    cmds.addAttr(maObj, longName='time', attributeType='long', keyable=1)
    cmds.connectAttr('time1.outTime', maObj + '.time')
    cmds.addAttr(maObj, longName='speed', attributeType='double', min=1, max=100, keyable=1)
    cmds.setAttr(maObj + '.speed', 1)
    cmds.addAttr(maObj, longName='offset', attributeType='long', min=-frameCount, max=frameCount, keyable=1)
    #
    cmds.addAttr(maObj, longName='box', attributeType='bool', keyable=1)
    cmds.setAttr(maObj + '.box', 0)
    cmds.addAttr(maObj, longName='gpu', attributeType='bool', keyable=1)
    cmds.setAttr(maObj + '.gpu', 1)
    #
    cmds.addAttr(maObj, longName='used', attributeType='enum', enumName='lod00:lod01:lod02:', keyable=1)
    cmds.addAttr(maObj, longName='override', attributeType='bool', keyable=1)
    cmds.addAttr(maObj, longName='mask', attributeType='double3', keyable=1)
    cmds.addAttr(maObj, longName='colorR', attributeType='double', parent='mask', keyable=1)
    cmds.addAttr(maObj, longName='colorG', attributeType='double', parent='mask', keyable=1)
    cmds.addAttr(maObj, longName='colorB', attributeType='double', parent='mask', keyable=1)
    # DSO
    inProxyNode = maObj + inProxyLabel
    #
    cmds.createNode('aiStandIn', name=inProxyNode, parent=maObj)
    cmds.setAttr(inProxyNode + '.mode', 1)
    cmds.setAttr(inProxyNode + '.visibleInReflections', 1)
    cmds.setAttr(inProxyNode + '.visibleInRefractions', 1)
    cmds.setAttr(inProxyNode + '.dso', proxy, type='string')
    cmds.connectAttr(maObj + '.override', inProxyNode + '.overrideShaders', force=1)
    #
    inExpressionNode = maObj + inExpressionLabel
    #
    gpuCommand = \
        '''%s.frame =
        abs((%s.time + %s.endFrame
        + %s.offset
        + floor(%s.time / %s.endFrame)*2)
        %% (%s.endFrame + 1))
        %% %s.endFrame * %s.speed + 1 ;\r\n''' % \
        (maObj, maObj, maObj, maObj, maObj, maObj, maObj, maObj, maObj)
    #
    proxyCommand = \
        '''%s.%s = %s.frame ;
        ''' % (inProxyNode, proxyFrameAttrName, maObj)
    cmds.expression(name=inExpressionNode, string=gpuCommand + proxyCommand, object=maObj, alwaysEvaluate=1,
                    unitConversion=1)
    cmds.setAttr(maObj + '.frame', lock=1)
    timeConversion = maObj + 'timeConversion'
    cmds.rename('timeToUnitConversion1', timeConversion)
    inNodes = [inExpressionNode, timeConversion]
    #
    setGpu(maObj, box, gpu, frameCount, inNodes)
    # Container
    inContainerNode = maObj + inContainerLabel
    cmds.container(type='dagContainer', name=inContainerNode)
    cmds.setAttr(inContainerNode + '.blackBox', 1, lock=1)
    cmds.setAttr(inContainerNode + '.iconName', 'out_gpuCache.png', type='string')
    cmds.setAttr(inContainerNode + '.hiddenInOutliner', 1)
    cmds.container(inContainerNode, edit=1, force=1, addNode=inNodes)
    #
    cmds.parent(inContainerNode, maObj)
    maUtils.setObjectLockTransform(maObj, True)
    #
    cmds.setAttr(inProxyNode + '.' + proxyFrameAttrName, lock=1)
    cmds.setAttr(inContainerNode + '.hiddenInOutliner', 1)


#
def setRedshiftActProxy(maObj, box, gpu, proxy, startFrame, endFrame):
    proxyFrameAttrName = 'frameExtension'
    #
    frameCount = endFrame - startFrame + 1
    cmds.createNode('transform', name=maObj)
    # Add Attr
    cmds.addAttr(maObj, longName='startFrame', attributeType='long', keyable=1)
    cmds.setAttr(maObj + '.startFrame', 1, lock=1)
    cmds.addAttr(maObj, longName='endFrame', attributeType='long', keyable=1)
    cmds.setAttr(maObj + '.endFrame', frameCount, lock=1)
    cmds.addAttr(maObj, longName='frame', attributeType='long', keyable=1)
    cmds.addAttr(maObj, longName='time', attributeType='long', keyable=1)
    cmds.connectAttr('time1.outTime', maObj + '.time')
    cmds.addAttr(maObj, longName='speed', attributeType='double', min=1, max=100, keyable=1)
    cmds.setAttr(maObj + '.speed', 1)
    cmds.addAttr(maObj, longName='offset', attributeType='long', min=-frameCount, max=frameCount, keyable=1)
    #
    cmds.addAttr(maObj, longName='box', attributeType='bool', keyable=1)
    cmds.setAttr(maObj + '.box', 0)
    cmds.addAttr(maObj, longName='gpu', attributeType='bool', keyable=1)
    cmds.setAttr(maObj + '.gpu', 1)
    #
    cmds.addAttr(maObj, longName='used', attributeType='enum', enumName='lod00:lod01:lod02:', keyable=1)
    cmds.addAttr(maObj, longName='override', attributeType='bool', keyable=1)
    cmds.addAttr(maObj, longName='mask', attributeType='double3', keyable=1)
    cmds.addAttr(maObj, longName='colorR', attributeType='double', parent='mask', keyable=1)
    cmds.addAttr(maObj, longName='colorG', attributeType='double', parent='mask', keyable=1)
    cmds.addAttr(maObj, longName='colorB', attributeType='double', parent='mask', keyable=1)
    # DSO
    inProxyNode = maObj + inProxyLabel
    #
    cmds.createNode('RedshiftProxyMesh', name=inProxyNode)
    inProxyMesh = maObj + inProxyMeshLabel
    cmds.createNode('mesh', name=inProxyMesh, parent=maObj)
    cmds.connectAttr(inProxyNode + '.outMesh', inProxyMesh + '.inMesh')
    cmds.setAttr(inProxyNode + '.displayMode', 3)
    cmds.setAttr(inProxyNode + '.fileName', proxy, type='string')
    cmds.connectAttr(maObj + '.override', inProxyNode + '.objectIdMode', force=1)
    cmds.connectAttr(maObj + '.override', inProxyNode + '.visibilityMode', force=1)
    #
    inExpressionNode = maObj + inExpressionLabel
    #
    gpuCommand = \
        '''%s.frame =
        abs((%s.time + %s.endFrame
        + %s.offset
        + floor(%s.time / %s.endFrame)*2)
        %% (%s.endFrame + 1))
        %% %s.endFrame * %s.speed + 1 ;\r\n''' % \
        (maObj, maObj, maObj, maObj, maObj, maObj, maObj, maObj, maObj)
    #
    proxyCommand = \
        '''%s.%s = %s.frame ;
        ''' % (inProxyNode, proxyFrameAttrName, maObj)
    cmds.expression(name=inExpressionNode, string=gpuCommand + proxyCommand, object=maObj, alwaysEvaluate=1,
                    unitConversion=1)
    cmds.setAttr(maObj + '.frame', lock=1)
    timeConversion = maObj + 'timeConversion'
    cmds.rename('timeToUnitConversion1', timeConversion)
    inNodes = [inExpressionNode, timeConversion]
    #
    setGpu(maObj, box, gpu, frameCount, inNodes)
    # Container
    inContainerNode = maObj + inContainerLabel
    cmds.container(type='dagContainer', name=inContainerNode)
    cmds.setAttr(inContainerNode + '.blackBox', 1, lock=1)
    cmds.setAttr(inContainerNode + '.iconName', 'out_gpuCache.png', type='string')
    cmds.setAttr(inContainerNode + '.hiddenInOutliner', 1)
    cmds.container(inContainerNode, edit=1, force=1, addNode=inNodes)
    #
    cmds.parent(inContainerNode, maObj)
    maUtils.setObjectLockTransform(maObj, True)
    #
    cmds.setAttr(inProxyNode + '.useFrameExtension', 1)
    cmds.setAttr(inProxyNode + '.' + proxyFrameAttrName, lock=1)


#
def setAssemblySceneDefinitionCreate(adFile, proxy):
    adObject = os.path.splitext(os.path.basename(adFile))[0]
    cmds.assembly(name=adObject, type='assemblyDefinition')
    # Proxy
    cmds.assembly(
        adObject,
        edit=1,
        createRepresentation='Scene',
        repName='Proxy',
        input=proxy
    )


#
def getPercentage(mesh, scale=.01):
    var = 53333
    worldArea = cmds.polyEvaluate(mesh, worldArea=1)
    vertex = cmds.polyEvaluate(mesh, vertex=1)
    return int(vertex / worldArea / scale / var)


#
def setReduce(mesh, scale, miniPercentage, maxPercentage):
    var = getPercentage(mesh, scale)
    percentage = [miniPercentage, [var, maxPercentage][var > maxPercentage]][var > miniPercentage]
    cmds.polyReduce(
        mesh,
        version=1,
        termination=0,
        percentage=percentage,
        symmetryPlaneX=0,
        symmetryPlaneY=0,
        symmetryPlaneZ=0,
        symmetryPlaneW=0,
        keepQuadsWeight=0,
        vertexCount=0,
        triangleCount=0,
        sharpness=0,
        keepColorBorder=0,
        keepFaceGroupBorder=0,
        keepHardEdge=0,
        keepCreaseEdge=1,
        keepBorderWeight=0,
        keepMapBorderWeight=0,
        keepColorBorderWeight=0,
        keepFaceGroupBorderWeight=0,
        keepHardEdgeWeight=0,
        keepCreaseEdgeWeight=.5,
        useVirtualSymmetry=0,
        symmetryTolerance=0.01,
        vertexMapName='',
        replaceOriginal=1,
        cachingReduce=1,
        constructionHistory=0)
    cmds.polyTriangulate(mesh, constructionHistory=0)


#
def setShadingEngine(shaderName, shadingEngineName, r, g, b):
    if not cmds.objExists(shaderName):
        cmds.shadingNode('lambert', name=shaderName, asShader=1)
    if not cmds.objExists(shadingEngineName):
        cmds.sets(name=shadingEngineName, renderable=1, noSurfaceShader=1, empty=1)
    sourceAttr = shaderName + '.color'
    targetAttr = shadingEngineName + '.surfaceShader'
    if not cmds.isConnected(sourceAttr, targetAttr):
        cmds.connectAttr(sourceAttr, targetAttr)
    cmds.setAttr(shaderName + '.color', r, g, b)


#
def setRandColor(colorRand, meshObjects=none):
    if not meshObjects:
        meshObjects = cmds.ls(type='mesh')
    #
    shadingEngineArray = []
    n = [str(i).zfill(3) for i in range(0, colorRand)]
    for i in n:
        shaderName = 'color_' + i
        shadingEngineName = shaderName + 'SG'
        shadingEngineArray.append(shadingEngineName)
        colorRange = [i / 100.0 for i in range(0, 100)]
        setShadingEngine(shaderName, shadingEngineName, choice(colorRange), choice(colorRange), choice(colorRange))
    bodyShaderName = 'skincls_color'
    bodyShadingEngine = bodyShaderName + 'SG'
    setShadingEngine(bodyShaderName, bodyShadingEngine, 1, .65, .65)
    if meshObjects:
        for mesh in meshObjects:
            cmds.sets(mesh, forceElement=choice(shadingEngineArray))
            if '_body' in mesh and not '_bodyAss' in mesh:
                cmds.sets(mesh, forceElement=bodyShadingEngine)