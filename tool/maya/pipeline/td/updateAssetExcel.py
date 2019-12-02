# encoding: utf-8
"""
@author: dongchangbao
@contact: dongchangbao@papegames.net
@time: 2019/6/25 16:15
@file: updateAssetExcel.py
@desc:
"""
import xlwt
#
from LxCore.preset.prod import projectPr, assetPr
LabelLis = ['Name', 'ID', 'Class', 'Priority', 'Model', 'Rig', 'Character - FX', 'Solver', 'Light', 'Assembly']
#
workbook = xlwt.Workbook(encoding = 'utf-8')
#
worksheet = workbook.add_sheet('My Worksheet')
#
[worksheet.write(0, seq, label=i) for seq, i in enumerate(LabelLis)]
#
projectName = projectPr.getMayaProjectName()
#
setData = assetPr.getUiAssetSetDataDic(projectName)
#
for seq, (k, v) in enumerate(setData.items()):
    assetIndex, assetVariant = k
    (
        viewName,
        assetClass, assetName, assetPriority,
        astModelEnable, astRigEnable, astCfxEnable, astSolverEnable, astLightEnable, astAssemblyEnable
    ) = v
    #
    showExplain = assetPr.getAssetViewInfo(assetIndex, assetClass, assetVariant)
    worksheet.write(seq + 1, 0, label=showExplain)
    worksheet.write(seq + 1, 1, label=assetName)
    worksheet.write(seq + 1, 2, label=assetClass)
    worksheet.write(seq + 1, 3, label=assetPriority)
    worksheet.write(seq + 1, 4, label=astModelEnable)
    worksheet.write(seq + 1, 5, label=astRigEnable)
    worksheet.write(seq + 1, 6, label=astCfxEnable)
    worksheet.write(seq + 1, 7, label=astSolverEnable)
    worksheet.write(seq + 1, 8, label=astLightEnable)
    worksheet.write(seq + 1, 9, label=astAssemblyEnable)
#
workbook.save('e:/{}_asset.xls'.format(projectName))