# coding=utf-8
from LxCore import lxBasic, lxConfigure, lxLog, lxTip
#
from LxCore.preset import appVariant
#
from LxCore.preset.prod import projectPr, assetPr, sceneryPr
#
from LxDatabase import dbGet, dbBasic
#
from LxMaya.command import maUtils, maFile, maShdr, maTxtr, maHier, maRender, maAsb, maFur
#
from LxMaya.product.data import datAsset
#
from LxMaya.product.op import assetOp
#
from LxMaya.database import maDbAstCmds
#
none = ''


@lxTip.viewExceptionMethod
@lxTip.viewTimeMethod
def astUnitModelCreateMainCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        isUseExistsHierarchy=False
):
    # Set Log Window
    logWin.setNameText(u'模型创建')
    lxLog.viewStartProcessMessage(logWin, 'Asset Model Create')
    #
    existsHierarchy = None
    #
    if isUseExistsHierarchy:
        selObjects = maUtils.getSelectedObjects()
        if selObjects:
            existsHierarchy = selObjects[0]
    #
    lxLog.viewStartProcess(logWin, 'Create Model - Hierarchy')
    #
    maHier.setCreateAstModelHierarchy(assetClass, assetName)
    maHier.setCreateAstUnitModelSolverHierarchy(assetClass, assetName)
    #
    astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName)
    maHier.refreshHierarchyBranch(
        astUnitModelProductGroup,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage
    )
    #
    if existsHierarchy:
        maUtils.setObjectParent(existsHierarchy, astUnitModelProductGroup)
    #
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage
    )
    #
    lxLog.viewCompleteProcess(logWin)
    lxLog.viewCompleteProcessMessage(logWin)
    #
    logWin.setCountdownClose(5)


@lxTip.viewExceptionMethod
@lxTip.viewTimeMethod
def astUnitModelLoadMainCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        force=True, lockTransform=True, collectionTexture=True,
):
    # Set Log Window
    logWin.setNameText(u'模型领取')
    # Start
    lxLog.viewStartLoadMessage(logWin)
    maUtils.setDisplayMode(5)
    #
    if force:
        maFile.new()
    #
    astUnitModelGeometryLoadCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        lockTransform=lockTransform
    )
    #
    astUnitModelMaterialLoadCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        collectionTexture=collectionTexture
    )
    # Extra >>> 4
    astUnitLoadExtraSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )
    # Create Root
    maHier.setCreateAstRootHierarchy(
        assetClass, assetName
    )
    # Refresh Root
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage
    )
    # Save Source to Local
    saveModelSource(logWin, projectName, assetClass, assetName, assetVariant, assetStage)
    # Complete
    lxLog.viewCompleteLoadMessage(logWin)
    #
    logWin.setCountdownClose(5)


#
def saveModelSource(
        logWin,
        projectName,
        assetClass, assetName, assetVariant, assetStage
):
    # Local
    localModelFile = assetPr.astUnitSourceFile(
        lxConfigure.LynxiRootIndex_Local,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    # Save to Local
    maUtils.setVisiblePanelsDelete()
    assetOp.setUnknownNodeClear()
    #
    lxLog.viewStartProcess(logWin, 'Save Model - Source ( Local )')
    #
    maFile.saveMayaFileToLocal(localModelFile)
    #
    lxLog.viewCompleteProcess(logWin)


#
def astUnitModelGeometryLoadCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        lockTransform=True
):
    isDbExists = dbGet.isDbAstExistsGeometry(assetIndex)
    if isDbExists:
        lxLog.viewStartProcess(logWin, 'Load Asset Model Geometry')
        #
        maDbAstCmds.dbAstGeometryLoadMainCmd(assetIndex, assetName, lockTransform)
        #
        lxLog.viewCompleteProcess(logWin)
        # Hide Solver Meshes
        assetOp.setSolverGroupGeometryHide(assetName)
    else:
        astUnitModelCreateMainCmd(
            logWin,
            projectName,
            assetIndex,
            assetClass, assetName, assetVariant, assetStage
        )


#
def astUnitModelMaterialLoadCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        collectionTexture=False, useServerTexture=False
):
    assetSubIndexKey = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
    isDbExists = dbGet.isDbAstMaterialExists(assetSubIndexKey)
    if isDbExists:
        renderer = projectPr.getProjectMayaRenderer(projectName)
        maRender.setLoadRenderer(renderer)
        #
        geometryObjectIndexLis = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
        astMaterialObjectIndexLis = dbGet.getDbMaterialIndexData(assetSubIndexKey)
        lxLog.viewStartProcess(logWin, u'Load Asset Model ( Material )')
        #
        maDbAstCmds.dbAstMaterialLoadMainCmd(assetSubIndexKey, geometryObjectIndexLis, astMaterialObjectIndexLis)
        #
        lxLog.viewCompleteProcess(logWin)
        # Load Texture >>> 02
        if collectionTexture:
            # Use Server Path
            if useServerTexture:
                modelTextureDirectory = assetPr.astUnitTextureFolder(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    assetClass, assetName, assetVariant, assetStage
                )
                isBackExists = False
            else:
                modelTextureDirectory = assetPr.astUnitTextureFolder(
                    lxConfigure.LynxiRootIndex_Local,
                    projectName,
                    assetClass, assetName, assetVariant, assetStage
                )
                isBackExists = True
            #
            lxLog.viewStartProcess(logWin, 'Load Model - Texture')
            #
            shaderObjects = datAsset.getAstMeshObjects(assetName, 1)
            # Debug ( Must Back of Rename Scene)
            modelTextureNodes = maShdr.getTextureNodeLisByObject(shaderObjects)
            #
            withTx = maTxtr.getTxTextureIsCollection(renderer)
            maTxtr.setTexturesCollection(
                modelTextureDirectory,
                withTx=withTx,
                inData=modelTextureNodes,
                backupExists=isBackExists
            )
            # Repath Texture
            maTxtr.setTexturesRepath(
                modelTextureDirectory,
                inData=modelTextureNodes
            )
            #
            lxLog.viewCompleteProcess(logWin)
        #
        astAovObjectIndexLis = dbGet.getDbAovIndexData(assetSubIndexKey)
        if astAovObjectIndexLis:
            lxLog.viewStartProcess(logWin, u'Load Asset Model ( AOV )')
            #
            maDbAstCmds.dbAstLoadAov(renderer, assetSubIndexKey, astAovObjectIndexLis)
            #
            lxLog.viewCompleteProcess(logWin)
        else:
            lxLog.viewFailProcess(logWin, u'Asset Model ( AOV ) is Non - Exists')
        # Collection Bridge Group
        astUnitModelLinkGroup = assetPr.astUnitModelLinkGroupName(assetName)
        astUnitModelBridgeGroup = assetPr.astUnitModelBridgeGroupName(assetName)
        maUtils.setObjectParent(astUnitModelBridgeGroup, astUnitModelLinkGroup)
    else:
        lxLog.viewFailProcess(logWin, u'Asset Model ( Material ) is Non - Exists')


#
def astUnitLoadModelTexture(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        useServerTexture=False):
    # Use Server Path
    if useServerTexture:
        modelTextureDirectory = assetPr.astUnitTextureFolder(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )
        isBackExists = False
    else:
        modelTextureDirectory = assetPr.astUnitTextureFolder(
            lxConfigure.LynxiRootIndex_Local,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )
        isBackExists = True
    #
    shaderObjectLis = datAsset.getAstMeshObjects(assetName, 1)
    # Debug ( Must Back of Rename Scene)
    textureNodeLis = maShdr.getTextureNodeLisByObject(shaderObjectLis)
    #
    renderer = projectPr.getProjectMayaRenderer(projectName)
    #
    withTx = maTxtr.getTxTextureIsCollection(renderer)
    #
    lxLog.viewStartProcess(logWin, 'Load Asset Model ( Texture )')
    #
    maTxtr.setTexturesCollection(
        modelTextureDirectory,
        withTx=withTx,
        inData=textureNodeLis,
        backupExists=isBackExists
    )
    # Repath Texture
    maTxtr.setTexturesRepath(
        modelTextureDirectory,
        inData=textureNodeLis
    )
    lxLog.viewCompleteProcess(logWin)


# Crate Rig File
@lxTip.viewExceptionMethod
@lxTip.viewTimeMethod
def astUnitRigCreateMainCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage
):
    logWin.setNameText(u'绑定创建')
    #
    isLoadMesh = dbGet.isDbAstExistsGeometry(assetIndex)
    modelIndex = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
    isLoadMaterial = dbGet.isDbAstMaterialExists(modelIndex)
    #
    maxProgress = [0, 1][isLoadMesh] + [0, 2][isLoadMaterial]
    logWin.setMaxProgressValue(maxProgress)
    # Start
    lxLog.viewStartLoadMessage(logWin)
    maUtils.setDisplayMode(5)
    #
    astUnitModelGeometryLoadCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        lockTransform=False
    )
    #
    astUnitModelMaterialLoadCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        collectionTexture=True,
        useServerTexture=True
    )
    # Extra
    astUnitLoadExtraSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )
    #
    maHier.setCreateAstRigHierarchy(assetClass, assetName)
    #
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage
    )
    #
    saveRigSource(
        logWin,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )
    # Complete
    lxLog.viewCompleteLoadMessage(logWin)


# Animation Rig Load
@lxTip.viewExceptionMethod
@lxTip.viewTimeMethod
def astUnitLoadRigMain(
        logWin,
        assetIndex,
        projectName, assetClass, assetName, assetVariant, assetStage,
        force=True
):
    # Set Log Window
    logWin.setNameText(u'绑定领取')
    maxProgress = 1
    logWin.setMaxProgressValue(maxProgress)
    # Start
    lxLog.viewStartLoadMessage(logWin)
    maUtils.setDisplayMode(5)
    #
    dbRigFile = dbGet.getDbAstRigAstProductFile(assetIndex)
    #
    localSourceFile = assetPr.astUnitSourceFile(
        lxConfigure.LynxiRootIndex_Local,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    # Save to Local
    lxLog.viewStartProcess(logWin, 'Load Rig - Asset')
    if lxBasic.isOsExistsFile(dbRigFile):
        if force:
            maFile.openMayaFileAsBack(dbRigFile, localSourceFile)
        elif not force:
            maFile.setFileImport(dbRigFile)
            maFile.saveMayaFileToLocal(localSourceFile)
        # Extra
        astUnitLoadExtraSub(
            logWin,
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )
        # Create Branch
        rigBranch = assetPr.astUnitRigLinkGroupName(assetName)
        if not maUtils.isAppExist(rigBranch):
            maHier.setCreateAstRigHierarchy(assetClass, assetName)
        #
        maHier.astUnitRefreshRoot(
            assetIndex,
            assetClass, assetName, assetVariant, assetStage
        )
        #
        lxLog.viewCompleteProcess(logWin)
    else:
        lxLog.viewFailProcess(logWin, 'Rig - Asset is Non - Exists')
    # Complete
    lxLog.viewCompleteLoadMessage(logWin)


#
def saveRigSource(logWin, projectName, assetClass, assetName, assetVariant, assetStage):
    # LocalFile
    localFile = assetPr.astUnitSourceFile(
        lxConfigure.LynxiRootIndex_Local,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    maUtils.setVisiblePanelsDelete()
    assetOp.setUnknownNodeClear()
    #
    lxLog.viewStartProcess(logWin, 'Save Asset Rig - Source ( Local )')
    #
    maFile.saveMayaFileToLocal(localFile)
    #
    lxLog.viewCompleteProcess(logWin)


# Create CFX File
@lxTip.viewExceptionMethod
@lxTip.viewTimeMethod
def astUnitCreateCfxMain(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        withRig=False
):
    # Set Log Window
    logWin.setNameText(u'毛发创建')
    #
    isLoadMesh = dbGet.isDbAstExistsGeometry(assetIndex)
    modelIndex = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
    isLoadMaterial = dbGet.isDbAstMaterialExists(modelIndex)
    #
    maxProgress = [0, 1][isLoadMesh] + [0, 2][isLoadMaterial]
    logWin.setMaxProgressValue(maxProgress)
    # Start
    lxLog.viewStartLoadMessage(logWin)
    #
    maUtils.setDisplayMode(5)
    # Load Model
    maDbAstCmds.dbAstLoadModelProduct(assetIndex, assetName, assetVariant)
    # Extra
    astUnitLoadExtraSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )
    # Create Root
    maHier.setCreateAstCfxHierarchy(assetClass, assetName)
    astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName)
    maUtils.setObjectReferenceDisplay(astUnitModelProductGroup)
    #
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage
    )
    # Save Source
    astUnitSaveSource(logWin, assetIndex, projectName, assetClass, assetName, assetVariant, assetStage)
    # Complete
    lxLog.viewCompleteLoadMessage(logWin)


# Load CFX File
@lxTip.viewExceptionMethod
@lxTip.viewTimeMethod
def astUnitCfxLoadMainCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        collectionMap=True, useServerMap=False,
        collectionTexture=True, useServerTexture=False,
):
    isExistsFur = dbGet.getExistsDbFur(assetIndex, assetVariant)
    isExistsCfxMaterial = dbGet.getExistsDbCfxMaterial(assetIndex, assetVariant)
    # Set Log Window
    logWin.setNameText(u'毛发领取')
    maxProgress = [0, 1][isExistsFur] + [0, 2][isExistsCfxMaterial]
    logWin.setMaxProgressValue(maxProgress)
    # Start
    lxLog.viewStartLoadMessage(logWin)
    maUtils.setDisplayMode(5)
    # Load Model
    maDbAstCmds.dbAstLoadModelProduct(
        assetIndex, assetName, assetVariant
    )
    #
    if collectionTexture is True:
        astUnitLoadModelTexture(
            logWin,
            projectName,
            assetIndex,
            assetClass, assetName, assetVariant, assetStage
        )
    # Create Root
    maHier.setCreateAstRootHierarchy(assetClass, assetName)
    astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName)
    maUtils.setObjectReferenceDisplay(astUnitModelProductGroup)
    #
    astUnitCfxFurLoadCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        collectionMap=collectionMap, useServerMap=useServerMap
    )
    astUnitLoadCfxMaterialSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        collectionTexture=collectionTexture, useServerTexture=useServerTexture
    )
    # Extra >>> 4
    astUnitLoadExtraSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )
    #
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage
    )
    # Save Source
    astUnitSaveSource(logWin, assetIndex, projectName, assetClass, assetName, assetVariant, assetStage)
    # Complete
    lxLog.viewCompleteLoadMessage(logWin)


#
def astUnitCfxFurLoadCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        collectionMap=False, useServerMap=False
):
    # Data
    cfxGroup = assetPr.astUnitCfxLinkGroupName(assetName)
    # Load Fur Node
    existDbFur = dbGet.getExistsDbFur(assetIndex, assetVariant)
    if existDbFur:
        lxLog.viewStartProcess(logWin, 'Load Asset CFX ( Fur )')
        #
        maDbAstCmds.dbAstLoadFurIntegration(assetIndex, assetVariant)
        maDbAstCmds.dbAstLoadFurIndexSub(assetIndex, assetVariant)
        #
        lxLog.viewCompleteProcess(logWin)
        if collectionMap is True:
            # Load Fur Map
            mapDirectory = assetPr.astUnitMapFolder(
                lxConfigure.LynxiRootIndex_Local,
                projectName,
                assetClass, assetName, assetVariant, assetStage
            )
            if useServerMap:
                mapDirectory = assetPr.astUnitMapFolder(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    assetClass, assetName, assetVariant, assetStage
                )
            #
            lxLog.viewStartProcess(logWin, u'Load Asset CFX ( Fur Map')
            #
            maTxtr.setCollectionMaps(mapDirectory)
            maTxtr.setRepathMaps(mapDirectory)
            #
            lxLog.viewCompleteProcess(logWin)
        #
        rootGroup = assetPr.astUnitRootGroupName(assetName)
        if maUtils.isAppExist(rootGroup):
            maUtils.setObjectParent(cfxGroup, rootGroup)
    else:
        lxLog.viewFailProcess(logWin, u'Asset CFX ( Fur ) is Non - Exists')


#
def astUnitLoadCfxMaterialSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        collectionTexture=False, useServerTexture=False
):
    renderer = projectPr.getProjectMayaRenderer(projectName)
    #
    cfxIndexKey = dbGet.getDbCfxIndex(assetIndex, assetVariant)
    #
    furCompIndexKeys = dbGet.getDbCompFurIndexData(cfxIndexKey)
    astMaterialObjectIndexLis = dbGet.getDbMaterialIndexData(cfxIndexKey)
    # Load Material >>> 01
    if astMaterialObjectIndexLis:
        lxLog.viewStartProcess(logWin, u'Load Asset CFX ( Material )')
        #
        maDbAstCmds.dbAstMaterialLoadMainCmd(cfxIndexKey, furCompIndexKeys, astMaterialObjectIndexLis)
        #
        lxLog.viewCompleteProcess(logWin)
        # Load Texture >>> 02
        if collectionTexture:
            if useServerTexture:
                cfxTextureDirectory = assetPr.astUnitTextureFolder(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    assetClass, assetName, assetVariant, assetStage
                )
            else:
                cfxTextureDirectory = assetPr.astUnitTextureFolder(
                    lxConfigure.LynxiRootIndex_Local,
                    projectName,
                    assetClass, assetName, assetVariant, assetStage
                )
            #
            lxLog.viewStartProcess(logWin, u'Load Asset CFX ( Fur - Texture )')
            #
            withTx = maTxtr.getTxTextureIsCollection(renderer)
            #
            shaderFurNodes = datAsset.getAstFurShaderObjects(assetName)
            #
            cfxTextureNodes = maShdr.getTextureNodeLisByObject(shaderFurNodes)
            if cfxTextureNodes:
                maTxtr.setTexturesCollection(
                    cfxTextureDirectory,
                    withTx=withTx,
                    inData=cfxTextureNodes
                )
                maTxtr.setTexturesRepath(
                    cfxTextureDirectory,
                    inData=cfxTextureNodes
                )
            #
            lxLog.viewCompleteProcess(logWin)
    else:
        lxLog.viewFailProcess(logWin, u'Asset CFX ( Material ) is Non - Exists')
    #
    astAovObjectIndexLis = dbGet.getDbAovIndexData(cfxIndexKey)
    if astAovObjectIndexLis:
        lxLog.viewStartProcess(logWin, u'Load Asset CFX ( AOV )')
        #
        maDbAstCmds.dbAstLoadAov(renderer, cfxIndexKey, astAovObjectIndexLis)
        #
        lxLog.viewCompleteProcess(logWin)
    else:
        lxLog.viewFailProcess(logWin, u'Asset CFX ( AOV ) is Non - Exists')


@lxTip.viewExceptionMethod
@lxTip.viewTimeMethod
def astUnitCreateRigSolMain(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        force=True):
    # Set Log Window
    logWin.setNameText(u'角色模拟创建')
    # Start
    lxLog.viewStartLoadMessage(logWin)
    maUtils.setDisplayMode(5)
    #
    lxLog.viewStartProcess(logWin, u'Load Asset CFX ( Fur )')
    #
    astUnitLoadReferenceSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )
    #
    lxLog.viewCompleteProcess(logWin)
    #
    maHier.setCreateAstRigSolverHierarchy(assetClass, assetName)
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage
    )
    # Save Source
    astUnitSaveSource(
        logWin,
        assetIndex,
        projectName, assetClass, assetName, assetVariant, assetStage
    )
    # Complete
    lxLog.viewCompleteLoadMessage(logWin)


@lxTip.viewExceptionMethod
@lxTip.viewTimeMethod
def astUnitCreateLightMain(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        force=True):
    # Set Log Window
    logWin.setNameText(u'灯光创建')
    #
    isLoadMesh = dbGet.isDbAstExistsGeometry(assetIndex)
    modelIndex = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
    isLoadMaterial = dbGet.isDbAstMaterialExists(modelIndex)
    #
    maxProgress = [0, 1][isLoadMesh] + [0, 2][isLoadMaterial]
    logWin.setMaxProgressValue(maxProgress)
    # Start
    lxLog.viewStartLoadMessage(logWin)
    #
    maUtils.setDisplayMode(5)
    #
    if force:
        maFile.new()
    #
    astUnitModelGeometryLoadCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        lockTransform=True
    )
    #
    astUnitModelMaterialLoadCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        collectionTexture=True, useServerTexture=True
    )
    # Create Root
    maHier.setCreateAstLightHierarchy(assetClass, assetName)
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage
    )
    # Complete
    lxLog.viewCompleteLoadMessage(logWin)


@lxTip.viewExceptionMethod
@lxTip.viewTimeMethod
def astUnitLoadMain(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        collectionTexture=False, useServerTexture=False,
        force=True
):
    # Set Log Window
    logWin.setNameText('%s Load' % assetStage.capitalize())
    maxProgress = 4
    logWin.setMaxProgressValue(maxProgress)
    # Start
    lxLog.viewStartLoadMessage(logWin)
    maUtils.setDisplayMode(5)
    # Refer >>> 01
    astUnitLoadReferenceSub(
        logWin,
        assetIndex, projectName, assetClass, assetName, assetVariant, assetStage
    )
    # Product >>> 02
    astUnitLoadProductSub(
        logWin,
        assetIndex, projectName, assetClass, assetName, assetVariant, assetStage
    )
    # Extra >>> 03
    astUnitLoadExtraSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )
    # Cache >>> 04
    astUnitLoadCacheSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        collectionCache=True, useServerTexture=False
    )
    # Save Source >>> 05
    maHier.setCreateAstRootHierarchy(
        assetClass, assetName
    )
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage
    )
    #
    astUnitSaveSource(
        logWin,
        assetIndex, projectName, assetClass, assetName, assetVariant, assetStage
    )
    # Complete
    lxLog.viewCompleteLoadMessage(logWin)


#
def astUnitLoadReferenceSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage
):
    lxLog.viewStartProcess(logWin, 'Load Asset ( %s ) Reference' % assetStage.capitalize())
    #
    if assetPr.isAstSolverLink(assetStage):
        # Model
        maDbAstCmds.dbAstGeometryLoadMainCmd(assetIndex, assetName)
        #
        assetSubIndex = dbGet.getDbCfxIndex(assetIndex, assetVariant)
        maDbAstCmds.dbAstLoadNurbsHairMain(assetSubIndex)
        # Refresh Root
        astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName)
        maUtils.setObjectReferenceDisplay(astUnitModelProductGroup)
    elif assetPr.isAstLightLink(assetStage):
        maDbAstCmds.dbAstLoadModelProduct(
            assetIndex,
            assetName, assetVariant
        )
        #
        astUnitLoadModelTexture(
            logWin,
            projectName,
            assetIndex,
            assetClass, assetName, assetVariant, assetStage
        )
        # Refresh Root
        astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName)
        maUtils.setObjectReferenceDisplay(astUnitModelProductGroup)
    #
    lxLog.viewCompleteProcess(logWin)


#
def astUnitLoadProductSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage
):
    serverProductFile = None
    if assetPr.isAstSolverLink(assetStage) or assetPr.isAstLightLink(assetStage):
        serverProductFile = assetPr.astUnitProductFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
    #
    if serverProductFile is not None:
        if lxBasic.isOsExistsFile(serverProductFile):
            lxLog.viewStartProcess(logWin, 'Load Asset ( %s ) Product' % lxBasic._toStringPrettify(assetStage))
            #
            maFile.setFileImport(serverProductFile)
            #
            lxLog.viewCompleteProcess(logWin)
            #
            astUnitLoadTextureSub(
                logWin,
                assetIndex,
                projectName,
                assetClass, assetName, assetVariant, assetStage
            )


#
def astUnitLoadTexture_(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        textureNodes,
        isWithTx
):
    if textureNodes:
        localTextureFolder = assetPr.astUnitTextureFolder(
            lxConfigure.LynxiRootIndex_Local,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )
        maTxtr.setTexturesCollection(
            localTextureFolder,
            withTx=isWithTx,
            inData=textureNodes,
            backupExists=True
        )
        maTxtr.setTexturesRepath(
            localTextureFolder,
            inData=textureNodes
        )


#
def astUnitLoadTextureSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage
):
    linkGroupName = None
    #
    isWithTx = False
    if assetPr.isAstLightLink(assetStage):
        linkGroupName = assetPr.astUnitLightLinkGroupName(assetName)
        isWithTx = True
    #
    if linkGroupName is not None:
        if maUtils.isAppExist(linkGroupName):
            shaderObjectLis = maUtils.getChildrenByRoot(linkGroupName)
            lxLog.viewStartProcess(logWin, 'Load Asset ( %s ) Texture' % lxBasic._toStringPrettify(assetStage))
            #
            if shaderObjectLis:
                textureNodes = maShdr.getTextureNodeLisByObject(shaderObjectLis)
                if textureNodes:
                    # Load
                    astUnitLoadTexture_(
                        assetIndex,
                        projectName,
                        assetClass, assetName, assetVariant, assetStage,
                        textureNodes,
                        isWithTx
                    )
                else:
                    lxLog.viewWarning(logWin, u'Texture - Node is Non - Exists')
            else:
                lxLog.viewWarning(logWin, u'Shader - Object is Non - Exists')
            #
            lxLog.viewCompleteProcess(logWin)


#
def astUnitLoadCacheSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        collectionCache=True, useServerTexture=False
):
    linkGroupName = None
    #
    isWithTx = False
    if assetPr.isAstSolverLink(assetStage):
        pass


#
def astUnitLoadExtraSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage):
    serverExtraFile = assetPr.astUnitExtraFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, assetClass, assetName, assetVariant, assetStage
    )[1]
    extraData = lxBasic.readOsJson(serverExtraFile)
    if extraData:
        assetOp.setCreateAstExtraData(extraData)
    #
    astUnitModelBridgeGroup = assetPr.astUnitModelBridgeGroupName(assetName)
    if maUtils.isAppExist(astUnitModelBridgeGroup):
        astUnitModelGroup = assetPr.astUnitModelLinkGroupName(assetName)
        maUtils.setObjectParent(astUnitModelBridgeGroup, astUnitModelGroup)


#
def astUnitSaveSource(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage):
    localSourceFile = assetPr.astUnitSourceFile(
        lxConfigure.LynxiRootIndex_Local,
        projectName, assetClass, assetName, assetVariant, assetStage
    )[1]
    # Save to Local
    maUtils.setVisiblePanelsDelete()
    assetOp.setUnknownNodeClear()
    #
    lxLog.viewStartProcess(logWin, 'Save Asset ( %s ) Source to Local' % assetStage.capitalize())
    #
    maFile.saveMayaFileToLocal(localSourceFile)
    #
    lxLog.viewCompleteProcess(logWin)


#
def astUnitLoadAssemblyForScenery(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant,
        isWithAnnotation=True, isWithHandle=True):
    #
    activeRepresentation = 'GPU'
    #
    arName = assetPr.astUnitAssemblyReferenceName(assetName)
    serverAstUnitAsbDefinitionFile = assetPr.astUnitAssemblyDefinitionFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Assembly
    )[1]
    if lxBasic.isOsExistsFile(serverAstUnitAsbDefinitionFile):
        assemblyAnnotation = assetPr.getAssetViewInfo(assetIndex, assetClass, assetVariant)
        maAsb.setAssemblyReferenceCreate(arName, serverAstUnitAsbDefinitionFile)
        #
        if isWithAnnotation:
            maAsb.setAssemblyAnnotation(arName, assemblyAnnotation)
        if isWithHandle:
            maUtils.setObjectDisplayHandleEnable(arName, True)
        #
        maAsb.setAssemblyActive(arName, activeRepresentation)
        colorConfig = sceneryPr.assemblyColorConfig()
        maUtils.setNodeOverrideColor(arName, colorConfig[activeRepresentation])
        maUtils.setNodeRename(arName, arName + '_0')


#
def astUnitRigLoadForAnimationCmd(
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant
):
    serverRigProductFile = assetPr.astUnitProductFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Rig
    )[1]
    if not lxBasic.isOsExistsFile(serverRigProductFile):
        maDbAstCmds.dbAstCopyRigProductTo(assetIndex, serverRigProductFile)
    #
    timeTag = lxBasic.getOsActiveTimeTag()
    namespace = assetPr.astRigNamespaceSet(assetName) + '_' + timeTag
    #
    maFile.setMaFileReference(serverRigProductFile, namespace)
    referenceNode = namespace + 'RN'
    maUtils.setAttrStringDatumForce_(referenceNode, appVariant.artistLabel, lxBasic.getOsUser())
    maUtils.setAttrStringDatumForce_(referenceNode, appVariant.updateLabel, lxBasic.getOsActiveTimestamp())
    maUtils.setAttrStringDatumForce_(referenceNode, appVariant.basicIndexAttrLabel, assetIndex)


#
def astAssetLoadRigSolForAnimation(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant):
    serverSolverProductFile = assetPr.astUnitProductFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Solver
    )[1]
    timeTag = lxBasic.getOsActiveTimeTag()
    namespace = assetPr.astSolverNamespaceSet(assetName, assetVariant) + '_' + timeTag
    #
    maFile.setMaFileReference(serverSolverProductFile, namespace)
    referenceNode = namespace + 'RN'
    maUtils.setAttrStringDatumForce_(referenceNode, appVariant.artistLabel, lxBasic.getOsUser())
    maUtils.setAttrStringDatumForce_(referenceNode, appVariant.updateLabel, lxBasic.getOsActiveTimestamp())
    maUtils.setAttrStringDatumForce_(referenceNode, appVariant.basicIndexAttrLabel, assetIndex)