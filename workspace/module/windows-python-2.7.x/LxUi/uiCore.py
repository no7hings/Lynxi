# coding:utf-8
import math

from LxCore import lxBasic, lxScheme

Lynxi_Ui_Family_Lis = [
    'Arial',
    'Arial Unicode MS',
    'Arial Black'
]

Lynxi_Ui_Window_Size_Default = 1920 * .85, 1080 * .85
Lynxi_Ui_Window_SubSize_Default = 1920 * .75, 1080 * .75
Lynxi_Ui_Window_Size_Dialog = 1920 * .5, 1080 * .5


class Basic(object):
    @classmethod
    def _lxIconRoot(cls):
        return lxScheme.Directory().icon.server
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

    @staticmethod
    def _toGeometryRemap(size0, size1):
        w0, h0 = size0
        w1, h1 = size1
        if h0 > 0 and h1 > 0:
            pr0 = float(w0)/float(h0)
            pr1 = float(w1)/float(h1)
            smax1 = max(w1, h1)
            smin1 = min(w1, h1)
            if pr0 > 1:
                w, h = smin1, smin1/pr0
            elif pr0 < 1:
                w, h = smin1, smin1*pr0
            else:
                w, h = smin1, smin1
            x, y = (w1 - w)/2, (h1 - h)/2
            return x, y, w, h
        else:
            return 0, 0, w0, h0

    @staticmethod
    def hsvToRgb(h, s, v, maximum=255):
        h = float(h % 360.0)
        s = float(max(min(s, 1.0), 0.0))
        v = float(max(min(v, 1.0), 0.0))
        #
        c = v * s
        x = c * (1 - abs((h / 60.0) % 2 - 1))
        m = v - c
        if 0 <= h < 60:
            r_, g_, b_ = c, x, 0
        elif 60 <= h < 120:
            r_, g_, b_ = x, c, 0
        elif 120 <= h < 180:
            r_, g_, b_ = 0, c, x
        elif 180 <= h < 240:
            r_, g_, b_ = 0, x, c
        elif 240 <= h < 300:
            r_, g_, b_ = x, 0, c
        else:
            r_, g_, b_ = c, 0, x
        #
        if maximum == 255:
            r, g, b = int(round((r_ + m) * maximum)), int(round((g_ + m) * maximum)), int(round((b_ + m) * maximum))
        else:
            r, g, b = float((r_ + m)), float((g_ + m)), float((b_ + m))
        return r, g, b

    @staticmethod
    def getRgbByString(string, maximum=255):
        a = int(''.join([str(ord(i)).zfill(3) for i in string]))
        b = a % 3
        i = int(a / 256) % 3
        n = int(a % 256)
        if a % 2:
            if i == 0:
                r, g, b = 64 + 64 * b, n, 0
            elif i == 1:
                r, g, b = 0, 64 + 64 * b, n
            else:
                r, g, b = 0, n, 64 + 64 * b
        else:
            if i == 0:
                r, g, b = 0, n, 64 + 64 * b
            elif i == 1:
                r, g, b = 64 + 64 * b, 0, n
            else:
                r, g, b = 64 + 64 * b, n, 0
        #
        return r / 255.0 * maximum, g / 255.0 * maximum, b / 255.0 * maximum

    @staticmethod
    def _toShowNumber(number):
        showNumber = number
        #
        dv = 1000
        lis = [(dv ** 4, 'T'), (dv ** 3, 'B'), (dv ** 2, 'M'), (dv ** 1, 'K')]
        #
        if number >= dv:
            for i in lis:
                s = int(abs(number)) / i[0]
                if s:
                    showNumber = str(round(float(number) / float(i[0]), 2)) + i[1]
                    break
        else:
            showNumber = number
        #
        return str(showNumber)

    @staticmethod
    def _toShowFileSize(number):
        showNumber = number
        #
        dv = 1024
        lis = [(dv ** 4, 'T'), (dv ** 3, 'G'), (dv ** 2, 'M'), (dv ** 1, 'K')]
        #
        for i in lis:
            s = abs(number) / i[0]
            if s:
                showNumber = str(round(float(number) / float(i[0]), 2)) + i[1]
                break
        #
        return str(showNumber)

    @staticmethod
    def _lxMayaPngIconKeyword(nodeTypeString):
        return 'maya#out_{}'.format(nodeTypeString)

    @staticmethod
    def _lxMayaSvgIconKeyword(nodeTypeString):
        return 'maya@svg#{}'.format(nodeTypeString)
