# coding:utf-8
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMaya, OpenMayaUI
#
from LxCore.method import _osMethod
#
from LxCore.method.basic import _methodBasic
#
from LxMaya.method.basic import _maMethodBasic
#
from LxMaya.method.config import _maConfig


#
class Mtd_MaAnimation(_methodBasic.Mtd_Basic):
    app_method = _maMethodBasic.Mtd_AppMaya
    @staticmethod
    def setCurrentFrame(frame):
        cmds.currentTime(frame)
    @staticmethod
    def getCurrentFrame():
        return cmds.currentTime(query=1)
    @staticmethod
    def setAnimationFrameRange(startFrame, endFrame):
        cmds.playbackOptions(minTime=startFrame), cmds.playbackOptions(animationStartTime=int(startFrame) - 5)
        cmds.playbackOptions(maxTime=endFrame), cmds.playbackOptions(animationEndTime=int(endFrame) + 5)
    @classmethod
    def toFrameRange(cls, frame):
        if isinstance(frame, tuple) or isinstance(frame, list):
            startFrame, endFrame = frame
        elif isinstance(frame, int) or isinstance(float, float):
            startFrame = endFrame = frame
        else:
            startFrame = endFrame = cls.getCurrentFrame()
        return startFrame, endFrame


#
class MaAssemblyMethod(_maMethodBasic.Mtd_AppMaya):
    _nodeMethod = _maMethodBasic.MaNodeMethodBasic
    @classmethod
    def getAssemblyReferenceLis(cls):
        pass
    @staticmethod
    def getAssemblyDefinitionFile(assemblyReferenceString):
        attr = assemblyReferenceString + '.definition'
        return cmds.getAttr(attr)
    @staticmethod
    def setAssemblyActive(assemblyReferenceString, name):
        cmds.assembly(assemblyReferenceString + '.representations', edit=1, active=name)
    @staticmethod
    def getAssemblyActive(assemblyReferenceString):
        return cmds.assembly(assemblyReferenceString, query=1, active=1) or 'None'
    @staticmethod
    def getAssemblyNamespace(assemblyReferenceString):
        return cmds.assembly(assemblyReferenceString, query=1, repNamespace=1)
    @classmethod
    def setAssemblySceneDefinitionCreate(cls, assemblyReferenceString, osFile):
        cmds.assembly(name=assemblyReferenceString, type=cls._maConfig.MaNodeType_AssemblyDefinition)
        cmds.assembly(assemblyReferenceString, edit=1, createRepresentation='Scene', input=osFile)
        cmds.assembly(assemblyReferenceString, edit=1, active=cls.getOsFileBasename(osFile))
    @classmethod
    def setAssemblyReferenceCreate(cls, assemblyReferenceString, osAssemblyDefinitionFile):
        cmds.assembly(name=assemblyReferenceString, type=cls._maConfig.MaNodeType_AssemblyReference)
        cmds.setAttr(assemblyReferenceString + '.definition', osAssemblyDefinitionFile, type='string')


#
class MaWindowMethod(_maMethodBasic.Mtd_AppMaya):
    MaDefShader = 'lambert1'
    MaDefWindowMaximum = 2048
    MaDefBackgroundRgb = .25, .25, .25
    MaDefShaderRgb = 0, .75, .75
    @staticmethod
    def isWindowExists(nameText):
        return cmds.window(nameText, exists=1)
    @staticmethod
    def setVisiblePanelsDelete():
        viewPanelLis = cmds.getPanel(visiblePanels=1)
        for viewport in viewPanelLis:
            if viewport != 'modelPanel4':
                if cmds.panel(viewport, exists=1):
                    window = viewport + 'Window'
                    if cmds.window(window, exists=1):
                        cmds.deleteUI(window)
    @classmethod
    def setCreateWindow(cls, nameText, width, height, percent=.5):
        cls.setWindowDelete(nameText)
        #
        width, height = cls._toSizeRemap(width, height, maximum=cls.MaDefWindowMaximum)
        cmds.window(
            nameText,
            title=cls.str_camelcase2prettify(nameText)
        )
        #
        cmds.showWindow(nameText)
        #
        return cmds.paneLayout(
            width=width*percent,
            height=height*percent
        )
    @classmethod
    def setDefaultShaderColor(cls, r, g, b):
        cmds.setAttr(cls.MaDefShader + '.color', r, g, b)
    @staticmethod
    def setBackgroundColor(r, g, b):
        cmds.displayRGBColor('background', r, g, b)
        cmds.displayRGBColor('backgroundTop', r, g, b)
        cmds.displayRGBColor('backgroundBottom', r, g, b)
    @classmethod
    def setWindowDelete(cls, nameText):
        if cls.isWindowExists(nameText):
            cmds.deleteUI(nameText)


#
class Mtd_MaViewport(_maMethodBasic.Mtd_AppMaya):
    MaDefViewportViewOptionKwargs = dict(
        displayAppearance='smoothShaded',
        displayLights='default',
        useDefaultMaterial=False,
        wireframeOnShaded=False,
        fogging=False,
        twoSidedLighting=True,
        manipulators=False,
        grid=False,
        headsUpDisplay=False,
        selectionHiliteDisplay=False,
    )
    MaDefViewportObjectDisplayOptionKwargs = dict(
        polymeshes=True,
        subdivSurfaces=True,
        fluids=True,
        strokes=True,
        nCloths=True,
        nParticles=True,
        pluginShapes=True,
        pluginObjects=['gpuCacheDisplayFilter', 1]
    )
    @classmethod
    def setCreateViewPanel(cls, viewport, layout, camera, menuBarVisible=False):
        return cmds.modelPanel(
            label=cls.str_camelcase2prettify(viewport),
            parent=layout,
            camera=camera,
            menuBarVisible=menuBarVisible,
        )
    @classmethod
    def setViewportView(cls, viewport, optionKwargs=None):
        if optionKwargs is None:
            optionKwargs = cls.MaDefViewportViewOptionKwargs.copy()
        cmds.modelEditor(
            viewport,
            edit=1,
            activeView=1,
            #
            **optionKwargs
        )
    @classmethod
    def setViewportObjectDisplay(cls, viewport, optionKwargs=None):
        cmds.modelEditor(
            viewport,
            edit=1,
            activeView=1,
            #
            allObjects=0,
        )
        if optionKwargs is None:
            optionKwargs = cls.MaDefViewportObjectDisplayOptionKwargs.copy()
        #
        cmds.modelEditor(
            viewport,
            edit=1,
            activeView=1,
            #
            **optionKwargs
        )
    @staticmethod
    def setViewportVp2Renderer(viewport, lineAAEnable=True, multiSampleEnable=True, ssaoEnable=True):
        rendererName = 'vp2Renderer'
        panelType = cmds.getPanel(typeOf=viewport)
        if panelType == 'modelPanel':
            cmds.modelEditor(
                viewport,
                edit=1,
                rendererName=rendererName,
                rendererOverrideName='myOverride'
            )
            cmds.setAttr('hardwareRenderingGlobals.lineAAEnable', lineAAEnable)
            cmds.setAttr('hardwareRenderingGlobals.multiSampleEnable', multiSampleEnable)
            cmds.setAttr('hardwareRenderingGlobals.ssaoEnable', ssaoEnable)
    @staticmethod
    def setViewportDefaultDisplayMode(viewport):
        cmds.modelEditor(
            viewport,
            edit=1,
            activeView=1,
            useDefaultMaterial=1,
            displayAppearance='smoothShaded',
            displayTextures=0,
            displayLights='default',
            shadows=0
        )
    @staticmethod
    def setViewportShaderDisplayMode(viewport):
        cmds.modelEditor(
            viewport,
            edit=1,
            activeView=1,
            useDefaultMaterial=0,
            displayAppearance='smoothShaded',
            displayTextures=0,
            displayLights='default',
            shadows=0
        )
    @staticmethod
    def setViewportTextureDisplayMode(viewport):
        cmds.modelEditor(
            viewport,
            edit=1,
            activeView=1,
            useDefaultMaterial=0,
            displayAppearance='smoothShaded',
            displayTextures=1,
            displayLights='default',
            shadows=0
        )
    @staticmethod
    def setViewportLightDisplayMode(viewport):
        cmds.modelEditor(
            viewport,
            edit=1,
            activeView=1,
            useDefaultMaterial=0,
            displayAppearance='smoothShaded',
            displayTextures=1,
            displayLights='all',
            shadows=1
        )
    @staticmethod
    def setViewportSelectObjectIsolate(viewport, boolean=True):
        cmds.isolateSelect(viewport, state=boolean)


#
class MaGeometryNodeMethod(_maMethodBasic.M2GeometryNodeMethodBasic):
    pass


#
class MaCheckMethod(_maMethodBasic.M2GeometryNodeMethodBasic, _maConfig.MaProductConfig):
    @classmethod
    def filterGroupEmptyLis(cls, groupString):
        lis = []
        stringLis = cls._toNodeLis(groupString)
        if stringLis:
            for i in stringLis:
                shapeLis = cls.getChildShapeLisByGroup(i)
                if not shapeLis:
                    lis.append(i)
        return lis
    @classmethod
    def fixGroupEmpty(cls, groupString):
        stringLis = cls._toNodeLis(groupString)
        [cls.setNodeDelete(i) for i in stringLis if cls.isAppExist(i)]
    #
    @classmethod
    def filterNonShapeTransformLis(cls, objectString):
        lis = []
        #
        stringLis = cls._toNodeLis(objectString)
        if stringLis:
            for transform in stringLis:
                shapePath = cls.getNodeShape(transform)
                if shapePath is None:
                    lis.append(transform)
        return lis
    @classmethod
    def fixNonShapeTransform(cls, objectString):
        stringLis = cls._toNodeLis(objectString)
        [cls.setNodeDelete(i) for i in stringLis if cls.isAppExist(i)]
    @classmethod
    def filterObjectInstanceLis(cls, objectString):
        lis = []
        stringLis = cls._toNodeLis(objectString)
        if stringLis:
            for transform in stringLis:
                shapePath = cls.getNodeShape(transform)
                if cls.isObjectInstanced(shapePath) is True:
                    lis.append(transform)
        return lis
    @classmethod
    def fixObjectInstance(cls, objectString):
        stringLis = cls._toNodeLis(objectString)
        if stringLis:
            for i in stringLis:
                cls.setObjectInstanceCovert(i)
    @classmethod
    def filterObjectHistoryNodeDic(cls, objectString):
        dic = {}
        exceptNodeTypeLis = [
            cls.MaNodeType_ShadingEngine,
            cls.MaNodeType_GroupId,
            cls.MaNodeType_Set
        ]
        #
        stringLis = cls._toNodeLis(objectString)
        if stringLis:
            for transform in stringLis:
                stringLis = cmds.listHistory(transform, pruneDagObjects=1) or []
                for node in stringLis:
                    nodeType = cls.getNodeType(node)
                    if not nodeType in exceptNodeTypeLis:
                        dic.setdefault(transform, []).append(node)
        return dic
    @classmethod
    def fixObjectHistory(cls, objectString):
        pass
    @classmethod
    def filterObjectNonDefaultMatrixLis(cls, objectString):
        lis = []
        #
        stringLis = cls._toNodeLis(objectString)
        if stringLis:
            for i in stringLis:
                if cls.isDefaultMatrix(i) is False:
                    lis.append(i)
        return lis
    @classmethod
    def fixTransformNonDefaultMatrix(cls, objectString):
        pass
    @classmethod
    def _toErrorDic(cls, errorLis):
        dic = {}
        if errorLis:
            for i in errorLis:
                meshPath = cls._getNodePathString(i.split(cls.Ma_Separator_Attribute)[0])
                compPath = i
                #
                dic.setdefault(meshPath, []).append(compPath)
        #
        cmds.select(clear=1)
        return dic
    @classmethod
    def getMeshNSideFaceDic(cls, meshObjectLis):
        cmds.select(meshObjectLis)
        cmds.polySelectConstraint(mode=3, type=8, size=3)
        cmds.polySelectConstraint(mode=0, type=8, size=0)
        return cls._toErrorDic(cmds.ls(selection=True))
    @classmethod
    def getMeshNonPlanarFaceDic(cls, meshObjectLis):
        cmds.select(meshObjectLis)
        cmds.polySelectConstraint(mode=3, type=8, planarity=1)
        cmds.polySelectConstraint(mode=0, type=8, planarity=0)
        return cls._toErrorDic(cmds.ls(selection=True))
    @classmethod
    def getMeshHoledFaceDic(cls, meshObjectLis):
        cmds.select(meshObjectLis)
        cmds.polySelectConstraint(mode=3, type=8, holes=1)
        cmds.polySelectConstraint(mode=0, type=8, holes=0)
        return cls._toErrorDic(cmds.ls(selection=True))
    @classmethod
    def getMeshConcaveFaceDic(cls, meshObjectLis):
        cmds.select(meshObjectLis)
        cmds.polySelectConstraint(mode=3, type=8, convexity=1)
        cmds.polySelectConstraint(mode=0, type=8, convexity=0)
        return cls._toErrorDic(cmds.ls(selection=True))
    @classmethod
    def getMeshSharedUvDic(cls, meshObjectLis):
        cmds.select(meshObjectLis)
        cmds.polySelectConstraint(mode=3, type=16, textureshared=1)
        cmds.polySelectConstraint(mode=0, type=16, textureshared=0)
        return cls._toErrorDic(cmds.ls(selection=True))
    @classmethod
    def getMeshZeroAreaFaceDic(cls, meshObjectLis):
        miniValue = .0
        maxiValue = .0
        cmds.select(meshObjectLis)
        cmds.polySelectConstraint(mode=3, type=8, geometricarea=1, geometricareabound=(miniValue, maxiValue))
        cmds.polySelectConstraint(mode=0, type=8, geometricarea=0)
        return cls._toErrorDic(cmds.ls(selection=True))
    @classmethod
    def getMeshZeroLengthEdgeDic(cls, meshObjectLis):
        miniValue = .0
        maxiValue = .0
        cmds.select(meshObjectLis)
        cmds.polySelectConstraint(mode=3, type=0x8000, length=1, lengthbound=(miniValue, maxiValue))
        cmds.polySelectConstraint(mode=0, type=0x8000, length=0)
        return cls._toErrorDic(cmds.ls(selection=True))
    @classmethod
    def getMeshZeroAreaUvDic(cls, meshObjectLis):
        miniValue = .0
        maxiValue = .0
        cmds.select(meshObjectLis)
        cmds.polySelectConstraint(mode=3, type=8, geometricarea=1, geometricareabound=(miniValue, maxiValue))
        cmds.polySelectConstraint(mode=3, type=8, texturedarea=1, texturedareabound=(miniValue, maxiValue))
        cmds.polySelectConstraint(mode=0, type=8, texturedarea=0, geometricarea=0)
        return cls._toErrorDic(cmds.ls(selection=True))
    @classmethod
    def getMeshLaminaFaceDic(cls, meshObjectLis):
        cmds.select(meshObjectLis)
        cmds.polySelectConstraint(mode=3, type=8, topology=2)
        cmds.polySelectConstraint(mode=0, type=8, topology=0)
        return cls._toErrorDic(cmds.ls(selection=True))
    @classmethod
    def getMeshNonTriangulableFaceDic(cls, meshObjectLis):
        cmds.select(meshObjectLis)
        cmds.polySelectConstraint(mode=3, type=8, topology=1)
        cmds.polySelectConstraint(mode=0, type=8, topology=0)
        return cls._toErrorDic(cmds.ls(selection=True))
    @classmethod
    def getMeshNonMappingFaceDic(cls, meshObjectLis):
        cmds.select(meshObjectLis)
        cmds.polySelectConstraint(mode=3, type=8, textured=2)
        cmds.polySelectConstraint(mode=0, type=8, textured=0)
        return cls._toErrorDic(cmds.ls(selection=True))
    @classmethod
    def getMeshNonManifoldVertexDic(cls, meshObjectLis):
        cmds.select(meshObjectLis)
        return cls._toErrorDic(cmds.polyInfo(nonManifoldVertices=1))
    @classmethod
    def getMeshNonManifoldEdgeDic(cls, meshObjectLis):
        cmds.select(meshObjectLis)
        return cls._toErrorDic(cmds.polyInfo(nonManifoldEdges=1))
    @classmethod
    def filterObjectNameOverlapDic(cls, objectString):
        dic = {}
        #
        stringLis = cls._toNodeLis(objectString)
        if stringLis:
            for transform in stringLis:
                nodeName = cls._toNodeName(transform)
                data = cmds.ls(nodeName, long=1) or []
                if len(data) > 1:
                    for i in data:
                        if not i == transform:
                            dic.setdefault(transform, []).append(i)
        return dic
    @classmethod
    def getMeshNormalLockVertexDic(cls, objectString):
        dic = {}
        #
        stringLis = cls._toNodeLis(objectString)
        if stringLis:
            for transform in stringLis:
                vertexIdLis = cls.getMeshNormalLockVertexLis(transform)
                if vertexIdLis:
                    dic[transform] = cls._toMeshVertexComp(transform, vertexIdLis)
        return dic
    @classmethod
    def getMeshOpenEdgeDic(cls, objectString):
        dic = {}
        #
        stringLis = cls._toNodeLis(objectString)
        if stringLis:
            for i in stringLis:
                edgeIdLis = cls.getMeshOpenEdgeIdLis(i)
                if edgeIdLis:
                    dic[i] = cls._toMeshEdgeComp(i, edgeIdLis)
        #
        return dic
    @classmethod
    def maAstModelGeometryCheckConfigDic(cls):
        return cls.orderedDict(
            [
                ('meshInstanceCheck', (True, 'Mesh has Instance', u'存在关联复制的"Mesh"', cls.filterObjectInstanceLis, None)),
                ('meshHistoryCheck', (True, 'Mesh has History Nde_Node(s)', u'存在历史记录的"Mesh"', cls.filterObjectHistoryNodeDic, None)),
                #
                ('meshOverlapNameCheck', (True, 'Mesh has Overlap Name', u'存在重名的"Mesh"', cls.filterObjectNameOverlapDic, None)),
                #
                ('meshMatrixNonDefaultCheck', (True, 'Mesh Matrix is Non - Default ', (u'非默认的"Mesh Matrix"', u'1."Transform"的"Transformation"存在数值', u'2."Group"的"Transformation"存在数值'), cls.filterObjectNonDefaultMatrixLis, None)),
                #
                ('meshFaceNSidedCheck', (True, 'Mesh Face(s) is N - Sided', u'超过四边的"Mesh Face"', cls.getMeshNSideFaceDic, None)),
                ('meshFaceHoledCheck', (True, 'Mesh Face(s) is Holed', u'破损的"Mesh Face"', cls.getMeshHoledFaceDic, None)),
                ('meshFaceConcaveCheck', (False, 'Mesh Face(s) is Concave', u'凹形的"Mesh Face"', cls.getMeshConcaveFaceDic, None)),
                ('meshFaceNonPlanarCheck', (False, 'Mesh Face(s) is Non - planar', u'不平整的"Mesh Face"', cls.getMeshNonPlanarFaceDic, None)),
                ('meshFaceNonTriangulableCheck', (True, 'Mesh Face(s) is Non - Triangulable', u'无法三角化的"Mesh Face"', cls.getMeshNonTriangulableFaceDic, None)),
                ('meshFaceNonMappingCheck', (True, 'Mesh Face(s) is Non - Mapping', u'无Uv的"Mesh Face"', cls.getMeshNonMappingFaceDic, None)),
                ('meshFaceLaminaCheck', (True, 'Mesh Face(s) is Lamina', u'重合的"Mesh Face"', cls.getMeshLaminaFaceDic, None)),
                #
                ('meshEdgeNonManifoldCheck', (True, 'Mesh Edge(s) is Non - Manifold', u'非流形的"Mesh Edge"', cls.getMeshNonManifoldEdgeDic, None)),
                ('meshFaceZeroAreaCheck', (True, 'Mesh Face(s) is Zero - Area', u'无面积的"Mesh Face"', cls.getMeshZeroAreaFaceDic, None)),
                ('meshEdgeZeroLengthCheck', (True, 'Mesh Edge(s) is Zero - Length', u'无长度的"Mesh Edge"', cls.getMeshZeroLengthEdgeDic, None)),
                ('meshEdgeOpenCheck', (True, 'Mesh Edge(s) is Open', u'开放的"Mesh Edge"', cls.getMeshOpenEdgeDic, None)),
                #
                ('meshVertexNormalLockCheck', (True, 'Mesh Vertex(s) is Normal - Lock', u'锁定的"Mesh Vertex Normal"', cls.getMeshNormalLockVertexDic, None)),
                ('meshVertexNonManifoldCheck', (True, 'Mesh Vertex(s) is Non - Manifold', u'非流形的"Mesh Vertex"', cls.getMeshNonManifoldVertexDic, None)),
                #
                ('meshUvSharedCheck', (False, 'Mesh Uv(s) is Shared', u'共用"Mesh Uv"', cls.getMeshSharedUvDic, None)),
                ('meshUvZeroAreaCheck', (True, 'Mesh Uv(s) is Zero - Area', u'无面积的"Mesh Uv"', cls.getMeshZeroAreaUvDic, None)),
            ]
        )
    @classmethod
    def maAstModelTransformCheckConfigDic(cls):
        return cls.orderedDict(
            [
                ('transformNonShapeCheck', (True, 'Transform has Non - Shape', u'无"Shape"的"Transform"', cls.filterNonShapeTransformLis, None))
            ]
        )
    @classmethod
    def maAstModelGroupCheckConfigDic(cls):
        return cls.orderedDict(
            [
                ('groupEmptyCheck', (True, 'Group is Empty', u'空的"Group"', cls.filterGroupEmptyLis, cls.fixGroupEmpty))
            ]
        )


#
class MaCameraNodeMethod(_maMethodBasic.MaNodeMethodBasic):
    MaDefDisplayGateMaskOpacity = 1
    MaDefDisplayGateMaskColor = 0, 0, 0
    #
    MaDefCameraOptionKwargs = dict(
        displayResolution=True,
        displayFilmGate=False,
        displayGateMask=True,
        displaySafeTitle=False,
        displaySafeAction=False,
        displayFieldChart=False,
        filmFit=1,
        overscan=1
    )
    @classmethod
    def setCameraView(cls, objectString=None, optionKwargs=None):
        if objectString is None:
            shapePath = cls.getActiveCameraShape()
        else:
            shapePath = cls.getNodeShape(objectString)
        #
        if optionKwargs is None:
            optionKwargs = cls.MaDefCameraOptionKwargs.copy()
        #
        cmds.camera(
            shapePath,
            edit=1,
            **optionKwargs
        )
        #
        cmds.setAttr(
            shapePath + '.displayGateMaskOpacity',
            cls.MaDefDisplayGateMaskOpacity
        )
        cmds.setAttr(
            shapePath + '.displayGateMaskColor',
            *cls.MaDefDisplayGateMaskColor, type='double3'
        )
    @staticmethod
    def getActiveCameraShape():
        cameraView, cameraDag = OpenMayaUI.M3dView.active3dView(), OpenMaya.MDagPath()
        cameraView.getCamera(cameraDag)
        return cameraDag.fullPathName()
    @classmethod
    def getActiveCameraObject(cls):
        shapePath = cls.getActiveCameraShape()
        return cls.getNodeTransform(shapePath)
    @staticmethod
    def setCameraDefPos(objectString):
        cmds.setAttr(objectString + '.translate', 28, 21, 28)
        cmds.setAttr(objectString + '.rotate', -27.9383527296, 45, 0)
        cmds.setAttr(objectString + '.nearClipPlane', .1)
        cmds.setAttr(objectString + '.farClipPlane', 1000000)
    @classmethod
    def setCameraViewFit(cls, objectString):
        shapePath = cls.getNodeShape(objectString)
        cmds.viewFit(shapePath, fitFactor=0, animate=1)
    @classmethod
    def getCameraFocalLength(cls, objectString):
        shapePath = cls.getNodeShape(objectString)
        return cmds.camera(shapePath, query=1, focalLength=1)
    @staticmethod
    def setCameraCloseHud():
        hudLis = cmds.headsUpDisplay(listHeadsUpDisplays=1)
        if hudLis:
            for i in hudLis:
                cmds.headsUpDisplay(i, remove=1)
    # noinspection PyBroadException
    @staticmethod
    def setHudColor(labelColor=19, valueColor=16):
        isExists = cmds.displayColor("headsUpDisplayLabels", query=1, dormant=1)
        if isExists:
            try:
                cmds.displayColor('headsUpDisplayLabels', labelColor, dormant=1)
            except:
                pass
        isExists = cmds.displayColor('headsUpDisplayValues', query=1, dormant=1)
        if isExists:
            try:
                cmds.displayColor('headsUpDisplayValues', valueColor, dormant=1)
            except:
                pass


#
class MaShaderNodeGraphMethod(_maMethodBasic.MaNodeGraphMethodBasic):
    MaDefShadingEngineLis = [
        'initialShadingGroup',
        'initialParticleSE',
        'defaultLightSet',
        'defaultObjectSet'
    ]
    @classmethod
    def getShadingEngineLis(cls):
        return cls.getNodeLisByType(cls.MaNodeType_ShadingEngine, exceptStrings=cls.MaDefShadingEngineLis)
    @classmethod
    def getShadingEngineLisByObject(cls, objectString):
        def getBranch(subObjectString):
            shapePath = cls.getNodeShape(subObjectString)
            if not shapePath:
                shapePath = subObjectString
            #
            outputObjectLis = cls.getOutputObjectLis(shapePath, cls.MaNodeType_ShadingEngine)
            if outputObjectLis:
                [lis.append(j) for j in outputObjectLis if not j in lis and not j in cls.MaDefShadingEngineLis]
        #
        lis = []
        #
        stringLis = cls._toNodeLis(objectString)
        [getBranch(i) for i in stringLis]
        return lis
    @classmethod
    def getShadingEngineObjSet(cls, objectString):
        """
        :param objectString: str
        :return: list
        """
        lis = []
        #
        objSetLis = cmds.sets(objectString, query=1)
        if objSetLis:
            shaderObjectPathLis = [i for i in cmds.ls(objSetLis, leaf=1, noIntermediate=1, long=1)]
            for shaderObjectPath in shaderObjectPathLis:
                # Object Group
                showType = cmds.ls(shaderObjectPath, showType=1)[1]
                if showType == 'float3':
                    shaderObjectPath_ = shaderObjectPath.split('.')[0]
                    shaderObjectUuid = cls.getNodeUniqueId(shaderObjectPath_)
                    objSetData = shaderObjectPath, shaderObjectUuid
                    if not objSetData in lis:
                        lis.append(objSetData)
                else:
                    shaderObjectUuid = cls.getNodeUniqueId(shaderObjectPath)
                    objSetData = shaderObjectPath, shaderObjectUuid
                    if not objSetData in lis:
                        lis.append(objSetData)
        return lis


#
class MaHairNodeGraphMethod(_maMethodBasic.MaNodeGraphMethodBasic):
    @classmethod
    def lynxiGroupName_hairOutputCurve(cls, groupNameLabel):
        return cls.lxNodeGroupName(groupNameLabel, cls.LynxiNameLabel_HairOutputCurve)
    @classmethod
    def _toLynxiHairOutputCurveObjectName(cls, objectNameLabel, seq):
        return cls.lxNodeName(objectNameLabel, cls.LynxiNameLabel_HairOutputCurve, seq)
    @classmethod
    def _toLynxiHairLocalCurveGroupName(cls, groupNameLabel):
        return cls.lxNodeGroupName(groupNameLabel, cls.LynxiNameLabel_HairLocalCurve)
    @classmethod
    def _toLynxiHairLocalCurveObjectName(cls, objectNameLabel, seq):
        return cls.lxNodeName(objectNameLabel, cls.LynxiNameLabel_HairLocalCurve, seq)
    @classmethod
    def _toLynxiHairSolverGroupName(cls, groupNameLabel):
        return cls.lxNodeGroupName(groupNameLabel, cls.LynxiNameLabel_HairSolver)
    @classmethod
    def _toLynxiHairSolverObjectName(cls, objectNameLabel, seq):
        return cls.lxNodeName(objectNameLabel, cls.LynxiNameLabel_HairSolver, seq)
    @classmethod
    def getHairFollicleObjectByOutputCurve(cls, outputCurveObject):
        if outputCurveObject is not None:
            shapePath = cls.getNodeShape(outputCurveObject)
            stringLis = cls.getInputNodeLisFilter(shapePath, source='outCurve')
            if stringLis:
                return cls.getNodeTransform(stringLis[0])
    @classmethod
    def getHairLocalObjectByFollicle(cls, follicleObject):
        if follicleObject is not None:
            shapePath = cls.getNodeShape(follicleObject)
            stringLis = cls.getInputNodeLisFilter(shapePath, source='local')
            if stringLis:
                return cls.getNodeTransform(stringLis[0])
    @classmethod
    def getHairSystemObjectByFollicle(cls, follicleObject):
        if follicleObject is not None:
            shapePath = cls.getNodeShape(follicleObject)
            stringLis = cls.getInputNodeLisFilter(shapePath, source='outputHair')
            if stringLis:
                return cls.getNodeTransform(stringLis[0])
    @classmethod
    def getHairNucleusNodeByHairSystem(cls, hairSystemObject):
        if hairSystemObject is not None:
            shapePath = cls.getNodeShape(hairSystemObject)
            stringLis = cls.getInputNodeLisFilter(shapePath, source='outputObjects')
            if stringLis:
                return stringLis[0]
    @classmethod
    def setHairCurveRename(cls, hairOutputCurveObject, newObjectNames):
        newHairOutputCurveObjectName, newHairLocalCurveObjectName = newObjectNames
        hairFollicleObject = cls.getHairFollicleObjectByOutputCurve(hairOutputCurveObject)
        hairLocalCurveObject = cls.getHairLocalObjectByFollicle(hairFollicleObject)
        #
        cls.setObjectRename(hairOutputCurveObject, newHairOutputCurveObjectName, withShape=True)
        cls.setObjectRename(hairLocalCurveObject, newHairLocalCurveObjectName, withShape=True)
        cls.setObjectRename(hairFollicleObject, newHairLocalCurveObjectName + '_follicle', withShape=True)
    @classmethod
    def setHairCurveCollection(cls, hairOutputCurveObject, rootGroupPath, objectCompGroupPath):
        furHairGroupName = cls.lxGroupName(cls.LynxiNameLabel_FurSolver)
        hairOutputCurveGroupName = cls.lxGroupName(cls.LynxiNameLabel_HairOutputCurve)
        hairLocalCurveGroupName = cls.lxGroupName(cls.LynxiNameLabel_HairLocalCurve)
        hairSolverGroupName = cls.lxGroupName(cls.LynxiNameLabel_HairSolver)
        #
        hairOutputCurveGroupPath = cls.Ma_Separator_Node.join([rootGroupPath, furHairGroupName, hairOutputCurveGroupName, objectCompGroupPath])
        cls.setAppPathCreate(hairOutputCurveGroupPath)
        hairLocalCurveGroupPath = cls.Ma_Separator_Node.join([rootGroupPath, furHairGroupName, hairLocalCurveGroupName, objectCompGroupPath])
        cls.setAppPathCreate(hairLocalCurveGroupPath)
        hairSolverGroupPath = cls.Ma_Separator_Node.join([rootGroupPath, furHairGroupName, hairSolverGroupName])
        cls.setAppPathCreate(hairSolverGroupPath)
        #
        hairFollicleObject = cls.getHairFollicleObjectByOutputCurve(hairOutputCurveObject)
        hairLocalCurveObject = cls.getHairLocalObjectByFollicle(hairFollicleObject)
        #
        hairSystemObject = cls.getHairSystemObjectByFollicle(hairFollicleObject)
        hairNucleusNode = cls.getHairNucleusNodeByHairSystem(hairSystemObject)
        #
        cls.setObjectParent(hairOutputCurveObject, hairOutputCurveGroupPath)
        if hairFollicleObject:
            if not hairLocalCurveObject.startswith(hairFollicleObject):
                cls.setObjectParent(hairLocalCurveObject, hairFollicleObject)
            #
            cls.setObjectParent(hairFollicleObject, hairLocalCurveGroupPath)
        #
        if hairSystemObject is not None:
            cls.setObjectParent(hairSystemObject, hairSolverGroupPath)
        if hairNucleusNode is not None:
            cls.setObjectParent(hairNucleusNode, hairSolverGroupPath)


#
class MaRenderNodeMethod(_maMethodBasic.MaNodeMethodBasic, _maConfig.MaRenderConfig):
    @classmethod
    def _toSizeRange(cls, size):
        if isinstance(size, tuple) or isinstance(size, list):
            width, height = size
        elif isinstance(size, int):
            width = height = size
        else:
            width = height = cls.getRenderSize()
        return width, height
    @classmethod
    def getRenderSize(cls):
        return cmds.getAttr('defaultResolution.width'), cmds.getAttr('defaultResolution.height')
    @staticmethod
    def setRenderSize(width, height, dpi=72):
        cmds.setAttr('defaultResolution.width', width), cmds.setAttr('defaultResolution.height', height)
        cmds.setAttr('defaultResolution.dpi', dpi)
        cmds.setAttr('defaultResolution.pixelAspect', 1)
    @classmethod
    def getCurrentRenderer(cls):
        return cmds.getAttr('defaultRenderGlobals.currentRenderer')
    @classmethod
    def getRenderableCameraLis(cls, fullPath=True):
        lis = []
        stringLis = cls.getNodeLisByType('camera')
        for camera in stringLis:
            renderable = cmds.getAttr(camera + '.renderable')
            if renderable:
                transformPath = cls.getNodeTransform(camera, fullPath=fullPath)
                lis.append(transformPath)
        return lis
    @classmethod
    def getRenderOptionDic(cls):
        def getBranch(nodeString):
            if cls.isAppExist(nodeString):
                attrDatumLis = cls.getNodeDefAttrDatumLis(nodeString)
                #
                dic[nodeString] = attrDatumLis
        #
        dic = {}
        #
        renderer = cls.getCurrentRenderer()
        if renderer == cls.MaRenderer_Software:
            nodeLis = cls.MaRender_Software_Node_Lis
        elif renderer == cls.MaRenderer_Arnold:
            nodeLis = cls.MaRender_Arnold_Node_Lis
        else:
            nodeLis = []
        #
        if nodeLis:
            [getBranch(i) for i in nodeLis]
        return dic
    @classmethod
    def setRenderOption(cls, setDic):
        if setDic:
            for k, v in setDic.items():
                cls.setNodeDefAttrByData(
                    k, v
                )


#
class MaLightNodeMethod(_maMethodBasic.MaNodeMethodBasic, _maMethodBasic.MaSetMethodBasic, _maConfig.MaLightNodeConfig):
    @classmethod
    def getLightTypeLis(cls):
        return cls.getNodeTypeLisByFilter(cls.MaNodeType_Light)
    @classmethod
    def getLightNodeLis(cls, groupString=None):
        typeLis = [i for i in cls.getLightTypeLis() if i not in cls.MaNodeTypeLis_LightDefaultSet_Except]
        stringLis = cls.getNodeLisByType(typeLis)
        if groupString is not None:
            if stringLis:
                if not cls.Ma_Separator_Node in groupString:
                    groupPath = cls._getNodePathString(groupString)
                    return [i for i in stringLis if i.startswith(groupPath)]
        else:
            return stringLis
    @classmethod
    def getLightDefaultSetLis(cls):
        transformLis = cls.getNodeLisBySet(cls.MaNodeName_DefaultLightSet)
        return [cls.getNodeShape(i) for i in transformLis]
    @classmethod
    def getLightLinkDic(cls, groupString=None, ignoreUnused=False):
        def getLightBranch(nodePath, useDefaultSet):
            sourceAttr = cls._toNodeAttr([nodePath, cls.MaAttrName_Message])
            #
            nodeType = cls.getNodeType(nodePath)
            pathDatum, namespaceDatum = cls._toNodePathRebuildDatum(nodePath)
            key = str((nodeType, pathDatum, namespaceDatum))
            #
            enable = False
            for mainAttrName, subLightAttrName, subObjectAttrName in searchDatumLis:
                objectLis = getObjectBranch(
                    sourceAttr,
                    subLightAttrName, subObjectAttrName
                )
                if objectLis:
                    enable = True
                    dic.setdefault(key, {})[mainAttrName] = objectLis
            #
            if ignoreUnused is True:
                if enable is True:
                    dic.setdefault(key, {})[cls.MaNodeName_DefaultLightSet] = useDefaultSet
            else:
                dic.setdefault(key, {})[cls.MaNodeName_DefaultLightSet] = useDefaultSet
        #
        def getObjectBranch(sourceAttr, subLightAttrName, subObjectAttrName):
            lis = []
            targetLightAttrLis = cls.getOutputAttrLisFilter(
                sourceAttr,
                target='*' + subLightAttrName
            )
            if targetLightAttrLis:
                for targetLightAttr in targetLightAttrLis:
                    targetNodeAttr = targetLightAttr[:-len(subLightAttrName)] + subObjectAttrName
                    nodeLis = cls.getInputNodeLisFilter(
                        targetNodeAttr, source='*' + cls.MaAttrName_Message
                    )
                    if nodeLis:
                        for node in nodeLis:
                            nodePath = cls._getNodePathString(node)
                            #
                            nodeType = cls.getNodeType(nodePath)
                            pathDatum, namespaceDatum = cls._toNodePathRebuildDatum(nodePath)
                            lis.append(str((nodeType, pathDatum, namespaceDatum)))
            return lis
        #
        def getMain():
            defaultLightLis = cls.getLightDefaultSetLis()
            lightNodeLis = cls.getLightNodeLis(groupString)
            if lightNodeLis:
                for lightNodePath in lightNodeLis:
                    if lightNodePath in defaultLightLis:
                        useDefaultSet = True
                    else:
                        useDefaultSet = False
                    #
                    getLightBranch(lightNodePath, useDefaultSet)
        #
        dic = cls.orderedDict()
        #
        searchDatumLis = [
            cls.MaAttrNameLis_LightLink,
            cls.MaAttrNameLis_LightLink_Ignore,
            cls.MaAttrNameLis_ShadowLink,
            cls.MaAttrNameLis_ShadowLink_Ignore
        ]
        #
        getMain()
        return dic
    @classmethod
    def setLightLink(cls, lightLinkData):
        def isUsedConnection(attr):
            boolean = False
            if cls.isAppExist(attr):
                if not cls.isAttrDestination(attr):
                    boolean = True
            return boolean
        #
        def toTargetAttr(mainAttrName, subAttrName, index):
            return '{1}{0}{2}[{3}]{0}{4}'.format(cls.Ma_Separator_Attribute, cls.MaNodeName_LightLink, mainAttrName, index, subAttrName)
        #
        def getTargetAttr(mainAttrName, subAttrName):
            index = maxIndexDic[mainAttrName]
            attr = toTargetAttr(mainAttrName, subAttrName, index)
            if isUsedConnection(attr):
                return attr
            else:
                index += 1
                maxIndexDic[mainAttrName] = index
                return getTargetAttr(mainAttrName, subAttrName)
        #
        def setMain():
            if lightLinkData:
                for mainAttrName, lightNodePath, objectNodePath in lightLinkData:
                    maxIndexDic[mainAttrName] = 0
                    #
                    sourceLightAttr, sourceObjectAttr = cls._toNodeAttr([lightNodePath, cls.MaAttrName_Message]), cls._toNodeAttr([objectNodePath, cls.MaAttrName_Message])
                    subLightAttrName, subObjectAttrName = cls.MaAttrNameDic_LightLink[mainAttrName]
                    targetLightAttr = getTargetAttr(mainAttrName, subLightAttrName)
                    targetObjectAttr = targetLightAttr[:-len(subLightAttrName)] + subObjectAttrName
                    #
                    cls.setAttrConnect(sourceLightAttr, targetLightAttr), cls.setAttrConnect(sourceObjectAttr, targetObjectAttr)
        #
        maxIndexDic = {}
        #
        setMain()
    @classmethod
    def setLightDefaultSet(cls, defaultSetData):
        def isUsedConnection(attr):
            boolean = False
            if cls.isAppExist(attr):
                if not cls.isAttrDestination(attr):
                    boolean = True
            return boolean
        #
        def toTargetAttr(nodeName, attrName, index):
            return '{1}{0}{2}[{3}]'.format(cls.Ma_Separator_Attribute, nodeName, attrName, index)
        #
        def getTargetAttr(nodeName, attrName):
            index = maxIndexDic[attrName]
            attr = toTargetAttr(nodeName, attrName, index)
            if isUsedConnection(attr):
                return attr
            else:
                index += 1
                maxIndexDic[attrName] = index
                return getTargetAttr(nodeName, attrName)
        #
        def setMain():
            if defaultSetData:
                nodeName = cls.MaNodeName_DefaultLightSet
                attrName = cls.MaAttrName_SetMember
                maxIndexDic[attrName] = 0
                for lightNodePath, boolean in defaultSetData:
                    transformPath = cls.getNodeTransform(lightNodePath)
                    sourceAttr = cls._toNodeAttr([transformPath, cls.MaAttrName_ObjectGroup])
                    if boolean is True:
                        targetNodeLis = cls.getOutputNodeLisFilter(transformPath, target=attrName)
                        if not nodeName in targetNodeLis:
                            targetAttr = getTargetAttr(nodeName, attrName)
                            cls.setAttrConnect(sourceAttr, targetAttr)
                    else:
                        connectionLis = cls.getOutputConnectionLisFilter(transformPath, target='defaultLightSet.dagSetMembers')
                        if connectionLis:
                            [cls.setAttrDisconnect(*i) for i in connectionLis]
        #
        maxIndexDic = {}
        #
        setMain()
    @classmethod
    def getLightLinkObjectLis(cls, lightNodeString, subLightAttrName, subObjectAttrName):
        lis = []
        #
        sourceAttr = cls._toNodeAttr([lightNodeString, cls.MaAttrName_Message])
        targetLightAttrLis = cls.getOutputAttrLisFilter(
            sourceAttr,
            target='*' + subLightAttrName
        )
        if targetLightAttrLis:
            for targetLightAttr in targetLightAttrLis:
                targetNodeAttr = targetLightAttr[:-len(subLightAttrName)] + subObjectAttrName
                nodeLis = cls.getInputNodeLisFilter(
                    targetNodeAttr, source='*' + cls.MaAttrName_Message
                )
                for node in nodeLis:
                    nodePath = cls._getNodePathString(node)
                    lis.append(nodePath)
        return lis
    @classmethod
    def setLightLinkConnection(cls, dic):
        def isUsedConnection(attr):
            boolean = False
            if cls.isAppExist(attr):
                if not cls.isAttrDestination(attr):
                    boolean = True
            return boolean
        #
        def toTargetAttr(mainAttrName, subAttrName, index):
            return '{1}{0}{2}[{3}]{0}{4}'.format(cls.Ma_Separator_Attribute, cls.MaNodeName_LightLink, mainAttrName, index, subAttrName)
        #
        def getTargetAttr(mainAttrName, subAttrName):
            index = maxIndexDic[mainAttrName]
            attr = toTargetAttr(mainAttrName, subAttrName, index)
            if isUsedConnection(attr):
                return attr
            else:
                index += 1
                maxIndexDic[mainAttrName] = index
                return getTargetAttr(mainAttrName, subAttrName)
        #
        def setMain():
            for mainAttrName, connectionLis in dic.items():
                maxIndexDic[mainAttrName] = 0
                for seq, connectionDatum in enumerate(connectionLis):
                    for attrDatum in connectionDatum:
                        namespace, nodeName, subAttrName = attrDatum
                        if not namespace == cls.Ma_Separator_Namespace:
                            node = cls.Ma_Separator_Namespace.join([namespace, nodeName])
                        else:
                            node = nodeName
                        #
                        sourceAttr = cls._toNodeAttr([node, cls.MaAttrName_Message])
                        #
                        existsTargetAttrLis = cls.getOutputAttrLisFilter(sourceAttr, target='*' + subAttrName)
                        if not existsTargetAttrLis:
                            targetAttr = getTargetAttr(mainAttrName, subAttrName)
                            #
                            cls.setAttrConnect(sourceAttr, targetAttr)
        #
        maxIndexDic = {}
        #
        setMain()
    @classmethod
    def getLightLinkUpdateConstantDatumLis(cls, localDic, serverDic):
        def getCountDic(dic):
            countDic = {}
            if dic:
                lightLis = []
                objectLis = []
                for k, v in dic.items():
                    for ik, iv in v.items():
                        if isinstance(iv, bool):
                            if iv is True:
                                countDic.setdefault(ik, []).append(1)
                        else:
                            countDic.setdefault(ik, []).append(len(iv))
                            for i in iv:
                                if i not in objectLis:
                                    objectLis.append(i)
                    if not k in lightLis:
                        lightLis.append(k)
                    #
                    countDic['light'] = [len(lightLis)]
                    countDic['object'] = [len(objectLis)]
            return countDic
        #
        def getMain():
            serverCountDic, localCountDic = getCountDic(serverDic), getCountDic(localDic)
            for k, v in configDic.items():
                if k in serverCountDic:
                    serverCount = sum(serverCountDic[k])
                else:
                    serverCount = 0
                if k in localCountDic:
                    localCount = sum(localCountDic[k])
                else:
                    localCount = 0
                #
                lis.append(
                    (v, serverCount, localCount)
                )
        #
        lis = []
        #
        configDic = cls.maAttrPrettifyNameDic_lightLink()
        #
        getMain()
        return lis
    @classmethod
    def getLightLinkLoadConstantDatumLis(cls, serverDic, ignorePath, ignoreNamespace):
        def getCountDic(dic):
            localCountDic, serverCountDic = {}, {}
            defaultSetLis = cls.getLightDefaultSetLis()
            if dic:
                localLightLis = []
                serverLightLis = []
                localObjectLis = []
                serverObjectLis = []
                for k, v in dic.items():
                    # Server Light
                    if not k in serverLightLis:
                        serverLightLis.append(k)
                    # Server Default Set
                    for ik, iv in v.items():
                        if isinstance(iv, bool):
                            serverCountDic.setdefault(ik, []).append(1)
                    #
                    nodeType, pathDatum, namespaceDatum = eval(k)
                    localLightNodeLis = cls.getNodeLisBySearchDatum(nodeType, pathDatum, namespaceDatum, ignorePath, ignoreNamespace)
                    if localLightNodeLis:
                        for lightNodePath in localLightNodeLis:
                            if not lightNodePath in localLightLis:
                                localLightLis.append(lightNodePath)
                            #
                            for ik, iv in v.items():
                                if isinstance(iv, bool):
                                    localDefaultSet = lightNodePath in defaultSetLis
                                    if iv == localDefaultSet:
                                        localCountDic.setdefault(ik, []).append(1)
                                else:
                                    localLightLinkObjectLis = cls.getLightLinkObjectLis(
                                        lightNodePath, *cls.MaAttrNameDic_LightLink[ik]
                                    )
                                    serverCountDic.setdefault(ik, []).append(len(iv))
                                    for i in iv:
                                        # Server Object
                                        if i not in serverObjectLis:
                                            serverObjectLis.append(i)
                                        #
                                        nodeType, pathDatum, namespaceDatum = eval(i)
                                        localObjectNodeLis = cls.getNodeLisBySearchDatum(nodeType, pathDatum, namespaceDatum, ignorePath, ignoreNamespace)
                                        for objectNodePath in localObjectNodeLis:
                                            # Local Object
                                            if not objectNodePath in localObjectLis:
                                                localObjectLis.append(objectNodePath)
                                            #
                                            if objectNodePath in localLightLinkObjectLis:
                                                localCountDic.setdefault(ik, []).append(1)
                    #
                    serverCountDic['light'] = [len(serverLightLis)]
                    localCountDic['light'] = [len(localLightLis)]
                    #
                    serverCountDic['object'] = [len(serverObjectLis)]
                    localCountDic['object'] = [len(localObjectLis)]
            return serverCountDic, localCountDic
        #
        def getMain():
            serverCountDic, localCountDic = getCountDic(serverDic)
            for k, v in configDic.items():
                if k in serverCountDic:
                    serverCount = sum(serverCountDic[k])
                else:
                    serverCount = 0
                #
                if k in localCountDic:
                    localCount = sum(localCountDic[k])
                else:
                    localCount = 0
                #
                lis.append(
                    (v, serverCount, localCount)
                )
        #
        lis = []
        #
        configDic = cls.maAttrPrettifyNameDic_lightLink()
        #
        getMain()
        return lis


#
class MaFileMethod(_maConfig.MaConfig):
    app_method = _maMethodBasic.Mtd_AppMaya
    plf_file_method = _osMethod.OsFileMethod

    MayaAsciiType = 'mayaAscii'
    MayaBinaryType = 'mayaBinary'
    AlembicType = 'Alembic'
    #
    FileTypeDic = {
        '.ma': MayaAsciiType,
        '.mb': MayaBinaryType,
        '.abc': AlembicType
    }
    #
    MaFileExportAllOption = 'exportAll'
    MaFileExportSelectedOption = 'exportSelected'
    #
    MaFileConstructionHistoryOption = 'constructionHistory'
    MaFileShaderOption = 'shader'
    #
    MaFileExportSelectedOptions = [
        MaFileConstructionHistoryOption,
        MaFileShaderOption
    ]
    MaDefFileExportKwargs = dict(
        type='mayaAscii',
        options='v=0',
        force=True,
        defaultExtensions=True,
        exportAll=True,
        preserveReferences=False,
    )
    MaDefFileImportKwargs = dict(
        options='v=0;',
        type='mayaAscii',
        i=True,
        renameAll=True,
        mergeNamespacesOnClash=True,
        namespace=':',
        preserveReferences=True
    )
    @classmethod
    def getFileType(cls, fileString):
        """
        :param fileString: str or unicode
        :return: str or unicode
        """
        ext = cls.plf_file_method.getOsFileExt(fileString)
        return cls.FileTypeDic.get(ext, cls.MayaAsciiType)
    @classmethod
    def fileExportCommand(cls, fileString, optionKwargs=None):
        if optionKwargs is None:
            optionKwargs = cls.MaDefFileExportKwargs.copy()
        #
        optionKwargs['type'] = cls.getFileType(fileString)
        #
        cmds.file(fileString, **optionKwargs)
    @classmethod
    def fileImportCommand(cls, fileString, optionKwargs=None):
        if optionKwargs is None:
            optionKwargs = cls.MaDefFileImportKwargs.copy()
        #
        optionKwargs['type'] = cls.getFileType(fileString)
        #
        cmds.file(
            fileString,
            **optionKwargs
        )
    @classmethod
    def setFileImport(cls, fileString, namespace=':'):
        optionKwargs = cls.MaDefFileImportKwargs.copy()
        #
        optionKwargs['type'] = cls.getFileType(fileString)
        optionKwargs['namespace'] = namespace
        #
        cmds.file(
            fileString,
            **optionKwargs
        )


#
class MaTextureNodeMethod(_maMethodBasic.MaNodeMethodBasic):
    pass


#
class MaTextureFileMethod(_maMethodBasic.Mtd_AppMaya, _methodBasic.Mtd_PlfFile):
    MaTexture_NodeTypeLis = [
        'file',
        'aiImage',
        'RedshiftNormalMap',
        'RedshiftCameraMap'
    ]
    #
    MaTexture_AttrNameLis = [
        'fileTextureName',
        'filename',
        'tex0'
    ]
    #
    MaTexture_AttrNameDic = {
        'file': 'fileTextureName',
        'aiImage': 'filename',
        'RedshiftNormalMap': 'tex0',
        'RedshiftCameraMap': 'tex0'
    }
    @classmethod
    def isTextureNode(cls, node):
        nodeType = cls.getNodeType(node)
        if nodeType in cls.MaTexture_NodeTypeLis:
            boolean = True
        else:
            boolean = False
        return boolean
    @classmethod
    def getTextureNodeLis(cls):
        return cls.getNodeLisByType(cls.MaTexture_NodeTypeLis)
    @classmethod
    def getTextureNodeLisByNamespace(cls, namespace):
        return cls.getNodeLisByFilter(cls.MaTexture_NodeTypeLis, namespace)
    @classmethod
    def getTextureNodeLisByObject(cls, objectString):
        pass
    #
    def getTextureLis(self, textureNode=None):
        pass


#
class MaPreviewFileMethod(_maMethodBasic.Mtd_AppMaya, _methodBasic.Mtd_PlfFile):
    MaPlayblastFormatLis = [
        'qt',
        'avi',
        'image',
        'iff'
    ]
    MaDefPreviewOptionKwargs = dict(
        startTime=1,
        endTime=1,
        framePadding=4,
        widthHeight=(1280, 720),
        format='iff',
        compression='jpg',
        percent=100,
        quality=100,
        clearCache=True,
        viewer=False,
        sequenceTime=False,
        showOrnaments=False,
        offScreen=True
    )
    @classmethod
    def previewExportCommand(cls, fileString, optionKwargs=None):
        fileBase, ext = cls.toOsFileSplitByExt(fileString)
        if optionKwargs is None:
            optionKwargs = cls.MaDefPreviewOptionKwargs.copy()
        #
        cmds.playblast(
            filename=fileBase,
            **optionKwargs
        )


#
class MaCameraMethod(object):
    pass
