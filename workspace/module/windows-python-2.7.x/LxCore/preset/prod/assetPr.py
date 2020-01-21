# coding=utf-8
from LxBasic import bscMethods, bscCommands

from LxCore import lxConfigure, lxScheme
#
from LxCore.config import assetCfg
#
from LxPreset import prsCore, prsVariants, prsMethods
#
from LxCore.preset.prod import projectPr
# do not delete and rename
serverBasicPath = lxScheme.Root().basic.server
localBasicPath = lxScheme.Root().basic.local
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
    return prsVariants.Util.Lynxi_Prefix_Product_Asset + formatString.format(*args)


# Group Name Config
def astBasicGroupNameSet(*args):
    return astBasicNameSet(*args) + prsVariants.Util.basicGroupLabel


#
def astBasicNodeNameSet(*args):
    return astBasicNameSet(*args)


#
def astBasicSetNameSet(*args):
    return astBasicNameSet(*args) + prsVariants.Util.basicSetLabel


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
    return prsVariants.Util.scnAssemblyPrefix + formatString.format(*args)


#
def astAssemblyBasicObjectNameSet(*args):
    return astUnitAssemblyBasicNameSet(*args)


#
def astRigNamespaceSet(*args):
    return astBasicNameSet(*args) + prsVariants.Util.astRigNodeLabel


#
def astSolverNamespaceSet(*args):
    return astBasicNameSet(*args) + prsVariants.Util.astSolverNodeLabel


# Group Name Config
def astNodeGroupNameSet(assetName, groupNameLabel, objectNameLabel):
    return astBasicGroupNameSet(assetName, groupNameLabel, objectNameLabel)


#
def astAssemblyProxyObjectName(assetName, namespace=none):
    return [none, namespace + ':'][namespace is not none] + astAssemblyBasicObjectNameSet(assetName) + prsVariants.Util.asbProxyFileLabel


# Compose Group Name
def astComposeRootGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsVariants.Util.basicComposeRootGroupLabel)
    return string


# Model Root Group Name
def astModelRootGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsVariants.Util.basicModelRootGroupLabel)
    return string


#
def astRigRootGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsVariants.Util.basicRigRootGroupLabel)
    return string


#
def astCfxRootGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsVariants.Util.basicCfxRootGroupLabel)
    return string


# Product Nde_Geometry Group Name
def astUnitModelProductGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsVariants.Util.basicGeometryGroupLabel)
    return string


# Solver Group Name
def astUnitModelSolverGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsVariants.Util.basicSolverGeometrySubGroupLabel)
    return string


#
def astUnitModelReferenceGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsVariants.Util.basicModelReferenceGroupLabel)
    return string


#
def astUnitModelBridgeGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsVariants.Util.basicModelBridgeGroupLabel)
    return string


#
def astUnitRigBridgeGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsVariants.Util.basicRigBridgeGroupLabel)
    return string


#
def astUnitSolverBridgeGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsVariants.Util.basicSolverBridgeGroupLabel)
    return string


# Rig Solver Link Group
def astUnitRigSolFurSubGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsVariants.Util.astFurSolverGroupLabel)
    return string


# Solver Group Name
def astUnitCfxFurCollisionFieldGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsVariants.Util.astRigSolFurCollisionFieldGroupLabel)
    return string


#
def astUnitModelSolClothFieldGroupName(assetName):
    string = astBasicGroupNameSet(assetName, prsVariants.Util.basicSolverClothFieldGroupLabel)
    return string


#
def astUnitModelSolHairFieldGroupName(assetName):
    string = astBasicGroupNameSet(assetName, prsVariants.Util.basicSolverHairFieldGroupLabel)
    return string


# Solver Group Name
def scAstCfxTempGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsVariants.Util.basicCfxLinkGroupLabel + '_temp')
    return string


# Solver Group Name
def scAstSolverTempGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsVariants.Util.basicSolverGeometrySubGroupLabel + '_temp')
    return string


#
def yetiGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, prsVariants.Util.basicCfxLinkGroupLabel)
    return string


#
def cfxSetName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicSetNameSet(assetName, prsVariants.Util.basicCfxLinkGroupLabel)
    return string


#
def solverCollisionFieldGroupName(assetName):
    string = astBasicGroupNameSet(assetName, prsVariants.Util.basicCollisionFieldGroupLabel)
    return string


#
def yetiNodeGroupName(assetName, namespace=none):
    subLabel = prsVariants.Util.astYetiNodeGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def guideSystemGroupName(assetName, namespace=none):
    subLabel = prsVariants.Util.astYetiGuideSolverNodeGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def guideFollicleGroupName(assetName):
    subLabel = prsVariants.Util.astYetiGuideFollicleGroupLabel
    string = astBasicGroupNameSet(assetName, subLabel)
    return string


#
def guideLocalCurveGroupName(assetName):
    subLabel = prsVariants.Util.astPfxHairLocalCurveNodeLabel
    string = astBasicGroupNameSet(assetName, subLabel)
    return string


#
def guideCurveGroupName(assetName):
    subLabel = prsVariants.Util.astYetiGuideCurveGroupLabel
    string = astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astPfxHairNodeGroupName(assetName, namespace=none):
    subLabel = prsVariants.Util.astPfxHairGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitCfxNhrFieldGroupName(assetName, namespace=none):
    subLabel = prsVariants.Util.astCfxFurNhrFieldGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astCfxNurbsHairNodeGroupName(assetName, namespace=none):
    subLabel = prsVariants.Util.astCfxFurNhrObjectGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astCfxNhrGrowObjectGroupName(assetName, namespace=none):
    subLabel = prsVariants.Util.astCfxFurNhrGrowGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitCfxNhrGuideObjectGroupName(assetName, namespace=none):
    subLabel = prsVariants.Util.astCfxFurNhrGuideGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitRigSolFurFieldGroupName(assetName, namespace=none):
    subLabel = prsVariants.Util.astRigSolFurFieldGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitRigSolNhrFieldGroupName(assetName, namespace=none):
    subLabel = prsVariants.Util.astRigSolNhrFieldGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitRigSolNhrSubGroupName(assetName, namespace=none):
    subLabel = prsVariants.Util.astRigSolNhrSubGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitSolverGrowFieldSubGroupName(assetName, namespace=none):
    subLabel = prsVariants.Util.astSolverGrowFieldSubGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitRigSolNhrGuideObjectGroupName(assetName, namespace=none):
    subLabel = prsVariants.Util.astRigSolNhrSolGuideGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitRigSolNhrCurveObjectGroupName(assetName, namespace=none):
    subLabel = prsVariants.Util.astRigSolNhrSolCurveGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
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
    subLabel = prsVariants.Util.astSolverGrowSourceGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
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
    subLabel = prsVariants.Util.astSolverGrowDeformGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
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
    subLabel = prsVariants.Util.astPfxHairSolverNodeGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitCfxGrowFieldSubGroupName(assetName, namespace=none):
    subLabel = prsVariants.Util.astCfxGrowFieldSubGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitCfxGrowSourceObjectGroupName(assetName, namespace=none):
    subLabel = prsVariants.Util.astCfxGrowSourceGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
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
    subLabel = prsVariants.Util.astCfxGrowDeformGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
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
        prsVariants.Util.Lynxi_Prefix_Product_Asset, assetName, number, variant, prsVariants.Util.astCfxProductFileLabel, prsVariants.Util.basicGroupLabel
    )
    return string


#
def astModelContainerName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicNameSet(assetName, prsVariants.Util.scModelNodeLabel, prsVariants.Util.astContainerNodeLabel)
    return string


#
def astCfxContainerName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicNameSet(assetName, prsVariants.Util.basicCharacterFxLinkLabel, prsVariants.Util.astContainerNodeLabel)
    return string


#
def astSolverContainerName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicNameSet(assetName, prsVariants.Util.basicSolverLinkLabel, prsVariants.Util.astContainerNodeLabel)
    return string


#
def astRootGroupHierarchyConfig(assetName):
    dic = bscCommands.orderedDict()
    dic[prsMethods.Asset.rootName(assetName)] = []
    return dic


# Pro Group Config
def astModelLinkHierarchyConfig(assetName):
    dic = bscCommands.orderedDict()
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
    dic = bscCommands.orderedDict()
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
    gpuName = '%s_%s%s' % (assetName, number, prsVariants.Util.asbGpuFileLabel)
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
    dic = bscCommands.orderedDict()
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
    dic = bscCommands.orderedDict()
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
    dic = bscCommands.orderedDict()
    dic[prsMethods.Asset.modelLinkGroupName(assetName)] = [
        astUnitModelReferenceGroupName(assetName)
    ]
    return dic


#
def astRigLinkHierarchyConfig(assetName):
    dic = bscCommands.orderedDict()
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
    astFurYetiGroupLabel = prsVariants.Util.astFurYetiGroupLabel
    astFurMayaGroupLabel = prsVariants.Util.astFurMayaGroupLabel
    astFurNurbsGroupLabel = prsVariants.Util.astFurNurbsGroupLabel
    #
    astYetiNodeGroupLabel = prsVariants.Util.astYetiNodeGroupLabel
    astYetiGroomGroupLabel = prsVariants.Util.astYetiGroomGroupLabel
    astYetiGrowGroupLabel = prsVariants.Util.astYetiGrowGroupLabel
    astYetiReferenceGroupLabel = prsVariants.Util.astYetiReferenceGroupLabel
    astYetiGuideGroupLabel = prsVariants.Util.astYetiGuideGroupLabel
    astYetiGuideFollicleGroupLabel = prsVariants.Util.astYetiGuideFollicleGroupLabel
    astYetiGuideCurveGroupLabel = prsVariants.Util.astYetiGuideCurveGroupLabel
    astYetiGuideSolverNodeGroupLabel = prsVariants.Util.astYetiGuideSolverNodeGroupLabel
    #
    astPfxHairGroupLabel = prsVariants.Util.astPfxHairGroupLabel
    astPfxHairGrowGroupLabel = prsVariants.Util.astPfxHairGrowGroupLabel
    astPfxHairFollicleGroupLabel = prsVariants.Util.astPfxHairFollicleGroupLabel
    astPfxHairCurveGroupLabel = prsVariants.Util.astPfxHairCurveGroupLabel
    astPfxHairSolverNodeGroupLabel = prsVariants.Util.astPfxHairSolverNodeGroupLabel
    #
    astCfxFurNhrFieldGroupLabel = prsVariants.Util.astCfxFurNhrFieldGroupLabel
    #
    astCfxGrowFieldSubGroupLabel = prsVariants.Util.astCfxGrowFieldSubGroupLabel
    astCfxGrowSourceGroupLabel = prsVariants.Util.astCfxGrowSourceGroupLabel
    astCfxFurGrowTargetGroupLabel = prsVariants.Util.astCfxFurGrowTargetGroupLabel
    astCfxGrowDeformGroupLabel = prsVariants.Util.astCfxGrowDeformGroupLabel
    astCfxFurCollisionSubGroupLabel = prsVariants.Util.astCfxFurCollisionSubGroupLabel
    #
    dic = bscCommands.orderedDict()
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
    dic = bscCommands.orderedDict()
    dic[prsMethods.Asset.solverLinkGroupName(assetName)] = [
        astBasicGroupNameSet(assetName, '_rigSolControl'),
        astBasicGroupNameSet(assetName, '_rigSolSkin'),
        astBasicGroupNameSet(assetName, '_rigSolField'),
        #
        astUnitRigSolNhrSubGroupName(assetName),
        #
        astBasicGroupNameSet(assetName, prsVariants.Util.astSolverGrowFieldSubGroupLabel),
        astBasicGroupNameSet(assetName, prsVariants.Util.astRigSolCollisionSubGroupLabel)
    ]
    dic[astUnitRigSolNhrSubGroupName(assetName)] = [
        astUnitRigSolNhrFieldGroupName(assetName)
    ]
    dic[astUnitRigSolNhrFieldGroupName(assetName)] = [
        astUnitRigSolNhrGuideObjectGroupName(assetName),
        astUnitRigSolNhrCurveObjectGroupName(assetName)
    ]
    dic[astBasicGroupNameSet(assetName, prsVariants.Util.astSolverGrowFieldSubGroupLabel)] = [
        astBasicGroupNameSet(assetName, prsVariants.Util.astSolverGrowSourceGroupLabel),
        astBasicGroupNameSet(assetName, prsVariants.Util.astRigSolGrowTargetGroupLabel),
        astBasicGroupNameSet(assetName, prsVariants.Util.astSolverGrowDeformGroupLabel)
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
    dic = bscCommands.orderedDict()
    dic[prsMethods.Asset.lightLinkGroupName(assetName)] = [
        astBasicGroupNameSet(assetName, prsVariants.Util.lgtFieldLabel)
    ]
    dic[astBasicGroupNameSet(assetName, prsVariants.Util.lgtFieldLabel)] = [
        astBasicGroupNameSet(assetName, '_' + i) for i in astLightBasicLeafs()
        ]
    return dic


# Asset AR Name
def astUnitAssemblyReferenceName(assetName):
    return astUnitAssemblyBasicNameSet(assetName)


#
def assetSchemeFileConfig():
    string = '{0}/{1}/{2}/{3}'.format(prsVariants.Util.dbAssetRoot, prsVariants.Util.dbBasicFolderName, lxConfigure.LynxiSchemeExt, prsVariants.Util.dbAssetBasicKey)
    return bscMethods.OsFile.uniqueFilename(string)


#
def assetSetFileConfig(assetIndex):
    string = '{0}/{1}/{2}/{3}'.format(
        prsVariants.Util.dbAssetRoot, prsVariants.Util.dbBasicFolderName, lxConfigure.LynxiSetExt, assetIndex
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
def defaultAssetSetConfig(projectName, number=0):
    lis = [
        [('project', u'项目 ( Project(s) )'), (projectName, )],
        [('name', u'名字 ( Name )'), 'ID{}'.format(str(number).zfill(6))],
        [('variant', u'变体 ( Variant(s) )'), (prsVariants.Util.astDefaultVariant,)],
        [('classify', u'类型 ( Classify )'), prsMethods.Asset.classShownameDic()],
        [('priority', u'优先级 ( Priority )'), prsMethods.Asset.priorityNames()],
        #
        [(lxConfigure.LynxiProduct_Asset_Link_Model, u'模型制作 Model'), False],
        [(lxConfigure.LynxiProduct_Asset_Link_Rig, u'绑定制作 ( Rig )'), False],
        [(lxConfigure.LynxiProduct_Asset_Link_Groom, u'角色特效制作 ( Character FX )'), False],
        [(lxConfigure.LynxiProduct_Asset_Link_Solver, u'角色模拟制作 ( Solver )'), False],
        [(lxConfigure.LynxiProduct_Asset_Link_Light, u'资产灯光 ( Light )'), False],
        #
        [(lxConfigure.LynxiProduct_Asset_Link_Assembly, u'资产组装 ( Assembly )'), False]
    ]
    return lis


#
def getUiAssetSetDataLis(projectName, assetIndex, number=0, overrideNumber=False):
    def getDefaultData():
        return defaultAssetSetConfig(projectName, number)
    #
    def getCustomData():
        osFile = assetSetFileConfig(assetIndex)
        return bscMethods.OsJson.read(osFile)
    #
    def getDic(defaultLis, customDic):
        lis = []
        if defaultLis:
            for i in defaultLis:
                setKey, uiData = i
                setUiKey = none
                if isinstance(setKey, str) or isinstance(setKey, unicode):
                    setUiKey = bscMethods.StrCamelcase.toPrettify(setKey)
                if isinstance(setKey, tuple):
                    setKey, setUiKey = setKey
                #
                defValue = uiData
                setValue = uiData
                if isinstance(uiData, list):
                    defValue = uiData[0]
                    setValue = uiData[0]
                elif isinstance(uiData, dict):
                    defValue = uiData.values()[0][0]
                    setValue = uiData.values()[0][0]
                #
                if customDic:
                    if setKey in customDic:
                        setValue = customDic[setKey]
                    else:
                        if setKey == 'name':
                            setValue = 'ID{}'.format(str(number).zfill(6))
                    #
                    if overrideNumber is True:
                        if setKey == 'name':
                            setValue = 'ID{}'.format(str(number).zfill(6))
                lis.append(
                    (setKey, setUiKey, setValue, defValue, uiData)
                )
        return lis
    #
    return getDic(getDefaultData(), getCustomData())


#
def getAssetCount():
    def getCustomData():
        osFile = assetSchemeFileConfig()
        return bscMethods.OsJson.read(osFile)
    #
    def getMain(data):
        return len(data)
    #
    return getMain(getCustomData())


#
def getAssetViewName(assetIndex):
    def getCustomData():
        osFile = assetSchemeFileConfig()
        return bscMethods.OsJson.read(osFile)
    #
    def getSubDic(data):
        dic = bscCommands.orderedDict()
        if data:
            for i in data:
                scheme, enable, description = i
                dic[scheme] = description
        return dic
    #
    def getMain(customDic):
        string = lxConfigure.LynxiValue_Unspecified
        if assetIndex in customDic:
            string = customDic[assetIndex]
        return string
    #
    return getMain(getSubDic(getCustomData()))


#
def getAssetClass(assetIndex):
    def getCustomData():
        osFile = assetSetFileConfig(assetIndex)
        return bscMethods.OsJson.read(osFile)
    #
    def getMain(customDic):
        if customDic:
            return customDic['classify']
    #
    return getMain(getCustomData())


#
def getAssetName(assetIndex):
    def getCustomData():
        osFile = assetSetFileConfig(assetIndex)
        return bscMethods.OsJson.read(osFile)
    #
    def getMain(customDic):
        if customDic:
            return customDic['name']
    #
    return getMain(getCustomData())


#
def getAssetPriority(assetIndex):
    def getCustomData():
        osFile = assetSetFileConfig(assetIndex)
        return bscMethods.OsJson.read(osFile)
    #
    def getMain(customDic):
        if customDic:
            return customDic['priority']
    #
    return getMain(getCustomData())


#
def getAssetVariantLis(assetIndex):
    def getCustomData():
        osFile = assetSetFileConfig(assetIndex)
        return bscMethods.OsJson.read(osFile)
    #
    def getMain(customDic):
        if customDic:
            return customDic['variant']
    #
    return getMain(getCustomData())


#
def getAssetIsLinkEnable(assetIndex, assetLink):
    def getCustomData():
        osFile = assetSetFileConfig(assetIndex)
        return bscMethods.OsJson.read(osFile)
    #
    def getMain(customDic):
        if customDic:
            return customDic[assetLink]
    #
    return getMain(getCustomData())


#
def getAssetIsAssemblyEnabled(assetIndex):
    def getCustomData():
        osFile = assetSetFileConfig(assetIndex)
        return bscMethods.OsJson.read(osFile)
    #
    def getMain(customDic):
        if customDic:
            return customDic['assembly']
    #
    return getMain(getCustomData())


#
def assetViewInfoSet(assetViewName, assetClass, assetVariant=None):
    if assetVariant is None:
        string = u'{} {}'.format(
            prsMethods.Asset.classShowname(assetClass)[1],
            assetViewName
        )
    else:
        string = u'{} {} ( {} )'.format(
            prsMethods.Asset.classShowname(assetClass)[1],
            assetViewName,
            assetVariant
        )
    return string


#
def getAssetViewInfo(assetIndex, assetClass=None, assetVariant=None):
    if assetClass is None:
        assetClass = getAssetClass(assetIndex)
    #
    return assetViewInfoSet(getAssetViewName(assetIndex), assetClass, assetVariant)


#
def getAssetNamesFilter(projectFilter, assetClassFilters=None):
    def getCustomData():
        osFile = assetSchemeFileConfig()
        return bscMethods.OsJson.read(osFile)
    #
    def getBranch(lis, assetIndex):
        osFile = assetSetFileConfig(assetIndex)
        data = bscMethods.OsJson.read(osFile)
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
        osFile = assetSchemeFileConfig()
        return bscMethods.OsJson.read(osFile)
    #
    def getLinks(data):
        lis = []
        for i in prsMethods.Asset.linknames():
            enable = data[i]
            if enable is True:
                lis.append(i)
        return lis
    #
    def getBranch(dic, assetIndex, description):
        osFile = assetSetFileConfig(assetIndex)
        data = bscMethods.OsJson.read(osFile)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                isMatch = False
                #
                assetClass = data['classify']
                assetName = data['name']
                assetLinks = getLinks(data)
                if assetClassFilters is not None:
                    if assetClass in assetClassFilters:
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
        dic = bscCommands.orderedDict()
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
        osFile = assetSchemeFileConfig()
        return bscMethods.OsJson.read(osFile)
    #
    def getBranch(dic, assetIndex):
        osFile = assetSetFileConfig(assetIndex)
        data = bscMethods.OsJson.read(osFile)
        if data:
            assetName = data['name']
            dic[assetName] = assetIndex
    #
    def getMain(data):
        dic = bscCommands.orderedDict()
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
        osFile = assetSchemeFileConfig()
        return bscMethods.OsJson.read(osFile)
    #
    def getBranch(dic, assetIndex, description):
        osFile = assetSetFileConfig(assetIndex)
        data = bscMethods.OsJson.read(osFile)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                assetClass = data['classify']
                assetName = data['name']
                assetVariants = data['variant']
                assetPriority = data['priority']
                modelEnabled = bscMethods.Dict.getAsBoolean(data, lxConfigure.LynxiProduct_Asset_Link_Model)
                rigEnabled = bscMethods.Dict.getAsBoolean(data, lxConfigure.LynxiProduct_Asset_Link_Rig)
                cfxEnabled = bscMethods.Dict.getAsBoolean(data, lxConfigure.LynxiProduct_Asset_Link_Groom)
                scSolverEnable = bscMethods.Dict.getAsBoolean(data, lxConfigure.LynxiProduct_Asset_Link_Solver)
                scLightEnable = bscMethods.Dict.getAsBoolean(data, lxConfigure.LynxiProduct_Asset_Link_Light)
                assemblyEnabled = bscMethods.Dict.getAsBoolean(data, lxConfigure.LynxiProduct_Asset_Link_Assembly)
                for assetVariant in assetVariants:
                    dic[(assetIndex, assetVariant)] = description, assetClass, assetName, assetPriority, modelEnabled, rigEnabled, cfxEnabled, scSolverEnable, scLightEnable, assemblyEnabled
    #
    def getMain(data):
        dic = bscCommands.orderedDict()
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
        osFile = assetSchemeFileConfig()
        return bscMethods.OsJson.read(osFile)
    #
    def getBranch(dic, assetIndex, description):
        osFile = assetSetFileConfig(assetIndex)
        data = bscMethods.OsJson.read(osFile)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                assetClass = data['classify']
                assetName = data['name']
                assemblyEnabled = data['assembly']
                assetVariants = data['variant']
                if assemblyEnabled is True:
                    for assetVariant in assetVariants:
                        serverAstUnitAsbDefinitionFile = astUnitAssemblyDefinitionFile(
                            lxConfigure.LynxiRootIndex_Server,
                            projectFilter,
                            assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Assembly
                        )[1]
                        if bscCommands.isOsExistsFile(serverAstUnitAsbDefinitionFile):
                            dic[assetIndex] = description, assetClass, assetName, assetVariant
    #
    def getMain(data):
        dic = bscCommands.orderedDict()
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
        if prsVariants.Util.astModelFolderEnabled is True:
            string = prsVariants.Util.astModelLinkFolder
    elif prsMethods.Asset.isRigStageName(assetStage):
        if prsVariants.Util.astRigFolderEnabled is True:
            string = prsVariants.Util.astRigLinkFolder
    elif prsMethods.Asset.isGroomStageName(assetStage):
        if prsVariants.Util.astCfxFolderEnabled is True:
            string = prsVariants.Util.astCfxLinkFolder
    elif prsMethods.Asset.isSolverStageName(assetStage):
        if prsVariants.Util.astSolverFolderEnabled is True:
            string = prsVariants.Util.astSolverFolder
    elif prsMethods.Asset.isLightStageName(assetStage):
        if prsVariants.Util.astLightFolderEnabled is True:
            string = prsVariants.Util.astLightLinkFolder
    elif prsMethods.Asset.isAssemblyStageName(assetStage):
        if prsVariants.Util.astAssemblyFolderEnabled is True:
            string = prsVariants.Util.astAssemblyLinkFolder
    return string


#
def astBasicLinkLabel(assetStage):
    string = prsVariants.Util.basicModelLinkLabel
    if prsMethods.Asset.isModelStageName(assetStage):
        string = prsVariants.Util.basicModelLinkLabel
    elif prsMethods.Asset.isRigStageName(assetStage):
        string = prsVariants.Util.basicRigLinkLabel
    elif prsMethods.Asset.isGroomStageName(assetStage):
        string = prsVariants.Util.basicCharacterFxLinkLabel
    elif prsMethods.Asset.isSolverStageName(assetStage):
        string = prsVariants.Util.basicSolverLinkLabel
    elif prsMethods.Asset.isLightStageName(assetStage):
        string = prsVariants.Util.basicLightLinkLabel
    elif prsMethods.Asset.isAssemblyStageName(assetStage):
        string = prsVariants.Util.basicAssemblyLinkLabel
    return string


#
def astBasicTextureFolder(assetStage):
    string = none
    if prsMethods.Asset.isModelStageName(assetStage):
        string = prsVariants.Util.astModelTextureFolder
    elif prsMethods.Asset.isRigStageName(assetStage):
        string = prsVariants.Util.astRigTextureFolder
    elif prsMethods.Asset.isGroomStageName(assetStage):
        string = prsVariants.Util.astCfxTextureFolder
    elif prsMethods.Asset.isSolverStageName(assetStage):
        string = prsVariants.Util.astSolverTextureFolder
    elif prsMethods.Asset.isLightStageName(assetStage):
        string = prsVariants.Util.astLightTextureFolder
    elif prsMethods.Asset.isAssemblyStageName(assetStage):
        string = prsVariants.Util.astAssemblyTextureFolder
    return string


#
def astBasicMapFolder(assetStage):
    mainLabel = astBasicLinkLabel(assetStage)
    if mainLabel.startswith('_'):
        mainLabel = mainLabel[1:]
    #
    subLabel = prsVariants.Util.basicMapSubLabel
    return bscMethods.StrUnderline.toLabel(mainLabel, subLabel)


#
def astBasicCacheFolder(assetStage):
    mainLabel = astBasicLinkLabel(assetStage)
    if mainLabel.startswith('_'):
        mainLabel = mainLabel[1:]
    #
    subLabel = prsVariants.Util.basicCacheSubLabel
    return bscMethods.StrUnderline.toLabel(mainLabel, subLabel)


#
def astBasicSourceFileLabel(assetStage):
    subLabel = prsVariants.Util.basicSourceSubLabel
    return bscMethods.StrUnderline.toLabel(astBasicLinkLabel(assetStage), subLabel)


#
def astBasicProductFileLabel(assetStage):
    if prsMethods.Asset.isRigStageName(assetStage):
        return prsVariants.Util.astAnimationRigFileLabel
    else:
        subLabel = prsVariants.Util.basicProductSubLabel
        return bscMethods.StrUnderline.toLabel(astBasicLinkLabel(assetStage), subLabel)


#
def astBasicAsbDefinitionFileLabel(assetStage):
    subLabel = prsVariants.Util.basicAssemblyDefinitionSubLabel
    return bscMethods.StrUnderline.toLabel(astBasicLinkLabel(assetStage), subLabel)


#
def astAssetFurFileLabel(assetStage):
    subLabel = prsVariants.Util.basicFurSubLabel
    return bscMethods.StrUnderline.toLabel(astBasicLinkLabel(assetStage), subLabel)


#
def assetPreviewFileLabel(assetStage):
    subLabel = prsVariants.Util.basicPreviewSubLabel
    return bscMethods.StrUnderline.toLabel(astBasicLinkLabel(assetStage), subLabel)


#
def astBasicOsFileNameConfig(assetName, fileLabel, extLabel):
    string = '{}{}{}'.format(assetName, fileLabel, extLabel)
    return string


# Asset Path
def astUnitBasicDirectory(rootIndexKey, projectName):
    root = [prsVariants.Util.serverAssetRoot, prsVariants.Util.localAssetRoot, prsVariants.Util.backupAssetRoot]
    directory = '%s/%s/%s/%s' % (root[rootIndexKey], projectName, prsVariants.Util.basicAssetFolder, prsVariants.Util.basicUnitFolder)
    return directory


# Asset Path
def astUnitAssemblyBasicDirectory(rootIndexKey, projectName):
    root = [prsVariants.Util.serverAssetRoot, prsVariants.Util.localAssetRoot, prsVariants.Util.backupAssetRoot]
    directory = '%s/%s/%s/%s' % (root[rootIndexKey], projectName, prsVariants.Util.basicAssemblyFolder, prsVariants.Util.basicUnitFolder)
    return directory


#
def basicUnitFolder(
        rootIndexKey,
        projectName,
        assetClass, assetName
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    osPath = '%s/%s' % (
        basicDirectory,
        assetName
    )
    return osPath


#
def astUnitAssemblyFolder(rootIndexKey, projectName, assetClass, assetName):
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
        assetClass, assetName, assetVariant, assetStage
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
        assetClass, assetName, assetVariant, assetStage
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
        assetClass, assetName, assetVariant, assetStage
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
        assetClass, assetName, assetVariant, assetStage):
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
        assetClass, assetName, assetVariant, assetStage):
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
        assetClass, assetName, assetVariant, assetStage):
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
        assetClass, assetName, assetVariant, assetStage):
    if prsMethods.Asset.isAssemblyStageName(assetStage):
        basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    else:
        basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    #
    fileLabel = astBasicProductFileLabel(assetStage)
    extLabel = prsVariants.Util.dbTextureUnitKey
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    osFile = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, osFile


#
def astUnitLogFile(
        rootIndexKey,
        projectName,
        assetClass, assetName, assetVariant, assetStage):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    #
    fileLabel = astBasicProductFileLabel(assetStage)
    extLabel = prsVariants.Util.logExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    osFile = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, osFile


#
def astUnitSourceFile(
        rootIndexKey,
        projectName,
        assetClass, assetName, assetVariant, assetStage):
    if prsMethods.Asset.isAssemblyStageName(assetStage):
        basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    else:
        basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    #
    fileLabel = astBasicSourceFileLabel(assetStage)
    extLabel = prsVariants.Util.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    osFile = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, osFile


#
def astUnitProductFile(
        rootIndexKey,
        projectName,
        assetClass, assetName, assetVariant, assetStage
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    #
    fileLabel = astBasicProductFileLabel(assetStage)
    extLabel = prsVariants.Util.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    osFile = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, osFile


#
def astUnitAssemblyIndexDatum(assetIndex, assetClass, assetName):
    return {
        lxConfigure.LynxiInfoKey_Index: assetIndex,
        lxConfigure.LynxiInfoKey_Class: assetClass,
        lxConfigure.LynxiInfoKey_Name: assetName
    }


#
def astUnitAssemblyIndexFile(
        projectName,
        assetName
):
    basicDirectory = astUnitAssemblyBasicDirectory(lxConfigure.LynxiRootIndex_Server, projectName)
    fileLabel = ''
    extLabel = prsVariants.Util.astAssemblyIndexExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    keyVars = [basicDirectory, assetName, osFileName]
    osFile = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, osFile


#
def astUnitAssemblyProductFile(projectName, assetName, assetVariant):
    basicDirectory = astUnitAssemblyBasicDirectory(lxConfigure.LynxiRootIndex_Server, projectName)
    #
    fileLabel = bscMethods.StrUnderline.toLabel(prsVariants.Util.basicAssemblyLinkLabel, prsVariants.Util.basicProductSubLabel)
    extLabel = prsVariants.Util.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    keyVars = [basicDirectory, assetName, assetVariant, osFileName]
    osFile = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, osFile


#
def astUnitAssemblyDefinitionFile(rootIndexKey, projectName, assetClass, assetName, assetVariant, assetStage):
    basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    #
    fileLabel = astBasicAsbDefinitionFileLabel(assetStage)
    extLabel = prsVariants.Util.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, osFileName]
    osFile = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, osFile


#
def astUnitAssemblyProxyCacheFile(projectName, assetName, assetVariant, lod=0):
    basicDirectory = astUnitAssemblyBasicDirectory(lxConfigure.LynxiRootIndex_Server, projectName)
    #
    if lod == 0:
        fileLabel = prsVariants.Util.asbProxyFileLabel
    else:
        fileLabel = prsVariants.Util.asbProxyFileLabel + '_lod%s' % str(lod).zfill(2)
    #
    extLabel = projectPr.getProjectProxyExt(projectName)
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    keyVars = [basicDirectory, assetName, assetVariant, osFileName]
    osFile = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, osFile


#
def astUnitAssemblyProxyFile(projectName, assetName, assetVariant, lod=0):
    basicDirectory = astUnitAssemblyBasicDirectory(lxConfigure.LynxiRootIndex_Server, projectName)
    #
    if lod == 0:
        fileLabel = prsVariants.Util.asbProxyFileLabel
    else:
        fileLabel = prsVariants.Util.asbProxyFileLabel + '_lod%s' % str(lod).zfill(2)
    #
    extLabel = prsVariants.Util.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    keyVars = [basicDirectory, assetName, assetVariant, osFileName]
    osFile = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, osFile


#
def astUnitAssemblyGpuCacheFile(projectName, assetName, lod=0):
    basicDirectory = astUnitAssemblyBasicDirectory(lxConfigure.LynxiRootIndex_Server, projectName)
    if lod == 0:
        fileLabel = prsVariants.Util.asbGpuFileLabel
    else:
        fileLabel = prsVariants.Util.asbGpuFileLabel + '_lod%s' % str(lod).zfill(2)
    #
    extLabel = prsVariants.Util.gpuCacheExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    keyVars = [basicDirectory, assetName, osFileName]
    osFile = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, osFile


#
def astUnitAssemblyBoxCacheFile(projectName, assetName):
    basicDirectory = astUnitAssemblyBasicDirectory(lxConfigure.LynxiRootIndex_Server, projectName)
    fileLabel = prsVariants.Util.asbBoxFileLabel
    #
    extLabel = prsVariants.Util.gpuCacheExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    keyVars = [basicDirectory, assetName, osFileName]
    osFile = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, osFile


#
def astUnitFurFile(
        rootIndexKey,
        projectName,
        assetClass, assetName, assetVariant, assetStage
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    #
    fileLabel = astAssetFurFileLabel(assetStage)
    extLabel = prsVariants.Util.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    osFile = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, osFile


#
def astUnitExtraFile(
        rootIndexKey,
        projectName,
        assetClass, assetName, assetVariant, assetStage
):
    if prsMethods.Asset.isAssemblyStageName(assetStage):
        basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    else:
        basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    fileLabel = astBasicProductFileLabel(assetStage)
    extLabel = prsVariants.Util.dbExtraUnitKey
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if prsMethods.Asset.isRigStageName(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    osFile = bscMethods.OsPath.composeBy(keyVars)
    return osFileName, osFile


def astUnitBasicPreviewFile(
        rootIndexKey,
        projectName,
        assetClass, assetName
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    fileLabel = ''
    extLabel = prsVariants.Util.dbPreviewUnitKey
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    osFile = '{0}/{1}/{2}'.format(
        basicDirectory,
        assetName,
        osFileName
    )
    return osFileName, osFile


#
def astUnitPreviewFile(
        rootIndexKey,
        projectName,
        assetClass, assetName, assetVariant, assetStage,
        extLabel=prsVariants.Util.jpgExt
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    fileLabel = assetPreviewFileLabel(assetStage)
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        assetName, assetVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def astUnitBasicMeshConstantFile(
        rootIndexKey,
        projectName,
        assetClass, assetName
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    fileLabel = ''
    extLabel = prsVariants.Util.dbMeshUnitKey
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    osFile = '{0}/{1}/{2}'.format(
        basicDirectory,
        assetName,
        osFileName
    )
    return osFileName, osFile


#
def astUnitMeshConstantFile(
        rootIndexKey,
        projectName,
        assetClass, assetName, assetVariant, assetStage
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    fileLabel = astBasicProductFileLabel(assetStage)
    extLabel = prsVariants.Util.dbMeshUnitKey
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        assetName, assetVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def astUnitTextureConstantFile(
        rootIndexKey,
        projectName,
        assetClass, assetName, assetVariant, assetStage
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    fileLabel = astBasicProductFileLabel(assetStage)
    extLabel = prsVariants.Util.dbTextureUnitKey
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        assetName, assetVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def getAssetMeshConstantDatumDic(projectName, assetClass, assetName, assetStage):
    pass


#
def getAssetUnitProductUpdate(projectName, assetClass, assetName, assetVariant, assetStage):
    string = prsVariants.Util.infoNonExistsLabel
    #
    serverProductFile = astUnitProductFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    #
    if bscCommands.isOsExistsFile(serverProductFile):
        data = bscMethods.OsFile.mtimeChnPrettify(serverProductFile)
        if data:
            string = data
    return string


#
def getAstUnitProductActiveTimeTag(projectName, assetClass, assetName, assetVariant, assetStage):
    serverProductFile = astUnitProductFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    return bscMethods.OsFile.mtimetag(serverProductFile)


#
def getAssetUnitExtraData(projectName, assetClass, assetName, assetVariant, assetStage):
    dic = bscCommands.orderedDict()
    extraFile = astUnitExtraFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    if bscCommands.isOsExistsFile(extraFile):
        data = bscMethods.OsJson.read(extraFile)
        if data:
            dic = data
    return dic


#
def getAstTdUploadCommand(projectName, link):
    dataDic = projectPr.getProjectMayaTdPresetDic(projectName)
    if dataDic:
        if link in dataDic:
            data = dataDic[link]
            if data:
                mayaPackageStr = data[lxConfigure.LynxiMayaScriptKey]
                #
                var = ''
                pathCmd = bscCommands.toVariantConvert('var', mayaPackageStr)
                exec pathCmd
                #
                if var:
                    if bscCommands.isOsExist(var):
                        osFile = var + '/' + lxConfigure.LynxiAssetUploadCommandKey + '.py'
                        if bscCommands.isOsExist(osFile):
                            command = bscMethods.OsFile.read(osFile)
                            pythonCommand = 'python(' + bscMethods.OsJson.dump(command) + ');'
                            #
                            return pythonCommand


#
def getAstTdLoadCommand(projectName, link):
    dataDic = projectPr.getProjectMayaTdPresetDic(projectName)
    if dataDic:
        if link in dataDic:
            data = dataDic[link]
            if data:
                mayaPackageStr = data[lxConfigure.LynxiMayaScriptKey]
                #
                var = ''
                pathCmd = bscCommands.toVariantConvert('var', mayaPackageStr)
                exec pathCmd
                #
                if var:
                    if bscCommands.isOsExist(var):
                        osFile = var + '/' + lxConfigure.LynxiAssetLoadCommandKey + '.py'
                        if bscCommands.isOsExist(osFile):
                            command = bscMethods.OsFile.read(osFile)
                            pythonCommand = 'python(' + bscMethods.OsJson.dump(command) + ');'
                            #
                            return pythonCommand
