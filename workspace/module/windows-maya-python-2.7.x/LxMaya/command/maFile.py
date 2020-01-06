# coding=utf-8
import os, time, shutil, json, platform, locale
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.mel as mel
#
from LxCore import lxBasic
from LxUi.qt import qtCommands
#
from LxCore.config import appCfg
#
from LxCore.preset import appVariant
#
from LxMaya.command import maUtils
#
temporaryDirectory = appVariant.localTemporaryDirectory()
astModelTextureFolder = appVariant.astModelTextureFolder
#
tempFolderLabel = 'temp'
gzExtLabel = '.gz'
#
none = ''


#
def setHideDirectory(directory):
    if os.path.isdir(directory):
        if 'Windows' in platform.system():
            command = 'attrib +h "' + directory + '"'
            command = command.encode(locale.getdefaultlocale()[1])
            os.popen(command).close()


#
def setRemoveDirectory(directory):
    if os.path.isdir(directory):
        for root, dirs, files in os.walk(directory, topdown=0):
            for seq, name in enumerate(files):
                osFile = os.path.join(root, name).replace('\\', '/')
                os.remove(osFile)
            os.removedirs(root)


#
def setCopyFile(sourceFile, targetFile):
    if os.path.isfile(sourceFile):
        lxBasic.setOsFileDirectoryCreate(targetFile)
        shutil.copy2(sourceFile, targetFile)


#
def setMoveFile(sourceFile, targetFile):
    if os.path.isfile(sourceFile):
        lxBasic.setOsFileDirectoryCreate(targetFile)
        shutil.move(sourceFile, targetFile)


#
def getFileSize(osFile):
    value = 0
    if os.path.isfile(osFile):
        fileSize = os.path.getsize(osFile)
        fileSize /= float(1024 * 1024)
        value = round(fileSize, 2)
    return value


# Get Upload Temp File
def getTemporaryOsFile(osFile):
    fileName = os.path.basename(osFile)
    temporaryFile = os.path.join(temporaryDirectory, fileName).replace('\\', '/')
    lxBasic.setOsFileDirectoryCreate(temporaryFile)
    return temporaryFile


#
def setTransferFile(osFile):
    temporaryFile = getTemporaryOsFile(osFile)
    cmds.file(rename=temporaryFile)
    cmds.file(save=1, type=getMayaFileType(osFile))
    setMoveFile(temporaryFile, osFile)


# Get Maya File Type
def getMayaFileType(osFile):
    mayaFileType = 'mayaAscii'
    fieType = os.path.splitext(osFile)[-1]
    if fieType == '.ma':
        mayaFileType = 'mayaAscii'
    elif fieType == '.mb':
        mayaFileType = 'mayaBinary'
    elif fieType == '.abc':
        mayaFileType = 'Alembic'
    return mayaFileType


# Reference Maya File
def setMaFileReference(osFile, namespace=':'):
    cmds.file(
        osFile,
        ignoreVersion=1,
        reference=1,
        mergeNamespacesOnClash=0,
        namespace=namespace,
        options='v=0;p=17;f=0',
        type=getMayaFileType(osFile)
    )


# Reference Cache File
def setCacheFileReference(osFile, nameSpace=':'):
    cmds.file(
        osFile,
        reference=1,
        mergeNamespacesOnClash=1,
        namespace=nameSpace
    )


# Open Maya File
def fileOpen(osFile):
    cmds.file(
        osFile,
        open=1,
        options='v=0',
        force=1,
        type=getMayaFileType(osFile)
    )


# Save Maya File
def saveMayaFile(osFile):
    temporaryFile = getTemporaryOsFile(osFile)
    cmds.file(rename=temporaryFile)
    cmds.file(save=1, type=getMayaFileType(osFile))
    lxBasic.setOsFileDirectoryCreate(osFile)
    setMoveFile(temporaryFile, osFile)


#
def saveToMayaFile(osFile):
    cmds.file(rename=osFile)
    cmds.file(save=1, type=getMayaFileType(osFile))
    lxBasic.setOsFileDirectoryCreate(osFile)


# Open Maya File as Back
def openMayaFileAsBack(osFile, backFile, timeTag=none):
    if not timeTag:
        timeTag = lxBasic.getOsActiveTimeTag()
    if os.path.isfile(osFile):
        lxBasic.setOsFileDirectoryCreate(backFile)
        fileJoinUpdate = lxBasic.getOsFileJoinTimeTag(backFile, timeTag)
        # Main
        shutil.copyfile(osFile, fileJoinUpdate)
        fileOpen(fileJoinUpdate)


#
def openMayaFileToLocal(osFile, localFile, timeTag=none):
    if not timeTag:
        timeTag = lxBasic.getOsActiveTimeTag()
    #
    if os.path.isfile(osFile):
        lxBasic.setOsFileDirectoryCreate(localFile)
        localFileJoinUpdateTag = lxBasic.getOsFileJoinTimeTag(localFile, timeTag)
        # Main
        shutil.copyfile(osFile, localFileJoinUpdateTag)
        fileOpen(localFileJoinUpdateTag)


#
def openFileToTemp(osFile):
    temporaryFile = getTemporaryOsFile(osFile)
    if os.path.isfile(osFile):
        lxBasic.setOsFileDirectoryCreate(temporaryFile)
        # Main
        shutil.copyfile(osFile, temporaryFile)
        fileOpen(temporaryFile)


#
def openMayaFileWithoutReference(osFile):
    cmds.osFile(
        file,
        open=1,
        options='v=0',
        force=1,
        loadReferenceDepth = 'none',
        type=getMayaFileType(osFile))


#
def updateMayaFile(osFile):
    origFile = cmds.file(query=1, sceneName=1)
    #
    saveMayaFile(osFile)
    cmds.file(rename=origFile)


#
def saveTempFile():
    origFile = cmds.file(query=1, sceneName=1)
    if not origFile:
        origFile = 'D:/Projects/temp.mb'
        lxBasic.setOsFileDirectoryCreate(origFile)
        saveMayaFile(origFile)
    temporaryFile = '_temp'.join(os.path.splitext(origFile))
    cmds.file(rename=temporaryFile)
    saveMayaFile(temporaryFile)
    cmds.file(rename=origFile)


# Save Maya File to Local
def saveMayaFileToLocal(osFile, timeTag=none):
    if not timeTag:
        timeTag = lxBasic.getOsActiveTimeTag()
    #
    lxBasic.setOsFileDirectoryCreate(osFile)
    fileJoinUpdate = lxBasic.getOsFileJoinTimeTag(osFile, timeTag)
    #
    maUtils.setCleanUnknownNodes()
    # Main
    cmds.file(rename=fileJoinUpdate)
    cmds.file(
        save=1,
        options='v=0;',
        force=1,
        type=getMayaFileType(osFile)
    )


# Back up Maya File
def backupMayaFile(osFile, backFile, timeTag=none):
    if os.path.isfile(osFile):
        if not timeTag:
            timeTag = lxBasic.getOsActiveTimeTag()
        #
        backFileJoinUpdateTag = lxBasic.getOsFileJoinTimeTag(backFile, timeTag)
        #
        setCopyFile(osFile, backFileJoinUpdateTag)


# Back up File
def backupFile(osFile, backFile, timeTag=none):
    if timeTag:
        if os.path.isfile(osFile):
            #
            backFileJoinUpdateTag = lxBasic.getOsFileJoinTimeTag(backFile, timeTag)
            #
            setCopyFile(osFile, backFileJoinUpdateTag)


# Backup Log File
def backupRecordFile(osFile, timeTag=none):
    if timeTag:
        if os.path.isfile(osFile):
            fileName = os.path.basename(osFile)
            recordDirectory = os.path.dirname(osFile) + '/record'
            backRecordFile = recordDirectory + '/' + fileName
            #
            backFileJoinUpdateTag = lxBasic.getOsFileJoinTimeTag(backRecordFile, timeTag)
            #
            setCopyFile(osFile, backFileJoinUpdateTag)


# New Maya Scene
def new():
    cmds.file(new=1, force=1)


# Export Maya File
def fileExport(objects, osFile, history=0):
    temporaryFile = getTemporaryOsFile(osFile)
    cmds.select(objects)
    cmds.file(
        temporaryFile,
        force=1,
        options='v=0',
        type=getMayaFileType(osFile),
        preserveReferences=0,
        exportSelected=1,
        constructionHistory=history
    )
    cmds.select(clear=1)
    setMoveFile(temporaryFile, osFile)


# Export Maya File
def exportMayaFileWithSet(osFile, cfxGroup, setObjects, history=1):
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
    temporaryFile = getTemporaryOsFile(osFile)
    cmds.file(
        temporaryFile,
        force=1,
        options='v=0',
        type=getMayaFileType(osFile),
        preserveReferences=0,
        exportSelected=1,
        constructionHistory=history)
    cmds.select(clear=1)
    setMoveFile(temporaryFile, osFile)


# Import Maya File
def setFileImport(osFile, namespace=':'):
    cmds.file(
        osFile,
        i=1,
        options='v=0;',
        type=getMayaFileType(osFile),
        ra=1,
        mergeNamespacesOnClash=1,
        namespace=namespace,
        preserveReferences=1
    )


#
def setAlembicCacheImport(osFile, namespace=':'):
    cmds.file(
        osFile,
        i=1,
        options='v=0;',
        type='Alembic',
        ra=1,
        mergeNamespacesOnClash=1,
        namespace=namespace,
        preserveReferences=1
    )
    #
    alembicNodeName = namespace + ':' + lxBasic.getOsFileName(osFile) + '_AlembicNode'
    if maUtils.isAppExist(alembicNodeName):
        pass
    else:
        if not maUtils.isAppExist(alembicNodeName):
            cmds.createNode(appCfg.MaNodeType_Alembic, name=alembicNodeName)
            cmds.setAttr(alembicNodeName + '.abc_File', osFile, type='string')


#
def setFileImportWithGroup(osFile, groupName, namespace=':'):
    cmds.file(
        osFile,
        i=1,
        options='v=0;',
        type=getMayaFileType(osFile),
        ra=1,
        mergeNamespacesOnClash=1,
        namespace=namespace,
        preserveReferences=1,
        groupReference=True,
        groupName=groupName
    )


# Export Maya Material File
def exportMayaMaterialFile(osFile, shadingEngines, aiAovs):
    cmds.select(clear=1)
    if shadingEngines:
        cmds.select(shadingEngines, noExpand=1)
        if aiAovs:
            cmds.select(aiAovs, add=1)
        cmds.file(rename=osFile)
        cmds.file(
            force=1,
            options='v=0',
            type=getMayaFileType(osFile),
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
    temporaryFile = getTemporaryOsFile(osImageFile)
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
    setMoveFile(tempPrvFile, osImageFile)
    cmds.setAttr('lambert1.color', .5, .5, .5)


# Load Maya File
def loadMayaFile(osFile, localFile, timeTag=none):
    if not timeTag:
        timeTag = lxBasic.getOsActiveTimeTag()
    #
    cmds.file(osFile, open=1, options='v=0', force=1)
    cmds.file(rename=localFile.replace('.', '_%s.' % time.strftime('%Y_%m%d_%H%M', time.localtime(time.time()))))


# Write Json
def writeOsJson(data, osFile, indent=0):
    if data:
        lxBasic.setOsFileDirectoryCreate(osFile)
        with open(osFile, 'w') as f:
            if indent:
                json.dump(data, f, ensure_ascii=True, indent=indent)
            elif not indent:
                json.dump(data, f, ensure_ascii=True)


#
def readOsJson(osFile):
    if os.path.isfile(osFile):
        with open(osFile) as f:
            data = json.load(f)
            return data


#
def writeOsData(data, osFile):
    if data:
        lxBasic.setOsFileDirectoryCreate(osFile)
        with open(osFile, 'wb') as f:
            f.write(data)
            f.close()


#
def readOsData(osFile):
    if os.path.isfile(osFile):
        with open(osFile, 'r') as f:
            data = f.readlines()
            f.close()
            return data


#
def fbxExport(objectStrings, osFile):
    objectStrings = maUtils._toStringList(objectStrings)
    maUtils.setNodeSelect(objectStrings)
    #
    temporaryFile = lxBasic.getOsTemporaryFile(osFile)
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
    lxBasic.setOsFileCopy(temporaryFile, osFile)
    #
    maUtils.setSelClear()


#
def abcExport(objectString, osFile, startFrame, endFrame, step, attrs=None):
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
            if maUtils.isAppExist(objectString):
                lis = [objectString]
        elif isinstance(objectString, tuple) or isinstance(objectString, list):
            for i in objectString:
                if maUtils.isAppExist(i):
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
    temporaryFile = getTemporaryOsFile(osFile)
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
        setMoveFile(temporaryFile, osFile)


#
def gpuExport(objectString, osFile, startFrame, endFrame, withMaterial=0):
    cmds.loadPlugin('gpuCache', quiet=1)
    if cmds.objExists(objectString):
        temporaryFile = getTemporaryOsFile(osFile)
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
        setMoveFile(temporaryFile, osFile)


#
def gpuSeqExport(objectString, startFrame, endFrame, osFile, withMaterial=0):
    frameRange = range(startFrame, endFrame + 1)
    sequenceRange = range(endFrame - startFrame + 1)
    # View Progress
    explain = '''Export GPU Sequence'''
    maxValue = endFrame - startFrame + 1
    progressBar = qtCommands.setProgressWindowShow(explain, maxValue)
    for seq in sequenceRange:
        # In Progress
        progressBar.updateProgress()
        currentFrame = frameRange[seq]
        subGpu = ('_' + str(seq + 1).zfill(4)).join(os.path.splitext(osFile))
        gpuExport(objectString, subGpu, currentFrame, currentFrame, withMaterial)


#
def setAlembicImport(cache):
    cmds.loadPlugin('AbcImport', quiet=1)
    cmds.AbcImport(cache)


#
def gpuImport(osFile, transformName):
    cmds.loadPlugin('gpuCache', quiet=1)
    if os.path.isfile(osFile):
        shapeName = transformName + 'Shape'
        cmds.createNode('transform', name=transformName)
        cmds.createNode('gpuCache', name=shapeName, parent=transformName)
        cmds.setAttr(shapeName + '.cacheFileName', osFile, type='string')


#
def abcConnect(cache, objectString):
    cmds.loadPlugin('AbcImport', quiet=1)
    cmds.AbcImport(
        cache,
        connect=objectString)


#
def animExport(osFile, objectString=none, mode=0):
    cmds.loadPlugin('animImportExport', quiet=1)
    lxBasic.setOsFileDirectoryCreate(osFile)
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
        osFile,
        force=1,
        options=options,
        type="animExport",
        pr=1,
        es=1)


#
def animImport(osFile, objectString=none, namespace=':'):
    cmds.loadPlugin('animImportExport', quiet=1)
    if objectString:
        cmds.select(objectString)
    animFile = osFile + '.anim'
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
    temporaryFile = getTemporaryOsFile(assFile)
    # Export Ass
    exportArnoldAss(temporaryFile, camera, startFrame, endFrame)
    # Get Temp ASS File
    tempSubAssFiles = [(os.path.splitext(temporaryFile)[0] + str(i).zfill(4) + os.path.splitext(temporaryFile)[1]).replace('\\', '/') for i in range(startFrame, endFrame + 1)]
    lxBasic.setOsFileDirectoryCreate(assFile)
    # View Progress
    explain = '''Upload ASS to Render Pool'''
    maxValue = len(tempSubAssFiles)
    progressBar = qtCommands.setProgressWindowShow(explain, maxValue)
    # Move to Server
    for seq, tempSubAssFile in enumerate(tempSubAssFiles):
        # In Progress
        progressBar.updateProgress()
        if os.path.isfile(tempSubAssFile):
            subAssFile = os.path.dirname(assFile) + '/' + os.path.basename(tempSubAssFile)
            setMoveFile(tempSubAssFile, subAssFile)


#
def loadPlugin(plugin):
    cmds.loadPlugin(plugin, quiet=1)