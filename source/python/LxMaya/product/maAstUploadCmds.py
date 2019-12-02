# coding=utf-8
import os
#
from LxCore import lxBasic, lxConfigure, lxProgress, lxLog, lxTip
#
from LxCore.preset import appVariant, databasePr
#
from LxCore.preset.prod import projectPr, assetPr
#
from LxCore.product.op import messageOp
#
from LxDatabase import dbBasic, dbGet
#
from LxMaya.command import maUtils, maFile, maUuid, maGeom, maShdr, maRender, maTxtr, maHier, maFur, maMshReduce, maMshBox, maScnAsb
#
from LxMaya.product.data import datAsset
#
from LxMaya.product.op import assetOp
#
from LxMaya.product import maAstLoadCmds
#
from LxMaya.database import maDbAstCmds
# Type Config
typeSet = appVariant.astBasicClassifications
typeLabel = appVariant.assetClassifyAbbDic
typeDic = appVariant.assetClassifyFullDic
# Shape Config
shapeSet = appVariant.shapeSet
shapeLabel = appVariant.shapeLabel
shapeDic = appVariant.shapeDic
# Utilities Label
astDefaultVersion = appVariant.astDefaultVersion
astDefaultVariant = appVariant.astDefaultVariant
#
isSendMail = lxConfigure.LynxiIsSendMail
isSendDingTalk = lxConfigure.LynxiIsSendDingTalk
#
none = ''


# Upload Model / Texture / Shader( Key Method )
@lxTip.viewExceptionMethod
def astUnitModelUploadMainCmd(
        logWin,
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
    # Set Log Window
    logWin.setNameText(description)
    # Log Target File
    logTarget = lxBasic.getOsFileJoinTimeTag(
        assetPr.astUnitLogFile(
            lxConfigure.LynxiRootIndex_Backup,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1],
        timeTag
    )
    logWin.setLogFile(logTarget)
    # Start
    lxLog.viewStartUploadMessage(logWin)
    #
    maUtils.setDisplayMode(5)
    maUtils.setVisiblePanelsDelete()
    # Rename Scene
    astUnitSceneRenameCmd_(
        logWin,
        assetName, assetVariant, assetStage,
        renderer
    )
    # Refresh Asset
    astUnitSceneRefreshCmd_(
        logWin,
        assetIndex, assetName, assetVariant, assetStage,
        renderer
    )
    maHier.astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage
    )
    # Upload Source File >>> 1
    astUnitUploadModelSourceSub(
        logWin,
        modelIndex,
        projectName, assetClass, assetName, assetVariant, assetStage,
        timeTag,
        description,
        notes
    )
    # Clean Scene
    astUnitSceneClearCmd(logWin)
    # Repair Model
    astUnitMeshRepairCmd_(
        logWin,
        assetName,
        repairTrans=repairTrans, repairHistory=repairHistory,
        repairUnlockNormal=repairUnlockNormal, repairSoftNormal=repairSoftNormal,
        repairUv=repairUv
    )
    # Repair Model
    astUnitShaderRepairCmd_(
        logWin,
        assetName,
        repairMatl=repairMatl, repairTexture=repairTexture, repairAov=repairAov
    )
    # Upload Index >>> 2
    dbAstUploadIndex(
        logWin,
        assetIndex,
        projectName, assetClass, assetName, assetVariant,
        withAssembly,
        timeTag
    )
    # Extra >>> 3
    astUnitUploadExtraSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Upload Material >>> 4 - 5
    astUnitModelMaterialUploadSubCmd(
        logWin,
        assetIndex, modelIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        renderer, withAov,
        timeTag
    )
    # Upload Geometry >>> 9
    astUnitUploadModelGeometrySub(
        logWin,
        assetIndex,
        modelIndex,
        assetName,
        timeTag
    )
    # Upload Asset >>> 7 - 8
    astUnitUploadModelProductSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        renderer,
        timeTag,
        withProduct=withProduct
    )
    # Upload Preview >>> 9
    astUnitModelPreviewUploadCmd(
        logWin,
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
            logWin,
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant, assetStage,
            renderer,
            withMesh=withMesh, withLod=withAssembly,
            timeTag=timeTag
        )
    # Open Source
    astUnitOpenModelSource(
        logWin,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Complete
    lxLog.viewCompleteUploadMessage(logWin)
    # Send Mail
    if isSendMail:
        messageOp.sendProductMessageByMail(
            logWin,
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
        logWin,
        assetName, assetVariant, assetStage,
        renderer
):
    lxLog.viewStartProcess(logWin, u'Rename Maya - Scene')
    # View Progress
    progressExplain = u'''Rename Maya - Scene'''
    maxValue = 2
    progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
    #
    usedObjects = []
    progressBar.updateProgress(u'''Rename Material' Node''')
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
    progressBar.updateProgress(u'''Rename AOV's Node''')
    if aovLis:
        # Rename AOV >>> 02
        maShdr.setRenameAovNodes(aovLis, assetName, assetVariant)
    #
    lxLog.viewCompleteProcess(logWin)
    #
    lxTip.viewMessage(
        u'Rename Maya Scene',
        u'Complete'
    )


#
def astUnitSceneRefreshCmd_(
        logWin,
        assetIndex,
        assetName, assetVariant, assetStage,
        renderer
):
    #
    lxLog.viewStartProcess(logWin, 'Refresh Asset')
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
    lxLog.viewCompleteProcess(logWin)


# Clean Scene
def astUnitSceneClearCmd(logWin):
    lxLog.viewStartProcess(logWin, 'Clean Maya Scene')
    # View Progress
    progressExplain = '''Clean Maya Scene'''
    maxValue = 8
    progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
    # Remove Reference >>> 01
    progressBar.updateProgress('''Clean Reference File(s)''')
    assetOp.setCleanReferenceFile()
    # Remove Reference Node >>> 02
    progressBar.updateProgress('''Clean Reference Node(s)''')
    assetOp.setCleanReferenceNode()
    # Clean Namespace >>> 03
    progressBar.updateProgress('''Clean Namespace(s)''')
    maUtils.setUnusedNamespacesClean()
    # Clean Unknown Node >>> 04
    progressBar.updateProgress('''Clean Unknown Node(s)''')
    assetOp.setUnknownNodeClear()
    # Clean Unknown Plug >>> 05
    progressBar.updateProgress('''Clean Unknown Plug(s)''')
    maUtils.setCleanUnknownPlugs()
    # Clean Display Layer >>> 06
    progressBar.updateProgress('''Clean Display Layer(s)''')
    assetOp.setDisplayLayerClear()
    # Clean Render Layer >>> 07
    progressBar.updateProgress('''Clean Render Layer(s)''')
    assetOp.setCleanRenderLayer()
    # Clean Unused Shader >>> 08
    progressBar.updateProgress('''Clean Unused Shader(s)''')
    assetOp.setUnusedShaderClear()
    #
    lxLog.viewCompleteProcess(logWin)
    #
    lxTip.viewMessage(
        u'Clean Maya Scene',
        u'Complete'
    )


#
def astUnitMeshRepairCmd_(
        logWin,
        assetName,
        repairTrans=True, repairHistory=True,
        repairUnlockNormal=True, repairSoftNormal=True,
        repairUv=True
):
    meshObjects = datAsset.getAstMeshObjects(assetName, 0)
    # Main
    lxLog.viewStartProcess(logWin, 'Repair Mesh')
    # View Progress
    progressExplain = '''Repair Mesh'''
    maxValue = 4 + [0, 3][repairTrans] + [0, 1][repairHistory] + [0, 1][repairUnlockNormal] + [0, 1][repairSoftNormal] + [0, 1][repairUv]
    progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
    # Low Quality Display >>> 01
    progressBar.updateProgress('''Set Mesh's Low Quality Display''')
    [maUtils.setObjectDisplayMode(i) for i in meshObjects]
    if repairTrans:
        # Clean Mesh's Transformations Key >>> 02
        progressBar.updateProgress('''Clean Mesh's Transformations - Keyframe''')
        maUtils.setObjectsCleanTransformKey(meshObjects)
        # Unlock Transformation >>> 03
        progressBar.updateProgress('''Unlock Mesh's Transformation''')
        maUtils.setObjectsLockTransform(meshObjects, 0)
        # Set Transformation Freeze and Rest >>> 04
        progressBar.updateProgress('''Freeze and Rest Mesh's Transformation ''')
        maUtils.setObjectsTransformationDefault(meshObjects)
    if repairUnlockNormal:
        progressBar.updateProgress('''Unlock Mesh's Normal''')
        assetOp.setMeshVertexNormalUnlockCmd(meshObjects)
    if repairSoftNormal:
        progressBar.updateProgress('''Soft ( Smooth ) Mesh's Edge''')
        assetOp.setMeshesSmoothNormal(meshObjects)
    if repairUv:
        # Clean Mesh's History >>> 06
        progressBar.updateProgress('''Repair Mesh's Uv ( Map )''')
        [maGeom.setRepairMeshMap(i) for i in meshObjects]
    if repairHistory:
        # Clean Mesh's History >>> 05
        progressBar.updateProgress('''Clean Mesh's History''')
        maUtils.setCleanHistory(meshObjects)
    # Clean Mesh's Unused Shape >>> 07
    progressBar.updateProgress('''Clean Mesh's Unused - Shape''')
    assetOp.setObjectUnusedShapeClear(meshObjects)
    # Clean Mesh's Handle >>> 08
    progressBar.updateProgress('''Clean Mesh's Handle''')
    [maUtils.hideHandel(i) for i in meshObjects]
    # Repair Mesh's Shape >>> 09
    progressBar.updateProgress('''Repair Mesh's Shape''')
    #
    lxLog.viewCompleteProcess(logWin)


#
def astUnitShaderRepairCmd_(
        logWin,
        assetName,
        repairMatl=True, repairTexture=True, repairAov=True
):
    meshObjects = datAsset.getAstMeshObjects(assetName, 0)
    # Main
    lxLog.viewStartProcess(logWin, 'Repair Shader')
    # View Progress
    progressExplain = '''Repair Shader'''
    maxValue = [0, 1][repairMatl] + [0, 2][repairTexture] + [0, 2][repairAov]
    progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
    if repairMatl is True:
        # Relink Model's Material >>> 01
        progressBar.updateProgress('''Repair Material Object - Set''')
        maShdr.setLinkObjectsMaterial(maShdr.getObjectsMaterialRelinkData(meshObjects))
        # Relink Model's Material >>> 02
        progressBar.updateProgress('''Repair Texture's Color - Space''')
        maShdr.setRefreshTextureColorSpace(maShdr.getTextureNodeLisByObject(meshObjects))
    if repairTexture is True:
        # Relink Model's Material >>> 03
        progressBar.updateProgress('''Repair Texture's Tx ( Arnold )''')
        maTxtr.setUpdateArnoldTx()
    if repairAov is True:
        # Relink Model's Material >>> 04
        progressBar.updateProgress('''Repair AOV's Driver and Filter ( Arnold )''')
        maShdr.setRepairArnoldAov()
        # Relink Model's Material >>> 05
        progressBar.updateProgress('''Repair AOV's Option ( Arnold )''')
        maShdr.setRepairAovNodesLink()


# Upload Model Source
def astUnitUploadModelSourceSub(
        logWin,
        modelIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        description, notes):
    # Source File >>> 01
    backModelFile = assetPr.astUnitSourceFile(
        lxConfigure.LynxiRootIndex_Backup,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    #
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset Model ( Source )')
    #
    linkFile = lxBasic.getOsFileJoinTimeTag(backModelFile, timeTag)
    maFile.saveMayaFile(linkFile)
    #
    dbBasic.writeDbAssetHistory(modelIndex, linkFile)
    # Update Data >>> 02
    updateData = lxConfigure.lxProductRecordDatumDic(
        linkFile,
        assetStage,
        description, notes
    )
    updateFile = lxConfigure._toLxProductRecordFile(linkFile)
    maFile.writeOsJson(updateData, updateFile, 4)
    #
    lxLog.viewCompleteProcess(logWin)


# Open Model Source
def astUnitOpenModelSource(
        logWin,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag):
    # Open Source
    backModelFile = assetPr.astUnitSourceFile(
        lxConfigure.LynxiRootIndex_Backup,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    localModelFile = assetPr.astUnitSourceFile(
        lxConfigure.LynxiRootIndex_Local,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    lxLog.viewStartProcess(logWin, u'Open Asset Model ( Source )')
    #
    backupSourceFileJoinUpdateTag = lxBasic.getOsFileJoinTimeTag(backModelFile, timeTag)
    maFile.openMayaFileToLocal(backupSourceFileJoinUpdateTag, localModelFile, timeTag)
    #
    lxLog.viewCompleteProcess(logWin)


# Model Preview File
def astUnitModelPreviewUploadCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        withProduct=False, useDefaultMaterial=1
):
    # Group Data
    astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName)
    # Model Preview File
    dbAssetPreviewFile = dbGet.getDbAstPreviewFile(assetIndex)
    # Main
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset Model ( Preview )')
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
                lxConfigure.LynxiRootIndex_Server,
                projectName, assetClass, assetName
            )[1]
            maFile.setCopyFile(dbAssetPreviewFile, serverBasicPreviewFile)
        #
        serverModelPreviewFile = assetPr.astUnitPreviewFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
        maFile.setCopyFile(dbAssetPreviewFile, serverModelPreviewFile)
    #
    lxLog.viewCompleteProcess(logWin)


# Model Mesh
def astUnitUploadModelGeometrySub(logWin, assetIndex, modelIndex, assetName, timeTag):
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
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset Model ( Geometry )')
    #
    maDbAstCmds.dbAstGeometryUploadMainCmd(assetIndex, assetName, astModelGroup, timeTag)
    #
    lxLog.viewCompleteProcess(logWin)
    # Model Mesh Constant Data >>>> 02
    dbAstUploadModelMeshConstant(assetIndex, assetName, timeTag)
    # Sub Model Mesh Constant Data >>>> 03
    dbAstUploadModelMeshConstant(modelIndex, assetName, timeTag)


#
def dbAstUploadIndex(logWin, assetIndex, projectName, assetClass, assetName, assetVariant, percentage, timeTag):
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset ( Index )')
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
    lxLog.viewCompleteProcess(logWin)


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
        logWin,
        assetIndex, modelIndex,
        projectName, assetClass, assetName, assetVariant, assetStage,
        renderer,
        withAov,
        timeTag
):
    # Collection Texture >>>> 01
    shaderObjects = datAsset.getAstMeshObjects(assetName, 1)
    # Debug ( Must Back of Rename Scene)
    modelTextureNodes = maShdr.getTextureNodeLisByObject(shaderObjects)
    #
    dbAstTextureDirectory = databasePr.dbAstTextureDirectory()
    #
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset Model( Texture )')
    #
    if modelTextureNodes:
        serverModelTextureDirectory = dbAstTextureDirectory + '/' + modelIndex
        if appVariant.isPushModelTextureToDatabase is False:
            serverModelTextureDirectory = assetPr.astUnitTextureFolder(
                lxConfigure.LynxiRootIndex_Server,
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
        astUnitBackupTexture_(
            assetIndex,
            projectName, assetClass, assetName, assetVariant, assetStage,
            modelTextureNodes, isWithTx,
            timeTag
        )
    #
    lxLog.viewCompleteProcess(logWin)
    # Material File >>>> 02
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset Model ( Material ) ')
    #
    maDbAstCmds.dbAstMaterialUploadMainCmd(shaderObjects, modelIndex, timeTag)
    if withAov is True:
        maDbAstCmds.dbAstAovUploadCmd(renderer, modelIndex, timeTag)
    #
    lxLog.viewCompleteProcess(logWin)


# Model Product File
def astUnitUploadModelProductSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        renderer,
        timeTag,
        withProduct=False
):
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset Model( Product )')
    #
    maFile.new()
    # Mesh
    maAstLoadCmds.astUnitModelGeometryLoadCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        lockTransform=False
    )
    # Material
    maAstLoadCmds.astUnitModelMaterialLoadCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        collectionTexture=False, useServerTexture=False
    )
    #
    maAstLoadCmds.astUnitLoadExtraSub(
        logWin,
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
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1]
        backupProductFile = assetPr.astUnitProductFile(
            lxConfigure.LynxiRootIndex_Backup,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        serverModelTextureDirectory = assetPr.astUnitTextureFolder(
            lxConfigure.LynxiRootIndex_Server,
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
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName
        )[1]
        if assetVariant == astDefaultVariant:
            lxBasic.writeOsJson(meshData, serverBasicMeshFile)
        #
        serverModelMeshFile = assetPr.astUnitMeshConstantFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        lxBasic.writeOsJson(meshData, serverModelMeshFile)
        #
        serverModelTextureDataFile = assetPr.astUnitTextureConstantFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        textureData = maTxtr.getTextureDatumDic(modelTextureNodes)
        #
        lxBasic.writeOsJson(textureData, serverModelTextureDataFile)
    #
    lxLog.viewCompleteProcess(logWin)


# Scenery Asset File
def astUnitUploadAssemblyProductSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        renderer,
        timeTag
):
    # Assembly Product File
    serverAssemblyProductFile = assetPr.astUnitAssemblyProductFile(
        projectName, assetName, assetVariant
    )[1]
    # Model Product File
    serverAstUnitModelProductFile = assetPr.astUnitProductFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Model
    )[1]
    # Cfx Product File
    serverAstUnitCfxProductFile = assetPr.astUnitProductFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Cfx
    )[1]
    # Main
    maFile.new()
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset Assembly ( Product )')
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
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Model
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
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Cfx
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
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Cfx
        )
        maTxtr.setCollectionMaps(serverAssemblyCfxMapDirectory)
        maTxtr.setRepathMaps(serverAssemblyCfxMapDirectory)
    # Set Texture to Tx >>> ( 05 )
    if renderer == 'Arnold':
        maTxtr.setTextureAttrToTx()
    #
    maFile.saveMayaFile(serverAssemblyProductFile)
    #
    lxLog.viewCompleteProcess(logWin)


#
def astUnitUploadAsbProxyCacheSub(
        logWin,
        projectName,
        assetClass, assetName, assetVariant,
        renderer, withLod=(50, 50)):
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
                lxConfigure.LynxiRootIndex_Server,
                projectName,
                assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Cfx
            )
            # Set Fur Cache
            maFur.setOutYetisCache(serverAstUnitAsbCfxCacheDirectory, furNodes, 1, 1, 3)
        # Proxy
        lxLog.viewStartProcess(logWin, u'Upload / Update Asset Assembly ( Proxy Cache )')
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
        lxLog.viewCompleteUploadFile(logWin)


#
def astUnitUploadAsbGpuCacheSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant,
        withLod=(50, 50), color=(.5, .5, .5)
):
    # Check is Default Variant
    if assetVariant == astDefaultVariant:
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
        lxLog.viewStartProcess(logWin, u'Upload / Update Asset Assembly ( GPU Cache )')
        #
        r, g, b = color
        maUtils.setDefaultShaderColor(r, g, b)
        #
        for meshObject in modelShaderObjects:
            renderVisible = maUtils.getAttrDatum(meshObject, lxConfigure.LynxiAttrName_Object_RenderVisible)
            transparent = maUtils.getAttrDatum(meshObject, lxConfigure.LynxiAttrName_Object_Transparent)
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
        lxLog.viewCompleteUploadFile(logWin)


#
def astUploadSceneryUnitBoxCacheSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant,
        color=(.5, .5, .5)
):
    # Check is Default Variant
    if assetVariant == astDefaultVariant:
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
        lxLog.viewStartProcess(logWin, u'Upload / Update Asset Assembly ( Box Cache )')
        #
        r, g, b = color
        maUtils.setDefaultShaderColor(r, g, b)
        maUtils.setObjectDefaultShaderCmd(modelShaderObjects)
        #
        maMshBox.setMeshesBox(astUnitModelProductGroup, boxGroup)
        maFile.gpuExport(boxGroup, serverAstUnitAsbBoxCacheFile, 0, 0)
        #
        lxLog.viewCompleteUploadFile(logWin)


#
def astUnitUploadAssemblyProxySub(
        logWin,
        projectName,
        assetClass, assetName, assetVariant,
        renderer, withLod=(50, 50)
):
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
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset Assembly ( Proxy )')
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
    lxLog.viewCompleteUploadFile(logWin)


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
        logWin,
        projectName,
        assetClass, assetName, assetVariant,
        withLod=(50, 50)
):
    # Scenery AD File
    maFile.new()
    # AD >>> 01
    serverAstUnitAsbDefinitionFile = assetPr.astUnitAssemblyDefinitionFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Assembly
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
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset Assembly ( Definition )')
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
    lxLog.viewCompleteUploadFile(logWin)


#
def astUnitUploadAssemblyMain(
        logWin,
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
        logWin,
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
            logWin,
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant,
            withLod=withLod, color=color
        )
        # Box
        astUploadSceneryUnitBoxCacheSub(
            logWin,
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant,
            color=color
        )
    # Proxy Cache >>>> 03
    astUnitUploadAsbProxyCacheSub(
        logWin,
        projectName,
        assetClass, assetName, assetVariant,
        renderer, withLod=withLod
    )
    # Proxy >>>> 04
    astUnitUploadAssemblyProxySub(
        logWin,
        projectName,
        assetClass, assetName, assetVariant,
        renderer, withLod=withLod
    )
    # AD >>>> 05
    astUnitUploadAssemblyDefinitionSub(
        logWin,
        projectName,
        assetClass, assetName, assetVariant,
        withLod=withLod
    )
    #
    maFile.new()


# Upload Rig
@lxTip.viewExceptionMethod
def astUnitUploadRigMain(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        withProduct,
        description, notes
):
    rigIndexKey = dbGet.getDbAstRigIndex(assetIndex)
    # Update Label
    timeTag = lxBasic.getOsActiveTimeTag()
    # Set Log Window
    logWin.setNameText(u'绑定上传')
    #
    maxProgress = 2
    # Log Target File
    logTarget = lxBasic.getOsFileJoinTimeTag(
        assetPr.astUnitLogFile(
            lxConfigure.LynxiRootIndex_Backup,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1],
        timeTag
    )
    logWin.setMaxProgressValue(maxProgress)
    logWin.setLogFile(logTarget)
    # Start
    lxLog.viewStartUploadMessage(logWin)
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
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        description, notes)
    # Clean Scene
    astUnitSceneClearCmd(logWin)
    # TD Command
    tdCommand = assetPr.getAstTdUploadCommand(projectName, lxConfigure.LynxiProduct_Asset_Link_Rig)
    if tdCommand:
        maUtils.runMelCommand(tdCommand)
    # Extra >>> 2
    astUnitUploadExtraSub(
        logWin,
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
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetStage, assetVariant,
        timeTag,
        withProduct=withProduct
    )
    # Open Source
    astUnitOpenSource(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Complete
    lxLog.viewCompleteUploadMessage(logWin)
    # Send Mail
    if isSendMail:
        messageOp.sendProductMessageByMail(
            logWin,
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
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetStage, assetVariant,
        timeTag,
        withProduct=False
):
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset Rig ( Product )')
    #
    serverRigProductFile = assetPr.astUnitProductFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Rig
    )[1]
    backupRigProductFile = assetPr.astUnitProductFile(
        lxConfigure.LynxiRootIndex_Backup,
        projectName,
        assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Rig
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
        lxConfigure.LynxiRootIndex_Server,
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
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        meshData = datAsset.getAstMeshConstantData(assetName)
        #
        maFile.writeOsJson(meshData, serverMeshConstantFile, 4)
    #
    lxLog.viewCompleteProcess(logWin)


@lxTip.viewExceptionMethod
def astUnitCfxUploadMainCmd(
        logWin,
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
    # Set Log Window
    logWin.setNameText(u'毛发上传')
    #
    maxProgress = 1 + 3 + 2
    # Log Target File
    logTarget = lxBasic.getOsFileJoinTimeTag(
        assetPr.astUnitLogFile(
            lxConfigure.LynxiRootIndex_Backup,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1],
        timeTag
    )
    logWin.setMaxProgressValue(maxProgress)
    logWin.setLogFile(logTarget)
    # Start
    lxLog.viewStartUploadMessage(logWin)
    # Switch Display Mode
    maUtils.setDisplayMode(5)
    maUtils.setVisiblePanelsDelete()
    # Rename Scene
    astUnitSceneRenameCmd_(
        logWin,
        assetName, assetVariant, assetStage,
        renderer
    )
    # Refresh Asset
    astUnitSceneRefreshCmd_(
        logWin,
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
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        description, notes
    )
    # Clean Scene >>> 02
    astUnitSceneClearCmd(logWin)
    # CFX Mesh Constant Data
    dbAstUploadModelMeshConstant(
        assetSubIndex,
        assetName,
        timeTag
    )
    # Upload Material >>> 04 - 05
    astUnitCfxMaterialUploadSubCmd(
        logWin,
        assetIndex, assetSubIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        renderer,
        withAov,
        timeTag
    )
    # Upload Node >>> 09 - 10 - 11
    astUnitUploadCfxFurSub(
        logWin,
        assetIndex, assetSubIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Upload Asset >>> 12
    astUnitUploadCfxProduct(
        logWin,
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
            logWin,
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant, assetStage,
            renderer,
            withMesh=False,
            withLod=False,
            timeTag=timeTag
        )
    # Open Source
    astUnitOpenSource(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Complete
    lxLog.viewCompleteUploadMessage(logWin)
    # Send Mail
    if isSendMail:
        messageOp.sendProductMessageByMail(
            logWin,
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


# Upload CFX Node
def astUnitUploadCfxFurSub(
        logWin,
        assetIndex, assetSubIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag):
    rootGroup = assetPr.astUnitRootGroupName(assetName)
    cfxAssetRoot = assetPr.astUnitCfxLinkGroupName(assetName)
    cfxSet = assetPr.cfxSetName(assetName)
    yetiObjects = datAsset.getYetiObjects(assetName)
    nurbsHairObjects = datAsset.getAstCfxNurbsHairObjects(assetName)
    # Assign Default Shader
    assetOp.setDefaultShader(logWin, cfxAssetRoot)
    #
    assetOp.setObjectDefaultShaderCmd(logWin, yetiObjects)
    assetOp.setObjectDefaultShaderCmd(logWin, nurbsHairObjects)
    # Set
    maFur.setYetisGuideSet(yetiObjects, cfxSet)
    # Parent to World
    maUtils.setParentToWorld(cfxAssetRoot)
    maUtils.setNodeDelete(rootGroup)
    # Export File
    serverAstUnitFurFile = assetPr.astUnitFurFile(
        lxConfigure.LynxiRootIndex_Server,
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
    # Node
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
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset CFX ( Fur Map )')
    if furObjects:
        serverMapFolder = dbCfxMapDirectory + '/' + assetSubIndex
        if appVariant.isPushCfxMapToDatabase is False:
            serverMapFolder = assetPr.astUnitMapFolder(
                lxConfigure.LynxiRootIndex_Server,
                projectName,
                assetClass, assetName, assetVariant, assetStage
            )
        # Collection
        maTxtr.setCollectionMaps(serverMapFolder, furObjects)
        # Repath Map
        maTxtr.setRepathMaps(serverMapFolder, furObjects)
    #
    lxLog.viewCompleteProcess(logWin)
    # Progress >>> 02
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset CFX ( Fur )')
    #
    maUtils.setAttrStringDatumForce(cfxAssetRoot, appVariant.basicVariantAttrLabel, assetVariant)
    # Production
    maDbAstCmds.dbAstUploadFurProduct(assetIndex, assetVariant)
    # HisTory
    maDbAstCmds.dbAstUploadFurMain(furObjects, assetSubIndex, timeTag)
    # Solver
    astUnitUploadCfxFurForSolver_(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    #
    lxLog.viewCompleteProcess(logWin)


#
def astUnitUploadCfxFurForSolver_(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag):
    #
    assetSubIndex = dbBasic.getDatabaseSubIndex(
        assetIndex,
        [assetPr.getAssetLink(assetStage), assetVariant]
    )
    lxLog.viewStartSubProcess(logWin, u'Upload / Update Asset CFX ( Fur Cache )')
    # NurbsHair
    nurbsHairObjects = datAsset.getAstCfxNurbsHairObjects(assetName)
    #
    lxLog.viewCompleteProcess(logWin)
    #
    maDbAstCmds.dbAstUploadNurbsHairMain(nurbsHairObjects, assetSubIndex, timeTag)


#
def astUnitCfxMaterialUploadSubCmd(
        logWin,
        assetIndex, assetSubIndex,
        projectName, assetClass, assetName, assetVariant, assetStage,
        renderer,
        withAov,
        timeTag
):
    # Collection Texture >>>> 01
    dbAstTextureDirectory = databasePr.dbAstTextureDirectory()
    #
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset CFX ( Texture )')
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
                lxConfigure.LynxiRootIndex_Server,
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
        astUnitBackupTexture_(
            assetIndex,
            projectName,
            assetClass, assetName, assetVariant, assetStage,
            textureNodeLis, isWithTx,
            timeTag
        )
    #
    lxLog.viewCompleteProcess(logWin)
    # Material File >>>> 02
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset CFX ( Material )')
    #
    maDbAstCmds.dbAstMaterialUploadMainCmd(shaderFurNodes, assetSubIndex, timeTag)
    if withAov is True:
        maDbAstCmds.dbAstAovUploadCmd(renderer, assetSubIndex, timeTag)
    #
    lxLog.viewCompleteProcess(logWin)


# Upload CFX Product
def astUnitUploadCfxProduct(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        renderer,
        withProduct=False
):
    # New Scene
    maFile.new()
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset CFX ( Product )')
    # Fur
    maAstLoadCmds.astUnitCfxFurLoadCmd(
        logWin,
        projectName,
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        collectionMap=False, useServerMap=False
    )
    # Material
    maAstLoadCmds.astUnitLoadCfxMaterialSub(
        logWin,
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
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1]
        backupCfxProductFile = assetPr.astUnitProductFile(
            lxConfigure.LynxiRootIndex_Backup,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        serverCfxTextureDirectory = assetPr.astUnitTextureFolder(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )
        serverCfxMapDirectory = assetPr.astUnitMapFolder(
            lxConfigure.LynxiRootIndex_Server,
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
    lxLog.viewCompleteProcess(logWin)


@lxTip.viewExceptionMethod
def astUnitUploadMain(
        logWin,
        assetIndex, projectName, assetClass, assetName, assetVariant, assetStage,
        withProduct=True, description=None, notes=None
):
    timeTag = lxBasic.getOsActiveTimeTag()
    # Set Log Window
    logWin.setNameText(description)
    #
    maxProgress = 4
    logWin.setMaxProgressValue(maxProgress)
    # Start
    lxLog.viewStartUploadMessage(logWin)
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
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        description, notes
    )
    # Clean Scene
    astUnitSceneClearCmd(logWin)
    # Extra >>> 02
    astUnitUploadExtraSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Remove Reference
    astUnitRemoveReferenceSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Product >>> 03
    astUnitUploadProductSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Preview >>> 04
    astUnitUploadPreviewSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Open Source
    astUnitOpenSource(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag
    )
    # Complete
    lxLog.viewCompleteUploadMessage(logWin)
    # Send Mail
    if isSendMail:
        messageOp.sendProductMessageByMail(
            logWin,
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
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag,
        description, notes):
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
        lxConfigure.LynxiRootIndex_Backup,
        projectName, assetClass, assetName, assetVariant, assetStage
    )[1]
    lxLog.viewStartProcess(logWin, u'Upload / Update Asset {} ( Source )'.format(assetPr.getAssetLink(assetStage)))
    #
    linkFile = lxBasic.getOsFileJoinTimeTag(backupSourceFile, timeTag)
    #
    maFile.saveMayaFile(linkFile)
    # Database History
    dbBasic.writeDbAssetHistory(assetSubIndex, linkFile)
    # Update
    updateData = lxConfigure.lxProductRecordDatumDic(
        linkFile,
        assetStage,
        description, notes
    )
    updateFile = lxConfigure._toLxProductRecordFile(linkFile)
    lxBasic.writeOsJson(updateData, updateFile, 4)
    #
    lxLog.viewCompleteProcess(logWin)


#
def astUnitOpenSource(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag):
    # Open Source
    backupSourceFile = assetPr.astUnitSourceFile(
        lxConfigure.LynxiRootIndex_Backup,
        projectName, assetClass, assetName, assetVariant, assetStage
    )[1]
    localSourceFile = assetPr.astUnitSourceFile(
        lxConfigure.LynxiRootIndex_Local,
        projectName, assetClass, assetName, assetVariant, assetStage
    )[1]
    lxLog.viewStartProcess(logWin, u'Open Asset %s ( Source )' % assetStage.capitalize())
    #
    backupSourceFileJoinUpdateTag = lxBasic.getOsFileJoinTimeTag(backupSourceFile, timeTag)
    maFile.openMayaFileToLocal(backupSourceFileJoinUpdateTag, localSourceFile, timeTag)
    #
    lxLog.viewCompleteProcess(logWin)


#
def astUnitBackupTexture_(
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        textureNodes,
        isWithTx,
        timeTag):
    backupTextureFolder = assetPr.astUnitTextureFolder(
        lxConfigure.LynxiRootIndex_Backup,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )
    serverTextureIndexFile = assetPr.astUnitTextureIndexFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    backupTextureIndexFile = assetPr.astUnitTextureIndexFile(
        lxConfigure.LynxiRootIndex_Backup,
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
def astUnitUploadTexture_(
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        textureNodes,
        isWithTx):
    if textureNodes:
        serverTextureFolder = assetPr.astUnitTextureFolder(
            lxConfigure.LynxiRootIndex_Server,
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
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag):
    referBranchLis = []
    if assetPr.isAstSolverLink(assetStage):
        modelBranch = assetPr.astUnitModelLinkGroupName(assetName)
        referBranchLis.append(modelBranch)
        #
        serverMeshConstantFile = assetPr.astUnitMeshConstantFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
        backupMeshConstantFile = assetPr.astUnitMeshConstantFile(
            lxConfigure.LynxiRootIndex_Backup,
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
            lxConfigure.LynxiRootIndex_Server,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
        backupMeshConstantFile = assetPr.astUnitMeshConstantFile(
            lxConfigure.LynxiRootIndex_Backup,
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
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag):
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
                lxConfigure.LynxiRootIndex_Server,
                projectName, assetClass, assetName, assetVariant, assetStage
            )[1]
            backupProductFile = assetPr.astUnitProductFile(
                lxConfigure.LynxiRootIndex_Backup,
                projectName, assetClass, assetName, assetVariant, assetStage
            )[1]
            #
            lxLog.viewStartProcess(logWin, u'Upload / Update Asset %s ( Product )' % assetStage.capitalize())
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
                logWin,
                assetIndex,
                projectName,
                assetClass, assetName, assetVariant, assetStage,
                timeTag
            )
            # Upload Cache
            maAstLoadCmds.astUnitLoadCacheSub(
                logWin,
                assetIndex,
                projectName,
                assetClass, assetName, assetVariant, assetStage,
                collectionCache=False, useServerTexture=True
            )
            #
            maFile.saveMayaFile(serverProductFile)
            maFile.backupFile(serverProductFile, backupProductFile, timeTag)
            #
            lxLog.viewCompleteProcess(logWin)


#
def astUnitUploadTextureSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag):
    linkBranch = None
    isWithTx = False
    if assetPr.isAstLightLink(assetStage):
        linkBranch = assetPr.astUnitLightLinkGroupName(assetName)
        isWithTx = True
    if linkBranch is not None:
        if maUtils.isAppExist(linkBranch):
            shaderObjects = maUtils.getChildrenByRoot(linkBranch)
            lxLog.viewStartProcess(logWin, u'Load Asset %s ( Texture )' % lxBasic._toStringPrettify(assetStage))
            #
            if shaderObjects:
                textureNodes = maShdr.getTextureNodeLisByObject(shaderObjects)
                if textureNodes:
                    # Backup
                    astUnitBackupTexture_(
                        assetIndex,
                        projectName,
                        assetClass, assetName, assetVariant, assetStage,
                        textureNodes,
                        isWithTx,
                        timeTag
                    )
                    # Upload
                    astUnitUploadTexture_(
                        projectName,
                        assetClass, assetName, assetVariant, assetStage,
                        textureNodes,
                        isWithTx
                    )
                else:
                    lxLog.viewWarning(
                        logWin,
                        u'Texture - Node is Non - Exists'
                    )
            else:
                lxLog.viewWarning(
                    logWin,
                    u'Shader - Object is Non - Exists'
                )
            #
            lxLog.viewCompleteProcess(logWin)


#
def astUnitUploadGeometrySub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag):
    pass


#
def astUnitUploadExtraSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag):
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
            lxConfigure.LynxiRootIndex_Server,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
        backupExtraFile = assetPr.astUnitExtraFile(
            lxConfigure.LynxiRootIndex_Backup,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        lxLog.viewStartProcess(logWin, u'Upload / Update Asset %s ( Extra ) ' % assetStage.capitalize())
        #
        lxBasic.writeOsJsonDic(extraData, serverExtraFile, 4)
        lxBasic.backupOsFile(serverExtraFile, backupExtraFile, timeTag)
        #
        lxLog.viewCompleteProcess(logWin)


#
def astUnitUploadPreviewSub(
        logWin,
        assetIndex,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        timeTag):
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
                lxConfigure.LynxiRootIndex_Server,
                projectName, assetClass, assetName, assetVariant, assetStage
            )[1]
            backupPreviewFile = assetPr.astUnitPreviewFile(
                lxConfigure.LynxiRootIndex_Backup,
                projectName, assetClass, assetName, assetVariant, assetStage
            )[1]
            # Main
            lxLog.viewStartProcess(logWin, u'Upload / Update Asset %s ( Preview ) ' % assetStage.capitalize())
            #
            maFile.makeSnapshot(
                linkBranch, serverPreviewFile
            )
            lxBasic.backupOsFile(serverPreviewFile, backupPreviewFile, timeTag)
            #
            lxLog.viewCompleteProcess(logWin)