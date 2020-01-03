# coding=utf-8
from LxCore import lxBasic, lxCore_
from LxUi.qt import qtLog, qtTip
#
from LxCore.preset import appVariant
#
from LxCore.preset.prod import projectPr, assetPr, sceneryPr
#
from LxDatabase import dbGet
#
from LxMaya.command import maUtils, maFile, maShdr, maTxtr, maHier, maRender, maAsb
#
from LxMaya.product.data import datAsset
#
from LxMaya.product.op import assetOp
#
from LxMaya.database import maDbAstCmds
#
none = ''


@qtTip.viewExceptionMethod
@qtTip.viewTimeMethod
def astUnitModelCreateMainCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        isUseExistsHierarchy=False
):
    # Set Log Window
    logWin.setNameText(u'模型创建')
    qtLog.viewStartProcessMessage(logWin, 'Asset Model Create')
    #
    existsHierarchy = None
    #
    if isUseExistsHierarchy:
        selObjects = maUtils.getSelectedObjects()
        if selObjects:
            existsHierarchy = selObjects[0]
    #
    qtLog.viewStartProcess(logWin, 'Create Model - Hierarchy')
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
    qtLog.viewCompleteProcess(logWin)
    qtLog.viewCompleteProcessMessage(logWin)
    #
    logWin.setCountdownClose(5)


@qtTip.viewExceptionMethod
@qtTip.viewTimeMethod
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
    qtLog.viewStartLoadMessage(logWin)
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
    qtLog.viewCompleteLoadMessage(logWin)
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
        lxCore_.LynxiRootIndex_Local,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    # Save to Local
    maUtils.setVisiblePanelsDelete()
    assetOp.setUnknownNodeClear()
    #
    qtLog.viewStartProcess(logWin, 'Save Model - Source ( Local )')
    #
    maFile.saveMayaFileToLocal(localModelFile)
    #
    qtLog.viewCompleteProcess(logWin)


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
        qtLog.viewStartProcess(logWin, 'Load Asset Model Nde_Geometry')
        #
        maDbAstCmds.dbAstGeometryLoadMainCmd(assetIndex, assetName, lockTransform)
        #
        qtLog.viewCompleteProcess(logWin)
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
        qtLog.viewStartProcess(logWin, u'Load Asset Model ( Material )')
        #
        maDbAstCmds.dbAstMaterialLoadMainCmd(assetSubIndexKey, geometryObjectIndexLis, astMaterialObjectIndexLis)
        #
        qtLog.viewCompleteProcess(logWin)
        # Load Texture >>> 02
        if collectionTexture:
            # Use Server Path
            if useServerTexture:
                modelTextureDirectory = assetPr.astUnitTextureFolder(
                    lxCore_.LynxiRootIndex_Server,
                    projectName,
                    assetClass, assetName, assetVariant, assetStage
                )
                isBackExists = False
            else:
                modelTextureDirectory = assetPr.astUnitTextureFolder(
                    lxCore_.LynxiRootIndex_Local,
                    projectName,
                    assetClass, assetName, assetVariant, assetStage
                )
                isBackExists = True
            #
            qtLog.viewStartProcess(logWin, 'Load Model - Texture')
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
            qtLog.viewCompleteProcess(logWin)
        #
        astAovObjectIndexLis = dbGet.getDbAovIndexData(assetSubIndexKey)
        if astAovObjectIndexLis:
            qtLog.viewStartProcess(logWin, u'Load Asset Model ( AOV )')
            #
            maDbAstCmds.dbAstLoadAov(renderer, assetSubIndexKey, astAovObjectIndexLis)
            #
            qtLog.viewCompleteProcess(logWin)
        else:
            qtLog.viewFailProcess(logWin, u'Asset Model ( AOV ) is Non - Exists')
        # Collection Bridge Group
        astUnitModelLinkGroup = assetPr.astUnitModelLinkGroupName(assetName)
        astUnitModelBridgeGroup = assetPr.astUnitModelBridgeGroupName(assetName)
        maUtils.setObjectParent(astUnitModelBridgeGroup, astUnitModelLinkGroup)
    else:
        qtLog.viewFailProcess(logWin, u'Asset Model ( Material ) is Non - Exists')


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
            lxCore_.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )
        isBackExists = False
    else:
        modelTextureDirectory = assetPr.astUnitTextureFolder(
            lxCore_.LynxiRootIndex_Local,
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
    qtLog.viewStartProcess(logWin, 'Load Asset Model ( Texture )')
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
    qtLog.viewCompleteProcess(logWin)


# Crate Rig File
@qtTip.viewExceptionMethod
@qtTip.viewTimeMethod
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
    qtLog.viewStartLoadMessage(logWin)
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
    qtLog.viewCompleteLoadMessage(logWin)


# Animation Rig Load
@qtTip.viewExceptionMethod
@qtTip.viewTimeMethod
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
    qtLog.viewStartLoadMessage(logWin)
    maUtils.setDisplayMode(5)
    #
    dbRigFile = dbGet.getDbAstRigAstProductFile(assetIndex)
    #
    localSourceFile = assetPr.astUnitSourceFile(
        lxCore_.LynxiRootIndex_Local,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    # Save to Local
    qtLog.viewStartProcess(logWin, 'Load Rig - Asset')
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
        qtLog.viewCompleteProcess(logWin)
    else:
        qtLog.viewFailProcess(logWin, 'Rig - Asset is Non - Exists')
    # Complete
    qtLog.viewCompleteLoadMessage(logWin)


#
def saveRigSource(logWin, projectName, assetClass, assetName, assetVariant, assetStage):
    # LocalFile
    localFile = assetPr.astUnitSourceFile(
        lxCore_.LynxiRootIndex_Local,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    maUtils.setVisiblePanelsDelete()
    assetOp.setUnknownNodeClear()
    #
    qtLog.viewStartProcess(logWin, 'Save Asset Rig - Source ( Local )')
    #
    maFile.saveMayaFileToLocal(localFile)
    #
    qtLog.viewCompleteProcess(logWin)


# Create CFX File
@qtTip.viewExceptionMethod
@qtTip.viewTimeMethod
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
    qtLog.viewStartLoadMessage(logWin)
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
    qtLog.viewCompleteLoadMessage(logWin)


# Load CFX File
@qtTip.viewExceptionMethod
@qtTip.viewTimeMethod
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
    qtLog.viewStartLoadMessage(logWin)
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
    qtLog.viewCompleteLoadMessage(logWin)


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
    # Load Fur Nde_Node
    existDbFur = dbGet.getExistsDbFur(assetIndex, assetVariant)
    if existDbFur:
        qtLog.viewStartProcess(logWin, 'Load Asset CFX ( Fur )')
        #
        maDbAstCmds.dbAstLoadFurIntegration(assetIndex, assetVariant)
        maDbAstCmds.dbAstLoadFurIndexSub(assetIndex, assetVariant)
        #
        qtLog.viewCompleteProcess(logWin)
        if collectionMap is True:
            # Load Fur Map
            mapDirectory = assetPr.astUnitMapFolder(
                lxCore_.LynxiRootIndex_Local,
                projectName,
                assetClass, assetName, assetVariant, assetStage
            )
            if useServerMap:
                mapDirectory = assetPr.astUnitMapFolder(
                    lxCore_.LynxiRootIndex_Server,
                    projectName,
                    assetClass, assetName, assetVariant, assetStage
                )
            #
            qtLog.viewStartProcess(logWin, u'Load Asset CFX ( Fur Map')
            #
            maTxtr.setCollectionMaps(mapDirectory)
            maTxtr.setRepathMaps(mapDirectory)
            #
            qtLog.viewCompleteProcess(logWin)
        #
        rootGroup = assetPr.astUnitRootGroupName(assetName)
        if maUtils.isAppExist(rootGroup):
            maUtils.setObjectParent(cfxGroup, rootGroup)
    else:
        qtLog.viewFailProcess(logWin, u'Asset CFX ( Fur ) is Non - Exists')


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
        qtLog.viewStartProcess(logWin, u'Load Asset CFX ( Material )')
        #
        maDbAstCmds.dbAstMaterialLoadMainCmd(cfxIndexKey, furCompIndexKeys, astMaterialObjectIndexLis)
        #
        qtLog.viewCompleteProcess(logWin)
        # Load Texture >>> 02
        if collectionTexture:
            if useServerTexture:
                cfxTextureDirectory = assetPr.astUnitTextureFolder(
                    lxCore_.LynxiRootIndex_Server,
                    projectName,
                    assetClass, assetName, assetVariant, assetStage
                )
            else:
                cfxTextureDirectory = assetPr.astUnitTextureFolder(
                    lxCore_.LynxiRootIndex_Local,
                    projectName,
                    assetClass, assetName, assetVariant, assetStage
                )
            #
            qtLog.viewStartProcess(logWin, u'Load Asset CFX ( Fur - Texture )')
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
            qtLog.viewCompleteProcess(logWin)
    else:
        qtLog.viewFailProcess(logWin, u'Asset CFX ( Material ) is Non - Exists')
    #
    astAovObjectIndexLis = dbGet.getDbAovIndexData(cfxIndexKey)
    if astAovObjectIndexLis:
        qtLog.viewStartProcess(logWin, u'Load Asset CFX ( AOV )')
        #
        maDbAstCmds.dbAstLoadAov(renderer, cfxIndexKey, astAovObjectIndexLis)
        #
        qtLog.viewCompleteProcess(logWin)
    else:
        qtLog.viewFailProcess(logWin, u'Asset CFX ( AOV ) is Non - Exists')


@qtTip.viewExceptionMethod
@qtTip.viewTimeMethod
def astUnitCreateRigSolMain(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        force=True):
    # Set Log Window
    logWin.setNameText(u'角色模拟创建')
    # Start
    qtLog.viewStartLoadMessage(logWin)
    maUtils.setDisplayMode(5)
    #
    qtLog.viewStartProcess(logWin, u'Load Asset CFX ( Fur )')
    #
    astUnitLoadReferenceSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )
    #
    qtLog.viewCompleteProcess(logWin)
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
    qtLog.viewCompleteLoadMessage(logWin)


@qtTip.viewExceptionMethod
@qtTip.viewTimeMethod
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
    qtLog.viewStartLoadMessage(logWin)
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
    qtLog.viewCompleteLoadMessage(logWin)


@qtTip.viewExceptionMethod
@qtTip.viewTimeMethod
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
    qtLog.viewStartLoadMessage(logWin)
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
    qtLog.viewCompleteLoadMessage(logWin)


#
def astUnitLoadReferenceSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage
):
    qtLog.viewStartProcess(logWin, 'Load Asset ( %s ) Reference' % assetStage.capitalize())
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
    qtLog.viewCompleteProcess(logWin)


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
            lxCore_.LynxiRootIndex_Server,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
    #
    if serverProductFile is not None:
        if lxBasic.isOsExistsFile(serverProductFile):
            qtLog.viewStartProcess(logWin, 'Load Asset ( %s ) Product' % lxBasic.str_camelcase2prettify(assetStage))
            #
            maFile.setFileImport(serverProductFile)
            #
            qtLog.viewCompleteProcess(logWin)
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
            lxCore_.LynxiRootIndex_Local,
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
            qtLog.viewStartProcess(logWin, 'Load Asset ( %s ) Texture' % lxBasic.str_camelcase2prettify(assetStage))
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
                    qtLog.viewWarning(logWin, u'Texture - Nde_Node is Non - Exists')
            else:
                qtLog.viewWarning(logWin, u'Nde_ShaderRef - Object is Non - Exists')
            #
            qtLog.viewCompleteProcess(logWin)


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
        lxCore_.LynxiRootIndex_Server,
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
        lxCore_.LynxiRootIndex_Local,
        projectName, assetClass, assetName, assetVariant, assetStage
    )[1]
    # Save to Local
    maUtils.setVisiblePanelsDelete()
    assetOp.setUnknownNodeClear()
    #
    qtLog.viewStartProcess(logWin, 'Save Asset ( %s ) Source to Local' % assetStage.capitalize())
    #
    maFile.saveMayaFileToLocal(localSourceFile)
    #
    qtLog.viewCompleteProcess(logWin)


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
        lxCore_.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, lxCore_.LynxiProduct_Asset_Link_Assembly
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
        lxCore_.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, lxCore_.LynxiProduct_Asset_Link_Rig
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
        lxCore_.LynxiRootIndex_Server,
        projectName, assetClass, assetName, assetVariant, lxCore_.LynxiProduct_Asset_Link_Solver
    )[1]
    timeTag = lxBasic.getOsActiveTimeTag()
    namespace = assetPr.astSolverNamespaceSet(assetName, assetVariant) + '_' + timeTag
    #
    maFile.setMaFileReference(serverSolverProductFile, namespace)
    referenceNode = namespace + 'RN'
    maUtils.setAttrStringDatumForce_(referenceNode, appVariant.artistLabel, lxBasic.getOsUser())
    maUtils.setAttrStringDatumForce_(referenceNode, appVariant.updateLabel, lxBasic.getOsActiveTimestamp())
    maUtils.setAttrStringDatumForce_(referenceNode, appVariant.basicIndexAttrLabel, assetIndex)