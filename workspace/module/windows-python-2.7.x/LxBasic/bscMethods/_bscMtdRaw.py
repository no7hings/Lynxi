# coding:utf-8
from LxBasic import bscConfigure, bscCore

from LxBasic.bscMethods import _bscMtdDcc


class StrUnderline(object):
    @classmethod
    def toLabel(cls, *labels):
        return labels[0] + ''.join([i.capitalize() for i in labels[1:]])


class StrCamelcase(bscCore.Basic):
    @classmethod
    def toPrettify(cls, string):
        return ' '.join([str(x).capitalize() for x in cls.MOD_re.findall(r'[a-zA-Z][a-z]*[0-9]*', string)])

    @classmethod
    def toUiPath(cls, strings, isPrettify=False):
        if isPrettify is True:
            strings = [cls.toPrettify(i) for i in cls.toStringList(strings)]
        return cls._toPathString(strings, '>')


class TxtHtml(bscCore.Basic):
    color_html_lis = bscConfigure.Ui().htmlColors
    color_html_dic = bscConfigure.Ui().htmlColorDict

    family_lis = bscConfigure.Ui().families

    @classmethod
    def _getHtmlColor(cls, *args):
        arg = args[0]
        if isinstance(arg, (float, int)):
            return cls.color_html_lis[int(arg)]
        elif isinstance(arg, (str, unicode)):
            return cls.color_html_dic.get(arg, '#dfdfdf')
        return '#dfdfdf'

    @classmethod
    def toHtml(cls, string, fontColor=u'white', fontSize=10, lineHeight=12):
        htmlColor = cls._getHtmlColor(fontColor)
        #
        html = u'''
            <html>
                <style type="text/css">p{{line-height:{4}px}}</style>
                <span style="font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>
            </html>
        '''.format(string, fontSize, cls.family_lis[0], htmlColor, lineHeight)
        return html
    
    @classmethod
    def getHtmls(cls, string, fontColor=u'white', fontSize=10, lineHeight=12):
        htmlColor = cls._getHtmlColor(fontColor)
        #
        stringLis = string.split('\r\n')
        if len(stringLis) > 1:
            s = ''.join([u'<p>{}</p>'.format(i) for i in stringLis])
        else:
            s = string
        #
        html = u'''
            <html>
                <style>p{{line-height:{4}px}}</style>
                <span style="font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>
            </html>
        '''.format(s, fontSize, cls.family_lis[0], htmlColor, lineHeight)
        return html

    @classmethod
    def toHtmlSpan(cls, string, fontColor=u'white', fontSize=10):
        htmlColor = cls._getHtmlColor(fontColor)
        #
        viewExplain = u'''
            <span style="font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>
        '''.format(string, fontSize, cls.family_lis[0], htmlColor)
        return viewExplain

    @classmethod
    def toHtmlSpanTime(cls, lString='', fontColor=u'gray', fontSize=10):
        htmlColor = cls._getHtmlColor(fontColor)
        #
        string = cls._getActivePrettifyTime()
        htmlString = u'''
            <span style="font-family:'{3}';font-size:{2}pt;color:{4};">{1}&lt;{0}&gt;</span>
        '''.format(string, lString, fontSize, cls.family_lis[0], htmlColor)
        return htmlString

    @classmethod
    def toHtmlSpanSuper(cls, string, fontColor=u'orange', fontSize=10):
        htmlColor = cls._getHtmlColor(fontColor)
        viewSuper = u'''
            <span style="vertical-align:super;font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>
        '''.format(string, fontSize, cls.family_lis[0], htmlColor)
        return viewSuper

    @classmethod
    def toHtmlSpanSub(cls, string, fontColor=u'orange', fontSize=10):
        htmlColor = cls._getHtmlColor(fontColor)
        viewSuper = u'''
            <span style="vertical-align:sub;font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>
        '''.format(string, fontSize, cls.family_lis[0], htmlColor)
        return viewSuper

    @classmethod
    def toHtmlMayaConnection(cls, sourceAttr, targetAttr, namespaceFilter):
        def getBranch(attr):
            namespace = _bscMtdDcc.MayaPath.getNamespace(attr)
            name = _bscMtdDcc.MayaPath.getName(attr)
            attrName = _bscMtdDcc.MayaPath.getAttributeName(attr)
            #
            namespaceSep = _bscMtdDcc.MayaPath.attributeSep()
            #
            if namespace:
                namespaceHtml = cls.toHtmlSpan(namespace, 7, 10) + cls.toHtmlSpan(namespaceSep, 3, 10)
            else:
                namespaceHtml = ''
            #
            if attr.startswith(namespaceFilter):
                html = namespaceHtml + cls.toHtmlSpan(name[:-len(attrName)], 4, 10) + cls.toHtmlSpan(attrName, 6, 10)
            else:
                html = namespaceHtml + cls.toHtmlSpan(name[:-len(attrName)], 1, 10) + cls.toHtmlSpan(attrName, 6, 10)
            #
            return html

        #
        sourceHtml = getBranch(sourceAttr)
        targetHtml = getBranch(targetAttr)
        #
        string = sourceHtml + cls.toHtmlSpan('>>', 3, 10) + targetHtml
        return string

    @classmethod
    def toHtmlMayaRenderImage(cls, prefix, string, fontSize=8, lineHeight=10):
        htmls = []
        #
        colorDic = {
            '<Scene>': '#ff0000',
            '<Camera>': '#ffaa00',
            '<RenderLayer>': '#aaff00',
            '<Version>': '#00ff00',
            '<Extension>': '#00ffaa',
            '<RenderPass>': '#00aaff',
            '<RenderPassFileGroup>': '#0000ff'
        }
        colorIndexDic = {}
        if prefix and string:
            splitPrefix = prefix.split('/')
            for seq, i in enumerate(splitPrefix):
                colorIndexDic[seq] = colorDic[i]
            #
            splitString = string.split('/')
            for seq, s in enumerate(splitString):
                if s:
                    htmlColor = colorIndexDic[seq]
                    #
                    html = u'''<span style="font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>'''.format(
                        s, fontSize, cls.family_lis[0], htmlColor
                    )
                    htmls.append(html)
        #
        htmlSep = u'''<span style="font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>'''.format(u'>', fontSize, cls.family_lis[0], cls.color_html_lis[6]
        )
        #
        htmlString = u'''<html><style>p{{line-height:{1}px}}</style>{0}</html>'''.format(htmlSep.join(htmls), lineHeight)
        return htmlString


class Value(object):
    @classmethod
    def stepTo(cls, value, delta, step, valueRange):
        min0, max0 = valueRange
        min1, max1 = min0 + step, max0 - step
        if value < min1:
            if 0 < delta:
                value += step
            else:
                value = min0
        elif min1 <= value <= max1:
            value += [-step, step][delta > 0]
        elif max1 < value:
            if delta < 0:
                value -= step
            else:
                value = max0
        return value

    @classmethod
    def mapTo(cls, value, sourceValueRange, targetValueRange):
        assert isinstance(sourceValueRange, (tuple, list)), 'Argument Error, "sourceValueRange" Must "tuple" or "list".'
        assert isinstance(targetValueRange, (tuple, list)), 'Argument Error, "targetValueRange" Must "tuple" or "list".'

        min0, max0 = sourceValueRange
        min1, max1 = targetValueRange
        #
        if max0 - min0 > 0:
            percent = float(value - min0) / float(max0 - min0)
            #
            value_ = (max1 - min1) * percent + min1
            return value_
        else:
            return min1

    @classmethod
    def toSizePrettify(cls, value):
        string = value
        #
        dv = 1000
        lis = [(dv ** 4, 'T'), (dv ** 3, 'B'), (dv ** 2, 'M'), (dv ** 1, 'K')]
        #
        if value >= dv:
            for i in lis:
                s = int(abs(value)) / i[0]
                if s:
                    string = str(round(float(value) / float(i[0]), 2)) + i[1]
                    break
        else:
            string = value
        #
        return str(string)

    @classmethod
    def toFileSizePrettify(cls, value):
        string = value
        #
        dv = 1024
        lis = [(dv ** 4, 'T'), (dv ** 3, 'G'), (dv ** 2, 'M'), (dv ** 1, 'K')]
        #
        for i in lis:
            s = abs(value) / i[0]
            if s:
                string = str(round(float(value) / float(i[0]), 2)) + i[1]
                break
        #
        return str(string)

    @classmethod
    def toPrettify(cls, value, useMode):
        if useMode == 0:
            return cls.toSizePrettify(value)
        else:
            return cls.toFileSizePrettify(value)

    @classmethod
    def toPercentPrettify(cls, value, maximumValue, roundCount=3):
        valueRange = 100
        if maximumValue > 0:
            percent = round(float(value) / float(maximumValue), roundCount) * valueRange
        else:
            if value > 0:
                percent = float('inf')
            elif value < 0:
                percent = float('-inf')
            else:
                percent = 0
        return percent


class Range(object):
    pass


class List(object):
    @classmethod
    def splitTo(cls, lis, splitCount):
        lis_ = []
        count = len(lis)
        cutCount = int(count / splitCount)
        for i in range(cutCount + 1):
            subLis = lis[i * splitCount:min((i + 1) * splitCount, count)]
            if subLis:
                lis_.append(subLis)
        return lis_

    @classmethod
    def cleanupTo(cls, lis):
        lis_ = []
        [lis_.append(i) for i in lis if i not in lis_]
        return lis_


class Array(List):
    @classmethod
    def getDefects(cls, lis, useMode=0):
        lis_ = []

        if lis:
            maxiNumber = max(lis)
            miniNumber = min(lis)
            if useMode == 1:
                miniNumber = 0
            for i in range(miniNumber, maxiNumber + 1):
                if not i in lis:
                    lis_.append(i)
        return lis_

    @classmethod
    def toRangecase(cls, lis):
        lis_ = []
        #
        if lis:
            maximum, minimum = max(lis), min(lis)
            #
            start, end = None, None
            count = len(lis)
            index = 0
            #
            lis.sort()
            for seq in lis:
                if index > 0:
                    pre = lis[index - 1]
                else:
                    pre = None
                #
                if index < (count - 1):
                    nex = lis[index + 1]
                else:
                    nex = None
                #
                if pre is None and nex is not None:
                    start = minimum
                    if seq - nex != -1:
                        lis_.append(start)
                elif pre is not None and nex is None:
                    end = maximum
                    if seq - pre == 1:
                        lis_.append((start, end))
                    else:
                        lis_.append(end)
                elif pre is not None and nex is not None:
                    if seq - pre != 1 and seq - nex != -1:
                        lis_.append(seq)
                    elif seq - pre == 1 and seq - nex != -1:
                        end = seq
                        lis_.append((start, end))
                    elif seq - pre != 1 and seq - nex == -1:
                        start = seq
                #
                index += 1
            #
            return lis_
        return []


class Position2d(bscCore.Basic):
    @classmethod
    def toRegion(cls, position, size):
        x, y = position
        width, height = size
        if 0 <= x < width / 2 and 0 <= y < height / 2:
            value = 0
        elif width / 2 <= x < width and 0 <= y < height / 2:
            value = 1
        elif 0 <= x < width / 2 and height / 2 <= y < height:
            value = 2
        else:
            value = 3

        return value

    @classmethod
    def regionTo(cls, position, size, maximumSize, offset):
        x, y = position
        width, height = size
        maxWidth, maxHeight = maximumSize
        xOffset, yOffset = offset

        region = cls.toRegion(
            position=position,
            size=(maxWidth, maxHeight)
        )

        if region == 0:
            x_ = x + xOffset
            y_ = y + yOffset
        elif region == 1:
            x_ = x - width - xOffset
            y_ = y + yOffset
        elif region == 2:
            x_ = x + xOffset
            y_ = y - height - yOffset
        else:
            x_ = x - width - xOffset
            y_ = y - height - yOffset

        return x_, y_, region

    @classmethod
    def toLength(cls, position0, position1):
        x0, y0 = position0
        x1, y1 = position1
        return cls.MOD_math.sqrt(((x0 - x1) ** 2) + ((y0 - y1) ** 2))

    @classmethod
    def toAngle(cls, position0, position1):
        x0, y0 = position0
        x1, y1 = position1

        radian = 0.0
        #
        r0 = 0.0
        r90 = cls.MOD_math.pi / 2.0
        r180 = cls.MOD_math.pi
        r270 = 3.0 * cls.MOD_math.pi / 2.0

        if x0 == x1:
            if y0 < y1:
                radian = r0
            elif y0 > y1:
                radian = r180
        elif y0 == y1:
            if x0 < x1:
                radian = r90
            elif x0 > x1:
                radian = r270

        elif x0 < x1 and y0 < y1:
            radian = cls.MOD_math.atan2((-x0 + x1), (-y0 + y1))
        elif x0 < x1 and y0 > y1:
            radian = r90 + cls.MOD_math.atan2((y0 - y1), (-x0 + x1))
        elif x0 > x1 and y0 > y1:
            radian = r180 + cls.MOD_math.atan2((x0 - x1), (y0 - y1))
        elif x0 > x1 and y0 < y1:
            radian = r270 + cls.MOD_math.atan2((-y0 + y1), (x0 - x1))
        return radian * 180 / cls.MOD_math.pi


class Rect2d(object):
    @classmethod
    def ContainPos(cls, rect, position):
        x0, y0, width, height = rect
        x1, y1 = position
        if rect is not None:
            return x0 <= x1 <= x0 + width and y0 <= y1 <= y0 + height
        return False


class Ellipse2d(bscCore.Basic):
    @classmethod
    def positionAtAngle(cls, center, radius, angle):
        x, y = center
        xp = cls.MOD_math.sin(cls.MOD_math.radians(angle)) * radius / 2 + x + radius / 2
        yp = cls.MOD_math.cos(cls.MOD_math.radians(angle)) * radius / 2 + y + radius / 2
        return xp, yp


class Color(object):
    @classmethod
    def mapToFloat(cls, r, g, b):
        def mapFnc_(v):
            return float(v) / float(255)
        return mapFnc_(r), mapFnc_(g), mapFnc_(b)

    @classmethod
    def mapTo256(cls, r, g, b):
        def mapFnc_(v):
            return int(v*256)
        return mapFnc_(r), mapFnc_(g), mapFnc_(b)

    @classmethod
    def hsv2Rgb(cls, h, s, v, maximum=255):
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


class Frame(object):
    @classmethod
    def toTime(cls, frameValue, fpsValue=24):
        second = int(frameValue) / fpsValue
        h = second / 3600
        m = second / 60 - 60 * h
        s = second - 3600 * h - 60 * m
        return h, m, s

    @classmethod
    def toTimeString(cls, frameValue, fpsValue=24):
        h, m, s = cls.toTime(frameValue, fpsValue)
        return '%s:%s:%s' % (str(h).zfill(2), str(m).zfill(2), str(s).zfill(2))