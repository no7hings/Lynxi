# coding=utf-8
from LxBasic import bscMethods, bscModifiers, bscObjects

from LxCore import lxConfigure

from LxCore.preset.prod import sceneryPr

from LxMaya.command import maUtils, maFile, maHier, maAsb

from LxMaya.product.op import sceneryOp

none = ''


@bscModifiers.fncExceptionCatch
@bscModifiers.fncCostTimeCatch
def scnUnitCreateMainCmd(
        sceneryIndex,
        projectName,
        sceneryCategory, sceneryName, sceneryVariant, sceneryStage
):
    logWin_ = bscObjects.If_Log(title=u'Scenery Create')
    logWin_.showUi()
    
    logWin_.addStartTask(u'Scenery Hierarchy Create')
    #
    if sceneryPr.isSceneryLinkName(sceneryStage) or sceneryPr.isLayoutLinkName(sceneryStage):
        maHier.setCreateScnAssemblyHierarchy(sceneryCategory, sceneryName, sceneryVariant)

    elif sceneryPr.isAnimationLinkName(sceneryStage):
        pass

    elif sceneryPr.isLightLinkName(sceneryStage):
        pass
    #
    maHier.refreshScnRoot(sceneryCategory, sceneryName, sceneryVariant, sceneryStage, sceneryIndex)
    #
    logWin_.addCompleteTask()


@bscModifiers.fncExceptionCatch
@bscModifiers.fncCostTimeCatch
def scnUnitLoadMainCmd(
        projectName,
        sceneryIndex,
        sceneryCategory, sceneryName, sceneryVariant, sceneryStage
):
    logWin_ = bscObjects.If_Log(title=u'Scenery Load')
    logWin_.showUi()

    logWin_.addStartTask(u'Scenery Load')

    if sceneryPr.isSceneryLinkName(sceneryStage):
        serverProductFile = sceneryPr.scnUnitProductFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage
        )[1]
        localSourceFile = sceneryPr.scnUnitSourceFile(
            lxConfigure.LynxiRootIndex_Local,
            projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage
        )[1]
        if bscMethods.OsFile.isExist(serverProductFile):
            maFile.openMayaFileAsBack(serverProductFile, localSourceFile)
        else:
            scnUnitMaAssemblyLoadCmd(
                projectName,
                sceneryIndex,
                sceneryCategory, sceneryName, sceneryVariant, sceneryStage,
                withAssembly=True
            )
            #
            timeTag = bscMethods.OsTimetag.active()
            localFile = bscMethods.OsFile.toJoinTimetag(localSourceFile, timeTag)
            #
            maFile.saveToMayaFile(localFile)

            logWin_.addResult(localFile)

    elif sceneryPr.isLayoutLinkName(sceneryStage) or sceneryPr.isAnimationLinkName(sceneryStage) or sceneryPr.isSimulationLinkName(sceneryStage):
        pass

    elif sceneryPr.isLightLinkName(sceneryStage):
        pass

    maHier.setCreateScnRootHierarchy(sceneryCategory, sceneryName, sceneryVariant)
    maHier.refreshScnRoot(sceneryCategory, sceneryName, sceneryVariant, sceneryStage, sceneryIndex)

    logWin_.addCompleteTask()


#
def scnUnitMaAssemblyLoadCmd(
        projectName,
        sceneryIndex,
        sceneryCategory, sceneryName, sceneryVariant, sceneryStage,
        parentPath=None,
        withAssembly=False
):
    logWin_ = bscObjects.If_Log()
    
    serverFile = sceneryPr.scnUnitAssemblyComposeFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneryCategory, sceneryName, sceneryVariant, sceneryStage
    )[1]
    datumLis = bscMethods.OsJson.read(serverFile)
    if datumLis:
        progressExplain = u'''Build Scenery Compose Unit(s)'''
        maxValue = len(datumLis)
        progressBar = bscObjects.If_Progress(progressExplain, maxValue)
        for i in datumLis:
            progressBar.update()
            scnUnitMaAssemblyLoadSubCmd(
                projectName, sceneryName,
                i,
                parentPath=parentPath,
                withAssembly=withAssembly
            )


#
def scnUnitMaAssemblyLoadSubCmd(
        projectName,
        sceneryName,
        composeDatum,
        parentPath=None,
        withAssembly=False
):
    logWin_ = bscObjects.If_Log()
    
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
            logWin_.addResult(arRelativePath)


#
def scnUnitComposeLoadCmd_(
        projectName,
        sceneryIndex,
        sceneryCategory, sceneryName, sceneryVariant, sceneryStage,
        parentPath=None
):
    logWin_ = bscObjects.If_Log()

    serverFile = sceneryPr.scnUnitAssemblyComposeFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneryCategory, sceneryName, sceneryVariant, sceneryStage
    )[1]
    datumLis = bscMethods.OsJson.read(serverFile)
    if datumLis:
        progressExplain = u'''Build Assembly Compose Unit(s)'''

        maxValue = len(datumLis)
        progressBar = bscObjects.If_Progress(progressExplain, maxValue)
        for i in datumLis:
            progressBar.update()
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
                r, g, b = bscMethods.String.toRgb(assetName, maximum=1)
                #
                maUtils.setNodeOverrideRgb(objectPath, r, g, b)
                maUtils.setNodeOutlinerRgb(objectPath, r, g, b)


#
def scnUnitAssemblyLoadCmd(
        projectName,
        sceneryIndex,
        sceneryCategory, sceneryName, sceneryVariant, sceneryStage
):
    logWin_ = bscObjects.If_Log()
    
    composeFile = sceneryPr.scnUnitAssemblyComposeFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneryCategory, sceneryName, sceneryVariant, sceneryStage
    )[1]
    locator = sceneryOp.setScnUnitLocatorCreate(sceneryName, sceneryVariant, composeFile)
    #
    scnUnitComposeLoadCmd_(
        projectName,
        sceneryIndex,
        sceneryCategory, sceneryName, sceneryVariant, sceneryStage,
        parentPath=locator
    )
    #
    maHier.refreshScnRoot(sceneryCategory, sceneryName, sceneryVariant, sceneryStage, sceneryIndex)


#
def scnUnitAssemblyLoadByReferenceCmd(
        projectName,
        sceneryIndex,
        sceneryCategory, sceneryName, sceneryVariant, sceneryStage,
        active='GPU'
):
    logWin_ = bscObjects.If_Log()
    
    scnAssemblyReference = sceneryPr.scnAssemblyArName(sceneryCategory, sceneryName, sceneryVariant) + '_0'
    serverSceneryAdFile = sceneryPr.scnUnitDefinitionFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneryCategory, sceneryName, sceneryVariant, lxConfigure.LynxiProduct_Scenery_Link_Scenery
    )[1]
    if bscMethods.OsFile.isExist(serverSceneryAdFile):
        maAsb.setAssemblyReferenceCreate(scnAssemblyReference, serverSceneryAdFile)
        sceneryOp.setAssembliesActiveSwitch(active)
        maHier.refreshScnBranch(
            scnAssemblyReference, sceneryCategory, sceneryName, sceneryVariant, sceneryStage, sceneryIndex
        )
