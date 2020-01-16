# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxBasic import bscMethods, bscCommands
#
from LxCore.preset import appVariant
#
from LxCore.preset.prod import assetPr, sceneryPr, scenePr
#
from LxMaya.command import maUtils, maUuid
# Shape Config
shapeSet = appVariant.shapeSet
shapeLabel = appVariant.shapeLabel
shapeDic = appVariant.shapeDic
# Group Config
basicGroupLabel = appVariant.basicGroupLabel
basicModelLinkGroupLabel = appVariant.basicModelLinkGroupLabel
basicGeometryGroupLabel = appVariant.basicGeometryGroupLabel
basicSolverGeometrySubGroupLabel = appVariant.basicSolverGeometrySubGroupLabel
basicCfxLinkGroupLabel = appVariant.basicCfxLinkGroupLabel
#
astDefaultVersion = appVariant.astDefaultVersion
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
    pathDic = bscCommands.getMayaPathDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    rootGroup = assetPr.astUnitRootGroupName(assetName)
    maUtils.setNodeOverrideColor(rootGroup, color=13)
    #
    branches = [
        assetPr.astUnitModelLinkGroupName(assetName),
        #
        assetPr.astUnitCfxLinkGroupName(assetName),
        #
        assetPr.astUnitRigLinkGroupName(assetName),
        assetPr.astUnitSolverLinkGroupName(assetName),
        #
        assetPr.astUnitLightLinkGroupName(assetName)
    ]
    [maUtils.setObjectParent(i, rootGroup) for i in branches if maUtils.isAppExist(i)]


#
def setCreateModelLinkHierarchy(assetClass, assetName, isLock=True):
    hierarchyData = assetPr.astModelLinkHierarchyConfig(assetName)
    pathDic = bscCommands.getMayaPathDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]


#
def setCreateAstModelHierarchy(assetClass, assetName, withRoot=True, isLock=True):
    setCreateModelLinkHierarchy(assetClass, assetName, isLock)
    if withRoot:
        setCreateAstRootHierarchy(assetClass, assetName)


#
def setCreateAstUnitModelSolverHierarchy(assetClass, assetName, isLock=True):
    hierarchyData = assetPr.astModelSolverHierarchyConfig(assetName)
    pathDic = bscCommands.getMayaPathDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]


#
def setCreateAstUnitModelReferenceHierarchy(assetClass, assetName, isLock=True):
    hierarchyData = assetPr.astModelReferenceHierarchyConfig(assetName)
    pathDic = bscCommands.getMayaPathDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]


#
def setCreateAstCfxHierarchy(assetClass, assetName, withRoot=True, isLock=True):
    hierarchyData = assetPr.astCfxHierarchyConfig(assetName)
    pathDic = bscCommands.getMayaPathDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateAstRootHierarchy(assetClass, assetName)


#
def setCreateAstRigHierarchy(assetClass, assetName, withRoot=True, isLock=True):
    hierarchyData = assetPr.astRigLinkHierarchyConfig(assetName)
    pathDic = bscCommands.getMayaPathDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateAstRootHierarchy(assetClass, assetName)


#
def setCreateAstRigSolverHierarchy(assetClass, assetName, withRoot=True, isLock=True):
    hierarchyData = assetPr.astRigSolverHierarchyConfig(assetName)
    pathDic = bscCommands.getMayaPathDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateAstRootHierarchy(assetClass, assetName)


#
def setCreateAstLightHierarchy(assetClass, assetName, withRoot=True, isLock=True):
    hierarchyData = assetPr.astLightHierarchyConfig(assetName)
    pathDic = bscCommands.getMayaPathDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateAstRootHierarchy(assetClass, assetName)


#
def setCreateScnRootHierarchy(sceneryClass, sceneryName, sceneryVariant, isLock=True):
    hierarchyData = sceneryPr.scnRootGroupHierarchyConfig(sceneryName)
    pathDic = bscCommands.getMayaPathDic(hierarchyData)
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
    pathDic = bscCommands.getMayaPathDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateScnRootHierarchy(sceneryClass, sceneryName, sceneryVariant)


#
def setCreateScnLightHierarchy(sceneryClass, sceneryName, sceneryVariant, withRoot=True, isLock=True):
    hierarchyData = sceneryPr.scnLightHierarchyConfig(sceneryName)
    pathDic = bscCommands.getMayaPathDic(hierarchyData)
    [maUtils.setAppPathCreate(i, isLock) for i in pathDic.values()]
    #
    if withRoot:
        setCreateScnRootHierarchy(sceneryClass, sceneryName, sceneryVariant)


#
def setCreateScRootHierarchy(sceneClass, sceneName, sceneVariant, sceneStage, isLock=True):
    hierarchyData = scenePr.scRootGroupHierarchyConfig(sceneName)
    pathDic = bscCommands.getMayaPathDic(hierarchyData)
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
    pathDic = bscCommands.getMayaPathDic(hierarchyData)
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
    maUtils.setAttrStringDatumForce(child, appVariant.basicHierarchyAttrLabel, branchName)
    maUtils.setAttrStringDatumForce(child, appVariant.basicArtistAttrLabel, username)
    maUtils.setAttrStringDatumForce(child, appVariant.basicUpdateAttrLabel, timetag)


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
                maUtils.setAttrStringDatumForce(objectString, appVariant.basicHierarchyAttrLabel, keyword)
                maUtils.setAttrStringDatumForce(objectString, appVariant.basicArtistAttrLabel, username)
                maUtils.setAttrStringDatumForce(objectString, appVariant.basicUpdateAttrLabel, timetag)
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
        maUtils.setAttrStringDatumForce(branch, appVariant.basicHierarchyAttrLabel, branchName)
        maUtils.setAttrStringDatumForce(branch, appVariant.basicArtistAttrLabel, username)
        maUtils.setAttrStringDatumForce(branch, appVariant.basicUpdateAttrLabel, timetag)
        #
        maUtils.setAttrStringDatumForce(branch, appVariant.basicClassAttrLabel, utilsClass)
        maUtils.setAttrStringDatumForce(branch, appVariant.basicNameAttrLabel, utilsName)
        maUtils.setAttrStringDatumForce(branch, appVariant.basicVariantAttrLabel, utilsVariant)
        maUtils.setAttrStringDatumForce(branch, appVariant.basicStageAttrLabel, utilsStage)
        #
        maUtils.setAttrStringDatumForce(branch, appVariant.basicIndexAttrLabel, utilsIndex)
        #
        if timeTag:
            maUtils.setAttrStringDatumForce(branch, appVariant.basicTagAttrLabel, timeTag)


#
def astUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        timeTag=None):
    #
    astRoot = assetPr.astUnitRootGroupName(assetName)
    #
    if maUtils.isAppExist(astRoot):
        refreshHierarchyBranch(
            astRoot,
            assetIndex,
            assetClass, assetName, assetVariant, assetStage
        )
    #
    astLinkBranch = none
    if assetPr.isAstModelLink(assetStage):
        astLinkBranch = assetPr.astUnitModelLinkGroupName(assetName)
    elif assetPr.isAstRigLink(assetStage):
        astLinkBranch = assetPr.astUnitRigLinkGroupName(assetName)
    elif assetPr.isAstCfxLink(assetStage):
        astLinkBranch = assetPr.astUnitCfxLinkGroupName(assetName)
    elif assetPr.isAstSolverLink(assetStage):
        astLinkBranch = assetPr.astUnitSolverLinkGroupName(assetName)
    elif assetPr.isAstLightLink(assetStage):
        astLinkBranch = assetPr.astUnitLightLinkGroupName(assetName)
    #
    if maUtils.isAppExist(astLinkBranch):
        refreshHierarchyBranch(
            astLinkBranch,
            assetIndex,
            assetClass, assetName, assetVariant, assetStage,
            timeTag
        )


#
def scUnitRefreshRoot(
        assetIndex,
        assetClass, assetName, assetVariant, assetStage,
        timeTag, namespace):
    branch = None
    if assetPr.isAstModelLink(assetStage):
        branch = assetPr.astUnitModelLinkGroupName(assetName, namespace)
    elif assetPr.isAstRigLink(assetStage):
        branch = assetPr.astUnitRigLinkGroupName(assetName, namespace)
    elif assetPr.isAstCfxLink(assetStage):
        branch = assetPr.astUnitCfxLinkGroupName(assetName, namespace)
    elif assetPr.isAstSolverLink(assetStage):
        branch = assetPr.astUnitSolverLinkGroupName(assetName, namespace)
    elif assetPr.isAstLightLink(assetStage):
        branch = assetPr.astUnitLightLinkGroupName(assetName, namespace)
    #
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
    maUtils.setAttrStringDatumForce(objectPath, appVariant.basicCacheArtistAttrLabel, username)
    maUtils.setAttrStringDatumForce(objectPath, appVariant.basicCacheUpdateAttrLabel, timetag)
    maUtils.setAttrStringDatumForce(objectPath, appVariant.basicCacheTagAttrLabel, timeTag)


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
    if sceneryPr.isScnSceneryLink(sceneryStage):
        branch = sceneryPr.scnAssemblyGroupName(sceneryName)
    elif sceneryPr.isScnLayoutLink(sceneryStage):
        branch = sceneryPr.scnAssemblyGroupName(sceneryName)
    elif sceneryPr.isScnAnimationLink(sceneryStage) or sceneryPr.isScnLightLink(sceneryStage):
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
    maUtils.setAttrStringDatumForce(branch, appVariant.basicArtistAttrLabel, username)
    maUtils.setAttrStringDatumForce(branch, appVariant.basicUpdateAttrLabel, timetag)
    #
    maUtils.setAttrStringDatumForce(branch, appVariant.basicIndexAttrLabel, assetIndex)
    maUtils.setAttrStringDatumForce(branch, appVariant.basicClassAttrLabel, assetClass)
    maUtils.setAttrStringDatumForce(branch, appVariant.basicNameAttrLabel, assetName)
    maUtils.setAttrStringDatumForce(branch, appVariant.basicVariantAttrLabel, assetVariant)
    maUtils.setAttrStringDatumForce(branch, appVariant.basicNumberAttrLabel, number)
    #
    maUtils.setAttrStringDatumForce(branch, appVariant.basicTagAttrLabel, timeTag)


#
def refreshScnBranch(branch, sceneryClass, sceneryName, sceneryVariant, sceneryStage, sceneryIndex):
    branchName = getHierarchyName(branch)
    username = bscMethods.OsSystem.username()
    timetag = bscMethods.OsTime.activeTimetag()
    #
    maUtils.setAttrStringDatumForce(branch, appVariant.basicHierarchyAttrLabel, branchName)
    maUtils.setAttrStringDatumForce(branch, appVariant.basicArtistAttrLabel, username)
    maUtils.setAttrStringDatumForce(branch, appVariant.basicUpdateAttrLabel, timetag)
    maUtils.setAttrStringDatumForce(branch, appVariant.basicClassAttrLabel, sceneryClass)
    maUtils.setAttrStringDatumForce(branch, appVariant.basicNameAttrLabel, sceneryName)
    maUtils.setAttrStringDatumForce(branch, appVariant.basicVariantAttrLabel, sceneryVariant)
    maUtils.setAttrStringDatumForce(branch, appVariant.basicStageAttrLabel, sceneryStage)
    maUtils.setAttrStringDatumForce(branch, appVariant.basicIndexAttrLabel, sceneryIndex)
