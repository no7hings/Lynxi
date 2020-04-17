# coding:utf-8
import functools

import collections

import MaterialX

from LxGraphic import grhCfg

from . import mtlCfg


class Mtd_MtlBasic(mtlCfg.Utility):
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
            nodeDic[grhCfg.Utility.DEF_grh_key_type] = nodeType
            nodeAttrLis = []
            for input_ in i.getInputs():
                portpath = input_.getName()
                porttypeString = input_.getType()
                portrawString = input_.getValueString()
                attrDic = collections.OrderedDict()
                attrDic[grhCfg.Utility.DEF_grh_key_portpath] = portpath
                attrDic[grhCfg.Utility.DEF_grh_key_porttype] = porttypeString
                attrDic[grhCfg.Utility.DEF_grh_key_portraw] = portrawString
                attrDic[grhCfg.Utility.DEF_grh_key_assign] = grhCfg.Utility.DEF_grh_keyword_inparm
                nodeAttrLis.append(attrDic)

            nodeDic[grhCfg.Utility.DEF_grh_key_port] = nodeAttrLis
            dic[nodeCategory] = nodeDic
        return dic

