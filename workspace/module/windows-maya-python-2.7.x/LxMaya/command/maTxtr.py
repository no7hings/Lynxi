# coding=utf-8
import glob, datetime
#
import re
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
from PIL import Image

from LxBasic import bscCore, bscMethods, bscObjects

from LxPreset import prsConfigure, prsMethods
#
from LxCore.config import appCfg
#
from LxDatabase import dtbCore
#
from LxMaya.command import maUtils, maFur
#
mayaVersion = maUtils.getMayaVersion()
#
MaTexture_AttrNameDic = {
    'file': 'fileTextureName',
    'aiImage': 'filename',
    'RedshiftNormalMap': 'tex0',
    'RedshiftCameraMap': 'tex0'
}
#
MaTexture_AttrNameLis = [
    'fileTextureName',
    'filename',
    'tex0'
]
#
none = ''


#
def getPTexture(textureFile):
    if bscMethods.OsFile.isExist(textureFile):
        return Image.open(str(textureFile))


#
def getTextureSize(textureFile, useMode=0):
    size = 0, 0
    if textureFile:
        try:
            if useMode == 0:
                size = getPTexture(textureFile).size
            elif useMode == 1:
                size = textureFile.size
        except:
            pass
    return size


#
def getTextureMode(textureFile, useMode=0):
    mode = '?'
    if textureFile:
        try:
            if useMode == 0:
                mode = getPTexture(textureFile).mode
            if useMode == 1:
                mode = textureFile.mode
        except:
            pass
    return mode


#
def isTextureNode(node):
    nodeType = maUtils._getNodeTypeString(node)
    if nodeType in appCfg.MaTexture_NodeTypeLis:
        boolean = True
    else:
        boolean = False
    #
    return boolean


#
def getOsTextureUdimLis(textureFile):
    lis = []
    textureFile = textureFile.replace('<UDIM>', '<udim>')
    subTextureFileLis = glob.glob(textureFile.replace('<udim>', '[0-9][0-9][0-9][0-9]'))
    if subTextureFileLis:
        for i in subTextureFileLis:
            subTextureFile = i.replace('\\', '/')
            lis.append(subTextureFile)
    return lis


#
def getOsTextureSequenceLis(textureFile):
    lis = []
    subTextureFileLis = glob.glob(textureFile.replace('<f>', '[0-9][0-9][0-9][0-9]'))
    if subTextureFileLis:
        for i in subTextureFileLis:
            subTextureFile = i.replace('\\', '/')
            lis.append(subTextureFile)
    return lis


#
def getOsTextureCompLis(textureFile):
    # List [ <Map>, <Map UDIM> ]
    lis = []
    if textureFile:
        # Debug First Texture is use to Repath
        lis = [textureFile]
        if '<udim>' in textureFile.lower():
            subTextureFileLis = getOsTextureUdimLis(textureFile)
            lis.extend(subTextureFileLis)
        elif '<f>' in textureFile.lower():
            subTextureFileLis = getOsTextureSequenceLis(textureFile)
            lis.extend(subTextureFileLis)
    return lis


#
def isOsTextureExist(textureFile):
    boolean = False
    textureBasename = bscMethods.OsFile.basename(textureFile)
    if '<udim>' in textureBasename.lower():
        subTextureFileLis = getOsTextureUdimLis(textureFile)
        if subTextureFileLis:
            boolean = True
    elif '<f>' in textureBasename.lower():
        subTextureFileLis = getOsTextureSequenceLis(textureFile)
        if subTextureFileLis:
            boolean = True
    else:
        if bscMethods.OsFile.isExist(textureFile):
            boolean = True
    return boolean


#
def getTargetTextureExists(textureNode, textureFile):
    if maUtils._getNodeTypeString(textureNode) == 'file':
        isUdim = True
        if textureFile:
            isSequence = maUtils.getAttrDatum(textureNode, 'useFrameExtension')
            textureDirname = bscMethods.OsFile.dirname(textureFile)
            textureBasename = bscMethods.OsFile.basename(textureFile)
            #
            findKeys = re.findall('[0-9][0-9][0-9][0-9]', textureBasename)
            if findKeys:
                if int(mayaVersion) > 2014:
                    uvTilingMode = maUtils.getAttrDatum(textureNode, 'uvTilingMode')
                    if '<udim>' in textureFile.lower():
                        isUdim = False
                    elif not uvTilingMode == 3:
                        isUdim = False
                elif int(mayaVersion) == 2014:
                    isUdim = False
                #
                if isUdim:
                    textureBasename = textureBasename.replace(findKeys[-1], '<udim>')
                elif isSequence:
                    textureBasename = textureBasename.replace(findKeys[-1], '<f>')
                #
                textureFile = bscMethods.OsPath.composeBy(textureDirname, textureBasename)
    return isOsTextureExist(textureFile)


#
def getTextureNodeLis(filterNamespace=none):
    filterType = appCfg.MaTexture_NodeTypeLis
    return maUtils.getNodeLisByFilter(filterType, filterNamespace)


#
def getTextureNodeAttrName(textureNode):
    textureNodeType = maUtils._getNodeTypeString(textureNode)
    attrName = MaTexture_AttrNameDic[textureNodeType]
    return attrName


#
def getTextureNodeAttrDatum(textureNode):
    attrName = getTextureNodeAttrName(textureNode)
    textureFile = maUtils.getAttrDatum(textureNode, attrName)
    return textureFile


#
def getTextures(textureFile):
    lis = []
    if '<udim>' in textureFile.lower():
        udimTexture = getOsTextureUdimLis(textureFile)
        if udimTexture:
            lis = udimTexture
    elif '<f>' in textureFile.lower():
        sequenceTexture = getOsTextureSequenceLis(textureFile)
        if sequenceTexture:
            lis = sequenceTexture
    else:
        if bscMethods.OsFile.isExist(textureFile):
            lis = [textureFile]
    return lis


#
def getRepathTexture(textureNode, textureFile):
    string = textureFile
    if cmds.nodeType(textureNode) == 'file':
        if int(mayaVersion) > 2014:
            if '<udim>' in textureFile.lower():
                udimTexture = getOsTextureUdimLis(textureFile)
                if udimTexture:
                    string = udimTexture[0]
            elif '<f>' in textureFile.lower():
                sequenceTexture = getOsTextureSequenceLis(textureFile)
                if sequenceTexture:
                    string = sequenceTexture[0]
    else:
        string = textureFile
    return string


#
def getTextureByTextureNodes(textureNodes):
    textures = []
    if textureNodes:
        for textureNode in textureNodes:
            textureAttrData = getTextureNodeAttrData(textureNode)
            if textureAttrData:
                subTextureFileLis = getTextures(textureAttrData)
                textures.extend(subTextureFileLis)
    return textures


#
def getTargetTexture(targetPath, sourceTextureFile):
    textureName, ext = getTextureData(sourceTextureFile)
    targetTexture = '%s/%s%s' % (targetPath, textureName, ext)
    return targetTexture


#
def getTxTexture(directory, textureFile):
    textureName, ext = getTextureData(textureFile)
    txTexture = '%s/%s%s' % (directory, textureName, appCfg.MaArnoldTxExt)
    return txTexture


#
def getTextureNodeAttrData(textureNode):
    textureFile = getTextureNodeAttrDatum(textureNode)
    if maUtils._getNodeTypeString(textureNode) == 'file':
        isUdim = True
        if textureFile:
            isSequence = maUtils.getAttrDatum(textureNode, 'useFrameExtension')
            textureDirname = bscMethods.OsFile.dirname(textureFile)
            textureBasename = bscMethods.OsFile.basename(textureFile)
            #
            findKeys = re.findall('[0-9][0-9][0-9][0-9]', textureBasename)
            if findKeys:
                if int(mayaVersion) > 2014:
                    uvTilingMode = maUtils.getAttrDatum(textureNode, 'uvTilingMode')
                    if '<udim>' in textureBasename.lower():
                        isUdim = False
                    elif not uvTilingMode == 3:
                        isUdim = False
                elif int(mayaVersion) == 2014:
                    isUdim = False
                #
                if isUdim:
                    textureBasename = textureBasename.replace(findKeys[-1], '<udim>')
                elif isSequence:
                    textureBasename = textureBasename.replace(findKeys[-1], '<f>')
                #
                textureFile = bscMethods.OsPath.composeBy(textureDirname, textureBasename)
    return textureFile


#
def getTextureAttrDataForRepath(textureNode):
    textureFile = getTextureNodeAttrDatum(textureNode)
    return textureFile


#
def getTextureDatumDic(inData=none, mode=0):
    dic = bscCore.orderedDict()
    #
    if inData:
        usedData = inData
    else:
        usedData = getTextureNodeLis()
    if usedData:
        for textureNode in usedData:
            textureFile = [getTextureNodeAttrData(textureNode), getTextureAttrDataForRepath(textureNode)][mode]
            subTextureFileLis = getOsTextureCompLis(textureFile)
            if subTextureFileLis:
                dic[textureNode] = subTextureFileLis
    return dic


#
def getFurMapNodes(filterNamespace=none):
    filterType = appCfg.MaFurMapNodeTypes
    return maUtils.getNodeLisByFilter(filterType, filterNamespace)


#
def getFurMapDataDic(inData=none):
    dic = bscCore.orderedDict()
    #
    usedData = []
    if inData:
        usedData = inData
    if not usedData:
        furObjects = []
        yetiObjects = maUtils.getYetiObjects()
        furObjects.extend(yetiObjects)
        pfxHairObjects = maUtils.getPfxHairObjects()
        furObjects.extend(pfxHairObjects)
        nurbsHairObjects = maFur.getNurbsHairObjects(True)
        furObjects.extend(nurbsHairObjects)
        #
        usedData = furObjects
    if usedData:
        # Yeti's Map
        for objectPath in usedData:
            if maUtils.getTransformType(objectPath) == appCfg.MaNodeType_Plug_Yeti:
                shapePath = maUtils._getNodeShapeString(objectPath)
                mapNodes = cmds.pgYetiGraph(shapePath, listNodes=1, type='texture')
                if mapNodes:
                    for node in mapNodes:
                        furMapFile = cmds.pgYetiGraph(shapePath, node=node, param='file_name', getParamValue=1)
                        mapNodePath = '%s - %s' % (shapePath, node)
                        osMaps = getOsTextureCompLis(furMapFile)
                        if osMaps:
                            dic[mapNodePath] = osMaps
            # Pfx Hair's Map
            elif maUtils.getTransformType(objectPath) == appCfg.MaPfxHairType:
                mapNodes = maUtils.getPfxHairMapNodes(objectPath)
                if mapNodes:
                    for node in mapNodes:
                        furMapFile = getTextureNodeAttrData(node)
                        osMaps = getOsTextureCompLis(furMapFile)
                        if osMaps:
                            dic[node] = osMaps
            # Nurbs Hair's Map
            elif maUtils._getNodeShapeTypeString(objectPath) == appCfg.MaNodeType_Plug_NurbsHair:
                mapNodes = maFur.getNurbsHairMapNodes(objectPath)
                if mapNodes:
                    for node in mapNodes:
                        furMapFile = maFur.getFurMapAttrData(node)
                        osMaps = getOsTextureCompLis(furMapFile)
                        if osMaps:
                            dic[node] = osMaps
    return dic


#
def setTextureAttr(textureNode, textureFile):
    textureAttrName = getTextureNodeAttrName(textureNode)
    textureFile = getRepathTexture(textureNode, textureFile)
    #
    maUtils.setAttrStringDatum(textureNode, textureAttrName, textureFile)


#
def setMapAttr(furNodePath, furMapFile, force=False):
    nodeData = furNodePath.split(' - ')
    # Filter is Yeti
    if len(nodeData) == 2:
        # Yeti Map
        shapePath, mapNode = nodeData
        if force:
            maUtils.setAttrDatumForce_(shapePath, 'fileMode', False)
            maUtils.setAttrStringDatum(shapePath, 'cacheFileName', none)
        #
        maUtils.setYetiTextureParam(shapePath, mapNode, furMapFile)
    elif len(nodeData) == 1:
        furMapNode = furNodePath
        #
        nodeType = maUtils._getNodeTypeString(furMapNode)
        # Texture Map
        if nodeType in appCfg.MaTexture_NodeTypeLis:
            setTextureAttr(furNodePath, furMapFile)
        # Other Map
        else:
            maFur.setFurMapAttrData(furMapNode, furMapFile)


# Set Texture to Tx
def setTextureAttrToTx(textureDatumDic=none):
    textureLis = []
    txLis = []
    #
    if not textureDatumDic:
        textureDatumDic = getTextureDatumDic()
    #
    if textureDatumDic:
        # View Progress
        explain = u'''Repath Texture to Tx ( Arnold )'''
        maxValue = len(textureDatumDic)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for k, v in textureDatumDic.items():
            # In Progress
            progressBar.update()
            #
            textureNode = k
            textureString = v[0]
            #
            textureDirectory, textureBasename = bscMethods.OsFile.dirname(textureString), bscMethods.OsFile.basename(textureString)
            textureName, ext = bscMethods.OsFile.toExtSplit(textureBasename)
            txTexture = '{}/{}{}'.format(textureDirectory, textureName, appCfg.MaArnoldTxExt)
            if len(v) == 1:
                if bscMethods.OsFile.isExist(textureString):
                    # Exists Filter
                    if bscMethods.OsFile.isExist(txTexture):
                        textureLis.append(textureString)
                        txLis.append(txTexture)
            elif len(v) > 1:
                for i in v[1:]:
                    subTextureFile = i
                    if bscMethods.OsFile.isExist(subTextureFile):
                        subTextureBaseName = bscMethods.OsFile.basename(subTextureFile)
                        subTextureName, subExt = bscMethods.OsFile.toExtSplit(subTextureBaseName)
                        #
                        subTxTexture = '{}/{}{}'.format(textureDirectory, subTextureName, appCfg.MaArnoldTxExt)
                        # Exists Filter
                        if bscMethods.OsFile.isExist(subTxTexture):
                            textureLis.append(subTextureFile)
                            txLis.append(subTxTexture)
            # Set Attr
            setTextureAttr(textureNode, txTexture)
    #
    if len(textureLis) == len(txLis):
        return True
    else:
        setTextureAttrToTx()


# Get File's Data
def getTextureData(textureFile):
    textureBaseName = bscMethods.OsFile.basename(textureFile)
    textureName, ext = bscMethods.OsFile.toExtSplit(textureBaseName)
    return textureName, ext


#
def getBackupTexture(targetPath, sourceTextureFile):

    timeTag = bscMethods.OsFile.mtimetag(sourceTextureFile)
    if timeTag:
        textureName, ext = getTextureData(sourceTextureFile)
        newTexture = '%s/%s%s.%s' % (targetPath, textureName, ext, timeTag)
        return newTexture


#
def getUdimTextureFolder(udimTexture):
    udimTextureFolder = bscMethods.OsFile.name(udimTexture)[:-len('<udim>')].replace('.', none)
    return udimTextureFolder


# Get Mult File's Update
def getMultUpdateLabel(textures):
    lis = []
    for textureFile in textures:
        timestamp = bscMethods.OsFile.mtimestamp(textureFile)
        update = datetime.datetime.fromtimestamp(timestamp)
        lis.append(update)
    return max(lis).strftime('%Y_%m%d_%H%M%S')


# Set To Render Pool
def setToRender(source, target):
    bscMethods.OsFile.copyTo(source, target)


#
def getTextureIsCollection(sourceTextureFile, targetTexture):
    boolean = False
    # Exists Filter
    if not bscMethods.OsFile.isSame(sourceTextureFile, targetTexture):
        textureExists = bscMethods.OsFile.isExist(targetTexture)
        if not textureExists:
            boolean = True
        # Update Filter
        else:
            sourceFileTimestamp = str(bscMethods.OsFile.mtimestamp(sourceTextureFile))
            targetFileTimestamp = str(bscMethods.OsFile.mtimestamp(targetTexture))
            if not sourceFileTimestamp == targetFileTimestamp:
                boolean = True
    #
    return boolean


#
def getTxTextureIsCollection(renderer):
    boolean = False
    if renderer == prsConfigure.Utility.DEF_value_renderer_arnold:
        boolean = True
    #
    return boolean


@dtbCore.fncThreadSemaphoreModifier
def copyFileThreadMethod(sourceFile, targetFile, backupExists=False):
    if backupExists is True:
        if bscMethods.OsFile.isExist(targetFile):
            backupFile = bscMethods.OsFile.backupName(targetFile)
            bscMethods.OsFile.copyTo(targetFile, backupFile)
    #
    bscMethods.OsFile.copyTo(sourceFile, targetFile)


#
def setBackupTextures(targetPath, withTx=True, inData=none):
    dic = bscCore.orderedDict()
    #
    collectionDatumLis = []
    # Filter Collection
    textureData = getTextureDatumDic(inData)
    if textureData:
        for k, v in textureData.items():
            sourceTextureFileLis = [[v[0]], v[1:]][len(v) > 1]
            for sourceTextureFile in sourceTextureFileLis:
                if bscMethods.OsFile.isExist(sourceTextureFile):
                    sourcePath = bscMethods.OsFile.dirname(sourceTextureFile)
                    #
                    backupTexture = getBackupTexture(targetPath, sourceTextureFile)
                    isCollectionTexture = not bscMethods.OsFile.isExist(backupTexture)
                    #
                    if isCollectionTexture:
                        collectionDatumLis.append((sourceTextureFile, backupTexture))
                    #
                    if withTx:
                        sourceTxTexture = getTxTexture(sourcePath, sourceTextureFile)
                        backupTxTexture = getBackupTexture(targetPath, sourceTxTexture)
                        isCollectionTxTexture = not bscMethods.OsFile.isExist(backupTxTexture)
                        #
                        if isCollectionTxTexture:
                            collectionDatumLis.append((sourceTxTexture, backupTxTexture))
                    #
                    dic[bscMethods.OsFile.basename(sourceTextureFile)] = bscMethods.OsFile.basename(backupTexture)
    #
    if collectionDatumLis:
        # View Progress
        explain = u'''Backup Texture(s)'''
        maxValue = len(collectionDatumLis)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        splitCollectionDatumLis = bscMethods.List.splitTo(collectionDatumLis, 250)
        for subCollectionDatum in splitCollectionDatumLis:
            copyThreadLis = []
            #
            for sourceTextureFile, targetTexture in subCollectionDatum:
                t = dtbCore.DtbThread(copyFileThreadMethod, sourceTextureFile, targetTexture)
                copyThreadLis.append(t)
                t.start()
            #
            if copyThreadLis:
                for i in copyThreadLis:
                    progressBar.update()
                    i.join()
    return dic


#
def setTexturesCollection(targetPath, inData=none, withTx=True, backupExists=False):
    collectionDatumLis = []
    # Filter Collection
    textureData = getTextureDatumDic(inData)
    if textureData:
        for k, v in textureData.items():
            sourceTextureFileLis = [[v[0]], v[1:]][len(v) > 1]
            for sourceTextureFile in sourceTextureFileLis:
                if bscMethods.OsFile.isExist(sourceTextureFile):
                    sourcePath = bscMethods.OsFile.dirname(sourceTextureFile)
                    #
                    targetTexture = getTargetTexture(targetPath, sourceTextureFile)
                    isCollectionTexture = getTextureIsCollection(sourceTextureFile, targetTexture)
                    #
                    if isCollectionTexture:
                        collectionDatumLis.append((sourceTextureFile, targetTexture))
                    #
                    if withTx:
                        sourceTxTexture = getTxTexture(sourcePath, sourceTextureFile)
                        targetTxTexture = getTxTexture(targetPath, targetTexture)
                        isCollectionTxTexture = getTextureIsCollection(sourceTxTexture, targetTxTexture)
                        #
                        if isCollectionTxTexture:
                            collectionDatumLis.append((sourceTxTexture, targetTxTexture))
    #
    if collectionDatumLis:
        # View Progress
        explain = u'''Collection Texture(s)'''
        maxValue = len(collectionDatumLis)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        #
        splitCollectionDatumLis = bscMethods.List.splitTo(collectionDatumLis, 250)
        for subCollectionDatum in splitCollectionDatumLis:
            copyThreadLis = []
            #
            for sourceTextureFile, targetTexture in subCollectionDatum:
                t = dtbCore.DtbThread(copyFileThreadMethod, sourceTextureFile, targetTexture, backupExists)
                copyThreadLis.append(t)
                t.start()
            if copyThreadLis:
                for i in copyThreadLis:
                    progressBar.update()
                    i.join()


#
def setCollectionMaps(targetPath, inData=none, backupExists=False):
    collectionDatumLis = []
    # Filter Collection
    mapData = getFurMapDataDic(inData)
    if mapData:
        for k, v in mapData.items():
            sourceMaps = [[v[0]], v[1:]][len(v) > 1]
            for sourceMap in sourceMaps:
                if bscMethods.OsFile.isExist(sourceMap):
                    targetMap = getTargetTexture(targetPath, sourceMap)
                    isCollectionMap = getTextureIsCollection(sourceMap, targetMap)
                    #
                    if isCollectionMap:
                        collectionDatumLis.append((sourceMap, targetMap))
    #
    if collectionDatumLis:
        explain = u'''Collection Character FX's Map'''
        maxValue = len(collectionDatumLis)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        #
        splitCollectionDatumLis = bscMethods.List.splitTo(collectionDatumLis, 250)
        for subCollectionDatum in splitCollectionDatumLis:
            copyThreadLis = []
            for sourceMap, targetMap in subCollectionDatum:
                t = dtbCore.DtbThread(copyFileThreadMethod, sourceMap, targetMap, backupExists)
                copyThreadLis.append(t)
                t.start()
            if copyThreadLis:
                for i in copyThreadLis:
                    progressBar.update()
                    i.join()


#
def setTextureRepath(targetPath, sourceTextureFile, textureNode):
    targetTexture = getTargetTexture(targetPath, sourceTextureFile)
    # Exists Filter
    if targetTexture.lower() != sourceTextureFile.lower():
        # Debug if Sequence Texture not Start from minimum Value
        if getTargetTextureExists(textureNode, targetTexture):
            setTextureAttr(textureNode, targetTexture)


#
def setTexturesRepath(targetPath, inData=none):
    textureData = getTextureDatumDic(inData, mode=1)
    if textureData:
        # View Progress
        explain = u'''Repath Texture(s)'''
        maxValue = len(textureData)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for k, v in textureData.items():
            # In Progress
            progressBar.update()
            #
            textureNode = k
            sourceTextureFile = v[0]
            setTextureRepath(
                targetPath, sourceTextureFile, textureNode
            )


#
def setRepathYetiMap(sourceMap, targetPath, yetiNode, mapNode):
    targetMap = getTargetTexture(targetPath, sourceMap)
    if targetMap.lower() != sourceMap.lower():
        if isOsTextureExist(targetMap):
            maUtils.setYetiTextureParam(yetiNode, mapNode, targetMap)


# Repath CFX Map
def setRepathMaps(targetPath, inData=none):
    mapData = getFurMapDataDic(inData)
    if mapData:
        # View Progress
        explain = u'''Repath Map'''
        maxValue = len(mapData)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for k, v in mapData.items():
            # In Progress
            progressBar.update()
            #
            sourceMap = v[0]
            isYetiNode = ' - ' in k
            if isYetiNode:
                shapePath, mapNode = k.split(' - ')
                setRepathYetiMap(sourceMap, targetPath, shapePath, mapNode)
            elif not isYetiNode:
                furMapNode = k
                #
                nodeType = maUtils._getNodeTypeString(furMapNode)
                if nodeType in appCfg.MaTexture_NodeTypeLis:
                    setTextureRepath(targetPath, sourceMap, furMapNode)
                else:
                    targetMap = getTargetTexture(targetPath, sourceMap)
                    maFur.setFurMapAttrData(furMapNode, targetMap)


#
def setRefreshTextureColorSpace(force=False):
    textureNodes = getTextureNodeLis()
    if textureNodes:
        for i in textureNodes:
            colorSpace = maUtils.getAttrDatum(i, 'colorSpace')
            if force is False:
                if not colorSpace == 'sRGB':
                    maUtils.setAttrDatumForce_(i, 'ignoreColorSpaceFileRules', 1)
            elif force is True:
                maUtils.setAttrDatumForce_(i, 'ignoreColorSpaceFileRules', 1)


#
def setUpdateArnoldTx():
    if prsMethods.Project.isMayaUsedArnoldRenderer():
        # noinspection PyUnresolvedReferences
        from mtoa import txManager
        txManager.UpdateAllTx(force=0)
        #


#
def setRefreshTextureColorSpace_():
    filterKeywords = ['Roughness', 'Metallic']
    textureNodes = getTextureNodeLis()
    if textureNodes:
        for i in textureNodes:
            textureFile = getTextureNodeAttrDatum(i)
            textureName = bscMethods.OsFile.name(textureFile)
            isEnabled = False
            for j in filterKeywords:
                if j in textureName:
                    isEnabled = True
            if isEnabled is True:
                maUtils.setAttrStringDatumForce(i, 'colorSpace', 'Raw')
