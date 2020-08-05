# coding=utf-8
from LxBasic import bscMtdCore, bscMethods

from LxScheme import shmOutput
#
from LxPreset import prsConfigure, prsOutputs, prsMethods
# do not delete and rename
serverBasicPath = shmOutput.Root().basic.server
localBasicPath = shmOutput.Root().basic.local
#
none = ''


#
def astBasicNameSet(*args):
    formatString = ''
    for i in args:
        if isinstance(i, str) or isinstance(i, unicode):
            if not i.startswith('_'):
                j = '_{}'
            else:
                j = '{}'
            formatString += j
    return prsOutputs.Util.Lynxi_Prefix_Product_Asset + formatString.format(*args)


# Group Name Config
def astBasicGroupNameSet(*args):
    return astBasicNameSet(*args) + prsOutputs.Util.basicGroupLabel


#
def astBasicNodeNameSet(*args):
    return astBasicNameSet(*args)


#
def astBasicSetNameSet(*args):
    return astBasicNameSet(*args) + prsOutputs.Util.basicSetLabel


#
def astBasicObjectNameSet(*args):
    return astBasicNameSet(*args)


#
def astUnitAssemblyBasicNameSet(*args):
    formatString = ''
    for i in args:
        if isinstance(i, str) or isinstance(i, unicode):
            if not i.startswith('_'):
                j = '_{}'
            else:
                j = '{}'
            formatString += j
    return prsOutputs.Util.scnAssemblyPrefix + formatString.format(*args)


#
def astAssemblyBasicObjectNameSet(*args):
    return astUnitAssemblyBasicNameSet(*args)


#
def astRigNamespaceSet(*args):
    return astBasicNameSet(*args) + prsOutputs.Util.astRigNodeLabel


#
def astSolverNamespaceSet(*args):
    return astBasicNameSet(*args) + prsOutputs.Util.astSolverNodeLabel


# Group Name Config
def astNodeGroupNameSet(assetName, groupNameLabel, objectNameLabel):
    return astBasicGroupNameSet(assetName, groupNameLabel, objectNameLabel)


#
def astAssemblyProxyObjectName(assetName, namespace=none):
    return [none, namespace + ':'][namespace is not none] + astAssemblyBasicObjectNameSet(assetName) + prsOutputs.Util.asbProxyFileLabel


# Compose Group Name
def astComposeRootGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsOutputs.Util.basicComposeRootGroupLabel)
    return string


# Model Root Group Name
def astModelRootGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsOutputs.Util.basicModelRootGroupLabel)
    return string


#
def astRigRootGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsOutputs.Util.basicRigRootGroupLabel)
    return string


#
def astCfxRootGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsOutputs.Util.basicCfxRootGroupLabel)
    return string


# Product Nde_Geometry Group Name
def astUnitModelProductGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsOutputs.Util.basicGeometryGroupLabel)
    return string


# Solver Group Name
def astUnitModelSolverGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsOutputs.Util.basicSolverGeometrySubGroupLabel)
    return string


#
def astUnitModelReferenceGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsOutputs.Util.basicModelReferenceGroupLabel)
    return string


#
def astUnitModelBridgeGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsOutputs.Util.basicModelBridgeGroupLabel)
    return string


#
def astUnitRigBridgeGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsOutputs.Util.basicRigBridgeGroupLabel)
    return string


#
def astUnitSolverBridgeGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsOutputs.Util.basicSolverBridgeGroupLabel)
    return string


# Rig Solver Link Group
def astUnitRigSolFurSubGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsOutputs.Util.astFurSolverGroupLabel)
    return string


# Solver Group Name
def astUnitCfxFurCollisionFieldGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsOutputs.Util.astRigSolFurCollisionFieldGroupLabel)
    return string


#
def astUnitModelSolClothFieldGroupName(assetName):
    string = astBasicGroupNameSet(assetName, prsOutputs.Util.basicSolverClothFieldGroupLabel)
    return string


#
def astUnitModelSolHairFieldGroupName(assetName):
    string = astBasicGroupNameSet(assetName, prsOutputs.Util.basicSolverHairFieldGroupLabel)
    return string


# Solver Group Name
def scAstCfxTempGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsOutputs.Util.basicCfxLinkGroupLabel + '_temp')
    return string


# Solver Group Name
def scAstSolverTempGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsOutputs.Util.basicSolverGeometrySubGroupLabel + '_temp')
    return string


#
def yetiGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsOutputs.Util.basicCfxLinkGroupLabel)
    return string


#
def cfxSetName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicSetNameSet(assetName, prsOutputs.Util.basicCfxLinkGroupLabel)
    return string


#
def solverCollisionFieldGroupName(assetName):
    string = astBasicGroupNameSet(assetName, prsOutputs.Util.basicCollisionFieldGroupLabel)
    return string


#
def yetiNodeGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astYetiNodeGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def guideSystemGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astYetiGuideSolverNodeGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def guideFollicleGroupName(assetName):
    subLabelString = prsOutputs.Util.astYetiGuideFollicleGroupLabel
    string = astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def guideLocalCurveGroupName(assetName):
    subLabelString = prsOutputs.Util.astPfxHairLocalCurveNodeLabel
    string = astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def guideCurveGroupName(assetName):
    subLabelString = prsOutputs.Util.astYetiGuideCurveGroupLabel
    string = astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astPfxHairNodeGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astPfxHairGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astUnitCfxNhrFieldGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astCfxFurNhrFieldGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astCfxNurbsHairNodeGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astCfxFurNhrObjectGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astCfxNhrGrowObjectGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astCfxFurNhrGrowGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astUnitCfxNhrGuideObjectGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astCfxFurNhrGuideGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astUnitRigSolFurFieldGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astRigSolFurFieldGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astUnitRigSolNhrFieldGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astRigSolNhrFieldGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astUnitRigSolNhrSubGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astRigSolNhrSubGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astUnitSolverGrowFieldSubGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astSolverGrowFieldSubGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astUnitRigSolNhrGuideObjectGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astRigSolNhrSolGuideGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astUnitRigSolNhrCurveObjectGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astRigSolNhrSolCurveGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astUnitRigSolNhrSolGuideObjectGroupPath(assetName, namespace=none):
    return '|'.join(
        [
            astUnitRigSolNhrFieldGroupName(assetName, namespace),
            astUnitRigSolNhrGuideObjectGroupName(assetName, namespace)
        ]
    )


#
def astUnitSolverGrowSourceObjectGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astSolverGrowSourceGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astUnitSolverGrowSourceObjectGroupPath(assetName, namespace=none):
    return '|'.join(
        [
            prsMethods.Asset.solverLinkGroupName(assetName, namespace),
            astUnitSolverGrowFieldSubGroupName(assetName, namespace),
            astUnitSolverGrowSourceObjectGroupName(assetName, namespace)
        ]
    )


#
def astUnitSolverGrowDeformObjectGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astSolverGrowDeformGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astUnitSolverGrowDeformObjectGroupPath(assetName, namespace=none):
    return '|'.join(
        [
            prsMethods.Asset.solverLinkGroupName(assetName, namespace),
            astUnitSolverGrowFieldSubGroupName(assetName, namespace),
            astUnitSolverGrowDeformObjectGroupName(assetName, namespace)
        ]
    )


#
def pfxSystemGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astPfxHairSolverNodeGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astUnitCfxGrowFieldSubGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astCfxGrowFieldSubGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astUnitCfxGrowSourceObjectGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astCfxGrowSourceGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astUnitCfxGroupSourceGroupPath(assetName, namespace=none):
    return '|'.join(
        [
            prsMethods.Asset.groomLinkGroupName(assetName, namespace),
            astUnitCfxGrowFieldSubGroupName(assetName, namespace),
            astUnitCfxGrowSourceObjectGroupName(assetName, namespace)
        ]
    )


#
def astUnitCfxGrowDeformObjectGroupName(assetName, namespace=none):
    subLabelString = prsOutputs.Util.astCfxGrowDeformGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabelString)
    return string


#
def astUnitCfxGrowDeformObjectGroupPath(assetName, namespace=none):
    return '|'.join(
        [
            prsMethods.Asset.groomLinkGroupName(assetName, namespace),
            astUnitCfxGrowFieldSubGroupName(assetName, namespace),
            astUnitCfxGrowDeformObjectGroupName(assetName, namespace)
        ]
    )


# Asset Namespace
def furAssetGroupName(assetName, number, variant):
    string = '%s_%s_%s_%s%s%s' % (
        prsOutputs.Util.Lynxi_Prefix_Product_Asset, assetName, number, variant, prsOutputs.Util.astCfxProductFileLabel, prsOutputs.Util.basicGroupLabel
    )
    return string


#
def astModelContainerName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicNameSet(assetName, prsOutputs.Util.scModelNodeLabel, prsOutputs.Util.astContainerNodeLabel)
    return string


#
def astCfxContainerName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicNameSet(assetName, prsOutputs.Util.basicCharacterFxLinkLabel, prsOutputs.Util.astContainerNodeLabel)
    return string


#
def astSolverContainerName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicNameSet(assetName, prsOutputs.Util.basicSolverLinkLabel, prsOutputs.Util.astContainerNodeLabel)
    return string


#
def astRootGroupHierarchyConfig(assetName):
    dic = bscMtdCore.orderedDict()
    dic[prsMethods.Asset.rootName(assetName)] = []
    return dic


# Pro Group Config
def astModelLinkHierarchyConfig(assetName):
    dic = bscMtdCore.orderedDict()
    #
    dic[prsMethods.Asset.modelLinkGroupName(assetName)] = [
        astUnitModelProductGroupName(assetName),
        astUnitModelSolverGroupName(assetName),
        astUnitModelReferenceGroupName(assetName),
        astUnitModelBridgeGroupName(assetName)
    ]
    return dic


#
def astModelCharHierarchyConfig(assetName):
    dic = bscMtdCore.orderedDict()
    dic[prsMethods.Asset.modelLinkGroupName(assetName)] = [
        astUnitModelProductGroupName(assetName)
    ]
    dic[astUnitModelProductGroupName(assetName)] = [
        astBasicGroupNameSet(assetName, '_headField'),
        astBasicGroupNameSet(assetName, '_bodyField'),
        astBasicGroupNameSet(assetName, '_clothField'),
    ]
    dic[astBasicGroupNameSet(assetName, '_headField')] = [
        astBasicGroupNameSet(assetName, '_head'),
        astBasicGroupNameSet(assetName, '_hair'),
        astBasicGroupNameSet(assetName, '_brow'),
        astBasicGroupNameSet(assetName, '_lash'),
        astBasicGroupNameSet(assetName, '_eye'),
        astBasicGroupNameSet(assetName, '_ear'),
        astBasicGroupNameSet(assetName, '_mouth'),
        astBasicGroupNameSet(assetName, '_beard'),
        astBasicGroupNameSet(assetName, '_headTar')
    ]
    dic[astBasicGroupNameSet(assetName, '_brow')] = [
        astBasicGroupNameSet(assetName, '_L_brow'),
        astBasicGroupNameSet(assetName, '_R_brow')
    ]
    dic[astBasicGroupNameSet(assetName, '_lash')] = [
        astBasicGroupNameSet(assetName, '_L_upLash'),
        astBasicGroupNameSet(assetName, '_L_lowLash'),
        astBasicGroupNameSet(assetName, '_L_tearGland'),
        astBasicGroupNameSet(assetName, '_R_upLash'),
        astBasicGroupNameSet(assetName, '_R_lowLash'),
        astBasicGroupNameSet(assetName, '_R_tearGland')
    ]
    dic[astBasicGroupNameSet(assetName, '_eye')] = [
        astBasicGroupNameSet(assetName, '_L_eyeIn'),
        astBasicGroupNameSet(assetName, '_L_eyeOut'),
        astBasicGroupNameSet(assetName, '_R_eyeIn'),
        astBasicGroupNameSet(assetName, '_R_eyeOut'),
    ]
    dic[astBasicGroupNameSet(assetName, '_ear')] = [
        astBasicGroupNameSet(assetName, '_L_ear'),
        astBasicGroupNameSet(assetName, '_L_earring'),
        astBasicGroupNameSet(assetName, '_R_ear'),
        astBasicGroupNameSet(assetName, '_R_earring')
    ]
    dic[astBasicGroupNameSet(assetName, '_mouth')] = [
        astBasicGroupNameSet(assetName, '_upTeeth'),
        astBasicGroupNameSet(assetName, '_tongue'),
        astBasicGroupNameSet(assetName, '_lowTeeth')
    ]
    dic[astBasicGroupNameSet(assetName, '_headTar')] = [
        astBasicGroupNameSet(assetName, '_closeEye'),
        astBasicGroupNameSet(assetName, '_openEye')
    ]
    dic[astBasicGroupNameSet(assetName, '_bodyField')] = [
        astBasicGroupNameSet(assetName, '_body'),
        astBasicGroupNameSet(assetName, '_arm'),
        astBasicGroupNameSet(assetName, '_hand'),
        astBasicGroupNameSet(assetName, '_leg'),
        astBasicGroupNameSet(assetName, '_foot')
    ]
    dic[astBasicGroupNameSet(assetName, '_arm')] = [
        astBasicGroupNameSet(assetName, '_L_arm'),
        astBasicGroupNameSet(assetName, '_R_arm')
    ]
    dic[astBasicGroupNameSet(assetName, '_hand')] = [
        astBasicGroupNameSet(assetName, '_L_hand'),
        astBasicGroupNameSet(assetName, '_R_hand')
    ]
    dic[astBasicGroupNameSet(assetName, '_leg')] = [
        astBasicGroupNameSet(assetName, '_L_leg'),
        astBasicGroupNameSet(assetName, '_R_leg')
    ]
    dic[astBasicGroupNameSet(assetName, '_foot')] = [
        astBasicGroupNameSet(assetName, '_L_foot'),
        astBasicGroupNameSet(assetName, '_R_foot')
    ]
    dic[astBasicGroupNameSet(assetName, '_clothField')] = [
        astBasicGroupNameSet(assetName, '_upCloth'),
        astBasicGroupNameSet(assetName, '_lowCloth'),
        astBasicGroupNameSet(assetName, '_headAss'),
        astBasicGroupNameSet(assetName, '_bodyAss'),
        astBasicGroupNameSet(assetName, '_glove'),
        astBasicGroupNameSet(assetName, '_shoe')
    ]
    dic[astBasicGroupNameSet(assetName, '_glove')] = [
        astBasicGroupNameSet(assetName, '_L_glove'),
        astBasicGroupNameSet(assetName, '_R_glove')
    ]
    dic[astBasicGroupNameSet(assetName, '_shoe')] = [
        astBasicGroupNameSet(assetName, '_L_shoe'),
        astBasicGroupNameSet(assetName, '_R_shoe')
    ]
    return dic


#
def astGpuName(assetName, number):
    gpuName = '%s_%s%s' % (assetName, number, prsOutputs.Util.asbGpuFileLabel)
    return gpuName


#
def astPropBasicLeafs():
    lis = [
        'prop_base',
        'prop_part',
    ]
    return lis


#
def astPropBuildBasicLeafs():
    lis = [
        'buildBase',
        'buildBody',
        'buildWindow',
        'buildGlass',
        'buildEmission'
    ]
    return lis


#
def astPropHierarchyConfig(assetName):
    dic = bscMtdCore.orderedDict()
    dic[prsMethods.Asset.modelLinkGroupName(assetName)] = [
        astUnitModelProductGroupName(assetName)
    ]
    dic[astUnitModelProductGroupName(assetName)] = [
        astBasicGroupNameSet(assetName, '_propField'),
        astBasicGroupNameSet(assetName, '_buildField')
    ]
    dic[astBasicGroupNameSet(assetName, '_propField')] = [
        astBasicGroupNameSet(assetName, '_' + i) for i in astPropBasicLeafs()
        ]
    dic[astBasicGroupNameSet(assetName, '_buildField')] = [
        astBasicGroupNameSet(assetName, '_' + i) for i in astPropBuildBasicLeafs()
    ]
    return dic


#
def astSolverClothBasicLeafs():
    lis = [
        'solCloth_base',
        'solCloth_part',
    ]
    return lis


#
def astSolverHairBasicLeafs():
    lis = [
        'solHair_base',
        'solHair_part'
    ]
    return lis


#
def astModelSolverHierarchyConfig(assetName):
    dic = bscMtdCore.orderedDict()
    dic[prsMethods.Asset.modelLinkGroupName(assetName)] = [
        astUnitModelSolverGroupName(assetName)
    ]
    dic[astUnitModelSolverGroupName(assetName)] = [
        astUnitModelSolClothFieldGroupName(assetName),
        astUnitModelSolHairFieldGroupName(assetName),
        solverCollisionFieldGroupName(assetName)
    ]
    dic[astUnitModelSolClothFieldGroupName(assetName)] = [
        astBasicGroupNameSet(assetName, '_' + i) for i in astSolverClothBasicLeafs()
    ]
    dic[astUnitModelSolHairFieldGroupName(assetName)] = [
        astBasicGroupNameSet(assetName, '_' + i) for i in astSolverHairBasicLeafs()
    ]
    dic[solverCollisionFieldGroupName(assetName)] = [
        astBasicGroupNameSet(assetName, '_clothCollision')
    ]
    return dic


#
def astModelReferenceHierarchyConfig(assetName):
    dic = bscMtdCore.orderedDict()
    dic[prsMethods.Asset.modelLinkGroupName(assetName)] = [
        astUnitModelReferenceGroupName(assetName)
    ]
    return dic


#
def astRigLinkHierarchyConfig(assetName):
    dic = bscMtdCore.orderedDict()
    # Main
    dic[prsMethods.Asset.rigLinkGroupName(assetName)] = [
        astBasicGroupNameSet(assetName, '_rigControl'),
        astBasicGroupNameSet(assetName, '_rigSkin'),
        # Bridge
        astUnitRigBridgeGroupName(assetName),
        astUnitSolverBridgeGroupName(assetName),
        #
        astBasicGroupNameSet(assetName, '_rigField')
    ]
    # Skin
    dic[astBasicGroupNameSet(assetName, '_rigSkin')] = [
        astBasicGroupNameSet(assetName, '_skinTarget'),
        astBasicGroupNameSet(assetName, '_skinDeform')
    ]
    return dic


#
def astCfxHierarchyConfig(assetName):
    astFurYetiGroupLabel = prsOutputs.Util.astFurYetiGroupLabel
    astFurMayaGroupLabel = prsOutputs.Util.astFurMayaGroupLabel
    astFurNurbsGroupLabel = prsOutputs.Util.astFurNurbsGroupLabel
    #
    astYetiNodeGroupLabel = prsOutputs.Util.astYetiNodeGroupLabel
    astYetiGroomGroupLabel = prsOutputs.Util.astYetiGroomGroupLabel
    astYetiGrowGroupLabel = prsOutputs.Util.astYetiGrowGroupLabel
    astYetiReferenceGroupLabel = prsOutputs.Util.astYetiReferenceGroupLabel
    astYetiGuideGroupLabel = prsOutputs.Util.astYetiGuideGroupLabel
    astYetiGuideFollicleGroupLabel = prsOutputs.Util.astYetiGuideFollicleGroupLabel
    astYetiGuideCurveGroupLabel = prsOutputs.Util.astYetiGuideCurveGroupLabel
    astYetiGuideSolverNodeGroupLabel = prsOutputs.Util.astYetiGuideSolverNodeGroupLabel
    #
    astPfxHairGroupLabel = prsOutputs.Util.astPfxHairGroupLabel
    astPfxHairGrowGroupLabel = prsOutputs.Util.astPfxHairGrowGroupLabel
    astPfxHairFollicleGroupLabel = prsOutputs.Util.astPfxHairFollicleGroupLabel
    astPfxHairCurveGroupLabel = prsOutputs.Util.astPfxHairCurveGroupLabel
    astPfxHairSolverNodeGroupLabel = prsOutputs.Util.astPfxHairSolverNodeGroupLabel
    #
    astCfxFurNhrFieldGroupLabel = prsOutputs.Util.astCfxFurNhrFieldGroupLabel
    #
    astCfxGrowFieldSubGroupLabel = prsOutputs.Util.astCfxGrowFieldSubGroupLabel
    astCfxGrowSourceGroupLabel = prsOutputs.Util.astCfxGrowSourceGroupLabel
    astCfxFurGrowTargetGroupLabel = prsOutputs.Util.astCfxFurGrowTargetGroupLabel
    astCfxGrowDeformGroupLabel = prsOutputs.Util.astCfxGrowDeformGroupLabel
    astCfxFurCollisionSubGroupLabel = prsOutputs.Util.astCfxFurCollisionSubGroupLabel
    #
    dic = bscMtdCore.orderedDict()
    # Main
    dic[prsMethods.Asset.groomLinkGroupName(assetName)] = [
        astBasicGroupNameSet(assetName, astFurYetiGroupLabel),
        astBasicGroupNameSet(assetName, astFurMayaGroupLabel),
        astBasicGroupNameSet(assetName, astFurNurbsGroupLabel),
        #
        astBasicGroupNameSet(assetName, astCfxGrowFieldSubGroupLabel),
        astBasicGroupNameSet(assetName, astCfxFurCollisionSubGroupLabel)
    ]
    # Yeti
    dic[astBasicGroupNameSet(assetName, astFurYetiGroupLabel)] = [
        astBasicGroupNameSet(assetName, astYetiNodeGroupLabel),
        astBasicGroupNameSet(assetName, astYetiGroomGroupLabel),
        astBasicGroupNameSet(assetName, astYetiGrowGroupLabel),
        astBasicGroupNameSet(assetName, astYetiReferenceGroupLabel),
        astBasicGroupNameSet(assetName, astYetiGuideGroupLabel)
    ]
    # Yeti Guide
    dic[astBasicGroupNameSet(assetName, astYetiGuideGroupLabel)] = [
        astBasicGroupNameSet(assetName, astYetiGuideSolverNodeGroupLabel),
        astBasicGroupNameSet(assetName, astYetiGuideFollicleGroupLabel),
        astBasicGroupNameSet(assetName, astYetiGuideCurveGroupLabel)
    ]
    # Pfx Hair
    dic[astBasicGroupNameSet(assetName, astFurMayaGroupLabel)] = [
        astBasicGroupNameSet(assetName, astPfxHairGroupLabel),
        astBasicGroupNameSet(assetName, astPfxHairGrowGroupLabel),
        astBasicGroupNameSet(assetName, astPfxHairFollicleGroupLabel),
        astBasicGroupNameSet(assetName, astPfxHairCurveGroupLabel),
        astBasicGroupNameSet(assetName, astPfxHairSolverNodeGroupLabel)
    ]
    # Nurbs Hair
    dic[astBasicGroupNameSet(assetName, astFurNurbsGroupLabel)] = [
        astBasicGroupNameSet(assetName, astCfxFurNhrFieldGroupLabel),
    ]
    # Field
    dic[astBasicGroupNameSet(assetName, astCfxGrowFieldSubGroupLabel)] = [
        astBasicGroupNameSet(assetName, astCfxGrowSourceGroupLabel),
        astBasicGroupNameSet(assetName, astCfxFurGrowTargetGroupLabel),
        astBasicGroupNameSet(assetName, astCfxGrowDeformGroupLabel)
    ]
    return dic


#
def astRigSolverHierarchyConfig(assetName):
    dic = bscMtdCore.orderedDict()
    dic[prsMethods.Asset.solverLinkGroupName(assetName)] = [
        astBasicGroupNameSet(assetName, '_rigSolControl'),
        astBasicGroupNameSet(assetName, '_rigSolSkin'),
        astBasicGroupNameSet(assetName, '_rigSolField'),
        #
        astUnitRigSolNhrSubGroupName(assetName),
        #
        astBasicGroupNameSet(assetName, prsOutputs.Util.astSolverGrowFieldSubGroupLabel),
        astBasicGroupNameSet(assetName, prsOutputs.Util.astRigSolCollisionSubGroupLabel)
    ]
    dic[astUnitRigSolNhrSubGroupName(assetName)] = [
        astUnitRigSolNhrFieldGroupName(assetName)
    ]
    dic[astUnitRigSolNhrFieldGroupName(assetName)] = [
        astUnitRigSolNhrGuideObjectGroupName(assetName),
        astUnitRigSolNhrCurveObjectGroupName(assetName)
    ]
    dic[astBasicGroupNameSet(assetName, prsOutputs.Util.astSolverGrowFieldSubGroupLabel)] = [
        astBasicGroupNameSet(assetName, prsOutputs.Util.astSolverGrowSourceGroupLabel),
        astBasicGroupNameSet(assetName, prsOutputs.Util.astRigSolGrowTargetGroupLabel),
        astBasicGroupNameSet(assetName, prsOutputs.Util.astSolverGrowDeformGroupLabel)
    ]
    return dic


#
def astLightBasicLeafs():
    lis = [
        'linkLightField',
        'keyLight',
        'fillLight',
        'rimLight',
        'meshLightField'
    ]
    return lis


#
def astLightHierarchyConfig(assetName):
    dic = bscMtdCore.orderedDict()
    dic[prsMethods.Asset.lightLinkGroupName(assetName)] = [
        astBasicGroupNameSet(assetName, prsOutputs.Util.lgtFieldLabel)
    ]
    dic[astBasicGroupNameSet(assetName, prsOutputs.Util.lgtFieldLabel)] = [
        astBasicGroupNameSet(assetName, '_' + i) for i in astLightBasicLeafs()
        ]
    return dic


# Asset AR Name
def astUnitAssemblyReferenceName(assetName):
    return astUnitAssemblyBasicNameSet(assetName)


#
def assetSchemeFileConfig():
    string = '{0}/{1}/{2}/{3}'.format(
        prsOutputs.Util.dbAssetRoot,
        prsOutputs.Util.dbBasicFolderName,
        prsConfigure.Utility.LynxiSchemeExt,
        prsOutputs.Util.dbAssetBasicKey
    )
    return bscMethods.OsFile.uniqueName(string)


#
def assetSetFileConfig(assetIndex):
    string = '{0}/{1}/{2}/{3}'.format(
        prsOutputs.Util.dbAssetRoot,
        prsOutputs.Util.dbBasicFolderName,
        prsConfigure.Utility.LynxiSetExt,
        assetIndex
    )
    return string


#
def defaultAssetSchemeConfig():
    lis = [
        True,
        u'请输入备注'
    ]
    return lis


#
def getAssetCount():
    def getCustomData():
        fileString_ = assetSchemeFileConfig()
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getMain(data):
        return len(data)
    #
    return getMain(getCustomData())


#
def getAssetViewName(assetIndex):
    def getCustomData():
        fileString_ = assetSchemeFileConfig()
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getSubDic(data):
        dic = bscMtdCore.orderedDict()
        if data:
            for i in data:
                scheme, enable, description = i
                dic[scheme] = description
        return dic
    #
    def getMain(customDic):
        string = prsConfigure.Utility.DEF_value_preset_unspecified
        if assetIndex in customDic:
            string = customDic[assetIndex]
        return string
    #
    return getMain(getSubDic(getCustomData()))


#
def getAssetClass(assetIndex):
    def getCustomData():
        fileString_ = assetSetFileConfig(assetIndex)
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic['classify']
    #
    return getMain(getCustomData())


#
def getAssetName(assetIndex):
    def getCustomData():
        fileString_ = assetSetFileConfig(assetIndex)
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic['name']
    #
    return getMain(getCustomData())


#
def getAssetPriority(assetIndex):
    def getCustomData():
        fileString_ = assetSetFileConfig(assetIndex)
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic['priority']
    #
    return getMain(getCustomData())


#
def getAssetVariantLis(assetIndex):
    def getCustomData():
        fileString_ = assetSetFileConfig(assetIndex)
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic['variant']
    #
    return getMain(getCustomData())


#
def getAssetIsLinkEnable(assetIndex, assetLink):
    def getCustomData():
        fileString_ = assetSetFileConfig(assetIndex)
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic[assetLink]
    #
    return getMain(getCustomData())


#
def getAssetIsAssemblyEnabled(assetIndex):
    def getCustomData():
        fileString_ = assetSetFileConfig(assetIndex)
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic['assembly']
    #
    return getMain(getCustomData())


#
def assetViewInfoSet(assetViewName, assetCategory, assetVariant=None):
    if assetVariant is None:
        string = u'{} {}'.format(
            prsMethods.Asset.categoryShowname(assetCategory),
            assetViewName
        )
    else:
        string = u'{} {} ( {} )'.format(
            prsMethods.Asset.categoryShowname(assetCategory),
            assetViewName,
            assetVariant
        )
    return string


#
def getAssetViewInfo(assetIndex, assetCategory=None, assetVariant=None):
    if assetCategory is None:
        assetCategory = getAssetClass(assetIndex)
    #
    return assetViewInfoSet(getAssetViewName(assetIndex), assetCategory, assetVariant)


#
def getAssetNamesFilter(projectFilter, assetClassFilters=None):
    def getCustomData():
        fileString_ = assetSchemeFileConfig()
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getBranch(lis, assetIndex):
        fileString_ = assetSetFileConfig(assetIndex)
        data = bscMethods.OsJsonFile.read(fileString_)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                isMatch = False
                #
                dbAssetClass = data['classify']
                dbAssetName = data['name']
                if assetClassFilters is not None:
                    if dbAssetClass in assetClassFilters:
                        isMatch = True
                elif assetClassFilters is None:
                    isMatch = True
                #
                if isMatch is True:
                    lis.append(dbAssetName)
    #
    def getMain(data):
        lis = []
        if data:
            for i in data:
                assetIndex, enable, description = i
                if enable is True:
                    getBranch(lis, assetIndex)
        return lis
    #
    return getMain(getCustomData())


#
def getUiAssetMultMsgDic(projectFilter, assetClassFilters=None, assetLinkFilter=None):
    def getCustomData():
        fileString_ = assetSchemeFileConfig()
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getLinks(data):
        lis = []
        for i in prsMethods.Asset.linkNames():
            enable = data[i]
            if enable is True:
                lis.append(i)
        return lis
    #
    def getBranch(dic, assetIndex, description):
        fileString_ = assetSetFileConfig(assetIndex)
        data = bscMethods.OsJsonFile.read(fileString_)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                isMatch = False
                #
                assetCategory = data['classify']
                assetName = data['name']
                assetLinks = getLinks(data)
                if assetClassFilters is not None:
                    if assetCategory in assetClassFilters:
                        if assetLinkFilter is not None:
                            if assetLinkFilter in assetLinks:
                                isMatch = True
                        elif assetLinkFilter is None:
                            isMatch = True
                elif assetClassFilters is None:
                    if assetLinkFilter is not None:
                        if assetLinkFilter in assetLinks:
                            isMatch = True
                    elif assetLinkFilter is None:
                        isMatch = True
                #
                if isMatch is True:
                    dic[assetIndex] = assetName, description
    #
    def getMain(data):
        dic = bscMtdCore.orderedDict()
        if data:
            for i in data:
                assetIndex, enable, description = i
                if enable is True:
                    getBranch(dic, assetIndex, description)
        return dic
    return getMain(getCustomData())


#
def getAssetIndexDic():
    def getCustomData():
        fileString_ = assetSchemeFileConfig()
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getBranch(dic, assetIndex):
        fileString_ = assetSetFileConfig(assetIndex)
        data = bscMethods.OsJsonFile.read(fileString_)
        if data:
            assetName = data['name']
            dic[assetName] = assetIndex
    #
    def getMain(data):
        dic = bscMtdCore.orderedDict()
        if data:
            for i in data:
                assetIndex, enable, description = i
                if enable is True:
                    getBranch(dic, assetIndex)
        return dic
    #
    return getMain(getCustomData())


#
def getUiAssetSetDataDic(projectFilter):
    def getCustomData():
        fileString_ = assetSchemeFileConfig()
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getBranch(dic, assetIndex, description):
        fileString_ = assetSetFileConfig(assetIndex)
        data = bscMethods.OsJsonFile.read(fileString_)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                assetCategory = data['classify']
                assetName = data['name']
                assetVariants = data['variant']
                assetPriority = data['priority']
                modelEnabled = bscMethods.Dict.getAsBoolean(data, prsMethods.Asset.modelLinkName())
                rigEnabled = bscMethods.Dict.getAsBoolean(data, prsMethods.Asset.rigLinkName())
                cfxEnabled = bscMethods.Dict.getAsBoolean(data, prsMethods.Asset.groomLinkName())
                scSolverEnable = bscMethods.Dict.getAsBoolean(data, prsMethods.Asset.solverLinkName())
                scLightEnable = bscMethods.Dict.getAsBoolean(data, prsMethods.Asset.lightLinkName())
                assemblyEnabled = bscMethods.Dict.getAsBoolean(data, prsMethods.Asset.assemblyLinkName())
                for assetVariant in assetVariants:
                    dic[(assetIndex, assetVariant)] = description, assetCategory, assetName, assetPriority, modelEnabled, rigEnabled, cfxEnabled, scSolverEnable, scLightEnable, assemblyEnabled
    #
    def getMain(data):
        dic = bscMtdCore.orderedDict()
        if data:
            for i in data:
                assetIndex, enable, description = i
                if enable is True:
                    getBranch(dic, assetIndex, description)
        return dic
    return getMain(getCustomData())


#
def getAstUnitAssemblyDic(projectFilter):
    def getCustomData():
        fileString_ = assetSchemeFileConfig()
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getBranch(dic, assetIndex, description):
        fileString_ = assetSetFileConfig(assetIndex)
        data = bscMethods.OsJsonFile.read(fileString_)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                assetCategory = data['classify']
                assetName = data['name']
                assemblyEnabled = data['assembly']
                assetVariants = data['variant']
                if assemblyEnabled is True:
                    for assetVariant in assetVariants:
                        serverAstUnitAsbDefinitionFile = astUnitAssemblyDefinitionFile(
                            prsConfigure.Utility.DEF_value_root_server,
                            projectFilter,
                            assetCategory, assetName, assetVariant, prsMethods.Asset.assemblyLinkName()
                        )[1]
                        if bscMethods.OsFile.isExist(serverAstUnitAsbDefinitionFile):
                            dic[assetIndex] = description, assetCategory, assetName, assetVariant
    #
    def getMain(data):
        dic = bscMtdCore.orderedDict()
        if data:
            for i in data:
                assetIndex, enable, description = i
                if enable is True:
                    getBranch(dic, assetIndex, description)
        return dic
    return getMain(getCustomData())


#
def astBasicLinkFolder(assetStage):
    string = none
    if prsMethods.Asset.isModelStageName(assetStage):
        if prsOutputs.Util.astModelFolderEnabled is True:
            string = prsOutputs.Util.astModelLinkFolder
    elif prsMethods.Asset.isRigStageName(assetStage):
        if prsOutputs.Util.astRigFolderEnabled is True:
            string = prsOutputs.Util.astRigLinkFolder
    elif prsMethods.Asset.isGroomStageName(assetStage):
        if prsOutputs.Util.astCfxFolderEnabled is True:
            string = prsOutputs.Util.astCfxLinkFolder
    elif prsMethods.Asset.isSolverStageName(assetStage):
        if prsOutputs.Util.astSolverFolderEnabled is True:
            string = prsOutputs.Util.astSolverFolder
    elif prsMethods.Asset.isLightStageName(assetStage):
        if prsOutputs.Util.astLightFolderEnabled is True:
            string = prsOutputs.Util.astLightLinkFolder
    elif prsMethods.Asset.isAssemblyStageName(assetStage):
        if prsOutputs.Util.astAssemblyFolderEnabled is True:
            string = prsOutputs.Util.astAssemblyLinkFolder
    return string


#
def astBasicLinkLabel(assetStage):
    string = prsOutputs.Util.basicModelLinkLabel
    if prsMethods.Asset.isModelStageName(assetStage):
        string = prsOutputs.Util.basicModelLinkLabel
    elif prsMethods.Asset.isRigStageName(assetStage):
        string = prsOutputs.Util.basicRigLinkLabel
    elif prsMethods.Asset.isGroomStageName(assetStage):
        string = prsOutputs.Util.basicCharacterFxLinkLabel
    elif prsMethods.Asset.isSolverStageName(assetStage):
        string = prsOutputs.Util.basicSolverLinkLabel
    elif prsMethods.Asset.isLightStageName(assetStage):
        string = prsOutputs.Util.basicLightLinkLabel
    elif prsMethods.Asset.isAssemblyStageName(assetStage):
        string = prsOutputs.Util.basicAssemblyLinkLabel
    return string


#
def astBasicTextureFolder(assetStage):
    string = none
    if prsMethods.Asset.isModelStageName(assetStage):
        string = prsOutputs.Util.astModelTextureFolder
    elif prsMethods.Asset.isRigStageName(assetStage):
        string = prsOutputs.Util.astRigTextureFolder
    elif prsMethods.Asset.isGroomStageName(assetStage):
        string = prsOutputs.Util.astCfxTextureFolder
    elif prsMethods.Asset.isSolverStageName(assetStage):
        string = prsOutputs.Util.astSolverTextureFolder
    elif prsMethods.Asset.isLightStageName(assetStage):
        string = prsOutputs.Util.astLightTextureFolder
    elif prsMethods.Asset.isAssemblyStageName(assetStage):
        string = prsOutputs.Util.astAssemblyTextureFolder
    return string


#
def astBasicMapFolder(assetStage):
    mainLabel = astBasicLinkLabel(assetStage)
    if mainLabel.startswith('_'):
        mainLabel = mainLabel[1:]
    #
    subLabelString = prsOutputs.Util.basicMapSubLabel
    return bscMethods.StrUnderline.toLabel(mainLabel, subLabelString)


#
def astBasicCacheFolder(assetStage):
    mainLabel = astBasicLinkLabel(assetStage)
    if mainLabel.startswith('_'):
        mainLabel = mainLabel[1:]
    #
    subLabelString = prsOutputs.Util.basicCacheSubLabel
    return bscMethods.StrUnderline.toLabel(mainLabel, subLabelString)


#
def astBasicSourceFileLabel(assetStage):
    subLabelString = prsOutputs.Util.basicSourceSubLabel
    return bscMethods.StrUnderline.toLabel(astBasicLinkLabel(assetStage), subLabelString)


#
def astBasicProductFileLabel(assetStage):
    if prsMethods.Asset.isRigStageName(assetStage):
        return prsOutputs.Util.astAnimationRigFileLabel
    else:
        subLabelString = prsOutputs.Util.basicProductSubLabel
        return bscMethods.StrUnderline.toLabel(astBasicLinkLabel(assetStage), subLabelString)


#
def astBasicAsbDefinitionFileLabel(assetStage):
    subLabelString = prsOutputs.Util.basicAssemblyDefinitionSubLabel
    return bscMethods.StrUnderline.toLabel(astBasicLinkLabel(assetStage), subLabelString)


#
def astAssetFurFileLabel(assetStage):
    subLabelString = prsOutputs.Util.basicFurSubLabel
    return bscMethods.StrUnderline.toLabel(astBasicLinkLabel(assetStage), subLabelString)


#
def assetPreviewFileLabel(assetStage):
    subLabelString = prsOutputs.Util.basicPreviewSubLabel
    return bscMethods.StrUnderline.toLabel(astBasicLinkLabel(assetStage), subLabelString)


#
def astBasicOsFileNameConfig(assetName, fileLabel, extLabel):
    string = '{}{}{}'.format(assetName, fileLabel, extLabel)
    return string


# Asset Path
def astUnitBasicDirectory(rootIndexKey, projectName):
    root = [prsOutputs.Util.serverAssetRoot, prsOutputs.Util.localAssetRoot, prsOutputs.Util.backupAssetRoot]
    directory = '%s/%s/%s/%s' % (root[rootIndexKey], projectName, prsOutputs.Util.basicAssetFolder, prsOutputs.Util.basicUnitFolder)
    return directory


# Asset Path
def astUnitAssemblyBasicDirectory(rootIndexKey, projectName):
    root = [prsOutputs.Util.serverAssetRoot, prsOutputs.Util.localAssetRoot, prsOutputs.Util.backupAssetRoot]
    directory = '%s/%s/%s/%s' % (root[rootIndexKey], projectName, prsOutputs.Util.basicAssemblyFolder, prsOutputs.Util.basicUnitFolder)
    return directory


#
def basicUnitFolder(
        rootIndexKey,
        projectName,
        assetCategory, assetName
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    osPath = '%s/%s' % (
        basicDirectory,
        assetName
    )
    return osPath


#
def astUnitAssemblyFolder(rootIndexKey, projectName, assetCategory, assetName):
    basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    #
    osPath = '%s/%s' % (
        basicDirectory,
        assetName
    )
    return osPath


#
def astUnitTextureFolder(
        rootIndexKey,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    #
    osFolderName = astBasicTextureFolder(assetStage)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFolderName]
    
    osFolder = bscMethods.OsPath.composeBy(keyVars)
    return osFolder


#
def astUnitMapFolder(
        rootIndexKey,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    #
    osFolderName = astBasicMapFolder(assetStage)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFolderName]
    osFolder = bscMethods.OsPath.composeBy(keyVars)
    return osFolder


#
def astUnitAssemblyTextureFolder(
        rootIndexKey,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
):
    basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    #
    osFolderName = astBasicTextureFolder(assetStage)
    #
    keyVars = [basicDirectory, assetName, assetVariant, osFolderName]
    osFolder = bscMethods.OsPath.composeBy(keyVars)
    return osFolder


#
def astUnitAssemblyMapFolder(
        rootIndexKey,
        projectName,
        assetCategory, assetName, assetVariant, assetStage):
    basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    #
    osFolderName = astBasicMapFolder(assetStage)
    #
    keyVars = [basicDirectory, assetName, assetVariant, osFolderName]
    osFolder = bscMethods.OsPath.composeBy(keyVars)
    return osFolder


#
def astUnitCacheFolder(
        rootIndexKey,
        projectName,
        assetCategory, assetName, assetVariant, assetStage):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    #
    osFolderName = astBasicCacheFolder(assetStage)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFolderName]
    osFolder = bscMethods.OsPath.composeBy(keyVars)
    return osFolder


#
def astUnitAssemblyCacheFolder(
        rootIndexKey,
        projectName,
        assetCategory, assetName, assetVariant, assetStage):
    basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    #
    osFolderName = astBasicCacheFolder(assetStage)
    #
    keyVars = [basicDirectory, assetName, assetVariant, osFolderName]
    osFolder = bscMethods.OsPath.composeBy(keyVars)
    return osFolder


#
def astUnitTextureIndexFile(
        rootIndexKey,
        projectName,
        assetCategory, assetName, assetVariant, assetStage):
    if prsMethods.Asset.isAssemblyStageName(assetStage):
        basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    else:
        basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    #
    fileLabel = astBasicProductFileLabel(assetStage)
    extLabel = prsOutputs.Util.dbTextureUnitKey
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    fileString_ = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, fileString_


#
def astUnitLogFile(
        rootIndexKey,
        projectName,
        assetCategory, assetName, assetVariant, assetStage):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    #
    fileLabel = astBasicProductFileLabel(assetStage)
    extLabel = prsOutputs.Util.logExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    fileString_ = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, fileString_


#
def astUnitSourceFile(
        rootIndexKey,
        projectName,
        assetCategory, assetName, assetVariant, assetStage):
    if prsMethods.Asset.isAssemblyStageName(assetStage):
        basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    else:
        basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    #
    fileLabel = astBasicSourceFileLabel(assetStage)
    extLabel = prsOutputs.Util.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    fileString_ = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, fileString_


#
def astUnitProductFile(
        rootIndexKey,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    #
    fileLabel = astBasicProductFileLabel(assetStage)
    extLabel = prsOutputs.Util.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    fileString_ = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, fileString_


#
def astUnitAssemblyIndexDatum(assetIndex, assetCategory, assetName):
    return {
        prsConfigure.Product.DEF_key_info_index: assetIndex,
        prsConfigure.Product.DEF_key_info_category: assetCategory,
        prsConfigure.Product.DEF_key_info_name: assetName
    }


#
def astUnitAssemblyIndexFile(
        projectName,
        assetName
):
    basicDirectory = astUnitAssemblyBasicDirectory(prsConfigure.Utility.DEF_value_root_server, projectName)
    fileLabel = ''
    extLabel = prsOutputs.Util.astAssemblyIndexExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    keyVars = [basicDirectory, assetName, osFileName]
    fileString_ = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, fileString_


#
def astUnitAssemblyProductFile(projectName, assetName, assetVariant):
    basicDirectory = astUnitAssemblyBasicDirectory(prsConfigure.Utility.DEF_value_root_server, projectName)
    #
    fileLabel = bscMethods.StrUnderline.toLabel(prsOutputs.Util.basicAssemblyLinkLabel, prsOutputs.Util.basicProductSubLabel)
    extLabel = prsOutputs.Util.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    keyVars = [basicDirectory, assetName, assetVariant, osFileName]
    fileString_ = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, fileString_


#
def astUnitAssemblyDefinitionFile(rootIndexKey, projectName, assetCategory, assetName, assetVariant, assetStage):
    basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    #
    fileLabel = astBasicAsbDefinitionFileLabel(assetStage)
    extLabel = prsOutputs.Util.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, osFileName]
    fileString_ = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, fileString_


#
def astUnitAssemblyProxyCacheFile(projectName, assetName, assetVariant, lod=0):
    basicDirectory = astUnitAssemblyBasicDirectory(prsConfigure.Utility.DEF_value_root_server, projectName)
    #
    if lod == 0:
        fileLabel = prsOutputs.Util.asbProxyFileLabel
    else:
        fileLabel = prsOutputs.Util.asbProxyFileLabel + '_lod%s' % str(lod).zfill(2)
    #
    extLabel = prsMethods.Project.mayaProxyExt(projectName)
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    keyVars = [basicDirectory, assetName, assetVariant, osFileName]
    fileString_ = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, fileString_


#
def astUnitAssemblyProxyFile(projectName, assetName, assetVariant, lod=0):
    basicDirectory = astUnitAssemblyBasicDirectory(prsConfigure.Utility.DEF_value_root_server, projectName)
    #
    if lod == 0:
        fileLabel = prsOutputs.Util.asbProxyFileLabel
    else:
        fileLabel = prsOutputs.Util.asbProxyFileLabel + '_lod%s' % str(lod).zfill(2)
    #
    extLabel = prsOutputs.Util.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    keyVars = [basicDirectory, assetName, assetVariant, osFileName]
    fileString_ = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, fileString_


#
def astUnitAssemblyGpuCacheFile(projectName, assetName, lod=0):
    basicDirectory = astUnitAssemblyBasicDirectory(prsConfigure.Utility.DEF_value_root_server, projectName)
    if lod == 0:
        fileLabel = prsOutputs.Util.asbGpuFileLabel
    else:
        fileLabel = prsOutputs.Util.asbGpuFileLabel + '_lod%s' % str(lod).zfill(2)
    #
    extLabel = prsOutputs.Util.gpuCacheExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    keyVars = [basicDirectory, assetName, osFileName]
    fileString_ = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, fileString_


#
def astUnitAssemblyBoxCacheFile(projectName, assetName):
    basicDirectory = astUnitAssemblyBasicDirectory(prsConfigure.Utility.DEF_value_root_server, projectName)
    fileLabel = prsOutputs.Util.asbBoxFileLabel
    #
    extLabel = prsOutputs.Util.gpuCacheExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    keyVars = [basicDirectory, assetName, osFileName]
    fileString_ = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, fileString_


#
def astUnitFurFile(
        rootIndexKey,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    #
    fileLabel = astAssetFurFileLabel(assetStage)
    extLabel = prsOutputs.Util.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    fileString_ = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, fileString_


#
def astUnitExtraFile(
        rootIndexKey,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
):
    if prsMethods.Asset.isAssemblyStageName(assetStage):
        basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    else:
        basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    fileLabel = astBasicProductFileLabel(assetStage)
    extLabel = prsOutputs.Util.dbExtraUnitKey
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    fileString_ = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, fileString_


def astUnitBasicPreviewFile(
        rootIndexKey,
        projectName,
        assetCategory, assetName
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    fileLabel = ''
    extLabel = prsOutputs.Util.dbPreviewUnitKey
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    fileString_ = '{0}/{1}/{2}'.format(
        basicDirectory,
        assetName,
        osFileName
    )
    return osFileName, fileString_


#
def astUnitPreviewFile(
        rootIndexKey,
        projectName,
        assetCategory, assetName, assetVariant, assetStage,
        extLabel=prsOutputs.Util.jpgExt
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    fileLabel = assetPreviewFileLabel(assetStage)
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        assetName, assetVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def astUnitBasicMeshConstantFile(
        rootIndexKey,
        projectName,
        assetCategory, assetName
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    fileLabel = ''
    extLabel = prsOutputs.Util.dbMeshUnitKey
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    fileString_ = '{0}/{1}/{2}'.format(
        basicDirectory,
        assetName,
        osFileName
    )
    return osFileName, fileString_


#
def astUnitMeshConstantFile(
        rootIndexKey,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    fileLabel = astBasicProductFileLabel(assetStage)
    extLabel = prsOutputs.Util.dbMeshUnitKey
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        assetName, assetVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def astUnitTextureConstantFile(
        rootIndexKey,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    fileLabel = astBasicProductFileLabel(assetStage)
    extLabel = prsOutputs.Util.dbTextureUnitKey
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        assetName, assetVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def getAssetMeshConstantDatumDic(projectName, assetCategory, assetName, assetStage):
    pass


#
def getAssetUnitProductUpdate(projectName, assetCategory, assetName, assetVariant, assetStage):
    string = prsOutputs.Util.infoNonExistsLabel
    #
    serverProductFile = astUnitProductFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )[1]
    #
    if bscMethods.OsFile.isExist(serverProductFile):
        data = bscMethods.OsFile.mtimeChnPrettify(serverProductFile)
        if data:
            string = data
    return string


#
def getAstUnitProductActiveTimeTag(projectName, assetCategory, assetName, assetVariant, assetStage):
    serverProductFile = astUnitProductFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )[1]
    return bscMethods.OsFile.mtimetag(serverProductFile)


#
def getAssetUnitExtraData(projectName, assetCategory, assetName, assetVariant, assetStage):
    dic = bscMtdCore.orderedDict()
    extraFile = astUnitExtraFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName,
        assetCategory, assetName, assetVariant, assetStage
    )[1]
    if bscMethods.OsFile.isExist(extraFile):
        data = bscMethods.OsJsonFile.read(extraFile)
        if data:
            dic = data
    return dic


#
def getAstTdUploadCommand(projectName, link):
    dataDic = prsMethods.Project.mayaTdPresetDict(projectName)
    if dataDic:
        if link in dataDic:
            data = dataDic[link]
            if data:
                mayaPackageStr = data[prsConfigure.Utility.LynxiMayaScriptKey]
                #
                var = ''
                pathCmd = bscMethods.Variant.covertTo('var', mayaPackageStr)
                exec pathCmd
                #
                if var:
                    if bscMethods.OsDirectory.isExist(var):
                        fileString_ = var + '/' + prsConfigure.Utility.LynxiAssetUploadCommandKey + '.py'
                        if bscMethods.OsFile.isExist(fileString_):
                            command = bscMethods.OsFile.read(fileString_)
                            pythonCommand = 'python(' + bscMethods.OsJsonFile.dump(command) + ');'
                            #
                            return pythonCommand


#
def getAstTdLoadCommand(projectName, link):
    dataDic = prsMethods.Project.mayaTdPresetDict(projectName)
    if dataDic:
        if link in dataDic:
            data = dataDic[link]
            if data:
                mayaPackageStr = data[prsConfigure.Utility.LynxiMayaScriptKey]
                #
                var = ''
                pathCmd = bscMethods.Variant.covertTo('var', mayaPackageStr)
                exec pathCmd
                #
                if var:
                    if bscMethods.OsDirectory.isExist(var):
                        fileString_ = var + '/' + prsConfigure.Utility.LynxiAssetLoadCommandKey + '.py'
                        if bscMethods.OsFile.isExist(fileString_):
                            command = bscMethods.OsFile.read(fileString_)
                            pythonCommand = 'python(' + bscMethods.OsJsonFile.dump(command) + ');'
                            #
                            return pythonCommand
