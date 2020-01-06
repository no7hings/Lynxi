# coding:utf-8
from LxBasic import bscConfigure, bscCore, bscObjects


class Mtd_Html(bscCore.Basic):
    color_html_lis = bscConfigure.Ui().htmlColors
    family_lis = bscConfigure.Ui().families
    @classmethod
    def toHtml(cls, string, inuse=5, fontSize=10, lineHeight=12):
        usedColor = cls.color_html_lis[inuse]
        #
        html = u'''
            <html>
                <style type="text/css">p{{line-height:{4}px}}</style>
                <span style="font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>
            </html>
        '''.format(string, fontSize, cls.family_lis[0], usedColor, lineHeight)
        return html
    
    @classmethod
    def getHtmls(cls, string, inuse=5, fontSize=10, lineHeight=12):
        usedColor = cls.color_html_lis[inuse]
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
        '''.format(s, fontSize, cls.family_lis[0], usedColor, lineHeight)
        return html
    
    @classmethod
    def toHtmlSpan(cls, string, inuse=5, fontSize=10):
        usedColor = cls.color_html_lis[inuse]
        #
        viewExplain = u'''
            <span style="font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>
        '''.format(string, fontSize, cls.family_lis[0], usedColor)
        return viewExplain
    
    @classmethod
    def toHtmlSpanTime(cls, inuse=7, fontSize=10):
        usedColor = cls.color_html_lis[inuse]
        #
        string = cls._getActiveViewTime()
        htmlString = u'''
            <span style="font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>
        '''.format(string, fontSize, cls.family_lis[0], usedColor)
        return htmlString
    
    @classmethod
    def toHtmlSpanSuper(cls, string, inuse=2, fontSize=10):
        usedColor = cls.color_html_lis[inuse]
        viewSuper = u'''
            <span style="vertical-align:super;font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>
        '''.format(string, fontSize, cls.family_lis[0], usedColor)
        return viewSuper
    
    @classmethod
    def toHtmlSpanSub(cls, string, inuse=2, fontSize=10):
        usedColor = cls.color_html_lis[inuse]
        viewSuper = u'''
            <span style="vertical-align:sub;font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>
        '''.format(string, fontSize, cls.family_lis[0], usedColor)
        return viewSuper
    
    @classmethod
    def toHtmlMayaConnection(cls, sourceAttr, targetAttr, namespaceFilter):
        def getBranch(attr):
            nodePath = bscObjects.Pth_Maya(attr)
            namespace = nodePath.namespace
            name = nodePath.name
            attrName = nodePath.attributeName
            #
            namespaceSep = nodePath.attributeSep
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
                    usedColor = colorIndexDic[seq]
                    #
                    html = u'''<span style="font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>'''.format(
                        s, fontSize, cls.family_lis[0], usedColor
                    )
                    htmls.append(html)
        #
        htmlSep = u'''<span style="font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>'''.format(u'>', fontSize, cls.family_lis[0], cls.color_html_lis[6]
        )
        #
        htmlString = u'''<html><style>p{{line-height:{1}px}}</style>{0}</html>'''.format(htmlSep.join(htmls), lineHeight)
        return htmlString
