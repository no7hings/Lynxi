# coding=utf-8
from LxBasic import bscMethods, bscModifiers, bscObjects

from LxCore import lxConfigure

from LxPreset import prsVariants, prsMethods

from LxCore.preset.prod import assetPr, sceneryPr

from LxDatabase import dbGet

from LxMaya.command import maUtils, maFile, maShdr, maTxtr, maHier, maRender, maAsb

from LxMaya.product.data import datAsset

from LxMaya.product.op import assetOp

from LxMaya.database import maDbAstCmds

none = ''


@bscModifiers.fncExceptionCatch
@bscModifiers.fncCostTimeCatch
def astUnitModelCreateMainCmd(
        projectName,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        isUseExistsHierarchy=False
):
    logWin_ = bscObjects.If_Log(title=u'Model Create')
    logWin_.showUi()

    logWin_.addStartTask(u'Model Create')
    #
    existsHierarchy = None
    #
    if isUseExistsHierarchy:
        selObjects = maUtils.getSelectedObjects()
        if selObjects:
            existsHierarchy = selObjects[0]
    #
    logWin_.addStartProgress(u'Model Hierarchy Create')
    #
    maHier.setCreateAstModelHierarchy(assetCategory, assetName)
    maHier.setCreateAstUnitModelSolverHierarchy(assetCategory, assetName)
    #
    astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName)
    maHier.refreshHierarchyBranch(
        astUnitModelProductGroup,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage
    )
    #
    if existsHierarchy:
        maUtils.setObjectParent(existsHierarchy, astUnitModelProductGroup)
    #
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage
    )
    #
    logWin_.addCompleteProgress()
    logWin_.addCompleteTask()


@bscModifiers.fncExceptionCatch
@bscModifiers.fncCostTimeCatch
def astUnitModelLoadMainCmd(
        projectName,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        force=True, lockTransform=True, collectionTexture=True,
):
    # Set Log Window
    logWin_ = bscObjects.If_Log(title=u'Model Load')
    logWin_.showUi()
    # Start
    logWin_.addStartTask(u'Load Model')

    maUtils.setDisplayMode(5)

    if force is True:
        maFile.new()
    # Geometry
    astUnitModelGeometryLoadCmd(
        projectName,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        lockTransform=lockTransform
    )
    # Material
    astUnitModelMaterialLoadCmd(
        projectName,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        collectionTexture=collectionTexture
    )
    # Extra
    astUnitExtraLoadCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )
    # Create Root
    maHier.setCreateAstRootHierarchy(
        assetCategory, assetName
    )
    # Refresh Root
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage
    )
    # Save Source to Local
    astUnitModelSourceSaveCmd(
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )
    # Complete
    logWin_.addCompleteTask()


#
def astUnitModelSourceSaveCmd(
        projectName,
        assetCategory, assetName, assetVariant, assetStage
):
    logWin_ = bscObjects.If_Log()
    # Local
    localAstModelFile = assetPr.astUnitSourceFile(
        lxConfigure.LynxiRootIndex_Local,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )[1]
    # Save to Local
    maUtils.setVisiblePanelsDelete()
    assetOp.setUnknownNodeClear()
    #
    logWin_.addStartProgress(u'Model Source ( Local ) Save')
    #
    maFile.saveMayaFileToLocal(localAstModelFile)
    logWin_.addResult(localAstModelFile)
    #
    logWin_.addCompleteProgress()


#
def astUnitModelGeometryLoadCmd(
        projectName,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        lockTransform=True
):
    logWin_ = bscObjects.If_Log()
    
    isDbExists = dbGet.isDbAstExistsGeometry(assetIndex)
    if isDbExists:
        logWin_.addStartProgress(u'Geometry Load')
        #
        maDbAstCmds.dbAstGeometryLoadMainCmd(assetIndex, assetName, lockTransform)
        #
        logWin_.addCompleteProgress()
        # Hide Solver Meshes
        assetOp.setSolverGroupGeometryHide(assetName)
    else:
        logWin_.closeUi()
        
        astUnitModelCreateMainCmd(
            projectName,
            assetIndex,
            assetCategory, assetName, assetVariant, assetStage
        )


#
def astUnitModelMaterialLoadCmd(
        projectName,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        collectionTexture=False, useServerTexture=False
):
    logWin_ = bscObjects.If_Log()
    
    assetSubIndexKey = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
    isDbExists = dbGet.isDbAstMaterialExists(assetSubIndexKey)
    if isDbExists:
        renderer = prsMethods.Project.mayaRenderer(projectName)
        maRender.setLoadRenderer(renderer)
        #
        geometryObjectIndexLis = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
        astMaterialObjectIndexLis = dbGet.getDbMaterialIndexData(assetSubIndexKey)
        logWin_.addStartProgress(u'Material Load')
        #
        maDbAstCmds.dbAstMaterialLoadMainCmd(assetSubIndexKey, geometryObjectIndexLis, astMaterialObjectIndexLis)
        #
        logWin_.addCompleteProgress()
        # Load Texture >>> 02
        if collectionTexture:
            # Use Server Path
            if useServerTexture:
                modelTextureDirectory = assetPr.astUnitTextureFolder(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    assetCategory, assetName, assetVariant, assetStage
                )
                isBackExists = False
            else:
                modelTextureDirectory = assetPr.astUnitTextureFolder(
                    lxConfigure.LynxiRootIndex_Local,
                    projectName,
                    assetCategory, assetName, assetVariant, assetStage
                )
                isBackExists = True
            #
            logWin_.addStartProgress(u'Texture Load')
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
            logWin_.addCompleteProgress()
        #
        astAovObjectIndexLis = dbGet.getDbAovIndexData(assetSubIndexKey)
        if astAovObjectIndexLis:
            logWin_.addStartProgress(u'AOV Load')
            #
            maDbAstCmds.dbAstLoadAov(renderer, assetSubIndexKey, astAovObjectIndexLis)
            #
            logWin_.addCompleteProgress()
        else:
            logWin_.addWarning(u'AOV is Non - Exists')
        # Collection Bridge Group
        astUnitModelLinkGroup = prsMethods.Asset.modelLinkGroupName(assetName)
        astUnitModelBridgeGroup = assetPr.astUnitModelBridgeGroupName(assetName)
        maUtils.setObjectParent(astUnitModelBridgeGroup, astUnitModelLinkGroup)
    else:
        logWin_.addWarning(u'Material is Non - Exists')


#
def astUnitLoadModelTexture(
        projectName,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        useServerTexture=False
):
    logWin_ = bscObjects.If_Log()
    # Use Server Path
    if useServerTexture:
        modelTextureDirectory = assetPr.astUnitTextureFolder(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            assetCategory, assetName, assetVariant, assetStage
        )
        isBackExists = False
    else:
        modelTextureDirectory = assetPr.astUnitTextureFolder(
            lxConfigure.LynxiRootIndex_Local,
            projectName,
            assetCategory, assetName, assetVariant, assetStage
        )
        isBackExists = True
    #
    shaderObjectLis = datAsset.getAstMeshObjects(assetName, 1)
    # Debug ( Must Back of Rename Scene)
    textureNodeLis = maShdr.getTextureNodeLisByObject(shaderObjectLis)
    #
    renderer = prsMethods.Project.mayaRenderer(projectName)
    #
    withTx = maTxtr.getTxTextureIsCollection(renderer)
    #
    logWin_.addStartProgress(u'Texture Load')
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
    logWin_.addCompleteProgress()


# Crate Rig File
@bscModifiers.fncExceptionCatch
@bscModifiers.fncCostTimeCatch
def astUnitRigCreateMainCmd(
        projectName,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage
):
    logWin_ = bscObjects.If_Log(u'Rig Create')
    logWin_.showUi()
    #
    isLoadMesh = dbGet.isDbAstExistsGeometry(assetIndex)
    modelIndex = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
    isLoadMaterial = dbGet.isDbAstMaterialExists(modelIndex)
    #
    maxProgress = [0, 1][isLoadMesh] + [0, 2][isLoadMaterial]
    # Start
    logWin_.addStartTask(u'Rig Create')
    maUtils.setDisplayMode(5)
    #
    astUnitModelGeometryLoadCmd(
        projectName,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        lockTransform=False
    )
    #
    astUnitModelMaterialLoadCmd(
        projectName,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        collectionTexture=True,
        useServerTexture=True
    )
    # Extra
    astUnitExtraLoadCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )
    #
    maHier.setCreateAstRigHierarchy(assetCategory, assetName)
    #
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage
    )
    #
    astUnitRigSaveCmd(
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )
    # Complete
    logWin_.addCompleteTask()


# Animation Rig Load
@bscModifiers.fncExceptionCatch
@bscModifiers.fncCostTimeCatch
def astUnitRigLoadMainCmd(
        assetIndex,
        projectName, assetCategory, assetName, assetVariant, assetStage,
        force=True
):
    # Set Log Window
    logWin_ = bscObjects.If_Log(u'Rig Load')
    logWin_.showUi()
    # Start
    logWin_.addStartTask(u'Rig Load')
    maUtils.setDisplayMode(5)
    #
    dbRigFile = dbGet.getDbAstRigAstProductFile(assetIndex)
    #
    localSourceFile = assetPr.astUnitSourceFile(
        lxConfigure.LynxiRootIndex_Local,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )[1]
    # Save to Local
    logWin_.addStartProgress(u'Rig Load')
    if bscMethods.OsFile.isExist(dbRigFile):
        if force:
            maFile.openMayaFileAsBack(dbRigFile, localSourceFile)
        elif not force:
            maFile.setFileImport(dbRigFile)
            maFile.saveMayaFileToLocal(localSourceFile)
        # Extra
        astUnitExtraLoadCmd(
            assetIndex,
            projectName,
            assetCategory, assetName, assetVariant, assetStage
        )
        # Create Branch
        rigBranch = prsMethods.Asset.rigLinkGroupName(assetName)
        if not maUtils.isAppExist(rigBranch):
            maHier.setCreateAstRigHierarchy(assetCategory, assetName)
        #
        maHier.astUnitRefreshRoot(
            assetIndex,
            assetCategory, assetName, assetVariant, assetStage
        )
        #
        logWin_.addCompleteProgress()
    else:
        logWin_.addWarning('Rig - Asset is Non - Exists')
    # Complete
    logWin_.addCompleteTask()


#
def astUnitRigSaveCmd(
        projectName,
        assetCategory, assetName, assetVariant, assetStage
):
    logWin_ = bscObjects.If_Log()
    # LocalFile
    localFile = assetPr.astUnitSourceFile(
        lxConfigure.LynxiRootIndex_Local,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )[1]
    maUtils.setVisiblePanelsDelete()
    assetOp.setUnknownNodeClear()
    #
    logWin_.addStartProgress(u'Source ( Local ) Save')
    #
    maFile.saveMayaFileToLocal(localFile)
    #
    logWin_.addCompleteProgress()


# Create CFX File
@bscModifiers.fncExceptionCatch
@bscModifiers.fncCostTimeCatch
def astUnitCreateCfxMain(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage,
        withRig=False
):
    # Set Log Window
    logWin_ = bscObjects.If_Log(u'Groom Create')
    logWin_.showUi()
    #
    isLoadMesh = dbGet.isDbAstExistsGeometry(assetIndex)
    modelIndex = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
    isLoadMaterial = dbGet.isDbAstMaterialExists(modelIndex)
    #
    maxProgress = [0, 1][isLoadMesh] + [0, 2][isLoadMaterial]
    # Start
    logWin_.addStartTask(u'Groom Create')
    #
    maUtils.setDisplayMode(5)
    # Load Model
    maDbAstCmds.dbAstLoadModelProduct(assetIndex, assetName, assetVariant)
    # Extra
    astUnitExtraLoadCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )
    # Create Root
    maHier.setCreateAstCfxHierarchy(assetCategory, assetName)
    astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName)
    maUtils.setObjectReferenceDisplay(astUnitModelProductGroup)
    #
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage
    )
    # Save Source
    astUnitSourceSaveCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )
    # Complete
    logWin_.addCompleteTask()


# Load CFX File
@bscModifiers.fncExceptionCatch
@bscModifiers.fncCostTimeCatch
def astUnitCfxLoadMainCmd(
        projectName,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        collectionMap=True, useServerMap=False,
        collectionTexture=True, useServerTexture=False,
):
    logWin_ = bscObjects.If_Log(u'Groom Load')
    logWin_.showUi()
    
    isExistsFur = dbGet.getExistsDbFur(assetIndex, assetVariant)
    isExistsCfxMaterial = dbGet.getExistsDbCfxMaterial(assetIndex, assetVariant)
    # Start
    logWin_.addStartTask(u'Groom Load')
    maUtils.setDisplayMode(5)
    # Load Model
    maDbAstCmds.dbAstLoadModelProduct(
        assetIndex, assetName, assetVariant
    )
    #
    if collectionTexture is True:
        astUnitLoadModelTexture(
            projectName,
            assetIndex,
            assetCategory, assetName, assetVariant, assetStage
        )
    # Create Root
    maHier.setCreateAstRootHierarchy(assetCategory, assetName)
    astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName)
    maUtils.setObjectReferenceDisplay(astUnitModelProductGroup)
    #
    astUnitCfxFurLoadCmd(
        projectName,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        collectionMap=collectionMap, useServerMap=useServerMap
    )
    astUnitLoadCfxMaterialSub(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage,
        collectionTexture=collectionTexture, useServerTexture=useServerTexture
    )
    # Extra >>> 4
    astUnitExtraLoadCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )
    #
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage
    )
    # Save Source
    astUnitSourceSaveCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )
    # Complete
    logWin_.addCompleteTask()


#
def astUnitCfxFurLoadCmd(
        projectName,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        collectionMap=False, useServerMap=False
):
    logWin_ = bscObjects.If_Log()
    # Data
    cfxGroup = prsMethods.Asset.groomLinkGroupName(assetName)
    # Load Fur Nde_Node
    existDbFur = dbGet.getExistsDbFur(assetIndex, assetVariant)
    if existDbFur:
        logWin_.addStartProgress(u'Fur Load')
        #
        maDbAstCmds.dbAstLoadFurIntegration(assetIndex, assetVariant)
        maDbAstCmds.dbAstLoadFurIndexSub(assetIndex, assetVariant)
        #
        logWin_.addCompleteProgress()
        if collectionMap is True:
            # Load Fur Map
            mapDirectory = assetPr.astUnitMapFolder(
                lxConfigure.LynxiRootIndex_Local,
                projectName,
                assetCategory, assetName, assetVariant, assetStage
            )
            if useServerMap:
                mapDirectory = assetPr.astUnitMapFolder(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    assetCategory, assetName, assetVariant, assetStage
                )
            #
            logWin_.addStartProgress(u'Map Load')
            #
            maTxtr.setCollectionMaps(mapDirectory)
            maTxtr.setRepathMaps(mapDirectory)
            #
            logWin_.addCompleteProgress()
        #
        rootGroup = prsMethods.Asset.rootName(assetName)
        if maUtils.isAppExist(rootGroup):
            maUtils.setObjectParent(cfxGroup, rootGroup)
    else:
        logWin_.addWarning(u'Fur is Non - Exists')


#
def astUnitLoadCfxMaterialSub(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage,
        collectionTexture=False, useServerTexture=False
):
    logWin_ = bscObjects.If_Log()
    
    renderer = prsMethods.Project.mayaRenderer(projectName)
    #
    cfxIndexKey = dbGet.getDbCfxIndex(assetIndex, assetVariant)
    #
    furCompIndexKeys = dbGet.getDbCompFurIndexData(cfxIndexKey)
    astMaterialObjectIndexLis = dbGet.getDbMaterialIndexData(cfxIndexKey)
    # Load Material >>> 01
    if astMaterialObjectIndexLis:
        logWin_.addStartProgress(u'Material Load')
        #
        maDbAstCmds.dbAstMaterialLoadMainCmd(cfxIndexKey, furCompIndexKeys, astMaterialObjectIndexLis)
        #
        logWin_.addCompleteProgress()
        # Load Texture >>> 02
        if collectionTexture:
            if useServerTexture:
                cfxTextureDirectory = assetPr.astUnitTextureFolder(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    assetCategory, assetName, assetVariant, assetStage
                )
            else:
                cfxTextureDirectory = assetPr.astUnitTextureFolder(
                    lxConfigure.LynxiRootIndex_Local,
                    projectName,
                    assetCategory, assetName, assetVariant, assetStage
                )
            #
            logWin_.addStartProgress(u'Texture Load')
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
            logWin_.addCompleteProgress()
    else:
        logWin_.addWarning(u'Material is Non - Exists')
    #
    astAovObjectIndexLis = dbGet.getDbAovIndexData(cfxIndexKey)
    if astAovObjectIndexLis:
        logWin_.addStartProgress(u'AOV Load')
        #
        maDbAstCmds.dbAstLoadAov(renderer, cfxIndexKey, astAovObjectIndexLis)
        #
        logWin_.addCompleteProgress()
    else:
        logWin_.addWarning(u'AOV is Non - Exists')


@bscModifiers.fncExceptionCatch
@bscModifiers.fncCostTimeCatch
def astUnitSolverCreateMainCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage,
        force=True
):
    # Set Log Window
    logWin_ = bscObjects.If_Log(u'Solver Create')
    logWin_.showUi()
    # Start
    logWin_.addStartTask(u'Solver Create')
    maUtils.setDisplayMode(5)
    #
    logWin_.addStartProgress(u'Groom Load')
    #
    astUnitReferenceLoadCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )
    #
    logWin_.addCompleteProgress()
    #
    maHier.setCreateAstRigSolverHierarchy(assetCategory, assetName)
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage
    )
    # Save Source
    astUnitSourceSaveCmd(
        assetIndex,
        projectName, assetCategory, assetName, assetVariant, assetStage
    )
    # Complete
    logWin_.addCompleteTask()


@bscModifiers.fncExceptionCatch
@bscModifiers.fncCostTimeCatch
def astUnitLightCreateMainCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage,
        force=True
):
    # Set Log Window
    logWin_ = bscObjects.If_Log(u'Light Create')
    logWin_.showUi()
    #
    isLoadMesh = dbGet.isDbAstExistsGeometry(assetIndex)
    modelIndex = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
    isLoadMaterial = dbGet.isDbAstMaterialExists(modelIndex)
    # Start
    logWin_.addStartTask(u'Light Create')
    #
    maUtils.setDisplayMode(5)
    #
    if force:
        maFile.new()
    #
    astUnitModelGeometryLoadCmd(
        projectName,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        lockTransform=True
    )
    #
    astUnitModelMaterialLoadCmd(
        projectName,
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        collectionTexture=True, useServerTexture=True
    )
    # Create Root
    maHier.setCreateAstLightHierarchy(assetCategory, assetName)
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage
    )
    # Complete
    logWin_.addCompleteTask()


@bscModifiers.fncExceptionCatch
@bscModifiers.fncCostTimeCatch
def astUnitLoadMainCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage,
        collectionTexture=False, useServerTexture=False,
        force=True
):
    # Set Log Window
    assetStagePrettify = assetStage.capitalize()
    logWin_ = bscObjects.If_Log(u'{} Load'.format(assetStagePrettify))
    logWin_.showUi()
    # Start
    logWin_.addStartTask(u'{} Load'.format(assetStagePrettify))
    maUtils.setDisplayMode(5)
    # Refer >>> 01
    astUnitReferenceLoadCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )
    # Product >>> 02
    astUnitProductLoadCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )
    # Extra >>> 03
    astUnitExtraLoadCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )
    # Cache >>> 04
    astUnitCacheLoadCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage,
        collectionCache=True, useServerTexture=False
    )
    # Save Source >>> 05
    maHier.setCreateAstRootHierarchy(
        assetCategory, assetName
    )
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage
    )
    #
    astUnitSourceSaveCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )
    # Complete
    logWin_.addCompleteTask()


#
def astUnitReferenceLoadCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
):
    assetStagePrettify = assetStage.capitalize()

    logWin_ = bscObjects.If_Log()
    
    logWin_.addStartProgress(u'Reference Load')
    #
    if prsMethods.Asset.isSolverStageName(assetStage):
        # Model
        maDbAstCmds.dbAstGeometryLoadMainCmd(assetIndex, assetName)
        #
        assetSubIndex = dbGet.getDbCfxIndex(assetIndex, assetVariant)
        maDbAstCmds.dbAstLoadNurbsHairMain(assetSubIndex)
        # Refresh Root
        astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName)
        maUtils.setObjectReferenceDisplay(astUnitModelProductGroup)
    elif prsMethods.Asset.isLightStageName(assetStage):
        maDbAstCmds.dbAstLoadModelProduct(
            assetIndex,
            assetName, assetVariant
        )
        #
        astUnitLoadModelTexture(
            projectName,
            assetIndex,
            assetCategory, assetName, assetVariant, assetStage
        )
        # Refresh Root
        astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName)
        maUtils.setObjectReferenceDisplay(astUnitModelProductGroup)
    #
    logWin_.addCompleteProgress()


#
def astUnitProductLoadCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
):
    assetStagePrettify = assetStage.capitalize()

    logWin_ = bscObjects.If_Log()
    
    serverProductFile = None
    if prsMethods.Asset.isSolverStageName(assetStage) or prsMethods.Asset.isLightStageName(assetStage):
        serverProductFile = assetPr.astUnitProductFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            assetCategory, assetName, assetVariant, assetStage
        )[1]
    #
    if serverProductFile is not None:
        if bscMethods.OsFile.isExist(serverProductFile):
            logWin_.addStartProgress(u'Product Load')
            #
            maFile.setFileImport(serverProductFile)
            #
            logWin_.addCompleteProgress()
            #
            astUnitTextureLoadCmd(
                assetIndex,
                projectName,
                assetCategory, assetName, assetVariant, assetStage
            )


#
def astUnitTextureLoadSubCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage,
        textureNodes,
        isWithTx
):
    assetStagePrettify = assetStage.capitalize()

    logWin_ = bscObjects.If_Log()
    
    if textureNodes:
        localTextureFolder = assetPr.astUnitTextureFolder(
            lxConfigure.LynxiRootIndex_Local,
            projectName,
            assetCategory, assetName, assetVariant, assetStage
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
def astUnitTextureLoadCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
):
    assetStagePrettify = assetStage.capitalize()

    logWin_ = bscObjects.If_Log()
    
    linkGroupName = None
    #
    isWithTx = False
    if prsMethods.Asset.isLightStageName(assetStage):
        linkGroupName = prsMethods.Asset.lightLinkGroupName(assetName)
        isWithTx = True
    #
    if linkGroupName is not None:
        if maUtils.isAppExist(linkGroupName):
            logWin_.addStartProgress(u'Texture Load')

            shaderObjectLis = maUtils.getChildrenByRoot(linkGroupName)
            #
            if shaderObjectLis:
                textureNodes = maShdr.getTextureNodeLisByObject(shaderObjectLis)
                if textureNodes:
                    # Load
                    astUnitTextureLoadSubCmd(
                        assetIndex,
                        projectName,
                        assetCategory, assetName, assetVariant, assetStage,
                        textureNodes,
                        isWithTx
                    )
                else:
                    logWin_.addWarning(u'Texture is Non - Exists')
            else:
                logWin_.addWarning(u'Shader is Non - Exists')
            #
            logWin_.addCompleteProgress()


#
def astUnitCacheLoadCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage,
        collectionCache=True, useServerTexture=False
):
    logWin_ = bscObjects.If_Log()
    
    linkGroupName = None
    #
    isWithTx = False
    if prsMethods.Asset.isSolverStageName(assetStage):
        pass


#
def astUnitExtraLoadCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
):
    logWin_ = bscObjects.If_Log()
    
    serverExtraFile = assetPr.astUnitExtraFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, assetCategory, assetName, assetVariant, assetStage
    )[1]
    extraData = bscMethods.OsJson.read(serverExtraFile)
    if extraData:
        assetOp.setCreateAstExtraData(extraData)
    #
    astUnitModelBridgeGroup = assetPr.astUnitModelBridgeGroupName(assetName)
    if maUtils.isAppExist(astUnitModelBridgeGroup):
        astUnitModelGroup = prsMethods.Asset.modelLinkGroupName(assetName)
        maUtils.setObjectParent(astUnitModelBridgeGroup, astUnitModelGroup)


#
def astUnitSourceSaveCmd(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
):
    assetStagePrettify = assetStage.capitalize()

    logWin_ = bscObjects.If_Log()
    
    localSourceFile = assetPr.astUnitSourceFile(
        lxConfigure.LynxiRootIndex_Local,
        projectName, assetCategory, assetName, assetVariant, assetStage
    )[1]
    # Save to Local
    maUtils.setVisiblePanelsDelete()
    assetOp.setUnknownNodeClear()
    #
    logWin_.addStartProgress(u'Source ( Local ) Save')
    #
    maFile.saveMayaFileToLocal(localSourceFile)
    #
    logWin_.addCompleteProgress()


#
def astUnitAssemblyLoadForScenery(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant,
        isWithAnnotation=True, isWithHandle=True
):
    logWin_ = bscObjects.If_Log()
    
    activeRepresentation = 'GPU'
    #
    arName = assetPr.astUnitAssemblyReferenceName(assetName)
    serverAstUnitAsbDefinitionFile = assetPr.astUnitAssemblyDefinitionFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetCategory, assetName, assetVariant, lxConfigure.VAR_product_asset_link_assembly
    )[1]
    if bscMethods.OsFile.isExist(serverAstUnitAsbDefinitionFile):
        assemblyAnnotation = assetPr.getAssetViewInfo(assetIndex, assetCategory, assetVariant)
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
        assetCategory, assetName, assetVariant
):
    logWin_ = bscObjects.If_Log()
    
    serverRigProductFile = assetPr.astUnitProductFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetCategory, assetName, assetVariant, lxConfigure.VAR_product_asset_link_rig
    )[1]
    if not bscMethods.OsFile.isExist(serverRigProductFile):
        maDbAstCmds.dbAstCopyRigProductTo(assetIndex, serverRigProductFile)
    #
    timeTag = bscMethods.OsTimetag.active()
    namespace = assetPr.astRigNamespaceSet(assetName) + '_' + timeTag
    #
    maFile.setMaFileReference(serverRigProductFile, namespace)
    referenceNode = namespace + 'RN'
    maUtils.setAttrStringDatumForce_(referenceNode, prsVariants.Util.artistLabel, bscMethods.OsSystem.username())
    maUtils.setAttrStringDatumForce_(referenceNode, prsVariants.Util.updateLabel, bscMethods.OsTimestamp.active())
    maUtils.setAttrStringDatumForce_(referenceNode, prsVariants.Util.basicIndexAttrLabel, assetIndex)


#
def astAssetSolverLoadForAnimation(
        assetIndex,
        projectName,
        assetCategory, assetName, assetVariant
):
    logWin_ = bscObjects.If_Log()
    
    serverSolverProductFile = assetPr.astUnitProductFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, assetCategory, assetName, assetVariant, lxConfigure.VAR_product_asset_link_solver
    )[1]
    timeTag = bscMethods.OsTimetag.active()
    namespace = assetPr.astSolverNamespaceSet(assetName, assetVariant) + '_' + timeTag
    #
    maFile.setMaFileReference(serverSolverProductFile, namespace)
    referenceNode = namespace + 'RN'
    maUtils.setAttrStringDatumForce_(referenceNode, prsVariants.Util.artistLabel, bscMethods.OsSystem.username())
    maUtils.setAttrStringDatumForce_(referenceNode, prsVariants.Util.updateLabel, bscMethods.OsTimestamp.active())
    maUtils.setAttrStringDatumForce_(referenceNode, prsVariants.Util.basicIndexAttrLabel, assetIndex)
