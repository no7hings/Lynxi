# encoding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.mel as mel
#
from LxCore import lxBasic, lxConfigure, lxProgress, lxTip
#
from LxCore.config import appCfg
#
from LxCore.preset import appVariant
#
from LxMaya.command import maUtils
#
mayaVersion = maUtils.getMayaVersion()
#
MaNode_DefaultRenderGlobals = 'defaultRenderGlobals'
MaNode_DefaultArnoldDriver = 'defaultArnoldDriver'
MaNode_DefaultArnoldRenderOptions = 'defaultArnoldRenderOptions'
#
MaArnold_DefaultRenderPass = 'beauty'
#
MaNodeAttrRenderOptionDic = {
    'renderer': 'defaultRenderGlobals.currentRenderer',
    'imagePrefix': 'defaultRenderGlobals.imageFilePrefix',
    'startFrame': 'defaultRenderGlobals.startFrame',
    'endFrame': 'defaultRenderGlobals.endFrame',
    'animation': 'defaultRenderGlobals.animation',
    'imageFormat': 'defaultRenderGlobals.imfPluginKey',
    'periodInExt': 'defaultRenderGlobals.periodInExt',
    'putFrameBeforeExt': 'defaultRenderGlobals.putFrameBeforeExt',
    'extensionPadding': 'defaultRenderGlobals.extensionPadding',
    'renderVersion': 'defaultRenderGlobals.renderVersion',
    #
    'imageWidth': 'defaultResolution.width',
    'imageHeight': 'defaultResolution.height',
    #
    'preMel': 'defaultRenderGlobals.preMel'
}
#
MaArnoldRenderOptionDic = {
    'aovMode': 'defaultArnoldRenderOptions.aovMode',
    'aovs': 'defaultArnoldRenderOptions.aovs',
    'mergeAov': 'defaultArnoldDriver.mergeAOVs'
}
#
MaArnoldLightAovLis = [
    'RGBA',
    'direct',
    'indirect',
    'emission',
    'diffuse',
    'specular',
    'transmission',
    'sss',
    'volume',
    'diffuse_direct',
    'diffuse_indirect',
    'diffuse_albedo',
    'specular_direct',
    'specular_indirect',
    'specular_albedo',
    'coat',
    'coat_direct',
    'coat_indirect',
    'coat_albedo',
    'transmission_direct',
    'transmission_indirect',
    'transmission_albedo',
    'sss_direct',
    'sss_indirect',
    'sss_albedo',
    'volume_direct',
    'volume_indirect',
    'shadow_matte'
]
#
MaRendererDic = {
    lxConfigure.LynxiArnoldRendererValue: 'arnold',
    lxConfigure.LynxiRedshiftRendererValue: 'redshift',
    lxConfigure.LynxiMayaSoftwareRendererValue: 'mayaSoftware',
    lxConfigure.LynxiMayaHardwareRendererValue: 'mayaHardware'
}
#
MaDefaultWorkspaceRuleDic = {
    'scene': 'scenes',
    'templates': 'assets',
    'images': 'images',
    'sourceImages': 'sourceimages',
    'renderData': 'renderData',
    'clips': 'clips',
    'sound': 'sound',
    'scripts': 'scripts',
    'diskCache': 'data',
    'movie': 'movies',
    'translatorData': 'data',
    'timeEditor': 'Time Editor',
    'autoSave': 'autosave',
    'sceneAssembly': 'sceneAssembly',
    'offlineEdit': 'scenes/edits',
    '3dPaintTextures': 'sourceimages/3dPaintTextures',
    'depth': 'renderData/depth',
    'iprImages': 'renderData/iprImages',
    'shaders': 'renderData/shaders',
    'furFiles': 'renderData/fur/furFiles',
    'furImages': 'renderData/fur/furImages',
    'furEqualMap': 'renderData/fur/furEqualMap',
    'furAttrMap': 'renderData/fur/furAttrMap',
    'furShadowMap': 'renderData/fur/furShadowMap',
    'particles': 'cache/particles',
    'fluidCache': 'cache/nCache/fluid',
    'fileCache': 'cache/nCache',
    'bifrostCache': 'cache/bifrost',
    'teClipExports': 'Time Editor/Clip Exports',
    'mayaAscii': 'scenes',
    'mayaBinary': 'scenes',
    'mel': 'scripts',
    'OBJ': 'data',
    'audio': 'sound',
    'move': 'data',
    'eps': 'data',
    'illustrator': 'data',
    'IGES_ATF': 'data',
    'JT_ATF': 'data',
    'SAT_ATF': 'data',
    'STEP_ATF': 'data',
    'STL_ATF': 'data',
    'WIRE_ATF': 'data',
    'INVENTOR_ATF': 'data',
    'CATIAV4_ATF': 'data',
    'CATIAV5_ATF': 'data',
    'NX_ATF': 'data',
    'PROE_ATF': 'data',
    'IGES_ATF Export': 'data',
    'JT_ATF Export': 'data',
    'SAT_ATF Export': 'data',
    'STEP_ATF Export': 'data',
    'STL_ATF Export': 'data',
    'WIRE_ATF Export': 'data',
    'INVENTOR_ATF Export': 'data',
    'CATIAV5_ATF Export': 'data',
    'NX_ATF Export': 'data',
    'OBJexport': 'data',
    'BIF': 'data',
    'FBX': 'data',
    'FBX export': 'data',
    'DAE_FBX': 'data',
    'DAE_FBX export': 'data',
    'ASS Export': 'data',
    'ASS': 'data',
    'Alembic': 'data',
    'animImport': 'data',
    'animExport': 'data'
}
#
MaRender_DefaultImageFilePrefix = '<RenderLayer>/<RenderPass>/<RenderPass>'
#
MaRender_DefaultRenderLayer = 'defaultRenderLayer'
#
none = ''


#
def isArnoldMergeAov():
    return cmds.getAttr(MaArnoldRenderOptionDic['mergeAov'])


#
def getArnoldAovMode():
    return cmds.getAttr(MaArnoldRenderOptionDic['aovMode'])


#
def isValidArnoldAovNode(aovNode):
    boolean = False
    if not maUtils.isReferenceNode(aovNode):
        if mayaVersion < 2017:
            boolean = True
        #
        hasRenderSetup = mel.eval('mayaHasRenderSetup()')
        if hasRenderSetup == 0:
            boolean = True
    return boolean


#
def getArnoldAovLis(useMode=0):
    lis = []
    aovAttr = MaArnoldRenderOptionDic['aovs']
    inputConns = cmds.listConnections(aovAttr, source=1, destination=0, plugs=1, connections=1) or []
    inputConns = dict(zip(inputConns[1::2], inputConns[::2]))
    nodeLis = [fromAttr.split('.')[0] for fromAttr, toAttr in inputConns.items() if isValidArnoldAovNode(fromAttr.split('.')[0])]
    if nodeLis:
        for aovNode in nodeLis:
            enableAttr = aovNode + '.' + 'enabled'
            if cmds.getAttr(enableAttr):
                if useMode == 0:
                    nameAttr = aovNode + '.' + 'name'
                    name = cmds.getAttr(nameAttr)
                    if not name in lis:
                        lis.append(name)
                #
                elif useMode == 1:
                    lis.append(aovNode)
    return lis


#
def getArnoldLightAovLis():
    lis = []
    #
    attrName = 'aiAov'
    #
    lightTypes = maUtils.getNodeTypeLisByFilter('light')
    if lightTypes:
        for lightType in lightTypes:
            lights = maUtils.getNodeTransforms(lightType)
            if lights:
                for lightPath in lights:
                    data = maUtils.getAttrDatum(lightPath, attrName)
                    if data:
                        lis.append(data)
    return lis


#
def getArnoldAovName(aovNode):
    attrName = 'name'
    data = maUtils.getAttrDatum(aovNode, attrName)
    return data


#
def isArnoldAovUseLightGroup(aovNode):
    boolean = False
    attrName = 'globalAov'
    aovName = getArnoldAovName(aovNode)
    if aovName in MaArnoldLightAovLis:
        data = maUtils.getAttrDatum(aovNode, attrName)
        if data is not None:
            boolean = data
    return boolean


#
def isArnoldAovUseAllLightGroup(aovNode):
    boolean = False
    attrName = 'lightGroups'
    aovName = getArnoldAovName(aovNode)
    if aovName in MaArnoldLightAovLis:
        data = maUtils.getAttrDatum(aovNode, attrName)
        if data is not None:
            boolean = data
    return boolean


#
def getArnoldLightAovLis_(aovNode):
    string = none
    aovName = getArnoldAovName(aovNode)
    if aovName in MaArnoldLightAovLis:
        enableAttrName = 'globalAov'
        useAllAttrName = 'lightGroups'
        lightAovAttrName = 'lightGroupsList'
        if maUtils.getAttrDatum(aovNode, enableAttrName):
            if maUtils.getAttrDatum(aovNode, useAllAttrName):
                string = 'lgroups'
            else:
                string = maUtils.getAttrDatum(lightAovAttrName) or none
    return string


#
def getArnoldRenderableAovLis(useMode=0):
    lis = []
    #
    if getArnoldAovMode():
        if not isArnoldMergeAov():
            if useMode == 0:
                lis = [MaArnold_DefaultRenderPass]
                lis.extend(getArnoldAovLis(useMode))
            elif useMode == 1:
                lis = getArnoldAovLis(useMode)
    #
    return lis


#
def getCurrentRenderer():
    return cmds.getAttr(MaNodeAttrRenderOptionDic['renderer'])


# Get Render Size
def getRenderSize():
    width = int(cmds.getAttr(MaNodeAttrRenderOptionDic['imageWidth']))
    height = int(cmds.getAttr(MaNodeAttrRenderOptionDic['imageHeight']))
    return width, height


#
def isAnimationEnable():
    return cmds.getAttr(MaNodeAttrRenderOptionDic['animation'])


#
def isRenderLayerEnable():
    renderLayers = getRenderLayers()
    if renderLayers:
        boolean = True
    else:
        boolean = False
    return boolean


#
def isRenderSetupEnable():
    data = mel.eval('mayaHasRenderSetup()')
    if data:
        boolean = True
    else:
        boolean = False
    return boolean


# Set Out Format
def setAnimationFrameMode(boolean=True):
    cmds.setAttr('defaultRenderGlobals.animation', boolean)
    #
    cmds.setAttr('defaultRenderGlobals.putFrameBeforeExt', True)
    cmds.setAttr('defaultRenderGlobals.periodInExt', True)
    #
    cmds.setAttr('defaultRenderGlobals.outFormatControl', False)


#
def getImagePrefix():
    return (cmds.getAttr(MaNodeAttrRenderOptionDic['imagePrefix']) or '').replace('\\', '/')


#
def getImageFormat():
    return cmds.getAttr(MaNodeAttrRenderOptionDic['imageFormat'])


#
def setImagePath(osPath):
    cmds.setAttr(MaNodeAttrRenderOptionDic['imagePrefix'], osPath, type='string')


#
def getCurrentRenderFrame():
    return int(cmds.currentTime(query=1))


#
def getCurrentImageFile(sceneRoot, userFrame=False):
    sceneName = getSceneName()
    renderLayer = getCurrentRenderLayer()
    cameraName = getRenderCameraName(getRenderableCameraLis()[0])
    renderPass = MaArnold_DefaultRenderPass
    if userFrame:
        frame = getCurrentRenderFrame()
    else:
        frame = None
    return getImageFile(sceneRoot, sceneName, cameraName, renderLayer, renderPass, frame)


#
def getImageFile(sceneRoot, sceneName, cameraName, renderLayer, renderPass, frame=None):
    if renderLayer == 'defaultRenderLayer':
        renderLayer = 'masterLayer'
    #
    # noinspection PyUnusedLocal
    Scene = sceneName
    # noinspection PyUnusedLocal
    Camera = getRenderCameraName(cameraName)
    # noinspection PyUnusedLocal
    RenderLayer = renderLayer
    # noinspection PyUnusedLocal
    RenderPass = renderPass
    # noinspection PyUnusedLocal
    Version = getRenderVersion()
    # noinspection PyUnusedLocal
    Extension = ''
    # noinspection PyUnusedLocal
    RenderPassFileGroup = ''
    #
    imageAbsPath = getWorkspaceRule('images')
    #
    imagePrefix = getImagePrefix()
    # No RenderLayer Prefix
    if not '<RenderLayer>' in imagePrefix:
        imagePrefix = '<RenderLayer>' + '/' + imagePrefix
    #
    imageFormat = getImageFormat()
    if not imageFormat:
        imageFormat = 'jpg'
    #
    if imageFormat == 'jpeg':
        imageFormat = 'jpg'
    #
    var = str
    pathCmd = lxBasic._toVariantConvert('var', imagePrefix)
    exec pathCmd
    #
    periodInExt = cmds.getAttr(MaNodeAttrRenderOptionDic['periodInExt'])
    extensionPadding = cmds.getAttr(MaNodeAttrRenderOptionDic['extensionPadding'])
    putFrameBeforeExt = cmds.getAttr(MaNodeAttrRenderOptionDic['putFrameBeforeExt'])
    if frame:
        frameLabel = str(frame).zfill(extensionPadding)
    else:
        frameLabel = '#'*extensionPadding
    #
    imagePath = '/'.join([sceneRoot, imageAbsPath, var])
    if periodInExt == 0:
        frameLabel = frameLabel
    elif periodInExt == 1:
        frameLabel = '.' + frameLabel
    elif periodInExt == 2:
        frameLabel = '_' + frameLabel
    #
    if putFrameBeforeExt:
        string = imagePath + frameLabel + '.' + imageFormat
    else:
        string = imagePath + '.' + imageFormat + frameLabel
    return string


#
def getImageFileLis(sceneRoot, sceneNameOverride=None, cameraOverride=None, renderLayerOverride=None):
    lis = []
    sceneName = getSceneName()
    if sceneNameOverride is not None:
        sceneName = sceneNameOverride
    #
    renderableCameras = getRenderableCameraLis()
    renderableLayers = getRenderableRenderLayers()
    if cameraOverride:
        renderableCameras = [cameraOverride]
    if renderLayerOverride:
        renderableLayers = [renderLayerOverride]
    #
    if renderableCameras:
        for camera in renderableCameras:
            if renderableLayers:
                for renderLayer in renderableLayers:
                    setCurrentRenderLayer(renderLayer)
                    renderablePasses = getArnoldRenderableAovLis()
                    if renderablePasses:
                        for renderPass in renderablePasses:
                            imageFile = getImageFile(
                                sceneRoot,
                                sceneName,
                                getRenderCameraName(camera),
                                renderLayer,
                                renderPass
                            )
                            lis.append(imageFile)
                    else:
                        imageFile = getImageFile(
                            sceneRoot,
                            sceneName,
                            getRenderCameraName(camera),
                            renderLayer,
                            MaArnold_DefaultRenderPass
                        )
                        lis.append(imageFile)
                #
                setCurrentRenderLayer(MaRender_DefaultRenderLayer)
    return lis


#
def getSceneName():
    string = none
    data = cmds.file(query=1, expandName=1)
    if data:
        if not data.endswith('untitled'):
            osFileName = lxBasic.getOsFileName(data)
            string = osFileName
        else:
            string = 'untitled'
    return string


#
def getSceneFile():
    string = none
    data = cmds.file(query=1, expandName=1)
    if data:
        string = data
    return string


#
def getScenePath():
    string = none
    data = cmds.file(query=1, expandName=1)
    if data:
        string = lxBasic.getOsFileDirname(data)
    return string


#
def getRenderVersion():
    return cmds.getAttr(MaNodeAttrRenderOptionDic['renderVersion'])


#
def getCurrentRenderLayer():
    string = none
    data = cmds.editRenderLayerGlobals(query=1, currentRenderLayer=1)
    if data:
        if data == 'defaultRenderLayer':
            string = 'masterLayer'
        else:
            string = data
    return string


#
def getRenderLayers():
    lis = []
    data = cmds.listConnections('renderLayerManager.renderLayerId')
    if data:
        lis = data
    return lis


#
def getRenderableRenderLayers():
    lis = []
    renderLayers = getRenderLayers()
    if renderLayers:
        for node in renderLayers:
            if not maUtils.isReferenceNode(node):
                enableAttr = node + '.' + 'renderable'
                if cmds.getAttr(enableAttr):
                    lis.append(node)
    return lis


#
def setCurrentRenderLayer(renderLayer):
    cmds.editRenderLayerGlobals(currentRenderLayer=renderLayer)


#
def getRenderableCameraLis(fullPath=True):
    lis = []
    cameras = maUtils.getNodeLisByType('camera')
    for camera in cameras:
        renderable = cmds.getAttr(camera + '.renderable')
        if renderable:
            transformPath = maUtils.getNodeTransform(camera, fullPath=fullPath)
            lis.append(transformPath)
    return lis


#
def getRenderableCameraNames(fullPath=True):
    lis = []
    cameras = maUtils.getNodeLisByType('camera')
    for camera in cameras:
        renderable = cmds.getAttr(camera + '.renderable')
        if renderable:
            transformPath = maUtils.getNodeTransform(camera, fullPath=fullPath)
            lis.append(transformPath)
    return lis


#
def setRenderCamera(filterCameras):
    cameraShapes = maUtils.getNodeLisByType('camera')
    for shapePath in cameraShapes:
        renderableAttr = shapePath + '.' + 'renderable'
        transformPath = maUtils.getNodeTransform(shapePath)
        objectName = maUtils._toNodeName(transformPath)
        if objectName in filterCameras:
            cmds.setAttr(renderableAttr, 1)
        else:
            cmds.setAttr(renderableAttr, 0)


#
def getRenderCameraName(camera):
    return lxBasic.getStrPathName(camera, appCfg.Ma_Separator_Node, appCfg.Ma_Separator_Namespace).replace(appCfg.Ma_Separator_Namespace, '_')


#
def setCreateRenderCameraScriptJob(window, method):
    cameraShapes = maUtils.getNodeLisByType('camera')
    for objectPath in cameraShapes:
        attr = objectPath + '.' + 'renderable'
        maUtils.setCreateAttrChangedScriptJob(window, attr, method)


#
def getWorkspacePath():
    string = none
    data = cmds.workspace(query=1, rootDirectory=1)
    if data:
        if data.endswith('/'):
            string = data[:-1]
    return string


#
def getWorkspaceRule(ruleString):
    return cmds.workspace(fileRuleEntry=ruleString)


#
def getImagePath():
    workspacePath = getWorkspacePath()
    imageAbsPath = getWorkspaceRule('images')
    return lxBasic._toOsFile(workspacePath, imageAbsPath)


#
def setCreateWorkspace(osPath):
    # Create Directory
    cmds.workspace(create=osPath)
    # Create Workspace
    cmds.workspace(osPath, openWorkspace=1)
    # Create Default Rule
    for k, v in MaDefaultWorkspaceRuleDic.items():
        cmds.workspace(fileRule=[k, v])
    # Save
    cmds.workspace(saveWorkspace=1)


#
def setCreateDefaultWorkspaceRule(osPath):
    cmds.workspace(osPath, openWorkspace=1)
    for k, v in MaDefaultWorkspaceRuleDic.items():
        cmds.workspace(fileRule=[k, v])
    #
    cmds.workspace(saveWorkspace=1)


#
def getTempRenderImage(imageFormat):
    imageAbsPath = getWorkspaceRule('images')
    localDirectory = imageAbsPath + '/tmp'
    aovs = cmds.ls(type='aiAOV')
    if aovs:
        localDirectory = imageAbsPath + '/tmp/beauty'
    #
    workspacePath = getWorkspacePath()
    if workspacePath:
        tempImagePath = '{0}/{1}'.format(workspacePath, localDirectory)
        currentFile = maUtils.getCurrentFile()
        currentFileName = lxBasic.getOsFileName(currentFile)
        renderImage = '{0}/{1}{2}'.format(tempImagePath, currentFileName, imageFormat)
        if lxBasic.isOsExistsFile(renderImage):
            return renderImage


#
def getRenderTime():
    startFrame = int(cmds.getAttr(MaNodeAttrRenderOptionDic['startFrame']))
    endFrame = int(cmds.getAttr(MaNodeAttrRenderOptionDic['endFrame']))
    return int(startFrame), int(endFrame)


#
def setRenderTime(startFrame=None, endFrame=None):
    if not startFrame:
        startFrame = int(cmds.playbackOptions(query=1, minTime=1))
    if not endFrame:
        endFrame = int(cmds.playbackOptions(query=1, maxTime=1))
    #
    cmds.setAttr(MaNodeAttrRenderOptionDic['startFrame'], startFrame)
    cmds.setAttr(MaNodeAttrRenderOptionDic['endFrame'], endFrame)
    #
    lxTip.viewMessage(
        u'''Render Time has''', u'''Change to : %s - %s''' % (startFrame, endFrame)
    )


#
def setArnoldImageFormat(imageFormat):
    setLoadArnoldRenderer()
    cmds.setAttr('defaultArnoldDriver.aiTranslator', imageFormat, type='string')


# noinspection PyUnresolvedReferences
def setLoadArnoldRenderer():
    try:
        import mtoa.core as core
        core.createOptions()
    except:pass


#
def setLoadRenderer(renderer):
    if renderer == lxConfigure.LynxiArnoldRendererValue:
        setLoadArnoldRenderer()


# Set Renderer
def setCurrentRenderer(renderer):
    if renderer == lxConfigure.LynxiArnoldRendererValue:
        cmds.setAttr(MaNodeAttrRenderOptionDic['renderer'], 'arnold', type='string')
        setLoadArnoldRenderer()
    elif renderer == lxConfigure.LynxiRedshiftRendererValue:
        cmds.setAttr(MaNodeAttrRenderOptionDic['renderer'], 'redshift', type='string')


#
def setRebuildMayaUi():
    maUtils.setWindowDelete('unifiedRenderGlobalsWindow')
    mel.eval("buildNewSceneUI;")


#
def setRelinkArnoldAov(aovNodeLis=None):
    if not aovNodeLis:
        aovNodeLis = cmds.ls(type='aiAOV')
    #
    defDriverAttr = 'defaultArnoldDriver.message'
    defFilterAttr = 'defaultArnoldFilter.message'
    if aovNodeLis:
        for aovNode in aovNodeLis:
            outputDriverAttr = aovNode + '.outputs[0].driver'
            if not cmds.isConnected(defDriverAttr, outputDriverAttr):
                cmds.connectAttr(defDriverAttr, outputDriverAttr)
            #
            outputFilterAttr = aovNode + '.outputs[0].filter'
            if not cmds.isConnected(defFilterAttr, outputFilterAttr):
                cmds.connectAttr(defFilterAttr, outputFilterAttr)


#
def setCreateLightWithName(nodeName, nodeType):
    shapeName = '%sShape' % nodeName
    transform = cmds.shadingNode(nodeType, name=shapeName, asLight=True)
    return shapeName, transform


#
def setCreateArnoldLight():
    nodeName = appVariant.lxPreviewLight
    nodeType = 'aiSkyDomeLight'
    if not maUtils.isAppExist(nodeName):
        setCreateLightWithName(nodeName, nodeType)
        #
        attrData = [('camera', .25)]
        [cmds.setAttr(nodeName + '.' + attrName, attrValue) for attrName, attrValue in attrData]


#
def setArnoldRender(camera, width, height):
    setLoadArnoldRenderer()
    #
    cmds.arnoldRender(cam=camera, w=width, h=height)
    return True


#
def setRenderPreMelCommand(melCommand):
    cmds.setAttr(MaNodeAttrRenderOptionDic['preMel'], melCommand, type='string')


#
def setRenderSnapshot(groupString, osFile, renderer, width, height, useDefaultView, useDefaultLight):
    setLoadArnoldRenderer()
    #
    imageFormat = appVariant.pngExt
    camera = 'persp'
    cameraShape = 'perspShape'
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
        focalLength=57.089,
        overscan=1.15
    )
    if useDefaultView:
        cmds.select(groupString)
        #
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
    #
    if renderer == lxConfigure.LynxiArnoldRendererValue:
        if useDefaultLight is True:
            setCreateArnoldLight()
        #
        cmds.setAttr('defaultArnoldDriver.colorManagement', 0)
        setArnoldImageFormat(imageFormat[1:])
        isRender = setArnoldRender(camera, width, height)
        if isRender:
            image = getTempRenderImage(imageFormat)
            if image:
                lxBasic.setOsFileCopy(image, osFile)


#
def getLightsByRoot(root):
    lightTypes = maUtils.getNodeTypeLisByFilter('light')
    return maUtils.getChildObjectsByRoot(root, lightTypes)


#
def getAiLightDecays(lightObjectPath):
    shape = maUtils.getNodeShape(lightObjectPath)
    return maUtils.getInputNodes(shape, 'aiLightDecay')


#
def setConnectLightsToScale(root):
    def setBranch(scaleAttr, attr):
        expressionNode = '_'.join(maUtils._toNodeName(attr).split('.')) + '_expression_0'
        attrData = cmds.getAttr(attr)
        command = '{0} = {1}*{2}*{2}'.format(attr, attrData, scaleAttr)
        #
        cmds.expression(
            name=expressionNode,
            string=command,
            object=root,
            alwaysEvaluate=1,
            unitConversion=1
        )
    #
    def setMain():
        if maUtils.isAppExist(root):
            scaleAttr = root + '.' + attrName
            #
            maUtils.setAttrAdd(root, attrName, attributeType='double', data=1)
            #
            lightObjectPaths = getLightsByRoot(root)
            if lightObjectPaths:
                aiLightDecays = []
                explain = '''Connect Light to Scale'''
                maxValue = len(lightObjectPaths)
                progressBar = lxProgress.viewSubProgress(explain, maxValue)
                for i in lightObjectPaths:
                    progressBar.updateProgress()
                    attr = i + '.intensity'
                    if maUtils.isAppExist(attr):
                        if not maUtils.isAttrDestination(attr):
                            setBranch(scaleAttr, attr)
                    #
                    lxBasic.setListExtendSubList(aiLightDecays, getAiLightDecays(i))
                #
                if aiLightDecays:
                    for i in aiLightDecays:
                        attr = i + '.farEnd'
                        if maUtils.isAppExist(attr):
                            if not maUtils.isAttrDestination(attr):
                                setBranch(scaleAttr, attr)
    #
    attrName = 'lightScale'
    setMain()


#
def getRenderColorSpace():
    return cmds.colorManagementPrefs(query=1, renderingSpaceName=1)


#
def getColorMangerEnabled():
    return cmds.colorManagementPrefs(query=True, cmEnabled=True)


# noinspection PyUnresolvedReferences
def setCovertTextureToTx(textures, force):
    import os
    from arnold.arnold_common import ai
    AiMakeTx = ai.AiMakeTx
    AiUniverseIsActive = ai.AiUniverseIsActive
    AiTextureInvalidate = ai.AiTextureInvalidate
    if maUtils.isArnoldEnable():
        txItems = []
        filesCount = []
        filesCount.append(0)
        filesCount.append(0)
        # first we need to make sure the options & color manager node were converted to arnold
        arnoldUniverseActive = AiUniverseIsActive()
        if not arnoldUniverseActive:
            cmds.arnoldScene(mode='create')
        GetTxList(txItems, filesCount)
        arg_options = "-v --unpremult --oiio"
        if force == 0:
            arg_options = "-u " + arg_options
        mayaVersion_ = lxBasic.getMayaAppVersion()
        if mel.eval("exists \"colorManagementPrefs\""):
            # only do this if command colorManagementPrefs exists
            renderColorSpace = getRenderColorSpace()
            cmEnable = getColorMangerEnabled()
        else:
            renderColorSpace = 'linear'
            cmEnable = False
        #
        textureList = []
        for textureLine in txItems:
            texture = textureLine[0]
            # we could use textureLine[2] for the colorSpace
            # but in case it hasn't been updated correctly
            # it's still better to ask maya again what is the color space
            nodes = textureLine[3]
            colorSpace = 'auto'
            conflictSpace = False
            # colorSpace didn't exist in maya 2015
            if mayaVersion_ >= 2016:
                for node in nodes:
                    nodeColorSpace = cmds.getAttr(node + '.colorSpace')
                    if colorSpace != 'auto' and colorSpace != nodeColorSpace:
                        conflictSpace = True
                    colorSpace = nodeColorSpace
                if colorSpace == 'auto' and textureLine[2] != '':
                    colorSpace = textureLine[2]
            if not texture:
                continue
            if conflictSpace:
                print ' Error : Conflicting color spaces'
            # Process all the files that were found previously for this texture (eventually multiple tokens)
            for inputFile in textureLine[4]:
                # here inputFile is already expanded, and only corresponds to existing files
                if len(textureLine[4]) > 1:
                    print '  -' + inputFile
                txArguments = arg_options
                if cmEnable is True and colorSpace != renderColorSpace:
                    txArguments += ' --colorconvert "'
                    txArguments += colorSpace
                    txArguments += '" "'
                    txArguments += renderColorSpace
                    txArguments += '"'
                # need to invalidate the TX texture from the cache
                outputTx = os.path.splitext(inputFile)[0] + '.tx'
                AiTextureInvalidate(outputTx)
                textureList.append([inputFile, txArguments])
        for textureToConvert in textureList:
            AiMakeTx(textureToConvert[0], textureToConvert[1])
