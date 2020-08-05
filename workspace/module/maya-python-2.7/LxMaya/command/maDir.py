# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxBasic import bscMtdCore, bscMethods, bscModifiers, bscObjects
#
from LxCore.config import appCfg
#
from LxMaya.command import maUtils, maTxtr, maFur, maAsb, maProxy, maAbc, maGeomCache, maArnold
#
none = ''


#
def getLinkDicMethod(dic, nodepathString, fileString_):
    fileString_ = fileString_.replace('\\', '/')
    fileString_ = bscMethods.OsFile.reduceFilename(fileString_)
    #
    key = fileString_.lower()
    dic.setdefault(key, []).append((nodepathString, fileString_))


#
def getTextureLinkDic(nodes=None):
    dic = bscMtdCore.orderedDict()
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
    base, ext = bscMethods.OsFile.toExtSplit(texture)
    txTexture = '%s%s' % (base, appCfg.MaArnoldTxExt)
    return txTexture


#
def getFurMapLinkDic(nodes=None):
    dic = bscMtdCore.orderedDict()
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
            if maUtils._getNodeShapeCategoryString(objectPath) == appCfg.MaNodeType_Plug_Yeti:
                shapePath = maUtils._dcc_getNodShapeNodepathStr(objectPath)
                mapNodes = cmds.pgYetiGraph(shapePath, listNodes=1, type='texture')
                if mapNodes:
                    for node in mapNodes:
                        furMapFile = cmds.pgYetiGraph(shapePath, node=node, param='file_name', getParamValue=1)
                        mapNodePath = '%s - %s' % (shapePath, node)
                        #
                        getLinkDicMethod(dic, mapNodePath, furMapFile)
            # Pfx Hair's Map
            elif maUtils._getNodeShapeCategoryString(objectPath) == appCfg.MaPfxHairType:
                mapNodes = maUtils.getPfxHairMapNodes(objectPath)
                if mapNodes:
                    for node in mapNodes:
                        furMapFile = maTxtr.getTextureNodeAttrData(node)
                        #
                        getLinkDicMethod(dic, node, furMapFile)
            # Nurbs Hair's Map
            elif maUtils._getNodeShapeCategoryString(objectPath) == appCfg.MaNodeType_Plug_NurbsHair:
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
    dic = bscMtdCore.orderedDict()
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
def setReferenceRepath(nodepathString, fileString_):
    sourceFile = maUtils.getReferenceFile(nodepathString, useMode=1)
    if not bscMethods.OsFile.isSame(sourceFile, fileString_):
        maUtils.setReloadReferenceFile(nodepathString)
        maUtils.setLoadReferenceFile(nodepathString, fileString_)


# Assembly Reference
def getAssemblyReferenceNodeLis(filterNamespace=None):
    filterType = appCfg.DEF_mya_type_assembly_reference
    return maUtils.getNodeLisByFilter(filterType, filterNamespace)


#
def getAsbRefLinkDic(nodes=None):
    dic = bscMtdCore.orderedDict()
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
def setAssemblyReferenceRepath(nodepathString, fileString_):
    attrName = 'definition'
    #
    sourceFile = maUtils.getAttrDatum(nodepathString, attrName)
    if not bscMethods.OsFile.isSame(sourceFile, fileString_):
        maUtils.setAttrStringDatum(nodepathString, attrName, fileString_)


# Proxy ( Arnold )
def getArnoldProxyLis(filterNamespace=None):
    filterType = appCfg.MaNodeType_AiStandIn
    return maUtils.getNodeLisByFilter(filterType, filterNamespace)


#
def getProxyCacheLinkDic(nodes=None):
    dic = bscMtdCore.orderedDict()
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
def setProxyCacheRepath(nodepathString, fileString_):
    attrName = 'dso'
    sourceFile = maUtils.getAttrDatum(nodepathString, attrName)
    if not bscMethods.OsFile.isSame(sourceFile, fileString_):
        maUtils.setAttrStringDatum(nodepathString, attrName, fileString_)


#
def getVolumeCacheNodeLis(filterNamespace=None):
    filterType = appCfg.MaNodeType_AiVolume
    return maUtils.getNodeLisByFilter(filterType, filterNamespace)


#
def getVolumeCacheLinkDic(nodes=None):
    dic = bscMtdCore.orderedDict()
    #
    usedData = []
    if nodes:
        usedData = nodes
    if not usedData:
        usedData = getVolumeCacheNodeLis()
    if usedData:
        for node in usedData:
            if maUtils._getNodeCategoryString(node) == appCfg.MaNodeType_AiVolume:
                fileString = maArnold.getVolumeCacheFile(node)
                if fileString:
                    getLinkDicMethod(dic, node, fileString)
    return dic


#
def setVolumeCacheRepath(nodepathString, fileString_):
    attrName = 'filename'
    sourceFile = maUtils.getAttrDatum(nodepathString, attrName)
    if not bscMethods.OsFile.isSame(sourceFile, fileString_):
        maUtils.setAttrStringDatum(nodepathString, attrName, fileString_)


# GPU Cache
def getGpuCacheNodeLis(filterNamespace=None):
    filterType = appCfg.MaGpuCache
    return maUtils.getNodeLisByFilter(filterType, filterNamespace)


#
def getGpuCacheLinkDic(nodes=None):
    dic = bscMtdCore.orderedDict()
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
def setGpuCacheRepath(nodepathString, fileString_):
    attrName = 'cacheFileName'
    #
    sourceFile = maUtils.getAttrDatum(nodepathString, attrName)
    if not bscMethods.OsFile.isSame(sourceFile, fileString_):
        maUtils.setAttrStringDatum(nodepathString, attrName, fileString_)


# Alembic Cache
def getAlembicCacheNodeLis(filterNamespace=None):
    filterType = appCfg.DEF_mya_type_alembic
    return maUtils.getNodeLisByFilter(filterType, filterNamespace)


#
def getAlembicCacheLinkDic(nodes=None):
    dic = bscMtdCore.orderedDict()
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
def setRepathAlembicCache(nodepathString, fileString_):
    attrName = 'abc_File'
    #
    sourceFile = maUtils.getAttrDatum(nodepathString, attrName)
    if not bscMethods.OsFile.isSame(sourceFile, fileString_):
        maUtils.setAttrStringDatum(nodepathString, attrName, fileString_)


#
def getYetiShapeLis():
    return maUtils.getNodeLisByType(appCfg.MaNodeType_Plug_Yeti)


#
def getFurCacheNodeLis(filterNamespace=None):
    filterType = appCfg.MaFurCacheNodeTypes
    return maUtils.getNodeLisByFilter(filterType, filterNamespace)


#
def getFurCacheLinkDic(nodes=None):
    dic = bscMtdCore.orderedDict()
    #
    usedData = []
    if nodes:
        usedData = nodes
    if not usedData:
        usedData = getFurCacheNodeLis()
    if usedData:
        for node in usedData:
            if maUtils._getNodeShapeCategoryString(node) == appCfg.MaNodeType_Plug_Yeti:
                yetiCacheFile = maFur.getYetiCacheFile(node)
                if yetiCacheFile:
                    getLinkDicMethod(dic, node, yetiCacheFile)
            elif maUtils._getNodeShapeCategoryString(node) == appCfg.MaNodeType_Plug_NurbsHair:
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
    dic = bscMtdCore.orderedDict()
    #
    usedData = []
    if nodes:
        usedData = nodes
    if not usedData:
        usedData = getGeomCacheNodeLis()
    if usedData:
        for node in usedData:
            if maUtils._getNodeCategoryString(node) == appCfg.MaNodeType_CacheFile:
                geomCacheFiles = maGeomCache.getGeomCacheFile(node)
                if geomCacheFiles:
                    geomCacheXmlFile, geomCacheFile = geomCacheFiles
                    #
                    getLinkDicMethod(dic, node, geomCacheXmlFile)
                    getLinkDicMethod(dic, node, geomCacheFile)
    return dic


#
def setFurCacheRepath(nodepathString, sourceFile, targetFile, force=False):
    nodeType = maUtils._getNodeCategoryString(nodepathString)
    if nodeType == appCfg.MaNodeType_Plug_Yeti:
        setRepathYetiCache(nodepathString, sourceFile, targetFile, force)
    elif nodeType == appCfg.MaNodeType_Plug_NurbsHair:
        maFur.setNhrCacheObjectReadCache(nodepathString, targetFile)


#
def setRepathGeomCache(nodepathString, fileString_):
    if maUtils._getNodeCategoryString(nodepathString) == 'cacheFile':
        maGeomCache.setRepathGeometryCache(nodepathString, fileString_)


#
def getYetiCacheRange(fileString_):
    startFrame = 0
    endFrame = 0

    existFrameLis = bscMethods.OsMultifile.existFrames(fileString_)
    if existFrameLis:
        startFrame = int(min(existFrameLis))
        endFrame = int(max(existFrameLis))
    return startFrame, endFrame


#
def setRepathYetiCache(nodepathString, sourceFile, targetFile, force=False):
    if force:
        startFrame, endFrame = getYetiCacheRange(sourceFile)
        sample = 3
        maFur.setYetiNodeWriteCache(
            targetFile, nodepathString,
            startFrame, endFrame, sample,
            isUpdateViewport=0,
            isGeneratePreview=0
        )
    #
    maFur.setYetiConnectCache(nodepathString, targetFile)


#
def setRepathGeneral(nodepathString, fileString_, fileType):
    if fileType == 'texture':
        setTextureRepath(nodepathString, fileString_)
    elif fileType == 'assemblyReference':
        setAssemblyReferenceRepath(nodepathString, fileString_)
    elif fileType == 'proxyCache':
        setProxyCacheRepath(nodepathString, fileString_)
    elif fileType == 'volumeCache':
        setVolumeCacheRepath(nodepathString, fileString_)
    elif fileType == 'gpuCache':
        setGpuCacheRepath(nodepathString, fileString_)
    elif fileType == 'alembicCache':
        setRepathAlembicCache(nodepathString, fileString_)
    elif fileType == 'geometryCache':
        setRepathGeomCache(nodepathString, fileString_)


#
def setTextureRepath(nodepathString, fileString_):
    # Mast Lower
    fileString_ = fileString_.replace('<UDIM>', '<udim>')
    maTxtr.setTextureAttr(nodepathString, fileString_)


#
def setRepathFurMap(nodepathString, fileString_, force=False):
    # Must Upper
    fileString_ = fileString_.replace('<udim>', '<UDIM>')
    maTxtr.setMapAttr(nodepathString, fileString_, force)


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
            for osFileKey, linkDatumLis in data.items():
                osPath = bscMethods.OsFile.dirname(osFileKey)
                if not osPath in osPathLis:
                    osPathLis.append(osPath)
                    osPathLis.append(osPath)
                #
                if linkDatumLis:
                    nodes = []
                    #
                    fileString_ = linkDatumLis[0][1]
                    for node, subOsFile in linkDatumLis:
                        nodes.append(node)
                    #
                    osFileDic.setdefault(osPath, []).append((fileType, fileString_, nodes))
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
        withTx=False
):
    def getBranch(key, value):
        def getExistsFile(fileString_):
            if not fileString_ in lis:
                lis.append(fileString_)
                if fileType == 'texture':
                    if withTx:
                        txTextureFile = getTxTexture(fileString_)
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
            for osFileKey, linkDatumLis in data.items():
                if linkDatumLis:
                    for node, fileString in linkDatumLis:
                        existFileLis = bscMethods.OsMultifile.existFiles(fileString)
                        if existFileLis:
                            [getExistsFile(i) for i in existFileLis]
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


@bscModifiers.fncExceptionCatch
def setDirectoryModifyCmd(
        collectionDataLis,
        isCollection,
        isIgnoreExists, isIgnoreTimeChanged,
        isWithTx,
        isAutoCache,
        isRepath
):
    logWin_ = bscObjects.LogWindow(u'Directory Modify')
    logWin_.addStartTask(u'Directory Modify')
    # Step 01 ( Get Collection and Repath Data )
    logWin_.addStartProgress(u'''Directory Statistical''')
    (
        collectionDataArray,
        referenceRepathDataArray,
        arRepathDataArray,
        otherRepathDataArray,
        mapRepathDataArray,
        furCacheRepathDataArray
    ) = getDirectoryModifyData(
        collectionDataLis,
        isCollection, isRepath
    )
    logWin_.addCompleteProgress()
    # Collection File(s)
    logWin_.addStartProgress(u'''Collection File(s)''')
    #
    setFileCollectionCmd(
        collectionDataArray,
        isIgnoreExists,
        isIgnoreTimeChanged,
        isWithTx
    )
    logWin_.addCompleteProgress()
    # Repath Reference First ( Debug )
    logWin_.addStartProgress(u'''Reference Node Repath ''')
    if referenceRepathDataArray:
        progressExplain = u'''Repath Reference Node'''
        maxValue = len(referenceRepathDataArray)
        progress = bscObjects.ProgressWindow(progressExplain, maxValue)
        for node, fileString_ in referenceRepathDataArray:
            progress.update()
            setReferenceRepath(node, fileString_)
        logWin_.addCompleteProgress()
    else:
        logWin_.addWarning(u'Non - Data ( Reference )')
    # Repath Assembly
    logWin_.addStartProgress(u'''Assembly - Reference Node Repath''')
    if arRepathDataArray:
        sceneryArRepathDataArray = []
        arUnitRepathDataArray = []
        for node, fileString_ in arRepathDataArray:
            isScenery = not 'assembly/unit' in fileString_.lower()
            if isScenery:
                sceneryArRepathDataArray.append((node, fileString_))
            else:
                arUnitRepathDataArray.append((node, fileString_))
        # Scenery
        if sceneryArRepathDataArray:
            progressExplain = u'''Repath Assembly - Reference ( Scenery ) Node'''
            maxValue = len(sceneryArRepathDataArray)
            progress = bscObjects.ProgressWindow(progressExplain, maxValue)
            for node, fileString_ in sceneryArRepathDataArray:
                progress.update()
                setAssemblyReferenceRepath(node, fileString_)
        # Assembly Unit
        if arUnitRepathDataArray:
            progressExplain = u'''Repath Assembly - Reference ( Unit ) Node'''
            maxValue = len(arUnitRepathDataArray)
            progress = bscObjects.ProgressWindow(progressExplain, maxValue)
            for node, fileString_ in arUnitRepathDataArray:
                progress.update()
                setAssemblyReferenceRepath(node, fileString_)
        logWin_.addCompleteProgress()
    else:
        logWin_.addWarning(u'Non - Data ( Assembly Reference )')
    # Step 05
    if isAutoCache is False:
        logWin_.addStartProgress(u'''Fur Cache and Fur Map Repath''')
        #
        if mapRepathDataArray:
            progressExplain = u'''Repath Fur Map'''
            maxValue = len(mapRepathDataArray)
            progress = bscObjects.ProgressWindow(progressExplain, maxValue)
            for node, fileString_, fileType in mapRepathDataArray:
                progress.update()
                setRepathFurMap(node, fileString_)
        #
        logWin_.addCompleteProgress()
        if not mapRepathDataArray:
            logWin_.addWarning(u'Non - Data ( Fur Map )')
        #
        if furCacheRepathDataArray:
            progressExplain = u'''Repath Fur Cache'''
            maxValue = len(furCacheRepathDataArray)
            progress = bscObjects.ProgressWindow(progressExplain, maxValue)
            for node, sourceFile, targetFile, fileType in furCacheRepathDataArray:
                progress.update()
                setFurCacheRepath(node, sourceFile, targetFile, force=False)
        else:
            logWin_.addWarning(u'Non - Data ( Fur Cache )')
    else:
        if mapRepathDataArray:
            progressExplain = u'''Repath Fur Map'''
            maxValue = len(mapRepathDataArray)
            progress = bscObjects.ProgressWindow(progressExplain, maxValue)
            for node, fileString_, fileType in mapRepathDataArray:
                progress.update()
                setRepathFurMap(node, fileString_, force=True)
        else:
            logWin_.addWarning(u'Non - Data ( Fur Map )')
        #
        if furCacheRepathDataArray:
            progressExplain = u'''Repath Fur Cache'''
            maxValue = len(furCacheRepathDataArray)
            progress = bscObjects.ProgressWindow(progressExplain, maxValue)
            for node, sourceFile, targetFile, fileType in furCacheRepathDataArray:
                progress.update()
                setFurCacheRepath(node, sourceFile, targetFile, force=True)
        else:
            logWin_.addWarning(u'Non - Data ( Fur Cache )')
    # Step 06 Other Nodes
    logWin_.addStartProgress(u'''Other Node ( Texture, DSO...) Repath''')
    if otherRepathDataArray:
        progressExplain = u'''Repath Other Node ( Texture, DSO...)'''
        maxValue = len(otherRepathDataArray)
        progress = bscObjects.ProgressWindow(progressExplain, maxValue)
        for node, fileString_, fileType in otherRepathDataArray:
            progress.update()
            setRepathGeneral(node, fileString_, fileType)
        logWin_.addCompleteProgress()
    else:
        logWin_.addWarning(u'Non - Data ( Other Node )')
    #
    logWin_.addCompleteProgress()
    #
    # maFile.saveTempFile()


#
def getDirectoryModifyData(
        collectionDataLis,
        isCollection,
        isRepath
):
    logWin_ = bscObjects.LogWindow()
    
    collectionDataArray = []

    referenceRepathDataArray = []
    arRepathDataArray = []
    otherRepathDataArray = []
    mapRepathDataArray = []
    furCacheRepathDataArray = []
    if collectionDataLis:
        logWin_.addStartProgress(u'''Directory Statistical''')

        progressExplain = u'''Directory Statistical'''
        maxValue = len(collectionDataLis)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for fileType, nodes, osFileArray in collectionDataLis:
            progressBar.update(fileType)
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
                    progressExplain = '''Get Repath Data %s''' % bscMethods.StrCamelcase.toPrettify(fileType)
                    maxValue = len(nodes)
                    subProgressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
                    for seq, node in enumerate(nodes):
                        subProgressBar.update()
                        logWin_.addStartProgress(u'Statistical Directory', node)
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
                        logWin_.addCompleteProgress()

        logWin_.addCompleteProgress()

    return collectionDataArray, referenceRepathDataArray, arRepathDataArray, otherRepathDataArray, mapRepathDataArray, furCacheRepathDataArray


#
def setFileCollectionCmd(
        collectionData,
        isIgnoreExists, isIgnoreTimeChanged,
        isWithTx
):
    def getCollectionEnable(sourceFile, targetFile, fileType):
        boolean = False
        if isIgnoreExists:
            if not bscMethods.OsFile.isExist(targetFile):
                boolean = True
            else:
                if not isIgnoreTimeChanged:
                    isChanged = bscMethods.OsFile.isFileTimeChanged(sourceFile, targetFile)
                    if isChanged:
                        boolean = True
        else:
            boolean = True
        return boolean
    #
    def setCollectionTx(sourceFile, targetFile, fileType):
        if fileType == 'texture':
            txExt = '.tx'
            sourceBase = bscMethods.OsFile.base(sourceFile)
            sourceTx = '%s%s' % (sourceBase, txExt)
            targetBase = bscMethods.OsFile.base(targetFile)
            targetTx = '%s%s' % (targetBase, txExt)
            #
            txEnable = getCollectionEnable(sourceTx, targetTx, fileType)
            if txEnable:
                logWin_.addStartProgress(u'Collection', targetTx)
                sourceTxExists = bscMethods.OsFile.isExist(sourceTx)
                if sourceTxExists:
                    bscMethods.OsFile.copyTo(sourceTx, targetTx)
                    logWin_.addCompleteProgress()
                else:
                    logWin_.addError(sourceTx, 'Non - Exists')
    #
    def setCollectionBranch(sourceFile, targetFile, fileType):
        enable = getCollectionEnable(sourceFile, targetFile, fileType)
        # Main File
        logWin_.addStartProgress(u'Collection', targetFile)
        #
        if enable:
            bscMethods.OsFile.copyTo(sourceFile, targetFile)
            logWin_.addCompleteProgress()
        else:
            logWin_.addWarning(targetFile, 'Is - Ignore')
        # Tx File
        if isWithTx:
            setCollectionTx(sourceFile, targetFile, fileType)
    #
    def setMain(data):
        if data:
            progressExplain = u'''Collection File(s)'''
            maxValue = len(data)
            progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
            for sourceFile, targetFile, fileType in data:
                progressBar.update(bscMethods.StrCamelcase.toPrettify(fileType))
                setCollectionBranch(sourceFile, targetFile, fileType)

    logWin_ = bscObjects.LogWindow()

    setMain(collectionData)
