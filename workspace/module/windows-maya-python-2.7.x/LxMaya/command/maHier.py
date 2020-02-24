# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxBasic import bscMtdCore, bscMethods
#
from LxPreset import prsOutputs, prsMethods
#
from LxCore.preset.prod import assetPr, sceneryPr, scenePr
#
from LxMaya.command import maUtils, maUuid
#
none = ''


#
def getHierarchyName(group):
    hierarchyName = '_'.join(group.split('_')[-2:-1])
    return hierarchyName


# Create Hierarchy Root
def setCreateHierarchy(root, hierarchyData):
    # Crate Root
    setCreateBranchGroup(none, root)
    maUtils.setNodeOverrideColor(root, color=17)
    # Create Tree
    if root:
        setCreateBranch(hierarchyData, root)


#
def setCreateAstRootHierarchy(assetCategory, assetName, isLock=True):
    hierarchyData = assetPr.astRootGroupHierarchyConfig(assetName)

    pathDic = bscMethods.MaNodeString.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    rootGroup = prsMethods.Asset.rootName(assetName)
    maUtils.setNodeOverrideColor(rootGroup, color=13)
    #
    branches = [
        prsMethods.Asset.modelLinkGroupName(assetName),
        prsMethods.Asset.groomLinkGroupName(assetName),
        prsMethods.Asset.rigLinkGroupName(assetName),
        prsMethods.Asset.solverLinkGroupName(assetName),
        prsMethods.Asset.lightLinkGroupName(assetName)
    ]
    [maUtils.setObjectParent(i, rootGroup) for i in branches if maUtils._isAppExist(i)]


#
def setCreateModelLinkHierarchy(assetCategory, assetName, isLock=True):
    hierarchyData = assetPr.astModelLinkHierarchyConfig(assetName)
    pathDic = bscMethods.MaNodeString.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]


#
def setCreateAstModelHierarchy(assetCategory, assetName, withRoot=True, isLock=True):
    setCreateModelLinkHierarchy(assetCategory, assetName, isLock)
    if withRoot:
        setCreateAstRootHierarchy(assetCategory, assetName)


#
def setCreateAstUnitModelSolverHierarchy(assetCategory, assetName, isLock=True):
    hierarchyData = assetPr.astModelSolverHierarchyConfig(assetName)
    pathDic = bscMethods.MaNodeString.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]


#
def setCreateAstUnitModelReferenceHierarchy(assetCategory, assetName, isLock=True):
    hierarchyData = assetPr.astModelReferenceHierarchyConfig(assetName)
    pathDic = bscMethods.MaNodeString.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]


#
def setCreateAstCfxHierarchy(assetCategory, assetName, withRoot=True, isLock=True):
    hierarchyData = assetPr.astCfxHierarchyConfig(assetName)
    pathDic = bscMethods.MaNodeString.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateAstRootHierarchy(assetCategory, assetName)


#
def setCreateAstRigHierarchy(assetCategory, assetName, withRoot=True, isLock=True):
    hierarchyData = assetPr.astRigLinkHierarchyConfig(assetName)
    pathDic = bscMethods.MaNodeString.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateAstRootHierarchy(assetCategory, assetName)


#
def setCreateAstRigSolverHierarchy(assetCategory, assetName, withRoot=True, isLock=True):
    hierarchyData = assetPr.astRigSolverHierarchyConfig(assetName)
    pathDic = bscMethods.MaNodeString.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateAstRootHierarchy(assetCategory, assetName)


#
def setCreateAstLightHierarchy(assetCategory, assetName, withRoot=True, isLock=True):
    hierarchyData = assetPr.astLightHierarchyConfig(assetName)
    pathDic = bscMethods.MaNodeString.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateAstRootHierarchy(assetCategory, assetName)


#
def setCreateScnRootHierarchy(sceneryCategory, sceneryName, sceneryVariant, isLock=True):
    hierarchyData = sceneryPr.scnRootGroupHierarchyConfig(sceneryName)
    pathDic = bscMethods.MaNodeString.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    rootGroup = sceneryPr.scnUnitRootGroupName(sceneryName)
    maUtils.setNodeOverrideColor(rootGroup, color=13)
    # Model Group
    scnAssembly = sceneryPr.scnAssemblyGroupName(sceneryName)
    if maUtils._isAppExist(scnAssembly):
        maUtils.setObjectParent(scnAssembly, rootGroup)
    sceneryUnitAr = sceneryPr.scnAssemblyArName(sceneryCategory, sceneryName, sceneryVariant)
    if maUtils._isAppExist(sceneryUnitAr):
        maUtils.setObjectParent(sceneryUnitAr, rootGroup)
    scnLightGroup = sceneryPr.scnLightGroupName(sceneryName)
    if maUtils._isAppExist(scnLightGroup):
        maUtils.setObjectParent(scnLightGroup, rootGroup)


#
def setCreateScnAssemblyHierarchy(sceneryCategory, sceneryName, sceneryVariant, withRoot=True, isLock=True):
    hierarchyData = sceneryPr.scnAssemblyHierarchyConfig(sceneryName)
    pathDic = bscMethods.MaNodeString.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateScnRootHierarchy(sceneryCategory, sceneryName, sceneryVariant)


#
def setCreateScnLightHierarchy(sceneryCategory, sceneryName, sceneryVariant, withRoot=True, isLock=True):
    hierarchyData = sceneryPr.scnLightHierarchyConfig(sceneryName)
    pathDic = bscMethods.MaNodeString.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateScnRootHierarchy(sceneryCategory, sceneryName, sceneryVariant)


#
def setCreateScRootHierarchy(sceneCategory, sceneName, sceneVariant, sceneStage, isLock=True):
    hierarchyData = scenePr.scRootGroupHierarchyConfig(sceneName)
    pathDic = bscMethods.MaNodeString.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    rootGroup = scenePr.scUnitRootGroupName(sceneName)
    maUtils.setNodeOverrideColor(rootGroup, color=13)
    # Scene Group
    scLinkGroup = scenePr.scUnitLinkGroupName(sceneName, sceneVariant, sceneStage)
    if maUtils._isAppExist(scLinkGroup):
        maUtils.setObjectParent(scLinkGroup, rootGroup)


#
def setCreateScLinkHierarchy(sceneCategory, sceneName, sceneVariant, sceneStage, withRoot=True, isLock=True):
    hierarchyData = scenePr.scLinkHierarchyConfig(sceneName, sceneVariant, sceneStage)
    pathDic = bscMethods.MaNodeString.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateScRootHierarchy(sceneCategory, sceneName, sceneVariant, sceneStage)


# Create Hierarchy's Branch
def setCreateBranchGroup(parent, child):
    if parent:
        cmds.group(empty=1, name=child, parent=parent)
    else:
        cmds.group(empty=1, name=child)
    #
    maUtils.setObjectTransformationAttr(child)
    #
    branchName = getHierarchyName(child)
    #
    username = bscMethods.OsSystem.username()
    timetag = bscMethods.OsTimetag.active()
    #
    maUtils.setAttrStringDatumForce(child, prsOutputs.Util.basicHierarchyAttrLabel, branchName)
    maUtils.setAttrStringDatumForce(child, prsOutputs.Util.basicArtistAttrLabel, username)
    maUtils.setAttrStringDatumForce(child, prsOutputs.Util.basicUpdateAttrLabel, timetag)


# Create Hierarchy's Branch ( Method )
def setCreateBranch(hierarchyData, parent):
    if parent in hierarchyData:
        children = hierarchyData[parent]
        for child in children:
            #
            setCreateBranchGroup(parent, child)
            #
            setCreateBranch(hierarchyData, child)


#
def getGroupNameLabel(group, assetName):
    hierarchyName = group.split(assetName)[-1][1:-4]
    return hierarchyName


#
def addHierarchyObject(parentPath, assetName, filterTypes, autoRename=True):
    parentName = maUtils._nodeString2nodename_(parentPath)
    #
    username = bscMethods.OsSystem.username()
    timetag = bscMethods.OsTimetag.active()
    #
    keyword = getGroupNameLabel(parentName, assetName)
    #
    selObjectStringLis = maUtils.getSelectedObjectsFilterByTypes(filterTypes)
    if maUtils._isAppExist(parentPath):
        if selObjectStringLis:
            for objectString in selObjectStringLis:
                meshUuid = maUuid._getNodeUniqueIdString(objectString)
                maUtils.setAttrStringDatumForce(objectString, prsOutputs.Util.basicHierarchyAttrLabel, keyword)
                maUtils.setAttrStringDatumForce(objectString, prsOutputs.Util.basicArtistAttrLabel, username)
                maUtils.setAttrStringDatumForce(objectString, prsOutputs.Util.basicUpdateAttrLabel, timetag)
                #
                cmds.setAttr(objectString + '.useOutlinerColor', 1)
                cmds.setAttr(objectString + '.outlinerColor', 0, 1, 0)
                #
                maUtils.setObjectParent(objectString, parentPath)
                if autoRename:
                    newPath = maUuid.getObject(meshUuid)
                    newMeshName = assetPr.astBasicObjectNameSet(assetName, '_' + keyword) + '_0'
                    maUtils.setNodeRename(newPath, newMeshName)


#
def refreshHierarchyBranch(
        branch,
        utilsIndex,
        utilsClass, utilsName, utilsVariant, utilsStage,
        timeTag=None):
    if not maUtils.isReferenceNode(branch):
        branchName = getHierarchyName(branch)
        username = bscMethods.OsSystem.username()
        timetag = bscMethods.OsTimetag.active()
        #
        maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicHierarchyAttrLabel, branchName)
        maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicArtistAttrLabel, username)
        maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicUpdateAttrLabel, timetag)
        #
        maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicClassAttrLabel, utilsClass)
        maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicNameAttrLabel, utilsName)
        maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicVariantAttrLabel, utilsVariant)
        maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicStageAttrLabel, utilsStage)
        #
        maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicIndexAttrLabel, utilsIndex)
        #
        if timeTag:
            maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicTagAttrLabel, timeTag)


#
def astUnitRefreshRoot(
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        timeTag=None
):
    #
    astRoot = prsMethods.Asset.rootName(assetName)
    #
    if maUtils._isAppExist(astRoot):
        refreshHierarchyBranch(
            astRoot,
            assetIndex,
            assetCategory, assetName, assetVariant, assetStage
        )
    #
    if prsMethods.Asset.isValidStageName(assetStage):
        branch = prsMethods.Asset.toLinkGroupName(assetName, assetStage)
        #
        if maUtils._isAppExist(branch):
            refreshHierarchyBranch(
                branch,
                assetIndex,
                assetCategory, assetName, assetVariant, assetStage,
                timeTag
            )


#
def scUnitRefreshRoot(
        assetIndex,
        assetCategory, assetName, assetVariant, assetStage,
        timeTag, namespace
):
    if prsMethods.Asset.isValidStageName(assetStage):
        branch = prsMethods.Asset.toLinkGroupName(assetName, assetStage, namespace)
        if maUtils._isAppExist(branch):
            refreshHierarchyBranch(
                branch,
                assetIndex,
                assetCategory, assetName, assetVariant, assetStage,
                timeTag
            )


#
def refreshSceneCacheTag(objectPath, timeTag):
    username = bscMethods.OsSystem.username()
    timetag = bscMethods.OsTimetag.active()
    #
    maUtils.setAttrStringDatumForce(objectPath, prsOutputs.Util.basicCacheArtistAttrLabel, username)
    maUtils.setAttrStringDatumForce(objectPath, prsOutputs.Util.basicCacheUpdateAttrLabel, timetag)
    maUtils.setAttrStringDatumForce(objectPath, prsOutputs.Util.basicCacheTagAttrLabel, timeTag)


#
def refreshScnRoot(sceneryCategory, sceneryName, sceneryVariant, sceneryStage, sceneryIndex):
    root = sceneryPr.scnUnitRootGroupName(sceneryName)
    if maUtils._isAppExist(root):
        refreshHierarchyBranch(
            root,
            sceneryIndex,
            sceneryCategory, sceneryName, sceneryVariant, sceneryStage
        )
    #
    branch = none
    if sceneryPr.isSceneryLinkName(sceneryStage):
        branch = sceneryPr.scnAssemblyGroupName(sceneryName)
    elif sceneryPr.isLayoutLinkName(sceneryStage):
        branch = sceneryPr.scnAssemblyGroupName(sceneryName)
    elif sceneryPr.isAnimationLinkName(sceneryStage) or sceneryPr.isLightLinkName(sceneryStage):
        branch = sceneryPr.scnAssemblyArName(sceneryCategory, sceneryName, sceneryVariant)
    #
    if maUtils._isAppExist(branch):
        refreshScnBranch(branch, sceneryCategory, sceneryName, sceneryVariant, sceneryStage, sceneryIndex)


#
def refreshScRoot(sceneCategory, sceneName, sceneVariant, sceneStage, sceneIndex):
    root = scenePr.scUnitRootGroupName(sceneName)
    if maUtils._isAppExist(root):
        refreshHierarchyBranch(
            root,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage
        )
    #
    branch = scenePr.scUnitLinkGroupName(sceneName, sceneVariant, sceneStage)
    #
    if maUtils._isAppExist(branch):
        refreshScnBranch(branch, sceneCategory, sceneName, sceneVariant, sceneStage, sceneIndex)


#
def refreshScAstUnitBranch(branch, assetIndex, assetCategory, assetName, number, assetVariant, timeTag):
    username = bscMethods.OsSystem.username()
    timetag = bscMethods.OsTimetag.active()
    #
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicArtistAttrLabel, username)
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicUpdateAttrLabel, timetag)
    #
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicIndexAttrLabel, assetIndex)
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicClassAttrLabel, assetCategory)
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicNameAttrLabel, assetName)
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicVariantAttrLabel, assetVariant)
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicNumberAttrLabel, number)
    #
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicTagAttrLabel, timeTag)


#
def refreshScnBranch(branch, sceneryCategory, sceneryName, sceneryVariant, sceneryStage, sceneryIndex):
    branchName = getHierarchyName(branch)
    username = bscMethods.OsSystem.username()
    timetag = bscMethods.OsTimetag.active()
    #
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicHierarchyAttrLabel, branchName)
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicArtistAttrLabel, username)
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicUpdateAttrLabel, timetag)
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicClassAttrLabel, sceneryCategory)
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicNameAttrLabel, sceneryName)
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicVariantAttrLabel, sceneryVariant)
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicStageAttrLabel, sceneryStage)
    maUtils.setAttrStringDatumForce(branch, prsOutputs.Util.basicIndexAttrLabel, sceneryIndex)
