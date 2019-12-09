# coding:utf-8
from LxCore import lxBasic, lxConfigure, lxProgress
#
from LxCore.config import assetCfg
#
from LxCore.preset import appVariant, databasePr, personnelPr
#
from LxCore.preset.prod import assetPr, scenePr
#
from LxDatabase import dbBasic
# Type Config
astBasicClassifications = appVariant.astBasicClassifications
astBasicPriorities = appVariant.astBasicPriorities
astSceneryClass = appVariant.astSceneryClass
#
astDefaultVariant = appVariant.astDefaultVersion
#
Ma_Separator_Node = lxBasic.Ma_Separator_Node
Ma_Separator_Namespace = lxBasic.Ma_Separator_Namespace
#
none = ''


# Get File's Update
def getFileUpdate(osFile):
    string = appVariant.infoNonExistsLabel
    if lxBasic.isOsExistsFile(osFile):
        data = lxBasic.getCnViewTime(lxBasic.getOsFileMtimestamp(osFile))
        if data:
            string = data
    return string


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
        osFile = getDbGzFile(assetIndex, directory)
        boolean = lxBasic.isOsExistsFile(osFile)
    return boolean


#
def getDbProductFile(assetIndex, directory):
    string = directory + '/' + assetIndex
    return string


#
def getExistsDbIntegrationFile(assetIndex, directory):
    boolean = False
    if assetIndex:
        osFile = getDbProductFile(assetIndex, directory)
        boolean = lxBasic.isOsExistsFile(osFile)
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
        osFile = getDbCompFile(assetIndex, scCompIndex, directory)
        boolean = lxBasic.isOsExistsFile(osFile)
    return boolean


#
def getExistsDbAsset(assetIndex):
    directory = databasePr.dbAstNameIndexDirectory()
    return isDbExistsGzFile(assetIndex, directory)


#
def getDbAssetIndex(projectName, assetName):
    # Lis [ <Name> ]
    string = none
    directory = databasePr.dbAstNameIndexDirectory()
    if projectName and assetName:
        assetIndex = dbBasic.getDatabaseMainIndex([projectName, assetName])
        if isDbExistsGzFile(assetIndex, directory):
            string = assetIndex
    return string


#
def getDbAssetLinkIndex(assetIndex, assetVariant, assetStage, version=None):
    assetLinkIndex = assetIndex
    if assetPr.isAstModelLink(assetStage) or assetPr.isAstCfxLink(assetStage) or assetPr.isAstSolverLink(assetStage):
        assetLinkIndex = dbBasic.getDatabaseSubIndex(assetIndex, [lxConfigure.LynxiProduct_Asset_Link_Model, assetVariant])
    elif assetPr.isAstRigLink(assetStage):
        assetLinkIndex = dbBasic.getDatabaseSubIndex(assetIndex, [lxConfigure.LynxiProduct_Asset_Link_Rig, version])
    #
    return assetLinkIndex


#
def getDbAstModelIndex(assetIndex, assetVariant):
    string = none
    if assetIndex:
        data = dbBasic.getDatabaseSubIndex(assetIndex, [lxConfigure.LynxiProduct_Asset_Link_Model, assetVariant])
        if data:
            string = data
    return string


#
def getDbAstRigIndex(assetIndex, version='anim'):
    string = none
    if assetIndex:
        data = dbBasic.getDatabaseSubIndex(assetIndex, [lxConfigure.LynxiProduct_Asset_Link_Rig, version])
        if data:
            string = data
    return string


#
def getDbCfxIndex(assetIndex, assetVariant):
    string = none
    if assetIndex:
        data = dbBasic.getDatabaseSubIndex(assetIndex, [lxConfigure.LynxiProduct_Asset_Link_Cfx, assetVariant])
        if data:
            string = data
    return string


#
def getDbAstSolverIndex(assetIndex, assetVariant):
    string = none
    if assetIndex:
        data = dbBasic.getDatabaseSubIndex(assetIndex, [lxConfigure.LynxiProduct_Asset_Link_Solver, assetVariant])
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
        directory = databasePr.dbAstFilterIndexDirectory()
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
        directory = databasePr.dbAstNameIndexDirectory()
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
        directory = databasePr.dbAstVariantIndexDirectory()
        data = dbBasic.dbCompDatumRead(assetIndex, directory)
        if data:
            lis = data
    return lis


#
def getDbAssemblyPercentage(assetIndex):
    # LIST [ <LOD01 Percentage>, <LOD02 Percentage> ]
    lis = []
    if assetIndex:
        directory = databasePr.dbAstAssemblyIndexDirectory()
        data = dbBasic.dbCompDatumRead(assetIndex, directory)
        if data:
            lis = data['percentage']
    return lis


#
def dbAssetPreviewFile(assetIndex, assetLink, assetVariant, extLabel=appVariant.jpgExt):
    if assetIndex:
        directory = databasePr.dbAstPreviewDirectory()
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
        directory = databasePr.dbAstPreviewDirectory()
        osFile = directory + '/' + assetIndex + appVariant.jpgExt
        if lxBasic.isOsExist(osFile):
            string = osFile
    return string


#
def dbAstRenderPreviewFile(assetIndex, assetVariant):
    string = none
    if assetIndex:
        directory = databasePr.dbAstPreviewDirectory()
        assetSubIndex = dbBasic.getDatabaseSubIndex(assetIndex, [lxConfigure.LynxiProduct_Asset_Link_Model, assetVariant])
        osFile = directory + '/' + assetSubIndex + appVariant.pngExt
        if lxBasic.isOsExist(osFile):
            string = osFile
    return string


#
def getDbAstPreviewFile(assetIndex, assetVariant=none):
    string = none
    if assetIndex:
        directory = databasePr.dbAstPreviewDirectory()
        string = directory + '/' + assetIndex + appVariant.jpgExt
        if assetVariant:
            dbModelIndex = getDbAstModelIndex(assetIndex, assetVariant)
            renderPrv = directory + '/' + dbModelIndex + appVariant.pngExt
            texturePrv = directory + '/' + dbModelIndex + appVariant.jpgExt
            if lxBasic.isOsExistsFile(renderPrv):
                string = renderPrv
            elif lxBasic.isOsExistsFile(texturePrv):
                string = texturePrv
    return string


#
def getDbSceneryUnitPreviewFile(assetIndex, assetVariant=none):
    string = none
    if assetIndex:
        directory = databasePr.dbScnUnitPreviewDirectory()
        string = directory + '/' + assetIndex + appVariant.jpgExt
        if assetVariant:
            dbModelIndex = getDbSceneryUnitIndex(assetIndex, assetVariant)
            renderPrv = directory + '/' + dbModelIndex + appVariant.pngExt
            texturePrv = directory + '/' + dbModelIndex + appVariant.jpgExt
            if lxBasic.isOsExistsFile(renderPrv):
                string = renderPrv
            elif lxBasic.isOsExistsFile(texturePrv):
                string = texturePrv
    return string


#
def getDbAstGeometryFile(assetIndex):
    directory = databasePr.dbAstGeometryIndexDirectory()
    return getDbGzFile(assetIndex, directory)


#
def isDbAstExistsGeometry(assetIndex):
    directory = databasePr.dbAstGeometryIndexDirectory()
    return isDbExistsGzFile(assetIndex, directory)


#
def getDbAstMaterialFile(dbSubIndex):
    directory = databasePr.dbAstMaterialIndexDirectory()
    return getDbGzFile(dbSubIndex, directory)


#
def isDbAstMaterialExists(dbSubIndex):
    directory = databasePr.dbAstMaterialIndexDirectory()
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
    directory = databasePr.dbAstAssemblyIndexDirectory()
    return isDbExistsGzFile(assetIndex, directory)


#
def getDbAstUpdate(assetIndex, assetVariant, assetStage):
    string = appVariant.infoNonExistsLabel
    if assetIndex:
        assetLink = assetPr.getAssetLink(assetStage)
        assetSubIndex = dbBasic.getDatabaseSubIndex(assetIndex, [assetLink, assetVariant])
        timestamp = dbBasic.readDbAssetHistory(assetSubIndex, appVariant.infoUpdateLabel)
        if timestamp:
            string = lxBasic.getCnViewTime(timestamp)
    return string


#
def getDbAstUpdater(assetIndex, assetVariant, assetStage):
    string = appVariant.infoNonExistsLabel
    if assetIndex:
        assetLink = assetPr.getAssetLink(assetStage)
        if assetPr.isAstRigLink(assetStage):
            assetSubIndex = getDbAstRigIndex(assetIndex)
        else:
            assetSubIndex = dbBasic.getDatabaseSubIndex(assetIndex, [assetLink, assetVariant])
        osUser = dbBasic.readDbAssetHistory(assetSubIndex, appVariant.infoUpdaterLabel)
        if osUser:
            string = personnelPr.getPersonnelUserCnName(osUser)
    return string


#
def getDbModelUpdate(assetIndex, assetVariant):
    string = appVariant.infoNonExistsLabel
    if assetIndex:
        # Mesh
        dbModelIndex = getDbAstModelIndex(assetIndex, assetVariant)
        dbGeometryFile = getDbAstGeometryFile(assetIndex)
        if lxBasic.isOsExistsFile(dbGeometryFile):
            dbMeshTimeStamp = lxBasic.getOsFileMtimestamp(dbGeometryFile)
            # Material
            dbMaterialFile = getDbAstMaterialFile(dbModelIndex)
            timestamp = dbMeshTimeStamp
            if lxBasic.isOsExistsFile(dbMaterialFile):
                dbMaterialTimeStamp = lxBasic.getOsFileMtimestamp(dbMaterialFile)
                timestamp = max([dbMeshTimeStamp, dbMaterialTimeStamp])
            #
            string = lxBasic.getCnViewTime(timestamp)
    return string


#
def getDbModelUpdater(assetIndex, assetVariant):
    string = appVariant.infoNonExistsLabel
    if assetIndex:
        # Mesh
        dbModelIndex = getDbAstModelIndex(assetIndex, assetVariant)
        data = dbBasic.readDbAssetHistory(dbModelIndex, appVariant.infoUpdaterLabel)
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
    dic = lxBasic.orderedDict()
    if assetIndex:
        directory = databasePr.dbAstGeometryIndexDirectory()
        data = dbBasic.dbCompDatumRead(assetIndex, directory)
        if data:
            dic = data
    return dic


#
def getDbGeometryObjectsInfoDic(assetIndex, dbName, namespace, searchRoot):
    dic = lxBasic.orderedDict()
    if assetIndex:
        directory = databasePr.dbAstGeometryIndexDirectory()
        data = dbBasic.dbCompDatumRead(assetIndex, directory)
        if data:
            for objectIndex, info in data.items():
                meshPath = getDbGeometryObjectPath(assetIndex, dbName, objectIndex)
                if searchRoot in meshPath:
                    key = [none, namespace + Ma_Separator_Namespace][namespace is not none] + lxBasic.getMayaObjectName(meshPath)
                    dic[key] = info
    return dic


#
def getDbGeometryObjectPath(assetIndex, dbName, objectIndex):
    string = none
    if assetIndex:
        directory = databasePr.dbAstGeometryTransformUnitDirectory()
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
        directory = databasePr.dbAstGeometryTransformUnitDirectory()
        dbCompIndex = dbBasic.getDatabaseCompIndex(assetIndex, objectIndex)
        data = dbBasic.dbCompDatumRead(dbCompIndex, directory)
        if data:
            tup = data
    return tup


#
def getDbGeometryUnitsPathDic(assetIndex):
    dic = lxBasic.orderedDict()
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
        directory = databasePr.dbAstMaterialObjAttrUnitDirectory()
        dbCompIndex = dbBasic.getDatabaseCompIndex(assetIndex, objectIndex)
        data = dbBasic.dbCompDatumRead(dbCompIndex, directory)
        if data:
            lis = data
    return lis


#
def getDbGeometryObjectsObjSetDic(assetIndex, objectIndex):
    lis = []
    if assetIndex:
        directory = databasePr.dbAstMaterialObjSetUnitDirectory()
        dbCompIndex = dbBasic.getDatabaseCompIndex(assetIndex, objectIndex)
        data = dbBasic.dbCompDatumRead(dbCompIndex, directory)
        if data:
            lis = data
    return lis


#
def getDbCompFurIndexData(dbSubIndex):
    dic = {}
    directory = databasePr.dbAstFurIndexDirectory()
    data = dbBasic.dbCompDatumRead(dbSubIndex, directory)
    if data:
        dic = data
    return dic


#
def getDbCompNurbsHairIndexData(dbSubIndex):
    dic = {}
    directory = databasePr.dbAstGraphIndexDirectory()
    data = dbBasic.dbCompDatumRead(dbSubIndex, directory)
    if data:
        dic = data
    return dic


#
def getDbMaterialIndexData(dbSubIndex):
    dic = {}
    if dbSubIndex:
        directory = databasePr.dbAstMaterialIndexDirectory()
        data = dbBasic.dbCompDatumRead(dbSubIndex, directory)
        if data:
            dic = data
    return dic


#
def getDbAovIndexData(dbSubIndex):
    dic = {}
    if dbSubIndex:
        directory = databasePr.dbAstAovIndexDirectory()
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
def getAstUnitDbAssemblyUpdate(projectName, assetClass, assetName, assetVariant):
    serverAstUnitAsbDefinitionFile = assetPr.astUnitAssemblyDefinitionFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Assembly
    )[1]
    return getFileUpdate(serverAstUnitAsbDefinitionFile)


#
def getDbFurFile(dbSubIndex):
    directory = databasePr.dbAstCfxFurProductDirectory()
    return getDbProductFile(dbSubIndex, directory)


#
def getExistsDbFur(assetIndex, assetVariant):
    directory = databasePr.dbAstCfxFurProductDirectory()
    dbCfxIndex = getDbCfxIndex(assetIndex, assetVariant)
    return getExistsDbIntegrationFile(dbCfxIndex, directory)


#
def getDbCfxUpdate(assetIndex, assetVariant):
    string = appVariant.infoNonExistsLabel
    if assetIndex:
        # Mesh
        dbCfxIndex = getDbCfxIndex(assetIndex, assetVariant)
        dbFurFile = getDbFurFile(dbCfxIndex)
        if lxBasic.isOsExistsFile(dbFurFile):
            dbFurTimeStamp = lxBasic.getOsFileMtimestamp(dbFurFile)
            # Material
            dbMaterialFile = getDbAstMaterialFile(dbCfxIndex)
            #
            timestamp = dbFurTimeStamp
            if lxBasic.isOsExistsFile(dbMaterialFile):
                dbMaterialTimeStamp = lxBasic.getOsFileMtimestamp(dbMaterialFile)
                timestamp = max([dbFurTimeStamp, dbMaterialTimeStamp])
            #
            string = lxBasic.getCnViewTime(timestamp)
    return string


#
def getDbCfxUpdater(assetIndex, assetVariant):
    string = appVariant.infoNonExistsLabel
    if assetIndex:
        # Mesh
        dbCfxIndex = getDbCfxIndex(assetIndex, assetVariant)
        data = dbBasic.readDbAssetHistory(dbCfxIndex, appVariant.infoUpdaterLabel)
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
    directory = databasePr.dbAstRigProductDirectory()
    return getDbProductFile(dbRigIndex, directory)


# Asset ( Rig ) File
def getDbAstSolverRigProductFile(assetIndex, assetVariant):
    dbRigIndex = getDbAstSolverIndex(assetIndex, assetVariant)
    directory = databasePr.dbAstRigSolProductDirectory()
    return getDbProductFile(dbRigIndex, directory)


#
def getExistsDbRigAstIntFile(assetIndex, version='anim'):
    dbRigIndex = getDbAstRigIndex(assetIndex, version)
    directory = databasePr.dbAstRigProductDirectory()
    return getExistsDbIntegrationFile(dbRigIndex, directory)


#
def getDbRigUpdate(assetIndex, version='anim'):
    dbRigAssetFile = getDbAstRigAstProductFile(assetIndex, version)
    return getFileUpdate(dbRigAssetFile)


#
def getDbAstSolverUpdate(assetIndex, assetVariant):
    dbRigAssetFile = getDbAstSolverRigProductFile(assetIndex, assetVariant)
    return getFileUpdate(dbRigAssetFile)


#
def getDbRigUpdater(assetIndex, version='anim'):
    string = appVariant.infoNonExistsLabel
    if assetIndex:
        # Mesh
        dbRigIndex = getDbAstRigIndex(assetIndex, version)
        data = dbBasic.readDbAssetHistory(dbRigIndex, appVariant.infoUpdaterLabel)
        if data:
            string = data
    return string


# Update
def getDbSceneryUnitUpdate(assetIndex, assetVariant):
    string = appVariant.infoNonExistsLabel
    if assetIndex:
        sceneryUnitIndex = getDbSceneryUnitIndex(assetIndex, assetVariant)
        data = dbBasic.readDbSceneryHistory(sceneryUnitIndex, appVariant.infoUpdateLabel)
        if data:
            string = lxBasic.getCnViewTime(data)
    return string


# Updater
def getDbSceneryUnitUpdater(assetIndex, assetVariant):
    string = appVariant.infoNonExistsLabel
    if assetIndex:
        # Mesh
        sceneryUnitIndex = getDbSceneryUnitIndex(assetIndex, assetVariant)
        data = dbBasic.readDbSceneryHistory(sceneryUnitIndex, appVariant.infoUpdaterLabel)

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
        directory = databasePr.dbAstGeometryConstantDirectory()
        gzData = dbBasic.dbCompDatumRead(dbSubIndex, directory)
        if gzData:
            dic = gzData
    return dic


# Get Gz Asset Indexes
def getDbAssetIndexesFilter(projectName, filterClassify=none, tag=none):
    # Lis [ <Index> ]
    lis = []
    dbAstNameIndexDirectory = databasePr.dbAstNameIndexDirectory()
    osFileNames = lxBasic.getOsFileBasenameLisByPath(dbAstNameIndexDirectory)
    if osFileNames:
        for subData in osFileNames:
            assetIndex = subData
            indexFile = '%s/%s' % (dbAstNameIndexDirectory, assetIndex)
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
    dic = lxBasic.orderedDict()
    models = []
    cfxs = []
    rigs = []
    dbAstNameIndexDirectory = databasePr.dbAstNameIndexDirectory()
    osFileNames = lxBasic.getOsFileBasenameLisByPath(dbAstNameIndexDirectory)
    if osFileNames:
        if osFileNames:
            explain = '''Read Asset Database'''
            maxValue = len(osFileNames)
            progressBar = lxProgress.viewSubProgress(explain, maxValue)
            for subData in osFileNames:
                progressBar.updateProgress()
                assetIndex = subData
                dbAssetClassify = getDbAssetClass(assetIndex)
                dbAssetTag = getDbAssetTag(assetIndex)
                #
                indexFile = '%s/%s' % (dbAstNameIndexDirectory, assetIndex)
                gzData = dbBasic.dbDatumRead(indexFile)
                if gzData:
                    if projectFilter in gzData:
                        for assetClass in astBasicClassifications:
                            for tag in astBasicPriorities:
                                key = '%s|%s' % (assetClass, tag)
                                if dbAssetClassify == assetClass and dbAssetTag == tag:
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
    dbAstNameIndexDirectory = databasePr.dbAstNameIndexDirectory()
    osFileNames = lxBasic.getOsFileBasenameLisByPath(dbAstNameIndexDirectory)
    if osFileNames:
        for osFileName in osFileNames:
            assetIndex = osFileName
            indexFile = '%s/%s' % (dbAstNameIndexDirectory, assetIndex)
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
        progressBar = lxProgress.viewSubProgress(explain, maxValue)
        for assetIndex in dbIndexes:
            progressBar.updateProgress()
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
        progressBar = lxProgress.viewSubProgress(explain, maxValue)
        for assetIndex in dbIndexes:
            progressBar.updateProgress()
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
        progressBar = lxProgress.viewSubProgress(explain, maxValue)
        for assetIndex in dbIndexes:
            progressBar.updateProgress()
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
        progressBar = lxProgress.viewSubProgress(explain, maxValue)
        for assetIndex in dbIndexes:
            progressBar.updateProgress()
            #
            if getExistsDbFur(assetIndex, appVariant.astDefaultVariant):
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
def getDbAssetFilterData(assetClass, tag=none):
    dic = lxBasic.orderedDict()
    dic['classify'] = assetClass
    dic['tag'] = tag
    return dic


#
def getDbAssetNameData(assetIndex, projectName, assetName):
    dic = {none: assetName}
    directory = databasePr.dbAstNameIndexDirectory()
    gzData = dbBasic.dbCompDatumRead(assetIndex, directory)
    if gzData:
        dic = gzData
    dic[projectName] = assetName
    return dic


#
def getDbAssetVariantData(assetIndex, assetVariant):
    lis = []
    directory = databasePr.dbAstVariantIndexDirectory()
    variantData = dbBasic.dbCompDatumRead(assetIndex, directory)
    if variantData:
        lis = variantData
    if not assetVariant in lis:
        lis.append(assetVariant)
    return lis


#
def getDbAssetAssemblyData(assetIndex, percentage):
    dic = {}
    directory = databasePr.dbAstAssemblyIndexDirectory()
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
    if assetLink == lxConfigure.LynxiProduct_Asset_Link_Model:
        assetSubIndex = getDbAstModelIndex(assetIndex, assetVariant)
    elif assetLink == lxConfigure.LynxiProduct_Asset_Link_Cfx:
        assetSubIndex = getDbCfxIndex(assetIndex, assetVariant)
    elif assetLink == lxConfigure.LynxiProduct_Asset_Link_Rig:
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
    if lxBasic.isOsExist(cacheFile):
        cacheMeshDataFile = scenePr.getMeshDataFile(cacheFile)
        targetData = lxBasic.readOsJson(cacheMeshDataFile)
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
    targetData = lxBasic.readOsJson(cacheMeshDataFile)
    return sourceData, targetData
