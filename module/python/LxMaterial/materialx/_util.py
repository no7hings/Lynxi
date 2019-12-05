# coding:utf-8
import collections

import MaterialX as Mx


#
class loadVariant(object):
    def __init__(self, fileString):
        self._nodeDefDic = collections.OrderedDict()
        self._defFile = fileString
        self._getNodeDef()

    def _getNodeDef(self):
        doc = Mx.createDocument()
        # noinspection PyArgumentList
        Mx.readFromXmlFile(doc, self._defFile)
        #
        for i in doc.getNodeDefs():
            nodeCategory = i.getNodeString()
            nodeType = i.getType()

            nodeDic = collections.OrderedDict()
            nodeDic['type'] = nodeType
            nodeAttrDic = collections.OrderedDict()
            for j in i.getInputs():
                attrName = j.getName()
                valueType = j.getType()
                valueString = j.getValueString()
                attrDic = collections.OrderedDict()
                attrDic['type'] = valueType
                attrDic['valueString'] = valueString
                nodeAttrDic[attrName] = attrDic

            nodeDic['attribute'] = nodeAttrDic
            self._nodeDefDic[nodeCategory] = nodeDic

    def nodeDefDic(self):
        return self._nodeDefDic




