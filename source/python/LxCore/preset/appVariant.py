# coding:utf-8
from LxCore import lxConfigure
#
from LxCore.preset import basicPr, pipePr, appPr
#
from LxCore.preset.prod import projectPr
# do not delete
serverBasicPath = lxConfigure.Root().root()


#
def setBuildLocalPresetVariants(data):
    moduleName, variables = data
    for i in variables:
        command = '''global {0}\r\n{0} = {1}.{0}'''.format(i, moduleName)
        #
        exec command


# Pipeline
pipelinePresetData = basicPr.setBuildBasicPresetVariants(pipePr.getPipelinePresetVariantDic(lxConfigure.LynxiDefaultPipelineValue))
setBuildLocalPresetVariants(pipelinePresetData)
# Project
projectPresetData = basicPr.setBuildBasicPresetVariants(projectPr.getProjectPresetVariantDic(projectPr.getAppProjectName()))
setBuildLocalPresetVariants(projectPresetData)
# App
projectPresetData = basicPr.setBuildBasicPresetVariants(appPr.getMayaAppPresetVariantDic())
setBuildLocalPresetVariants(projectPresetData)
# Type Config
assetClassifyAbbDic = projectPr.getAssetClassifyAbbLabelDic(astBasicClassifications)
assetClassifyFullDic = projectPr.getAssetClassifyDic(astBasicClassifications)
# Shape Config
objectShapePreset = pipePr.objectShapePreset()
#
shapeSet = objectShapePreset[0]
shapeLabel = objectShapePreset[2]
shapeDic = objectShapePreset[3]
#
none = ''


#
def temporaryDirectory(keyPath, projectName, artist, timeTag):
    directory = '%s/%s/%s/%s/%s' % (keyPath, projectName, utilsTemporaryFolder, artist, timeTag[:9])
    return directory


# Upload Temp Path
def localTemporaryDirectory():
    directory = '%s/%s' % (localTemporaryRoot, utilsTemporaryFolder)
    return directory


# Asset Name Config
def astBasicOsFileNameConfig(name, customLabel, ext):
    # <typeLabel>_<Name>_<Asset Type Label>.<Ext>
    return '%s%s%s' % (name, customLabel, ext)


# Animation Cache File Name Config
def cacheFileNameConfig(name, number, customLabel, timeTag, ext=alembicCacheExt):
    # <Type Label>_<Name>_<Asset Type Label>.<Ext>
    return '%s_%s%s_%s%s' % (name, number, customLabel, timeTag, ext)


#
def assemblyUnitShowName(name, variant):
    return '%s ( %s )' % (name, variant)


# Tree View Name
def assetTreeViewName(name, number, variant=none, subLabel=none):
    showName = '%s - %s' % (name, number)
    if variant:
        showName = '%s - %s ( %s )' % (name, number, variant)
    if variant and subLabel:
        showName = '%s - %s ( %s%s )' % (name, number, variant, subLabel)
    return showName
