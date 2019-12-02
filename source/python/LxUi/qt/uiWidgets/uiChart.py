# coding:utf-8
from LxUi import uiCore
#
from LxUi.qt.uiModels import uiChartModel
#
from LxUi.qt.uiBasic import uiWidgetBasic


#
class UiRadarChart(uiWidgetBasic._UiChartBasic):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(uiCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initChartBasic()
        self._initRadarChart()
        #
        self.setupUi()
        #
        self.sectorDrawData = []
        self.markDrawData = []
        self.percentDrawData = []
    #
    def _initRadarChart(self):
        self._initRadarChartUi()
    #
    def _initRadarChartUi(self):
        self._mapBackgroundRgba = 63, 127, 255, 255
        self._mapBorderRgba = 159, 159, 159, 255
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        #
        if self.chartModel().image() is not None:
            if self.chartModel().imageClipPath() is not None:
                painter.setClipPath(self.chartModel().imageClipPath())
            #
            painter.setDrawImage(
                self.chartModel().imageRect(),
                self.chartModel().image()
            )
            painter.setClipRect(self.chartModel().basicRect())
        #
        painter.setRenderHint(uiCore.QtGui.QPainter.Antialiasing)
        #
        drawDatum = self.chartModel().drawDatum()
        if drawDatum:
            basicDrawDatum = self.chartModel()._radarBasicDrawDatum
            mapDrawDatum = self.chartModel()._radarMapDrawDatum
            hoverPoint = uiCore.QtCore.QPoint(*self.chartModel().pressHoverPos())
            #
            if basicDrawDatum is not None:
                for seq, i in enumerate(basicDrawDatum):
                    painter.setBackgroundRgba(self._uiRimBackgroundRgba)
                    painter.setBorderRgba(self._uiRimBorderRgba)
                    painter.setBrushStyle(uiCore.QtCore.Qt.FDiagPattern)
                    if seq == 0:
                        if self.chartModel().image() is None:
                            painter.drawPolygon(i)
                        else:
                            painter.drawPolyline(i)
                    else:
                        painter.drawPolyline(i)
            #
            if mapDrawDatum is not None:
                mapBrush, serverPolygon, localPolygon = mapDrawDatum
                #
                painter.setBrush(mapBrush)
                painter.setBorderRgba(self._mapBorderRgba)
                painter.drawPolygon(localPolygon)
                #
                painter.setBackgroundRgba(self._mapBackgroundRgba)
                painter.setBorderRgba(self._mapBorderRgba)
                painter.setBrushStyle(uiCore.QtCore.Qt.FDiagPattern)
                # painter.drawPolygon(serverPolygon)
            #
            for i in drawDatum:
                backgroundRgba, borderRgba, basicPath, textPoint0, textPoint1, showText0, showText1, _, _, mapEllipse = i
                #
                r, g, b, a = backgroundRgba
                painter.setBackgroundRgba([(r * .75, g * .75, b * .75, 255), (r, g, b, 255)][mapEllipse.contains(hoverPoint)])
                painter.setBorderRgba(borderRgba)
                #
                painter.drawEllipse(mapEllipse)
                #
                painter.drawText(textPoint0, showText0)
                painter.drawText(textPoint1, showText1)
    #
    def chartModel(self):
        return self._chartModel
    #
    def setupUi(self):
        self._chartModel = uiChartModel.UiRadarChartModel(self)


#
class UiSectorChart(uiWidgetBasic._UiChartBasic):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(uiCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initChartBasic()
        #
        self.setupUi()
        #
        self.sectorDrawData = []
        self.markDrawData = []
        self.percentDrawData = []
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        #
        if self.chartModel().image() is not None:
            painter.setDrawImage(
                self.chartModel().imageRect(),
                self.chartModel().image()
            )
            #
            painter.setBackgroundRgba(self._uiImageBackgroundRgba)
            painter.setBorderRgba(self._uiImageBorderRgba)
            painter.drawRect(self.chartModel().imageRect())
        #
        painter.setRenderHint(uiCore.QtGui.QPainter.Antialiasing)
        #
        drawDatum = self.chartModel().drawDatum()
        if drawDatum:
            hoverPoint = uiCore.QtCore.QPoint(*self.chartModel().pressHoverPos())
            for i in drawDatum:
                backgroundRgba, borderRgba, basicPath, percentPath, textPoint, textPolyline, textEllipse, showPercent = i
                #
                painter.setBackgroundRgba(self._uiRimBackgroundRgba)
                painter.setBorderRgba(self._uiRimBorderRgba)
                painter.setBrushStyle(uiCore.QtCore.Qt.FDiagPattern)
                painter.drawPath(basicPath)
                #
                r, g, b, a = backgroundRgba
                painter.setBackgroundRgba([(r, g, b, 96), (r, g, b, 255)][percentPath.contains(hoverPoint) or textEllipse.contains(hoverPoint)])
                painter.setBorderRgba(borderRgba)
                painter.drawPath(percentPath)
                #
                painter.drawPolyline(textPolyline)
                painter.drawEllipse(textEllipse)
                #
                painter.drawText(textPoint, showPercent)
    #
    def setupUi(self):
        self._chartModel = uiChartModel.UiSectorChartModel(self)