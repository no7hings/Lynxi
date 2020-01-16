# coding=utf-8
from LxBasic import bscCommands
#
from LxCore.preset.prod import projectPr
#
#
from LxUi.qt import qtWidgets, qtCore

#
# Project Data
currentProjectName = projectPr.getMayaProjectName()
#
none = ''


#
class IfAstModelRadarChartUnit(qtCore.QWidget_):
    widthSet = 400
    def __init__(self, *args, **kwargs):
        super(IfAstModelRadarChartUnit, self).__init__(*args, **kwargs)
        self.setupUnit()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def setStatisticsBoxShow(self, config, localData, serverData=None):
        lis = []
        #
        serverDic = {}
        if serverData:
            serverDic = serverData
        #
        if localData:
            for i in config:
                if i in localData:
                    explain = i
                    localValue = localData[i]
                    serverValue = 0
                    if i in serverDic:
                        serverValue = serverDic[i]
                    #
                    lis.append((explain, serverValue, localValue))
        #
        if not localData:
            self.setDef(config)
        #
        if lis:
            self._radarChart.setChartDatum(lis)
        self._radarChart.update()
    #
    def setWidth(self, width):
        self.widthSet = width
    #
    def setBackground(self, image):
        if bscCommands.isOsExistsFile(image):
            self._radarChart.setImage(image)
        else:
            self._radarChart.setImage(qtCore.iconRoot() + '/panel/defaultPreview.png')
    #
    def setDef(self, config):
        defValue = [6, 1, 8, 12, 6, 12]
        lis = [(i, defValue[seq], 0) for seq, i in enumerate(config)]
        self._radarChart.setChartDatum(lis)
    #
    def setupUnit(self):
        mainLayout = qtCore.QGridLayout_(self)
        # Statistics
        self._radarChart = qtWidgets.QtRadarchart()
        mainLayout.addWidget(self._radarChart, 0, 0, 0, 0)


