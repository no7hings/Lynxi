# coding=utf-8
import os
#
from LxBasic import bscMethods, bscModifiers
#
from LxCore import lxBasic, lxCore_
#
from LxCore.preset import appVariant, databasePr
#
from LxCore.preset.prod import projectPr, assetPr
#
from LxCore.product.op import messageOp
#
from LxDatabase import dbBasic, dbGet
#
from LxMaya.command import maUtils, maFile, maUuid, maGeom, maShdr, maTxtr, maHier, maFur, maMshReduce, maMshBox, maScnAsb
#
from LxMaya.product.data import datAsset
#
from LxMaya.product.op import assetOp
#
from LxMaya.product import maAstLoadCmds
#
from LxMaya.database import maDbAstCmds
#
isSendMail = lxCore_.LynxiIsSendMail
isSendDingTalk = lxCore_.LynxiIsSendDingTalk
#
none = ''


# Upload Model / Texture / Shader( Key Method )
@bscModifiers.fncCatchException
def astUnitModelUploadMainCmd(
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        withProduct, withAssembly, withAnimation, withAov,
        description, notes,
        repairTrans, repairHistory, repairUnlockNormal, repairSoftNormal, repairUv,
        repairMatl, repairTexture, repairAov
):
    # Renderer
    renderer = projectPr.getProjectMayaRenderer(projectName)
    # Index
    modelIndex = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
    # Updater
    timeTag = lxBasic.getOsActiveTimeTag()
    # Log Target File
    logTargetFile = lxBasic.getOsFileJoinTimeTag(
        assetPr.astUnitLogFile(
            lxCore_.LynxiRootIndex_Backup,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1],
        timeTag
    )
    # Set Log Window
    logWin_ = bscMethods.If_Log(title=u'Model Upload', logTargetFile=logTargetFile)
    logWin_.showUi()
    # Start
    logWin_.addStartTask(u'Model Upload')
    #
    maUtils.setDisplayMode(5)
    maUtils.setVisiblePanelsDelete()
    # Rename Scene
    astUnitSceneRenameCmd_(
        assetName, assetVariant, assetStage,
        renderer
    )
    # Refresh Asset
    astUnitSceneRefreshCmd_(
        assetIndex,
        assetName, assetVariant, assetStage,
        renderer
    )
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage
    )
    # Upload Source File >>> 1
    astUnitUploadModelSourceSub(
        modelIndex,
        projectName, assetClass, assetName, assetVariant, assetStage,
        timeTag,
        description,
        notes
    )
    # Clean Scene
    astUnitSceneClearCmd()
    # Repair Model
    astUnitMeshRepairCmd_(
        assetName,
        repairTrans=repairTrans, repairHistory=repairHistory,
        repairUnlockNormal=repairUnlockNormal, repairSoftNormal=repairSoftNormal,
        repairUv=repairUv
    )
    # Repair Model
    astUnitShaderRepairCmd_(
        assetName,
        repairMatl=repairMatl, repairTexture=repairTexture, repairAov=repairAov
    )
    # Upload Index >>> 2
    dbAstUploadIndex(
        assetIndex,
        projectName, assetClass, assetName, assetVariant,
        withAssembly,
        timeTag
    )
    # Extra >>> 3
    astUnitUploadExtraSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Upload Material >>> 4 - 5
    astUnitModelMaterialUploadSubCmd(
        assetIndex, modelIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        renderer, withAov,
        timeTag
    )
    # Upload Nde_Geometry >>> 9
    astUnitUploadModelGeometrySub(
        assetIndex,
        modelIndex,
        assetName,
        timeTag
    )
    # Upload Asset >>> 7 - 8
    astUnitUploadModelProductSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        renderer,
        timeTag,
        withProduct=withProduct
    )
    # Upload Preview >>> 9
    astUnitModelPreviewUploadCmd(
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        withProduct=withProduct,
        useDefaultMaterial=1
    )
    # Upload Assembly
    if withAssembly:
        withMesh = True
        # Upload Assembly
        astUnitUploadAssemblyMain(
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant, assetStage,
            renderer,
            withMesh=withMesh, withLod=withAssembly,
            timeTag=timeTag
        )
    # Open Source
    astUnitOpenModelSource(
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Complete
    logWin_.addCompleteTask()
    htmlLog = logWin_.htmlLog
    # Send Mail
    if isSendMail:
        messageOp.sendProductMessageByMail(
            htmlLog,
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant, assetStage,
            description, notes
        )
    # Send Ding Talk
    if isSendDingTalk:
        messageOp.sendProductMessageByDingTalk(
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant, assetStage,
            timeTag,
            description, notes
        )


#
def astUnitSceneRenameCmd_(
        assetName, assetVariant, assetStage,
        renderer
):
    logWin_ = bscMethods.If_Log()
    
    logWin_.addStartProgress(u'Rename Maya - Scene')
    # View Progress
    progressExplain = u'''Rename Maya - Scene'''
    maxValue = 2
    progressBar = bscMethods.If_Progress(progressExplain, maxValue)
    #
    usedObjects = []
    progressBar.update(u'''Rename Material' Nde_Node''')
    #
    if assetPr.isAstModelLink(assetStage):
        usedObjects = datAsset.getAstMeshObjects(assetName, 0)
    elif assetPr.isAstCfxLink(assetStage):
        yetiObject = datAsset.getYetiObjects(assetName)
        nurbsHairObjects = datAsset.getAstCfxNurbsHairObjects(assetName)
        #
        usedObjects = yetiObject
        usedObjects.extend(nurbsHairObjects)
    elif assetPr.isAstLightLink(assetStage):
        linkBranch = assetPr.astUnitLightLinkGroupName(assetName)
        #
        usedObjects = maUtils.getChildrenByRoot(linkBranch)
    #
    if usedObjects:
        # Rename Material >>> 01
        maShdr.setObjectsMaterialNodesRename(usedObjects, assetName, assetVariant, assetStage)
    #
    aovLis = maShdr.getAovNodeLis(renderer)
    progressBar.update(u'''Rename AOV's Nde_Node''')
    if aovLis:
        # Rename AOV >>> 02
        maShdr.setRenameAovNodes(aovLis, assetName, assetVariant)
    #
    logWin_.addCompleteProgress()


#
def astUnitSceneRefreshCmd_(
        assetIndex,
        assetName, assetVariant, assetStage,
        renderer
):
    logWin_ = bscMethods.If_Log()
    #
    logWin_.addStartProgress(u'Refresh Asset')
    #
    astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName)
    maUtils.setAttrStringDatumForce(astUnitModelProductGroup, appVariant.basicVariantAttrLabel, assetVariant)
    maUtils.setAttrStringDatumForce(astUnitModelProductGroup, appVariant.basicStageAttrLabel, assetStage)
    #
    if assetPr.isAstModelLink(assetStage):
        # Show All
        modelLinkGroupName = assetPr.astUnitModelLinkGroupName(assetName)
        maUtils.setNodeShowByGroup(modelLinkGroupName)
        #
        modelObjectLis = datAsset.getAstMeshObjects(assetName, 0)
        datAsset.getMeshesCompIndexForce(assetIndex, modelObjectLis)
        maUuid.setAttrUniqueIds(modelObjectLis)
        assetOp.setObjectTransparentRefresh(modelObjectLis)
        #
        modelShaderObjects = datAsset.getAstMeshObjects(assetName, 1)
        #
        modelIndex = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
        modelMaterials = maShdr.getObjectsMaterials(modelShaderObjects)
        datAsset.getMaterialCompIndexesForce(modelIndex, modelMaterials)
        maUuid.setAttrUniqueIds(modelMaterials)
        #
        modelAovs = maShdr.getAovNodeLis(renderer)
        datAsset.getAovCompIndexesForce(modelIndex, modelAovs)
        maUuid.setAttrUniqueIds(modelAovs)
    #
    elif assetPr.isAstCfxLink(assetStage):
        # Show All
        cfxLinkGroup = assetPr.astUnitCfxLinkGroupName(assetName)
        maUtils.setNodeShowByGroup(cfxLinkGroup)
        #
        assetSubIndex = dbGet.getDbCfxIndex(assetIndex, assetVariant)
        #
        furObjects = datAsset.getFurObjects(assetName)
        datAsset.getFurCompIndexForce(assetSubIndex, furObjects)
        #
        maUuid.setAttrUniqueIds(furObjects)
        #
        cfxShaderObjects = datAsset.getAstFurShaderObjects(assetName)
        #

        furMaterials = maShdr.getObjectsMaterials(cfxShaderObjects)
        datAsset.getMaterialCompIndexesForce(assetSubIndex, furMaterials)
        maUuid.setAttrUniqueIds(furMaterials)
        #
        cfxAovs = maShdr.getAovNodeLis(renderer)
        datAsset.getAovCompIndexesForce(assetSubIndex, cfxAovs)
        maUuid.setAttrUniqueIds(cfxAovs)
    #
    logWin_.addCompleteProgress()


# Clean Scene
def astUnitSceneClearCmd():
    logWin_ = bscMethods.If_Log()
    
    logWin_.addStartProgress(u'Scene Clean')
    # View Progress
    progressExplain = u'''Scene Clean'''
    maxValue = 8
    progressBar = bscMethods.If_Progress(progressExplain, maxValue)
    # Remove Reference >>> 01
    progressBar.update(u'''Reference File(s) Clean''')
    assetOp.setCleanReferenceFile()
    # Remove Reference Nde_Node >>> 02
    progressBar.update(u'''Reference Nde_Node(s) Clean''')
    assetOp.setCleanReferenceNode()
    # Clean Namespace >>> 03
    progressBar.update(u'''Namespace(s) Clean''')
    maUtils.setUnusedNamespacesClean()
    # Clean Unknown Nde_Node >>> 04
    progressBar.update(u'''Unknown Nde_Node(s) Clean''')
    assetOp.setUnknownNodeClear()
    # Clean Unknown Plug >>> 05
    progressBar.update(u'''Unknown Plug(s) Clean''')
    maUtils.setCleanUnknownPlugs()
    # Clean Display Layer >>> 06
    progressBar.update(u'''Display Layer(s) Clean''')
    assetOp.setDisplayLayerClear()
    # Clean Render Layer >>> 07
    progressBar.update(u'''Render Layer(s) Clean''')
    assetOp.setCleanRenderLayer()
    # Clean Unused Shader >>> 08
    progressBar.update(u'''Unused Shader(s) Clean''')
    assetOp.setUnusedShaderClear()
    #
    logWin_.addCompleteProgress()


#
def astUnitMeshRepairCmd_(
        assetName,
        repairTrans=True, repairHistory=True,
        repairUnlockNormal=True, repairSoftNormal=True,
        repairUv=True
):
    logWin_ = bscMethods.If_Log()

    logWin_.addStartProgress(u'Mesh Repair')
    
    meshObjects = datAsset.getAstMeshObjects(assetName, 0)
    # View Progress
    progressExplain = u'''Mesh Repair'''
    maxValue = 4 + [0, 3][repairTrans] + [0, 1][repairHistory] + [0, 1][repairUnlockNormal] + [0, 1][repairSoftNormal] + [0, 1][repairUv]
    progressBar = bscMethods.If_Progress(progressExplain, maxValue)
    # Low Quality Display >>> 01
    progressBar.update(u'''Set Mesh's Low Quality Display''')
    [maUtils.setObjectDisplayMode(i) for i in meshObjects]
    if repairTrans:
        # Clean Mesh's Transformations Key >>> 02
        progressBar.update(u'''Clean Mesh's Transformations - Keyframe''')
        maUtils.setObjectsCleanTransformKey(meshObjects)
        # Unlock Transformation >>> 03
        progressBar.update(u'''Unlock Mesh's Transformation''')
        maUtils.setObjectsLockTransform(meshObjects, 0)
        # Set Transformation Freeze and Rest >>> 04
        progressBar.update(u'''Freeze and Rest Mesh's Transformation ''')
        maUtils.setObjectsTransformationDefault(meshObjects)
    if repairUnlockNormal:
        progressBar.update(u'''Unlock Mesh's Normal''')
        assetOp.setMeshVertexNormalUnlockCmd(meshObjects)
    if repairSoftNormal:
        progressBar.update(u'''Soft ( Smooth ) Mesh's Edge''')
        assetOp.setMeshesSmoothNormal(meshObjects)
    if repairUv:
        # Clean Mesh's History >>> 06
        progressBar.update(u'''Repair Mesh's Uv ( Map )''')
        [maGeom.setRepairMeshMap(i) for i in meshObjects]
    if repairHistory:
        # Clean Mesh's History >>> 05
        progressBar.update(u'''Clean Mesh's History''')
        maUtils.setCleanHistory(meshObjects)
    # Clean Mesh's Unused Shape >>> 07
    progressBar.update(u'''Clean Mesh's Unused - Shape''')
    assetOp.setObjectUnusedShapeClear(meshObjects)
    # Clean Mesh's Handle >>> 08
    progressBar.update(u'''Clean Mesh's Handle''')
    [maUtils.hideHandel(i) for i in meshObjects]
    # Repair Mesh's Shape >>> 09
    progressBar.update(u'''Repair Mesh's Shape''')
    #
    logWin_.addCompleteProgress()


#
def astUnitShaderRepairCmd_(
        assetName,
        repairMatl=True, repairTexture=True, repairAov=True
):
    logWin_ = bscMethods.If_Log()

    logWin_.addStartProgress(u'Shader Repair')
    
    meshObjects = datAsset.getAstMeshObjects(assetName, 0)
    # View Progress
    progressExplain = u'''Shader Repair'''
    maxValue = [0, 1][repairMatl] + [0, 2][repairTexture] + [0, 2][repairAov]
    progressBar = bscMethods.If_Progress(progressExplain, maxValue)
    if repairMatl is True:
        # Relink Model's Material >>> 01
        progressBar.update(u'''Material Object - Set Repair''')
        maShdr.setLinkObjectsMaterial(maShdr.getObjectsMaterialRelinkData(meshObjects))
        # Relink Model's Material >>> 02
        progressBar.update(u'''Texture's Color - Space Repair''')
        maShdr.setRefreshTextureColorSpace(maShdr.getTextureNodeLisByObject(meshObjects))
    if repairTexture is True:
        # Relink Model's Material >>> 03
        progressBar.update(u'''Texture's Tx ( Arnold ) Repair''')
        maTxtr.setUpdateArnoldTx()
    if repairAov is True:
        # Relink Model's Material >>> 04
        progressBar.update(u'''AOV's Driver and Filter ( Arnold ) Repair''')
        maShdr.setRepairArnoldAov()
        # Relink Model's Material >>> 05
        progressBar.update(u'''AOV's Option ( Arnold ) Repair''')
        maShdr.setRepairAovNodesLink()


# Upload Model Source
def astUnitUploadModelSourceSub(
        modelIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        description, notes
):
    logWin_ = bscMethods.If_Log()
    # Source File >>> 01
    backModelFile = assetPr.astUnitSourceFile(
        lxCore_.LynxiRootIndex_Backup,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    #
    logWin_.addStartProgress(u'Source Upload')
    #
    linkFile = lxBasic.getOsFileJoinTimeTag(backModelFile, timeTag)
    maFile.saveMayaFile(linkFile)
    #
    dbBasic.writeDbAssetHistory(modelIndex, linkFile)
    # Update Data >>> 02
    updateData = lxCore_.lxProductRecordDatumDic(
        linkFile,
        assetStage,
        description, notes
    )
    updateFile = lxCore_._toLxProductRecordFile(linkFile)
    maFile.writeOsJson(updateData, updateFile, 4)
    #
    logWin_.addCompleteProgress()


# Open Model Source
def astUnitOpenModelSource(
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
):
    logWin_ = bscMethods.If_Log()
    # Open Source
    backModelFile = assetPr.astUnitSourceFile(
        lxCore_.LynxiRootIndex_Backup,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    localModelFile = assetPr.astUnitSourceFile(
        lxCore_.LynxiRootIndex_Local,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    logWin_.addStartProgress(u'Source ( Local ) Open')
    #
    backupSourceFileJoinUpdateTag = lxBasic.getOsFileJoinTimeTag(backModelFile, timeTag)
    maFile.openMayaFileToLocal(backupSourceFileJoinUpdateTag, localModelFile, timeTag)
    #
    logWin_.addCompleteProgress()


# Model Preview File
def astUnitModelPreviewUploadCmd(
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        withProduct=False, useDefaultMaterial=1
):
    logWin_ = bscMethods.If_Log()
    # Group Data
    astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName)
    # Model Preview File
    dbAssetPreviewFile = dbGet.getDbAstPreviewFile(assetIndex)
    # Main
    logWin_.addStartProgress(u'Preview Upload')
    #
    if not useDefaultMaterial:
        maUtils.setDisplayMode(6)
    #
    overrideColor = lxBasic.getRgbByString(assetName, maximum=1.0)
    maFile.makeSnapshot(
        astUnitModelProductGroup, dbAssetPreviewFile,
        useDefaultMaterial=useDefaultMaterial, overrideColor=overrideColor
    )
    #
    if not useDefaultMaterial:
        maUtils.setDisplayMode(5)
    #
    if withProduct:
        if assetVariant == appVariant.astDefaultVariant:
            serverBasicPreviewFile = assetPr.astUnitBasicPreviewFile(
                lxCore_.LynxiRootIndex_Server,
                projectName, assetClass, assetName
            )[1]
            maFile.setCopyFile(dbAssetPreviewFile, serverBasicPreviewFile)
        #
        serverModelPreviewFile = assetPr.astUnitPreviewFile(
            lxCore_.LynxiRootIndex_Server,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
        maFile.setCopyFile(dbAssetPreviewFile, serverModelPreviewFile)
    #
    logWin_.addCompleteProgress()


# Model Mesh
def astUnitUploadModelGeometrySub(
        assetIndex,
        modelIndex, assetName, timeTag
):
    logWin_ = bscMethods.If_Log()
    # Data
    rootGroup = assetPr.astUnitRootGroupName(assetName)
    astModelGroup = assetPr.astUnitModelLinkGroupName(assetName)
    # Parent to World
    maUtils.setParentToWorld(astModelGroup)
    maUtils.setNodeDelete(rootGroup)
    #
    shaderGeometryObjects = datAsset.getAstMeshObjects(assetName, 1)
    # Mesh Datas
    messageInScene = datAsset.getMeshObjectsEvaluateDic(shaderGeometryObjects)
    meshesInformation = datAsset.getMeshObjectsConstantDic(assetName)
    for k, v in meshesInformation.items():
        messageInScene[k] = v
    # Mesh >>>> 01
    logWin_.addStartProgress(u'Geometry Upload')
    #
    maDbAstCmds.dbAstGeometryUploadMainCmd(assetIndex, assetName, astModelGroup, timeTag)
    #
    logWin_.addCompleteProgress()
    # Model Mesh Constant Data >>>> 02
    dbAstUploadModelMeshConstant(assetIndex, assetName, timeTag)
    # Sub Model Mesh Constant Data >>>> 03
    dbAstUploadModelMeshConstant(modelIndex, assetName, timeTag)


#
def dbAstUploadIndex(
        assetIndex,
        projectName, 
        assetClass, assetName, assetVariant, 
        percentage, timeTag
):
    logWin_ = bscMethods.If_Log()
    logWin_.addStartProgress(u'Index Upload')
    # Name >>> 01
    dbAstUploadNameIndex(assetIndex, projectName, assetName, timeTag)
    # Filter >>> 02
    dbAstUploadFilter(assetIndex, assetClass, timeTag)
    # Variant >>> 03
    dbAstUploadVariant(assetIndex, assetVariant, timeTag)
    # Assembly >>> 04
    if percentage:
        dbAstUploadAssembly(assetIndex, percentage, timeTag)
    #
    logWin_.addCompleteProgress()


#
def dbAstUploadNameIndex(assetIndex, projectName, assetName, timeTag):
    # Name File
    directory = databasePr.dbAstNameIndexDirectory()
    data = dbGet.getDbAssetNameData(assetIndex, projectName, assetName)
    dbBasic.dbCompDatumWrite(assetIndex, data, directory, timeTag)


#
def dbAstUploadFilter(assetIndex, assetClass, timeTag):
    # Filter File
    directory = databasePr.dbAstFilterIndexDirectory()
    data = dbGet.getDbAssetFilterData(assetClass)
    dbBasic.dbCompDatumWrite(assetIndex, data, directory, timeTag)


#
def dbAstUploadVariant(assetIndex, assetVariant, timeTag):
    # Variant File
    directory = databasePr.dbAstVariantIndexDirectory()
    data = dbGet.getDbAssetVariantData(assetIndex, assetVariant)
    dbBasic.dbCompDatumWrite(assetIndex, data, directory, timeTag)


#
def dbAstUploadAssembly(assetIndex, percentage, timeTag):
    # Assembly File
    directory = databasePr.dbAstAssemblyIndexDirectory()
    data = dbGet.getDbAssetAssemblyData(assetIndex, percentage)
    dbBasic.dbCompDatumWrite(assetIndex, data, directory, timeTag)


#
def dbAstUploadModelMeshConstant(
        assetIndex,
        assetName,
        timeTag
):
    # Mesh Constant
    directory = databasePr.dbAstGeometryConstantDirectory()
    constantData = datAsset.getAstMeshConstantData(assetName)
    dbBasic.dbCompDatumWrite(assetIndex, constantData, directory, timeTag)


# Model Material
def astUnitModelMaterialUploadSubCmd(
        assetIndex, modelIndex,
        projectName, 
        assetClass, assetName, assetVariant, assetStage,
        renderer,
        withAov,
        timeTag
):
    logWin_ = bscMethods.If_Log()
    # Collection Texture >>>> 01
    shaderObjects = datAsset.getAstMeshObjects(assetName, 1)
    # Debug ( Must Back of Rename Scene)
    modelTextureNodes = maShdr.getTextureNodeLisByObject(shaderObjects)
    #
    dbAstTextureDirectory = databasePr.dbAstTextureDirectory()
    #
    logWin_.addStartProgress(u'Texture Upload')
    #
    if modelTextureNodes:
        serverModelTextureDirectory = dbAstTextureDirectory + '/' + modelIndex
        if appVariant.isPushModelTextureToDatabase is False:
            serverModelTextureDirectory = assetPr.astUnitTextureFolder(
                lxCore_.LynxiRootIndex_Server,
                projectName,
                assetClass, assetName, assetVariant, assetStage
            )
        isWithTx = maTxtr.getTxTextureIsCollection(renderer)
        # Collection Texture
        maTxtr.setTexturesCollection(
            serverModelTextureDirectory,
            withTx=isWithTx,
            inData=modelTextureNodes
        )
        # Repath Texture
        maTxtr.setTexturesRepath(
            serverModelTextureDirectory,
            inData=modelTextureNodes
        )
        #
        astUnitTextureBackupCmd_(
            assetIndex,
            projectName, assetClass, assetName, assetVariant, assetStage,
            modelTextureNodes, isWithTx,
            timeTag
        )
    #
    logWin_.addCompleteProgress()
    # Material File >>>> 02
    logWin_.addStartProgress(u'Material Upload')
    #
    maDbAstCmds.dbAstMaterialUploadMainCmd(shaderObjects, modelIndex, timeTag)
    if withAov is True:
        maDbAstCmds.dbAstAovUploadCmd(renderer, modelIndex, timeTag)
    #
    logWin_.addCompleteProgress()


# Model Product File
def astUnitUploadModelProductSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        renderer,
        timeTag,
        withProduct=False
):
    logWin_ = bscMethods.If_Log()
    
    logWin_.addStartProgress(u'Product Upload')
    #
    maFile.new()
    # Mesh
    maAstLoadCmds.astUnitModelGeometryLoadCmd(
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        lockTransform=False
    )
    # Material
    maAstLoadCmds.astUnitModelMaterialLoadCmd(
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        collectionTexture=False, useServerTexture=False
    )
    #
    maAstLoadCmds.astUnitExtraLoadCmd(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )
    # Refresh Branch Root
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Database
    maDbAstCmds.dbAstUploadModelProduct(assetIndex, assetVariant)
    # Server
    if withProduct:
        # Product
        serverProductFile = assetPr.astUnitProductFile(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1]
        backupProductFile = assetPr.astUnitProductFile(
            lxCore_.LynxiRootIndex_Backup,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        serverModelTextureDirectory = assetPr.astUnitTextureFolder(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )
        #
        shaderObjects = datAsset.getAstMeshObjects(assetName, 1)
        # Debug ( Must Back of Rename Scene)
        modelTextureNodes = maShdr.getTextureNodeLisByObject(shaderObjects)
        if modelTextureNodes:
            maTxtr.setTexturesCollection(
                serverModelTextureDirectory,
                withTx=maTxtr.getTxTextureIsCollection(renderer),
                inData=modelTextureNodes
            )
            maTxtr.setTexturesRepath(
                serverModelTextureDirectory,
                inData=modelTextureNodes
            )
        #
        maFile.saveMayaFile(serverProductFile)
        maFile.backupFile(serverProductFile, backupProductFile, timeTag)
        #
        meshData = datAsset.getAstMeshConstantData(assetName)
        #
        serverBasicMeshFile = assetPr.astUnitBasicMeshConstantFile(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName
        )[1]
        if assetVariant == appVariant.astDefaultVariant:
            lxBasic.writeOsJson(meshData, serverBasicMeshFile)
        #
        serverModelMeshFile = assetPr.astUnitMeshConstantFile(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        lxBasic.writeOsJson(meshData, serverModelMeshFile)
        #
        serverModelTextureDataFile = assetPr.astUnitTextureConstantFile(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        textureData = maTxtr.getTextureDatumDic(modelTextureNodes)
        #
        lxBasic.writeOsJson(textureData, serverModelTextureDataFile)
    #
    logWin_.addCompleteProgress()


# Scenery Asset File
def astUnitUploadAssemblyProductSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        renderer,
        timeTag
):
    logWin_ = bscMethods.If_Log()
    # Assembly Product File
    serverAssemblyProductFile = assetPr.astUnitAssemblyProductFile(
        projectName, assetName, assetVariant
    )[1]
    # Model Product File
    serverAstUnitModelProductFile = assetPr.astUnitProductFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, lxCore_.LynxiProduct_Asset_Link_Model
    )[1]
    # Cfx Product File
    serverAstUnitCfxProductFile = assetPr.astUnitProductFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, lxCore_.LynxiProduct_Asset_Link_Cfx
    )[1]
    # Main
    maFile.new()
    logWin_.addStartProgress(u'Product Upload')
    assetUnitRoot = assetPr.astUnitRootGroupName(assetName)
    if not maUtils.isAppExist(assetUnitRoot):
        maUtils.setAppPathCreate(assetUnitRoot)
    # Model
    if os.path.isfile(serverAstUnitModelProductFile):
        # Merger Model and Fur >>> 01
        maFile.setFileImport(serverAstUnitModelProductFile)
        astModelGroup = assetPr.astUnitModelLinkGroupName(assetName)
        maUtils.setObjectParent(astModelGroup, assetUnitRoot)
        # Collection Model Texture >>> 02
        serverAstAssemblyModelTextureDirectory = assetPr.astUnitAssemblyTextureFolder(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, lxCore_.LynxiProduct_Asset_Link_Model
        )
        #
        shaderObjects = datAsset.getAstMeshObjects(assetName, 1)
        modelTextureNodes = maShdr.getTextureNodeLisByObject(shaderObjects)
        if modelTextureNodes:
            maTxtr.setTexturesCollection(
                serverAstAssemblyModelTextureDirectory,
                withTx=maTxtr.getTxTextureIsCollection(renderer),
                inData=modelTextureNodes
            )
            maTxtr.setTexturesRepath(
                serverAstAssemblyModelTextureDirectory,
                inData=modelTextureNodes
            )
    # CFX
    if os.path.isfile(serverAstUnitCfxProductFile):
        maFile.setFileImport(serverAstUnitCfxProductFile)
        # Connect Solver Fur Group
        cfxAssetRoot = assetPr.astUnitCfxLinkGroupName(assetName)
        maUtils.setObjectParent(cfxAssetRoot, assetUnitRoot)
        forHide = maUtils.getNodeLisByType('mesh', 1, cfxAssetRoot)
        [maUtils.setHide(maUtils.getNodeTransform(i)) for i in forHide]
        # Collection CFX Texture >>> 03
        serverAssemblyCfxTextureDirectory = assetPr.astUnitAssemblyTextureFolder(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, lxCore_.LynxiProduct_Asset_Link_Cfx
        )
        #
        shaderFurObjects = datAsset.getAstFurShaderObjects(assetName)
        textureNodeLis = maShdr.getTextureNodeLisByObject(shaderFurObjects)
        if textureNodeLis:
            maTxtr.setTexturesCollection(
                serverAssemblyCfxTextureDirectory,
                withTx=maTxtr.getTxTextureIsCollection(renderer),
                inData=textureNodeLis
            )
            maTxtr.setTexturesRepath(
                serverAssemblyCfxTextureDirectory,
                inData=textureNodeLis
            )
        # Collection CFX Map >>> 04
        serverAssemblyCfxMapDirectory = assetPr.astUnitAssemblyMapFolder(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, lxCore_.LynxiProduct_Asset_Link_Cfx
        )
        maTxtr.setCollectionMaps(serverAssemblyCfxMapDirectory)
        maTxtr.setRepathMaps(serverAssemblyCfxMapDirectory)
    # Set Texture to Tx >>> ( 05 )
    if renderer == 'Arnold':
        maTxtr.setTextureAttrToTx()
    #
    maFile.saveMayaFile(serverAssemblyProductFile)
    #
    logWin_.addCompleteProgress()


#
def astUnitUploadAsbProxyCacheSub(
        projectName,
        assetClass, assetName, assetVariant,
        renderer, withLod=(50, 50)
):
    logWin_ = bscMethods.If_Log()
    # Open File
    serverAssemblyProductFile = assetPr.astUnitAssemblyProductFile(
        projectName, assetName, assetVariant
    )[1]
    if os.path.isfile(serverAssemblyProductFile):
        maFile.new()
        maFile.fileOpen(serverAssemblyProductFile)
        #
        assetUnitRoot = assetPr.astUnitRootGroupName(assetName)
        modelShaderObjects = datAsset.getAstMeshObjects(assetName, 1)
        # Main Proxy Cache
        serverAstUnitAsbProxyCacheFile = assetPr.astUnitAssemblyProxyCacheFile(
            projectName, assetName, assetVariant
        )[1]
        # CFX Cache
        furNodes = datAsset.getYetiObjects(assetName)
        if furNodes:
            serverAstUnitAsbCfxCacheDirectory = assetPr.astUnitAssemblyCacheFolder(
                lxCore_.LynxiRootIndex_Server,
                projectName,
                assetClass, assetName, assetVariant, lxCore_.LynxiProduct_Asset_Link_Cfx
            )
            # Set Fur Cache
            maFur.setOutYetisCache(serverAstUnitAsbCfxCacheDirectory, furNodes, 1, 1, 3)
        # Proxy
        logWin_.addStartProgress(u'Proxy Cache Upload')
        #
        maScnAsb.setOutAstProxy(serverAstUnitAsbProxyCacheFile, assetUnitRoot, renderer)
        # Proxy LOD
        if withLod:
            for seq in range(2):
                level = seq + 1
                percentage = withLod[seq]
                # Sub Proxy Cache
                serverAstUnitAsbProxyCacheLodFile = assetPr.astUnitAssemblyProxyCacheFile(
                    projectName, assetName, assetVariant,
                    lod=level
                )[1]
                #
                maMshReduce.setMeshesReduce(modelShaderObjects, percentage)
                maScnAsb.setOutAstProxy(serverAstUnitAsbProxyCacheLodFile, assetUnitRoot, renderer)
        #
        logWin_.addCompleteProgress()


#
def astUnitUploadAsbGpuCacheSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant,
        withLod=(50, 50), color=(.5, .5, .5)
):
    logWin_ = bscMethods.If_Log()
    # Check is Default Variant
    if assetVariant == appVariant.astDefaultVariant:
        maFile.new()
        #
        maDbAstCmds.dbAstGeometryLoadMainCmd(
            assetIndex, assetName, lockTransform=False
        )
        #
        astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName)
        modelShaderObjects = datAsset.getAstMeshObjects(assetName, 1)
        #
        serverAstUnitAsbGpuCacheFile = assetPr.astUnitAssemblyGpuCacheFile(
            projectName, assetName
        )[1]
        logWin_.addStartProgress(u'GPU Cache Upload')
        #
        r, g, b = color
        maUtils.setDefaultShaderColor(r, g, b)
        #
        for meshObject in modelShaderObjects:
            renderVisible = maUtils.getAttrDatum(meshObject, lxCore_.LynxiAttrName_Object_RenderVisible)
            transparent = maUtils.getAttrDatum(meshObject, lxCore_.LynxiAttrName_Object_Transparent)
            if renderVisible is False:
                maUtils.setGpuShader(meshObject, r, g, b, 1)
            elif transparent is True:
                maUtils.setGpuShader(meshObject, r, g, b, .75)
            else:
                maUtils.setGpuShader(meshObject, r, g, b, 0)

        # GPU
        maFile.gpuExport(
            astUnitModelProductGroup, serverAstUnitAsbGpuCacheFile,
            0, 0
        )
        # GPU LOD
        if withLod:
            for seq in range(2):
                level = seq + 1
                percentage = withLod[seq]
                #
                serverAstUnitAsbGpuCacheLodFile = assetPr.astUnitAssemblyGpuCacheFile(
                    projectName, assetName, lod=level
                )[1]
                maMshReduce.setMeshesReduce(modelShaderObjects, percentage)
                maFile.gpuExport(
                    astUnitModelProductGroup, serverAstUnitAsbGpuCacheLodFile,
                    0, 0
                )
        #
        logWin_.addCompleteProgress()


#
def astUploadSceneryUnitBoxCacheSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant,
        color=(.5, .5, .5)
):
    logWin_ = bscMethods.If_Log()
    # Check is Default Variant
    if assetVariant == appVariant.astDefaultVariant:
        maFile.new()
        #
        maDbAstCmds.dbAstGeometryLoadMainCmd(assetIndex, assetName, lockTransform=False)
        #
        boxGroup = 'box_temp'
        astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName)
        modelShaderObjects = datAsset.getAstMeshObjects(assetName, 1)
        #
        serverAstUnitAsbBoxCacheFile = assetPr.astUnitAssemblyBoxCacheFile(
            projectName, assetName
        )[1]
        logWin_.addStartProgress(u'Box Cache Upload')
        #
        r, g, b = color
        maUtils.setDefaultShaderColor(r, g, b)
        maUtils.setObjectDefaultShaderCmd(modelShaderObjects)
        #
        maMshBox.setMeshesBox(astUnitModelProductGroup, boxGroup)
        maFile.gpuExport(boxGroup, serverAstUnitAsbBoxCacheFile, 0, 0)
        #
        logWin_.addCompleteProgress()


#
def astUnitUploadAssemblyProxySub(
        projectName,
        assetClass, assetName, assetVariant,
        renderer, withLod=(50, 50)
):
    logWin_ = bscMethods.If_Log()
    # Proxy
    serverAstUnitAsbProxyFile = assetPr.astUnitAssemblyProxyFile(
        projectName, assetName, assetVariant
    )[1]
    # Box Cache
    serverAstUnitAsbBoxCacheFile = assetPr.astUnitAssemblyBoxCacheFile(
        projectName, assetName
    )[1]
    # GPU Cache
    serverAstUnitAsbGpuCacheFile = assetPr.astUnitAssemblyGpuCacheFile(
        projectName, assetName
    )[1]
    # Proxy Cache
    serverAstUnitAsbProxyCacheFile = assetPr.astUnitAssemblyProxyCacheFile(
        projectName, assetName, assetVariant
    )[1]
    #
    logWin_.addStartProgress(u'Proxy Upload')
    #
    astUnitAssemblyProxyUploadCmd(
        assetName,
        serverAstUnitAsbProxyFile,
        serverAstUnitAsbBoxCacheFile, serverAstUnitAsbGpuCacheFile, serverAstUnitAsbProxyCacheFile,
        renderer
    )
    # LOD
    if withLod:
        for seq in range(2):
            level = seq + 1
            # Proxy
            serverAstUnitAsbProxyLodFile = assetPr.astUnitAssemblyProxyFile(
                projectName, assetName, assetVariant,
                lod=level
            )[1]
            # Gpu Cache
            serverSceneryUnitGpuCacheLodFile = assetPr.astUnitAssemblyGpuCacheFile(
                projectName, assetName,
                lod=level
            )[1]
            # Proxy Cache
            serverAstUnitAsbProxyCacheLodFile = assetPr.astUnitAssemblyProxyCacheFile(
                projectName, assetName, assetVariant,
                lod=level
            )[1]
            # To Proxy
            astUnitAssemblyProxyUploadCmd(
                assetName,
                serverAstUnitAsbProxyLodFile,
                serverAstUnitAsbBoxCacheFile, serverSceneryUnitGpuCacheLodFile, serverAstUnitAsbProxyCacheLodFile,
                renderer
            )
    #
    logWin_.addCompleteProgress()


#
def astUnitAssemblyProxyUploadCmd(
        assetName,
        serverAstUnitAsbProxyFile, serverAstUnitAsbBoxCacheFile, serverAstUnitAsbGpuCacheFile, serverAstUnitAsbProxyCacheFile,
        renderer
):
    maFile.new()
    #
    astAssemblyObject = assetPr.astAssemblyBasicObjectNameSet(assetName)
    #
    maScnAsb.setProxyCreate(
        astAssemblyObject,
        serverAstUnitAsbBoxCacheFile,
        serverAstUnitAsbGpuCacheFile,
        serverAstUnitAsbProxyCacheFile,
        renderer
    )
    #
    maFile.saveMayaFile(serverAstUnitAsbProxyFile)


#
def astUnitUploadAssemblyDefinitionSub(
        projectName,
        assetClass, assetName, assetVariant,
        withLod=(50, 50)
):
    logWin_ = bscMethods.If_Log()
    # Scenery AD File
    maFile.new()
    # AD >>> 01
    serverAstUnitAsbDefinitionFile = assetPr.astUnitAssemblyDefinitionFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, lxCore_.LynxiProduct_Asset_Link_Assembly
    )[1]
    # Box Cache
    serverAstUnitAsbBoxCacheFile = assetPr.astUnitAssemblyBoxCacheFile(
        projectName, assetName
    )[1]
    # GPU Cache
    serverAstUnitAsbGpuCacheFile = assetPr.astUnitAssemblyGpuCacheFile(
        projectName, assetName
    )[1]
    # Proxy
    serverAstUnitAsbProxyFile = assetPr.astUnitAssemblyProxyFile(
        projectName, assetName, assetVariant
    )[1]
    # Asset
    serverAssemblyProductFile = assetPr.astUnitAssemblyProductFile(
        projectName, assetName, assetVariant
    )[1]
    # Set AD
    logWin_.addStartProgress(u'Definition Upload')
    #
    if not os.path.isfile(serverAstUnitAsbDefinitionFile):
        astAssemblyObject = assetPr.astAssemblyBasicObjectNameSet(assetName)
        # Create
        maScnAsb.setCreateAssemblyDefinition(
            astAssemblyObject,
            serverAstUnitAsbBoxCacheFile,
            serverAstUnitAsbGpuCacheFile,
            serverAstUnitAsbProxyFile,
            serverAssemblyProductFile
        )
        #
        maFile.saveMayaFile(serverAstUnitAsbDefinitionFile)
    #
    logWin_.addCompleteProgress()


#
def astUnitUploadAssemblyMain(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        renderer,
        withMesh,
        withLod=(50, 50),
        timeTag=None
):
    #
    astAssemblyIndexFile = assetPr.astUnitAssemblyIndexFile(projectName, assetName)[1]
    if not lxBasic.isOsExistsFile(astAssemblyIndexFile):
        astAssemblyIndexDatum = assetPr.astUnitAssemblyIndexDatum(assetIndex, assetClass, assetName)
        lxBasic.writeOsJson(astAssemblyIndexDatum, astAssemblyIndexFile)
    # Upload Sub Asset >>>> 01
    astUnitUploadAssemblyProductSub(
        assetIndex,
        projectName, assetClass, assetName, assetVariant, assetStage,
        renderer,
        timeTag
    )
    # GPU and Box >>>> 02
    if withMesh:
        # Get Random Color
        color = lxBasic.getRgbByString(
            assetName, maximum=1.0
        )
        # GPU
        astUnitUploadAsbGpuCacheSub(
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant,
            withLod=withLod, color=color
        )
        # Box
        astUploadSceneryUnitBoxCacheSub(
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant,
            color=color
        )
    # Proxy Cache >>>> 03
    astUnitUploadAsbProxyCacheSub(
        projectName,
        assetClass, assetName, assetVariant,
        renderer, withLod=withLod
    )
    # Proxy >>>> 04
    astUnitUploadAssemblyProxySub(
        projectName,
        assetClass, assetName, assetVariant,
        renderer, withLod=withLod
    )
    # AD >>>> 05
    astUnitUploadAssemblyDefinitionSub(
        projectName,
        assetClass, assetName, assetVariant,
        withLod=withLod
    )
    #
    maFile.new()


# Upload Rig
@bscModifiers.fncCatchException
def astUnitUploadRigMain(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        withProduct,
        description, notes
):
    rigIndexKey = dbGet.getDbAstRigIndex(assetIndex)
    # Update Label
    timeTag = lxBasic.getOsActiveTimeTag()
    logTargetFile = lxBasic.getOsFileJoinTimeTag(
        assetPr.astUnitLogFile(
            lxCore_.LynxiRootIndex_Backup,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1],
        timeTag
    )
    # Set Log Window
    logWin_ = bscMethods.If_Log(title=u'Rig Upload', logTargetFile=logTargetFile)
    logWin_.showUi()
    # Start
    logWin_.addStartTask(u'Rig Upload')
    # Switch Display Mode
    maUtils.setDisplayMode(5)
    maUtils.setVisiblePanelsDelete()
    #
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage
    )
    # Save Source >>> 1
    astUnitUploadSourceSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        description, notes)
    # Clean Scene
    astUnitSceneClearCmd()
    # TD Command
    tdCommand = assetPr.getAstTdUploadCommand(projectName, lxCore_.LynxiProduct_Asset_Link_Rig)
    if tdCommand:
        maUtils.runMelCommand(tdCommand)
    # Extra >>> 2
    astUnitUploadExtraSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Mesh Constant  >>> 3
    dbAstUploadModelMeshConstant(
        rigIndexKey,
        assetName,
        timeTag
    )
    # Product  >>> 4
    astUnitUploadRigProduct(
        assetIndex,
        projectName,
        assetClass, assetName, assetStage, assetVariant,
        timeTag,
        withProduct=withProduct
    )
    # Open Source
    astUnitSourceOpenCmd_(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Complete
    logWin_.addCompleteTask()
    htmlLog = logWin_.htmlLog
    # Send Mail
    if isSendMail:
        messageOp.sendProductMessageByMail(
            htmlLog,
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant, assetStage,
            description, notes
        )
    # Send Ding Talk
    if isSendDingTalk:
        messageOp.sendProductMessageByDingTalk(
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant, assetStage,
            timeTag,
            description, notes
        )


#
def astUnitUploadRigProduct(
        assetIndex,
        projectName,
        assetClass, assetName, assetStage, assetVariant,
        timeTag,
        withProduct=False
):
    logWin_ = bscMethods.If_Log()
    
    logWin_.addStartProgress(u'Product Upload')
    #
    serverRigProductFile = assetPr.astUnitProductFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, lxCore_.LynxiProduct_Asset_Link_Rig
    )[1]
    backupRigProductFile = assetPr.astUnitProductFile(
        lxCore_.LynxiRootIndex_Backup,
        projectName,
        assetClass, assetName, assetVariant, lxCore_.LynxiProduct_Asset_Link_Rig
    )[1]
    rigAstTempFile = lxBasic.getOsTemporaryFile(serverRigProductFile, timeTag)
    #
    rigAstRoot = assetPr.astUnitRootGroupName(assetName)
    rigAstSetObjects = maUtils.getSets()
    maFile.exportMayaFileWithSet(rigAstTempFile, rigAstRoot, rigAstSetObjects)
    # Open and Upload
    maFile.fileOpen(rigAstTempFile)
    #
    assetVariant = appVariant.astDefaultVariant
    serverRigTextureDirectory = assetPr.astUnitTextureFolder(
        lxCore_.LynxiRootIndex_Server,
        projectName, assetClass, assetName, assetVariant, assetStage
    )
    # Collection Texture
    shaderObjects = datAsset.getAstMeshObjects(assetName, 1)
    if shaderObjects:
        modelTextureNodes = maShdr.getTextureNodeLisByObject(shaderObjects)
        maTxtr.setTexturesCollection(
            serverRigTextureDirectory,
            withTx=False,
            inData=modelTextureNodes
        )
        maTxtr.setTexturesRepath(
            serverRigTextureDirectory,
            inData=modelTextureNodes
        )
    # Refresh Branch Root
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    maDbAstCmds.dbAstUploadRigAssetIntegration(assetIndex)
    if withProduct:
        maFile.saveMayaFile(serverRigProductFile)
        maFile.backupFile(serverRigProductFile, backupRigProductFile, timeTag)
        #
        serverMeshConstantFile = assetPr.astUnitMeshConstantFile(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        meshData = datAsset.getAstMeshConstantData(assetName)
        #
        maFile.writeOsJson(meshData, serverMeshConstantFile, 4)
    #
    logWin_.addCompleteProgress()


@bscModifiers.fncCatchException
def astUnitCfxUploadMainCmd(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        withProduct, withAssembly, withAov,
        description, notes
):
    renderer = projectPr.getProjectMayaRenderer(projectName)
    # Index
    assetSubIndex = dbGet.getDbCfxIndex(assetIndex, assetVariant)
    timeTag = lxBasic.getOsActiveTimeTag()
    # Log Target File
    logTargetFile = lxBasic.getOsFileJoinTimeTag(
        assetPr.astUnitLogFile(
            lxCore_.LynxiRootIndex_Backup,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1],
        timeTag
    )
    # Set Log Window
    logWin_ = bscMethods.If_Log(title=u'Groom Upload', logTargetFile=logTargetFile)
    logWin_.showUi()
    # Start
    logWin_.addStartTask(u'Groom Upload')
    # Switch Display Mode
    maUtils.setDisplayMode(5)
    maUtils.setVisiblePanelsDelete()
    # Rename Scene
    astUnitSceneRenameCmd_(
        assetName, assetVariant, assetStage,
        renderer
    )
    # Refresh Asset
    astUnitSceneRefreshCmd_(
        assetIndex,
        assetName, assetVariant, assetStage,
        renderer
    )
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage
    )
    # Source >>> 01
    astUnitUploadSourceSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        description, notes
    )
    # Clean Scene >>> 02
    astUnitSceneClearCmd()
    # CFX Mesh Constant Data
    dbAstUploadModelMeshConstant(
        assetSubIndex,
        assetName,
        timeTag
    )
    # Upload Material >>> 04 - 05
    astUnitCfxMaterialUploadSubCmd(
        assetIndex, assetSubIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        renderer,
        withAov,
        timeTag
    )
    # Upload Nde_Node >>> 09 - 10 - 11
    astUnitUploadCfxFurSub(
        assetIndex, assetSubIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Upload Asset >>> 12
    astUnitUploadCfxProduct(
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        renderer, withProduct
    )
    # Upload Scenery
    if withAssembly:
        # Upload Scenery
        astUnitUploadAssemblyMain(
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant, assetStage,
            renderer,
            withMesh=False,
            withLod=False,
            timeTag=timeTag
        )
    # Open Source
    astUnitSourceOpenCmd_(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Complete
    logWin_.addCompleteTask()
    htmlLog = logWin_.htmlLog
    # Send Mail
    if isSendMail:
        messageOp.sendProductMessageByMail(
            htmlLog,
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant, assetStage,
            description, notes
        )
    # Send Ding Talk
    if isSendDingTalk:
        messageOp.sendProductMessageByDingTalk(
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant, assetStage,
            timeTag,
            description, notes
        )


# Upload CFX Nde_Node
def astUnitUploadCfxFurSub(
        assetIndex, assetSubIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
):
    logWin_ = bscMethods.If_Log()
    
    rootGroup = assetPr.astUnitRootGroupName(assetName)
    cfxAssetRoot = assetPr.astUnitCfxLinkGroupName(assetName)
    cfxSet = assetPr.cfxSetName(assetName)
    yetiObjects = datAsset.getYetiObjects(assetName)
    nurbsHairObjects = datAsset.getAstCfxNurbsHairObjects(assetName)
    # Assign Default Shader
    assetOp.setRootDefaultShaderCmd(cfxAssetRoot)
    #
    assetOp.setObjectDefaultShaderCmd(yetiObjects)
    assetOp.setObjectDefaultShaderCmd(nurbsHairObjects)
    # Set
    maFur.setYetisGuideSet(yetiObjects, cfxSet)
    # Parent to World
    maUtils.setParentToWorld(cfxAssetRoot)
    maUtils.setNodeDelete(rootGroup)
    # Export File
    serverAstUnitFurFile = assetPr.astUnitFurFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    #
    tempFurFile = lxBasic.getOsTemporaryFile(serverAstUnitFurFile, timeTag)
    maFile.exportMayaFileWithSet(tempFurFile, cfxAssetRoot, cfxSet)
    # Open and Upload
    maFile.fileOpen(tempFurFile)
    #
    assetOp.setUnusedShaderClear()
    # Nde_Node
    furObjects = []
    #
    yetiObjects = datAsset.getYetiObjects(assetName)
    pfxHairObjects = datAsset.getPfxHairObjects(assetName)
    nurbsHairObjects = datAsset.getAstCfxNurbsHairObjects(assetName)
    # Set Nurbs Hair Show Mode
    maFur.setNurbsHairObjectsShowMode_(nurbsHairObjects)
    #
    furObjects.extend(yetiObjects)
    furObjects.extend(pfxHairObjects)
    furObjects.extend(nurbsHairObjects)
    # Debug ( Close Hair System's Solver )
    [maFur.setYetiObjectCloseSolver(i) for i in yetiObjects]
    [maFur.setPfxHairObjectCloseSolver(i) for i in pfxHairObjects]
    # Collection Map
    dbCfxMapDirectory = databasePr.dbAstMapDirectory()
    #
    logWin_.addStartProgress(u'Map Upload')
    if furObjects:
        serverMapFolder = dbCfxMapDirectory + '/' + assetSubIndex
        if appVariant.isPushCfxMapToDatabase is False:
            serverMapFolder = assetPr.astUnitMapFolder(
                lxCore_.LynxiRootIndex_Server,
                projectName,
                assetClass, assetName, assetVariant, assetStage
            )
        # Collection
        maTxtr.setCollectionMaps(serverMapFolder, furObjects)
        # Repath Map
        maTxtr.setRepathMaps(serverMapFolder, furObjects)
    #
    logWin_.addCompleteProgress()
    # Progress >>> 02
    logWin_.addStartProgress(u'Fur Upload')
    #
    maUtils.setAttrStringDatumForce(cfxAssetRoot, appVariant.basicVariantAttrLabel, assetVariant)
    # Production
    maDbAstCmds.dbAstUploadFurProduct(assetIndex, assetVariant)
    # HisTory
    maDbAstCmds.dbAstUploadFurMain(furObjects, assetSubIndex, timeTag)
    # Solver
    astUnitUploadCfxFurForSolver_(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    #
    logWin_.addCompleteProgress()


#
def astUnitUploadCfxFurForSolver_(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
):
    #
    logWin_ = bscMethods.If_Log()
    
    assetSubIndex = dbBasic.getDatabaseSubIndex(
        assetIndex,
        [assetPr.getAssetLink(assetStage), assetVariant]
    )
    logWin_.addStartProgress(u'Cache Upload')
    # NurbsHair
    nurbsHairObjects = datAsset.getAstCfxNurbsHairObjects(assetName)
    #
    logWin_.addCompleteProgress()
    #
    maDbAstCmds.dbAstUploadNurbsHairMain(nurbsHairObjects, assetSubIndex, timeTag)


#
def astUnitCfxMaterialUploadSubCmd(
        assetIndex, assetSubIndex,
        projectName, assetClass, assetName, assetVariant, assetStage,
        renderer,
        withAov,
        timeTag
):
    logWin_ = bscMethods.If_Log()
    # Collection Texture >>>> 01
    dbAstTextureDirectory = databasePr.dbAstTextureDirectory()
    #
    logWin_.addStartProgress(u'Texture Upload')
    #
    yetiObject = datAsset.getYetiObjects(assetName)
    nurbsHairObjects = datAsset.getAstCfxNurbsHairObjects(assetName)
    #
    shaderFurNodes = yetiObject
    shaderFurNodes.extend(nurbsHairObjects)
    # Debug ( Must Back of Rename Scene)
    textureNodeLis = maShdr.getTextureNodeLisByObject(shaderFurNodes)
    if textureNodeLis:
        if appVariant.isPushCfxTextureToDatabase is False:
            cfxTextureDirectory = assetPr.astUnitTextureFolder(
                lxCore_.LynxiRootIndex_Server,
                projectName,
                assetClass, assetName, assetVariant, assetStage
            )
        else:
            cfxTextureDirectory = dbAstTextureDirectory + '/' + assetSubIndex
        #
        isWithTx = maTxtr.getTxTextureIsCollection(renderer)
        #
        maTxtr.setTexturesCollection(
            cfxTextureDirectory,
            withTx=isWithTx,
            inData=textureNodeLis
        )
        #
        maTxtr.setTexturesRepath(
            cfxTextureDirectory,
            inData=textureNodeLis
        )
        #
        astUnitTextureBackupCmd_(
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant, assetStage,
            textureNodeLis, isWithTx,
            timeTag
        )
    #
    logWin_.addCompleteProgress()
    # Material File >>>> 02
    logWin_.addStartProgress(u'Material Upload')
    #
    maDbAstCmds.dbAstMaterialUploadMainCmd(shaderFurNodes, assetSubIndex, timeTag)
    if withAov is True:
        maDbAstCmds.dbAstAovUploadCmd(renderer, assetSubIndex, timeTag)
    #
    logWin_.addCompleteProgress()


# Upload CFX Product
def astUnitUploadCfxProduct(
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        renderer,
        withProduct=False
):
    logWin_ = bscMethods.If_Log()
    
    logWin_.addStartProgress(u'Product Upload')
    # New Scene
    maFile.new()
    # Fur
    maAstLoadCmds.astUnitCfxFurLoadCmd(
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        collectionMap=False, useServerMap=False
    )
    # Material
    maAstLoadCmds.astUnitLoadCfxMaterialSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        collectionTexture=False, useServerTexture=False
    )
    # Refresh Branch Root
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Database
    maDbAstCmds.dbAstUploadCfxProduct(assetIndex, assetVariant)
    if withProduct:
        furObjects = []
        yetiObjects = datAsset.getYetiObjects(assetName)
        furObjects.extend(yetiObjects)
        pfxHairObjects = datAsset.getPfxHairObjects(assetName)
        furObjects.extend(pfxHairObjects)
        # Asset File
        serverCfxProductFile = assetPr.astUnitProductFile(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1]
        backupCfxProductFile = assetPr.astUnitProductFile(
            lxCore_.LynxiRootIndex_Backup,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        serverCfxTextureDirectory = assetPr.astUnitTextureFolder(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )
        serverCfxMapDirectory = assetPr.astUnitMapFolder(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )
        #
        textureNodeLis = maShdr.getTextureNodeLisByObject(yetiObjects)
        if textureNodeLis:
            withTx = maTxtr.getTxTextureIsCollection(renderer)
            maTxtr.setTexturesCollection(
                serverCfxTextureDirectory,
                withTx=withTx,
                inData=textureNodeLis
            )
            maTxtr.setTexturesRepath(
                serverCfxTextureDirectory,
                inData=textureNodeLis
            )
        #
        if furObjects:
            maTxtr.setCollectionMaps(
                serverCfxMapDirectory,
                inData=furObjects
            )
            maTxtr.setRepathMaps(
                serverCfxMapDirectory,
                inData=furObjects
            )
        #
        maFile.saveMayaFile(serverCfxProductFile)
        maFile.backupFile(serverCfxProductFile, backupCfxProductFile, timeTag)
    #
    logWin_.addCompleteProgress()


@bscModifiers.fncCatchException
def astUnitUploadMain(
        assetIndex,
        projectName, 
        assetClass, assetName, assetVariant, assetStage,
        withProduct=True, description=None, notes=None
):
    assetStagePrettify = assetStage.capitalize()
    timeTag = lxBasic.getOsActiveTimeTag()

    logTargetFile = lxBasic.getOsFileJoinTimeTag(
        assetPr.astUnitLogFile(
            lxCore_.LynxiRootIndex_Backup,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1],
        timeTag
    )
    logWin_ = bscMethods.If_Log(title=u'{} Upload'.format(assetStagePrettify), logTargetFile=logTargetFile)
    logWin_.showUi()
    # Start
    logWin_.addStartTask(u'{} Upload'.format(assetStagePrettify))
    # Switch Display Mode
    maUtils.setDisplayMode(5)
    maUtils.setVisiblePanelsDelete()
    #
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage
    )
    # Source >>> 01
    astUnitUploadSourceSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        description, notes
    )
    # Clean Scene
    astUnitSceneClearCmd()
    # Extra >>> 02
    astUnitUploadExtraSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Remove Reference
    astUnitRemoveReferenceSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Product >>> 03
    astUnitUploadProductSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Preview >>> 04
    astUnitUploadPreviewSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Open Source
    astUnitSourceOpenCmd_(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Complete
    logWin_.addCompleteTask()
    htmlLog = logWin_.htmlLog
    # Send Mail
    if isSendMail:
        messageOp.sendProductMessageByMail(
            htmlLog,
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant, assetStage,
            description, notes
        )
    # Send Ding Talk
    if isSendDingTalk:
        messageOp.sendProductMessageByDingTalk(
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant, assetStage,
            timeTag,
            description, notes
        )


#
def astUnitUploadSourceSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        description, notes
):
    logWin_ = bscMethods.If_Log()
    # Sub Index
    if assetPr.isAstRigLink(assetStage):
        assetSubIndex = dbGet.getDbAstRigIndex(assetIndex)
    else:
        assetSubIndex = dbBasic.getDatabaseSubIndex(
            assetIndex,
            [assetPr.getAssetLink(assetStage), assetVariant]
        )
    # Source
    backupSourceFile = assetPr.astUnitSourceFile(
        lxCore_.LynxiRootIndex_Backup,
        projectName, assetClass, assetName, assetVariant, assetStage
    )[1]
    logWin_.addStartProgress(u'Source Upload')
    #
    linkFile = lxBasic.getOsFileJoinTimeTag(backupSourceFile, timeTag)
    #
    maFile.saveMayaFile(linkFile)
    # Database History
    dbBasic.writeDbAssetHistory(assetSubIndex, linkFile)
    # Update
    updateData = lxCore_.lxProductRecordDatumDic(
        linkFile,
        assetStage,
        description, notes
    )
    updateFile = lxCore_._toLxProductRecordFile(linkFile)
    lxBasic.writeOsJson(updateData, updateFile, 4)
    #
    logWin_.addCompleteProgress()


#
def astUnitSourceOpenCmd_(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
):
    logWin_ = bscMethods.If_Log()
    # Open Source
    backupSourceFile = assetPr.astUnitSourceFile(
        lxCore_.LynxiRootIndex_Backup,
        projectName, assetClass, assetName, assetVariant, assetStage
    )[1]
    localSourceFile = assetPr.astUnitSourceFile(
        lxCore_.LynxiRootIndex_Local,
        projectName, assetClass, assetName, assetVariant, assetStage
    )[1]
    logWin_.addStartProgress(u'Source ( Local ) Open')
    #
    backupSourceFileJoinUpdateTag = lxBasic.getOsFileJoinTimeTag(backupSourceFile, timeTag)
    maFile.openMayaFileToLocal(backupSourceFileJoinUpdateTag, localSourceFile, timeTag)
    #
    logWin_.addCompleteProgress()


#
def astUnitTextureBackupCmd_(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        textureNodes,
        isWithTx,
        timeTag
):
    backupTextureFolder = assetPr.astUnitTextureFolder(
        lxCore_.LynxiRootIndex_Backup,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )
    serverTextureIndexFile = assetPr.astUnitTextureIndexFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    backupTextureIndexFile = assetPr.astUnitTextureIndexFile(
        lxCore_.LynxiRootIndex_Backup,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    # Backup Texture
    textureIndexData = maTxtr.setBackupTextures(
        backupTextureFolder,
        withTx=isWithTx,
        inData=textureNodes
    )
    # Texture Index
    lxBasic.writeOsJson(textureIndexData, serverTextureIndexFile)
    lxBasic.backupOsFile(serverTextureIndexFile, backupTextureIndexFile, timeTag)


#
def astUnitTextureUploadCmd_(
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        textureNodes,
        isWithTx
):
    if textureNodes:
        serverTextureFolder = assetPr.astUnitTextureFolder(
            lxCore_.LynxiRootIndex_Server,
            projectName, assetClass, assetName, assetVariant, assetStage
        )
        maTxtr.setTexturesCollection(
            serverTextureFolder,
            withTx=isWithTx,
            inData=textureNodes
        )
        maTxtr.setTexturesRepath(
            serverTextureFolder,
            inData=textureNodes
        )


#
def astUnitRemoveReferenceSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
):
    referBranchLis = []
    if assetPr.isAstSolverLink(assetStage):
        modelBranch = assetPr.astUnitModelLinkGroupName(assetName)
        referBranchLis.append(modelBranch)
        #
        serverMeshConstantFile = assetPr.astUnitMeshConstantFile(
            lxCore_.LynxiRootIndex_Server,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
        backupMeshConstantFile = assetPr.astUnitMeshConstantFile(
            lxCore_.LynxiRootIndex_Backup,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        meshData = datAsset.getAstMeshConstantData(assetName)
        #
        lxBasic.writeOsJson(meshData, serverMeshConstantFile, 4)
        lxBasic.backupOsFile(serverMeshConstantFile, backupMeshConstantFile, timeTag)
        #
        cfxBranch = assetPr.astUnitCfxLinkGroupName(assetName)
        referBranchLis.append(cfxBranch)
        #
        assetOp.setDisconnectNhrGuideObjectsConnection(assetName)
    #
    elif assetPr.isAstLightLink(assetStage):
        modelBranch = assetPr.astUnitModelLinkGroupName(assetName)
        referBranchLis.append(modelBranch)
        #
        serverMeshConstantFile = assetPr.astUnitMeshConstantFile(
            lxCore_.LynxiRootIndex_Server,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
        backupMeshConstantFile = assetPr.astUnitMeshConstantFile(
            lxCore_.LynxiRootIndex_Backup,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        meshData = datAsset.getAstMeshConstantData(assetName)
        #
        lxBasic.writeOsJson(meshData, serverMeshConstantFile, 4)
        lxBasic.backupOsFile(serverMeshConstantFile, backupMeshConstantFile, timeTag)
    #
    if referBranchLis is not None:
        for referBranch in referBranchLis:
            if maUtils.isAppExist(referBranch):
                maUtils.setNodeDelete(referBranch)


#
def astUnitUploadProductSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
):
    logWin_ = bscMethods.If_Log()
    
    rootGroup = assetPr.astUnitRootGroupName(assetName)
    linkBranch = None
    if assetPr.isAstSolverLink(assetStage):
        linkBranch = assetPr.astUnitSolverLinkGroupName(assetName)
    elif assetPr.isAstLightLink(assetStage):
        linkBranch = assetPr.astUnitLightLinkGroupName(assetName)
    #
    if linkBranch is not None:
        if maUtils.isAppExist(linkBranch):
            serverProductFile = assetPr.astUnitProductFile(
                lxCore_.LynxiRootIndex_Server,
                projectName, assetClass, assetName, assetVariant, assetStage
            )[1]
            backupProductFile = assetPr.astUnitProductFile(
                lxCore_.LynxiRootIndex_Backup,
                projectName, assetClass, assetName, assetVariant, assetStage
            )[1]
            #
            logWin_.addStartProgress(u'Product Upload')
            #
            tempFile = lxBasic.getOsTemporaryFile(serverProductFile, timeTag)
            #
            maUtils.setParentToWorld(linkBranch)
            maUtils.setNodeDelete(rootGroup)
            #
            maFile.fileExport(linkBranch, tempFile, history=1)
            # Open and Upload
            maFile.fileOpen(tempFile)
            # Refresh Branch Root
            maHier.astUnitRefreshRoot(
                assetIndex,
                assetClass, assetName, assetVariant, assetStage,
                timeTag
            )
            # Upload Texture
            astUnitUploadTextureSub(
                assetIndex,
                projectName,
                assetClass, assetName, assetVariant, assetStage,
                timeTag
            )
            # Upload Cache
            maAstLoadCmds.astUnitCacheLoadCmd(
                assetIndex,
                projectName,
                assetClass, assetName, assetVariant, assetStage,
                collectionCache=False, useServerTexture=True
            )
            #
            maFile.saveMayaFile(serverProductFile)
            maFile.backupFile(serverProductFile, backupProductFile, timeTag)
            #
            logWin_.addCompleteProgress()


#
def astUnitUploadTextureSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
):
    logWin_ = bscMethods.If_Log()
    
    linkBranch = None
    isWithTx = False
    if assetPr.isAstLightLink(assetStage):
        linkBranch = assetPr.astUnitLightLinkGroupName(assetName)
        isWithTx = True
    if linkBranch is not None:
        if maUtils.isAppExist(linkBranch):
            shaderObjects = maUtils.getChildrenByRoot(linkBranch)
            logWin_.addStartProgress(u'Texture Upload')
            #
            if shaderObjects:
                textureNodes = maShdr.getTextureNodeLisByObject(shaderObjects)
                if textureNodes:
                    # Backup
                    astUnitTextureBackupCmd_(
                        assetIndex,
                        projectName,
                        assetClass, assetName, assetVariant, assetStage,
                        textureNodes,
                        isWithTx,
                        timeTag
                    )
                    # Upload
                    astUnitTextureUploadCmd_(
                        projectName,
                        assetClass, assetName, assetVariant, assetStage,
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
def astUnitUploadGeometrySub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
):
    pass


#
def astUnitUploadExtraSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
):
    logWin_ = bscMethods.If_Log()
    
    extraData = None
    # Rig
    if assetPr.isAstModelLink(assetStage):
        extraData = datAsset.getAstUnitModelExtraData(assetName)
    elif assetPr.isAstRigLink(assetStage):
        extraData = datAsset.getAstUnitRigExtraData(assetName)
    elif assetPr.isAstSolverLink(assetStage):
        extraData = datAsset.getAstUnitRigSolExtraData(assetName)
    #
    if extraData:
        serverExtraFile = assetPr.astUnitExtraFile(
            lxCore_.LynxiRootIndex_Server,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
        backupExtraFile = assetPr.astUnitExtraFile(
            lxCore_.LynxiRootIndex_Backup,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        logWin_.addStartProgress(u'Extra Upload')
        #
        lxBasic.writeOsJsonDic(extraData, serverExtraFile, 4)
        lxBasic.backupOsFile(serverExtraFile, backupExtraFile, timeTag)
        #
        logWin_.addCompleteProgress()


#
def astUnitUploadPreviewSub(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
):
    logWin_ = bscMethods.If_Log()
    # GeometryGroup
    linkBranch = None
    if assetPr.isAstLightLink(assetStage):
        linkBranch = assetPr.astUnitLightLinkGroupName(assetName)
    elif assetPr.isAstSolverLink(assetStage):
        linkBranch = assetPr.astUnitSolverLinkGroupName(assetName)
    if linkBranch is not None:
        if maUtils.isAppExist(linkBranch):
            # Model Preview File
            serverPreviewFile = assetPr.astUnitPreviewFile(
                lxCore_.LynxiRootIndex_Server,
                projectName, assetClass, assetName, assetVariant, assetStage
            )[1]
            backupPreviewFile = assetPr.astUnitPreviewFile(
                lxCore_.LynxiRootIndex_Backup,
                projectName, assetClass, assetName, assetVariant, assetStage
            )[1]
            # Main
            logWin_.addStartProgress(u'Preview Upload')
            #
            maFile.makeSnapshot(
                linkBranch, serverPreviewFile
            )
            lxBasic.backupOsFile(serverPreviewFile, backupPreviewFile, timeTag)
            #
            logWin_.addCompleteProgress()
