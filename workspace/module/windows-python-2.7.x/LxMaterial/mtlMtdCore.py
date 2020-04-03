# coding:utf-8
import functools

import collections

import MaterialX

from . import mtlConfigure


class Mtd_MtlBasic(mtlConfigure.Utility):
    MOD_materialx = MaterialX
    MOD_functools = functools
    CLS_ordered_dict = collections.OrderedDict


class Mtd_MtlFile(Mtd_MtlBasic):
    @classmethod
    def _getNodeDefDict(cls, fileString):
        dic = cls.CLS_ordered_dict()
        doc = cls.MOD_materialx.createDocument()
        # noinspection PyArgumentList
        cls.MOD_materialx.readFromXmlFile(doc, fileString)
        #
        for i in doc.getNodeDefs():
            nodeCategory = i.getNodeString()
            nodeType = i.getType()

            nodeDic = collections.OrderedDict()
            nodeDic[cls.DEF_mtl_key_type] = nodeType
            nodeAttrLis = []
            for input_ in i.getInputs():
                portpath = input_.getName()
                porttypeString = input_.getType()
                portdataString = input_.getValueString()
                attrDic = collections.OrderedDict()
                attrDic[cls.DEF_mtl_key_portpath] = portpath
                attrDic[cls.DEF_mtl_key_porttype] = porttypeString
                attrDic[cls.DEF_mtl_key_portdata] = portdataString
                attrDic[cls.DEF_mtl_key_assign] = cls.DEF_mtl_keyword_input
                nodeAttrLis.append(attrDic)

            nodeDic[cls.DEF_mtl_key_port] = nodeAttrLis
            dic[nodeCategory] = nodeDic
        return dic

