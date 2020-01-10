# coding=utf-8
from LxBasic import bscMethods

from LxCore import lxBasic, lxConfigure, lxScheme
#
from LxCore.config import assetCfg
#
from LxCore.preset import appVariant
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
    return appVariant.Lynxi_Prefix_Product_Asset + formatString.format(*args)


# Group Name Config
def astBasicGroupNameSet(*args):
    return astBasicNameSet(*args) + appVariant.basicGroupLabel


#
def astBasicNodeNameSet(*args):
    return astBasicNameSet(*args)


#
def astBasicSetNameSet(*args):
    return astBasicNameSet(*args) + appVariant.basicSetLabel


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
    return appVariant.scnAssemblyPrefix + formatString.format(*args)


#
def astAssemblyBasicObjectNameSet(*args):
    return astUnitAssemblyBasicNameSet(*args)


#
def astRigNamespaceSet(*args):
    return astBasicNameSet(*args) + appVariant.astRigNodeLabel


#
def astSolverNamespaceSet(*args):
    return astBasicNameSet(*args) + appVariant.astSolverNodeLabel


# Group Name Config
def astNodeGroupNameSet(assetName, groupNameLabel, objectNameLabel):
    return astBasicGroupNameSet(assetName, groupNameLabel, objectNameLabel)


#
def astAssemblyProxyObjectName(assetName, namespace=none):
    return [none, namespace + ':'][namespace is not none] + astAssemblyBasicObjectNameSet(assetName) + appVariant.asbProxyFileLabel


# Compose Group Name
def astComposeRootGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicComposeRootGroupLabel)
    return string


# Unit Group Name
def astUnitRootGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicUnitRootGroupLabel)
    return string


#
def astUnitLinkGroupLabel(assetStage):
    string = ''
    if isAstModelLink(assetStage):
        string = appVariant.basicModelLinkGroupLabel
    elif isAstRigLink(assetStage):
        string = appVariant.basicRigLinkGroupLabel
    elif isAstCfxLink(assetStage):
        string = appVariant.basicCfxLinkGroupLabel
    elif isAstSolverLink(assetStage):
        string = appVariant.basicSolverLinkGroupLabel
    elif isAstLightLink(assetStage):
        string = appVariant.basicLightLinkGroupLabel
    return string


#
def astUnitLinkGroupName(assetName, assetStage, namespace=None):
    return ('' if namespace is None else namespace + ':') + astBasicGroupNameSet(assetName, astUnitLinkGroupLabel(assetStage))


# Model Root Group Name
def astModelRootGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicModelRootGroupLabel)
    return string


#
def astRigRootGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicRigRootGroupLabel)
    return string


#
def astCfxRootGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicCfxRootGroupLabel)
    return string


# Model Group Name
def astUnitModelLinkGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicModelLinkGroupLabel)
    return string


#
def astUnitRigLinkGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicRigLinkGroupLabel)
    return string


#
def astUnitCfxLinkGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicCfxLinkGroupLabel)
    return string


#
def astUnitSolverLinkGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicRigSolLinkGroupLabel)
    return string


#
def astUnitLightLinkGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicLightLinkGroupLabel)
    return string


# Product Nde_Geometry Group Name
def astUnitModelProductGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicGeometryGroupLabel)
    return string


# Solver Group Name
def astUnitModelSolverGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicSolverGeometrySubGroupLabel)
    return string


#
def astUnitModelReferenceGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicModelReferenceGroupLabel)
    return string


#
def astUnitModelBridgeGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicModelBridgeGroupLabel)
    return string


#
def astUnitRigBridgeGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicRigBridgeGroupLabel)
    return string


#
def astUnitSolverBridgeGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicSolverBridgeGroupLabel)
    return string


# Rig Solver Link Group
def astUnitRigSolFurSubGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.astFurSolverGroupLabel)
    return string


# Solver Group Name
def astUnitCfxFurCollisionFieldGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.astRigSolFurCollisionFieldGroupLabel)
    return string


#
def astUnitModelSolClothFieldGroupName(assetName):
    string = astBasicGroupNameSet(assetName, appVariant.basicSolverClothFieldGroupLabel)
    return string


#
def astUnitModelSolHairFieldGroupName(assetName):
    string = astBasicGroupNameSet(assetName, appVariant.basicSolverHairFieldGroupLabel)
    return string


# Solver Group Name
def scAstCfxTempGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicCfxLinkGroupLabel + '_temp')
    return string


# Solver Group Name
def scAstSolverTempGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicSolverGeometrySubGroupLabel + '_temp')
    return string


#
def yetiGroupName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, appVariant.basicCfxLinkGroupLabel)
    return string


#
def cfxSetName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicSetNameSet(assetName, appVariant.basicCfxLinkGroupLabel)
    return string


#
def solverCollisionFieldGroupName(assetName):
    string = astBasicGroupNameSet(assetName, appVariant.basicCollisionFieldGroupLabel)
    return string


#
def yetiNodeGroupName(assetName, namespace=none):
    subLabel = appVariant.astYetiNodeGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def guideSystemGroupName(assetName, namespace=none):
    subLabel = appVariant.astYetiGuideSolverNodeGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def guideFollicleGroupName(assetName):
    subLabel = appVariant.astYetiGuideFollicleGroupLabel
    string = astBasicGroupNameSet(assetName, subLabel)
    return string


#
def guideLocalCurveGroupName(assetName):
    subLabel = appVariant.astPfxHairLocalCurveNodeLabel
    string = astBasicGroupNameSet(assetName, subLabel)
    return string


#
def guideCurveGroupName(assetName):
    subLabel = appVariant.astYetiGuideCurveGroupLabel
    string = astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astPfxHairNodeGroupName(assetName, namespace=none):
    subLabel = appVariant.astPfxHairGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitCfxNhrFieldGroupName(assetName, namespace=none):
    subLabel = appVariant.astCfxFurNhrFieldGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astCfxNurbsHairNodeGroupName(assetName, namespace=none):
    subLabel = appVariant.astCfxFurNhrObjectGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astCfxNhrGrowObjectGroupName(assetName, namespace=none):
    subLabel = appVariant.astCfxFurNhrGrowGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitCfxNhrGuideObjectGroupName(assetName, namespace=none):
    subLabel = appVariant.astCfxFurNhrGuideGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitRigSolFurFieldGroupName(assetName, namespace=none):
    subLabel = appVariant.astRigSolFurFieldGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitRigSolNhrFieldGroupName(assetName, namespace=none):
    subLabel = appVariant.astRigSolNhrFieldGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitRigSolNhrSubGroupName(assetName, namespace=none):
    subLabel = appVariant.astRigSolNhrSubGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitSolverGrowFieldSubGroupName(assetName, namespace=none):
    subLabel = appVariant.astSolverGrowFieldSubGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitRigSolNhrGuideObjectGroupName(assetName, namespace=none):
    subLabel = appVariant.astRigSolNhrSolGuideGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitRigSolNhrCurveObjectGroupName(assetName, namespace=none):
    subLabel = appVariant.astRigSolNhrSolCurveGroupLabel
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
    subLabel = appVariant.astSolverGrowSourceGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitSolverGrowSourceObjectGroupPath(assetName, namespace=none):
    return '|'.join(
        [
            astUnitSolverLinkGroupName(assetName, namespace),
            astUnitSolverGrowFieldSubGroupName(assetName, namespace),
            astUnitSolverGrowSourceObjectGroupName(assetName, namespace)
        ]
    )


#
def astUnitSolverGrowDeformObjectGroupName(assetName, namespace=none):
    subLabel = appVariant.astSolverGrowDeformGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitSolverGrowDeformObjectGroupPath(assetName, namespace=none):
    return '|'.join(
        [
            astUnitSolverLinkGroupName(assetName, namespace),
            astUnitSolverGrowFieldSubGroupName(assetName, namespace),
            astUnitSolverGrowDeformObjectGroupName(assetName, namespace)
        ]
    )


#
def pfxSystemGroupName(assetName, namespace=none):
    subLabel = appVariant.astPfxHairSolverNodeGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitCfxGrowFieldSubGroupName(assetName, namespace=none):
    subLabel = appVariant.astCfxGrowFieldSubGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitCfxGrowSourceObjectGroupName(assetName, namespace=none):
    subLabel = appVariant.astCfxGrowSourceGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitCfxGroupSourceGroupPath(assetName, namespace=none):
    return '|'.join(
        [
            astUnitCfxLinkGroupName(assetName, namespace),
            astUnitCfxGrowFieldSubGroupName(assetName, namespace),
            astUnitCfxGrowSourceObjectGroupName(assetName, namespace)
        ]
    )


#
def astUnitCfxGrowDeformObjectGroupName(assetName, namespace=none):
    subLabel = appVariant.astCfxGrowDeformGroupLabel
    string = [none, namespace + ':'][namespace is not none] + astBasicGroupNameSet(assetName, subLabel)
    return string


#
def astUnitCfxGrowDeformObjectGroupPath(assetName, namespace=none):
    return '|'.join(
        [
            astUnitCfxLinkGroupName(assetName, namespace),
            astUnitCfxGrowFieldSubGroupName(assetName, namespace),
            astUnitCfxGrowDeformObjectGroupName(assetName, namespace)
        ]
    )


# Asset Namespace
def furAssetGroupName(assetName, number, variant):
    string = '%s_%s_%s_%s%s%s' % (appVariant.Lynxi_Prefix_Product_Asset, assetName, number, variant, appVariant.astCfxProductFileLabel, appVariant.basicGroupLabel)
    return string


#
def astModelContainerName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicNameSet(assetName, appVariant.scModelNodeLabel, appVariant.astContainerNodeLabel)
    return string


#
def astCfxContainerName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicNameSet(assetName, appVariant.basicCharacterFxLinkLabel, appVariant.astContainerNodeLabel)
    return string


#
def astSolverContainerName(assetName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + astBasicNameSet(assetName, appVariant.basicSolverLinkLabel, appVariant.astContainerNodeLabel)
    return string


#
def astRootGroupHierarchyConfig(assetName):
    dic = lxBasic.orderedDict()
    dic[astUnitRootGroupName(assetName)] = []
    return dic


# Pro Group Config
def astModelLinkHierarchyConfig(assetName):
    dic = lxBasic.orderedDict()
    #
    dic[astUnitModelLinkGroupName(assetName)] = [
        astUnitModelProductGroupName(assetName),
        astUnitModelSolverGroupName(assetName),
        astUnitModelReferenceGroupName(assetName),
        astUnitModelBridgeGroupName(assetName)
    ]
    return dic


#
def astModelCharHierarchyConfig(assetName):
    dic = lxBasic.orderedDict()
    dic[astUnitModelLinkGroupName(assetName)] = [
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
    gpuName = '%s_%s%s' % (assetName, number, appVariant.asbGpuFileLabel)
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
    dic = lxBasic.orderedDict()
    dic[astUnitModelLinkGroupName(assetName)] = [
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
    dic = lxBasic.orderedDict()
    dic[astUnitModelLinkGroupName(assetName)] = [
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
    dic = lxBasic.orderedDict()
    dic[astUnitModelLinkGroupName(assetName)] = [
        astUnitModelReferenceGroupName(assetName)
    ]
    return dic


#
def astRigLinkHierarchyConfig(assetName):
    dic = lxBasic.orderedDict()
    # Main
    dic[astUnitRigLinkGroupName(assetName)] = [
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
    astFurYetiGroupLabel = appVariant.astFurYetiGroupLabel
    astFurMayaGroupLabel = appVariant.astFurMayaGroupLabel
    astFurNurbsGroupLabel = appVariant.astFurNurbsGroupLabel
    #
    astYetiNodeGroupLabel = appVariant.astYetiNodeGroupLabel
    astYetiGroomGroupLabel = appVariant.astYetiGroomGroupLabel
    astYetiGrowGroupLabel = appVariant.astYetiGrowGroupLabel
    astYetiReferenceGroupLabel = appVariant.astYetiReferenceGroupLabel
    astYetiGuideGroupLabel = appVariant.astYetiGuideGroupLabel
    astYetiGuideFollicleGroupLabel = appVariant.astYetiGuideFollicleGroupLabel
    astYetiGuideCurveGroupLabel = appVariant.astYetiGuideCurveGroupLabel
    astYetiGuideSolverNodeGroupLabel = appVariant.astYetiGuideSolverNodeGroupLabel
    #
    astPfxHairGroupLabel = appVariant.astPfxHairGroupLabel
    astPfxHairGrowGroupLabel = appVariant.astPfxHairGrowGroupLabel
    astPfxHairFollicleGroupLabel = appVariant.astPfxHairFollicleGroupLabel
    astPfxHairCurveGroupLabel = appVariant.astPfxHairCurveGroupLabel
    astPfxHairSolverNodeGroupLabel = appVariant.astPfxHairSolverNodeGroupLabel
    #
    astCfxFurNhrFieldGroupLabel = appVariant.astCfxFurNhrFieldGroupLabel
    #
    astCfxGrowFieldSubGroupLabel = appVariant.astCfxGrowFieldSubGroupLabel
    astCfxGrowSourceGroupLabel = appVariant.astCfxGrowSourceGroupLabel
    astCfxFurGrowTargetGroupLabel = appVariant.astCfxFurGrowTargetGroupLabel
    astCfxGrowDeformGroupLabel = appVariant.astCfxGrowDeformGroupLabel
    astCfxFurCollisionSubGroupLabel = appVariant.astCfxFurCollisionSubGroupLabel
    #
    dic = lxBasic.orderedDict()
    # Main
    dic[astUnitCfxLinkGroupName(assetName)] = [
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
    dic = lxBasic.orderedDict()
    dic[astUnitSolverLinkGroupName(assetName)] = [
        astBasicGroupNameSet(assetName, '_rigSolControl'),
        astBasicGroupNameSet(assetName, '_rigSolSkin'),
        astBasicGroupNameSet(assetName, '_rigSolField'),
        #
        astUnitRigSolNhrSubGroupName(assetName),
        #
        astBasicGroupNameSet(assetName, appVariant.astSolverGrowFieldSubGroupLabel),
        astBasicGroupNameSet(assetName, appVariant.astRigSolCollisionSubGroupLabel)
    ]
    dic[astUnitRigSolNhrSubGroupName(assetName)] = [
        astUnitRigSolNhrFieldGroupName(assetName)
    ]
    dic[astUnitRigSolNhrFieldGroupName(assetName)] = [
        astUnitRigSolNhrGuideObjectGroupName(assetName),
        astUnitRigSolNhrCurveObjectGroupName(assetName)
    ]
    dic[astBasicGroupNameSet(assetName, appVariant.astSolverGrowFieldSubGroupLabel)] = [
        astBasicGroupNameSet(assetName, appVariant.astSolverGrowSourceGroupLabel),
        astBasicGroupNameSet(assetName, appVariant.astRigSolGrowTargetGroupLabel),
        astBasicGroupNameSet(assetName, appVariant.astSolverGrowDeformGroupLabel)
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
    dic = lxBasic.orderedDict()
    dic[astUnitLightLinkGroupName(assetName)] = [
        astBasicGroupNameSet(assetName, appVariant.lgtFieldLabel)
    ]
    dic[astBasicGroupNameSet(assetName, appVariant.lgtFieldLabel)] = [
        astBasicGroupNameSet(assetName, '_' + i) for i in astLightBasicLeafs()
        ]
    return dic


# Asset AR Name
def astUnitAssemblyReferenceName(assetName):
    return astUnitAssemblyBasicNameSet(assetName)


#
def assetSchemeFileConfig():
    string = '{0}/{1}/{2}/{3}'.format(appVariant.dbAssetRoot, appVariant.dbBasicFolderName, lxConfigure.LynxiSchemeExt, appVariant.dbAssetBasicKey)
    return lxBasic.getOsUniqueFile(string)


#
def assetSetFileConfig(assetIndex):
    string = '{0}/{1}/{2}/{3}'.format(
        appVariant.dbAssetRoot, appVariant.dbBasicFolderName, lxConfigure.LynxiSetExt, assetIndex
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
        [('variant', u'变体 ( Variant(s) )'), (appVariant.astDefaultVariant, )],
        [('classify', u'类型 ( Classify )'), assetCfg.astBasicClassDatumDic()],
        [('priority', u'优先级 ( Priority )'), assetCfg.basicAssetPriorityLis()],
        #
        [(lxConfigure.LynxiProduct_Asset_Link_Model, u'模型制作 Model'), False],
        [(lxConfigure.LynxiProduct_Asset_Link_Rig, u'绑定制作 ( Rig )'), False],
        [(lxConfigure.LynxiProduct_Asset_Link_Cfx, u'角色特效制作 ( Character FX )'), False],
        [(lxConfigure.LynxiProduct_Asset_Link_Solver, u'角色模拟制作 ( Solver )'), False],
        [(lxConfigure.LynxiProduct_Asset_Link_Light, u'资产灯光 ( Light )'), False],
        #
        [(lxConfigure.LynxiProduct_Asset_Link_Assembly, u'资产组装 ( Assembly )'), False]
    ]
    return lis


# Scheme Data
def getUiAssetSchemeDataDic():
    def getCustomData():
        osFile = assetSchemeFileConfig()
        
        return bscMethods.OsJson.read(osFile)
    #
    def getDic(data):
        dic = lxBasic.orderedDict()
        if data:
            for i in data:
                scheme, enable, description = i
                dic[scheme] = enable, description
        return dic
    #
    return getDic(getCustomData())


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
                    setUiKey = lxBasic.str_camelcase2prettify(setKey)
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
        dic = lxBasic.orderedDict()
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
            assetCfg.astBasicViewClassDic(assetClass)[1],
            assetViewName
        )
    else:
        string = u'{} {} ( {} )'.format(
            assetCfg.astBasicViewClassDic(assetClass)[1],
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
        for i in assetCfg.basicAssetLinks():
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
        dic = lxBasic.orderedDict()
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
        dic = lxBasic.orderedDict()
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
                modelEnabled = lxBasic.getKeyEnabled(data, lxConfigure.LynxiProduct_Asset_Link_Model)
                rigEnabled = lxBasic.getKeyEnabled(data, lxConfigure.LynxiProduct_Asset_Link_Rig)
                cfxEnabled = lxBasic.getKeyEnabled(data, lxConfigure.LynxiProduct_Asset_Link_Cfx)
                scSolverEnable = lxBasic.getKeyEnabled(data, lxConfigure.LynxiProduct_Asset_Link_Solver)
                scLightEnable = lxBasic.getKeyEnabled(data, lxConfigure.LynxiProduct_Asset_Link_Light)
                assemblyEnabled = lxBasic.getKeyEnabled(data, lxConfigure.LynxiProduct_Asset_Link_Assembly)
                for assetVariant in assetVariants:
                    dic[(assetIndex, assetVariant)] = description, assetClass, assetName, assetPriority, modelEnabled, rigEnabled, cfxEnabled, scSolverEnable, scLightEnable, assemblyEnabled
    #
    def getMain(data):
        dic = lxBasic.orderedDict()
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
                        if lxBasic.isOsExistsFile(serverAstUnitAsbDefinitionFile):
                            dic[assetIndex] = description, assetClass, assetName, assetVariant
    #
    def getMain(data):
        dic = lxBasic.orderedDict()
        if data:
            for i in data:
                assetIndex, enable, description = i
                if enable is True:
                    getBranch(dic, assetIndex, description)
        return dic
    return getMain(getCustomData())


#
def isCharacterClass(assetClass):
    boolean = False
    if assetClass == assetCfg.LynxiProduct_Asset_Class_Character:
        boolean = True
    return boolean


#
def isPropClass(assetClass):
    boolean = False
    if assetClass == assetCfg.LynxiProduct_Asset_Class_Prop:
        boolean = True
    return boolean


#
def isAstModelLink(assetStage):
    boolean = False
    if assetStage in lxConfigure.LynxiAstModelStages or assetStage == lxConfigure.LynxiProduct_Asset_Link_Model:
        boolean = True
    return boolean


#
def isAstRigLink(assetStage):
    boolean = False
    if assetStage in lxConfigure.LynxiAstRigStages or assetStage == lxConfigure.LynxiProduct_Asset_Link_Rig:
        boolean = True
    return boolean


#
def isAstCfxLink(assetStage):
    boolean = False
    if assetStage in lxConfigure.LynxiAstCfxStages or assetStage == lxConfigure.LynxiProduct_Asset_Link_Cfx:
        boolean = True
    return boolean


#
def isAstSolverLink(assetStage):
    boolean = False
    if assetStage in lxConfigure.LynxiAstRigSolStages or assetStage == lxConfigure.LynxiProduct_Asset_Link_Solver:
        boolean = True
    return boolean


#
def isAstLightLink(assetStage):
    boolean = False
    if assetStage in lxConfigure.LynxiScLightStages or assetStage == lxConfigure.LynxiProduct_Asset_Link_Light:
        boolean = True
    return boolean


#
def isAstAssemblyLink(assetStage):
    boolean = False
    if assetStage in lxConfigure.LynxiAstAssemblyStages:
        boolean = True
    return boolean


#
def isAssetLink(assetStage):
    if isAstModelLink(assetStage):
        boolean = True
    elif isAstRigLink(assetStage):
        boolean = True
    elif isAstCfxLink(assetStage):
        boolean = True
    elif isAstSolverLink(assetStage):
        boolean = True
    elif isAstLightLink(assetStage):
        boolean = True
    else:
        boolean = False
    return boolean


#
def getAssetLink(assetStage):
    link = lxConfigure.LynxiProduct_Asset_Link_Model
    if isAstModelLink(assetStage):
        link = lxConfigure.LynxiProduct_Asset_Link_Model
    elif isAstRigLink(assetStage):
        link = lxConfigure.LynxiProduct_Asset_Link_Rig
    elif isAstCfxLink(assetStage):
        link = lxConfigure.LynxiProduct_Asset_Link_Cfx
    elif isAstSolverLink(assetStage):
        link = lxConfigure.LynxiProduct_Asset_Link_Solver
    elif isAstLightLink(assetStage):
        link = lxConfigure.LynxiProduct_Asset_Link_Light
    return link


#
def astBasicLinkFolder(assetStage):
    string = none
    if isAstModelLink(assetStage):
        if appVariant.astModelFolderEnabled is True:
            string = appVariant.astModelLinkFolder
    elif isAstRigLink(assetStage):
        if appVariant.astRigFolderEnabled is True:
            string = appVariant.astRigLinkFolder
    elif isAstCfxLink(assetStage):
        if appVariant.astCfxFolderEnabled is True:
            string = appVariant.astCfxLinkFolder
    elif isAstSolverLink(assetStage):
        if appVariant.astSolverFolderEnabled is True:
            string = appVariant.astRigSolFolder
    elif isAstLightLink(assetStage):
        if appVariant.astLightFolderEnabled is True:
            string = appVariant.astLightLinkFolder
    elif isAstAssemblyLink(assetStage):
        if appVariant.astAssemblyFolderEnabled is True:
            string = appVariant.astAssemblyLinkFolder
    return string


#
def astBasicLinkLabel(assetStage):
    string = appVariant.basicModelLinkLabel
    if isAstModelLink(assetStage):
        string = appVariant.basicModelLinkLabel
    elif isAstRigLink(assetStage):
        string = appVariant.basicRigLinkLabel
    elif isAstCfxLink(assetStage):
        string = appVariant.basicCharacterFxLinkLabel
    elif isAstSolverLink(assetStage):
        string = appVariant.basicSolverLinkLabel
    elif isAstLightLink(assetStage):
        string = appVariant.basicLightLinkLabel
    elif isAstAssemblyLink(assetStage):
        string = appVariant.basicAssemblyLinkLabel
    return string


#
def astBasicTextureFolder(assetStage):
    string = none
    if isAstModelLink(assetStage):
        string = appVariant.astModelTextureFolder
    elif isAstRigLink(assetStage):
        string = appVariant.astRigTextureFolder
    elif isAstCfxLink(assetStage):
        string = appVariant.astCfxTextureFolder
    elif isAstSolverLink(assetStage):
        string = appVariant.astSolverTextureFolder
    elif isAstLightLink(assetStage):
        string = appVariant.astLightTextureFolder
    elif isAstAssemblyLink(assetStage):
        string = appVariant.astAssemblyTextureFolder
    return string


#
def astBasicMapFolder(assetStage):
    mainLabel = astBasicLinkLabel(assetStage)
    if mainLabel.startswith('_'):
        mainLabel = mainLabel[1:]
    #
    subLabel = appVariant.basicMapSubLabel
    return bscMethods.LabelText.toLabel(mainLabel, subLabel)


#
def astBasicCacheFolder(assetStage):
    mainLabel = astBasicLinkLabel(assetStage)
    if mainLabel.startswith('_'):
        mainLabel = mainLabel[1:]
    #
    subLabel = appVariant.basicCacheSubLabel
    return bscMethods.LabelText.toLabel(mainLabel, subLabel)


#
def astBasicSourceFileLabel(assetStage):
    subLabel = appVariant.basicSourceSubLabel
    return bscMethods.LabelText.toLabel(astBasicLinkLabel(assetStage), subLabel)


#
def astBasicProductFileLabel(assetStage):
    if isAstRigLink(assetStage):
        return appVariant.astAnimationRigFileLabel
    else:
        subLabel = appVariant.basicProductSubLabel
        return bscMethods.LabelText.toLabel(astBasicLinkLabel(assetStage), subLabel)


#
def astBasicAsbDefinitionFileLabel(assetStage):
    subLabel = appVariant.basicAssemblyDefinitionSubLabel
    return bscMethods.LabelText.toLabel(astBasicLinkLabel(assetStage), subLabel)


#
def astAssetFurFileLabel(assetStage):
    subLabel = appVariant.basicFurSubLabel
    return bscMethods.LabelText.toLabel(astBasicLinkLabel(assetStage), subLabel)


#
def assetPreviewFileLabel(assetStage):
    subLabel = appVariant.basicPreviewSubLabel
    return bscMethods.LabelText.toLabel(astBasicLinkLabel(assetStage), subLabel)


#
def astBasicOsFileNameConfig(assetName, fileLabel, extLabel):
    string = '{}{}{}'.format(assetName, fileLabel, extLabel)
    return string


# Asset Path
def astUnitBasicDirectory(rootIndexKey, projectName):
    root = [appVariant.serverAssetRoot, appVariant.localAssetRoot, appVariant.backupAssetRoot]
    directory = '%s/%s/%s/%s' % (root[rootIndexKey], projectName, appVariant.basicAssetFolder, appVariant.basicUnitFolder)
    return directory


# Asset Path
def astUnitAssemblyBasicDirectory(rootIndexKey, projectName):
    root = [appVariant.serverAssetRoot, appVariant.localAssetRoot, appVariant.backupAssetRoot]
    directory = '%s/%s/%s/%s' % (root[rootIndexKey], projectName, appVariant.basicAssemblyFolder, appVariant.basicUnitFolder)
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
    if isAstRigLink(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFolderName]
    osFolder = lxBasic.getOsFileByKeyVars(keyVars)
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
    if isAstRigLink(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFolderName]
    osFolder = lxBasic.getOsFileByKeyVars(keyVars)
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
    osFolder = lxBasic.getOsFileByKeyVars(keyVars)
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
    osFolder = lxBasic.getOsFileByKeyVars(keyVars)
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
    if isAstRigLink(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFolderName]
    osFolder = lxBasic.getOsFileByKeyVars(keyVars)
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
    osFolder = lxBasic.getOsFileByKeyVars(keyVars)
    return osFolder


#
def astUnitTextureIndexFile(
        rootIndexKey,
        projectName,
        assetClass, assetName, assetVariant, assetStage):
    if isAstAssemblyLink(assetStage):
        basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    else:
        basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    #
    fileLabel = astBasicProductFileLabel(assetStage)
    extLabel = appVariant.dbTextureUnitKey
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if isAstRigLink(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    osFile = lxBasic.getOsFileByKeyVars(keyVars)
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
    extLabel = appVariant.logExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if isAstRigLink(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    osFile = lxBasic.getOsFileByKeyVars(keyVars)
    return osFileName, osFile


#
def astUnitSourceFile(
        rootIndexKey,
        projectName,
        assetClass, assetName, assetVariant, assetStage):
    if isAstAssemblyLink(assetStage):
        basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    else:
        basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    #
    fileLabel = astBasicSourceFileLabel(assetStage)
    extLabel = appVariant.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if isAstRigLink(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    osFile = lxBasic.getOsFileByKeyVars(keyVars)
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
    extLabel = appVariant.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if isAstRigLink(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    osFile = lxBasic.getOsFileByKeyVars(keyVars)
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
    extLabel = appVariant.astAssemblyIndexExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    keyVars = [basicDirectory, assetName, osFileName]
    osFile = lxBasic.getOsFileByKeyVars(keyVars)
    return osFileName, osFile


#
def astUnitAssemblyProductFile(projectName, assetName, assetVariant):
    basicDirectory = astUnitAssemblyBasicDirectory(lxConfigure.LynxiRootIndex_Server, projectName)
    #
    fileLabel = bscMethods.LabelText.toLabel(appVariant.basicAssemblyLinkLabel, appVariant.basicProductSubLabel)
    extLabel = appVariant.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    keyVars = [basicDirectory, assetName, assetVariant, osFileName]
    osFile = lxBasic.getOsFileByKeyVars(keyVars)
    return osFileName, osFile


#
def astUnitAssemblyDefinitionFile(rootIndexKey, projectName, assetClass, assetName, assetVariant, assetStage):
    basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    #
    fileLabel = astBasicAsbDefinitionFileLabel(assetStage)
    extLabel = appVariant.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if isAstRigLink(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, osFileName]
    osFile = lxBasic.getOsFileByKeyVars(keyVars)
    return osFileName, osFile


#
def astUnitAssemblyProxyCacheFile(projectName, assetName, assetVariant, lod=0):
    basicDirectory = astUnitAssemblyBasicDirectory(lxConfigure.LynxiRootIndex_Server, projectName)
    #
    if lod == 0:
        fileLabel = appVariant.asbProxyFileLabel
    else:
        fileLabel = appVariant.asbProxyFileLabel + '_lod%s' % str(lod).zfill(2)
    #
    extLabel = projectPr.getProjectProxyExt(projectName)
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    keyVars = [basicDirectory, assetName, assetVariant, osFileName]
    osFile = lxBasic.getOsFileByKeyVars(keyVars)
    return osFileName, osFile


#
def astUnitAssemblyProxyFile(projectName, assetName, assetVariant, lod=0):
    basicDirectory = astUnitAssemblyBasicDirectory(lxConfigure.LynxiRootIndex_Server, projectName)
    #
    if lod == 0:
        fileLabel = appVariant.asbProxyFileLabel
    else:
        fileLabel = appVariant.asbProxyFileLabel + '_lod%s' % str(lod).zfill(2)
    #
    extLabel = appVariant.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    keyVars = [basicDirectory, assetName, assetVariant, osFileName]
    osFile = lxBasic.getOsFileByKeyVars(keyVars)
    return osFileName, osFile


#
def astUnitAssemblyGpuCacheFile(projectName, assetName, lod=0):
    basicDirectory = astUnitAssemblyBasicDirectory(lxConfigure.LynxiRootIndex_Server, projectName)
    if lod == 0:
        fileLabel = appVariant.asbGpuFileLabel
    else:
        fileLabel = appVariant.asbGpuFileLabel + '_lod%s' % str(lod).zfill(2)
    #
    extLabel = appVariant.gpuCacheExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    keyVars = [basicDirectory, assetName, osFileName]
    osFile = lxBasic.getOsFileByKeyVars(keyVars)
    return osFileName, osFile


#
def astUnitAssemblyBoxCacheFile(projectName, assetName):
    basicDirectory = astUnitAssemblyBasicDirectory(lxConfigure.LynxiRootIndex_Server, projectName)
    fileLabel = appVariant.asbBoxFileLabel
    #
    extLabel = appVariant.gpuCacheExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    keyVars = [basicDirectory, assetName, osFileName]
    osFile = lxBasic.getOsFileByKeyVars(keyVars)
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
    extLabel = appVariant.mayaAsciiExt
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if isAstRigLink(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    osFile = lxBasic.getOsFileByKeyVars(keyVars)
    return osFileName, osFile


#
def astUnitExtraFile(
        rootIndexKey,
        projectName,
        assetClass, assetName, assetVariant, assetStage
):
    if isAstAssemblyLink(assetStage):
        basicDirectory = astUnitAssemblyBasicDirectory(rootIndexKey, projectName)
    else:
        basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = astBasicLinkFolder(assetStage)
    fileLabel = astBasicProductFileLabel(assetStage)
    extLabel = appVariant.dbExtraUnitKey
    #
    osFileName = astBasicOsFileNameConfig(assetName, fileLabel, extLabel)
    #
    if isAstRigLink(assetStage):
        assetVariant = none
    #
    keyVars = [basicDirectory, assetName, assetVariant, linkFolder, osFileName]
    osFile = lxBasic.getOsFileByKeyVars(keyVars)
    return osFileName, osFile


def astUnitBasicPreviewFile(
        rootIndexKey,
        projectName,
        assetClass, assetName
):
    basicDirectory = astUnitBasicDirectory(rootIndexKey, projectName)
    #
    fileLabel = ''
    extLabel = appVariant.dbPreviewUnitKey
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
        extLabel=appVariant.jpgExt
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
    extLabel = appVariant.dbMeshUnitKey
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
    extLabel = appVariant.dbMeshUnitKey
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
    extLabel = appVariant.dbTextureUnitKey
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
    string = appVariant.infoNonExistsLabel
    #
    serverProductFile = astUnitProductFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    #
    if lxBasic.isOsExistsFile(serverProductFile):
        data = bscMethods.OsTime.getCnPrettifyByTimestamp(lxBasic.getOsFileMtimestamp(serverProductFile))
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
    return lxBasic.getOsFileMtimeTag(serverProductFile)


#
def getAssetUnitExtraData(projectName, assetClass, assetName, assetVariant, assetStage):
    dic = lxBasic.orderedDict()
    extraFile = astUnitExtraFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, assetStage
    )[1]
    if lxBasic.isOsExistsFile(extraFile):
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
                pathCmd = lxBasic._toVariantConvert('var', mayaPackageStr)
                exec pathCmd
                #
                if var:
                    if lxBasic.isOsExist(var):
                        osFile = var + '/' + lxConfigure.LynxiAssetUploadCommandKey + '.py'
                        if lxBasic.isOsExist(osFile):
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
                pathCmd = lxBasic._toVariantConvert('var', mayaPackageStr)
                exec pathCmd
                #
                if var:
                    if lxBasic.isOsExist(var):
                        osFile = var + '/' + lxConfigure.LynxiAssetLoadCommandKey + '.py'
                        if lxBasic.isOsExist(osFile):
                            command = bscMethods.OsFile.read(osFile)
                            pythonCommand = 'python(' + bscMethods.OsJson.dump(command) + ');'
                            #
                            return pythonCommand
