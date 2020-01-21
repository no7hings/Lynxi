# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxBasic import bscMethods
#
from LxPreset import prsVariants, prsMethods
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
def setCreateAstRootHierarchy(assetClass, assetName, isLock=True):
    hierarchyData = assetPr.astRootGroupHierarchyConfig(assetName)

    pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
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
    [maUtils.setObjectParent(i, rootGroup) for i in branches if maUtils.isAppExist(i)]


#
def setCreateModelLinkHierarchy(assetClass, assetName, isLock=True):
    hierarchyData = assetPr.astModelLinkHierarchyConfig(assetName)
    pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]


#
def setCreateAstModelHierarchy(assetClass, assetName, withRoot=True, isLock=True):
    setCreateModelLinkHierarchy(assetClass, assetName, isLock)
    if withRoot:
        setCreateAstRootHierarchy(assetClass, assetName)


#
def setCreateAstUnitModelSolverHierarchy(assetClass, assetName, isLock=True):
    hierarchyData = assetPr.astModelSolverHierarchyConfig(assetName)
    pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]


#
def setCreateAstUnitModelReferenceHierarchy(assetClass, assetName, isLock=True):
    hierarchyData = assetPr.astModelReferenceHierarchyConfig(assetName)
    pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]


#
def setCreateAstCfxHierarchy(assetClass, assetName, withRoot=True, isLock=True):
    hierarchyData = assetPr.astCfxHierarchyConfig(assetName)
    pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateAstRootHierarchy(assetClass, assetName)


#
def setCreateAstRigHierarchy(assetClass, assetName, withRoot=True, isLock=True):
    hierarchyData = assetPr.astRigLinkHierarchyConfig(assetName)
    pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateAstRootHierarchy(assetClass, assetName)


#
def setCreateAstRigSolverHierarchy(assetClass, assetName, withRoot=True, isLock=True):
    hierarchyData = assetPr.astRigSolverHierarchyConfig(assetName)
    pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateAstRootHierarchy(assetClass, assetName)


#
def setCreateAstLightHierarchy(assetClass, assetName, withRoot=True, isLock=True):
    hierarchyData = assetPr.astLightHierarchyConfig(assetName)
    pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateAstRootHierarchy(assetClass, assetName)


#
def setCreateScnRootHierarchy(sceneryClass, sceneryName, sceneryVariant, isLock=True):
    hierarchyData = sceneryPr.scnRootGroupHierarchyConfig(sceneryName)
    pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    rootGroup = sceneryPr.scnUnitRootGroupName(sceneryName)
    maUtils.setNodeOverrideColor(rootGroup, color=13)
    # Model Group
    scnAssembly = sceneryPr.scnAssemblyGroupName(sceneryName)
    if maUtils.isAppExist(scnAssembly):
        maUtils.setObjectParent(scnAssembly, rootGroup)
    sceneryUnitAr = sceneryPr.scnAssemblyArName(sceneryClass, sceneryName, sceneryVariant)
    if maUtils.isAppExist(sceneryUnitAr):
        maUtils.setObjectParent(sceneryUnitAr, rootGroup)
    scnLightGroup = sceneryPr.scnLightGroupName(sceneryName)
    if maUtils.isAppExist(scnLightGroup):
        maUtils.setObjectParent(scnLightGroup, rootGroup)


#
def setCreateScnAssemblyHierarchy(sceneryClass, sceneryName, sceneryVariant, withRoot=True, isLock=True):
    hierarchyData = sceneryPr.scnAssemblyHierarchyConfig(sceneryName)
    pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateScnRootHierarchy(sceneryClass, sceneryName, sceneryVariant)


#
def setCreateScnLightHierarchy(sceneryClass, sceneryName, sceneryVariant, withRoot=True, isLock=True):
    hierarchyData = sceneryPr.scnLightHierarchyConfig(sceneryName)
    pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateScnRootHierarchy(sceneryClass, sceneryName, sceneryVariant)


#
def setCreateScRootHierarchy(sceneClass, sceneName, sceneVariant, sceneStage, isLock=True):
    hierarchyData = scenePr.scRootGroupHierarchyConfig(sceneName)
    pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    rootGroup = scenePr.scUnitRootGroupName(sceneName)
    maUtils.setNodeOverrideColor(rootGroup, color=13)
    # Scene Group
    scLinkGroup = scenePr.scUnitLinkGroupName(sceneName, sceneVariant, sceneStage)
    if maUtils.isAppExist(scLinkGroup):
        maUtils.setObjectParent(scLinkGroup, rootGroup)


#
def setCreateScLinkHierarchy(sceneClass, sceneName, sceneVariant, sceneStage, withRoot=True, isLock=True):
    hierarchyData = scenePr.scLinkHierarchyConfig(sceneName, sceneVariant, sceneStage)
    pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateScRootHierarchy(sceneClass, sceneName, sceneVariant, sceneStage)


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
    timetag = bscMethods.OsTime.activeTimetag()
    #
    maUtils.setAttrStringDatumForce(child, prsVariants.Util.basicHierarchyAttrLabel, branchName)
    maUtils.setAttrStringDatumForce(child, prsVariants.Util.basicArtistAttrLabel, username)
    maUtils.setAttrStringDatumForce(child, prsVariants.Util.basicUpdateAttrLabel, timetag)


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
    parentName = maUtils._toNodeName(parentPath)
    #
    username = bscMethods.OsSystem.username()
    timetag = bscMethods.OsTime.activeTimetag()
    #
    keyword = getGroupNameLabel(parentName, assetName)
    #
    selObjectStringLis = maUtils.getSelectedObjectsFilterByTypes(filterTypes)
    if maUtils.isAppExist(parentPath):
        if selObjectStringLis:
            for objectString in selObjectStringLis:
                meshUuid = maUuid.getNodeUniqueId(objectString)
                maUtils.setAttrStringDatumForce(objectString, prsVariants.Util.basicHierarchyAttrLabel, keyword)
                maUtils.setAttrStringDatumForce(objectString, prsVariants.Util.basicArtistAttrLabel, username)
                maUtils.setAttrStringDatumForce(objectString, prsVariants.Util.basicUpdateAttrLabel, timetag)
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
        timetag = bscMethods.OsTime.activeTimetag()
        #
        maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicHierarchyAttrLabel, branchName)
        maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicArtistAttrLabel, username)
        maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicUpdateAttrLabel, timetag)
        #
        maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicClassAttrLabel, utilsClass)
        maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicNameAttrLabel, utilsName)
        maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicVariantAttrLabel, utilsVariant)
        maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicStageAttrLabel, utilsStage)
        #
        maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicIndexAttrLabel, utilsIndex)
        #
        if timeTag:
            maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicTagAttrLabel, timeTag)


#
def astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        timeTag=None
):
    #
    astRoot = prsMethods.Asset.rootName(assetName)
    #
    if maUtils.isAppExist(astRoot):
        refreshHierarchyBranch(
            astRoot,
            assetIndex,
            assetClass, assetName, assetVariant, assetStage
        )
    #
    if prsMethods.Asset.isValidStageName(assetStage):
        branch = prsMethods.Asset.toLinkGroupName(assetName, assetStage)
        #
        if maUtils.isAppExist(branch):
            refreshHierarchyBranch(
                branch,
                assetIndex,
                assetClass, assetName, assetVariant, assetStage,
                timeTag
            )


#
def scUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        timeTag, namespace
):
    if prsMethods.Asset.isValidStageName(assetStage):
        branch = prsMethods.Asset.toLinkGroupName(assetName, assetStage, namespace)
        if maUtils.isAppExist(branch):
            refreshHierarchyBranch(
                branch,
                assetIndex,
                assetClass, assetName, assetVariant, assetStage,
                timeTag
            )


#
def refreshSceneCacheTag(objectPath, timeTag):
    username = bscMethods.OsSystem.username()
    timetag = bscMethods.OsTime.activeTimetag()
    #
    maUtils.setAttrStringDatumForce(objectPath, prsVariants.Util.basicCacheArtistAttrLabel, username)
    maUtils.setAttrStringDatumForce(objectPath, prsVariants.Util.basicCacheUpdateAttrLabel, timetag)
    maUtils.setAttrStringDatumForce(objectPath, prsVariants.Util.basicCacheTagAttrLabel, timeTag)


#
def refreshScnRoot(sceneryClass, sceneryName, sceneryVariant, sceneryStage, sceneryIndex):
    root = sceneryPr.scnUnitRootGroupName(sceneryName)
    if maUtils.isAppExist(root):
        refreshHierarchyBranch(
            root,
            sceneryIndex,
            sceneryClass, sceneryName, sceneryVariant, sceneryStage
        )
    #
    branch = none
    if sceneryPr.isSceneryLinkName(sceneryStage):
        branch = sceneryPr.scnAssemblyGroupName(sceneryName)
    elif sceneryPr.isLayoutLinkName(sceneryStage):
        branch = sceneryPr.scnAssemblyGroupName(sceneryName)
    elif sceneryPr.isAnimationLinkName(sceneryStage) or sceneryPr.isLightLinkName(sceneryStage):
        branch = sceneryPr.scnAssemblyArName(sceneryClass, sceneryName, sceneryVariant)
    #
    if maUtils.isAppExist(branch):
        refreshScnBranch(branch, sceneryClass, sceneryName, sceneryVariant, sceneryStage, sceneryIndex)


#
def refreshScRoot(sceneClass, sceneName, sceneVariant, sceneStage, sceneIndex):
    root = scenePr.scUnitRootGroupName(sceneName)
    if maUtils.isAppExist(root):
        refreshHierarchyBranch(
            root,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage
        )
    #
    branch = scenePr.scUnitLinkGroupName(sceneName, sceneVariant, sceneStage)
    #
    if maUtils.isAppExist(branch):
        refreshScnBranch(branch, sceneClass, sceneName, sceneVariant, sceneStage, sceneIndex)


#
def refreshScAstUnitBranch(branch, assetIndex, assetClass, assetName, number, assetVariant, timeTag):
    username = bscMethods.OsSystem.username()
    timetag = bscMethods.OsTime.activeTimetag()
    #
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicArtistAttrLabel, username)
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicUpdateAttrLabel, timetag)
    #
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicIndexAttrLabel, assetIndex)
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicClassAttrLabel, assetClass)
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicNameAttrLabel, assetName)
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicVariantAttrLabel, assetVariant)
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicNumberAttrLabel, number)
    #
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicTagAttrLabel, timeTag)


#
def refreshScnBranch(branch, sceneryClass, sceneryName, sceneryVariant, sceneryStage, sceneryIndex):
    branchName = getHierarchyName(branch)
    username = bscMethods.OsSystem.username()
    timetag = bscMethods.OsTime.activeTimetag()
    #
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicHierarchyAttrLabel, branchName)
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicArtistAttrLabel, username)
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicUpdateAttrLabel, timetag)
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicClassAttrLabel, sceneryClass)
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicNameAttrLabel, sceneryName)
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicVariantAttrLabel, sceneryVariant)
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicStageAttrLabel, sceneryStage)
    maUtils.setAttrStringDatumForce(branch, prsVariants.Util.basicIndexAttrLabel, sceneryIndex)
