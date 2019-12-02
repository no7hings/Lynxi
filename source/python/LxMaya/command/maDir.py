# coding=utf-8
import glob
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxCore import lxBasic, lxProgress, lxLog, lxTip
#
from LxCore.config import appCfg
#
from LxMaya.command import maUtils, maFile, maTxtr, maFur, maAsb, maProxy, maAbc, maGeomCache, maArnold
#
pathsep = appCfg.OsFilePathSep
#
none = ''


#
def getLinkDicMethod(dic, nodeString, osFile):
    osFile = osFile.replace('\\', pathsep)
    osFile = lxBasic.getPathReduce(osFile, pathsep)
    #
    key = osFile.lower()
    dic.setdefault(key, []).append((nodeString, osFile))


#
def getTextureLinkDic(nodes=None):
    dic = lxBasic.orderedDict()
    #
    if nodes:
        usedData = nodes
    else:
        usedData = maTxtr.getTextureNodeLis()
    #
    for node in usedData:
        textureFile = maTxtr.getTextureNodeAttrData(node)
        if textureFile:
            getLinkDicMethod(dic, node, textureFile)
    return dic


#
def getTxTexture(texture):
    base, ext = lxBasic.toOsFileSplitByExt(texture)
    txTexture = '%s%s' % (base, appCfg.MaArnoldTxExt)
    return txTexture


#
def getFurMapLinkDic(nodes=None):
    dic = lxBasic.orderedDict()
    #
    usedData = []
    if nodes:
        usedData = nodes
    if not usedData:
        usedData = maTxtr.getFurMapNodes()
    #
    if usedData:
        for objectPath in usedData:
            # Yeti's Map
            if maUtils.getShapeType(objectPath) == appCfg.MaNodeType_Plug_Yeti:
                shapePath = maUtils.getNodeShape(objectPath)
                mapNodes = cmds.pgYetiGraph(shapePath, listNodes=1, type='texture')
                if mapNodes:
                    for node in mapNodes:
                        furMapFile = cmds.pgYetiGraph(shapePath, node=node, param='file_name', getParamValue=1)
                        mapNodePath = '%s - %s' % (shapePath, node)
                        #
                        getLinkDicMethod(dic, mapNodePath, furMapFile)
            # Pfx Hair's Map
            elif maUtils.getShapeType(objectPath) == appCfg.MaPfxHairType:
                mapNodes = maUtils.getPfxHairMapNodes(objectPath)
                if mapNodes:
                    for node in mapNodes:
                        furMapFile = maTxtr.getTextureNodeAttrData(node)
                        #
                        getLinkDicMethod(dic, node, furMapFile)
            # Nurbs Hair's Map
            elif maUtils.getShapeType(objectPath) == appCfg.MaNodeType_Plug_NurbsHair:
                mapNodes = maFur.getNurbsHairMapNodes(objectPath)
                if mapNodes:
                    for node in mapNodes:
                        furMapFile = maFur.getFurMapAttrData(node)
                        #
                        getLinkDicMethod(dic, node, furMapFile)
    return dic


#
def getReferenceNodeLis(filterNamespace=None):
    if filterNamespace:
        return maUtils.getReferenceNodeFilterByNamespace(filterNamespace)
    else:
        return maUtils.getReferenceNodeLis()


#
def getReferenceLinkDic(nodes=None):
    dic = lxBasic.orderedDict()
    #
    if nodes:
        usedData = nodes
    else:
        usedData = getReferenceNodeLis()
    #
    if usedData:
        for node in usedData:
            isLoaded = cmds.referenceQuery(node, isLoaded=1)
            if isLoaded:
                referenceFile = maUtils.getReferenceFile(node, useMode=1)
                #
                if referenceFile:
                    getLinkDicMethod(dic, node, referenceFile)
    return dic


#
def setReferenceRepath(nodeString, osFile):
    sourceFile = maUtils.getReferenceFile(nodeString, useMode=1)
    if not lxBasic.isOsSameFile(sourceFile, osFile):
        maUtils.setReloadReferenceFile(nodeString)
        maUtils.setLoadReferenceFile(nodeString, osFile)


# Assembly Reference
def getAssemblyReferenceNodeLis(filterNamespace=None):
    filterType = appCfg.MaNodeType_AssemblyReference
    return maUtils.getNodeLisByFilter(filterType, filterNamespace)


#
def getAsbRefLinkDic(nodes=None):
    dic = lxBasic.orderedDict()
    #
    if nodes:
        usedData = nodes
    else:
        usedData = getAssemblyReferenceNodeLis()
    if usedData:
        for node in usedData:
            adFile = maAsb.getAssemblyDefinitionFile(node)
            if adFile:
                getLinkDicMethod(dic, node, adFile)
    return dic


#
def setAssemblyReferenceRepath(nodeString, osFile):
    attrName = 'definition'
    #
    sourceFile = maUtils.getAttrDatum(nodeString, attrName)
    if not lxBasic.isOsSameFile(sourceFile, osFile):
        maUtils.setAttrStringDatum(nodeString, attrName, osFile)


# Proxy ( Arnold )
def getArnoldProxyLis(filterNamespace=None):
    filterType = appCfg.MaNodeType_AiStandIn
    return maUtils.getNodeLisByFilter(filterType, filterNamespace)


#
def getProxyCacheLinkDic(nodes=None):
    dic = lxBasic.orderedDict()
    #
    if nodes:
        usedData = nodes
    else:
        usedData = getArnoldProxyLis()
    if usedData:
        for node in usedData:
            proxyFile = maProxy.getArnoldProxyFile(node)
            if proxyFile:
                getLinkDicMethod(dic, node, proxyFile)
    return dic


#
def setProxyCacheRepath(nodeString, osFile):
    attrName = 'dso'
    sourceFile = maUtils.getAttrDatum(nodeString, attrName)
    if not lxBasic.isOsSameFile(sourceFile, osFile):
        maUtils.setAttrStringDatum(nodeString, attrName, osFile)


#
def getVolumeCacheNodeLis(filterNamespace=None):
    filterType = appCfg.MaNodeType_AiVolume
    return maUtils.getNodeLisByFilter(filterType, filterNamespace)


#
def getVolumeCacheLinkDic(nodes=None):
    dic = lxBasic.orderedDict()
    #
    usedData = []
    if nodes:
        usedData = nodes
    if not usedData:
        usedData = getVolumeCacheNodeLis()
    if usedData:
        for node in usedData:
            if maUtils.getNodeType(node) == appCfg.MaNodeType_AiVolume:
                fileString = maArnold.getVolumeCacheFile(node)
                if fileString:
                    getLinkDicMethod(dic, node, fileString)
    return dic


#
def setVolumeCacheRepath(nodeString, osFile):
    attrName = 'filename'
    sourceFile = maUtils.getAttrDatum(nodeString, attrName)
    if not lxBasic.isOsSameFile(sourceFile, osFile):
        maUtils.setAttrStringDatum(nodeString, attrName, osFile)


# GPU Cache
def getGpuCacheNodeLis(filterNamespace=None):
    filterType = appCfg.MaGpuCache
    return maUtils.getNodeLisByFilter(filterType, filterNamespace)


#
def getGpuCacheLinkDic(nodes=None):
    dic = lxBasic.orderedDict()
    #
    usedData = []
    if nodes:
        usedData = nodes
    if not usedData:
        usedData = getGpuCacheNodeLis()
    if usedData:
        for node in usedData:
            gpuCacheFile = maAbc.getGpuCacheFile(node)
            if gpuCacheFile:
                getLinkDicMethod(dic, node, gpuCacheFile)
    return dic


#
def setGpuCacheRepath(nodeString, osFile):
    attrName = 'cacheFileName'
    #
    sourceFile = maUtils.getAttrDatum(nodeString, attrName)
    if not lxBasic.isOsSameFile(sourceFile, osFile):
        maUtils.setAttrStringDatum(nodeString, attrName, osFile)


# Alembic Cache
def getAlembicCacheNodeLis(filterNamespace=None):
    filterType = appCfg.MaNodeType_Alembic
    return maUtils.getNodeLisByFilter(filterType, filterNamespace)


#
def getAlembicCacheLinkDic(nodes=None):
    dic = lxBasic.orderedDict()
    #
    usedData = []
    if nodes:
        usedData = nodes
    if not usedData:
        usedData = getAlembicCacheNodeLis()
    #
    if usedData:
        for node in usedData:
            fileString = maAbc.getAlembicCacheFile(node)
            if fileString:
                getLinkDicMethod(dic, node, fileString)
    return dic


#
def setRepathAlembicCache(nodeString, osFile):
    attrName = 'abc_File'
    #
    sourceFile = maUtils.getAttrDatum(nodeString, attrName)
    if not lxBasic.isOsSameFile(sourceFile, osFile):
        maUtils.setAttrStringDatum(nodeString, attrName, osFile)


#
def getYetiShapeLis():
    return maUtils.getNodeLisByType(appCfg.MaNodeType_Plug_Yeti)


#
def getFurCacheNodeLis(filterNamespace=None):
    filterType = appCfg.MaFurCacheNodeTypes
    return maUtils.getNodeLisByFilter(filterType, filterNamespace)


#
def getFurCacheLinkDic(nodes=None):
    dic = lxBasic.orderedDict()
    #
    usedData = []
    if nodes:
        usedData = nodes
    if not usedData:
        usedData = getFurCacheNodeLis()
    if usedData:
        for node in usedData:
            if maUtils.getShapeType(node) == appCfg.MaNodeType_Plug_Yeti:
                yetiCacheFile = maFur.getYetiCacheFile(node)
                if yetiCacheFile:
                    getLinkDicMethod(dic, node, yetiCacheFile)
            elif maUtils.getShapeType(node) == appCfg.MaNodeType_Plug_NurbsHair:
                nurbsHairCacheFile = maFur.getNurbsHairCacheFile(node)
                if nurbsHairCacheFile:
                    getLinkDicMethod(dic, node, nurbsHairCacheFile)
    return dic


#
def getGeomCacheNodeLis(filterNamespace=None):
    filterType = appCfg.MaNodeType_CacheFile
    return maUtils.getNodeLisByFilter(filterType, filterNamespace)


#
def getGeomCacheLinkDic(nodes=None):
    dic = lxBasic.orderedDict()
    #
    usedData = []
    if nodes:
        usedData = nodes
    if not usedData:
        usedData = getGeomCacheNodeLis()
    if usedData:
        for node in usedData:
            if maUtils.getNodeType(node) == appCfg.MaNodeType_CacheFile:
                geomCacheFiles = maGeomCache.getGeomCacheFile(node)
                if geomCacheFiles:
                    geomCacheXmlFile, geomCacheFile = geomCacheFiles
                    #
                    getLinkDicMethod(dic, node, geomCacheXmlFile)
                    getLinkDicMethod(dic, node, geomCacheFile)
    return dic


#
def setFurCacheRepath(nodeString, sourceFile, targetFile, force=False):
    nodeType = maUtils.getNodeType(nodeString)
    if nodeType == appCfg.MaNodeType_Plug_Yeti:
        setRepathYetiCache(nodeString, sourceFile, targetFile, force)
    elif nodeType == appCfg.MaNodeType_Plug_NurbsHair:
        maFur.setNhrCacheObjectReadCache(nodeString, targetFile)


#
def setRepathGeomCache(nodeString, osFile):
    if maUtils.getNodeType(nodeString) == 'cacheFile':
        maGeomCache.setRepathGeometryCache(nodeString, osFile)


#
def getYetiCacheRange(osFile):
    startFrame = 0
    endFrame = 0
    existsYetiCaches = lxBasic.getOsMultFileLis(osFile)
    if existsYetiCaches:
        usedCaches = existsYetiCaches[1:]
        if usedCaches:
            startFrame = int(min(usedCaches)[-8:-4])
            endFrame = int(max(usedCaches)[-8:-4])
    return startFrame, endFrame


#
def setRepathYetiCache(nodeString, sourceFile, targetFile, force=False):
    if force:
        startFrame, endFrame = getYetiCacheRange(sourceFile)
        sample = 3
        maFur.setYetiNodeWriteCache(
            targetFile, nodeString,
            startFrame, endFrame, sample,
            isUpdateViewport=0,
            isGeneratePreview=0
        )
    #
    maFur.setYetiConnectCache(nodeString, targetFile)


#
def setRepathGeneral(nodeString, osFile, fileType):
    if fileType == 'texture':
        setTextureRepath(nodeString, osFile)
    elif fileType == 'assemblyReference':
        setAssemblyReferenceRepath(nodeString, osFile)
    elif fileType == 'proxyCache':
        setProxyCacheRepath(nodeString, osFile)
    elif fileType == 'volumeCache':
        setVolumeCacheRepath(nodeString, osFile)
    elif fileType == 'gpuCache':
        setGpuCacheRepath(nodeString, osFile)
    elif fileType == 'alembicCache':
        setRepathAlembicCache(nodeString, osFile)
    elif fileType == 'geometryCache':
        setRepathGeomCache(nodeString, osFile)


#
def setTextureRepath(nodeString, osFile):
    # Mast Lower
    osFile = osFile.replace('<UDIM>', '<udim>')
    maTxtr.setTextureAttr(nodeString, osFile)


#
def setRepathFurMap(nodeString, osFile, force=False):
    # Must Upper
    osFile = osFile.replace('<udim>', '<UDIM>')
    maTxtr.setMapAttr(nodeString, osFile, force)


#
def getDirData(
        withTexture=False,
        withFurMap=False,
        withReference=False,
        withAssemblyReference=False,
        withProxyCache=False,
        withVolumeCache=False,
        withGpuCache=False,
        withAlembicCache=False,
        withFurCache=False,
        withGeomCache=False):
    def getBranch(key, value):
        fileType = key
        args, method = value
        #
        data = None
        if isinstance(args, bool):
            if args is True:
                data = method()
        elif isinstance(args, list):
            if args:
                data = method(args)
        #
        if data:
            for osFileKey, linkDatas in data.items():
                osPath = lxBasic.getOsFileDirname(osFileKey)
                if not osPath in osPathLis:
                    osPathLis.append(osPath)
                    osPathLis.append(osPath)
                #
                if linkDatas:
                    nodes = []
                    #
                    osFile = linkDatas[0][1]
                    for node, subOsFile in linkDatas:
                        nodes.append(node)
                    #
                    osFileDic.setdefault(osPath, []).append((fileType, osFile, nodes))
    #
    osPathLis = []
    osFileDic = {}
    #
    methodDic = dict(
        texture=(withTexture, getTextureLinkDic),
        furMap=(withFurMap, getFurMapLinkDic),
        reference=(withReference, getReferenceLinkDic),
        assemblyReference=(withAssemblyReference, getAsbRefLinkDic),
        proxyCache=(withProxyCache, getProxyCacheLinkDic),
        volumeCache=(withVolumeCache, getVolumeCacheLinkDic),
        gpuCache=(withGpuCache, getGpuCacheLinkDic),
        alembicCache=(withAlembicCache, getAlembicCacheLinkDic),
        furCache=(withFurCache, getFurCacheLinkDic),
        geometryCache=(withGeomCache, getGeomCacheLinkDic)
    )
    #
    for k, v in methodDic.items():
        getBranch(k, v)
    #
    return osPathLis, osFileDic


#
def getComposeFileLis(
        withCurrent=False,
        withTexture=False,
        withFurMap=False,
        withReference=False,
        withAssemblyReference=False,
        withProxyCache=False,
        withVolumeCache=False,
        withGpuCache=False,
        withAlembicCache=False,
        withFurCache=False,
        withGeomCache=False,
        withTx=False):
    def getBranch(key, value):
        def getExistsFile(osFile):
            if not osFile in lis:
                lis.append(osFile)
                if fileType == 'texture':
                    if withTx:
                        txTextureFile = getTxTexture(osFile)
                        if not txTextureFile in lis:
                            lis.append(txTextureFile)
        fileType = key
        args, method = value
        #
        data = None
        if isinstance(args, bool):
            if args is True:
                data = method()
        elif isinstance(args, list):
            if args:
                data = method(args)
        #
        if data:
            for osFileKey, linkDatas in data.items():
                if linkDatas:
                    for node, subOsFile in linkDatas:
                        multFiles = lxBasic.getOsMultFileLis(subOsFile)
                        if multFiles:
                            count = len(multFiles)
                            if count == 1:
                                getExistsFile(multFiles[0])
                            elif count > 1:
                                [getExistsFile(i) for i in multFiles[1:]]
    #
    lis = []
    if withCurrent is True:
        lis = [maUtils.getCurrentFile()]
    #
    methodDic = dict(
        texture=(withTexture, getTextureLinkDic),
        furMap=(withFurMap, getFurMapLinkDic),
        reference=(withReference, getReferenceLinkDic),
        assemblyReference=(withAssemblyReference, getAsbRefLinkDic),
        proxyCache=(withProxyCache, getProxyCacheLinkDic),
        volumeCache=(withVolumeCache, getVolumeCacheLinkDic),
        gpuCache=(withGpuCache, getGpuCacheLinkDic),
        alembicCache=(withAlembicCache, getAlembicCacheLinkDic),
        furCache=(withFurCache, getFurCacheLinkDic),
        geometryCache=(withGeomCache, getGeomCacheLinkDic)
    )
    #
    for k, v in methodDic.items():
        getBranch(k, v)
    #
    return lis


#
def getDirDataByNamespaceFilter(
        namespaces,
        withTexture=False,
        withFurMap=False,
        withReference=False,
        withAssemblyReference=False,
        withProxyCache=False,
        withVolumeCache=False,
        withGpuCache=False,
        withAlembicCache=False,
        withFurCache=False,
        withGeomCache=False):
    methodDatas = [
        (withTexture, maTxtr.getTextureNodeLis),
        (withFurMap, maTxtr.getFurMapNodes),
        (withReference, getReferenceNodeLis),
        (withAssemblyReference, getAssemblyReferenceNodeLis),
        (withProxyCache, getArnoldProxyLis),
        (withVolumeCache, getVolumeCacheNodeLis),
        (withGpuCache, getGpuCacheNodeLis),
        (withAlembicCache, getAlembicCacheNodeLis),
        (withFurCache, getFurCacheNodeLis),
        (withGeomCache, getGeomCacheNodeLis)
    ]
    args = []
    for enabled, method in methodDatas:
        if enabled:
            arg = method(namespaces)
        else:
            arg = False
        #
        args.append(arg)
    #
    return getDirData(*args)


@lxTip.viewExceptionMethod
def setDirectory(
        logWin,
        collectionDataLis,
        isCollection,
        isIgnoreExists, isIgnoreTimeChanged,
        isWithTx,
        isAutoCache,
        isRepath):
    maxProgress = 6
    logWin.setMaxProgressValue(maxProgress)
    lxLog.viewStartProcessMessage(logWin, u'Directory Modify')
    # Step 01 ( Get Collection and Repath Data )
    lxLog.viewStartProcess(logWin, u'''Directory Statistical''')
    (
        collectionDataArray,
        referenceRepathDataArray,
        arRepathDataArray,
        otherRepathDataArray,
        mapRepathDataArray,
        furCacheRepathDataArray
    ) = getCollectionDataLis(
        logWin,
        collectionDataLis,
        isCollection, isRepath
    )
    lxLog.viewCompleteProcess(logWin)
    # Collection File(s)
    lxLog.viewStartProcess(logWin, u'''Collection File(s)''')
    #
    setCollectionFile(
        logWin,
        collectionDataArray,
        isIgnoreExists,
        isIgnoreTimeChanged,
        isWithTx
    )
    lxLog.viewCompleteProcess(logWin)
    # Repath Reference First ( Debug )
    lxLog.viewStartProcess(logWin, u'''Repath Reference Node''')
    if referenceRepathDataArray:
        progressExplain = u'''Repath Reference Node'''
        maxValue = len(referenceRepathDataArray)
        progress = lxProgress.viewSubProgress(progressExplain, maxValue)
        for node, osFile in referenceRepathDataArray:
            progress.updateProgress()
            setReferenceRepath(node, osFile)
        lxLog.viewCompleteProcess(logWin)
    else:
        lxLog.viewFailProcess(logWin, u'Non - Data ( Reference )')
    # Repath Assembly
    lxLog.viewStartProcess(logWin, u'''Repath Assembly - Reference Node''')
    if arRepathDataArray:
        sceneryArRepathDataArray = []
        arUnitRepathDataArray = []
        for node, osFile in arRepathDataArray:
            isScenery = not 'assembly/unit' in osFile.lower()
            if isScenery:
                sceneryArRepathDataArray.append((node, osFile))
            else:
                arUnitRepathDataArray.append((node, osFile))
        # Scenery
        if sceneryArRepathDataArray:
            progressExplain = u'''Repath Assembly - Reference ( Scenery ) Node'''
            maxValue = len(sceneryArRepathDataArray)
            progress = lxProgress.viewSubProgress(progressExplain, maxValue)
            for node, osFile in sceneryArRepathDataArray:
                progress.updateProgress()
                setAssemblyReferenceRepath(node, osFile)
        # Assembly Unit
        if arUnitRepathDataArray:
            progressExplain = u'''Repath Assembly - Reference ( Unit ) Node'''
            maxValue = len(arUnitRepathDataArray)
            progress = lxProgress.viewSubProgress(progressExplain, maxValue)
            for node, osFile in arUnitRepathDataArray:
                progress.updateProgress()
                setAssemblyReferenceRepath(node, osFile)
        lxLog.viewCompleteProcess(logWin)
    else:
        lxLog.viewFailProcess(logWin, u'Non - Data ( Assembly Reference )')
    # Step 05
    if isAutoCache is False:
        lxLog.viewStartProcess(logWin, u'''Repath Fur Cache and Fur Map''')
        #
        if mapRepathDataArray:
            progressExplain = u'''Repath Fur Map'''
            maxValue = len(mapRepathDataArray)
            progress = lxProgress.viewSubProgress(progressExplain, maxValue)
            for node, osFile, fileType in mapRepathDataArray:
                progress.updateProgress()
                setRepathFurMap(node, osFile)
        #
        lxLog.viewCompleteProcess(logWin)
        if not mapRepathDataArray:
            lxLog.viewFailProcess(logWin, u'Non - Data ( Fur Map )')
        #
        if furCacheRepathDataArray:
            progressExplain = u'''Repath Fur Cache'''
            maxValue = len(furCacheRepathDataArray)
            progress = lxProgress.viewSubProgress(progressExplain, maxValue)
            for node, sourceFile, targetFile, fileType in furCacheRepathDataArray:
                progress.updateProgress()
                setFurCacheRepath(node, sourceFile, targetFile, force=False)
        else:
            lxLog.viewFailProcess(logWin, u'Non - Data ( Fur Cache )')
    else:
        if mapRepathDataArray:
            progressExplain = u'''Repath Fur Map'''
            maxValue = len(mapRepathDataArray)
            progress = lxProgress.viewSubProgress(progressExplain, maxValue)
            for node, osFile, fileType in mapRepathDataArray:
                progress.updateProgress()
                setRepathFurMap(node, osFile, force=True)
        else:
            lxLog.viewFailProcess(logWin, u'Non - Data ( Fur Map )')
        #
        if furCacheRepathDataArray:
            progressExplain = u'''Repath Fur Cache'''
            maxValue = len(furCacheRepathDataArray)
            progress = lxProgress.viewSubProgress(progressExplain, maxValue)
            for node, sourceFile, targetFile, fileType in furCacheRepathDataArray:
                progress.updateProgress()
                setFurCacheRepath(node, sourceFile, targetFile, force=True)
        else:
            lxLog.viewFailProcess(logWin, u'Non - Data ( Fur Cache )')
    # Step 06 Other Nodes
    lxLog.viewStartProcess(logWin, u'''Repath Other Node ( Texture, DSO...)''')
    if otherRepathDataArray:
        progressExplain = u'''Repath Other Node ( Texture, DSO...)'''
        maxValue = len(otherRepathDataArray)
        progress = lxProgress.viewSubProgress(progressExplain, maxValue)
        for node, osFile, fileType in otherRepathDataArray:
            progress.updateProgress()
            setRepathGeneral(node, osFile, fileType)
        lxLog.viewCompleteProcess(logWin)
    else:
        lxLog.viewFailProcess(logWin, u'Non - Data ( Other Node )')
    #
    lxLog.viewCompleteProcessMessage(logWin)
    #
    # maFile.saveTempFile()


#
def getCollectionDataLis(
        logWin,
        collectionDataLis,
        isCollection,
        isRepath):
    collectionDataArray = []
    #
    referenceRepathDataArray = []
    arRepathDataArray = []
    otherRepathDataArray = []
    mapRepathDataArray = []
    furCacheRepathDataArray = []
    if collectionDataLis:
        lxLog.viewStartProcess(logWin, u'''Directory Statistical''')
        #
        progressExplain = u'''Directory Statistical'''
        maxValue = len(collectionDataLis)
        progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
        for fileType, nodes, osFileArray in collectionDataLis:
            progressBar.updateProgress(fileType)
            if osFileArray:
                # Debug Mult File in the Index 0 ( <UDIM>... ) for Repath
                sourceFile, targetFile = osFileArray[0]
                # Get Collection Data
                if isCollection:
                    if len(osFileArray) == 1:
                        collectionDataArray.append((sourceFile, targetFile, fileType))
                    elif len(osFileArray) > 1:
                        for i in osFileArray[1:]:
                            subSourceFile, subTargetFile = i
                            collectionDataArray.append((subSourceFile, subTargetFile, fileType))
                # Get Repath Data
                if isRepath:
                    progressExplain = '''Get Repath Data %s''' % lxBasic._toStringPrettify(fileType)
                    maxValue = len(nodes)
                    subProgressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
                    for seq, node in enumerate(nodes):
                        subProgressBar.updateProgress()
                        lxLog.viewStartSubProcess(logWin, 'Statistical Directory: ', node)
                        #
                        if fileType == 'reference':
                            referenceRepathDataArray.append((node, targetFile))
                        elif fileType == 'assemblyReference':
                            arRepathDataArray.append((node, targetFile))
                        elif fileType == 'furCache':
                            furCacheRepathDataArray.append((node, sourceFile, targetFile, fileType))
                        elif fileType == 'furMap':
                            mapRepathDataArray.append((node, targetFile, fileType))
                        else:
                            otherRepathDataArray.append((node, targetFile, fileType))
                        #
                        lxLog.viewCompleteSubProcess(logWin)
        #
        lxLog.viewCompleteProcess(logWin)
    #
    return collectionDataArray, referenceRepathDataArray, arRepathDataArray, otherRepathDataArray, mapRepathDataArray, furCacheRepathDataArray


#
def setCollectionFile(
        logWin,
        collectionData,
        isIgnoreExists, isIgnoreTimeChanged,
        isWithTx):
    def getCollectionEnable(sourceFile, targetFile, fileType):
        boolean = False
        if isIgnoreExists:
            if not lxBasic.isOsExistsFile(targetFile):
                boolean = True
            else:
                if not isIgnoreTimeChanged:
                    isChanged = lxBasic.getOsFileIsMtimeChanged(sourceFile, targetFile)
                    if isChanged:
                        boolean = True
        else:
            boolean = True
        return boolean
    #
    def setCollectionTx(sourceFile, targetFile, fileType):
        if fileType == 'texture':
            txExt = '.tx'
            sourceBase = lxBasic.getOsFileBase(sourceFile)
            sourceTx = '%s%s' % (sourceBase, txExt)
            targetBase = lxBasic.getOsFileBase(targetFile)
            targetTx = '%s%s' % (targetBase, txExt)
            #
            txEnable = getCollectionEnable(sourceTx, targetTx, fileType)
            if txEnable:
                lxLog.viewStartSubProcess(logWin, 'Collection : ', targetTx)
                sourceTxExists = lxBasic.isOsExistsFile(sourceTx)
                if sourceTxExists:
                    maFile.setCopyFile(sourceTx, targetTx)
                    lxLog.viewCompleteSubProcess(logWin)
                else:
                    lxLog.viewError(logWin, sourceTx, 'Non - Exists')
    #
    def setCollectionBranch(sourceFile, targetFile, fileType):
        enable = getCollectionEnable(sourceFile, targetFile, fileType)
        # Main File
        lxLog.viewStartSubProcess(logWin, 'Collection : ', targetFile)
        #
        if enable:
            lxBasic.setOsFileCopy(sourceFile, targetFile)
            lxLog.viewCompleteSubProcess(logWin)
        else:
            lxLog.viewWarning(logWin, targetFile, 'Is - Ignore')
        # Tx File
        if isWithTx:
            setCollectionTx(sourceFile, targetFile, fileType)
    #
    def setMain(data):
        if data:
            progressExplain = u'''Collection File(s)'''
            maxValue = len(data)
            progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
            for sourceFile, targetFile, fileType in data:
                progressBar.updateProgress(lxBasic._toStringPrettify(fileType))
                setCollectionBranch(sourceFile, targetFile, fileType)
    #
    setMain(collectionData)
