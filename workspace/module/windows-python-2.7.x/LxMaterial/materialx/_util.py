# coding:utf-8
from LxMaterial import mtlCore

import collections

import MaterialX as Mx


class loadVariant(object):
    def __init__(self, fileString):
        self._nodeDefDic = collections.OrderedDict()
        self._defFile = fileString
        self._getNodeDefs()

    def _getTypeDefs(self):
        pass

    def _getNodeDefs(self):
        doc = Mx.createDocument()
        # noinspection PyArgumentList
        Mx.readFromXmlFile(doc, self._defFile)
        #
        for i in doc.getNodeDefs():
            nodeCategory = i.getNodeString()
            nodeType = i.getType()

            nodeDic = collections.OrderedDict()
            nodeDic[mtlCore.Mtd_MtlBasic.Key_Type_String] = nodeType
            nodeAttrLis = []
            for j in i.getInputs():
                attrName = j.name()
                valueTypeString = j.getType()
                valueString = j.getValueString()
                attrDic = collections.OrderedDict()
                attrDic[mtlCore.Mtd_MtlBasic.Key_Name] = attrName
                attrDic[mtlCore.Mtd_MtlBasic.Key_Type_String] = valueTypeString
                attrDic[mtlCore.Mtd_MtlBasic.Key_Value_String] = valueString
                nodeAttrLis.append(attrDic)

            nodeDic[mtlCore.Mtd_MtlBasic.Key_Port] = nodeAttrLis
            self._nodeDefDic[nodeCategory] = nodeDic

    def nodeDefs(self):
        return self._nodeDefDic




