# coding:utf-8
from LxBasic import bscMtdCore, bscCfg, bscMtdCore

from LxBasic.bscMethods import _bscMtdPath


class Raw(bscMtdCore.Mtd_BscUtility):
    @classmethod
    def toHash(cls, raw):
        return cls._stringToHash(unicode(raw))


class String(bscMtdCore.Mtd_BscUtility):
    @classmethod
    def toNumberEmbeddedList(cls, string):
        pieces = cls.MOD_re.compile(r'(\d+)').split(unicode(string))
        pieces[1::2] = map(int, pieces[1::2])
        return pieces

    @classmethod
    def toVariantCommand(cls, varName, string):
        def getStringLis():
            # noinspection RegExpSingleCharAlternation
            return [i for i in cls.MOD_re.split("<|>", string) if i]

        #
        def getVariantLis():
            varPattern = cls.MOD_re.compile(r'[<](.*?)[>]', cls.MOD_re.S)
            return cls.MOD_re.findall(varPattern, string)

        #
        def getVarStringLis():
            lis = []
            for i in strings:
                if i in variants:
                    lis.append(i)
                else:
                    v = '''"%s"''' % i
                    lis.append(v)
            return lis

        #
        strings = getStringLis()
        variants = getVariantLis()
        #
        varStrings = getVarStringLis()
        #
        command = '''{0} = u'{1}' % ({2})'''.format(varName, '%s' * len(strings), ', '.join(varStrings))
        return command

    @classmethod
    def toList(cls, string, includes=None):
        lis = []
        if isinstance(string, (str, unicode)):
            if includes:
                if string in includes:
                    lis = [string]
            else:
                lis = [string]
        elif isinstance(string, (tuple, list)):
            for i in string:
                if includes:
                    if i in includes:
                        lis.append(i)
                else:
                    lis.append(i)
        return lis

    @staticmethod
    def toRgb(string, maximum=255):
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

    @classmethod
    def toUniqueId(cls, string):
        return cls._stringToUniqueId(string)

    @classmethod
    def findSpans(cls, contentStr, keywordStr, matchCaseFlag=False, matchWordFlag=False):
        lis = []
        if contentStr and keywordStr:
            if matchWordFlag is True:
                p = r'\b{}\b'.format(keywordStr)
            else:
                p = keywordStr

            if matchCaseFlag is True:
                r = cls.MOD_re.finditer(p, contentStr)
            else:
                r = cls.MOD_re.finditer(p, contentStr, cls.MOD_re.I)

            for i in r:
                lis.append(i.span())
        return lis


class Variant(bscMtdCore.Mtd_BscUtility):
    @classmethod
    def covertTo(cls, varName, string):
        def getStringLis():
            # noinspection RegExpSingleCharAlternation
            return [i for i in cls.MOD_re.split("<|>", string) if i]
        #
        def getVariantLis():
            varPattern = cls.MOD_re.compile(r'[<](.*?)[>]', cls.MOD_re.S)
            return cls.MOD_re.findall(varPattern, string)
        #
        def getVarStringLis():
            lis = []
            for i in strings:
                if i in variants:
                    lis.append(i)
                else:
                    v = '''"%s"''' % i
                    lis.append(v)
            return lis
        #
        strings = getStringLis()
        variants = getVariantLis()
        #
        varStrings = getVarStringLis()
        #
        command = '''{0} = u'{1}' % ({2})'''.format(varName, '%s'*len(strings), ', '.join(varStrings))
        return command


class StrUnderline(bscMtdCore.Mtd_BscUtility):
    @classmethod
    def toLabel(cls, *labels):
        return labels[0] + ''.join([i.capitalize() for i in labels[1:]])

    @classmethod
    def toCamelcase(cls, string):
        return cls.MOD_re.sub(r'_(\w)', lambda x: x.group(1).upper(), string)


class StrCamelcase(bscMtdCore.Mtd_BscUtility):
    @classmethod
    def toPrettify(cls, string):
        return ' '.join([str(x).capitalize() for x in cls.MOD_re.findall(r'[a-zA-Z][a-z]*[0-9]*', string)])

    @classmethod
    def toUnderline(cls, string):
        return '_'.join([str(x).lower() for x in cls.MOD_re.findall(r'[a-zA-Z][a-z]*[0-9]*', string)])

    @classmethod
    def toUiPath(cls, strings, isPrettify=False):
        if isPrettify is True:
            strings = [cls.toPrettify(i) for i in cls._string2list(strings)]
        return cls._toPathString(strings, '>')


class TxtHtml(bscMtdCore.Mtd_BscUtility):
    color_html_lis = bscCfg.Ui().htmlColors
    color_html_dic = bscCfg.Ui().htmlColorDict

    family_lis = bscCfg.Ui().families

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
            namespace = _bscMtdPath.MaNodeString.namespace(attr)
            name = _bscMtdPath.MaNodeString.nodename(attr)
            attrName = _bscMtdPath.MaAttrpath.portpathString(attr)
            #
            namespacesep = _bscMtdPath.MaAttrpath.portsep()
            #
            if namespace:
                namespaceHtml = cls.toHtmlSpan(namespace, 7, 10) + cls.toHtmlSpan(namespacesep, 3, 10)
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
                percent = float(u'inf')
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
        lis_ = list(filter(None, set(lis)))
        lis_.sort(key=lis.index)
        return lis_

    @classmethod
    def extendFrom(cls, lis, subLis):
        [lis.append(i) for i in subLis if i not in lis]

    @staticmethod
    def toFrameRange(array):
        lis = []
        #
        maximum, minimum = max(array), min(array)
        #
        start, end = None, None
        count = len(array)
        index = 0
        #
        array.sort()
        for seq in array:
            if index > 0:
                pre = array[index - 1]
            else:
                pre = None
            #
            if index < (count - 1):
                nex = array[index + 1]
            else:
                nex = None
            #
            if pre is None and nex is not None:
                start = minimum
                if seq - nex != -1:
                    lis.append(start)
            elif pre is not None and nex is None:
                end = maximum
                if seq - pre == 1:
                    lis.append((start, end))
                else:
                    lis.append(end)
            elif pre is not None and nex is not None:
                if seq - pre != 1 and seq - nex != -1:
                    lis.append(seq)
                elif seq - pre == 1 and seq - nex != -1:
                    end = seq
                    lis.append((start, end))
                elif seq - pre != 1 and seq - nex == -1:
                    start = seq
            #
            index += 1
        #
        return lis


class Dict(object):
    @classmethod
    def getValue(cls, dic, key, failobj=None):
        if key in dic:
            return dic.get(key, failobj)

    @classmethod
    def getAsBoolean(cls, dic, key, failobj=False):
        if key in dic:
            return dic.get(key, failobj)
        return False


class NestedArray(object):
    @classmethod
    def mapTo(cls, nestedArray):
        """
        :param nestedArray: etc.[[1, 2], [1, 2]]
        :return: etc.[[1, 1], [1, 2], [2, 1], [2, 2]]
        """
        def rcsFnc_(index_):
            if index_ < count:
                _array = nestedArray[index_]
                for _i in _array:
                    c[index_] = _i
                    rcsFnc_(index_ + 1)
            else:
                lis.append(
                    bscCfg.BscUtility.MOD_copy.deepcopy(c)
                )

        lis = []
        count = len(nestedArray)
        c = [None]*count
        rcsFnc_(0)
        return lis


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


class Position2d(bscMtdCore.Mtd_BscUtility):
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
    def isContainPos(cls, rect, position):
        x0, y0, width, height = rect
        x1, y1 = position
        if rect is not None:
            return x0 <= x1 <= x0 + width and y0 <= y1 <= y0 + height
        return False


class Size2d(object):
    @classmethod
    def remapTo(cls, width, height, maximum):
        maxValue = max([width, height])
        if maxValue > maximum:
            if width > height:
                return maximum, maximum*(float(height)/float(width))
            elif width < height:
                return maximum*(float(width)/float(height)), maximum
        return width, height

    @classmethod
    def mapToRect(cls, size0, size1):
        w0, h0 = size0
        w1, h1 = size1
        if h0 > 0 and h1 > 0:
            pr0 = float(w0) / float(h0)
            pr1 = float(w1) / float(h1)
            smax1 = max(w1, h1)
            smin1 = min(w1, h1)
            if pr0 > 1:
                w, h = smin1, smin1 / pr0
            elif pr0 < 1:
                w, h = smin1, smin1 * pr0
            else:
                w, h = smin1, smin1
            x, y = (w1 - w) / 2, (h1 - h) / 2
            return x, y, w, h
        else:
            return 0, 0, w0, h0


class Ellipse2d(bscMtdCore.Mtd_BscUtility):
    @classmethod
    def positionAtAngle(cls, center, radius, angle):
        x, y = center
        xp = cls.MOD_math.sin(cls.MOD_math.radians(angle)) * radius / 2 + x + radius / 2
        yp = cls.MOD_math.cos(cls.MOD_math.radians(angle)) * radius / 2 + y + radius / 2
        return xp, yp


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


class Math2D(bscMtdCore.Mtd_BscUtility):
    @classmethod
    def getAngleByCoord(cls, x1, y1, x2, y2):
        radian = 0.0
        #
        r0 = 0.0
        r90 = cls.MOD_math.pi / 2.0
        r180 = cls.MOD_math.pi
        r270 = 3.0 * cls.MOD_math.pi / 2.0
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
            radian = cls.MOD_math.atan2((-x1 + x2), (-y1 + y2))
        elif x1 < x2 and y1 > y2:
            radian = r90 + cls.MOD_math.atan2((y1 - y2), (-x1 + x2))
        elif x1 > x2 and y1 > y2:
            radian = r180 + cls.MOD_math.atan2((x1 - x2), (y1 - y2))
        elif x1 > x2 and y1 < y2:
            radian = r270 + cls.MOD_math.atan2((-y1 + y2), (x1 - x2))
        #
        return radian * 180 / cls.MOD_math.pi

    @classmethod
    def getLengthByCoord(cls, x1, y1, x2, y2):
        return cls.MOD_math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


class Color(bscMtdCore.Mtd_BscUtility):
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
    def hsv2rgb(cls, h, s, v, maximum=255):
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


class UniqueId(bscMtdCore.Mtd_BscUtility):
    @classmethod
    def getByString(cls, string):
        return cls._stringToUniqueId(string)

    @classmethod
    def getByStrings(cls, *args):
        return cls._stringsToUniqueId(*args)

    @classmethod
    def new(cls):
        return cls._getUniqueId()

    @classmethod
    def isUsable(cls, string):
        boolean = False
        if string is not None:
            pattern = cls.MOD_re.compile(r'[0-9A-F]' * 8 + '-' + (r'[0-9A-F]' * 4 + '-') * 3 + r'[0-9A-F]' * 12)
            match = pattern.match(string)
            if match:
                boolean = True
        return boolean

    @classmethod
    def toList(cls, uniqueId):
        lis = []
        if isinstance(uniqueId, str) or isinstance(uniqueId, unicode):
            if cls.isUsable(uniqueId):
                lis = [uniqueId]
        elif isinstance(uniqueId, tuple) or isinstance(uniqueId, list):
            for i in uniqueId:
                if cls.isUsable(i):
                    lis.append(i)
        return lis


class IconKeyword(object):
    @staticmethod
    def mayaPng(nodeTypeString):
        return 'maya/out_{}'.format(nodeTypeString)

    @staticmethod
    def mayaSvg(nodeTypeString):
        return 'maya/{}'.format(nodeTypeString)
