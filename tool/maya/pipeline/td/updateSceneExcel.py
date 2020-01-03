# encoding: utf-8
"""
@author: dongchangbao
@contact: dongchangbao@papegames.net
@time: 2019/6/25 16:18
@file: updateSceneExcel.py
@desc: 
"""
import xlwt
#
from LxCore import lxCore_
#
from LxCore.preset.prod import assetPr, sceneryPr, scenePr
LabelLis = ['Name', 'ID', 'Class', 'Priority', 'Frame', 'Layout Enable', 'Animation Enable', 'Simulation Enable', 'Solver Enable', 'Light Enable', 'Asset Enable', 'Scenery']
#
workbook = xlwt.Workbook(encoding='utf-8')
#
worksheet = workbook.add_sheet('My Worksheet')
#
[worksheet.write(0, s, label=i) for s, i in enumerate(LabelLis)]
#
projectName = 'NuanNuan'
# projectName = 'nn4_mv1'


#
def setBranch(seq, k, v):
    def getAsset():
        assetDataDic = scenePr.getSceneAssetIndexDataDic(
            projectName,
            sceneClass, sceneName, sceneVariant
        )
        #
        string = 'N/a'
        if assetDataDic:
            subLis = []
            for ik, iv in assetDataDic.items():
                for j in iv:
                    (
                        scAstModelCacheTimestamp,
                        cacheSceneStage,
                        _, _,
                        scAstModelCacheFile,
                        assetIndex,
                        assetClass, assetName, number, assetVariant
                    ) = j
                    #
                    subLis.append(assetPr.getAssetViewInfo(assetIndex))
            string = '\n'.join(subLis)
        #
        return string
    #
    def getScenery():
        sceneryDataDic = scenePr.getScSceneryIndexDataDic(
            projectName,
            sceneClass, sceneName, sceneVariant
        )
        string = 'N/a'
        for ik, iv in sceneryDataDic.items():
            subLis = []
            for j in iv:
                (
                    timestamp,
                    sceneStage,
                    sceneryIndex,
                    sceneryClass, sceneryName, sceneryVariant, sceneryStage,
                    sceneryFile, sceneryExtraFile
                ) = j
                if sceneryClass in lxCore_.LynxiAssetClassLis:
                    subLis.append(assetPr.getAssetViewInfo(sceneryIndex))
                elif sceneryClass == lxCore_.LynxiSceneryClassKey:
                    subLis.append(sceneryPr.getSceneryViewInfo(sceneryIndex))
            #
            string = '\n'.join(subLis)
        #
        return string
    sceneIndex, sceneVariant = k
    (
        viewName,
        sceneClass, sceneName, scenePriority,
        scLayoutEnable, scAnimationEnable, scSolverEnable, scSimulationEnable, scLightEnable
    ) = v
    #
    startFrame, endFrame = scenePr.getScUnitFrameRange(
        projectName,
        sceneClass, sceneName, sceneVariant
    )
    # Frame Count
    frameCount = endFrame - startFrame + 1
    #
    showExplain = scenePr.getSceneViewInfo(sceneIndex, sceneClass, sceneVariant)
    worksheet.write(seq + 1, 0, label=showExplain)
    worksheet.write(seq + 1, 1, label=sceneName)
    worksheet.write(seq + 1, 2, label=sceneClass)
    worksheet.write(seq + 1, 3, label=scenePriority)
    worksheet.write(seq + 1, 4, label=frameCount)
    worksheet.write(seq + 1, 5, label=scLayoutEnable)
    worksheet.write(seq + 1, 6, label=scAnimationEnable)
    worksheet.write(seq + 1, 7, label=scSolverEnable)
    worksheet.write(seq + 1, 8, label=scSimulationEnable)
    worksheet.write(seq + 1, 9, label=scLightEnable)
    worksheet.write(seq + 1, 10, label=getAsset())
    worksheet.write(seq + 1, 11, label=getScenery())


#
def setMain():
    setData = scenePr.getUiSceneSetDataDic(projectName)
    #
    for seq, (k, v) in enumerate(setData.items()):
        setBranch(seq, k, v)
    #
    workbook.save('d:/{}_scene.xls'.format(projectName))

#
setMain()

