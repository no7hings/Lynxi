# coding=utf-8
import os
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import pymel.core as core

from LxBasic import bscMethods, bscObjects
#
from LxCore import lxBasic, lxConfigure
#
from LxCore.config import appCfg
#
from LxCore.preset import appVariant, databasePr
#
from LxCore.preset.prod import assetPr
#
from LxDatabase import dbGet, dbBasic
#
from LxMaya.command import maUtils, maGeom, maAttr, maFur, maShdr, maTxtr, maUuid
#
none = ''


# Get Poly Mesh Evaluate ( Method )
def getMeshObjectEvaluate(objectLis, vertex, edge, face, triangle, uvcoord, area, worldArea, shell, boundingBox, showMode):
    # Dict { <Evaluate Name>: <Evaluate Data> }
    dic = lxBasic.orderedDict()
    used = [vertex, edge, face, triangle, uvcoord, area, worldArea, shell, boundingBox]
    # View Progress
    progressExplain = '''Read Mesh Evaluate Data'''
    maxValue = sum(used)
    progressBar = bscObjects.If_Progress(progressExplain, maxValue)
    # >>>> 01
    if vertex:
        progressBar.update('Vertex')
        dic['vertex'] = cmds.polyEvaluate(objectLis, vertex=1)
    # >>>> 02
    if edge:
        progressBar.update('Edge')
        dic['edge'] = cmds.polyEvaluate(objectLis, edge=1)
    # >>>> 03
    if face:
        progressBar.update('Face')
        dic['face'] = cmds.polyEvaluate(objectLis, face=1)
    # >>>> 04
    if triangle:
        progressBar.update('Triangle')
        dic['triangle'] = cmds.polyEvaluate(objectLis, triangle=1)
    # >>>> 05
    if uvcoord:
        progressBar.update('UV')
        dic['uvcoord'] = cmds.polyEvaluate(objectLis, uvcoord=1)
    # >>>> 06
    if area:
        progressBar.update('Area')
        dic['area'] = cmds.polyEvaluate(objectLis, area=1)
    # >>>> 07
    if worldArea:
        progressBar.update('World Area')
        dic['worldArea'] = cmds.polyEvaluate(objectLis, worldArea=1)
    # >>>> 08
    if shell:
        progressBar.update('Shell')
        dic['shell'] = cmds.polyEvaluate(objectLis, shell=1)
    # >>>> 09
    if boundingBox:
        progressBar.update('Bounding Box')
        dic['boundingBox'] = cmds.polyEvaluate(objectLis, boundingBox=1)
    return dic


#
def getAssetIndex(assetName):
    string = none
    #
    rootGroup = assetPr.astUnitRootGroupName(assetName)
    #
    if maUtils.isAppExist(rootGroup):
        data = maUtils.getAttrDatum(rootGroup, appVariant.basicIndexAttrLabel)
        if data:
            string = data
    return string


#
def getAssetInfo():
    lis = []
    keyword = appVariant.basicUnitRootGroupLabel + appVariant.basicGroupLabel
    rootGroups = cmds.ls('*%s' % keyword)
    if rootGroups:
        for rootGroup in rootGroups:
            if maUtils.isAppExist(rootGroup):
                if rootGroup.startswith(appVariant.Lynxi_Prefix_Product_Asset):
                    assetClass = maUtils.getAttrDatum(rootGroup, appVariant.basicClassAttrLabel)
                    assetName = maUtils.getAttrDatum(rootGroup, appVariant.basicNameAttrLabel)
                    assetVariant = maUtils.getAttrDatum(rootGroup, appVariant.basicVariantAttrLabel)
                    assetStage = maUtils.getAttrDatum(rootGroup, appVariant.basicStageAttrLabel)
                    assetIndex = maUtils.getAttrDatum(rootGroup, appVariant.basicIndexAttrLabel)
                    if assetIndex is not None:
                        data = assetIndex, assetClass, assetName, assetVariant, assetStage
                        #
                        print '''assetIndex = '{}'\nassetClass = '{}'\nassetName = '{}'\nassetVariant = '{}'\nassetStage = '{}'\n'''.format(
                            assetIndex,
                            assetClass, assetName, assetVariant, assetStage
                        )
                        lis.append(data)
    return lis


# Get Nde_Geometry ( Data )
def getAstMeshObjects(assetName, key=0, namespace=none):
    # List [ <Nde_Geometry(Transfer)> ]
    meshObjects = []
    astModelGroup = assetPr.astUnitModelLinkGroupName(assetName, namespace)
    astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName, namespace)
    #
    root = none
    if key == 0 and maUtils.isAppExist(astModelGroup):
        root = astModelGroup
    elif key == 0 and not maUtils.isAppExist(astModelGroup) and maUtils.isAppExist(astUnitModelProductGroup):
        root = astUnitModelProductGroup
    elif key == 1 and maUtils.isAppExist(astUnitModelProductGroup):
        root = astUnitModelProductGroup
    #
    if maUtils.isAppExist(root):
        meshObjects = maGeom.getMeshObjectsByGroup(root)
    return meshObjects


#
def getAstGeometryObjects(assetName, namespace=none):
    astModelGroup = assetPr.astUnitModelLinkGroupName(assetName, namespace)
    return maGeom.getGeometryObjectsByGroup(astModelGroup)


# Get Instance In Check Objects( Data )
def getInstanceObjectLis(objectLis):
    # List [ <Instance Nde_Geometry> ]
    lis = [i for i in objectLis if core.nodetypes.Shape(maUtils.getNodeShape(i, 1)).isInstanced()]
    return lis


#
def getMeshesIsNormalLock(meshObjects):
    lis = [i for i in meshObjects if maGeom.getMeshObjectIsNormalLocked(i)]
    return lis


# Get Error Shape Name
def getObjectsShapeIsErrorNaming(objectLis, shapeSet=appVariant.shapeSet[0]):
    # List [  <Shape Naming Error Nde_Geometry> ]
    lis = [i for i in objectLis if not maUtils.getNodeShape(i, 1).endswith(shapeSet)]
    return lis


# Get Poly Meshes's Evaluate ( Data )
def getMeshObjectsEvaluateDic(objectLis, showMode=0):
    # Dict { <Poly Mesh> :
    #        List [ <Evaluate Info> ] }
    dic = lxBasic.orderedDict()
    if objectLis:
        count = len(objectLis)
        data = getMeshObjectEvaluate(
            objectLis,
            vertex=1, edge=1, face=1, triangle=1, uvcoord=1, area=1, worldArea=1, shell=1, boundingBox=1,
            showMode=showMode
        )
        box = data['boundingBox']
        #
        dic['geometries'] = count
        dic['vertex'] = data['vertex']
        dic['edge'] = data['edge']
        dic['face'] = data['face']
        dic['triangle'] = data['triangle']
        dic['uvcoord'] = data['uvcoord']
        dic['area'] = data['area']
        dic['worldArea'] = data['worldArea']
        dic['shell'] = data['shell']
        dic['axisX'] = box[0][1] + box[0][0]
        dic['horz'] = box[1][0]
        dic['widthX'] = box[0][1] - box[0][0]
        dic['heightY'] = box[1][1] - box[1][0]
        dic['widthZ'] = box[2][1] - box[2][0]
    return dic


#
def getMaterialEvaluateData(objectLis, showMode=0):
    dic = lxBasic.orderedDict()
    if objectLis:
        evaluateData = maShdr.getMaterialEvaluateData(objectLis)
        #
        textureNodeLis = maShdr.getTextureNodeLisByObject(objectLis)
        textures = maTxtr.getTextureByTextureNodes(textureNodeLis)
        subEvaluateData = {'textureNode': len(textureNodeLis), 'texture': len(textures), 'averagePixel': 2048}
        #
        dic = evaluateData.copy()
        dic.update(subEvaluateData)
    return dic


# Get Objects Transformation (Data)
def getObjectNonZeroTransAttrDic(objectLis):
    dic = lxBasic.orderedDict()
    #
    channelLabel = [
        'translate',
        'rotate',
        'scale',
        'pivot'
    ]
    channelSet = [
        '.translate',
        '.rotate',
        '.scale',
        '.rotatePivot'
    ]
    if objectLis:
        for objectString in objectLis:
            subDic = lxBasic.orderedDict()
            for seq, channel in enumerate(channelSet):
                subDic[channelLabel[seq]] = cmds.getAttr(objectString + channel)[0]
                dic[objectString] = subDic
    return dic


#
def filterObjectHistoryNodeDic(objectLis):
    dic = lxBasic.orderedDict()
    if objectLis:
        for objectString in objectLis:
            stringLis = cmds.listHistory(objectString, pruneDagObjects=1)
            if stringLis:
                for i in stringLis:
                    typeData = cmds.ls(i, showType=1, long=1)
                    dic.setdefault(objectString, []).append(typeData)
    return dic


# List [ <Output Connection Nde_Node> ]
def getOutputNode(node, assetClass=none):
    outputNodes = cmds.listConnections(node, destination=1, source=0, type=assetClass)
    return outputNodes


# Get Arnold's Aov
def getArnoldAovNodeLis():
    # List [ <Aov> ]
    arnoldAovs = []
    if maUtils.isRedshiftEnable():
        arnoldAovs = maUtils.getInputNodes('defaultArnoldRenderOptions', 'aiAOV')
    return arnoldAovs


# Get Redshift's Aov
def getRedshiftAovNodes():
    # List [ <Aov> ]
    redshiftAovs = []
    if maUtils.isRedshiftEnable():
        redshiftAovs = maUtils.getNodeLisByType('RedshiftAOV')
    return redshiftAovs


#
def getAovNodesData(renderer):
    aovNodesData = lxBasic.orderedDict()
    if renderer == 'Arnold':
        aovNodesData = getArnoldAovNodesData()
    if renderer == 'Redshift':
        aovNodesData = getRedshiftAovNodesData()
    return aovNodesData


#
def getArnoldAovNodesData():
    dic = lxBasic.orderedDict()
    aovNodes = getArnoldAovNodeLis()
    if aovNodes:
        for aovNode in aovNodes:
            aovName = maUtils.getAttrDatum(aovNode, 'name')
            dic[aovNode] = aovName
    return dic


#
def getRedshiftAovNodesData():
    dic = lxBasic.orderedDict()
    aovNodes = getRedshiftAovNodes()
    if aovNodes:
        for aovNode in aovNodes:
            aovName = maUtils.getAttrDatum(aovNode, 'name')
            dic[aovNode] = aovName
    return dic


# Get Objects Shading Group
def getShadingGroupsByObjects(objectLis):
    # List [ <Shading Engine> ]
    lis = []
    MaDefShadingEngineLis = ['initialShadingGroup', 'initialParticleSE', 'defaultLightSet', 'defaultObjectSet']
    for objectString in objectLis:
        shape = maUtils.getNodeShape(objectString, 1)
        shadingGroups = getOutputNode(shape, 'shadingEngine')
        if shadingGroups:
            [lis.append(shadingGroup) for shadingGroup in shadingGroups if shadingGroup not in MaDefShadingEngineLis]

    lisR = lxBasic.getReduceList(lis)
    lisR.sort()
    return lisR


#
def getAstUnitModelExtraData(assetName, namespace=none):
    extraData = {
        lxConfigure.LynxiAttributeDataKey: getAstUnitModelBridgeAttrData(assetName, namespace),
        lxConfigure.LynxiConnectionDataKey: getAstUnitModelReferenceConnectionData(assetName, namespace)
    }
    return extraData


#
def getAstUnitModelBridgeAttrData(assetName, namespace=none):
    def getBranch(objectString):
        objectDefinedAttrData = maAttr.getNodeDefAttrDatumLis(objectString)
        objectCustomAttrData = maAttr.getNodeUserDefAttrData(objectString)
        dic[astUnitModelBridgeGroup + objectString.split(astUnitModelBridgeGroup)[-1]] = objectDefinedAttrData, objectCustomAttrData
    #
    dic = {}
    #
    astUnitModelBridgeGroup = assetPr.astUnitModelBridgeGroupName(assetName, namespace)
    if maUtils.isAppExist(astUnitModelBridgeGroup):
        getBranch(astUnitModelBridgeGroup)
    return dic


#
def getAstUnitModelReferenceConnectionData(assetName, namespace=none):
    def getBranch(objectString):
        objectShape = maUtils.getNodeShape(objectString)
        outputConnectLis = maUtils.getNodeOutputConnectionLis(objectShape)
        if outputConnectLis:
            for sourceAttr, targetAttr in outputConnectLis:
                if sourceAttr.endswith('.message') and targetAttr.endswith('.referenceObject'):
                    dic.setdefault(objectString.split(astUnitRoot)[-1], []).append((sourceAttr, targetAttr))
        #
        objectShapeName = maUtils._toNodeName(objectShape)
        maUtils.setAttrStringDatumForce_(objectString, lxConfigure.LynxiObjectShapeNameAttrName, objectShapeName)
    #
    dic = {}
    #
    astUnitRoot = assetPr.astUnitRootGroupName(assetName)
    astUnitModelReferenceGroup = assetPr.astUnitModelReferenceGroupName(assetName, namespace)
    #
    objectLis = maUtils.getChildObjectsByRoot(astUnitModelReferenceGroup, appCfg.MaNodeType_Mesh)
    if objectLis:
        # View Progress
        progressExplain = u'''Read Connection Data'''
        maxValue = len(objectLis)
        progressBar = bscObjects.If_Progress(progressExplain, maxValue)
        for i in objectLis:
            progressBar.update()
            getBranch(i)
    return dic


#
def getAstUnitRigExtraData(assetName):
    astUnitRigBridgeGroup = assetPr.astUnitRigBridgeGroupName(assetName)
    alembicAttrData = getAstAlembicAttrData(astUnitRigBridgeGroup)
    extraData = {
        lxConfigure.LynxiAlembicAttrDataKey: alembicAttrData
    }
    return extraData


#
def getAstAlembicAttrData(root):
    lis = []
    children = maUtils.getRootCompose(root)
    if children:
        for i in children:
            data = maAttr.getNodeUserDefAttrNameLis(i)
            if data:
                lis.extend(data)
    return lis


#
def getFurObjects(assetName, namespace=none):
    lis = []
    yetiObjects = getYetiObjects(assetName, namespace)
    lis.extend(yetiObjects)
    pfxHairObjects = getPfxHairObjects(assetName, namespace)
    lis.extend(pfxHairObjects)
    nurbsHairObjects = getAstCfxNurbsHairObjects(assetName, namespace)
    lis.extend(nurbsHairObjects)
    return lis


#
def getAstFurShaderObjects(assetName, namespace=none):
    lis = []
    yetiObjects = getYetiObjects(assetName, namespace)
    lis.extend(yetiObjects)
    nurbsHairObjects = getAstCfxNurbsHairObjects(assetName, namespace)
    lis.extend(nurbsHairObjects)
    return lis


# Get Yeti Nde_Node
def getYetiObjects(assetName, namespace=none):
    maGroup = assetPr.yetiNodeGroupName(assetName, namespace)
    yetiObjects = maUtils.getChildObjectsByRoot(maGroup, 'pgYetiMaya', fullPath=True)
    return yetiObjects


# Get Yeti Nde_Node
def getYetiShapeLis(assetName, namespace=none):
    maGroup = assetPr.yetiNodeGroupName(assetName, namespace)
    yetiNodes = maUtils.getChildShapesByRoot(maGroup, 'pgYetiMaya', 1)
    return yetiNodes


#
def getPfxHairObjects(assetName, namespace=none):
    maGroup = assetPr.astPfxHairNodeGroupName(assetName, namespace)
    pfxHairObjects = maUtils.getChildObjectsByRoot(maGroup, 'pfxHair', fullPath=True)
    return pfxHairObjects


#
def getAstCfxGrowSourceObjectLis(assetName, namespace=none):
    groupName = assetPr.astUnitCfxGrowSourceObjectGroupName(assetName, namespace)
    return maUtils.getNodeChildLis(groupName)


#
def getAstCfxGrowSourceConnectionDic(assetName, namespace=none):
    dic = lxBasic.orderedDict()
    objectPathLis = getAstCfxGrowSourceObjectLis(assetName, namespace)
    if objectPathLis:
        for objectString in objectPathLis:
            sourceObject = maUtils.getAttrDatum(objectString, 'growSource')
            dic[sourceObject] = objectString
    return dic


#
def getAstSolverGrowSourceObjectLis(assetName, namespace):
    groupName = assetPr.astUnitSolverGrowSourceObjectGroupName(assetName, namespace)
    return maUtils.getNodeChildLis(groupName)


#
def getAstSolverGrowSourceConnectionDic(assetName, namespace=none):
    dic = lxBasic.orderedDict()
    objectPathLis = getAstSolverGrowSourceObjectLis(assetName, namespace)
    if objectPathLis:
        for objectString in objectPathLis:
            sourceObject = maUtils.getAttrDatum(objectString, 'growSource')
            dic[sourceObject] = objectString
    return dic


# Get Yeti Nde_Node Data
def getYetiNodeData(assetClass, assetName):
    dic = lxBasic.orderedDict()
    yetiObjects = getYetiObjects(assetName)
    if yetiObjects:
        for yetiObject in yetiObjects:
            subDic = lxBasic.orderedDict()
            groomObjects = maUtils.getYetiGroomDic(yetiObject)
            if groomObjects:
                for groomObject in groomObjects:
                    subDic.setdefault('groom', []).append(groomObject)
            # Grow
            growObjects = maUtils.getYetiGrowDic(yetiObject)
            if growObjects:
                for growObject in growObjects:
                    subDic.setdefault('grow', []).append(growObject)
                    # Reference
                    referenceObjects = maUtils.getYetiRefObject(growObject)
                    if referenceObjects:
                        for referenceObject in referenceObjects:
                            subDic.setdefault('reference', []).append('%s|%s' % (growObject, referenceObject))
            # Map
            mapObjects = maUtils.getYetiMapDic(yetiObject)
            if mapObjects:
                for mapObject in mapObjects:
                    subDic.setdefault('map', []).append(mapObject)
            dic[yetiObject] = subDic
    return dic


#
def getAstCfxNurbsHairObjects(assetName, namespace=none):
    maGroup = assetPr.astCfxNurbsHairNodeGroupName(assetName, namespace)
    return maUtils.getChildObjectsByRoot(maGroup, appCfg.MaNodeType_Plug_NurbsHair)


#
def getAstCfxNurbsHairSolverCheckData(assetName, namespace=none):
    dic = lxBasic.orderedDict()
    objectPaths = getAstCfxNurbsHairObjects(assetName, namespace)
    if objectPaths:
        for objectPath in objectPaths:
            dic[objectPath] = maFur.isNhrHasSolGuideObject(objectPath)
    return dic


#
def getAstUnitSolverNhrGuideObjects(assetName, namespace=none):
    groupStr = assetPr.astUnitRigSolNhrGuideObjectGroupName(assetName, namespace)
    if maUtils.isAppExist(groupStr):
        maUtils.setNodeOutlinerRgb(groupStr, 1, .5, 1)
    return maUtils.getChildObjectsByRoot(groupStr, appVariant.maNurbsHairInGuideCurvesNode, fullPath=True)


#
def getAstUnitCfxNhrGuideObjects(assetName, namespace=none):
    groupStr = assetPr.astUnitCfxNhrGuideObjectGroupName(assetName, namespace)
    if maUtils.isAppExist(groupStr):
        maUtils.setNodeOutlinerRgb(groupStr, 1, .25, .25)
    return maUtils.getChildObjectsByRoot(groupStr, [appCfg.MaNodeType_Mesh, appCfg.MaNodeType_NurbsSurface, appCfg.MaNodeType_NurbsCurve], fullPath=True)


#
def getAstSolverFurGuideCurveGroups(assetName, namespace=none):
    maGroup = assetPr.astUnitRigSolNhrCurveObjectGroupName(assetName, namespace)
    return maUtils.getChildGroupLisByGroup(maGroup, fullPath=True)


#
def getAstSolverGuideCheckData(assetName, namespace=none):
    dic = lxBasic.orderedDict()
    nhrGuideObjects = getAstUnitSolverNhrGuideObjects(assetName, namespace)
    if nhrGuideObjects:
        for nhrGuideObject in nhrGuideObjects:
            dic[nhrGuideObject] = maFur.getNhrObjectsByGuide(nhrGuideObject)
    return dic


#
def getAstUnitRigSolExtraData(assetName, namespace=none):
    dic = {
        lxConfigure.LynxiConnectionDataKey: getAstUnitSolverConnectionData(assetName, namespace),
        lxConfigure.LynxiNhrConnectionDataKey: getAstUnitSolverNhrConnectionData(assetName, namespace)
    }
    return dic


#
def getAstUnitSolverConnectionData(assetName, namespace=none):
    def getBranch(objectString):
        objectShape = maUtils.getNodeShape(objectString)
        inputConnections = maUtils.getNodeInputConnectionLis(objectShape)
        if inputConnections:
            for sourceAttr, targetAttr in inputConnections:
                dic.setdefault(objectString.split(astUnitRoot)[-1], []).append((sourceAttr, targetAttr))
        #
        outputConnectLis = maUtils.getNodeOutputConnectionLis(objectShape)
        if outputConnectLis:
            for sourceAttr, targetAttr in outputConnectLis:
                dic.setdefault(objectString.split(astUnitRoot)[-1], []).append((sourceAttr, targetAttr))
    #
    dic = {}
    #
    astUnitRoot = assetPr.astUnitRootGroupName(assetName)
    #
    objectStrings = getAstUnitSolverNhrGuideObjects(assetName, namespace)
    if objectStrings:
        # View Progress
        progressExplain = u'''Read Connection Data'''
        maxValue = len(objectStrings)
        progressBar = bscObjects.If_Progress(progressExplain, maxValue)
        for i in objectStrings:
            progressBar.update()
            getBranch(i)
    return dic


#
def getAstUnitSolverNhrConnectionData(assetName, namespace=none):
    def getBranch(objectString):
        objectShape = maUtils.getNodeShape(objectString)
        outputConnectLis = maUtils.getNodeOutputConnectionLis(objectShape)
        if outputConnectLis:
            for sourceAttr, targetAttr in outputConnectLis:
                if sourceAttr.endswith('.message') and targetAttr.endswith('.scatterObj'):
                    dic.setdefault(objectString.split(astUnitRoot)[-1], []).append((sourceAttr, targetAttr))
    #
    dic = {}
    #
    astUnitRoot = assetPr.astUnitRootGroupName(assetName)
    #
    objectStrings = getAstUnitCfxNhrGuideObjects(assetName, namespace)
    if objectStrings:
        # View Progress
        progressExplain = u'''Read Connection Data'''
        maxValue = len(objectStrings)
        progressBar = bscObjects.If_Progress(progressExplain, maxValue)
        for i in objectStrings:
            progressBar.update()
            getBranch(i)
    #
    return dic


#
def getAstUnitRigSolAttributeData(assetName, namespace=none):
    def getBranch(objectString):
        shapePath = maUtils.getNodeShape(objectString)
        shapeDefinedAttrData = maAttr.getNodeDefAttrDatumLis(shapePath)
        shapeCustomAttrData = maAttr.getNodeUserDefAttrData(objectString)
        dic[rigSolLinkGroup + objectString.split(rigSolLinkGroup)[-1]] = shapeDefinedAttrData, shapeCustomAttrData
    #
    dic = lxBasic.orderedDict()
    rigSolLinkGroup = assetPr.astUnitRigSolFurSubGroupName(assetName)
    #
    objectPaths = getAstUnitSolverNhrGuideObjects(assetName, namespace)
    if objectPaths:
        [getBranch(i) for i in objectPaths]

    return dic


#
def getTextureDatumLis(textureNode, textureString, texturePathDic, textureNodeDic, textureMtimestampDic):
    if textureString:
        textureFilePath = lxBasic.getOsFileDirname(textureString)
        #
        textureFileBasename = lxBasic.getOsFileBasename(textureString)
        # Texture Path
        texturePathDic.setdefault(textureFilePath, []).append(textureFileBasename)
        #
        if '<udim>' in textureString.lower():
            subTextureFileLis = maTxtr.getOsTextureUdimLis(textureString)
            if subTextureFileLis:
                subTextureDatumLis = []
                for subTextureFile in subTextureFileLis:
                    subTextureFileBasename = os.path.basename(subTextureFile)
                    timestamp = lxBasic.getOsFileMtimestamp(subTextureFile)
                    if not (subTextureFileBasename, timestamp) in subTextureDatumLis:
                        subTextureDatumLis.append((subTextureFileBasename, timestamp))
                #
                textureMtimestampDic[textureFileBasename] = subTextureDatumLis
            else:
                textureMtimestampDic[textureFileBasename] = None
        elif '<f>' in textureString.lower():
            subTextureFileLis = maTxtr.getOsTextureSequenceLis(textureString)
            if subTextureFileLis:
                subTextureDatumLis = []
                for subTextureFile in subTextureFileLis:
                    subTextureFileBasename = os.path.basename(subTextureFile)
                    timestamp = lxBasic.getOsFileMtimestamp(subTextureFile)
                    if not (subTextureFileBasename, timestamp) in subTextureDatumLis:
                        subTextureDatumLis.append((subTextureFileBasename, timestamp))
                #
                textureMtimestampDic[textureFileBasename] = subTextureDatumLis
            else:
                textureMtimestampDic[textureFileBasename] = None
        else:
            if lxBasic.isOsExistsFile(textureString):
                timestamp = lxBasic.getOsFileMtimestamp(textureString)
                textureMtimestampDic[textureFileBasename] = timestamp
            else:
                textureMtimestampDic[textureFileBasename] = None
        # Texture Nde_Node
        textureNodeDic.setdefault(textureFileBasename, []).append(textureNode)


# Get Texture's Datum List Link
def getTextureStatisticsDic(objectLis):
    dic = lxBasic.orderedDict()
    #
    texturePathDic = lxBasic.orderedDict()
    #
    textureMtimestampDic = lxBasic.orderedDict()
    textureNodeDic = lxBasic.orderedDict()
    #
    textureNodeLis = maShdr.getTextureNodeLisByObject(objectLis)
    if textureNodeLis:
        # View Progress
        progressExplain = '''Read Data'''
        maxValue = len(textureNodeLis)
        progressBar = bscObjects.If_Progress(progressExplain, maxValue)
        for textureNode in textureNodeLis:
            # In Progress
            progressBar.update()
            textureString = maTxtr.getTextureNodeAttrData(textureNode)
            getTextureDatumLis(textureNode, textureString, texturePathDic, textureNodeDic, textureMtimestampDic)
    #
    for k, v in texturePathDic.items():
        for i in lxBasic.getReduceList(v):
            dic.setdefault(k, []).append((i, textureMtimestampDic[i], textureNodeDic[i]))
    return dic


# Str <Object's Volume>
def getVolume(objectString):
    box = cmds.polyEvaluate(objectString, boundingBox=1)
    volume = (box[0][1] - box[0][0]) * (box[1][1] - box[1][0]) * (box[2][1] - box[2][0])
    return volume


#
def getMeshObjectsConstantDic(assetName, namespace=none):
    infoConfig = ['hierarchy', 'geometry', 'geometryShape', 'map', 'mapShape']
    dic = lxBasic.orderedDict()
    astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName, namespace)
    meshesInformation = maGeom.getGeometryObjectsInfo(astUnitModelProductGroup)
    for seq, i in enumerate(infoConfig):
        dic[i] = meshesInformation[seq]
    return dic


#
def getMeshConstant(uniqueId, localInfoDic, serverInfoDic):
    pathCheck = False
    geomCheck = False
    geomShapeCheck = False
    mapCheck = False
    mapShapeCheck = False
    if uniqueId in localInfoDic.keys() and uniqueId in serverInfoDic:
        localInfos = localInfoDic[uniqueId]
        serverInfos = serverInfoDic[uniqueId]
        pathCheck = localInfos[0] == serverInfos[0]
        geomCheck = localInfos[1] == serverInfos[1]
        geomShapeCheck = localInfos[2] == serverInfos[2]
        mapCheck = localInfos[3] == serverInfos[3]
        mapShapeCheck = localInfos[4] == serverInfos[4]
    return pathCheck, geomCheck, geomShapeCheck, mapCheck, mapShapeCheck


#
def getAstGeometryObjectsConstantData(assetIndex, assetClass, assetName, namespace):
    totalArray = []
    pathChangedArray = []
    geomChangedArray = []
    geomShapeChangedArray = []
    mapChangedArray = []
    mapShapeChangedArray = []
    #
    meshRoot = assetPr.astUnitModelLinkGroupName(assetName, namespace)
    if maUtils.isAppExist(meshRoot):
        localInfoDic = maGeom.getGeometryObjectsInfoDic(meshRoot)
        #
        serverInfoDic = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
        #
        if localInfoDic and serverInfoDic:
            unionUniqueInfoDic = localInfoDic.copy()
            unionUniqueInfoDic.update(serverInfoDic)
            # View Progress
            progressExplain = '''Read Asset ( Mesh ) Data'''
            maxValue = len(unionUniqueInfoDic)
            progressBar = bscObjects.If_Progress(progressExplain, maxValue)
            for uniqueId in unionUniqueInfoDic:
                progressBar.update()
                #
                totalArray.append(uniqueId)
                pathCheck, geomCheck, geomShapeCheck, mapCheck, mapShapeCheck = getMeshConstant(uniqueId, localInfoDic, serverInfoDic)
                if not pathCheck:
                    pathChangedArray.append(uniqueId)
                if not geomCheck:
                    geomChangedArray.append(uniqueId)
                if not geomShapeCheck:
                    geomShapeChangedArray.append(uniqueId)
                if not mapCheck:
                    mapChangedArray.append(uniqueId)
                if not mapShapeCheck:
                    mapShapeChangedArray.append(uniqueId)
    #
    return totalArray, pathChangedArray, geomChangedArray, geomShapeChangedArray, mapChangedArray, mapShapeChangedArray


#
def getAstMeshObjectsConstantData(assetIndex, assetClass, assetName, namespace):
    totalArray = []
    pathChangedArray = []
    geomChangedArray = []
    geomShapeChangedArray = []
    mapChangedArray = []
    mapShapeChangedArray = []
    #
    meshRoot = assetPr.astUnitModelLinkGroupName(assetName, namespace)
    if maUtils.isAppExist(meshRoot):
        localInfoDic = maGeom.getMeshObjectsInfoDic(meshRoot)
        #
        serverInfoDic = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
        #
        if localInfoDic and serverInfoDic:
            unionUniqueInfoDic = localInfoDic.copy()
            unionUniqueInfoDic.update(serverInfoDic)
            # View Progress
            progressExplain = '''Read Asset ( Mesh ) Data'''
            maxValue = len(unionUniqueInfoDic)
            progressBar = bscObjects.If_Progress(progressExplain, maxValue)
            for uniqueId in unionUniqueInfoDic:
                progressBar.update()
                #
                totalArray.append(uniqueId)
                pathCheck, geomCheck, geomShapeCheck, mapCheck, mapShapeCheck = getMeshConstant(uniqueId, localInfoDic,
                                                                                                serverInfoDic)
                if not pathCheck:
                    pathChangedArray.append(uniqueId)
                if not geomCheck:
                    geomChangedArray.append(uniqueId)
                if not geomShapeCheck:
                    geomShapeChangedArray.append(uniqueId)
                if not mapCheck:
                    mapChangedArray.append(uniqueId)
                if not mapShapeCheck:
                    mapShapeChangedArray.append(uniqueId)
    #
    return totalArray, pathChangedArray, geomChangedArray, geomShapeChangedArray, mapChangedArray, mapShapeChangedArray


#
def getObjectSetDic(data):
    dic = lxBasic.orderedDict()
    if data:
        for objectUniqueId, linkDataArray in data.items():
            for objIndex, materialUniqueId in linkDataArray:
                dic.setdefault(materialUniqueId, []).append(objectUniqueId + objIndex)
    return dic


#
def getLocalMeshSetData(objectLis):
    data = maShdr.getShaderObjectsObjSetDic(objectLis)
    return getObjectSetDic(data)


#
def getServerMeshSetData(projectName, assetName, assetVariant):
    assetIndex = getAssetIndex(assetName)
    uniqueIds = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
    modelIndexKey = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
    directory = databasePr.dbAstMaterialObjSetUnitDirectory()
    data = dbBasic.dbCompDatumDicRead(uniqueIds, modelIndexKey, directory)
    return getObjectSetDic(data)


#
def setMaterialConstant(uniqueId, localInfoDic, serverInfoDic, localMeshSetData, serverMeshSetData):
    composeCheck = False
    attributeCheck = False
    relationCheck = False
    objectSetCheck = False
    if uniqueId in localInfoDic.keys() and uniqueId in serverInfoDic:
        localInfos = localInfoDic[uniqueId]
        serverInfos = serverInfoDic[uniqueId]
        composeCheck = localInfos[0] == serverInfos[0]
        attributeCheck = localInfos[1] == serverInfos[1]
        relationCheck = localInfos[2] == serverInfos[2]
    if uniqueId in localMeshSetData.keys() and uniqueId in serverMeshSetData:
        localMeshSet = localMeshSetData[uniqueId]
        serverMeshSet = serverMeshSetData[uniqueId]
        localMeshSet.sort()
        serverMeshSet.sort()
        objectSetCheck = localMeshSet == serverMeshSet
    return composeCheck, attributeCheck, relationCheck, objectSetCheck


#
def getMaterialsConstantData(assetIndex, projectName, assetClass, assetName, assetVariant, namespace=none):
    totalArray = []
    composeChangedArray = []
    attributeChangedArray = []
    relationChangedArray = []
    objectSetChangedArray = []
    #
    shaderGeomObjects = getAstMeshObjects(assetName, 1)
    materials = maShdr.getObjectsMaterials(shaderGeomObjects)
    localInfoDic = maShdr.getMaterialsInformationData(materials)
    modelIndexKey = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
    serverInfoDic = dbGet.getDbMaterialIndexData(modelIndexKey)
    localMeshSetData = getLocalMeshSetData(shaderGeomObjects)
    serverMeshSetData = getServerMeshSetData(projectName, assetName, assetVariant)
    #
    if localInfoDic and serverInfoDic:
        unionUniqueInfoData = localInfoDic.copy()
        unionUniqueInfoData.update(serverInfoDic)
        # View Progress
        progressExplain = '''Read Data'''
        maxValue = len(unionUniqueInfoData)
        progressBar = bscObjects.If_Progress(progressExplain, maxValue)
        for uniqueId in unionUniqueInfoData:
            progressBar.update()
            #
            totalArray.append(uniqueId)
            composeCheck, attributeCheck, relationCheck, objectSetCheck = setMaterialConstant(uniqueId, localInfoDic, serverInfoDic, localMeshSetData, serverMeshSetData)
            if not composeCheck:
                composeChangedArray.append(uniqueId)
            if not attributeCheck:
                attributeChangedArray.append(uniqueId)
            if not relationCheck:
                relationChangedArray.append(uniqueId)
            if not objectSetCheck:
                objectSetChangedArray.append(uniqueId)
    #
    return totalArray, composeChangedArray, attributeChangedArray, relationChangedArray, objectSetChangedArray


#
def getErrorTransforms(assetName):
    lis = []
    #
    group = assetPr.astUnitModelLinkGroupName(assetName)
    #
    transforms = maUtils.getChildTransformLisByGroup(group)
    for transform in transforms:
        mainShapes = maUtils.getMainShapes(transform)
        if not mainShapes:
            lis.append(transform)
    return lis


#
def getMeshesCompIndexForce(assetIndex, meshObjects):
    uniqueIds = []
    if meshObjects:
        for mesh in meshObjects:
            uniqueId = maUuid.getNodeUniqueId(mesh)
            uniqueIds.append(uniqueId)
    #
    if uniqueIds:
        nonExistsUniqueIds = dbGet.getNonExistsDbMeshCompIndex(assetIndex, uniqueIds)
        if nonExistsUniqueIds:
            for currentUniqueId in nonExistsUniqueIds:
                newUniqueId = maUuid.getUuid()
                if currentUniqueId != newUniqueId:
                    maUuid.setRefreshMayaUniqueId(currentUniqueId, newUniqueId)


#
def getFurCompIndexForce(dbSubIndex, furObjects):
    uniqueIds = []
    if furObjects:
        for furObject in furObjects:
            uniqueId = maUuid.getNodeUniqueId(furObject)
            uniqueIds.append(uniqueId)
    #
    if uniqueIds:
        nonExistsUniqueIds = dbGet.getNonExistsDbFurCompIndex(dbSubIndex, uniqueIds)
        if nonExistsUniqueIds:
            for currentUniqueId in nonExistsUniqueIds:
                newUniqueId = maUuid.getUuid()
                if currentUniqueId != newUniqueId:
                    maUuid.setRefreshMayaUniqueId(currentUniqueId, newUniqueId)


#
def getMaterialCompIndexesForce(subIndex, materials):
    uniqueIds = []
    if materials:
        for material in materials:
            uniqueId = maUuid.getNodeUniqueId(material)
            uniqueIds.append(uniqueId)
    #
    if uniqueIds:
        nonExistsUniqueIds = dbGet.getNonExistsDbMaterialComp(subIndex, uniqueIds)
        if nonExistsUniqueIds:
            for currentUniqueId in nonExistsUniqueIds:
                newUniqueId = maUuid.getUuid()
                if currentUniqueId != newUniqueId:
                    maUuid.setRefreshMayaUniqueId(currentUniqueId, newUniqueId)


#
def getAovCompIndexesForce(subIndex, aovs):
    uniqueIds = []
    if aovs:
        for aov in aovs:
            uniqueId = maUuid.getNodeUniqueId(aov)
            uniqueIds.append(uniqueId)
    #
    if uniqueIds:
        nonExistsUniqueIds = dbGet.getNonExistsDbAovComp(subIndex, uniqueIds)
        if nonExistsUniqueIds:
            for currentUniqueId in nonExistsUniqueIds:
                newUniqueId = maUuid.getUuid()
                if currentUniqueId != newUniqueId:
                    maUuid.setRefreshMayaUniqueId(currentUniqueId, newUniqueId)


#
def getAstMeshConstantData(assetName, namespace=none):
    dic = lxBasic.orderedDict()
    #
    geometryObjects = getAstMeshObjects(assetName, 1, namespace)
    if geometryObjects:
        dic = getMeshObjectsEvaluateDic(geometryObjects)
        subData = getMeshObjectsConstantDic(assetName, namespace)
        for k, v in subData.items():
            dic[k] = v
    return dic
