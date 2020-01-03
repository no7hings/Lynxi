# coding=utf-8
from LxCore import lxBasic
#
from LxCore.config import appCfg
#
from LxUi import uiCore
#
_htmlColors = uiCore.Lynxi_Ui_Color_Html_Lis
#
_families = uiCore.Lynxi_Ui_Family_Lis


#
def getHtml(string, inuse=5, fontSize=10, lineHeight=12):
    usedColor = _htmlColors[inuse]
    #
    html = u'''
        <html>
            <style type="text/css">p{{line-height:{4}px}}</style>
            <span style="font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>
        </html>
    '''.format(string, fontSize, _families[0], usedColor, lineHeight)
    return html


#
def getHtmls(string, inuse=5, fontSize=10, lineHeight=12):
    usedColor = _htmlColors[inuse]
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
    '''.format(s, fontSize, _families[0], usedColor, lineHeight)
    return html


#
def getHtmlString(string, inuse=5, fontSize=10):
    usedColor = _htmlColors[inuse]
    #
    viewExplain = u'''
        <span style="font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>
    '''.format(string, fontSize, _families[0], usedColor)
    return viewExplain


#
def getHtmlTime(inuse=7, fontSize=10):
    usedColor = _htmlColors[inuse]
    #
    string = lxBasic.getOsActiveViewTime()
    htmlString = u'''
        <span style="font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>
    '''.format(string, fontSize, _families[0], usedColor)
    return htmlString


#
def getHtmlSuper(string, inuse=2, fontSize=10):
    usedColor = _htmlColors[inuse]
    viewSuper = u'''
        <span style="vertical-align:super;font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>
    '''.format(string, fontSize, _families[0], usedColor)
    return viewSuper


#
def getHtmlSub(string, inuse=2, fontSize=10):
    usedColor = _htmlColors[inuse]
    viewSuper = u'''
        <span style="vertical-align:sub;font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>
    '''.format(string, fontSize, _families[0], usedColor)
    return viewSuper


#
def getHtmlConnection(sourceAttr, targetAttr, namespaceFilter):
    def getBranch(attr):
        namespace = lxBasic.getStrPathNamespace(attr, objectSep, namespaceSep)
        name = lxBasic.getStrPathName(attr, objectSep, namespaceSep)
        attrName = lxBasic._toAttrString(attr, attributeSep)
        #
        if namespace:
            namespaceHtml = getHtmlString(namespace, 7, 10) + getHtmlString(namespaceSep, 3, 10)
        else:
            namespaceHtml = ''
        #
        if attr.startswith(namespaceFilter):
            html = namespaceHtml + getHtmlString(name[:-len(attrName)], 4, 10) + getHtmlString(attrName, 6, 10)
        else:
            html = namespaceHtml + getHtmlString(name[:-len(attrName)], 1, 10) + getHtmlString(attrName, 6, 10)
        #
        return html
    #
    objectSep = appCfg.Ma_Separator_Node
    namespaceSep = appCfg.Ma_Separator_Namespace
    attributeSep = appCfg.Ma_Separator_Attribute
    #
    sourceHtml = getBranch(sourceAttr)
    targetHtml = getBranch(targetAttr)
    #
    string = sourceHtml + getHtmlString('>>', 3, 10) + targetHtml
    return string


#
def getHtmlRenderImage(prefix, string, fontSize=8, lineHeight=10):
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
                    s, fontSize, _families[0], usedColor
                )
                htmls.append(html)
    #
    htmlSep = u'''<span style="font-family:'{2}';font-size:{1}pt;color:{3};">{0}</span>'''.format(
        u'>', fontSize, _families[0], _htmlColors[6]
    )
    #
    htmlString = u'''<html><style>p{{line-height:{1}px}}</style>{0}</html>'''.format(htmlSep.join(htmls), lineHeight)
    return htmlString
