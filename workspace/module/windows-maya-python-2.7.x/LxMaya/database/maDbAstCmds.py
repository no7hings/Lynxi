# coding:utf-8
from LxBasic import bscMethods, bscObjects

from LxUi.qt import qtCommands
#
from LxPreset import prsVariants, prsMethods
#
from LxDatabase import dbBasic, dbGet
#
from LxMaya.command import maUtils, maUuid, maGeom, maShdr, maFur
#
DEF_separator_node = '|'


# Nde_Geometry
def dbAstGeometryUploadMainCmd(assetIndex, assetName, groupString, timeTag):
    objectStrings = maGeom.getGeometryObjectsByGroup(groupString)
    if objectStrings:
        dbAstGeometryUploadMainCmd_(assetIndex, objectStrings, groupString, assetName, timeTag)


#
def dbAstGeometryUploadMainCmd_(assetIndex, objectStrings, groupString, assetName, timeTag):
    if objectStrings:
        progressExplain = u'''Uploading Database Asset Mesh'''
        #
        subProgressDataLis = [
            (True, u'''Index''', dbAstUploadGeometryObjectsIndexSub, (assetIndex, objectStrings, groupString, timeTag)),
            #
            (True, u'''Transform''', dbAstUploadGeometryObjectsTransformSub, (assetIndex, objectStrings, groupString, assetName, timeTag)),
            #
            (True, u'''Nde_Geometry''', dbAstUploadGeometryObjectsGeometrySub, (assetIndex, objectStrings, timeTag)),
            (True, u'''Map''', dbAstUploadGeometryObjectsMapSub, (assetIndex, objectStrings, timeTag)),
            #
            (True, u'''Vertex - Normal''', dbAstUploadGeometryObjectsVertexNormalSub, (assetIndex, objectStrings, timeTag)),
            (True, u'''Edge - Smooth''', dbAstUploadGeometryObjectsEdgeSmoothSub, (assetIndex, objectStrings, timeTag))
        ]
        #
        qtCommands.setProgressRun(progressExplain, subProgressDataLis)


#
def dbAstUploadGeometryObjectsIndexSub(assetIndex, objectStrings, groupString, timeTag):
    directory = prsVariants.Database.assetGeometryIndex
    dataDic = maGeom.getGeometryObjectsInfoDic_(objectStrings, groupString)
    dbBasic.dbCompDatumWrite(assetIndex, dataDic, directory, timeTag)


#
def dbAstUploadGeometryObjectsTransformSub(assetIndex, objectStrings, groupString, assetName, timeTag):
    directory = prsVariants.Database.assetGeometryTransform
    dataDic = maGeom.getGeometryObjectsTransformDic_(objectStrings, groupString, assetName)
    dbBasic.dbCompDatumDicWrite(dataDic, assetIndex, directory, timeTag)


#
def dbAstUploadGeometryObjectsGeometrySub(assetIndex, objectStrings, timeTag):
    geomTopoDir, geomShapeDir = prsVariants.Database.assetGeometryTopology, prsVariants.Database.assetGeometryShape
    geomTopoDic, geomShapeDic = maGeom.getGeometryObjectsGeometryDic_(objectStrings)
    dbBasic.dbCompDatumDicWrite(geomTopoDic, assetIndex, geomTopoDir, timeTag), dbBasic.dbCompDatumDicWrite(geomShapeDic, assetIndex, geomShapeDir, timeTag)


#
def dbAstUploadGeometryObjectsMapSub(assetIndex, objectStrings, timeTag):
    directory = prsVariants.Database.assetGeometryMap
    dataDic = maGeom.getGeometryObjectsMapDic_(objectStrings)
    dbBasic.dbCompDatumDicWrite(dataDic, assetIndex, directory, timeTag)


#
def dbAstUploadGeometryObjectsVertexNormalSub(assetIndex, objectStrings, timeTag):
    directory = prsVariants.Database.assetGeometryVertexNormal
    dataDic = maGeom.getGeometryObjectsVertexNormalDic_(objectStrings)
    dbBasic.dbCompDatumDicWrite(dataDic, assetIndex, directory, timeTag)


#
def dbAstUploadGeometryObjectsEdgeSmoothSub(assetIndex, objectStrings, timeTag):
    directory = prsVariants.Database.assetGeometryEdgeSmooth
    dataDic = maGeom.getGeometryObjectsEdgeSmoothDic_(objectStrings)
    dbBasic.dbCompDatumDicWrite(dataDic, assetIndex, directory, timeTag)


#
def dbAstUploadModelGeometryConstantSub(assetIndex, groupString, timeTag):
    # Mesh Constant
    directory = prsVariants.Database.assetGeometryConstantIndex
    data = maGeom.getGeometryObjectsConstantDic_(groupString)
    dbBasic.dbCompDatumWrite(assetIndex, data, directory, timeTag)


# Asset Fur
def dbAstUploadFurMain(compFurObjects, assetSubIndex, timeTag):
    if compFurObjects:
        progressExplain = u'''Uploading Database Asset Fur'''
        #
        subProgressDataLis = [
            (True, u'''Index''', dbAstUploadFurIndexSub, (compFurObjects, assetSubIndex, timeTag)),
            (True, u'''Path''', dbAstUploadFurPathSub, (compFurObjects, assetSubIndex, timeTag))
        ]
        #
        qtCommands.setProgressRun(progressExplain, subProgressDataLis)


#
def dbAstUploadFurIndexSub(compFurObjects, assetSubIndex, timeTag):
    directory = prsVariants.Database.assetFurIndex
    dataDic = maFur.getFurObjectsInfoDic(compFurObjects)
    dbBasic.dbCompDatumWrite(assetSubIndex, dataDic, directory, timeTag)


#
def dbAstUploadFurPathSub(compFurObjects, assetSubIndex, timeTag):
    directory = prsVariants.Database.assetFurPath
    dataDic = maFur.getFurObjectsPathDic(compFurObjects)
    dbBasic.dbCompDatumDicWrite(dataDic, assetSubIndex, directory, timeTag)


# Nurbs Hair
def dbAstUploadNurbsHairMain(nurbsHairObjects, assetSubIndex, timeTag):
    if nurbsHairObjects:
        progressExplain = u'''Uploading Database Asset Nurbs Hair'''
        #
        subProgressDataLis = [
            (True, u'''Index''', dbAstUploadNurbsHairObjectsIndexSub, (nurbsHairObjects, assetSubIndex, timeTag)),
            #
            (True, u'''Graph ( Nde_Node )''', dbAstUploadNurbsHairObjectsGraphNodeSub, (nurbsHairObjects, assetSubIndex, timeTag)),
            (True, u'''Graph ( Nde_Geometry )''', dbAstUploadNurbsHairObjectsGraphGeometrySub, (nurbsHairObjects, assetSubIndex, timeTag)),
            (True, u'''Graph ( Relation )''', dbAstUploadNurbsHairObjectsGraphRelationSub, (nurbsHairObjects, assetSubIndex, timeTag))
        ]
        #
        qtCommands.setProgressRun(progressExplain, subProgressDataLis)


#
def dbAstUploadNurbsHairObjectsIndexSub(nurbsHairObjects, assetSubIndex, timeTag):
    directory = prsVariants.Database.assetGraphIndex
    dataDic = maFur.getNhrObjectsInfoDic(nurbsHairObjects)
    dbBasic.dbCompDatumWrite(assetSubIndex, dataDic, directory, timeTag)


#
def dbAstUploadNurbsHairObjectsGraphNodeSub(nurbsHairObjects, assetSubIndex, timeTag):
    directory = prsVariants.Database.assetGraphNode
    dataDic = maFur.getNhrObjectsGraphNodeDic(nurbsHairObjects)
    dbBasic.dbCompDatumDicWrite(dataDic, assetSubIndex, directory, timeTag)


#
def dbAstUploadNurbsHairObjectsGraphGeometrySub(nurbsHairObjects, assetSubIndex, timeTag):
    directory = prsVariants.Database.assetGraphGeometry
    dataDic = maFur.getNhrObjectsGraphGeometryDic(nurbsHairObjects)
    dbBasic.dbCompDatumDicWrite(dataDic, assetSubIndex, directory, timeTag)


#
def dbAstUploadNurbsHairObjectsGraphRelationSub(nurbsHairObjects, assetSubIndex, timeTag):
    directory = prsVariants.Database.assetGraphRelation
    dataDic = maFur.getNhrObjectsGraphRelationDic(nurbsHairObjects)
    dbBasic.dbCompDatumDicWrite(dataDic, assetSubIndex, directory, timeTag)


# Material
def dbAstMaterialUploadMainCmd(compMatlObjects, assetSubIndex, timeTag):
    compMaterials = maShdr.getObjectsMaterials(compMatlObjects)
    if compMaterials:
        progressExplain = u'''Uploading Database Asset Material'''
        #
        subProgressDataLis = [
            (True, u'''Index''', dbAstUploadMaterialIndexSub, (compMaterials, assetSubIndex, timeTag)),
            (True, u'''Nde_Node''', dbAstUploadMaterialCompNodeSub, (compMaterials, assetSubIndex, timeTag)),
            (True, u'''Relation''', dbAstUploadMaterialCompRelationSub, (compMaterials, assetSubIndex, timeTag)),
            (True, u'''Object - Attribute''', dbAstUploadMaterialObjAttrSub, (compMatlObjects, assetSubIndex, timeTag)),
            (True, u'''Object - Set''', dbAstUploadMaterialObjSetSub, (compMatlObjects, assetSubIndex, timeTag)),
        ]
        #
        qtCommands.setProgressRun(progressExplain, subProgressDataLis)


#
def dbAstUploadMaterialIndexSub(compMaterials, assetSubIndex, timeTag):
    directory = prsVariants.Database.assetMaterialIndex
    dataDic = maShdr.getMaterialsInformationData(compMaterials)
    dbBasic.dbCompDatumWrite(assetSubIndex, dataDic, directory, timeTag)


#
def dbAstUploadMaterialCompNodeSub(compMaterials, assetSubIndex, timeTag):
    directory = prsVariants.Database.assetMaterialNode
    dataDic = maShdr.getMaterialsNodeData(compMaterials)
    dbBasic.dbCompDatumDicWrite(dataDic, assetSubIndex, directory, timeTag)


#
def dbAstUploadMaterialCompRelationSub(compMaterials, assetSubIndex, timeTag):
    directory = prsVariants.Database.assetMaterialRelation
    dataDic = maShdr.getMaterialsRelationData(compMaterials)
    dbBasic.dbCompDatumDicWrite(dataDic, assetSubIndex, directory, timeTag)


#
def dbAstUploadMaterialObjSetSub(compMatlObjects, assetSubIndex, timeTag):
    directory = prsVariants.Database.assetMaterialObjectSet
    dataDic = maShdr.getShaderObjectsObjSetDic(compMatlObjects)
    dbBasic.dbCompDatumDicWrite(dataDic, assetSubIndex, directory, timeTag)


#
def dbAstUploadMaterialObjAttrSub(compMatlObjects, assetSubIndex, timeTag):
    directory = prsVariants.Database.assetMaterialAttribute
    dataDic = maShdr.getObjectsAttrData(compMatlObjects)
    dbBasic.dbCompDatumDicWrite(dataDic, assetSubIndex, directory, timeTag)


# AOV
def dbAstAovUploadCmd(renderer, assetSubIndex, timeTag):
    aovNodeLis = maShdr.getAovNodeLis(renderer)
    progressExplain = u'''Uploading Database Asset AOV'''
    subProgressDataLis = [
        (True, u'''Index''', dbAstUploadAovIndexSub, (aovNodeLis, assetSubIndex, timeTag)),
        (True, u'''Nde_Node''', dbAstUploadAovCompNodeSub, (aovNodeLis, assetSubIndex, timeTag)),
        (True, u'''Relation''', dbAstUploadAovCompRelationSub, (aovNodeLis, assetSubIndex, timeTag)),
    ]
    #
    qtCommands.setProgressRun(progressExplain, subProgressDataLis)


#
def dbAstUploadAovIndexSub(aovNodeLis, assetSubIndex, timeTag):
    directory = prsVariants.Database.assetAovIndex
    dataDic = maShdr.getMaterialsInformationData(aovNodeLis)
    dbBasic.dbCompDatumWrite(assetSubIndex, dataDic, directory, timeTag)


#
def dbAstUploadAovCompNodeSub(aovNodeLis, assetSubIndex, timeTag):
    directory = prsVariants.Database.assetAovNode
    dataDic = maShdr.getMaterialsNodeData(aovNodeLis)
    dbBasic.dbCompDatumDicWrite(dataDic, assetSubIndex, directory, timeTag)


#
def dbAstUploadAovCompRelationSub(aovNodeLis, assetSubIndex, timeTag):
    directory = prsVariants.Database.assetAovRelation
    dataDic = maShdr.getMaterialsRelationData(aovNodeLis)
    dbBasic.dbCompDatumDicWrite(dataDic, assetSubIndex, directory, timeTag)


#
def dbAstUploadModelProduct(assetIndex, assetVariant):
    dbModelIndex = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
    directory = prsVariants.Database.assetModelProduct
    dbBasic.saveDbMayaAscii(dbModelIndex, directory)


#
def dbAstUploadMeshProduct(assetIndex, assetVariant):
    directory = prsVariants.Database.assetMeshProduct
    dbBasic.saveDbMayaAscii(assetIndex, directory)


#
def dbAstUploadCfxProduct(assetIndex, assetVariant):
    dbCfxIndex = dbGet.getDbCfxIndex(assetIndex, assetVariant)
    directory = prsVariants.Database.assetGroomProduct
    dbBasic.saveDbMayaAscii(dbCfxIndex, directory)


#
def dbAstUploadFurProduct(assetIndex, assetVariant):
    dbCfxIndex = dbGet.getDbCfxIndex(assetIndex, assetVariant)
    directory = prsVariants.Database.assetFurProduct
    dbBasic.saveDbMayaAscii(dbCfxIndex, directory)


#
def dbAstUploadRigAssetIntegration(assetIndex):
    dbRigIndex = dbGet.getDbAstRigIndex(assetIndex)
    directory = prsVariants.Database.assetRigProduct
    dbBasic.saveDbMayaAscii(dbRigIndex, directory)


def dbAstCopyRigProductTo(assetIndex, targetFile):
    dbSubIndex = dbGet.getDbAstRigIndex(assetIndex)
    directory = prsVariants.Database.assetRigProduct
    asciiFile = directory + '/' + dbSubIndex
    if bscMethods.OsFile.isExist(asciiFile):
        bscMethods.OsFile.copyTo(asciiFile, targetFile)


# Nde_Geometry Load
def dbAstGeometryLoadMainCmd(assetIndex, assetName, lockTransform=True):
    objectIndexes = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
    if objectIndexes:
        dbAstLoadGeometryObjectsSub(assetIndex, assetName, objectIndexes, lockTransform)


#
def dbAstLoadGeometryObjectsSub(assetIndex, assetName, objectIndexes, lockTransform=True):
    if objectIndexes:
        progressExplain = u'''Load Database Nde_Geometry Object(s)'''
        #
        subProgressDataLis = [
            (True, u'''Transform''', dbAstLoadGeometryTransformSub, (assetIndex, objectIndexes, assetName, lockTransform)),
            #
            (True, u'''Shape''', dbAstLoadGeometryGeometrySub, (assetIndex, objectIndexes)),
            (True, u'''Map''', dbAstLoadGeometryMapSub, (assetIndex, objectIndexes)),
            #
            (True, u'''Edge - Smooth''', dbAstLoadGeometryEdgeSmoothSub, (assetIndex, objectIndexes))
        ]
        #
        qtCommands.setProgressRun(progressExplain, subProgressDataLis)
        #
        maGeom.setGeometryObjectsDefaultShadingEngine(objectIndexes)


#
def dbAstLoadGeometryTransformSub(assetIndex, objectIndexes, assetName, lockTransform):
    directory = prsVariants.Database.assetGeometryTransform
    dataDic = dbBasic.dbCompDatumDicRead(objectIndexes, assetIndex, directory)
    maGeom.setCreateObjectsTransform(dataDic, assetName, lockTransform)


#
def dbAstLoadGeometryGeometrySub(assetIndex, objectIndexes):
    geomTopoDir = prsVariants.Database.assetGeometryTopology
    geomShapeDir = prsVariants.Database.assetGeometryShape
    geomTopoDic = dbBasic.dbCompDatumDicRead(objectIndexes, assetIndex, geomTopoDir)
    geomShapeDic = dbBasic.dbCompDatumDicRead(objectIndexes, assetIndex, geomShapeDir)
    maGeom.setCreateGeometryObjectsShape((geomTopoDic, geomShapeDic))


#
def dbAstLoadGeometryMapSub(assetIndex, objectIndexes):
    directory = prsVariants.Database.assetGeometryMap
    dataDic = dbBasic.dbCompDatumDicRead(objectIndexes, assetIndex, directory)
    maGeom.setCreateGeometryObjectMap(dataDic)


#
def dbAstLoadGeometryEdgeSmoothSub(assetIndex, objectIndexes):
    directory = prsVariants.Database.assetGeometryEdgeSmooth
    dataDic = dbBasic.dbCompDatumDicRead(objectIndexes, assetIndex, directory)
    maGeom.setCreateGeometryObjectsEdgeSmooth(dataDic)


#
def dbAstLoadFurIndexSub(assetIndex, assetVariant):
    dbCfxIndex = dbGet.getDbCfxIndex(assetIndex, assetVariant)
    objectIndexes = dbGet.getDbCompFurIndexData(dbCfxIndex)
    #
    dbAstLoadFurCompIndex(dbCfxIndex, objectIndexes)


#
def dbAstLoadFurCompIndex(assetSubIndex, objectIndexes):
    # Mesh Nde_Geometry
    directory = prsVariants.Database.assetFurPath
    dataDic = dbBasic.dbCompDatumDicRead(objectIndexes, assetSubIndex, directory)
    maFur.setCreateFurObjectsUniqueId(dataDic)


# Nurbs Hair
def dbAstLoadNurbsHairMain(assetSubIndex):
    maUtils.setPlugLoad('nurbsHair')
    #
    objectIndexes = dbGet.getDbCompNurbsHairIndexData(assetSubIndex)
    if objectIndexes:
        progressExplain = u'''Load Database Asset Nurbs Hair'''
        #
        subProgressDataLis = [
            (True, u'''Graph ( Nde_Node )''', dbAstLoadNhrObjectsGraphNodeSub, (assetSubIndex, objectIndexes)),
            (True, u'''Graph ( Nde_Geometry )''', dbAstLoadNhrObjectsGraphGeometrySub, (assetSubIndex, objectIndexes)),
            (True, u'''Graph ( Relation )''', dbAstLoadNhrObjectsGraphRelationSub, (assetSubIndex, objectIndexes))
        ]
        #
        qtCommands.setProgressRun(progressExplain, subProgressDataLis)
        #
        maShdr.setObjectsDefaultShadingEngine(objectIndexes)
        maFur.setNurbsHairObjectsShowMode(objectIndexes, showMode=3)


#
def dbAstLoadNhrObjectsGraphNodeSub(assetSubIndex, objectIndexes):
    directory = prsVariants.Database.assetGraphNode
    dataDic = dbBasic.dbCompDatumDicRead(objectIndexes, assetSubIndex, directory)
    maFur.setCreateNurbsHairObjects(dataDic)


#
def dbAstLoadNhrObjectsGraphGeometrySub(assetSubIndex, objectIndexes):
    directory = prsVariants.Database.assetGraphGeometry
    dataDic = dbBasic.dbCompDatumDicRead(objectIndexes, assetSubIndex, directory)
    maFur.setCreateNhrObjectsGeometry(dataDic)


#
def dbAstLoadNhrObjectsGraphRelationSub(assetSubIndex, objectIndexes):
    directory = prsVariants.Database.assetGraphRelation
    dataDic = dbBasic.dbCompDatumDicRead(objectIndexes, assetSubIndex, directory)
    maFur.setCreateNhrObjectsRelation(dataDic)


#
def dbAstMaterialLoadMainCmd(assetSubIndex, compObjectIndexes, compMaterialIndexes):
    progressExplain = u'''Load Database Asset Material'''
    #
    subProgressDataLis = [
        (True, u'''Nde_Node''', dbAstMaterialCompNodesLoadCmd, (assetSubIndex, compMaterialIndexes)),
        (True, u'''Relation''', dbAstMaterialCompRelationsLoadCmd, (assetSubIndex, compMaterialIndexes)),
        (True, u'''Object - Attribute''', dbAstMaterialCompObjectAttrsLoadCmd, (assetSubIndex, compObjectIndexes)),
        (True, u'''Object - Set''', dbAstMaterialCompObjectSetsLoadCmd, (assetSubIndex, compObjectIndexes)),
    ]
    #
    qtCommands.setProgressRun(progressExplain, subProgressDataLis)
    maShdr.setObjectsDefaultShadingEngine(compObjectIndexes)


#
def dbAstMaterialCompNodesLoadCmd(assetSubIndex, compMaterialIndexes):
    directory = prsVariants.Database.assetMaterialNode
    dataDic = dbBasic.dbCompDatumDicRead(compMaterialIndexes, assetSubIndex, directory)
    maShdr.setCreateCompMaterialsNodes(dataDic)


#
def dbAstMaterialCompRelationsLoadCmd(assetSubIndex, compMaterialIndexes):
    directory = prsVariants.Database.assetMaterialRelation
    dataDic = dbBasic.dbCompDatumDicRead(compMaterialIndexes, assetSubIndex, directory)
    maShdr.setCreateMaterialsConnections(dataDic)


#
def dbAstMaterialCompObjectAttrsLoadCmd(assetIndex, compObjectIndexes):
    directory = prsVariants.Database.assetMaterialAttribute
    dataDic = dbBasic.dbCompDatumDicRead(compObjectIndexes, assetIndex, directory)
    maShdr.setObjectsAttrsCreate(dataDic)


# Material Object Set(s)
def dbAstMaterialCompObjectSetsLoadCmd(assetSubIndex, compObjectIndexes):
    directory = prsVariants.Database.assetMaterialObjectSet
    dataDic = dbBasic.dbCompDatumDicRead(compObjectIndexes, assetSubIndex, directory)
    maShdr.setMaterialsObjectSetsConnect(dataDic)


#
def dbAstLoadAov(renderer, assetSubIndex, dbAovCompIndexes):
    progressExplain = u'''Load Database Asset AOV'''
    #
    subProgressDataLis = [
        (True, u'''Nde_Node''', dbAstLoadAovCompNodes, (assetSubIndex, dbAovCompIndexes)),
        (True, u'''Relation''', dbAstLoadAovCompRelations, (assetSubIndex, dbAovCompIndexes))
    ]
    #
    qtCommands.setProgressRun(progressExplain, subProgressDataLis)


#
def dbAstLoadAovCompNodes(assetSubIndex, objectIndexes):
    directory = prsVariants.Database.assetAovNode
    dataDic = dbBasic.dbCompDatumDicRead(objectIndexes, assetSubIndex, directory)
    maShdr.setCreateCompAovsNodes(dataDic)


#
def dbAstLoadAovCompRelations(assetSubIndex, objectIndexes):
    directory = prsVariants.Database.assetAovRelation
    dataDic = dbBasic.dbCompDatumDicRead(objectIndexes, assetSubIndex, directory)
    maShdr.setCreateMaterialsConnections(dataDic)


#
def dbAstLoadFurIntegration(assetIndex, assetVariant):
    dbCfxIndex = dbGet.getDbCfxIndex(assetIndex, assetVariant)
    directory = prsVariants.Database.assetFurProduct
    dbBasic.importDbMayaAscii(dbCfxIndex, directory)


#
def dbAstLoadGeometryObjectsIndex(assetIndex, assetName, objectIndexes, mode=0):
    # Mesh Nde_Geometry
    directory = prsVariants.Database.assetGeometryTransform
    dataDic = dbBasic.dbCompDatumDicRead(objectIndexes, assetIndex, directory)
    if dataDic:
        # Path Mode
        if mode == 0:
            for uniqueId, dataDic in dataDic.items():
                parentPath, nodeName = dataDic[:2]
                parentPath = parentPath.replace('<assetName>', assetName)
                nodeName = nodeName.replace('<assetName>', assetName)
                #
                if parentPath.startswith('|'):
                    parentLocalPath = parentPath[1:]
                else:
                    parentLocalPath = parentPath
                #
                objectLocalPath = parentLocalPath + '|' + nodeName
                maUuid.setUniqueIdForce(objectLocalPath, uniqueId)
        # Name Mode
        elif mode == 1:
            nodeDic = {}
            for uniqueId, dataDic in dataDic.items():
                nodeName = dataDic[1]
                nodeName = nodeName.replace('<assetName>', assetName)
                nodeDic[nodeName] = uniqueId
            groupString = prsMethods.Asset.modelLinkGroupName(assetName)
            childPaths = maGeom.getGeometryObjectsByGroup(groupString)
            for objectPath in childPaths:
                objectName = maUtils._getNodeNameString(objectPath)
                if objectName in nodeDic:
                    uniqueId = nodeDic[objectName]
                    maUuid.setUniqueIdForce(objectPath, uniqueId)


#
def dbAstLoadMaterialCompIndex(assetSubIndex, objectIndexes):
    directory = prsVariants.Database.assetMaterialNode
    dataDic = dbBasic.dbCompDatumDicRead(objectIndexes, assetSubIndex, directory)
    maShdr.setCreateCompMaterialsUniqueId(dataDic)


#
def dbAstLoadModelProduct(assetIndex, assetName, assetVariant):
    dbModelIndex = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
    directory = prsVariants.Database.assetModelProduct
    # Debug Current Variant Non - Exists
    dbProductFile = directory + '/' + dbModelIndex
    if not bscMethods.OsFile.isExist(dbProductFile):
        dbModelIndex = dbGet.getDbAstModelIndex(assetIndex, prsVariants.Util.astDefaultVariant)
    #
    dbBasic.importDbMayaAscii(dbModelIndex, directory)
    #
    compMeshIndexes = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
    dbAstLoadGeometryObjectsIndex(assetIndex, assetName, compMeshIndexes)
    #
    compMaterialIndexes = dbGet.getDbMaterialIndexData(dbModelIndex)
    dbAstLoadMaterialCompIndex(dbModelIndex, compMaterialIndexes)


#
def dbAstLoadGeometryUnitsPath(assetIndex, assetName, objectIndexes, lockTransform=True):
    def setBranch(objectIndex):
        transformData = dbGet.getDbAstGeometryUnitTransform(assetIndex, objectIndex)
        if transformData:
            parentPath, objectName = transformData[:2]
            parentPath = parentPath.replace('<assetName>', assetName)
            objectName = objectName.replace('<assetName>', assetName)
            #
            if parentPath.startswith('|'):
                parentLocalPath = parentPath[1:]
            else:
                parentLocalPath = parentPath
            #
            objectLocalPath = parentLocalPath + '|' + objectName
            currentObjectPath = maUuid.getObject(objectIndex)
            if not maUtils._isNodeExist(objectLocalPath):
                if not maUtils._isNodeExist(parentLocalPath):
                    maUtils.setAppPathCreate(parentLocalPath, lockTransform)
                #
                maUtils.setObjectParent(currentObjectPath, parentLocalPath)
                maUtils.setObjectRename(currentObjectPath, objectName)
    #
    if objectIndexes:
        # View Progress
        progressExplain = u'''Load Database Nde_Geometry Object(s) Path'''
        maxValue = len(objectIndexes)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for i in objectIndexes:
            progressBar.update()
            setBranch(i)


#
def dbAstRemoveGeometryObjects(objectIndexes):
    def setBranch(objectIndex):
        objectStrings = maUuid.getObjects(objectIndex)
        if objectStrings:
            [maUtils.setNodeDelete(objectIndex) for objectIndex in objectStrings]
    #
    if objectIndexes:
        # View Progress
        progressExplain = u'''Remove Database Nde_Geometry Object(s)'''
        maxValue = len(objectIndexes)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for i in objectIndexes:
            progressBar.update()
            setBranch(i)


#
def refreshOutlineColor(objectIndexes, r, g, b):
    for i in objectIndexes:
        objects = maUuid.getObjects(i)
        if objects:
            [maUtils.setNodeOutlinerRgb(i, r, g, b) for i in objects]
