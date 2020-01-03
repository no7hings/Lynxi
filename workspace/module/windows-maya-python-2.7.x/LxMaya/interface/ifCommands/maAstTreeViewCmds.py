# encoding=utf-8
import os, collections
#
from LxCore import lxBasic, lxCore_
#
from LxCore.config import appCfg, assetCfg
#
from LxCore.preset import appVariant
#
from LxCore.preset.prod import assetPr
#
#
from LxUi.qt import qtWidgets_
#
from LxDatabase import dbGet
#
from LxMaya.command import maUtils, maUuid, maGeom, maTxtr, maFur
#
from LxMaya.product.data import datAsset
#
from LxMaya.database import maDbAstCmds
#
astPfxHairGroupLabel = appVariant.astPfxHairGroupLabel
astPfxHairGrowGroupLabel = appVariant.astPfxHairGrowGroupLabel
astPfxHairFollicleGroupLabel = appVariant.astPfxHairFollicleGroupLabel
astPfxHairCurveGroupLabel = appVariant.astPfxHairCurveGroupLabel
astPfxHairSolverNodeGroupLabel = appVariant.astPfxHairSolverNodeGroupLabel
astPfxHairNucleusNodeLabel = appVariant.astPfxHairNucleusNodeLabel
astPfxHairShaderNodeLabel = appVariant.astPfxHairShaderNodeLabel
#
astYetiGuideGroupLabel = appVariant.astYetiGuideGroupLabel
#
astYetiGuideSolverNodeGroupLabel = appVariant.astYetiGuideSolverNodeGroupLabel
astYetiGuideFollicleGroupLabel = appVariant.astYetiGuideFollicleGroupLabel
astYetiGuideCurveGroupLabel = appVariant.astYetiGuideCurveGroupLabel
astPfxHairLocalCurveNodeLabel = appVariant.astPfxHairLocalCurveNodeLabel
#
astYetiGuideSetNodeLabel = appVariant.astYetiGuideSetNodeLabel
astYetiGuideNucleusNodeLabel = appVariant.astYetiGuideNucleusNodeLabel
#
astCfxGrowSourceGroupLabel = appVariant.astCfxGrowSourceGroupLabel
astCfxFurGrowTargetGroupLabel = appVariant.astCfxFurGrowTargetGroupLabel
astCfxGrowDeformGroupLabel = appVariant.astCfxGrowDeformGroupLabel
astCfxFurCollisionSubGroupLabel = appVariant.astCfxFurCollisionSubGroupLabel
#
none = ''
txExt = '.tx'


#
def setObjectBranch(uiData, treeBox, objectPath, parentItem=None):
    objectName = maUtils._toNodeName(objectPath)
    objectType = maUtils.getShapeType(objectPath)
    objectUuid = maUuid.getNodeUniqueId(objectPath)
    #
    if objectUuid in uiData:
        objectItem = uiData[objectUuid]
        objectItem.setText(0, objectName)
        objectItem.name = objectName
        objectItem.path = objectPath
    else:
        objectItem = qtWidgets_.QTreeWidgetItem_([objectName, objectType])
        objectItem.name = objectName
        objectItem.path = objectPath
        objectItem.uuid = objectUuid
        if parentItem:
            parentItem.addChild(objectItem)
        else:
            treeBox.addItem(objectItem)
        #
        uiData[objectUuid] = objectItem
    #
    stateLabel = none
    objectItem.setItemMayaIcon(0, objectType, stateLabel)
    return objectItem


#
def setCheckObjectBranch(objectPath, parentItem=None):
    objectName = maUtils._toNodeName(objectPath)
    #
    objectType = maUtils.getShapeType(objectPath)
    objectUuid = maUuid.getNodeUniqueId(objectPath)
    #
    objectItem = qtWidgets_.QTreeWidgetItem_([objectName, objectType])
    objectItem.name = objectName
    objectItem.path = objectPath
    objectItem.uuid = objectUuid
    #
    if type(parentItem) == qtWidgets_.QTreeWidget_():
        parentItem.addItem(objectItem)
    else:
        parentItem.addChild(objectItem)
    #
    stateLabel = none
    objectItem.setItemMayaIcon(0, objectType, stateLabel)
    #
    return objectItem


#
def setCheckResult(main, enExplain, treeItem, checkData, errorData):
    if errorData:
        stateLabel = 'error'
        treeItem.setExpanded(True)
    else:
        stateLabel = 'on'
    #
    treeItem.setText(
        0, '%s [ %s / %s ]' % (enExplain, str(len(checkData) - len(errorData)).zfill(4), str(len(checkData)).zfill(4))
    )
    treeItem.setItemCheckIcon(0, 'svg_basic@svg#check', stateLabel)


#
def setAstHierarchyView(treeBox, root, searchDic=none, expandedDic=none):
    def setBranchView(treeItem):
        objectPath = treeItem.path
        objectName = treeItem.name
        #
        nodeType = maUtils.getShapeType(objectPath)
        treeItem.setText(1, maUtils.getNodeType(objectPath))
        #
        isParentExpanded = False
        if objectPath in expandedDic:
            isParentExpanded = expandedDic[objectPath]
        #
        treeItem.setItemMayaIcon(0, nodeType)
        #
        treeItem.setExpanded(isParentExpanded)
    #
    pathsep = appCfg.Ma_Separator_Node
    paths = maUtils.getChildrenByRoot(root)
    if not paths:
        rootItem = qtWidgets_.QTreeWidgetItem_([root])
        rootItem.path = root
        rootItem.name = root
        treeBox.addItem(rootItem)
        setBranchView(rootItem)
    #
    hierarchyData = treeBox.getGraphDatumDic(paths, pathsep)
    if hierarchyData:
        treeBox.setupGraph(hierarchyData, setBranchView, expandedDic)
    #
    treeBox.setFilterExplainRefresh()


#
def setAstGeometryConstantSub(
        treeBox,
        assetIndex,
        assetName, assetVariant,
        className, paths, uniqueIdDic, localInfoDic,
        serverInfoDic, expandedDic, meshItemDic
):
    def setBranchView(treeItem):
        # Menu Method
        def loadGeometryObject():
            objectIndexes = [compIndexKey]
            maDbAstCmds.dbAstRemoveGeometryObjects(objectIndexes)
            maDbAstCmds.dbAstLoadGeometryObjectsSub(assetIndex, assetName, objectIndexes)
        #
        def loadGeometryObjectPath():
            objectIndexes = [compIndexKey]
            maDbAstCmds.dbAstLoadGeometryUnitsPath(assetIndex, assetName, objectIndexes)
        #
        def enableReversePath():
            pass
        #
        def enableReverseMesh():
            print compIndexKey
        #
        def reverseMeshGeo():
            print compIndexKey
        #
        def reverseMeshGeoShape():
            if geomCheck:
                print compIndexKey
        #
        def reverseMeshMap():
            if geomCheck:
                print compIndexKey
        #
        def reverseMeshMapShape():
            if geomCheck and mapCheck:
                print compIndexKey
        #
        def removeGeometryObject():
            if maUtils.isAppExist(localObjectPath):
                maUtils.setNodeDelete(localObjectPath)
        #
        def addGeometryObject():
            objectIndexes = [compIndexKey]
            maDbAstCmds.dbAstLoadGeometryObjectsSub(assetIndex, assetName, objectIndexes)
        #
        def enableAddMesh():
            boolean = False
            maObj = maUuid.getObject(compIndexKey)
            if not maObj:
                boolean = True
            return boolean
        #
        objectName = treeItem.name
        objectPath = treeItem.path
        #
        isGeometryObject = objectPath in uniqueIdDic
        #
        if objectPath.startswith('|'):
            localObjectPath = objectPath[1:]
        else:
            localObjectPath = objectPath
        #
        treeItem.path = localObjectPath
        #
        if isGeometryObject:
            if maUtils.isAppExist(localObjectPath):
                objectType = maUtils.getShapeType(localObjectPath)
            else:
                objectType = appCfg.MaNodeType_Mesh
            #
            compIndexKey = uniqueIdDic[objectPath]
            #
            meshInfoCheck = getMeshInfoCheck(compIndexKey)
            pathCheck, geomCheck, geomShapeCheck, mapCheck, mapShapeCheck = meshInfoCheck
            #
            iconState = None
            if 'error' in meshInfoCheck:
                iconState = 'warning'
            #
            statusBar = qtWidgets_.xTreeLabelBar()
            statusBar.addItem('object#meshPath', pathCheck)
            statusBar.addItem('object#meshGeo', geomCheck)
            statusBar.addItem('object#meshGeoShape', geomShapeCheck)
            statusBar.addItem('object#meshMap', mapCheck)
            statusBar.addItem('object#meshMapShape', mapShapeCheck)
            #
            actionDatumLis = []
            if className == 'intersection':
                actionDatumLis.extend(
                    [
                        ('Reverse ( Mesh )', 'svg_basic@svg#undo', True, loadGeometryObject),
                        (),
                        ('Reverse ( Mesh ) Path', 'svg_basic@svg#undo', True, loadGeometryObjectPath),
                        ('Reverse ( Mesh ) Nde_Geometry', 'svg_basic@svg#undo', False, reverseMeshGeo),
                        ('Reverse ( Mesh ) Geom - Shape', 'svg_basic@svg#undo', False, reverseMeshGeoShape),
                        (),
                        ('Reverse ( Mesh ) Map', 'svg_basic@svg#undo', False, reverseMeshMap),
                        ('Reverse ( Mesh ) Map - Shape', 'svg_basic@svg#undo', False, reverseMeshMapShape)
                    ]
                )
            elif className == 'addition':
                actionDatumLis.extend(
                    [
                        ('Remove ( Mesh )', 'svg_basic@svg#delete', True, removeGeometryObject)
                    ]
                )
            elif className == 'deletion':
                actionDatumLis.extend(
                    [
                        ('Add ( Mesh )', 'svg_basic@svg#add', enableAddMesh, addGeometryObject)
                    ]
                )
            #
            treeItem.setItemWidget(1, statusBar)
            #
            treeItem.setText(2, compIndexKey)
            itemWidget = treeItem.setItemIconWidget(0, 'maya#out_{}'.format(objectType), objectName, iconState)
            itemWidget.setActionData(
                actionDatumLis
            )
            #
            meshItemDic[treeItem] = compIndexKey
        #
        else:
            treeItem.setItemMayaIcon(0, appCfg.MaNodeType_Transform)
            #
            treeItem.setExpanded(True)
    #
    def getHierarchyData():
        dic = collections.OrderedDict()
        pathsep = appCfg.Ma_Separator_Node
        subPaths = treeBox.getGraphPaths(paths, pathsep)
        hierarchyData = treeBox.getGraphDatumDic(subPaths, pathsep)
        for seq, (k, v) in enumerate(hierarchyData.items()):
            if seq == 0:
                dic[(className, className)] = v
            elif seq > 0:
                dic[k] = v
        return dic
    #
    def getMeshInfoCheck(compIndexKey):
        pathCheck = 'off'
        geomCheck = 'off'
        geomShapeCheck = 'off'
        mapCheck = 'off'
        mapShapeCheck = 'off'
        if localInfoDic and serverInfoDic:
            if compIndexKey in localInfoDic:
                isIntersection = compIndexKey in serverInfoDic
                if isIntersection:
                    localInfos = localInfoDic[compIndexKey]
                    serverInfos = serverInfoDic[compIndexKey]
                    pathCheck = getSubLabel(localInfos[0] == serverInfos[0])
                    geomCheck = getSubLabel(localInfos[1] == serverInfos[1])
                    geomShapeCheck = getSubLabel(localInfos[2] == serverInfos[2])
                    mapCheck = getSubLabel(localInfos[3] == serverInfos[3])
                    mapShapeCheck = getSubLabel(localInfos[4] == serverInfos[4])
        return pathCheck, geomCheck, geomShapeCheck, mapCheck, mapShapeCheck
    #
    def getSubLabel(checkResult):
        return ['error', 'on'][checkResult]
    #
    treeBox.setupGraph(getHierarchyData(), setBranchView, expandedDic, clearItemGraphDic=False)


#
def setAstGeometryConstantMain(
        main,
        treeBox,
        assetIndex,
        assetName, assetVariant,
        localPathDic, localInfoDic,
        serverPathDic, serverInfoDic
):
    def getUniqueDic(inData):
        dic = lxBasic.orderedDict()
        if inData:
            for k, v in inData.items():
                if not v.startswith('|'):
                    v = '|' + v
                dic[v] = k
        return dic
    #
    def getPaths():
        dic = {}
        #
        if localPathDic:
            for compIndexKey, compPath in localPathDic.items():
                if serverPathDic:
                    if compIndexKey in serverPathDic:
                        intersectionObjectIndexLis.append(compIndexKey)
                        dic.setdefault(classNames[0], []).append(compPath)
                    if not compIndexKey in serverPathDic:
                        additionObjectIndexLis.append(compIndexKey)
                        dic.setdefault(classNames[1], []).append(compPath)
                #
                if not serverPathDic:
                    additionObjectIndexLis.append(compIndexKey)
                    dic.setdefault(classNames[1], []).append(compPath)
        #
        if serverPathDic:
            for compIndexKey, compPath in serverPathDic.items():
                if not compIndexKey in localPathDic:
                    deletionObjectIndexLis.append(compIndexKey)
                    dic.setdefault(classNames[2], []).append(compPath)
        return dic
    #
    def setClassItemBranch(itemWidget, className, classState):
        def loadIntersectionGeometryObjects():
            if intersectionObjectIndexLis:
                maDbAstCmds.dbAstRemoveGeometryObjects(intersectionObjectIndexLis)
                #
                maDbAstCmds.dbAstLoadGeometryObjectsSub(assetIndex, assetName, intersectionObjectIndexLis)
        #
        def loadIntersectionGeometryObjectsPath():
            if intersectionObjectIndexLis:
                maDbAstCmds.dbAstLoadGeometryUnitsPath(assetIndex, assetName, intersectionObjectIndexLis)
        #
        def removeExtraGeometryObjects():
            if additionObjectIndexLis:
                maDbAstCmds.dbAstRemoveGeometryObjects(additionObjectIndexLis)
        #
        def uploadExtraGeometryObjects():
            if additionObjectIndexLis:
                pass
        #
        def addDeletionGeometryObjects():
            if deletionObjectIndexLis:
                maDbAstCmds.dbAstLoadGeometryObjectsSub(assetIndex, assetName, deletionObjectIndexLis)
        #
        actionData = []
        if className == 'intersection' and classState == none:
            actionData = [
                ('Load Nde_Geometry', 'menu#loadMenu', True, loadIntersectionGeometryObjects),
                (),
                ('Load Nde_Geometry ( Path )', 'menu#loadMenu', True, loadIntersectionGeometryObjectsPath)
            ]
        elif className == 'addition' and classState == none:
            actionData = [
                ('Remove Extra Nde_Geometry', 'menu#deleteMenu', True, removeExtraGeometryObjects),
                (),
                ('Upload Extra Nde_Geometry', 'uploadObject', False, uploadExtraGeometryObjects)
            ]
        elif className == 'deletion' and classState == none:
            actionData = [
                ('Add Deletion Nde_Geometry', 'menu#addMenu', True, addDeletionGeometryObjects)
            ]
        #
        itemWidget.setActionData(actionData)
        #
    #
    def setMain():
        maxValue = len(classNames)
        for seq, className in enumerate(classNames):
            main.setProgressValue(seq + 1, maxValue)
            classItem = qtWidgets_.QTreeWidgetItem_()
            treeBox.addItem(classItem)
            #
            classItem.setExpanded(True)
            classItem.path = className
            #
            treeItemGraphDic[className] = classItem
            classState = none
            #
            if className in pathDic:
                paths = pathDic[className]
                setAstGeometryConstantSub(
                    treeBox,
                    assetIndex, assetName, assetVariant,
                    className, paths, unionUniqueIdDic, localInfoDic,
                    serverInfoDic, expandedDic, meshItemDic
                )
            #
            elif not className in pathDic:
                classState = 'off'
            #
            classItemWidget = classItem.setItemIconWidget(
                0,
                'treeBox#{}'.format(className),
                lxBasic.str_camelcase2prettify(className),
                classState
            )
            setClassItemBranch(classItemWidget, className, classState)
    #
    classNames = ['intersection', 'addition', 'deletion']
    #
    localUniqueDic = getUniqueDic(localPathDic)
    serverUniqueDic = getUniqueDic(serverPathDic)
    #
    unionUniqueIdDic = localUniqueDic.copy()
    unionUniqueIdDic.update(serverUniqueDic)
    #
    intersectionObjectIndexLis = []
    additionObjectIndexLis = []
    deletionObjectIndexLis = []
    #
    pathDic = getPaths()
    #
    treeItemGraphDic = treeBox.itemGraphDic()
    expandedDic = treeBox.getGraphExpandDic()
    #
    meshItemDic = collections.OrderedDict()
    #
    treeBox.clear()
    treeBox.clearGraphDic()
    setMain()
    #
    treeBox.setFilterExplainRefresh()


#
def setAstMeshTopoConstantView(treeBox, assetIndex, assetName, assetNamespace=none):
    def setBranchView(treeItem):
        objectName = treeItem.name
        objectPath = treeItem.path
        #
        isMesh = objectPath in serverMeshes
        #
        if isMesh:
            treeItem.setItemMayaIcon(0, 'list')
            #
            treeItem.setText(0, objectName + endKey)
            compIndexKey = serverIndexKeyDic[objectPath]
            #
            treeItem.setText(1, compIndexKey)
            #
            constantKey = serverTopoConstantDic[objectPath]
            setBranchTopoConstant(treeItem, compIndexKey, constantKey)
        #
        elif not isMesh:
            treeItem.setItemMayaIcon(0, appCfg.MaNodeType_Transform)
            #
            treeItem.setExpanded(True)
    #
    def setBranchTopoConstant(treeItem, compIndexKey, constantKey):
        if constantKey in localTopoConstantDic:
            matchLocalMeshes = localTopoConstantDic[constantKey]
            if matchLocalMeshes:
                for localMeshPath in matchLocalMeshes:
                    localMeshName = maUtils._toNodeName(localMeshPath)
                    localMeshItem = qtWidgets_.QTreeWidgetItem_([localMeshName])
                    #
                    treeItem.addChild(localMeshItem)
                    treeItem.setExpanded(True)
                    #
                    localMeshItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh)
                    #

                    localMeshUniqueId = maUuid.getNodeUniqueId(localMeshPath)
                    localMeshItem.setText(1, localMeshUniqueId)
                    if localMeshUniqueId == compIndexKey:
                        stateLabel = 'on'
                    else:
                        stateLabel = 'off'
                    #
                    treeItem.setItemMayaIcon(0, 'list', stateLabel)
    #
    def getDatas():
        if serverInfoDic:
            for k, v in serverInfoDic.items():
                objectPath = serverPathDic[k]
                if not objectPath.startswith('|'):
                    objectPath = '|' + objectPath
                #
                serverMeshes.append(objectPath)
                serverIndexKeyDic[objectPath] = k
                serverInfoDic[objectPath] = v
                serverTopoConstantDic[objectPath] = v[1]
    #
    serverMeshes = []
    serverIndexKeyDic = {}
    serverInfoDic = {}
    serverTopoConstantDic = {}
    #
    endKey = ' ( Data - Base )'
    root = assetPr.astUnitModelLinkGroupName(assetName, assetNamespace)
    #
    serverInfoDic = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
    serverPathDic = dbGet.getDbGeometryUnitsPathDic(assetIndex)
    # Get Data
    getDatas()
    #
    localTopoConstantDic = maGeom.getMeshesTopoConstantData(root)
    #
    treeBox.clear()
    if serverMeshes:
        pathsep = appCfg.Ma_Separator_Node
        subPaths = treeBox.getGraphPaths(serverMeshes, pathsep)
        graphDatumDic = treeBox.getGraphDatumDic(subPaths, pathsep)
        if graphDatumDic:
            treeBox.setupGraph(graphDatumDic, setBranchView)
    #
    treeBox.setFilterExplainRefresh()


#
def setAstMeshGeomCheckView(main, treeBox, inData, checkData, errorData):
    tempErrorData = []
    checkConfig = assetCfg.astMeshGeomCheckConfig()
    maxValue = len(checkConfig)
    for seq, (k, v) in enumerate(checkConfig.items()):
        main.setProgressValue(seq + 1, maxValue)
        #
        enabled, enExplain, cnExplain = v[:3]
        if enabled is not False:
            inspectionItem = qtWidgets_.QTreeWidgetItem_([enExplain, cnExplain])
            treeBox.addItem(inspectionItem)
            if enabled is True:
                inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check')
                if inData:
                    if k in inData:
                        subErrorData = inData[k]
                        if subErrorData:
                            inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'error')
                            inspectionItem.setExpanded(True)
                            for meshPath, compPaths in subErrorData.items():
                                meshName = maUtils._toNodeName(meshPath)
                                #
                                meshItem = qtWidgets_.QTreeWidgetItem_([meshName])
                                meshItem.path = meshPath
                                meshItem.name = meshName
                                inspectionItem.addChild(meshItem)
                                #
                                meshItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh)
                                #
                                if compPaths:
                                    tempErrorData.append(meshPath)
                                    #
                                    meshItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh, 'error')
                                    meshItem.setExpanded(True)
                                    for compPath in compPaths:
                                        compName = maUtils._toNodeName(compPath)
                                        #
                                        compItem = qtWidgets_.QTreeWidgetItem_([compName])
                                        compItem.path = compPath
                                        compItem.name = compName
                                        #
                                        compItem.setItemMayaIcon(0, 'dagNode', 'error')
                                        meshItem.addChild(compItem)
                        else:
                            inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'on')
            else:
                inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'off')
    #
    [errorData.append(i) for i in tempErrorData if i not in errorData]
    #
    treeBox.setFilterExplainRefresh()


#
def setAstMeshTransCheckView(main, treeBox, inData, checkData, errorData):
    enExplain = 'Mesh Transformation Checking'
    cnExplain = u'确认模型不存在错误的位移，旋转，缩放'
    #
    tempErrorData = []
    #
    inspectionItem = qtWidgets_.QTreeWidgetItem_([enExplain, cnExplain])
    inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check')
    treeBox.addItem(inspectionItem)
    if inData:
        maxValue = len(inData)
        for seq, (k, v) in enumerate(inData.items()):
            main.setProgressValue(seq + 1, maxValue)
            #
            meshPath = k
            meshName = maUtils._toNodeName(meshPath)
            #
            meshItem = qtWidgets_.QTreeWidgetItem_([meshName])
            meshItem.path = meshPath
            meshItem.name = meshName
            meshItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh)
            #
            isTransError = False
            for ik, iv in v.items():
                xValue, yValue, zValue = iv
                transItem = qtWidgets_.QTreeWidgetItem_([lxBasic.str_camelcase2prettify(ik), str(xValue), str(yValue), str(zValue)])
                transItem.setItemMayaIcon(0, 'dagNode')
                meshItem.addChild(transItem)
                if ik in ['translate', 'rotate', 'pivot']:
                    if sum(iv) != 0:
                        isTransError = True
                        transItem.setItemMayaIcon(0, 'dagNode', 'error')
                if ik in ['scale']:
                    if sum(iv) != 3:
                        isTransError = True
                        transItem.setItemMayaIcon(0, 'dagNode', 'error')
            if isTransError is True:
                tempErrorData.append(meshPath)
                #
                inspectionItem.addChild(meshItem)
                meshItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh, 'error')
                meshItem.setExpanded(True)
        #
        if tempErrorData:
            inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'error')
            inspectionItem.setExpanded(True)
        elif not tempErrorData:
            inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'On')
    else:
        inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'off')
    #
    [errorData.append(i) for i in tempErrorData if i not in errorData]
    #
    treeBox.setFilterExplainRefresh()


#
def setAstMeshHistCheckView(main, treeBox, inData, inCheck, errorData):
    enExplain = 'Mesh History Checking'
    cnExplain = u'''确认模型不存在多余的历史记录'''
    #
    tempErrorData = []
    inData = datAsset.filterObjectHistoryNodeDic(inCheck)
    inspectionItem = qtWidgets_.QTreeWidgetItem_([enExplain, cnExplain])
    inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check')
    treeBox.addItem(inspectionItem)
    if inData:
        maxValue = len(inData)
        for seq, (k, v) in enumerate(inData.items()):
            main.setProgressValue(seq + 1, maxValue)
            #
            meshPath = k
            meshName = maUtils._toNodeName(meshPath)
            #
            meshItem = qtWidgets_.QTreeWidgetItem_([meshName, appCfg.MaNodeType_Transform])
            meshItem.path = meshPath
            meshItem.name = meshName
            meshItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh)
            #
            isHistError = False
            if v:
                for i in v:
                    histNodePath, nodeType = i
                    histNodeName = maUtils._toNodeName(histNodePath)
                    #
                    histNodeItem = qtWidgets_.QTreeWidgetItem_([histNodeName, nodeType])
                    histNodeItem.path = histNodePath
                    histNodeItem.name = histNodeName
                    meshItem.addChild(histNodeItem)
                    histNodeItem.setItemMayaIcon(0, nodeType)
                    if nodeType == 'mesh':
                        histNodeItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh)
                        meshItem.addChild(histNodeItem)
                    elif nodeType == 'shadingEngine':
                        meshItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh, 'warning')
                        histNodeItem.setItemMayaIcon(0, nodeType, 'warning')
                    elif nodeType == 'groupId':
                        meshItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh, 'warning')
                        histNodeItem.setItemMayaIcon(0, nodeType, 'warning')
                    else:
                        isHistError = True
                        histNodeItem.setItemMayaIcon(0, nodeType, 'error')
                #
                if isHistError is True:
                    tempErrorData.append(meshPath)
                    #
                    meshItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh, 'error')
                    inspectionItem.addChild(meshItem)
                    meshItem.setExpanded(True)
        #
        if tempErrorData:
            inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'error')
            inspectionItem.setExpanded(True)
        elif not tempErrorData:
            inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'On')
    #
    else:
        inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'Off')
    #
    [errorData.append(i) for i in tempErrorData if i not in errorData]
    #
    treeBox.setFilterExplainRefresh()


#
def setAstCfxFurCheckTreeView(main, assetClass, assetName, treeBox, checkData, errorData):
    checkFnDic = lxBasic.orderedDict()
    checkFnDic['astYetiCheck'] = setAstCfxFurYetiCheckTreeView
    checkFnDic['astPfxHairCheck'] = setAstCfxFurMayaCheckTreeView
    checkFnDic['astNurbsHairCheck'] = setAstCfxFurNhrCheckTreeView
    checkFnDic['astGrowSourceCheck'] = setAstCfxGrowSourceCheckView
    checkFnDic['astSolverGuideCheck'] = setAstCfxSolverGuideCheckView
    checkConfig = assetCfg.astCfxGroomCheckConfig()
    if checkConfig:
        for k, v in checkConfig.items():
            enable, enExplain, cnExplain = v
            if enable is not False:
                if k in checkFnDic:
                    fn = checkFnDic[k]
                    fn(main, assetClass, assetName, treeBox, checkData, errorData)


#
def setAstCfxFurYetiCheckTreeView(main, assetClass, assetName, treeBox, checkData, errorData):
    enExplain = 'Yeti Check'
    inspectionItem = qtWidgets_.QTreeWidgetItem_(['%s [ 0000 / 0000 ]' % enExplain])
    inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check')
    treeBox.addItem(inspectionItem)
    #
    inData = datAsset.getYetiObjects(assetName)
    inData.sort()
    if inData:
        maxValue = len(inData)
        for seq, yetiObject in enumerate(inData):
            main.setProgressValue(seq + 1, maxValue)
            showName = yetiObject.split('|')[-1]
            isChecked = True
            yetiItem = qtWidgets_.QTreeWidgetItem_([showName, appCfg.MaNodeType_Plug_Yeti])
            yetiItem.setItemMayaIcon(0, appCfg.MaNodeType_Plug_Yeti)
            #
            inspectionItem.addChild(yetiItem)
            #
            rootNode = maFur.getYetiRootNode(yetiObject)
            if not rootNode:
                isChecked = False
                yetiItem.setItemMayaIcon(0, appCfg.MaNodeType_Plug_Yeti, 'error')
                yetiItem.setText(2, 'Root Nde_Node is Non - Exists')
            # Groom
            groomObjects = maUtils.getYetiGroomDic(yetiObject)
            if groomObjects:
                for groomObject in groomObjects:
                    groomItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(groomObject), 'Groom'])
                    groomItem.setItemMayaIcon(0, appCfg.MaNodeType_YetiGroom)
                    #
                    groomObjectGroup = assetPr.astBasicGroupNameSet(assetName, appVariant.astYetiGroomGroupLabel)
                    #
                    if not maUtils.isChild(groomObjectGroup, groomObject):
                        isChecked = False
                        groomItem.setText(2, 'Non - Collection')
                        groomItem.setItemMayaIcon(0, appCfg.MaNodeType_YetiGroom, 'error')
                    #
                    if not maUtils.isAppExist(groomObject):
                        isChecked = False
                        groomItem.setText(2, 'Non - Exists')
                        groomItem.setItemMayaIcon(0, appCfg.MaNodeType_YetiGroom, 'error')
                    #
                    yetiItem.addChild(groomItem)
            # Grow
            growObjects = maUtils.getYetiGrowDic(yetiObject)
            if growObjects:
                growStateLabel = none
                for growObject in growObjects:
                    growItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(growObject), 'Grow'])
                    yetiItem.addChild(growItem)
                    #
                    growObjectGroup = \
                        assetPr.astBasicGroupNameSet(assetName, appVariant.astYetiGrowGroupLabel)
                    #
                    if not maUtils.isChild(growObjectGroup, growObject):
                        isChecked = False
                        growStateLabel = 'error'
                        growItem.setText(2, 'Non - Collection')
                    #
                    if not maUtils.isAppExist(growObject):
                        isChecked = False
                        growStateLabel = 'error'
                        growItem.setText(2, 'Non - Exists')
                    #
                    if maGeom.getMeshObjectIsNormalLocked(growObject):
                        isChecked = False
                        growStateLabel = 'error'
                        growItem.setText(2, 'Locked - Normal')
                    #
                    growItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh, growStateLabel)
                    # Reference
                    referenceObjects = maUtils.getYetiRefObject(growObject)
                    if referenceObjects:
                        for referenceObject in referenceObjects:
                            referenceItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(referenceObject), 'Reference Object'])
                            referenceItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh)
                            #
                            referenceObjectGroup = \
                                assetPr.astBasicGroupNameSet(assetName, appVariant.astYetiReferenceGroupLabel)
                            if not maUtils.isChild(referenceObjectGroup, referenceObject):
                                isChecked = False
                                referenceItem.setText(2, 'Non - Collection')
                                referenceItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh, 'error')
                            #
                            growItem.addChild(referenceItem)
            # Map
            osImageFileLis = maUtils.getYetiMapDic(yetiObject)
            if osImageFileLis:
                for osImageFile in osImageFileLis:
                    mapName = os.path.basename(osImageFile)
                    mapItem = qtWidgets_.QTreeWidgetItem_([mapName, 'Map'])
                    mapItem.setItemMayaIcon(0, appCfg.MaTextureNodeType)
                    #
                    yetiItem.addChild(mapItem)
                    #
                    if not maTxtr.isOsTextureExist(osImageFile):
                        isChecked = False
                        mapItem.setText(2, 'Non - Exists')
                        mapItem.setItemMayaIcon(0, appCfg.MaTextureNodeType, 'error')
            #
            guideSystems = []
            guideNuclei = []
            guideSets = maUtils.getYetiGuideSetDic(yetiObject)
            guideData = maUtils.getYetiGuideData(yetiObject)
            #
            guideSystemGroup = None
            if guideSets:
                guideSystemGroup = \
                    assetPr.guideSystemGroupName(assetName)
                #
                follicleGroup = \
                    assetPr.guideFollicleGroupName(assetName)
                #
                guideCurveGroup = \
                    assetPr.guideCurveGroupName(assetName)
                for guideSet in guideSets:
                    guideSetItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(guideSet), 'Guide Set'])
                    guideSetItem.setItemMayaIcon(0, 'list')
                    #
                    yetiItem.addChild(guideSetItem)
                    #
                    guideCheck = True
                    guideCheckExplain = none
                    #
                    if not maUtils.isAppExist(guideSet):
                        isChecked = False
                        guideCheck = False
                        guideCheckExplain = 'Non - Exists'
                    #
                    if guideSet in guideData:
                        data = guideData[guideSet]
                        for k, v in data.items():
                            guideCurve = k
                            #
                            guideCurveItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(guideCurve), 'Guide Curve'])
                            guideCurveItem.setItemMayaIcon(0, appCfg.MaNodeType_NurbsCurve)
                            #
                            if not maUtils.isChild(guideCurveGroup, guideCurve):
                                isChecked = False
                                guideCheck = False
                                guideCheckExplain = 'Non - Collection'
                                #
                                guideCurveItem.setText(2, 'Non - Collection')
                                guideCurveItem.setItemMayaIcon(0, appCfg.MaNodeType_NurbsCurve, 'error')
                            #
                            guideSetItem.addChild(guideCurveItem)
                            #
                            follicle, localCurve, hairSystem, nucleus = v
                            #
                            if follicle:
                                follicleItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(follicle), 'Follicle'])
                                follicleItem.setItemMayaIcon(0, appCfg.MaFollicleType)
                                guideCurveItem.addChild(follicleItem)
                                #
                                if not maUtils.isChild(follicleGroup, follicle):
                                    isChecked = False
                                    guideCheck = False
                                    guideCheckExplain = 'Non - Collection'
                                    #
                                    follicleItem.setText(2, 'Non - Collection')
                                    follicleItem.setItemMayaIcon(0, appCfg.MaFollicleType, 'error')
                                    #
                                    guideCurveItem.setExpanded(True)
                            #
                            if localCurve:
                                localCurveItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(localCurve), 'Local Curve'])
                                localCurveItem.setItemMayaIcon(0, appCfg.MaNodeType_NurbsCurve)
                                guideCurveItem.addChild(localCurveItem)
                                #
                                if not maUtils.isChild(follicleGroup, localCurve):
                                    isChecked = False
                                    guideCheck = False
                                    guideCheckExplain = 'Non - Collection'
                                    #
                                    localCurveItem.setText(2, 'Non - Collection')
                                    localCurveItem.setItemMayaIcon(0, appCfg.MaNodeType_NurbsCurve, 'error')
                                    #
                                    guideCurveItem.setExpanded(True)
                            #
                            if hairSystem:
                                guideSystems.append(hairSystem)
                            #
                            if nucleus:
                                guideNuclei.append(nucleus)
                    #
                    if not guideCheck:
                        guideSetItem.setText(2, guideCheckExplain)
                        guideSetItem.setItemMayaIcon(0, 'list', 'error')
                        #
                        guideSetItem.setExpanded(True)
            #
            if guideSystems:
                guideSystems = maUtils.getReduceList(guideSystems)
                for guideSystem in guideSystems:
                    guideSystemItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(guideSystem), 'Guide System'])
                    guideSystemItem.setItemMayaIcon(0, appCfg.MaHairSystemType)
                    yetiItem.addChild(guideSystemItem)
                    #
                    if not maUtils.isChild(guideSystemGroup, guideSystem):
                        isChecked = False
                        #
                        guideSystemItem.setText(2, 'Non - Collection')
                        guideSystemItem.setItemMayaIcon(0, appCfg.MaHairSystemType, 'error')
                    #
                    solverMode = maFur.getHairSystemSolverMode(guideSystem)
                    if not solverMode == 'Static':
                        isChecked = False
                        #
                        guideSystemItem.setText(2, 'Solver - Mode Error')
                        guideSystemItem.setItemMayaIcon(0, appCfg.MaHairSystemType, 'error')
            #
            if guideNuclei:
                guideNuclei = maUtils.getReduceList(guideNuclei)
                for guideNucleus in guideNuclei:
                    guideNucleusItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(guideNucleus), 'Guide Nucleus'])
                    guideNucleusItem.setItemMayaIcon(0, appCfg.MaNucleusType)
                    yetiItem.addChild(guideNucleusItem)
                    #
                    if not maUtils.isChild(guideSystemGroup, guideNucleus):
                        isChecked = False
                        #
                        guideNucleusItem.setText(2, 'Non - Collection')
                        guideNucleusItem.setItemMayaIcon(0, appCfg.MaNucleusType, 'error')
            #
            if not isChecked:
                yetiItem.setItemMayaIcon(0, appCfg.MaNodeType_Plug_Yeti, 'error')
                yetiItem.setExpanded(True)
                errorData.append(yetiObject)
            checkData.append(yetiObject)
        #
        setCheckResult(main, enExplain, inspectionItem, checkData, errorData)
    elif not inData:
        inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'Off')
    #
    treeBox.setFilterExplainRefresh()


#
def setAstCfxFurMayaCheckTreeView(main, assetClass, assetName, treeBox, checkData, errorData):
    # Sub Method
    def setCheckBranch(pfxHairObject, errorArray):
        def setCheckLeaf(mObjects, rootItem, explain, nodeType, objectGroup, subErrorArray, subRootItem=False):
            notInGroup = []
            #
            if subRootItem:
                subRootItem = qtWidgets_.QTreeWidgetItem_([explain, 'Nodes'])
                subRootItem.setItemMayaIcon(0, 'list')
                rootItem.addChild(subRootItem)
            #
            for maObj in mObjects:
                showObject = maUtils._toNodeName(maObj)
                objectItem = qtWidgets_.QTreeWidgetItem_([showObject, explain])
                objectItem.setItemMayaIcon(0, nodeType)
                #
                if subRootItem:
                    subRootItem.addChild(objectItem)
                #
                if not subRootItem:
                    rootItem.addChild(objectItem)
                #
                subCheck = True
                # is In - Group
                boolean = maUtils.isChild(objectGroup, maObj)
                #
                if not boolean:
                    subCheck = False
                    subErrorArray.append(objectItem)
                    notInGroup.append(objectItem)
                    objectItem.setText(2, 'Non - Collection')
                # is Enable Solver
                if nodeType == 'hairSystem':
                    solverMode = maFur.getHairSystemSolverMode(maObj)
                    if not solverMode == 'Static':
                        subCheck = False
                        subErrorArray.append(objectItem)
                        notInGroup.append(objectItem)
                        objectItem.setText(2, 'Solver - Mode Error')
                #
                objectItem.setItemMayaIcon(0, nodeType, ['error', none][subCheck])
            #
            if subRootItem:
                subRootBoolean = notInGroup == []
                subRootItem.setItemMayaIcon(0, 'list', ['error', none][subRootBoolean])
        # Pfx Hair
        subErrorArray = []
        showPfxHairObject = maUtils._toNodeName(pfxHairObject)
        pfxHairItem = qtWidgets_.QTreeWidgetItem_([showPfxHairObject, 'Pfx Hair'])
        inspectionItem.addChild(pfxHairItem)
        pfxHairItem.setItemMayaIcon(0, appCfg.MaPfxHairType)
        growObjects, shaders, textures, maps, systemObjects, nucleusObjects, follicleData = maUtils.getPfxHairConnectionData(pfxHairObject)
        # Grow
        if growObjects:
            growGroup = assetPr.astBasicGroupNameSet(assetName, appVariant.astPfxHairGrowGroupLabel)
            setCheckLeaf(growObjects, pfxHairItem, 'Grow', 'poly', growGroup, subErrorArray)
        # Nde_ShaderRef
        if shaders:
            for shader in shaders:
                shaderItem = qtWidgets_.QTreeWidgetItem_([shader, 'Nde_ShaderRef'])
                pfxHairItem.addChild(shaderItem)
                shaderItem.setItemMayaIcon(0, 'lambert')
        # Texture
        if textures:
            for texture in textures:
                textureItem = qtWidgets_.QTreeWidgetItem_([texture, 'Texture'])
                pfxHairItem.addChild(textureItem)
                textureItem.setItemMayaIcon(0, appCfg.MaTextureNodeType)
        # Map
        if maps:
            for mapNode in maps:
                mapItem = qtWidgets_.QTreeWidgetItem_([mapNode, 'Map'])
                pfxHairItem.addChild(mapItem)
                mapItem.setItemMayaIcon(0, 'checker')
                map = maTxtr.getTextureNodeAttrData(mapNode)
                boolean = os.path.isfile(map)
                mapItem.setItemMayaIcon(0, 'checker', ['error', none][boolean])
                if not boolean:
                    subErrorArray.append(mapItem)
                    mapItem.setText(2, 'Non - Exists')
        # System
        if systemObjects:
            systemGroup = assetPr.astBasicGroupNameSet(assetName, astPfxHairSolverNodeGroupLabel)
            setCheckLeaf(systemObjects, pfxHairItem, 'System', 'hairSystem', systemGroup, subErrorArray)
        # Nucleus
        if nucleusObjects:
            nucleusGroup = assetPr.astBasicGroupNameSet(assetName, astPfxHairSolverNodeGroupLabel)
            setCheckLeaf(nucleusObjects, pfxHairItem, 'Nucleus', 'nucleus', nucleusGroup, subErrorArray)
        # Follicle
        if follicleData:
            follicleObjects = []
            localCurveObjects = []
            outputCurveObjects = []
            for follicleObject, (subLocalCurveObjects, subOutputCurveObjects) in follicleData.items():
                follicleObjects.append(follicleObject)
                localCurveObjects.extend(subLocalCurveObjects)
                outputCurveObjects.extend(subOutputCurveObjects)
            if follicleObjects:
                follicleGroup = assetPr.astBasicGroupNameSet(assetName, astPfxHairFollicleGroupLabel)
                setCheckLeaf(follicleObjects, pfxHairItem, 'Follicle', 'follicle', follicleGroup, subErrorArray,  subRootItem=True)
            if localCurveObjects:
                localCurveGroup = assetPr.astBasicGroupNameSet(assetName, astPfxHairFollicleGroupLabel)
                setCheckLeaf(localCurveObjects, pfxHairItem, 'Local Curve', 'inputCurve', localCurveGroup, subErrorArray, subRootItem=True)
            if outputCurveObjects:
                outputCurveGroup = assetPr.astBasicGroupNameSet(assetName, astPfxHairCurveGroupLabel)
                setCheckLeaf(outputCurveObjects, pfxHairItem, 'Output Curve', 'outputCurve', outputCurveGroup, subErrorArray,  subRootItem=True)
        #
        isChecked = subErrorArray == []
        pfxHairItem.setItemMayaIcon(0, appCfg.MaPfxHairType, ['error', none][isChecked])
        if not isChecked:
            pfxHairItem.setExpanded(True)
            errorArray.append(pfxHairItem)
    # Check
    enExplain = 'Pfx - Hair Check'
    inspectionItem = qtWidgets_.QTreeWidgetItem_(['%s [ 0000 / 0000 ]' % enExplain])
    inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check')
    treeBox.addItem(inspectionItem)
    inData = datAsset.getPfxHairObjects(assetName)
    if inData:
        maxValue = len(inData)
        for seq, pfxHairObject in enumerate(inData):
            main.setProgressValue(seq + 1, maxValue)
            #
            setCheckBranch(pfxHairObject, errorData)
            #
            checkData.append(pfxHairObject)
        setCheckResult(main, enExplain, inspectionItem, checkData, errorData)
    elif not inData:
        inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'Off')
    #
    treeBox.setFilterExplainRefresh()


#
def setAstCfxFurNhrCheckTreeView(main, assetClass, assetName, treeBox, checkData, errorData):
    # Sub Method
    def setObjectCheckBranch(objectPath, iconKeyword, parentItem=None):
        objectName = maUtils._toNodeName(objectPath)
        objectType = maUtils.getShapeType(objectPath)
        objectUuid = maUuid.getNodeUniqueId(objectPath)
        #
        objectItem = qtWidgets_.QTreeWidgetItem_([objectName, objectType])
        if parentItem:
            parentItem.addChild(objectItem)
        else:
            treeBox.addItem(objectItem)
        #
        stateLabel = none
        if not astCfxRoot in objectPath:
            stateLabel = 'error'
            objectItem.setText(2, 'Non - Collection')
            #
            isChecked = False
        else:
            isChecked = True
        #
        objectItem.setItemMayaIcon(0, objectType, stateLabel)
        #
        objectItem.name = objectName
        objectItem.path = objectPath
        objectItem.uuid = objectUuid
        #
        return objectItem, isChecked
    #
    def setMapCheckBranch(node, iconKeyword, parentItem=None):
        nodeName = node
        nodeType = maUtils.getNodeType(node)
        nodeUuid = maUuid.getNodeUniqueId(node)
        nodeItem = qtWidgets_.QTreeWidgetItem_([nodeName, nodeType])
        if parentItem:
            parentItem.addChild(nodeItem)
        else:
            treeBox.addItem(nodeItem)
        #
        stateLabel = none
        furMapFile = maFur.getFurMapAttrData(node)
        if not lxBasic.isOsExistsFile(furMapFile):
            stateLabel = 'error'
            nodeItem.setText(2, 'Non - Exists')
            #
            isChecked = False
        else:
            isChecked = True
        #
        nodeItem.setItemMayaIcon(0, nodeType, stateLabel)
        #
        nodeItem.name = nodeName
        nodeItem.path = node
        nodeItem.uuid = nodeUuid
        #
        return nodeItem, isChecked
    #
    def setMain():
        inspectionItem = qtWidgets_.QTreeWidgetItem_(['%s [ 0000 / 0000 ]' % enExplain])
        inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check')
        treeBox.addItem(inspectionItem)
        nurbsHairObjects = datAsset.getAstCfxNurbsHairObjects(assetName)
        if nurbsHairObjects:
            maxValue = len(nurbsHairObjects)
            for seq, objectPath in enumerate(nurbsHairObjects):
                main.setProgressValue(seq + 1, maxValue)
                #
                parentItem, isChecked = setObjectCheckBranch(objectPath, 'treeBox#nurbsHair', parentItem=inspectionItem)
                graphObjects, graphNodes, graphGrowMeshes, graphGuideMeshes = maFur.getNurbsHairConnectObjectData(objectPath)
                mapNodes = maFur.getNurbsHairMapNodes(objectPath)
                checkExplain = none
                if graphObjects:
                    if len(graphObjects) >= 1:
                        subErrors = []
                        #
                        childObjects = graphObjects
                        childObjects.extend(graphGrowMeshes)
                        childObjects.extend(graphGuideMeshes)
                        if childObjects:
                            for childObjectPath in childObjects:
                                childItem, isSubChecked = setObjectCheckBranch(
                                    childObjectPath,
                                    'treeBox#transform',
                                    parentItem=parentItem
                                )
                                if isSubChecked is False:
                                    subErrors.append(childObjectPath)
                        #
                        if mapNodes:
                            for node in mapNodes:
                                childItem, isSubChecked = setMapCheckBranch(
                                    node,
                                    'treeBox#node',
                                    parentItem
                                )
                                #
                                if isSubChecked is False:
                                    subErrors.append(node)
                        #
                        isChecked = [False, True][subErrors == []]
                        if isChecked is False:
                            checkExplain = 'Non - Collection'
                    else:
                        isChecked = False
                        checkExplain = 'Non - Guide'
                else:
                    isChecked = False
                    checkExplain = 'Non - Guide'
                #
                checkData.append(objectPath)
                #
                if isChecked is False:
                    parentItem.setText(2, checkExplain)
                    parentItem.setItemMayaIcon(0, appCfg.MaNodeType_Plug_NurbsHair, 'error')
                    parentItem.setExpanded(True)
                    errorData.append(objectPath)
            #
            setCheckResult(main, enExplain, inspectionItem, checkData, errorData)
        elif not nurbsHairObjects:
            inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'Off')
        #
        treeBox.setFilterExplainRefresh()
    #
    enExplain = 'Nurbs - Hair Check'
    astCfxRoot = assetPr.astUnitCfxLinkGroupName(assetName)
    #
    setMain()


#
def setAstCfxGrowSourceCheckView(main, assetClass, assetName, treeBox, checkData, errorData):
    enExplain = 'Grow - Mesh ( Source ) Check'
    inspectionItem = qtWidgets_.QTreeWidgetItem_(['%s [ 0000 / 0000 ]' % enExplain])
    inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check')
    treeBox.addItem(inspectionItem)
    subCheckData = []
    subErrorData = []
    #
    inData = datAsset.getAstCfxGrowSourceConnectionDic(assetName)
    #
    if inData:
        maxValue = len(inData)
        for seq, (sourceMeshObject, targetMeshObject) in enumerate(inData.items()):
            main.setProgressValue(seq + 1, maxValue)
            targetMeshName = maUtils._toNodeName(targetMeshObject)
            growItem = qtWidgets_.QTreeWidgetItem_([targetMeshName, 'Grow Source'])
            growItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh)
            #
            inspectionItem.addChild(growItem)
            #
            if not maGeom.isMeshGeomTopoMatch(sourceMeshObject, targetMeshObject):
                growItem.setText(2, 'Contrast - Error')
                if not maUtils.isAppExist(sourceMeshObject):
                    growItem.setText(2, 'Non - Exists')
                growItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh, 'error')
                inspectionItem.setExpanded(True)
                errorData.append(targetMeshObject)
                subErrorData.append(targetMeshObject)
            checkData.append(targetMeshObject)
            subCheckData.append(targetMeshObject)
        #
        setCheckResult(main, enExplain, inspectionItem, subCheckData, subErrorData)
    elif not inData:
        inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'Off')
    #
    treeBox.setFilterExplainRefresh()


#
def setAstCfxSolverGuideCheckView(main, assetClass, assetName, treeBox, checkData, errorData):
    enExplain = 'Solver - Guide Check'
    inspectionItem = qtWidgets_.QTreeWidgetItem_(['%s [ 0000 / 0000 ]' % enExplain])
    inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check')
    treeBox.addItem(inspectionItem)
    subCheckData = []
    subErrorData = []
    #
    inData = datAsset.getAstCfxNurbsHairSolverCheckData(assetName)
    #
    if inData:
        maxValue = len(inData)
        for seq, (objectPath, data) in enumerate(inData.items()):
            main.setProgressValue(seq + 1, maxValue)
            objectName = maUtils._toNodeName(objectPath)
            objectItem = qtWidgets_.QTreeWidgetItem_([objectName, maUtils.getShapeType(objectPath)])
            objectItem.setItemMayaIcon(0, appCfg.MaNodeType_Transform)
            #
            inspectionItem.addChild(objectItem)
            #
            if not data:
                objectItem.setText(2, 'Non - Exists')
                objectItem.setItemMayaIcon(0, appCfg.MaNodeType_Transform, 'error')
                #
                inspectionItem.setExpanded(True)
                errorData.append(data)
                subErrorData.append(data)
            checkData.append(data)
            subCheckData.append(data)
        #
        setCheckResult(main, enExplain, inspectionItem, subCheckData, subErrorData)
    elif not inData:
        inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'Off')
    #
    treeBox.setFilterExplainRefresh()


#
def setAstSolverGuideCheckSub(main, assetClass, assetName, treeBox, checkData, errorData):
    enExplain = 'Solver - Guide Check'
    inspectionItem = qtWidgets_.QTreeWidgetItem_(['%s [ 0000 / 0000 ]' % enExplain])
    inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check')
    treeBox.addItem(inspectionItem)
    #
    subCheckData = []
    subErrorData = []
    #
    inData = datAsset.getAstSolverGuideCheckData(assetName)
    #
    if inData:
        maxValue = len(inData)
        for seq, (objectPath, data) in enumerate(inData.items()):
            main.setProgressValue(seq + 1, maxValue)
            objectItem = setCheckObjectBranch(objectPath, inspectionItem)
            subCheckResult = True
            if data:
                nhrObjects = data
                for nhrObject in nhrObjects:
                    setCheckObjectBranch(nhrObject, objectItem)
            else:
                subCheckResult = False
                objectItem.setItemMayaIcon(0, appCfg.MaNurbsHairInGuideCurvesType, 'error')
                objectItem.setText(2, 'Non - Exists')
            #
            if subCheckResult is False:
                objectItem.setItemMayaIcon(0, appCfg.MaNurbsHairInGuideCurvesType, 'error')
                objectItem.setText(2, 'Non - Exists')
                objectItem.setExpanded(True)
                #
                errorData.append(objectPath)
                subErrorData.append(objectPath)
            #
            checkData.append(objectPath)
            subCheckData.append(objectPath)
        #
        setCheckResult(main, enExplain, inspectionItem, subCheckData, subErrorData)
    elif not inData:
        inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'Off')
    #
    treeBox.setFilterExplainRefresh()


#
def setAstSolverGrowSourceCheckSub(main, assetClass, assetName, treeBox, checkData, errorData):
    enExplain = 'Grow - Mesh ( Source ) Check'
    inspectionItem = qtWidgets_.QTreeWidgetItem_(['%s [ 0000 / 0000 ]' % enExplain])
    inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check')
    treeBox.addItem(inspectionItem)
    subCheckData = []
    subErrorData = []
    #
    inData = datAsset.getAstSolverGrowSourceConnectionDic(assetName)
    #
    if inData:
        maxValue = len(inData)
        for seq, (sourceMeshObject, targetMeshObject) in enumerate(inData.items()):
            main.setProgressValue(seq + 1, maxValue)
            targetMeshName = maUtils._toNodeName(targetMeshObject)
            growItem = qtWidgets_.QTreeWidgetItem_([targetMeshName, 'Grow Source'])
            growItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh)
            #
            inspectionItem.addChild(growItem)
            #
            if not maGeom.isMeshGeomTopoMatch(sourceMeshObject, targetMeshObject):
                growItem.setText(2, 'Contrast - Error')
                if not maUtils.isAppExist(sourceMeshObject):
                    growItem.setText(2, 'Non - Exists')
                growItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh, 'error')
                inspectionItem.setExpanded(True)
                errorData.append(targetMeshObject)
                subErrorData.append(targetMeshObject)
            checkData.append(targetMeshObject)
            subCheckData.append(targetMeshObject)
        #
        setCheckResult(main, enExplain, inspectionItem, subCheckData, subErrorData)
    elif not inData:
        inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'Off')
    #
    treeBox.setFilterExplainRefresh()


#
def setAstTextureCheckView(projectName, assetClass, assetName, assetVariant, assetStage, treeBox, inData, checkData, errorData):
    isFormatCheck = appVariant.arTextureFormatCheck
    isArTxCheck = appVariant.arTextureTxCheck
    isArColorSpaceCheck = appVariant.arTextureColorSpaceCheck
    #
    folderItemDic = {}
    textureFileItemDic = {}
    #
    enExplain = 'Texture Check'
    inspectionItem = qtWidgets_.QTreeWidgetItem_(['%s [ 0000 / 0000 ]' % enExplain])
    inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check')
    treeBox.addItem(inspectionItem)
    if inData:
        serverTextureDirectory = assetPr.astUnitTextureFolder(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            assetClass, assetName, assetVariant, assetStage
        )
        setAstTextureCheckSubMethod(
            inData,
            checkData, errorData,
            targetDirectory=serverTextureDirectory,
            parentItem=inspectionItem,
            formatCheckEnable=isFormatCheck,
            txCheckEnable=isArTxCheck,
            colorSpaceCheckEnable=isArColorSpaceCheck
        )
        #
        if errorData:
            inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'error')
            inspectionItem.setExpanded(True)
        else:
            inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'on')
        #
        inspectionItem.setText(
            0, '%s [ %s / %s ]' % (enExplain, str(len(checkData) - len(errorData)).zfill(4), str(len(checkData)).zfill(4))
        )
    else:
        inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'Off')
    #
    treeBox.setFilterExplainRefresh()


#
def setAstTextureCheckSubMethod(
        inData,
        checkData=None, errorData=None, targetDirectory=None, parentItem=None,
        formatCheckEnable=False, txCheckEnable=False, colorSpaceCheckEnable=False
):
    def setFolderItemBranch(parentItem_, osPath):
        def setFolderItemAction():
            def folderOpenCmd():
                lxBasic.setOsFolderOpen(osPath)
            #
            actionDatumLis = [
                ('Basic',),
                ('Open Folder', 'svg_basic@svg#folder', True, folderOpenCmd)
            ]
            itemWidget.setActionData(actionDatumLis)
        #
        treeItem = qtWidgets_.QTreeWidgetItem_()
        #
        if hasattr(parentItem_, 'addItem'):
            parentItem_.addItem(treeItem)
        elif hasattr(parentItem_, 'addChild'):
            parentItem_.addChild(treeItem)
        #
        itemWidget = treeItem.setItemIconWidget(0, 'svg_basic@svg#folder', osPath)
        #
        setFolderItemAction()
        return treeItem
    #
    def setFileItemBranch(folderItem, datum, osPath):
        def setTextureItemAction(itemWidget):
            def textureTxDeleteCmd():
                if textureTxFileLis:
                    for i in textureTxFileLis:
                        lxBasic.setOsFileRemove(i)
                #
                [textureTxFileLis.remove(i) for i in textureTxFileLis]
            #
            actionDatumLis = [
                ('Basic',),
                ('Delete Texture Tx(s)', 'svg_basic@svg#delete', True, textureTxDeleteCmd)
            ]
            itemWidget.setActionData(actionDatumLis)
        #
        def setFormatCheck(osTextureFile):
            textureFormat_ = maTxtr.getTextureMode(osTextureFile)
            if textureFormat_ == 'L' or textureFormat_ == 'F' or textureFormat_ == 'I':
                check = False
            else:
                check = True
            return textureFormat_, check
        #
        def setUpdateCheck(origFileMtimestamp, osTargetTextureFile):
            if os.path.isfile(osTargetTextureFile):
                timestamp = lxBasic.getOsFileMtimestamp(osTargetTextureFile)
                if str(origFileMtimestamp) != str(timestamp):
                    check = False
                else:
                    check = True
            else:
                timestamp = None
                check = True
            return check, timestamp
        #
        def setTxCheck(osTxTextureFile, origFileMtimestamp):
            if os.path.isfile(osTxTextureFile):
                timestamp = lxBasic.getOsFileMtimestamp(osTxTextureFile)
                if int(timestamp) != int(origFileMtimestamp):

                    check = False
                else:
                    check = True
            else:
                timestamp = None
                check = False
            return check, timestamp
        #
        def setSubTextureFilesBranch(parentItem_, subTextureDatumLis):
            subFormatCheckLis = []
            suTxCheckLis = []
            subUpdateCheckLis = []
            subTextureMtimestampLis = []
            subTextureTxMtimestampLis = []
            subUpdateCheck = True
            #
            count = len(subTextureDatumLis)
            #
            branchItem = qtWidgets_.QTreeWidgetItem_()
            branchItem.setText(0, 'File ( {} )'.format(count))
            branchItem.setItemIcon_(0, 'svg_basic@svg#branch_sub')
            parentItem_.addChild(branchItem)
            for subTextureDatum in subTextureDatumLis:
                subTextureFileBasename,  subTextureMtimestamp = subTextureDatum
                subTextureTxMtimestamp = None
                #
                subTextureName, subExt = os.path.splitext(subTextureFileBasename)
                subTextureFile = lxBasic._toOsFile(osPath, subTextureFileBasename)
                #
                subWidth, subHeight = maTxtr.getTextureSize(subTextureFile)
                subTextureText1 = '%s ( %s*%s )' % (
                    'Image', str(subWidth).zfill(4), str(subHeight).zfill(4)
                )
                subTextureItem = qtWidgets_.QTreeWidgetItem_()
                branchItem.addChild(subTextureItem)
                # Format Check
                if formatCheckEnable is True:
                    subTextureFormat, subTextureFormat = setFormatCheck(subTextureFile)
                    subFormatCheckLis.append(subTextureFormat)
                # Tx Check
                if txCheckEnable is True:
                    subTextureTxFile = '{}/{}{}'.format(osPath, subTextureName, txExt)
                    subTxCheck, subTextureTxMtimestamp = setTxCheck(
                        subTextureTxFile, subTextureMtimestamp
                    )
                    #
                    subTextureTxMtimestampLis.append(subTextureTxMtimestamp)
                    suTxCheckLis.append(subTxCheck)
                    #
                    if subTextureTxMtimestamp is not None:
                        textureTxFileLis.append(subTextureTxFile)
                # Update Check
                if targetDirectory:
                    targetSubTextureFile = '%s/%s%s' % (targetDirectory, subTextureName, subExt)
                    subUpdateCheck, subTargetMtimestamp = setUpdateCheck(
                        subTextureMtimestamp, targetSubTextureFile
                    )
                #
                subTextureMtimestampLis.append(subTextureMtimestamp)
                subUpdateCheckLis.append(subUpdateCheck)
                #
                subTextureItem.setItemIcon_(0, 'svg_basic@svg#image')
                subTextureItem.setItemIcon_(1, 'svg_basic@svg#name')
                subTextureItem.setItemIcon_(2, 'svg_basic@svg#time')
                subTextureItem.setItemIcon_(3, 'svg_basic@svg#time')
                #
                subTextureItem.setText(0, subTextureFileBasename)
                subTextureItem.setText(1, subTextureText1)
                subTextureItem.setText(2, lxBasic.getCnViewTime(subTextureMtimestamp))
                subTextureItem.setText(3, lxBasic.getCnViewTime(subTextureTxMtimestamp))
            # Check
            formatCheck = sum([1 for i in suTxCheckLis if i is True]) == count
            txCheck = sum([1 for i in suTxCheckLis if i is True]) == count
            updateCheck = sum([1 for i in subUpdateCheckLis if i is True]) == count
            #
            mTimestamp = max(subTextureMtimestampLis)
            txMtimestamp = max(subTextureTxMtimestampLis)
            return formatCheck, txCheck, updateCheck, mTimestamp, txMtimestamp
        #
        def setTextureNodesBranch(parentItem_, datumLis):
            colorSpaceLis = []
            #
            count = len(datumLis)
            #
            branchItem = qtWidgets_.QTreeWidgetItem_()
            branchItem.setText(0, 'Nde_Node ( {} )'.format(count))
            branchItem.setItemIcon_(0, 'svg_basic@svg#branch_sub')
            parentItem_.addChild(branchItem)
            for textureNode in datumLis:
                textureNodeType = maUtils.getNodeType(textureNode)
                colorSpace = maUtils.getAttrDatum(textureNode, 'colorSpace')
                if not colorSpace in colorSpaceLis:
                    colorSpaceLis.append(colorSpace)
                #
                textureNodeItem = qtWidgets_.QTreeWidgetItem_(
                    [textureNode, '{} ( {} )'.format(textureNodeType, colorSpace)]
                )
                branchItem.addChild(textureNodeItem)
                textureNodeItem.setItemMayaIcon(0, textureNodeType)
                textureNodeItem.setItemIcon_(1, 'svg_basic@svg#name')
            #
            colorSpaceCount = len(colorSpaceLis)
            if colorSpaceCheckEnable is True:
                if colorSpaceCount > 1:
                    folderItem.setExpanded(True)
                    colorSpaceCheck = False
                else:
                    colorSpaceCheck = True
            else:
                colorSpaceCheck = True
            #
            return colorSpaceCheck
        #
        textureTxFileLis = []
        #
        textureFileBasename,  textureMtimestampDatum, textureNodeDatumLis = datum
        #
        textureName, ext = lxBasic.toOsFileSplitByExt(textureFileBasename)
        #
        textureFile = lxBasic._toOsFile(osPath, textureFileBasename)
        #
        textureFileText0 = textureFileBasename
        textureFileIconState0 = None
        textureFileTooltipLis = []
        #
        textureFileMtimestamp = textureMtimestampDatum
        textureTxFileMtimestamp = None
        #
        textureItem = qtWidgets_.QTreeWidgetItem_()
        folderItem.addChild(textureItem)
        #
        textureFormatCheck = True
        textureTxCheck = True
        textureUpdateCheck = True
        #
        checkData.append(textureName)
        if textureFileMtimestamp is not None:
            if '<udim>' in textureFile.lower() or '<f>' in textureFile.lower():
                subTextureFileCount = len(textureMtimestampDatum)
                #
                textureIconKeyword0 = 'svg_basic@svg#images'
                textureText1 = '{} ( {} )'.format(
                    'Image(s)', subTextureFileCount
                )
                #
                _textureFormatCheck, _textureTxCheck, textureUpdateCheck, textureFileMtimestamp, textureTxFileMtimestamp = setSubTextureFilesBranch(textureItem, textureMtimestampDatum)
                if formatCheckEnable is True:
                    textureFormatCheck = _textureFormatCheck
                if txCheckEnable is True:
                    textureTxCheck = _textureTxCheck
            else:
                textureIconKeyword0 = 'svg_basic@svg#image'
                width, height = maTxtr.getTextureSize(textureFile)
                textureText1 = 'Image ( {}*{} )'.format(str(width).zfill(4), str(height).zfill(4))
                # Format Check
                if formatCheckEnable is True:
                    textureFormat, textureFormatCheck = setFormatCheck(textureFile)
                # Tx Check
                if txCheckEnable is True:
                    textureTxFile = '{}/{}{}'.format(osPath, textureName, txExt)
                    textureTxCheck, textureTxFileMtimestamp = setTxCheck(
                        textureTxFile, textureFileMtimestamp
                    )
                    if textureTxFileMtimestamp is not None:
                        textureTxFileLis.append(textureTxFile)
                # Update Check
                if targetDirectory:
                    targetTextureFile = '%s/%s%s' % (targetDirectory, textureName, ext)
                    textureUpdateCheck, targetTextureMtimestamp = setUpdateCheck(
                        textureFileMtimestamp, targetTextureFile
                    )
        else:
            textureIconKeyword0 = 'svg_basic@svg#image'
            textureText1 = 'Image ( ????*???? )'
            #
            textureFileTooltipLis.append(u'贴图丢失：\n1，请找到丢失的贴图。')
            textureFileIconState0 = 'error'
        #
        textureColorSpaceCheck = setTextureNodesBranch(textureItem, textureNodeDatumLis)
        #
        if textureFormatCheck is False:
            textureFileTooltipLis.append(u'贴图格式错误：\n1，请修改贴图格式。')
            textureFileIconState0 = 'error'
        if textureTxCheck is False:
            textureFileTooltipLis.append(u'贴图“tx”丢失 / 时间不匹配\n1，请重新生成“tx”。')
            textureFileIconState0 = 'error'
        if textureUpdateCheck is False:
            textureFileTooltipLis.append(u'贴图有更新：\n')
            textureFileIconState0 = 'warning'
        if textureColorSpaceCheck is False:
            textureFileTooltipLis.append(u'贴图节点“Color Space”不一致')
            textureFileIconState0 = 'error'
        #
        if textureFileIconState0 == 'error':
            errorData.append(textureName)
            folderItem.setExpanded(True)
        #
        textureItemWidget = textureItem.setItemIconWidget(0, textureIconKeyword0, textureFileText0, textureFileIconState0)
        if textureFileTooltipLis:
            textureItemWidget.setTooltip('；\n'.join(textureFileTooltipLis))
        else:
            textureItemWidget.setTooltip(None)
        #
        textureItem.setItemIcon_(1, 'svg_basic@svg#name')
        textureItem.setItemIcon_(2, 'svg_basic@svg#time')
        textureItem.setItemIcon_(3, 'svg_basic@svg#time')
        textureItem.setText(1, textureText1)
        textureItem.setText(2, lxBasic.getCnViewTime(textureFileMtimestamp))
        textureItem.setText(3, lxBasic.getCnViewTime(textureTxFileMtimestamp))
        #
        setTextureItemAction(textureItemWidget)
    #
    def setMain():
        for k, v in inData.items():
            osPath = k
            folderItem = setFolderItemBranch(parentItem, osPath)
            for seq, i in enumerate(v):
                setFileItemBranch(folderItem, i, osPath)
    #
    setMain()


#
def setAstShaderCheckView(assetClass, assetName, treeBox):
    treeBox.setFilterExplainRefresh()
