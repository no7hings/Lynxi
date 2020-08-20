# coding:utf-8
from LxBasic import bscMethods

from LxGui.qt import qtCore, guiQtMdlAbs


#


#
class QtRadarchartModel(guiQtMdlAbs.AbsGuiQtChartMdl):
    def __init__(self, widget):
        self._initAbsGuiQtChartMdl()
        self._initRadarChart()
        #
        self.setWidget(widget)
    #
    def _initRadarChart(self):
        self._initRadarChartAttr()
    #
    def _initRadarChartAttr(self):
        self._radarBasicDrawDatum = None
        self._radarMapDrawDatum = None
    #
    def _updateDrawDatum(self):
        widget = self.widget()
        datum = self.chartDatum()
        if datum:
            width, height = self.width(), self.height()
            xPos, yPos = 0, 0
            side = self._uiSide
            #
            radius = int(min(width, height)) - side*2
            #
            spacing = 8
            #
            if self._hAlign is qtCore.AlignLeft:
                xOffset = xPos + side
            elif self._hAlign is qtCore.AlignHCenter:
                xOffset = xPos + (width - radius)/2
            else:
                xOffset = width - radius - side
            if self._vAlign is qtCore.AlignTop:
                yOffset = yPos + side
            elif self._vAlign is qtCore.AlignVCenter:
                yOffset = yPos + (height - radius)/2
            else:
                yOffset = height - radius - side
            #
            drawDatum = self._toRadarChartDrawDatum(
                widget, datum, xOffset, yOffset, radius, spacing
            )
            self.setDrawDatum(drawDatum)
            #
            self._radarBasicDrawDatum, self._uiImageClipPath = self._toRadarBasicDrawDatum(
                datum, xOffset, yOffset, radius, spacing
            )
            self._radarMapDrawDatum = self._toRadarMapDrawDatum(
                drawDatum, xOffset, yOffset, radius
            )
        #
        self._updateWidgetState()
    @classmethod
    def _toRadarSubBasicPointLis(cls, cx, cy, radius, count):
        pointLis = []
        for seq in range(count):
            angle = 360 * float(seq) / float(count) + 180
            x, y = cx + cls.fnc_sin(cls.fnc_angle(angle)) * radius / 2, cy + cls.fnc_cos(cls.fnc_angle(angle)) * radius / 2
            pointLis.append(cls.CLS_point(x, y))
        #
        return pointLis + pointLis[0:1]
    @classmethod
    def _toRadarBasicDrawDatum(cls, datum, xOffset, yOffset, radius, spacing):
        count = len(datum)
        cx, cy = xOffset + radius/2, yOffset + radius/2
        #
        polygonLis = []
        for i in range(6):
            r = radius*float(i + 1)/float(6)
            polygon = cls.CLS_polygon(
                cls._toRadarSubBasicPointLis(cx, cy, r, count)
            )
            polygonLis.append(polygon)
        #
        clipPath = cls.CLS_painterPath()
        clipPath.addPolygon(cls.CLS_polygonF(cls._toRadarSubBasicPointLis(cx, cy, radius, count)))
        #
        polygonLis.reverse()
        return polygonLis, clipPath
    @classmethod
    def _toRadarMapDrawDatum(cls, drawDatum, xOffset, yOffset, radius):
        ia = 90
        cx, cy = xOffset + radius/2, yOffset + radius/2
        #
        serverPointLis = []
        localPointLis = []
        rgbaLis0 = []
        if drawDatum:
            for i in drawDatum:
                backgroundRgba, borderRgba, basicPath, textPoint0, textPoint1, showText0, showText1, serverMapPoint, localMapPoint, mapEllipse = i
                serverPointLis.append(serverMapPoint)
                localPointLis.append(localMapPoint)
                rgbaLis0.append(backgroundRgba)
        #
        backgroundGradient = qtCore.QtGui.QConicalGradient(cx, cy, ia)
        for seq, rgba in enumerate(rgbaLis0):
            r, g, b, a = rgba
            backgroundGradient.setColorAt(float(seq) / float(len(rgbaLis0)), qtCore.CLS_color(r, g, b, 127))
        #
        r, g, b, a = rgbaLis0[0]
        backgroundGradient.setColorAt(1, qtCore.CLS_color(r, g, b, 127))
        #
        brush = cls.CLS_brush(backgroundGradient)
        #
        serverPolygon = cls.CLS_polygon(serverPointLis)
        localPolygon = cls.CLS_polygon(localPointLis)
        return brush, serverPolygon, localPolygon
    @classmethod
    def _toRadarSubChartDrawDatumAt(cls, widget, itemIndex, itemIndexCount, maxValue, subDatum, xOffset, yOffset, radius, spacing):
        eR = 4
        ia = -90
        explain, serverValue, localValue = subDatum
        #
        serverPercent = float(serverValue)/float(max(maxValue, 1))
        localPercent = float(localValue)/float(max(maxValue, 1))
        #
        subValue = localValue - serverValue
        subPercent = float(subValue)/float(max(serverValue, 1))
        showText0 = explain
        if subValue == 0:
            showText1 = '{}'.format(cls.mtd_raw_value.toSizePrettify(localValue))
        else:
            showText1 = '{} ( {}% )'.format(
                cls.mtd_raw_value.toSizePrettify(localValue),
                cls.mtd_raw_value.toPercentPrettify(value=serverValue, maximumValue=subValue)
            )
        #
        if maxValue == 0:
            borderRgba = 95, 95, 95, 255
            backgroundRgba = 95, 95, 95, 255
        else:
            if subPercent == 0:
                r, g, b = 64, 255, 127
            elif subPercent > 0:
                
                r, g, b = bscMethods.Color.hsv2rgb(45*(1 - min(subPercent, 1)), 1, 1)
            else:
                r, g, b = bscMethods.Color.hsv2rgb(120 + 45*(1 - min(subPercent, 1)), 1, 1)
            #
            backgroundRgba = r, g, b, 255
            borderRgba = r, g, b, 255
        #
        localDrawPercent = localPercent*.75
        serverDrawPercent = serverPercent*.75
        #
        x, y = xOffset, yOffset
        r = radius
        cx, cy = x + r/2, y + r/2
        basicPath = cls.CLS_painterPath()
        basicPath.moveTo(cx, cy)
        startAngle = 360*(float(itemIndex)/float(itemIndexCount)) + 180
        endAngle = 360*(float(itemIndex + 1)/float(itemIndexCount)) + 180
        basicPath.arcTo(x, y, r, r, startAngle + ia, endAngle + ia)
        #
        xText0, yText0 = cx + cls.fnc_sin(cls.fnc_angle(startAngle))*radius/2, cy + cls.fnc_cos(cls.fnc_angle(startAngle))*radius/2
        #
        xMap0, yMap0 = cx + cls.fnc_sin(cls.fnc_angle(startAngle))*radius/2*localDrawPercent, cy + cls.fnc_cos(cls.fnc_angle(startAngle))*radius/2*localDrawPercent
        xMap1, yMap1 = cx + cls.fnc_sin(cls.fnc_angle(startAngle))*radius/2*serverDrawPercent, cy + cls.fnc_cos(cls.fnc_angle(startAngle))*radius/2*serverDrawPercent
        #
        textWidth0 = widget.fontMetrics().width(explain)
        textWidth1 = widget.fontMetrics().width(showText1)
        textHeight = widget.fontMetrics().height()
        #
        textPoint0 = cls.CLS_point(xText0 - textWidth0/2, yText0 - textHeight/2)
        textPoint1 = cls.CLS_point(xText0 - textWidth1/2, yText0 + textHeight/2)
        mapEllipse = cls.CLS_rect(xMap0 - eR, yMap0 - eR, eR*2, eR*2)
        #
        localMapPoint = cls.CLS_point(xMap0, yMap0)
        serverMapPoint = cls.CLS_point(xMap1, yMap1)
        return backgroundRgba, borderRgba, basicPath, textPoint0, textPoint1, showText0, showText1, serverMapPoint, localMapPoint, mapEllipse
    @classmethod
    def _toRadarChartDrawDatum(cls, widget, datum, xOffset, yOffset, radius, spacing):
        lis = []
        if datum:
            itemIndexCount = len(datum)
            maxValue = max([i[2] for i in datum])
            for itemIndex, subDatum in enumerate(datum):
                subDrawDatum = cls._toRadarSubChartDrawDatumAt(
                    widget, itemIndex, itemIndexCount, maxValue, subDatum, xOffset, yOffset, radius, spacing
                )
                lis.append(subDrawDatum)
        return lis


#
class QtSectorchartModel(guiQtMdlAbs.AbsGuiQtChartMdl):
    # noinspection PyUnusedLocal
    def __init__(self, widget):
        self._initAbsGuiQtChartMdl()
        self._initSectorChart()
        #
        self.setWidget(widget)
    #
    def _initSectorChart(self):
        self._initSectorChartAttr()
    #
    def _initSectorChartAttr(self):
        pass
    #
    def _updateDrawDatum(self):
        datum = self.chartDatum()
        if datum:
            count = len(datum)
            #
            width, height = self.width(), self.height()
            xPos, yPos = 0, 0
            side = self._uiSide
            #
            radius = int(min(width, height)) - side*2
            tapeWidth = int(radius/count*.75)
            #
            spacing = 8
            #
            if self._hAlign is qtCore.AlignLeft:
                xOffset = xPos + side
            elif self._hAlign is qtCore.AlignHCenter:
                xOffset = xPos + (width - radius)/2
            else:
                xOffset = width - radius - side
            if self._vAlign is qtCore.AlignTop:
                yOffset = yPos + side
            elif self._vAlign is qtCore.AlignVCenter:
                yOffset = yPos + (height - radius)/2
            else:
                yOffset = height - radius - side
            #
            drawDatum = self._toSectorDrawDatum(
                datum, xOffset, yOffset, radius, tapeWidth, spacing
            )
            self.setDrawDatum(drawDatum)
        #
        self._updateWidgetState()
    @classmethod
    def _toSectorSubDrawDatumAt(cls, itemIndex, subDatum, xOffset, yOffset, radius, tapeWidth, spacing):
        eR = 4
        ia = 90
        explain, maxValue, value = subDatum
        percent = float(value)/float(max(maxValue, 1))
        #
        showText = '{} : {}%'.format(explain, cls.mtd_raw_value.toPercentPrettify(value=value, maximumValue=maxValue))
        #
        colorPercent = max(min(percent, 1), .05)
        if maxValue == 0:
            borderRgba = 95, 95, 95, 255
            backgroundRgba = 95, 95, 95, 255
        else:
            if percent == 1:
                r, g, b = 64, 255, 127
            elif percent > 1:
                r, g, b = bscMethods.Color.hsv2rgb(240 - min(percent*15, 45), 1, 1)
            else:
                r, g, b = bscMethods.Color.hsv2rgb(45*colorPercent, 1, 1)
            #
            backgroundRgba = r, g, b, 255
            borderRgba = r, g, b, 255
        #
        drawPercent = colorPercent*.75
        #
        xOut, yOut = xOffset + itemIndex*tapeWidth/2, yOffset + itemIndex*tapeWidth/2
        xIn, yIn = xOut + (tapeWidth - spacing)/2, yOut + (tapeWidth - spacing)/2
        rOut = radius - itemIndex*tapeWidth
        rIn = rOut - tapeWidth + spacing
        #
        rimPath = cls.CLS_painterPath()
        rimPath.addEllipse(
            xOut, yOut, rOut, rOut
        )
        rimPath.addEllipse(
            xIn, yIn, rIn, rIn
        )
        #
        cx, cy = xOut + rOut/2, yOut + rOut/2
        #
        subBasicPath = cls.CLS_painterPath()
        subBasicPath.moveTo(cx, cy)
        basicSubAngle = -360*.25
        subBasicPath.arcTo(xOut - 1, yOut - 1, rOut + 2, rOut + 2, ia, basicSubAngle)
        #
        subPercentPath = cls.CLS_painterPath()
        subPercentPath.moveTo(cx, cy)
        percentSubAngle = -360*(1 - drawPercent)
        subPercentPath.arcTo(xOut - 1, yOut - 1, rOut + 2, rOut + 2, ia, percentSubAngle)
        #
        basicPath = rimPath - subBasicPath
        percentPath = rimPath - subPercentPath
        #
        x1, y1 = cx, yOut + (tapeWidth - spacing)/4
        x2, y2 = x1 + tapeWidth/4, y1
        x3, y3 = x2 + tapeWidth/4, y2 + tapeWidth/4
        x4, y4 = x3 + tapeWidth/4, y3
        textPolyline = cls.CLS_polygon(
            [cls.CLS_point(x1, y1), cls.CLS_point(x2, y2), cls.CLS_point(x3, y3), cls.CLS_point(x4 - eR, y4)]
        )
        textPoint = cls.CLS_point(x4 + eR + 4, y4 + 4)
        mapEllipse = cls.CLS_rect(x4 - eR, y4 - eR, eR*2, eR*2)
        return backgroundRgba, borderRgba, basicPath, percentPath, textPoint, textPolyline, mapEllipse, showText
    @classmethod
    def _toSectorDrawDatum(cls, datum, xOffset, yOffset, radius, tapeWidth, spacing):
        lis = []
        if datum:
            for itemIndex, i in enumerate(datum):
                subDrawDatum = cls._toSectorSubDrawDatumAt(
                    itemIndex, i, xOffset, yOffset, radius, tapeWidth, spacing
                )
                lis.append(subDrawDatum)
        return lis

