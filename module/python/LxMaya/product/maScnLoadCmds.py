# coding=utf-8
from LxCore import lxBasic, lxConfigure, lxLog, lxTip, lxProgress
#
from LxCore.preset import appVariant
#
from LxCore.preset.prod import assetPr, sceneryPr
#
from LxMaya.command import maUtils, maAttr, maFile, maHier, maAsb, maGeom
#
from LxMaya.product.op import sceneryOp
#
none = ''


@lxTip.viewExceptionMethod
@lxTip.viewTimeMethod
def scnUnitCreateMainCmd(
        logWin,
        sceneryIndex,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage):
    lxLog.viewStartProcess(logWin, 'Create Assembly - Hierarchy')
    #
    if sceneryPr.isScnSceneryLink(sceneryStage) or sceneryPr.isScnLayoutLink(sceneryStage):
        maHier.setCreateScnAssemblyHierarchy(sceneryClass, sceneryName, sceneryVariant)
    elif sceneryPr.isScnAnimationLink(sceneryStage):
        pass
    elif sceneryPr.isScnLightLink(sceneryStage):
        pass
    #
    maHier.refreshScnRoot(sceneryClass, sceneryName, sceneryVariant, sceneryStage, sceneryIndex)
    #
    lxLog.viewCompleteProcess(logWin)


@lxTip.viewExceptionMethod
@lxTip.viewTimeMethod
def scnUnitLoadMainCmd(
        logWin,
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
):
    #
    lxLog.viewStartProcess(logWin, 'Load Scenery - Unit')
    if sceneryPr.isScnSceneryLink(sceneryStage):
        serverProductFile = sceneryPr.scnUnitProductFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
        )[1]
        localSourceFile = sceneryPr.scnUnitSourceFile(
            lxConfigure.LynxiRootIndex_Local,
            projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
        )[1]
        if lxBasic.isOsExistsFile(serverProductFile):
            maFile.openMayaFileAsBack(serverProductFile, localSourceFile)
        else:
            scnUnitMaAssemblyLoadCmd(
                logWin,
                projectName,
                sceneryIndex,
                sceneryClass, sceneryName, sceneryVariant, sceneryStage,
                withAssembly=True
            )
            #
            timeTag = lxBasic.getOsActiveTimeTag()
            localFile = lxBasic.getOsFileJoinTimeTag(localSourceFile, timeTag)
            #
            maFile.saveToMayaFile(localFile)
            lxLog.viewResult(logWin, localFile)
    elif sceneryPr.isScnLayoutLink(sceneryStage) or sceneryPr.isScnAnimationLink(sceneryStage) or sceneryPr.isScnSimulationLink(sceneryStage):
        pass
    elif sceneryPr.isScnLightLink(sceneryStage):
        pass
    #
    maHier.setCreateScnRootHierarchy(sceneryClass, sceneryName, sceneryVariant)
    maHier.refreshScnRoot(sceneryClass, sceneryName, sceneryVariant, sceneryStage, sceneryIndex)
    lxLog.viewCompleteProcess(logWin)


#
def scnUnitMaAssemblyLoadCmd(
        logWin,
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        parentPath=None,
        withAssembly=False
):
    serverFile = sceneryPr.scnUnitAssemblyComposeFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    datumLis = lxBasic.readOsJson(serverFile)
    if datumLis:
        progressExplain = u'''Build Scenery Compose Unit(s)'''
        maxValue = len(datumLis)
        progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
        for i in datumLis:
            progressBar.updateProgress()
            scnUnitMaAssemblyLoadSubCmd(
                logWin,
                projectName, sceneryName,
                i,
                parentPath=parentPath,
                withAssembly=withAssembly
            )


#
def scnUnitMaAssemblyLoadSubCmd(
        logWin,
        projectName,
        sceneryName,
        composeDatum,
        parentPath=None,
        withAssembly=False
):
    (
        (assetName, assetVariant),
        (arRelativePath, arNamespace, lodLevel, worldMatrix, worldBoundingBox, isVisible),
        (adFile, proxyCacheFile, gpuCacheFile, assetFile)
    ) = composeDatum
    #
    if parentPath is not None:
        arRelativePath = parentPath + '|' + arRelativePath
    #
    assemblyPath = maUtils._toNodeParentPath(arRelativePath)
    arName = maUtils._toNodeName(arRelativePath)
    if not maUtils.isAppExist(arRelativePath):
        if withAssembly is True:
            maUtils.setNodeParentPathCreate(arRelativePath)
            maAsb.setAssemblyReferenceCreate(arName, adFile)
            maUtils.setObjectParent('|' + arName, assemblyPath)
            #
            if 'assembly/unit/' in adFile:
                maAsb.setAssemblyLodLevel(arRelativePath, lodLevel)
            #
            maUtils.setNodeWorldMatrix(arRelativePath, worldMatrix)
            maUtils.setNodeVisible(arRelativePath, isVisible)
            #
            lxLog.viewResult(logWin, arRelativePath)


#
def scnUnitComposeLoadCmd_(
        logWin,
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        parentPath=None
):
    serverFile = sceneryPr.scnUnitAssemblyComposeFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    datumLis = lxBasic.readOsJson(serverFile)
    if datumLis:
        progressExplain = u'''Build Assembly Compose Unit(s)'''
        progressBar = maUtils.MaProgressBar()
        maxValue = len(datumLis)
        progressBar.viewProgress(progressExplain, maxValue)
        for i in datumLis:
            progressBar.updateProgress()
            #
            (
                (assetName, assetVariant),
                (arRelativePath, arNamespace, lodLevel, worldMatrix, worldBoundingBox, isVisible),
                (adFile, proxyCacheFile, gpuCacheFile, assetFile)
            ) = i
            #
            if 'assembly/unit/' in adFile.lower():
                if parentPath is not None:
                    objectPath = maUtils._toNodePathString([parentPath, arRelativePath])
                else:
                    objectPath = arRelativePath
                #
                lod = int(lodLevel[-2:])
                #
                assemblyMethod = maAsb.LxAssemblyMethod(objectPath)
                #
                assemblyMethod.create(
                    proxyCacheFile=proxyCacheFile, gpuCacheFile=gpuCacheFile, assetFile=assetFile,
                    lod=lod
                )
                assemblyMethod.updateGeometry(
                    worldMatrix, worldBoundingBox
                )
                #
                r, g, b = lxBasic.getRgbByString(assetName, maximum=1)
                #
                maUtils.setNodeOverrideRgb(objectPath, r, g, b)
                maUtils.setNodeOutlinerRgb(objectPath, r, g, b)


#
def scnUnitAssemblyLoadCmd(
        logWin,
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
):
    composeFile = sceneryPr.scnUnitAssemblyComposeFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    locator = sceneryOp.setScnUnitLocatorCreate(sceneryName, sceneryVariant, composeFile)
    #
    scnUnitComposeLoadCmd_(
        logWin,
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        parentPath=locator
    )
    #
    maHier.refreshScnRoot(sceneryClass, sceneryName, sceneryVariant, sceneryStage, sceneryIndex)


#
def scnUnitAssemblyLoadByReferenceCmd(
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        active='GPU'
):
    scnAssemblyReference = sceneryPr.scnAssemblyArName(sceneryClass, sceneryName, sceneryVariant) + '_0'
    serverSceneryAdFile = sceneryPr.scnUnitDefinitionFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneryClass, sceneryName, sceneryVariant, lxConfigure.LynxiProduct_Scenery_Link_Scenery
    )[1]
    if lxBasic.isOsExistsFile(serverSceneryAdFile):
        maAsb.setAssemblyReferenceCreate(scnAssemblyReference, serverSceneryAdFile)
        sceneryOp.setAssembliesActiveSwitch(active)
        maHier.refreshScnBranch(
            scnAssemblyReference, sceneryClass, sceneryName, sceneryVariant, sceneryStage, sceneryIndex
        )
