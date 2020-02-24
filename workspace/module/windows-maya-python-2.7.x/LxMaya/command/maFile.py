# coding=utf-8
import os, shutil, json
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.mel as mel

from LxBasic import bscMethods, bscObjects
#
from LxCore.config import appCfg
#
from LxMaya.command import maUtils
#
tempFolderLabel = 'temp'
gzExtLabel = '.gz'
#
none = ''


# Remove Maya Window
def removeMayaWindow(window):
    try:
        cmds.deleteUI(window, window=1)
        cmds.windowPref(window, remove=1)
    except:
        cmds.windowPref(window, exists=0)


# Make Snapshot
def makeSnapshot(objectString, osImageFile, useDefaultMaterial=1, width=720, height=720, useDefaultView=1, overrideColor=None):
    temporaryFile = bscMethods.OsFile.temporaryName(osImageFile)
    tempPrv = os.path.splitext(temporaryFile)[0]
    #
    prvWindow = 'snapShot'
    removeMayaWindow(prvWindow)
    cmds.window(prvWindow, title='Snap Shot')
    paneLayout = cmds.paneLayout(width=width, height=height)
    snapView = cmds.modelPanel(
        label='snapShotPanel',
        parent=paneLayout,
        menuBarVisible=1,
        modelEditor=1,
        camera='persp'
    )
    #
    camera = 'persp'
    cameraShape = 'perspShape'
    #
    cmds.camera(
        cameraShape,
        edit=1,
        displayFilmGate=0,
        displaySafeAction=0,
        displaySafeTitle=0,
        displayFieldChart=0,
        displayResolution=0,
        displayGateMask=0,
        filmFit=1,
        overscan=1.15
    )
    #
    if not useDefaultMaterial:
        maUtils.setDisplayMode(6)
    else:
        maUtils.setDisplayMode(5)
    #
    cmds.displayRGBColor('background', .25, .25, .25)
    cmds.displayRGBColor('backgroundTop', .25, .25, .25)
    cmds.displayRGBColor('backgroundBottom', .25, .25, .25)
    cmds.showWindow(prvWindow)
    # Set ModelPanel ( Viewport 2.0 )
    maUtils.setViewportVp2Renderer(snapView, 1)
    #
    cmds.modelEditor(
        snapView,
        edit=1,
        activeView=1,
        useDefaultMaterial=useDefaultMaterial,
        wireframeOnShaded=0,
        fogging=0,
        dl='default',
        twoSidedLighting=1,
        allObjects=0,
        manipulators=0,
        grid=0,
        hud=1,
        sel=0)
    #
    cmds.modelEditor(
        snapView,
        edit=1,
        activeView=1,
        polymeshes=1,
        subdivSurfaces=1,
        fluids=1,
        strokes=1,
        nCloths=1,
        nParticles=1,
        pluginShapes=1,
        pluginObjects=['gpuCacheDisplayFilter', 1],
        displayAppearance='smoothShaded')
    #
    cmds.select(objectString)
    cmds.isolateSelect(snapView, state=1)
    #
    if useDefaultView:
        cmds.setAttr(camera + '.translateX', 28)
        cmds.setAttr(camera + '.translateY', 21)
        cmds.setAttr(camera + '.translateZ', 28)
        cmds.setAttr(camera + '.rotateX', -27.9383527296)
        cmds.setAttr(camera + '.rotateY', 45)
        cmds.setAttr(camera + '.rotateZ', 0)
        cmds.setAttr(camera + '.farClipPlane', 1000000)
        #
        cmds.viewFit(cameraShape, fitFactor=0, animate=1)
    cmds.select(clear=1)
    # Y Axis Adjust
    yAxis = cmds.getAttr('persp.translateY')
    # Default Nde_ShaderRef Adjust
    if overrideColor is not None:
        r, g, b = overrideColor
        cmds.setAttr('lambert1.color', r, g, b)
    else:
        cmds.setAttr('lambert1.color', 0, .75, .75)
    # Image Preview
    cmds.playblast(
        startTime=0,
        endTime=0,
        format='iff',
        filename=tempPrv,
        sequenceTime=0,
        clearCache=1,
        viewer=0,
        showOrnaments=0,
        offScreen=0,
        framePadding=4,
        percent=100,
        compression='jpg',
        quality=100,
        widthHeight=(width, height))
    #
    cmds.isolateSelect(snapView, state=0)
    removeMayaWindow(prvWindow)
    maUtils.setDisplayMode(5)
    #
    tempPrvFile = tempPrv + '.0000.jpg'
    bscMethods.OsFile.copyTo(tempPrvFile, osImageFile)
    cmds.setAttr('lambert1.color', .5, .5, .5)


#
def fbxExport(objectStrings, fileString):
    objectStrings = bscMethods.String.toList(objectStrings)
    maUtils.setNodeSelect(objectStrings)
    #
    temporaryFile = bscMethods.OsFile.temporaryName(fileString)
    #
    cmds.loadPlugin('gameFbxExporter', quiet=1)
    #
    cmds.file(
        temporaryFile,
        exportSelected=1,
        type='FBX export',
        options='v=0',
        preserveReferences=0,
        force=1
    )
    bscMethods.OsFile.copyTo(temporaryFile, fileString)
    #
    maUtils.setSelClear()


#
def abcExport(objectString, fileString, startFrame, endFrame, step, attrs=None):
    def getOptionArg():
        return '-worldSpace -writeVisibility -dataFormat ogawa'
    #
    def getFileArg():
        return '-file {0}'.format(temporaryFile)
    #
    def getTimeArg():
        return '-frameRange {0} {1} -step {2}'.format(startFrame, endFrame, step)
    #
    def getRootArg():
        argString = None
        #
        lis = []
        #
        if isinstance(objectString, str) or isinstance(objectString, unicode):
            if maUtils._isAppExist(objectString):
                lis = [objectString]
        elif isinstance(objectString, tuple) or isinstance(objectString, list):
            for i in objectString:
                if maUtils._isAppExist(i):
                    lis.append(i)
        #
        if lis:
            argString = ' '.join(['-root %s' % i for i in lis])
        #
        return argString
    #
    def getAttrArg():
        argString = None
        #
        lis = []
        #
        if isinstance(attrs, str) or isinstance(attrs, unicode):
            lis = [attrs]
        elif isinstance(attrs, tuple) or isinstance(attrs, list):
            for i in attrs:
                lis.append(i)
        #
        if lis:
            argString = ' '.join(['-attr %s' % i for i in lis])
        #
        return argString
    #
    temporaryFile = bscMethods.OsFile.temporaryName(fileString)
    #
    exportArg = None
    #
    timeArg = getTimeArg()
    optionArg = getOptionArg()
    fileArg = getFileArg()
    # Root
    rootArg = getRootArg()
    # Attribute
    attrArg = getAttrArg()
    #
    if rootArg:
        exportArg = ' '.join([timeArg, optionArg, rootArg, fileArg])
        if attrArg:
            exportArg = ' '.join([timeArg, attrArg, optionArg, rootArg, fileArg])
    #
    if exportArg:
        cmds.loadPlugin('AbcExport', quiet=1)
        #
        cmds.AbcExport(j=exportArg)
        #
        bscMethods.OsFile.copyTo(temporaryFile, fileString)


#
def gpuExport(objectString, fileString, startFrame, endFrame, withMaterial=0):
    cmds.loadPlugin('gpuCache', quiet=1)
    if cmds.objExists(objectString):
        temporaryFile = bscMethods.OsFile.temporaryName(fileString)
        #
        path = os.path.dirname(temporaryFile)
        fileName = os.path.splitext(os.path.basename(temporaryFile))[0]
        cmds.gpuCache(
            objectString,
            startTime=startFrame, endTime=endFrame,
            optimize=1, optimizationThreshold=40000,
            writeMaterials=withMaterial, dataFormat='ogawa',
            directory=path,
            fileName=fileName
        )
        #
        bscMethods.OsFile.copyTo(temporaryFile, fileString)


#
def gpuSeqExport(objectString, startFrame, endFrame, fileString, withMaterial=0):
    frameRange = range(startFrame, endFrame + 1)
    sequenceRange = range(endFrame - startFrame + 1)
    # View Progress
    explain = '''Export GPU Sequence'''
    maxValue = endFrame - startFrame + 1
    progressBar = bscObjects.ProgressWindow(explain, maxValue)
    for seq in sequenceRange:
        # In Progress
        progressBar.update()
        currentFrame = frameRange[seq]
        subGpu = ('_' + str(seq + 1).zfill(4)).join(os.path.splitext(fileString))
        gpuExport(objectString, subGpu, currentFrame, currentFrame, withMaterial)


#
def gpuImport(fileString, transformName):
    cmds.loadPlugin('gpuCache', quiet=1)
    if os.path.isfile(fileString):
        shapeName = transformName + 'Shape'
        cmds.createNode('transform', name=transformName)
        cmds.createNode('gpuCache', name=shapeName, parent=transformName)
        cmds.setAttr(shapeName + '.cacheFileName', fileString, type='string')


#
def abcConnect(cache, objectString):
    cmds.loadPlugin('AbcImport', quiet=1)
    cmds.AbcImport(
        cache,
        connect=objectString)


#
def animExport(fileString, objectString=none, mode=0):
    cmds.loadPlugin('animImportExport', quiet=1)
    bscMethods.OsFile.createDirectory(fileString)
    if objectString:
        cmds.select(objectString)
    options = \
        "precision=8;" \
        "intValue=17;" \
        "nodeNames=1;" \
        "verboseUnits=0;" \
        "whichRange=1;" \
        "range=0:10;" \
        "options=keys;" \
        "hierarchy=below;" \
        "controlPoints=0;" \
        "shapes=1;" \
        "helpPictures=0;" \
        "useChannelBox=0;" \
        "copyKeyCmd=-animation objects -option keys -hierarchy below -controlPoints 0 -shape 1"
    if mode == 1:
        "precision=8;" \
        "intValue=17;" \
        "nodeNames=1;" \
        "verboseUnits=0;" \
        "whichRange=1;" \
        "range=0:10;" \
        "options=keys;" \
        "hierarchy=none;" \
        "controlPoints=0;" \
        "shapes=1;" \
        "helpPictures=0;" \
        "useChannelBox=0;" \
        "copyKeyCmd=-animation objects -option keys -hierarchy none -controlPoints 0 -shape 1 "
    cmds.file(
        fileString,
        force=1,
        options=options,
        type="animExport",
        pr=1,
        es=1)


#
def animImport(fileString, objectString=none, namespace=':'):
    cmds.loadPlugin('animImportExport', quiet=1)
    if objectString:
        cmds.select(objectString)
    animFile = fileString + '.anim'
    if os.path.isfile(animFile):
        command = '''file -import -type "animImport"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace "%s" -options ";targetTime=4;copies=1;option=replace;pictures=0;connect=0;"  -pr "%s";''' \
                  % (namespace, animFile)
        mel.eval(command)


#
def exportArnoldAss(assFile, camera, startFrame, endFrame):
    cmds.arnoldExportAss(
        f=assFile,
        cam=camera,
        startFrame=startFrame,
        endFrame=endFrame
    )


#
def exportSubArnoldAss(subAssFile, camera, frame):
    cmds.currentTime(frame)
    #
    cmds.arnoldExportAss(
        f=subAssFile,
        cam=camera
    )


#
def assExport(assFile, camera, startFrame, endFrame):
    # Use Temp Folder
    temporaryFile = bscMethods.OsFile.temporaryName(assFile)
    # Export Ass
    exportArnoldAss(temporaryFile, camera, startFrame, endFrame)
    # Get Temp ASS File
    tempSubAssFiles = [(os.path.splitext(temporaryFile)[0] + str(i).zfill(4) + os.path.splitext(temporaryFile)[1]).replace('\\', '/') for i in range(startFrame, endFrame + 1)]
    bscMethods.OsFile.createDirectory(assFile)
    # View Progress
    explain = '''Upload ASS to Render Pool'''
    maxValue = len(tempSubAssFiles)
    progressBar = bscObjects.ProgressWindow(explain, maxValue)
    # Move to Server
    for seq, tempSubAssFile in enumerate(tempSubAssFiles):
        # In Progress
        progressBar.update()
        if os.path.isfile(tempSubAssFile):
            subAssFile = os.path.dirname(assFile) + '/' + os.path.basename(tempSubAssFile)
            bscMethods.OsFile.copyTo(tempSubAssFile, subAssFile)


#
def loadPlugin(plugin):
    cmds.loadPlugin(plugin, quiet=1)