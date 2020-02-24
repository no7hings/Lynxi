# coding=utf-8
import os
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxBasic import bscMethods
#
from LxMaya.command import maUtils, maCam
#
previewWindowName = 'animationPreviewWindow'
previewPanelName = 'animationPreviewPanel'
#
none = ''


# Remove Preview Window
def removeMayaWindow(window):
    try:
        cmds.deleteUI(window, window=1)
        cmds.windowPref(window, remove=1)
    except:
        cmds.windowPref(window, exists=0)


#
def setPreviewCamera(camera, object):
    cmds.setAttr(camera + '.translateX', 28)
    cmds.setAttr(camera + '.translateY', 21)
    cmds.setAttr(camera + '.translateZ', 28)
    cmds.setAttr(camera + '.rotateX', -27.9383527296)
    cmds.setAttr(camera + '.rotateY', 45)
    cmds.setAttr(camera + '.rotateZ', 0)
    #
    cmds.select(object)
    cmds.viewFit(camera, fitFactor=0, animate=1)
    #
    cmds.setAttr(camera + '.focalLength', 57.089)
    cmds.select(clear=1)


#
def setViewportVp2Renderer(modelPanel, mode=0):
    # Render Name [<vp2Renderer>, ]
    currentPanel = modelPanel
    rendererName = 'base_OpenGL_Renderer'
    if mode == 1:
        rendererName = 'vp2Renderer'
    panelType = cmds.getPanel(typeOf=currentPanel)
    if panelType == 'modelPanel':
        cmds.modelEditor(currentPanel, edit=1, rendererName=rendererName, rom='myOverride')
        if rendererName == 'vp2Renderer':
            cmds.setAttr('hardwareRenderingGlobals.lineAAEnable', 1)
            cmds.setAttr('hardwareRenderingGlobals.multiSampleEnable', 1)
            # cmds.setAttr('hardwareRenderingGlobals.ssaoEnable', 1)


# Make Preview
def makePreview(
        fileString_, camera,
        useDefaultMaterial, percent, quality,
        startFrame, endFrame, widthHeight,
        showOrnaments=1, displayResolution=0, displaySafeTitle=0,
        displayMode=6
):
    width, height = widthHeight
    #
    widthReduce = width
    heightReduce = height
    # Reduce Width and Height
    checkValue = max(widthHeight)
    if checkValue > 2048:
        if width > height:
            widthReduce = 2048
            heightReduce = 2048 * height / width
        elif width < height:
            widthReduce = 2048 * width / height
            heightReduce = 2048
    #
    widthHeightReduce = (widthReduce, heightReduce)
    #
    bscMethods.OsFile.createDirectory(fileString_)
    fileName = os.path.basename(fileString_)
    #
    isMov = os.path.splitext(fileName)[-1] == '.mov'
    osFormat = [os.path.splitext(fileName)[-1][1:], u'qt'][isMov]
    compression = [u'IYUV 编码解码器', u'H.264'][isMov]
    #
    prvName = os.path.splitext(fileString_)[0]
    #
    prvWindow = previewWindowName
    removeMayaWindow(prvWindow)
    cmds.window(prvWindow, title='Animation Preview')
    paneLayout = cmds.paneLayout(width=widthReduce / 2, height=heightReduce / 2)
    #
    animationPanel = cmds.modelPanel(
        label=previewPanelName,
        parent=paneLayout,
        menuBarVisible=0,
        modelEditor=0,
        camera=camera
    )
    #
    cmds.displayRGBColor('background', .25, .25, .25)
    cmds.displayRGBColor('backgroundTop', .25, .25, .25)
    cmds.displayRGBColor('backgroundBottom', .25, .25, .25)
    #
    cmds.showWindow(prvWindow)
    setViewportVp2Renderer(animationPanel, 1)
    # Open HUD
    maCam.setCameraCloseHud()
    maCam.setCameraView(maUtils._getNodeShapeNodeString(camera), displayResolution, displaySafeTitle)
    maCam.setCameraHud('large')
    # Set Maye View
    cmds.modelEditor(
        animationPanel,
        edit=1,
        activeView=1,
        wireframeOnShaded=0,
        fogging=0,
        dl='default',
        twoSidedLighting=1,
        allObjects=0,
        manipulators=0,
        grid=0,
        hud=1,
        sel=0
    )
    #
    cmds.modelEditor(
        animationPanel,
        edit=1,
        activeView=1,
        useDefaultMaterial=useDefaultMaterial,
        polymeshes=1,
        subdivSurfaces=1,
        fluids=1,
        strokes=1,
        nCloths=1,
        nParticles=1,
        pluginShapes=1,
        pluginObjects=['gpuCacheDisplayFilter', 1],
        displayAppearance='smoothShaded',
    )
    if displayMode == 5:
        maUtils.setViewportShaderDisplayMode(animationPanel)
    elif displayMode == 6:
        maUtils.setViewportTextureDisplayMode(animationPanel)
    elif displayMode == 7:
        maUtils.setViewportLightDisplayMode(animationPanel)
    # Video Preview
    cmds.playblast(
        startTime=startFrame,
        endTime=endFrame,
        format=osFormat,
        filename=prvName,
        clearCache=1,
        viewer=0,
        showOrnaments=showOrnaments,
        offScreen=1,
        framePadding=4,
        percent=percent,
        compression=compression,
        quality=quality,
        widthHeight=widthHeightReduce
    )
    # Image Preview
    maCam.setCameraCloseHud()
    # maCam.setCameraView(maUtils._getNodeShapeNodeString(camera))
    midFrame = int((endFrame - startFrame) / 2 + startFrame)
    frameRange = [startFrame, midFrame, endFrame]
    frameDic = {startFrame: '0000', midFrame: '0001', endFrame: '0002'}
    imagePreviewFiles = []
    for frame in frameRange:
        cmds.playblast(
            startTime=frame,
            endTime=frame,
            format='iff',
            filename=prvName,
            sequenceTime=0,
            clearCache=1,
            viewer=0,
            showOrnaments=0,
            offScreen=0,
            framePadding=4,
            percent=percent,
            compression='jpg',
            quality=quality
        )
        imagePreviewFile = prvName + '_' + frameDic[frame] + '.jpg'
        if bscMethods.OsFile.isExist(imagePreviewFile):
            bscMethods.OsFile.remove(imagePreviewFile)
        #
        bscMethods.OsFile.renameTo(prvName + '.' + str(frame).zfill(4) + '.jpg', imagePreviewFile)
        imagePreviewFiles.append(imagePreviewFile)
    # Remove Widow
    removeMayaWindow(prvWindow)
    return imagePreviewFiles


# Make Snapshot
def makeSnapshot(
        fileString_, camera,
        useDefaultMaterial, percent, quality,
        startFrame, endFrame, widthHeight):
    bscMethods.OsFile.createDirectory(fileString_)
    filePath = os.path.dirname(fileString_)
    fileName = os.path.basename(fileString_)
    #
    format = fileName.split('.')[1]
    prvName = '%s/%s' % (filePath, fileName.split('.')[0])
    prvWindow = 'animationSnapshotWindow'
    removeMayaWindow(prvWindow)
    cmds.window(prvWindow, title='Animation Snapshot')
    paneLayout = cmds.paneLayout(width=widthHeight[0] / 2, height=widthHeight[1] / 2)
    animationPanel = cmds.modelPanel(
        label='animationPreviewPanel',
        parent=paneLayout,
        menuBarVisible=0,
        modelEditor=0,
        camera=camera)
    # View Texture
    if useDefaultMaterial == 0:
        maUtils.setViewportTextureDisplayMode(animationPanel)
    # Default Nde_ShaderRef
    cmds.setAttr('lambert1.color', .5, .5, .5)
    # Background
    cmds.displayRGBColor('background', .25, .25, .25)
    cmds.displayRGBColor('backgroundTop', .25, .25, .25)
    cmds.displayRGBColor('backgroundBottom', .25, .25, .25)
    cmds.showWindow(prvWindow)
    maCam.setCameraCloseHud()
    maCam.setCameraView(maUtils._getNodeShapeNodeString(camera))
    # Set Maye View
    cmds.modelEditor(
        animationPanel,
        edit=1,
        activeView=1,
        useDefaultMaterial=useDefaultMaterial,
        wireframeOnShaded=0,
        dl='default',
        twoSidedLighting=1,
        allObjects=0,
        manipulators=0,
        grid=0,
        hud=1,
        sel=0
    )
    # Set Maye View
    cmds.modelEditor(
        animationPanel,
        edit=1,
        activeView=1,
        polymeshes=1,
        subdivSurfaces=1,
        fluids=1,
        strokes=1,
        nCloths=1,
        nParticles=1,
        pluginObjects=['gpuCacheDisplayFilter', 1],
        displayAppearance='flatShaded'
    )
    # Image Preview
    midFrame = int((endFrame - startFrame) / 2 + startFrame)
    frameRange = [startFrame, midFrame, endFrame]
    frameDic = {startFrame: '0000', midFrame: '0001', endFrame: '0002'}
    for frame in frameRange:
        cmds.playblast(
            startTime=frame,
            endTime=frame,
            format='iff',
            filename=prvName,
            sequenceTime=0,
            clearCache=1,
            viewer=0,
            showOrnaments=0,
            offScreen=0,
            framePadding=4,
            percent=percent,
            compression='jpg',
            quality=quality
        )
        previewFile = prvName + frameDic[frame] + '.jpg'
        if os.path.exists(previewFile):
            os.remove(previewFile)
        os.rename(prvName + '.' + str(frame).zfill(4) + '.jpg', previewFile)
    # Display Mode
    if useDefaultMaterial == 0:
        maUtils.setViewportShaderDisplayMode(animationPanel)
    # Default Nde_ShaderRef
    cmds.setAttr('lambert1.color', .5, .5, .5)
    # Remove Widow
    removeMayaWindow(prvWindow)