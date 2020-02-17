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


# Get Maya File Type
def getMayaFileType(fileString_):
    mayaFileType = 'mayaAscii'
    fieType = os.path.splitext(fileString_)[-1]
    if fieType == '.ma':
        mayaFileType = 'mayaAscii'
    elif fieType == '.mb':
        mayaFileType = 'mayaBinary'
    elif fieType == '.abc':
        mayaFileType = 'Alembic'
    return mayaFileType


# Reference Maya File
def setMaFileReference(fileString_, namespace=':'):
    cmds.file(
        fileString_,
        ignoreVersion=1,
        reference=1,
        mergeNamespacesOnClash=0,
        namespace=namespace,
        options='v=0;p=17;f=0',
        type=getMayaFileType(fileString_)
    )


# Reference Cache File
def setCacheFileReference(fileString_, nameSpace=':'):
    cmds.file(
        fileString_,
        reference=1,
        mergeNamespacesOnClash=1,
        namespace=nameSpace
    )


# Open Maya File
def fileOpen(fileString_):
    cmds.file(
        fileString_,
        open=1,
        options='v=0',
        force=1,
        type=getMayaFileType(fileString_)
    )


# Save Maya File
def saveMayaFile(fileString_):
    temporaryFile = bscMethods.OsFile.temporaryName(fileString_)
    cmds.file(rename=temporaryFile)
    cmds.file(save=1, type=getMayaFileType(fileString_))
    bscMethods.OsFile.createDirectory(fileString_)
    bscMethods.OsFile.copyTo(temporaryFile, fileString_)


#
def saveToMayaFile(fileString_):
    cmds.file(rename=fileString_)
    cmds.file(save=1, type=getMayaFileType(fileString_))
    bscMethods.OsFile.createDirectory(fileString_)


# Open Maya File as Back
def openMayaFileAsBack(fileString_, backFile, timeTag=none):
    if not timeTag:
        timeTag = bscMethods.OsTimetag.active()
    if os.path.isfile(fileString_):
        bscMethods.OsFile.createDirectory(backFile)
        fileJoinUpdate = bscMethods.OsFile.toJoinTimetag(backFile, timeTag)
        # Main
        shutil.copyfile(fileString_, fileJoinUpdate)
        fileOpen(fileJoinUpdate)


#
def openMayaFileToLocal(fileString_, localFile, timeTag=none):
    if not timeTag:
        timeTag = bscMethods.OsTimetag.active()
    #
    if os.path.isfile(fileString_):
        bscMethods.OsFile.createDirectory(localFile)
        localFileJoinUpdateTag = bscMethods.OsFile.toJoinTimetag(localFile, timeTag)
        # Main
        shutil.copyfile(fileString_, localFileJoinUpdateTag)
        fileOpen(localFileJoinUpdateTag)


#
def openFileToTemp(fileString_):
    temporaryFile = bscMethods.OsFile.temporaryName(fileString_)
    if os.path.isfile(fileString_):
        bscMethods.OsFile.createDirectory(temporaryFile)
        # Main
        shutil.copyfile(fileString_, temporaryFile)
        fileOpen(temporaryFile)


#
def openMayaFileWithoutReference(fileString_):
    cmds.fileString_(
        file,
        open=1,
        options='v=0',
        force=1,
        loadReferenceDepth = 'none',
        type=getMayaFileType(fileString_))


#
def updateMayaFile(fileString_):
    origFile = cmds.file(query=1, sceneName=1)
    #
    saveMayaFile(fileString_)
    cmds.file(rename=origFile)


#
def saveTempFile():
    origFile = cmds.file(query=1, sceneName=1)
    if not origFile:
        origFile = 'D:/Projects/temp.mb'
        bscMethods.OsFile.createDirectory(origFile)
        saveMayaFile(origFile)
    temporaryFile = '_temp'.join(os.path.splitext(origFile))
    cmds.file(rename=temporaryFile)
    saveMayaFile(temporaryFile)
    cmds.file(rename=origFile)


# Save Maya File to Local
def saveMayaFileToLocal(fileString_, timeTag=none):
    if not timeTag:
        timeTag = bscMethods.OsTimetag.active()
    #
    bscMethods.OsFile.createDirectory(fileString_)
    fileJoinUpdate = bscMethods.OsFile.toJoinTimetag(fileString_, timeTag)
    #
    maUtils.setCleanUnknownNodes()
    # Main
    cmds.file(rename=fileJoinUpdate)
    cmds.file(
        save=1,
        options='v=0;',
        force=1,
        type=getMayaFileType(fileString_)
    )


# New Maya Scene
def new():
    cmds.file(new=1, force=1)


# Export Maya File
def fileExport(objects, fileString_, history=0):
    temporaryFile = bscMethods.OsFile.temporaryName(fileString_)
    cmds.select(objects)
    cmds.file(
        temporaryFile,
        force=1,
        options='v=0',
        type=getMayaFileType(fileString_),
        preserveReferences=0,
        exportSelected=1,
        constructionHistory=history
    )
    cmds.select(clear=1)
    bscMethods.OsFile.copyTo(temporaryFile, fileString_)


# Export Maya File
def exportMayaFileWithSet(fileString_, cfxGroup, setObjects, history=1):
    cmds.select(clear=1)
    cmds.select(cfxGroup)
    if isinstance(setObjects, str):
        if cmds.objExists(setObjects):
            cmds.select(setObjects, add=1, noExpand=1)
    elif isinstance(setObjects, list):
        for i in setObjects:
            if cmds.objExists(i):
                cmds.select(i, add=1, noExpand=1)
    #
    temporaryFile = bscMethods.OsFile.temporaryName(fileString_)
    cmds.file(
        temporaryFile,
        force=1,
        options='v=0',
        type=getMayaFileType(fileString_),
        preserveReferences=0,
        exportSelected=1,
        constructionHistory=history)
    cmds.select(clear=1)
    bscMethods.OsFile.copyTo(temporaryFile, fileString_)


# Import Maya File
def setFileImport(fileString_, namespace=':'):
    cmds.file(
        fileString_,
        i=1,
        options='v=0;',
        type=getMayaFileType(fileString_),
        ra=1,
        mergeNamespacesOnClash=1,
        namespace=namespace,
        preserveReferences=1
    )


#
def setAlembicCacheImport(fileString_, namespace=':'):
    cmds.loadPlugin('AbcImport', quiet=1)

    cmds.file(
        fileString_,
        i=1,
        options='v=0;',
        type='Alembic',
        ra=1,
        mergeNamespacesOnClash=1,
        namespace=namespace,
        preserveReferences=1
    )
    #
    alembicNodeName = namespace + ':' + bscMethods.OsFile.name(fileString_) + '_AlembicNode'
    if maUtils._isNodeExist(alembicNodeName):
        pass
    else:
        if not maUtils._isNodeExist(alembicNodeName):
            cmds.createNode(appCfg.MaNodeType_Alembic, name=alembicNodeName)
            cmds.setAttr(alembicNodeName + '.abc_File', fileString_, type='string')


#
def setFileImportWithGroup(fileString_, groupName, namespace=':'):
    cmds.file(
        fileString_,
        i=1,
        options='v=0;',
        type=getMayaFileType(fileString_),
        ra=1,
        mergeNamespacesOnClash=1,
        namespace=namespace,
        preserveReferences=1,
        groupReference=True,
        groupName=groupName
    )


# Export Maya Material File
def exportMayaMaterialFile(fileString_, shadingEngines, aiAovs):
    cmds.select(clear=1)
    if shadingEngines:
        cmds.select(shadingEngines, noExpand=1)
        if aiAovs:
            cmds.select(aiAovs, add=1)
        cmds.file(rename=fileString_)
        cmds.file(
            force=1,
            options='v=0',
            type=getMayaFileType(fileString_),
            preserveReferences=0,
            exportSelected=1)
        cmds.select(clear=1)


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
def fbxExport(objectStrings, fileString_):
    objectStrings = maUtils.string2list(objectStrings)
    maUtils.setNodeSelect(objectStrings)
    #
    temporaryFile = bscMethods.OsFile.temporaryName(fileString_)
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
    bscMethods.OsFile.copyTo(temporaryFile, fileString_)
    #
    maUtils.setSelClear()


#
def abcExport(objectString, fileString_, startFrame, endFrame, step, attrs=None):
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
            if maUtils._isNodeExist(objectString):
                lis = [objectString]
        elif isinstance(objectString, tuple) or isinstance(objectString, list):
            for i in objectString:
                if maUtils._isNodeExist(i):
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
    temporaryFile = bscMethods.OsFile.temporaryName(fileString_)
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
        bscMethods.OsFile.copyTo(temporaryFile, fileString_)


#
def gpuExport(objectString, fileString_, startFrame, endFrame, withMaterial=0):
    cmds.loadPlugin('gpuCache', quiet=1)
    if cmds.objExists(objectString):
        temporaryFile = bscMethods.OsFile.temporaryName(fileString_)
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
        bscMethods.OsFile.copyTo(temporaryFile, fileString_)


#
def gpuSeqExport(objectString, startFrame, endFrame, fileString_, withMaterial=0):
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
        subGpu = ('_' + str(seq + 1).zfill(4)).join(os.path.splitext(fileString_))
        gpuExport(objectString, subGpu, currentFrame, currentFrame, withMaterial)


#
def gpuImport(fileString_, transformName):
    cmds.loadPlugin('gpuCache', quiet=1)
    if os.path.isfile(fileString_):
        shapeName = transformName + 'Shape'
        cmds.createNode('transform', name=transformName)
        cmds.createNode('gpuCache', name=shapeName, parent=transformName)
        cmds.setAttr(shapeName + '.cacheFileName', fileString_, type='string')


#
def abcConnect(cache, objectString):
    cmds.loadPlugin('AbcImport', quiet=1)
    cmds.AbcImport(
        cache,
        connect=objectString)


#
def animExport(fileString_, objectString=none, mode=0):
    cmds.loadPlugin('animImportExport', quiet=1)
    bscMethods.OsFile.createDirectory(fileString_)
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
        fileString_,
        force=1,
        options=options,
        type="animExport",
        pr=1,
        es=1)


#
def animImport(fileString_, objectString=none, namespace=':'):
    cmds.loadPlugin('animImportExport', quiet=1)
    if objectString:
        cmds.select(objectString)
    animFile = fileString_ + '.anim'
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