# coding:utf-8
import math

from LxCore import lxBasic, lxConfigure

Lynxi_Module_Load_Order = [

]

Lynxi_Ui_Family_Lis = [
    'Arial',
    'Arial Unicode MS',
    'Arial Black'
]

# 0 ( 255, 0, 64 ), 1 (255, 255, 64), 2 (255, 127, 0), 3 (64, 255, 127), 4 (0, 223, 223),
# 5 (191, 191, 191), 6 (223, 223, 223), 7 (127, 127, 127), 8 (0, 0, 0)
Lynxi_Ui_Color_Html_Lis = [
    '#ff0040',
    '#ffff40',
    '#ff7f00',
    '#40ff7f',
    '#00bfbf',
    '#bfbfbf',
    '#dfdfdf',
    '#7f7f7f',
    '#000000'
]

Lynxi_Ui_Window_Size_Default = 1920 * .85, 1080 * .85
Lynxi_Ui_Window_SubSize_Default = 1920 * .75, 1080 * .75
Lynxi_Ui_Window_Size_Dialog = 1920 * .5, 1080 * .5


class Basic(object):
    @classmethod
    def _lxIconRoot(cls):
        return lxConfigure.IconSubRoot()._serverDirectory()
    @staticmethod
    def _toUiDatum(data):
        string = None
        if data is not None:
            if isinstance(data, bool):
                string = unicode(data)
            elif isinstance(data, int) or isinstance(data, float):
                string = unicode(data)
            elif isinstance(data, str) or isinstance(data, unicode):
                string = data
            elif isinstance(data, tuple) or isinstance(data, list):
                data = [unicode(i) for i in data]
                string = ','.join(data)
            elif isinstance(data, dict):
                string = ','.join([':'.join(i) for i in data.items()])
        else:
            string = unicode(data)
        #
        return string

    @staticmethod
    def isRectContainPos(rect, pos):
        boolean = False
        if rect is not None:
            x, y = pos
            #
            x_, y_ = rect.x(), rect.y()
            w_, h_ = rect.width(), rect.height()
            #
            boolean = x_ <= x <= x_ + w_ and y_ <= y <= y_ + h_
        return boolean

    @staticmethod
    def getLength(x1, y1, x2, y2):
        return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

    @staticmethod
    def getPointOnEllipse(x, y, r, a):
        xp = math.sin(math.radians(a)) * r / 2 + x + r / 2
        yp = math.cos(math.radians(a)) * r / 2 + y + r / 2
        return xp, yp

    @staticmethod
    def getRegionPos(xPos, yPos, maxWidth, maxHeight, width, height, xOffset=0, yOffset=0):
        def getRegion(x, y, w, h):
            if 0 <= x < w / 2 and 0 <= y < h / 2:
                value = 0
            elif w / 2 <= x < w and 0 <= y < h / 2:
                value = 1
            elif 0 <= x < w / 2 and h / 2 <= y < h:
                value = 2
            else:
                value = 3
            return value

        #
        region = getRegion(xPos, yPos, maxWidth, maxHeight)
        #
        if region == 0:
            xp = xPos + xOffset
            yp = yPos + yOffset
        elif region == 1:
            xp = xPos - width - xOffset
            yp = yPos + yOffset
        elif region == 2:
            xp = xPos + xOffset
            yp = yPos - height - yOffset
        else:
            xp = xPos - width - xOffset
            yp = yPos - height - yOffset
        #
        return xp, yp, region

    @staticmethod
    def getUiRegion(xPos, yPos, maxWidth, maxHeight):
        # 0, 1
        # 2, 3
        def getRegion(x, y, w, h):
            if 0 <= x < w / 2 and 0 <= y < h / 2:
                value = 0
            elif w / 2 <= x < w and 0 <= y < h / 2:
                value = 1
            elif 0 <= x < w / 2 and h / 2 <= y < h:
                value = 2
            else:
                value = 3
            return value

        #
        region = getRegion(xPos, yPos, maxWidth, maxHeight)
        #
        return region

    @staticmethod
    def getUiStrWidth(ui, string):
        linesep = '\n'
        if linesep in string:
            splitData = string.split(linesep)
            values = [ui.fontMetrics().width(i) for i in splitData]
            value = max(values)
        else:
            value = ui.fontMetrics().width(string)
        return value

    @classmethod
    def getUiStrWidthReduce(cls, ui, string, maxiWidth):
        def getIndex():
            width = 0
            for seq, i in enumerate(string):
                subWidth = cls.getUiStrWidth(ui, i)
                width = width + subWidth
                if width >= maxiWidth:
                    return seq - 3

        #
        index = getIndex()
        splitIndex = [max(getIndex(), 0), -1][index is None]
        boolean = cls.getUiStrWidth(ui, string) > maxiWidth
        return [string, string[:splitIndex] + '...'][boolean]

    @classmethod
    def setSvgColor(cls):
        pass

    @staticmethod
    def mapStepValue(value, delta, step, maximum, minimum):
        _max = maximum - step
        _min = minimum + step
        if value < _min:
            if 0 < delta:
                value += step
            else:
                value = minimum
        elif _min <= value <= _max:
            value += [-step, step][delta > 0]
        elif _max < value:
            if delta < 0:
                value -= step
            else:
                value = maximum
        return value

    @staticmethod
    def mapRangeValue(range1, range2, value1):
        assert isinstance(range1, tuple) or isinstance(range1, list), 'Argument Error, "range1" Must "tuple" or "list".'
        assert isinstance(range2, tuple) or isinstance(range2, list), 'Argument Error, "range1" Must "tuple" or "list".'
        min1, max1 = range1
        min2, max2 = range2
        #
        if max1 - min1 > 0:
            percent = float(value1 - min1) / float(max1 - min1)
            #
            value2 = (max2 - min2) * percent + min2
            return value2
        else:
            return min2

    @classmethod
    def _toLxOsIconFile(cls, iconKeyword, ext='.png'):
        isMayaIcon = iconKeyword.startswith('maya')
        #
        subLabel = 'table'
        #
        if iconKeyword:
            if '#' in iconKeyword:
                subLabel = iconKeyword.split('#')[0]
                iconKeyword = iconKeyword.split('#')[-1]
            if '@' in subLabel:
                ext = '.' + subLabel.split('@')[-1]
                subLabel = subLabel.split('@')[0]
        else:
            iconKeyword = ''
        #
        osFile = cls._lxIconRoot() + '/{}/{}{}'.format(subLabel, iconKeyword, ext)
        #
        if isMayaIcon:
            if lxBasic.isOsExist(osFile):
                return osFile
            else:
                return cls._lxIconRoot() + '/{}/{}{}'.format(subLabel, 'default', ext)
        else:
            return osFile

    @staticmethod
    def toShowPercent(maxValue, value, roundCount=3):
        valueRange = 100
        if maxValue > 0:
            percent = round(float(value) / float(maxValue), roundCount) * valueRange
        else:
            if value > 0:
                percent = float('inf')
            elif value < 0:
                percent = float('-inf')
            else:
                percent = 0
        return percent

    @staticmethod
    def frameToTime(frame, mode=0):
        second = int(frame) / 24
        h = second / 3600
        m = second / 60 - 60 * h
        s = second - 3600 * h - 60 * m
        if mode == 0:
            if s < 1:
                s = 1
        return '%s:%s:%s' % (str(h).zfill(2), str(m).zfill(2), str(s).zfill(2))

    @staticmethod
    def getAngle(x1, y1, x2, y2):
        radian = 0.0
        #
        r0 = 0.0
        r90 = math.pi / 2.0
        r180 = math.pi
        r270 = 3.0 * math.pi / 2.0
        #
        if x1 == x2:
            if y1 < y2:
                radian = r0
            elif y1 > y2:
                radian = r180
        elif y1 == y2:
            if x1 < x2:
                radian = r90
            elif x1 > x2:
                radian = r270
        elif x1 < x2 and y1 < y2:
            radian = math.atan2((-x1 + x2), (-y1 + y2))
        elif x1 < x2 and y1 > y2:
            radian = r90 + math.atan2((y1 - y2), (-x1 + x2))
        elif x1 > x2 and y1 > y2:
            radian = r180 + math.atan2((x1 - x2), (y1 - y2))
        elif x1 > x2 and y1 < y2:
            radian = r270 + math.atan2((-y1 + y2), (x1 - x2))
        return radian * 180 / math.pi
