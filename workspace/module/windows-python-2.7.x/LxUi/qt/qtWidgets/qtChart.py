# coding:utf-8
from LxUi.qt import qtCore
#
from LxUi.qt.qtModels import qtChartModel
#
from LxUi.qt.qtObjects import qtAbcWidget


#
class QtRadarchart(qtAbcWidget.QtAbcObj_Chart):
    MODEL_CHART_CLS = qtChartModel.QtRadarchartModel

    def __init__(self, *args, **kwargs):
        self.clsSuper = super(qtCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjChart()
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
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix

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
        painter.setRenderHint(qtCore.QtGui.QPainter.Antialiasing)
        #
        drawDatum = self.chartModel().drawDatum()
        if drawDatum:
            basicDrawDatum = self.chartModel()._radarBasicDrawDatum
            mapDrawDatum = self.chartModel()._radarMapDrawDatum
            hoverPoint = qtCore.QtCore.QPoint(*self.chartModel().pressHoverPos())
            #
            if basicDrawDatum is not None:
                for seq, i in enumerate(basicDrawDatum):
                    painter.setBackgroundRgba(self._uiRimBackgroundRgba)
                    painter.setBorderRgba(self._uiRimBorderRgba)
                    painter.setBrushStyle(qtCore.QtCore.Qt.FDiagPattern)
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
                painter.setBrushStyle(qtCore.QtCore.Qt.FDiagPattern)
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

        # painter.end()
    #
    def chartModel(self):
        return self._chartModel


#
class QtSectorchart(qtAbcWidget.QtAbcObj_Chart):
    MODEL_CHART_CLS = qtChartModel.QtSectorchartModel

    def __init__(self, *args, **kwargs):
        self.clsSuper = super(qtCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjChart()
        #
        self.setupUi()
        #
        self.sectorDrawData = []
        self.markDrawData = []
        self.percentDrawData = []
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix
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
        painter.setRenderHint(qtCore.QtGui.QPainter.Antialiasing)
        #
        drawDatum = self.chartModel().drawDatum()
        if drawDatum:
            hoverPoint = qtCore.QtCore.QPoint(*self.chartModel().pressHoverPos())
            for i in drawDatum:
                backgroundRgba, borderRgba, basicPath, percentPath, textPoint, textPolyline, textEllipse, showPercent = i
                #
                painter.setBackgroundRgba(self._uiRimBackgroundRgba)
                painter.setBorderRgba(self._uiRimBorderRgba)
                painter.setBrushStyle(qtCore.QtCore.Qt.FDiagPattern)
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

        # painter.end()
