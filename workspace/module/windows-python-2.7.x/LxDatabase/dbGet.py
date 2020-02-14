# coding:utf-8
from LxBasic import bscConfigure, bscCore, bscMethods, bscObjects

from LxCore import lxConfigure
#
from LxCore.config import assetCfg

from LxPreset import prsVariants, prsMethods
#
from LxCore.preset.prod import assetPr, scenePr
#
from LxDatabase import dbBasic
# Type Config
astBasicClassifications = prsVariants.Util.astBasicClassifications
astBasicPriorities = prsVariants.Util.astBasicPriorities
astSceneryClass = prsVariants.Util.astSceneryClass
#
astDefaultVariant = prsVariants.Util.astDefaultVersion
#
Ma_Separator_Node = bscConfigure.Ma_Separator_Node
Ma_Separator_Namespace = bscConfigure.Ma_Separator_Namespace
#
none = ''


#
def getDbGzFile(assetIndex, directory):
    string = none
    if assetIndex:
        string = directory + '/' + assetIndex
    return string


#
def isDbExistsGzFile(assetIndex, directory):
    boolean = False
    if assetIndex:
        fileString_ = getDbGzFile(assetIndex, directory)
        boolean = bscMethods.OsFile.isExist(fileString_)
    return boolean


#
def getDbProductFile(assetIndex, directory):
    string = directory + '/' + assetIndex
    return string


#
def getExistsDbIntegrationFile(assetIndex, directory):
    boolean = False
    if assetIndex:
        fileString_ = getDbProductFile(assetIndex, directory)
        boolean = bscMethods.OsFile.isExist(fileString_)
    return boolean


#
def getDbCompFile(assetIndex, scCompIndex, directory):
    databaseSubIndex = dbBasic.getDatabaseSubIndex(assetIndex, scCompIndex)
    string = directory + '/' + databaseSubIndex
    return string


#
def getExistsDbCompFile(assetIndex, scCompIndex, directory):
    boolean = False
    if assetIndex and scCompIndex:
        fileString_ = getDbCompFile(assetIndex, scCompIndex, directory)
        boolean = bscMethods.OsFile.isExist(fileString_)
    return boolean


#
def getExistsDbAsset(assetIndex):
    directory = prsVariants.Database.assetNameIndex
    return isDbExistsGzFile(assetIndex, directory)


#
def getDbAssetIndex(projectName, assetName):
    # Lis [ <Name> ]
    string = none
    directory = prsVariants.Database.assetNameIndex
    if projectName and assetName:
        assetIndex = bscMethods.UniqueId.getByStrings(projectName, assetName)
        if isDbExistsGzFile(assetIndex, directory):
            string = assetIndex
    return string


#
def getDbAssetLinkIndex(assetIndex, assetVariant, assetStage, version=None):
    assetLinkIndex = assetIndex
    if prsMethods.Asset.isModelStageName(assetStage) or prsMethods.Asset.isGroomStageName(assetStage) or prsMethods.Asset.isSolverStageName(assetStage):
        assetLinkIndex = dbBasic.getDatabaseSubIndex(assetIndex, [lxConfigure.VAR_product_asset_link_model, assetVariant])
    elif prsMethods.Asset.isRigStageName(assetStage):
        assetLinkIndex = dbBasic.getDatabaseSubIndex(assetIndex, [lxConfigure.VAR_product_asset_link_rig, version])
    #
    return assetLinkIndex


#
def getDbAstModelIndex(assetIndex, assetVariant):
    string = none
    if assetIndex:
        data = dbBasic.getDatabaseSubIndex(assetIndex, [lxConfigure.VAR_product_asset_link_model, assetVariant])
        if data:
            string = data
    return string


#
def getDbAstRigIndex(assetIndex, version='anim'):
    string = none
    if assetIndex:
        data = dbBasic.getDatabaseSubIndex(assetIndex, [lxConfigure.VAR_product_asset_link_rig, version])
        if data:
            string = data
    return string


#
def getDbCfxIndex(assetIndex, assetVariant):
    string = none
    if assetIndex:
        data = dbBasic.getDatabaseSubIndex(assetIndex, [lxConfigure.VAR_product_asset_link_groom, assetVariant])
        if data:
            string = data
    return string


#
def getDbAstSolverIndex(assetIndex, assetVariant):
    string = none
    if assetIndex:
        data = dbBasic.getDatabaseSubIndex(assetIndex, [lxConfigure.VAR_product_asset_link_solver, assetVariant])
        if data:
            string = data
    return string


#
def getDbSceneryUnitIndex(assetIndex, assetVariant):
    string = none
    if assetIndex:
        data = dbBasic.getDatabaseSubIndex(assetIndex, ['sceneryUnit', assetVariant])
        if data:
            string = data
    return string


#
def getDbAssetClass(assetIndex):
    return assetPr.getAssetClass(assetIndex)


#
def getDbAssetTag(assetIndex):
    string = astBasicPriorities[0]
    if assetIndex:
        directory = prsVariants.Database.assetFilterIndex
        data = dbBasic.dbCompDatumRead(assetIndex, directory)
        if data:
            value = data['tag']
            if value:
                string = value
    return string


#
def getDbAssetName(assetIndex, projectName=none):
    string = none
    if assetIndex:
        directory = prsVariants.Database.assetNameIndex
        data = dbBasic.dbCompDatumRead(assetIndex, directory)
        if data:
            if projectName in data:
                string = data[projectName]
    return string


#
def getDbAssetVariants(assetIndex):
    # LIST [ <Variant> ]
    lis = []
    if assetIndex:
        directory = prsVariants.Database.assetVariantIndex
        data = dbBasic.dbCompDatumRead(assetIndex, directory)
        if data:
            lis = data
    return lis


#
def getDbAssemblyPercentage(assetIndex):
    # LIST [ <LOD01 Percentage>, <LOD02 Percentage> ]
    lis = []
    if assetIndex:
        directory = prsVariants.Database.assetAssemblyIndex
        data = dbBasic.dbCompDatumRead(assetIndex, directory)
        if data:
            lis = data['percentage']
    return lis


#
def dbAssetPreviewFile(assetIndex, assetLink, assetVariant, extLabel=prsVariants.Util.jpgExt):
    if assetIndex:
        directory = prsVariants.Database.assetPreview
        string = directory + '/' + assetIndex + extLabel
        if assetVariant:
            subIndex = dbBasic.getDatabaseSubIndex(assetIndex, [assetLink, assetVariant])
            string = directory + '/' + subIndex + extLabel
    else:
        string = none
    return string


#
def dbAstViewportPreviewFile(assetIndex):
    string = none
    if assetIndex:
        directory = prsVariants.Database.assetPreview
        fileString_ = directory + '/' + assetIndex + prsVariants.Util.jpgExt
        if bscMethods.OsFile.isExist(fileString_):
            string = fileString_
    return string


#
def dbAstRenderPreviewFile(assetIndex, assetVariant):
    string = none
    if assetIndex:
        directory = prsVariants.Database.assetPreview
        assetSubIndex = dbBasic.getDatabaseSubIndex(assetIndex, [lxConfigure.VAR_product_asset_link_model, assetVariant])
        fileString_ = directory + '/' + assetSubIndex + prsVariants.Util.pngExt
        if bscMethods.OsFile.isExist(fileString_):
            string = fileString_
    return string


#
def getDbAstPreviewFile(assetIndex, assetVariant=none):
    string = none
    if assetIndex:
        directory = prsVariants.Database.assetPreview
        string = directory + '/' + assetIndex + prsVariants.Util.jpgExt
        if assetVariant:
            dbModelIndex = getDbAstModelIndex(assetIndex, assetVariant)
            renderPrv = directory + '/' + dbModelIndex + prsVariants.Util.pngExt
            texturePrv = directory + '/' + dbModelIndex + prsVariants.Util.jpgExt
            if bscMethods.OsFile.isExist(renderPrv):
                string = renderPrv
            elif bscMethods.OsFile.isExist(texturePrv):
                string = texturePrv
    return string


#
def getDbSceneryUnitPreviewFile(assetIndex, assetVariant=none):
    string = none
    if assetIndex:
        directory = prsVariants.Database.sceneryPreview
        string = directory + '/' + assetIndex + prsVariants.Util.jpgExt
        if assetVariant:
            dbModelIndex = getDbSceneryUnitIndex(assetIndex, assetVariant)
            renderPrv = directory + '/' + dbModelIndex + prsVariants.Util.pngExt
            texturePrv = directory + '/' + dbModelIndex + prsVariants.Util.jpgExt
            if bscMethods.OsFile.isExist(renderPrv):
                string = renderPrv
            elif bscMethods.OsFile.isExist(texturePrv):
                string = texturePrv
    return string


#
def getDbAstGeometryFile(assetIndex):
    directory = prsVariants.Database.assetGeometryIndex
    return getDbGzFile(assetIndex, directory)


#
def isDbAstExistsGeometry(assetIndex):
    directory = prsVariants.Database.assetGeometryIndex
    return isDbExistsGzFile(assetIndex, directory)


#
def getDbAstMaterialFile(dbSubIndex):
    directory = prsVariants.Database.assetMaterialIndex
    return getDbGzFile(dbSubIndex, directory)


#
def isDbAstMaterialExists(dbSubIndex):
    directory = prsVariants.Database.assetMaterialIndex
    return isDbExistsGzFile(dbSubIndex, directory)


#
def getDbExistsAstModelMaterial(assetIndex, assetVariant):
    dbModelIndex = getDbAstModelIndex(assetIndex, assetVariant)
    return isDbAstMaterialExists(dbModelIndex)


#
def getExistsDbCfxMaterial(assetIndex, assetVariant):
    dbCfxIndex = getDbCfxIndex(assetIndex, assetVariant)
    return isDbAstMaterialExists(dbCfxIndex)


#
def getExistsDbAssembly(assetIndex):
    directory = prsVariants.Database.assetAssemblyIndex
    return isDbExistsGzFile(assetIndex, directory)


#
def getDbAstUpdate(assetIndex, assetVariant, assetStage):
    string = prsVariants.Util.infoNonExistsLabel
    if assetIndex:
        assetLink = prsMethods.Asset.stageName2linkName(assetStage)
        assetSubIndex = dbBasic.getDatabaseSubIndex(assetIndex, [assetLink, assetVariant])
        timestamp = dbBasic.readDbAssetHistory(assetSubIndex, prsVariants.Util.infoUpdateLabel)
        if timestamp:
            string = bscMethods.OsTimestamp.toChnPrettify(timestamp)
    return string


#
def getDbAstUpdater(assetIndex, assetVariant, assetStage):
    string = prsVariants.Util.infoNonExistsLabel
    if assetIndex:
        assetLink = prsMethods.Asset.stageName2linkName(assetStage)
        if prsMethods.Asset.isRigStageName(assetStage):
            assetSubIndex = getDbAstRigIndex(assetIndex)
        else:
            assetSubIndex = dbBasic.getDatabaseSubIndex(assetIndex, [assetLink, assetVariant])
        osUser = dbBasic.readDbAssetHistory(assetSubIndex, prsVariants.Util.infoUpdaterLabel)
        if osUser:
            string = prsMethods.Personnel.userChnname(osUser)
    return string


#
def getDbModelUpdate(assetIndex, assetVariant):
    string = prsVariants.Util.infoNonExistsLabel
    if assetIndex:
        # Mesh
        dbModelIndex = getDbAstModelIndex(assetIndex, assetVariant)
        dbGeometryFile = getDbAstGeometryFile(assetIndex)
        if bscMethods.OsFile.isExist(dbGeometryFile):
            dbMeshTimeStamp = bscMethods.OsFile.mtimestamp(dbGeometryFile)
            # Material
            dbMaterialFile = getDbAstMaterialFile(dbModelIndex)
            timestamp = dbMeshTimeStamp
            if bscMethods.OsFile.isExist(dbMaterialFile):
                dbMaterialTimeStamp = bscMethods.OsFile.mtimestamp(dbMaterialFile)
                timestamp = max([dbMeshTimeStamp, dbMaterialTimeStamp])
            #
            string = bscMethods.OsTimestamp.toChnPrettify(timestamp)
    return string


#
def getDbModelUpdater(assetIndex, assetVariant):
    string = prsVariants.Util.infoNonExistsLabel
    if assetIndex:
        # Mesh
        dbModelIndex = getDbAstModelIndex(assetIndex, assetVariant)
        data = dbBasic.readDbAssetHistory(dbModelIndex, prsVariants.Util.infoUpdaterLabel)
        if data:
            string = data
    return string


#
def getDbModelStage(assetIndex, assetVariant):
    string = lxConfigure.LynxiAstModelStages[0]
    isExistsDbMesh = isDbAstExistsGeometry(assetIndex)
    if isExistsDbMesh:
        string = lxConfigure.LynxiAstModelStages[0]
        dbModelIndex = getDbAstModelIndex(assetIndex, assetVariant)
        isExistsDbMaterial = isDbAstMaterialExists(dbModelIndex)
        if isExistsDbMaterial:
            string = lxConfigure.LynxiAstModelStages[1]
    return string


#
def getDbGeometryObjectsIndexDic(assetIndex):
    dic = bscCore.orderedDict()
    if assetIndex:
        directory = prsVariants.Database.assetGeometryIndex
        data = dbBasic.dbCompDatumRead(assetIndex, directory)
        if data:
            dic = data
    return dic


#
def getDbGeometryObjectsInfoDic(assetIndex, dbName, namespace, searchRoot):
    dic = bscCore.orderedDict()
    if assetIndex:
        directory = prsVariants.Database.assetGeometryIndex
        data = dbBasic.dbCompDatumRead(assetIndex, directory)
        if data:
            for objectIndex, info in data.items():
                meshPath = getDbGeometryObjectPath(assetIndex, dbName, objectIndex)
                if searchRoot in meshPath:
                    key = [none, namespace + Ma_Separator_Namespace][namespace is not none] + bscMethods.MayaPath.name(meshPath)
                    dic[key] = info
    return dic


#
def getDbGeometryObjectPath(assetIndex, dbName, objectIndex):
    string = none
    if assetIndex:
        directory = prsVariants.Database.assetGeometryTransform
        dbCompIndex = dbBasic.getDatabaseCompIndex(assetIndex, objectIndex)
        data = dbBasic.dbCompDatumRead(dbCompIndex, directory)
        if data:
            parentPath, nodeName = data[:2]
            if parentPath.startswith('|'):
                parentPath = parentPath[1:]
            #
            string = parentPath + Ma_Separator_Node + nodeName
            string = string.replace('<assetName>', dbName)
    return string


#
def getDbAstGeometryUnitTransform(assetIndex, objectIndex):
    tup = ()
    if assetIndex:
        directory = prsVariants.Database.assetGeometryTransform
        dbCompIndex = dbBasic.getDatabaseCompIndex(assetIndex, objectIndex)
        data = dbBasic.dbCompDatumRead(dbCompIndex, directory)
        if data:
            tup = data
    return tup


#
def getDbGeometryUnitsPathDic(assetIndex):
    dic = bscCore.orderedDict()
    dbName = assetPr.getAssetName(assetIndex)
    objectIndexes = getDbGeometryObjectsIndexDic(assetIndex)
    if objectIndexes:
        for objectIndex in objectIndexes:
            path = getDbGeometryObjectPath(assetIndex, dbName, objectIndex)
            dic[objectIndex] = path
    return dic


#
def getDbGeometryObjectsAttributeDic(assetIndex, objectIndex):
    lis = []
    if assetIndex:
        directory = prsVariants.Database.assetMaterialAttribute
        dbCompIndex = dbBasic.getDatabaseCompIndex(assetIndex, objectIndex)
        data = dbBasic.dbCompDatumRead(dbCompIndex, directory)
        if data:
            lis = data
    return lis


#
def getDbGeometryObjectsObjSetDic(assetIndex, objectIndex):
    lis = []
    if assetIndex:
        directory = prsVariants.Database.assetMaterialObjectSet
        dbCompIndex = dbBasic.getDatabaseCompIndex(assetIndex, objectIndex)
        data = dbBasic.dbCompDatumRead(dbCompIndex, directory)
        if data:
            lis = data
    return lis


#
def getDbCompFurIndexData(dbSubIndex):
    dic = {}
    directory = prsVariants.Database.assetFurIndex
    data = dbBasic.dbCompDatumRead(dbSubIndex, directory)
    if data:
        dic = data
    return dic


#
def getDbCompNurbsHairIndexData(dbSubIndex):
    dic = {}
    directory = prsVariants.Database.assetGraphIndex
    data = dbBasic.dbCompDatumRead(dbSubIndex, directory)
    if data:
        dic = data
    return dic


#
def getDbMaterialIndexData(dbSubIndex):
    dic = {}
    if dbSubIndex:
        directory = prsVariants.Database.assetMaterialIndex
        data = dbBasic.dbCompDatumRead(dbSubIndex, directory)
        if data:
            dic = data
    return dic


#
def getDbAovIndexData(dbSubIndex):
    dic = {}
    if dbSubIndex:
        directory = prsVariants.Database.assetAovIndex
        data = dbBasic.dbCompDatumRead(dbSubIndex, directory)
        if data:
            dic = data
    return dic


#
def getNonExistsDbMeshCompIndex(assetIndex, objectIndexes):
    lis = []
    dbCompIndexes = getDbGeometryObjectsIndexDic(assetIndex)
    if objectIndexes:
        for objectIndex in objectIndexes:
            isExists = objectIndex in dbCompIndexes.keys()
            if not isExists:
                lis.append(objectIndex)
    return lis


#
def getNonExistsDbFurCompIndex(dbSubIndex, objectIndexes):
    lis = []
    dbCompIndexes = getDbCompFurIndexData(dbSubIndex)
    if objectIndexes:
        for objectIndex in objectIndexes:
            isExists = objectIndex in dbCompIndexes.keys()
            if not isExists:
                lis.append(objectIndex)
    return lis


#
def getNonExistsDbMaterialComp(dbSubIndex, objectIndexes):
    lis = []
    dbMaterialCompIndexes = getDbMaterialIndexData(dbSubIndex)
    if objectIndexes:
        for objectIndex in objectIndexes:
            isExists = objectIndex in dbMaterialCompIndexes.keys()
            if not isExists:
                lis.append(objectIndex)
    return lis


#
def getNonExistsDbAovComp(dbSubIndex, objectIndexes):
    lis = []
    dbMaterialCompIndexes = getDbAovIndexData(dbSubIndex)
    if objectIndexes:
        for objectIndex in objectIndexes:
            isExists = objectIndex in dbMaterialCompIndexes.keys()
            if not isExists:
                lis.append(objectIndex)
    return lis


#
def getAstUnitDbAssemblyUpdate(projectName, assetCategory, assetName, assetVariant):
    serverAstUnitAsbDefinitionFile = assetPr.astUnitAssemblyDefinitionFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetCategory, assetName, assetVariant, lxConfigure.VAR_product_asset_link_assembly
    )[1]
    return bscMethods.OsFile.mtimeChnPrettify(serverAstUnitAsbDefinitionFile)


#
def getDbFurFile(dbSubIndex):
    directory = prsVariants.Database.assetFurProduct
    return getDbProductFile(dbSubIndex, directory)


#
def getExistsDbFur(assetIndex, assetVariant):
    directory = prsVariants.Database.assetFurProduct
    dbCfxIndex = getDbCfxIndex(assetIndex, assetVariant)
    return getExistsDbIntegrationFile(dbCfxIndex, directory)


#
def getDbCfxUpdate(assetIndex, assetVariant):
    string = prsVariants.Util.infoNonExistsLabel
    if assetIndex:
        # Mesh
        dbCfxIndex = getDbCfxIndex(assetIndex, assetVariant)
        dbFurFile = getDbFurFile(dbCfxIndex)
        if bscMethods.OsFile.isExist(dbFurFile):
            dbFurTimeStamp = bscMethods.OsFile.mtimestamp(dbFurFile)
            # Material
            dbMaterialFile = getDbAstMaterialFile(dbCfxIndex)
            #
            timestamp = dbFurTimeStamp
            if bscMethods.OsFile.isExist(dbMaterialFile):
                dbMaterialTimeStamp = bscMethods.OsFile.mtimestamp(dbMaterialFile)
                timestamp = max([dbFurTimeStamp, dbMaterialTimeStamp])
            #
            string = bscMethods.OsTimestamp.toChnPrettify(timestamp)
    return string


#
def getDbCfxUpdater(assetIndex, assetVariant):
    string = prsVariants.Util.infoNonExistsLabel
    if assetIndex:
        # Mesh
        dbCfxIndex = getDbCfxIndex(assetIndex, assetVariant)
        data = dbBasic.readDbAssetHistory(dbCfxIndex, prsVariants.Util.infoUpdaterLabel)
        if data:
            string = data
    return string


#
def getDbCfxStage(assetIndex, assetVariant):
    string = lxConfigure.LynxiAstCfxStages[0]
    dbCfxIndex = getDbCfxIndex(assetIndex, assetVariant)
    isExistsDbFur = getExistsDbFur(assetIndex, assetVariant)
    if isExistsDbFur:
        string = lxConfigure.LynxiAstCfxStages[0]
        isExistsDbFurMaterial = isDbAstMaterialExists(dbCfxIndex)
        if isExistsDbFurMaterial:
            string = lxConfigure.LynxiAstCfxStages[1]
    return string


# Asset ( Rig ) File
def getDbAstRigAstProductFile(assetIndex, version='anim'):
    dbRigIndex = getDbAstRigIndex(assetIndex, version)
    directory = prsVariants.Database.assetRigProduct
    return getDbProductFile(dbRigIndex, directory)


# Asset ( Rig ) File
def getDbAstSolverRigProductFile(assetIndex, assetVariant):
    dbRigIndex = getDbAstSolverIndex(assetIndex, assetVariant)
    directory = prsVariants.Database.assetSolverProduct
    return getDbProductFile(dbRigIndex, directory)


#
def getExistsDbRigAstIntFile(assetIndex, version='anim'):
    dbRigIndex = getDbAstRigIndex(assetIndex, version)
    directory = prsVariants.Database.assetRigProduct
    return getExistsDbIntegrationFile(dbRigIndex, directory)


#
def getDbRigUpdate(assetIndex, version='anim'):
    dbRigAssetFile = getDbAstRigAstProductFile(assetIndex, version)
    return bscMethods.OsFile.mtimeChnPrettify(dbRigAssetFile)


#
def getDbAstSolverUpdate(assetIndex, assetVariant):
    dbRigAssetFile = getDbAstSolverRigProductFile(assetIndex, assetVariant)
    return bscMethods.OsFile.mtimeChnPrettify(dbRigAssetFile)


#
def getDbRigUpdater(assetIndex, version='anim'):
    string = prsVariants.Util.infoNonExistsLabel
    if assetIndex:
        # Mesh
        dbRigIndex = getDbAstRigIndex(assetIndex, version)
        data = dbBasic.readDbAssetHistory(dbRigIndex, prsVariants.Util.infoUpdaterLabel)
        if data:
            string = data
    return string


# Update
def getDbSceneryUnitUpdate(assetIndex, assetVariant):
    string = prsVariants.Util.infoNonExistsLabel
    if assetIndex:
        sceneryUnitIndex = getDbSceneryUnitIndex(assetIndex, assetVariant)
        data = dbBasic.readDbSceneryHistory(sceneryUnitIndex, prsVariants.Util.infoUpdateLabel)
        if data:
            string = bscMethods.OsTimestamp.toChnPrettify(data)
    return string


# Updater
def getDbSceneryUnitUpdater(assetIndex, assetVariant):
    string = prsVariants.Util.infoNonExistsLabel
    if assetIndex:
        # Mesh
        sceneryUnitIndex = getDbSceneryUnitIndex(assetIndex, assetVariant)
        data = dbBasic.readDbSceneryHistory(sceneryUnitIndex, prsVariants.Util.infoUpdaterLabel)

        if data:
            string = data
    return string


#
def getDbRigStage(assetIndex, assetVariant):
    string = lxConfigure.LynxiAstRigStages[0]
    isExistsDbLayoutRig = getExistsDbRigAstIntFile(assetIndex, version='lay')
    if isExistsDbLayoutRig:
        string = lxConfigure.LynxiAstRigStages[0]
        isExistsDbAnimRig = getExistsDbRigAstIntFile(assetIndex, version='anim')
        if isExistsDbAnimRig:
            string = lxConfigure.LynxiAstRigStages[1]
    return string


#
def getDbMeshConstantData(dbSubIndex):
    dic = {}
    if dbSubIndex:
        directory = prsVariants.Database.assetGeometryConstantIndex
        gzData = dbBasic.dbCompDatumRead(dbSubIndex, directory)
        if gzData:
            dic = gzData
    return dic


# Get Gz Asset Indexes
def getDbAssetIndexesFilter(projectName, filterClassify=none, tag=none):
    # Lis [ <Index> ]
    lis = []
    assetNameIndex = prsVariants.Database.assetNameIndex
    osFileNames = bscMethods.OsDirectory.fileBasenames(assetNameIndex)
    if osFileNames:
        for subData in osFileNames:
            assetIndex = subData
            indexFile = '%s/%s' % (assetNameIndex, assetIndex)
            gzData = dbBasic.dbDatumRead(indexFile)
            if gzData:
                if projectName in gzData:
                    # Classify Filter
                    if filterClassify:
                        dbAssetClassify = getDbAssetClass(assetIndex)
                        dbAssetTag = getDbAssetTag(assetIndex)
                        # Character and Prop
                        if dbAssetClassify == filterClassify:
                            # Tag Filter
                            if not tag:
                                lis.append(assetIndex)
                            if tag:
                                if dbAssetTag == tag:
                                    lis.append(assetIndex)
                        # Scenery
                        if filterClassify == astSceneryClass:
                            isAssembly = getExistsDbAssembly(assetIndex)
                            if isAssembly:
                                lis.append(assetIndex)
                    if not filterClassify:
                        lis.append(assetIndex)
    return lis


#
def getDbAssetIndexDic(projectFilter):
    # Lis [ <Index> ]
    dic = bscCore.orderedDict()
    models = []
    cfxs = []
    rigs = []
    assetNameIndex = prsVariants.Database.assetNameIndex
    osFileNames = bscMethods.OsDirectory.fileBasenames(assetNameIndex)
    if osFileNames:
        if osFileNames:
            explain = '''Read Asset Database'''
            maxValue = len(osFileNames)
            progressBar = bscObjects.If_Progress(explain, maxValue)
            for subData in osFileNames:
                progressBar.update()
                assetIndex = subData
                dbAssetClassify = getDbAssetClass(assetIndex)
                dbAssetTag = getDbAssetTag(assetIndex)
                #
                indexFile = '%s/%s' % (assetNameIndex, assetIndex)
                gzData = dbBasic.dbDatumRead(indexFile)
                if gzData:
                    if projectFilter in gzData:
                        for assetCategory in astBasicClassifications:
                            for tag in astBasicPriorities:
                                key = '%s|%s' % (assetCategory, tag)
                                if dbAssetClassify == assetCategory and dbAssetTag == tag:
                                    dic.setdefault(key, []).append(assetIndex)
                #
                if isDbAstExistsGeometry(assetIndex):
                    models.append(assetIndex)
                #
                if getExistsDbFur(assetIndex, astDefaultVariant):
                    cfxs.append(assetIndex)
                #
                if getExistsDbRigAstIntFile(assetIndex):
                    rigs.append(assetIndex)
    return dic, models, cfxs, rigs


# Get Asset Name
def getDbAssetIndexDicFilter(projectName, filterClassify=none, tag=none):
    # Lis [ <Name> ]
    dic = {}
    assetNameIndex = prsVariants.Database.assetNameIndex
    osFileNames = bscMethods.OsDirectory.fileBasenames(assetNameIndex)
    if osFileNames:
        for osFileName in osFileNames:
            assetIndex = osFileName
            indexFile = '%s/%s' % (assetNameIndex, assetIndex)
            gzData = dbBasic.dbDatumRead(indexFile)
            if gzData:
                if projectName in gzData:
                    assetName = gzData[projectName]
                    # Classify Filter
                    if filterClassify:
                        dbAssetClassify = getDbAssetClass(assetIndex)
                        dbAssetTag = getDbAssetTag(assetIndex)
                        # Character and Prop
                        if dbAssetClassify == filterClassify:
                            # Tag Filter
                            if not tag:
                                dic[assetName] = assetIndex
                            if tag:
                                if dbAssetTag == tag:
                                    dic[assetName] = assetIndex
                        # Scenery
                        if filterClassify == astSceneryClass:
                            isAssembly = getExistsDbAssembly(assetIndex)
                            if isAssembly:
                                dic[assetName] = assetIndex
                    if not filterClassify:
                        dic[assetName] = assetIndex
    return dic


# Get Gz Asset Models
def getDbModels(dbIndexes):
    # Lis [ <Index> ]
    lis = []
    if dbIndexes:
        explain = '''Read Model'''
        maxValue = len(dbIndexes)
        progressBar = bscObjects.If_Progress(explain, maxValue)
        for assetIndex in dbIndexes:
            progressBar.update()
            #
            if isDbAstExistsGeometry(assetIndex):
                lis.append(assetIndex)
    return lis


# Get Gz Asset Models
def getDbCfxs(dbIndexes):
    # Lis [ <Index> ]
    lis = []
    if dbIndexes:
        explain = '''Read CFX'''
        maxValue = len(dbIndexes)
        progressBar = bscObjects.If_Progress(explain, maxValue)
        for assetIndex in dbIndexes:
            progressBar.update()
            #
            if getExistsDbFur(assetIndex, astDefaultVariant):
                lis.append(assetIndex)
    return lis


# Get Gz Asset Models
def getDbRigs(dbIndexes):
    # Lis [ <Index> ]
    lis = []
    if dbIndexes:
        explain = '''Read Rig'''
        maxValue = len(dbIndexes)
        progressBar = bscObjects.If_Progress(explain, maxValue)
        for assetIndex in dbIndexes:
            progressBar.update()
            #
            if getExistsDbRigAstIntFile(assetIndex):
                lis.append(assetIndex)
    return lis


#
def getDbAssetCompletion(dbIndexes):
    models = []
    cfxs = []
    rigs = []
    if dbIndexes:
        models = getDbModels(dbIndexes)
        cfxs = getDbCfxs(dbIndexes)
        rigs = getDbRigs(dbIndexes)
    return models, cfxs, rigs


# Get Gz Asset Models
def getDbCfxNamesByClassify(projectName, filterClassify=none):
    # Lis [ <Index> ]
    lis = []
    dbIndexes = getDbAssetIndexesFilter(projectName, filterClassify)
    if dbIndexes:
        explain = '''Read CFX's Data'''
        maxValue = len(dbIndexes)
        progressBar = bscObjects.If_Progress(explain, maxValue)
        for assetIndex in dbIndexes:
            progressBar.update()
            #
            if getExistsDbFur(assetIndex, prsVariants.Util.astDefaultVariant):
                assetName = getDbAssetName(assetIndex, projectName)
                lis.append(assetName)
    if lis:
        lis.sort()
    return lis


# Get Gz Asset Models
def getDbRigNamesByClassify(projectName, filterClassify=none):
    # Lis [ <Index> ]
    lis = []
    dbIndexes = getDbAssetIndexesFilter(projectName, filterClassify)
    if dbIndexes:
        for assetIndex in dbIndexes:
            if getExistsDbRigAstIntFile(assetIndex):
                assetName = getDbAssetName(assetIndex, projectName)
                lis.append(assetName)
    lis.sort()
    return lis


#
def getDbAssetFilterData(assetCategory, tag=none):
    dic = bscCore.orderedDict()
    dic['classify'] = assetCategory
    dic['tag'] = tag
    return dic


#
def getDbAssetNameData(assetIndex, projectName, assetName):
    dic = {none: assetName}
    directory = prsVariants.Database.assetNameIndex
    gzData = dbBasic.dbCompDatumRead(assetIndex, directory)
    if gzData:
        dic = gzData
    dic[projectName] = assetName
    return dic


#
def getDbAssetVariantData(assetIndex, assetVariant):
    lis = []
    directory = prsVariants.Database.assetVariantIndex
    variantData = dbBasic.dbCompDatumRead(assetIndex, directory)
    if variantData:
        lis = variantData
    if not assetVariant in lis:
        lis.append(assetVariant)
    return lis


#
def getDbAssetAssemblyData(assetIndex, percentage):
    dic = {}
    directory = prsVariants.Database.assetAssemblyIndex
    dbAssemblyData = dbBasic.dbCompDatumRead(assetIndex, directory)
    if dbAssemblyData:
        dic = dbAssemblyData
    dic['percentage'] = percentage
    return dic


#
def getDbAssetMeshCheck(assetIndex, assetVariant, assetLink):
    def getBranch(key):
        return sourceData[key] == targetData[key]
    #
    checkKeys = assetCfg.basicAssetMeshCheckKeys()
    #
    sourceData = getDbMeshConstantData(assetIndex)
    assetSubIndex = assetIndex
    if assetLink == lxConfigure.VAR_product_asset_link_model:
        assetSubIndex = getDbAstModelIndex(assetIndex, assetVariant)
    elif assetLink == lxConfigure.VAR_product_asset_link_groom:
        assetSubIndex = getDbCfxIndex(assetIndex, assetVariant)
    elif assetLink == lxConfigure.VAR_product_asset_link_rig:
        assetSubIndex = getDbAstRigIndex(assetIndex)
    #
    targetData = getDbMeshConstantData(assetSubIndex)
    #
    meshCheck = None
    if sourceData:
        if targetData:
            checkResult = [getBranch(i) for i in checkKeys]
            if checkResult[0] is False or checkResult[1] is False:
                meshCheck = 'error'
            elif checkResult[:3] == [True, True, False]:
                meshCheck = 'warning'
        else:
            meshCheck = 'wait'
    else:
        meshCheck = 'error'
    return meshCheck


#
def getScModelCacheMeshCheck(assetIndex, cacheFile):
    def getBranch(key):
        return sourceData[key] == targetData[key]
    #
    checkKeys = assetCfg.basicAssetMeshCheckKeys()
    #
    sourceData = getDbMeshConstantData(assetIndex)
    #
    if bscMethods.OsFile.isExist(cacheFile):
        cacheMeshDataFile = scenePr.getMeshDataFile(cacheFile)
        targetData = bscMethods.OsJson.read(cacheMeshDataFile)
        #
        if sourceData:
            if targetData:
                checkResult = [getBranch(i) for i in checkKeys]
                if checkResult[:2] == [True, True]:
                    meshCheck = 'on'
                else:
                    meshCheck = 'error'
            else:
                meshCheck = 'warning'
        else:
            meshCheck = 'error'
    else:
        meshCheck = 'off'
    #
    return meshCheck


#
def getScModelCacheMeshEvaluateData(assetIndex, cacheFile):
    sourceData = getDbMeshConstantData(assetIndex)
    #
    cacheMeshDataFile = scenePr.getMeshDataFile(cacheFile)
    targetData = bscMethods.OsJson.read(cacheMeshDataFile)
    return sourceData, targetData
