# coding=utf-8
from LxBasic import bscMethods, bscModifiers

from LxCore import lxBasic, lxCore_

from LxCore.preset.prod import sceneryPr

from LxMaya.command import maUtils, maFile, maHier, maAsb

from LxMaya.product.op import sceneryOp

none = ''


@bscModifiers.fncCatchException
@bscModifiers.fncCatchCostTime
def scnUnitCreateMainCmd(
        sceneryIndex,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
):
    logWin_ = bscMethods.If_Log(title=u'Scenery Create')
    logWin_.showUi()
    
    logWin_.addStartTask(u'Scenery Hierarchy Create')
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
    logWin_.addCompleteTask()


@bscModifiers.fncCatchException
@bscModifiers.fncCatchCostTime
def scnUnitLoadMainCmd(
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
):
    logWin_ = bscMethods.If_Log(title=u'Scenery Load')
    logWin_.showUi()

    logWin_.addStartTask(u'Scenery Load')

    if sceneryPr.isScnSceneryLink(sceneryStage):
        serverProductFile = sceneryPr.scnUnitProductFile(
            lxCore_.LynxiRootIndex_Server,
            projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
        )[1]
        localSourceFile = sceneryPr.scnUnitSourceFile(
            lxCore_.LynxiRootIndex_Local,
            projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
        )[1]
        if lxBasic.isOsExistsFile(serverProductFile):
            maFile.openMayaFileAsBack(serverProductFile, localSourceFile)
        else:
            scnUnitMaAssemblyLoadCmd(
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

            logWin_.addResult(localFile)

    elif sceneryPr.isScnLayoutLink(sceneryStage) or sceneryPr.isScnAnimationLink(sceneryStage) or sceneryPr.isScnSimulationLink(sceneryStage):
        pass

    elif sceneryPr.isScnLightLink(sceneryStage):
        pass

    maHier.setCreateScnRootHierarchy(sceneryClass, sceneryName, sceneryVariant)
    maHier.refreshScnRoot(sceneryClass, sceneryName, sceneryVariant, sceneryStage, sceneryIndex)

    logWin_.addCompleteTask()


#
def scnUnitMaAssemblyLoadCmd(
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        parentPath=None,
        withAssembly=False
):
    logWin_ = bscMethods.If_Log()
    
    serverFile = sceneryPr.scnUnitAssemblyComposeFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    datumLis = lxBasic.readOsJson(serverFile)
    if datumLis:
        progressExplain = u'''Build Scenery Compose Unit(s)'''
        maxValue = len(datumLis)
        progressBar = bscMethods.If_Progress(progressExplain, maxValue)
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
    logWin_ = bscMethods.If_Log()
    
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
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        parentPath=None
):
    logWin_ = bscMethods.If_Log()

    serverFile = sceneryPr.scnUnitAssemblyComposeFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    datumLis = lxBasic.readOsJson(serverFile)
    if datumLis:
        progressExplain = u'''Build Assembly Compose Unit(s)'''

        maxValue = len(datumLis)
        progressBar = bscMethods.If_Progress(progressExplain, maxValue)
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
                r, g, b = lxBasic.getRgbByString(assetName, maximum=1)
                #
                maUtils.setNodeOverrideRgb(objectPath, r, g, b)
                maUtils.setNodeOutlinerRgb(objectPath, r, g, b)


#
def scnUnitAssemblyLoadCmd(
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
):
    logWin_ = bscMethods.If_Log()
    
    composeFile = sceneryPr.scnUnitAssemblyComposeFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    locator = sceneryOp.setScnUnitLocatorCreate(sceneryName, sceneryVariant, composeFile)
    #
    scnUnitComposeLoadCmd_(
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
    logWin_ = bscMethods.If_Log()
    
    scnAssemblyReference = sceneryPr.scnAssemblyArName(sceneryClass, sceneryName, sceneryVariant) + '_0'
    serverSceneryAdFile = sceneryPr.scnUnitDefinitionFile(
        lxCore_.LynxiRootIndex_Server,
        projectName, sceneryClass, sceneryName, sceneryVariant, lxCore_.LynxiProduct_Scenery_Link_Scenery
    )[1]
    if lxBasic.isOsExistsFile(serverSceneryAdFile):
        maAsb.setAssemblyReferenceCreate(scnAssemblyReference, serverSceneryAdFile)
        sceneryOp.setAssembliesActiveSwitch(active)
        maHier.refreshScnBranch(
            scnAssemblyReference, sceneryClass, sceneryName, sceneryVariant, sceneryStage, sceneryIndex
        )
