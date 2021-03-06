# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds

from LxBasic import bscObjects
#
from LxPreset import prsConfigure, prsOutputs
#
from LxCore.preset.prod import assetPr, sceneryPr
#
from LxMaya.command import maUtils, maAsb
#
from LxMaya.product.data import datScenery
# Utilities Label
adFileAttrLabel = prsOutputs.Util.adFileAttrLabel
asbLodLevelAttrLabel = prsOutputs.Util.asbLodLevelAttrLabel


#
def setAssembliesActiveSwitch(keyword='GPU'):
    datumDic = datScenery.getAssemblyFilterDic()
    if datumDic:
        for k, v in datumDic.items():
            # Switch
            if k != keyword:
                # View Progress
                explain = '''Switch Assembly(s) "{}" to "{}"'''.format(k, keyword)
                maxValue = len(v)
                progressBar = bscObjects.ProgressWindow(explain, maxValue)
                for i in v:
                    progressBar.update()
                    assemblyReferenceString = i
                    lodLevel = maAsb.getAssemblyLodLevel(assemblyReferenceString)
                    levelLabel = ['', lodLevel][lodLevel != 'LOD00']
                    targetItem = [keyword, keyword + '-' + lodLevel][levelLabel != '']
                    maAsb.setAssemblyActive(assemblyReferenceString, targetItem)


#
def setAssemblyVariantSwitch(assemblyReferenceString, projectName, assetCategory, assetName, assetVariant):
    adFile = assetPr.astUnitAssemblyDefinitionFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName,
        assetCategory, assetName, assetVariant, prsMethods.Asset.assemblyLinkName()
    )[1]
    #
    maUtils.setAttrStringDatum(assemblyReferenceString, 'definition', adFile)


#
def setAssemblyAnnotationSwitch(assemblyReferenceString, assemblyAnnotation):
    annotationName = assemblyReferenceString + '_annotationShape'
    annotationObject = assemblyReferenceString + '|' + annotationName
    #
    if cmds.objExists(annotationObject):
        cmds.setAttr(annotationObject + '.text', assemblyAnnotation, type='string')


#
def setScnUnitLocatorCreate(sceneryName, sceneryVariant, composeFile):
    sceneryLocatorName = sceneryPr.scnUnitLocatorName(sceneryName, sceneryVariant) + '_0'
    locator = maUtils.setLocatorCreate(sceneryLocatorName)[0]
    cmds.addAttr(locator, longName='composeFile', dataType='string', usedAsFilename=1)
    cmds.setAttr(locator + '.' + 'composeFile', composeFile, type='string')
    return locator


#
def setAssemblyShapeClear():
    lis = datScenery.getAssetAssemblyReferenceLis()
    subLis = datScenery.getActAssemblyReferenceLis()
    lis.extend(subLis)
    if lis:
        for nodepathString in lis:
            shapeLis = cmds.listRelatives(nodepathString, children=1, shapes=1, noIntermediate=0, fullPath=1)
            if shapeLis:
                for shape in shapeLis:
                    try:
                        cmds.delete(shape)
                    except:
                        pass


#
def setAssemblyChildClear():
    lis = datScenery.getAssetAssemblyReferenceLis()
    subLis = datScenery.getActAssemblyReferenceLis()
    lis.extend(subLis)
    if lis:
        for nodepathString in lis:
            childLis = cmds.listRelatives(nodepathString, children=1, fullPath=1)
            if childLis:
                for node in childLis:
                    try:
                        cmds.delete(node)
                    except:
                        pass
