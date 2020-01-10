# coding:utf-8
from LxBasic import bscConfigure, bscCore

from LxBasic.bscMethods import _bscMtdDcc


class HtmlText(bscCore.Basic):
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


class List(object):
    @classmethod
    def getBadNumber(cls, lis, useMode=0):
        lis_ = []

        if lis:
            maxiNumber = max(lis)
            miniNumber = min(lis)
            if useMode == 1:
                miniNumber = 0
            for number in range(miniNumber, maxiNumber + 1):
                if not number in lis:
                    lis_.append(number)
        return lis_


class LabelText(bscCore.Basic):
    @classmethod
    def toLabel(cls, *labels):
        return labels[0] + ''.join([i.capitalize() for i in labels[1:]])


class Value(object):
    @classmethod
    def stepTo(cls, value, delta, step, maximum, minimum):
        max_ = maximum - step
        min_ = minimum + step
        if value < min_:
            if 0 < delta:
                value += step
            else:
                value = minimum
        elif min_ <= value <= max_:
            value += [-step, step][delta > 0]
        elif max_ < value:
            if delta < 0:
                value -= step
            else:
                value = maximum
        return value
