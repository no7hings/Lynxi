# coding:utf-8
import functools

import collections

import MaterialX

from LxGraphic import grhCfg

from . import mtxCfg


class Mtd_MtxBasic(mtxCfg.MtxUtility):
    MOD_materialx = MaterialX
    MOD_functools = functools


class Mtd_MtxFile(Mtd_MtxBasic):
    @classmethod
    def _getNodeDefDict(cls, fileString):
        dic = cls.CLS_ordered_dict()
        doc = cls.MOD_materialx.createDocument()
        # noinspection PyArgumentList
        cls.MOD_materialx.readFromXmlFile(doc, fileString)
        #
        for i in doc.getNodeDefs():
            typepathString = i.getNodeString()
            datatypeStr = i.getType()

            nodeDic = collections.OrderedDict()
            nodeDic[grhCfg.GrhUtility.DEF_grh__key_node_datatype] = datatypeStr
            nodeAttrLis = []
            for input_ in i.getInputs():
                portpathStr = input_.getName()
                datatypeStr = input_.getType()
                portrawStr = input_.getValueString()
                attrDic = collections.OrderedDict()

                attrDic[grhCfg.GrhUtility.DEF_grh__key_portpath] = portpathStr
                attrDic[grhCfg.GrhUtility.DEF_grh__key_porttype] = datatypeStr
                attrDic[grhCfg.GrhUtility.DEF_grh__key_port_datatype] = datatypeStr
                attrDic[grhCfg.GrhUtility.DEF_grh__key_portraw] = portrawStr
                attrDic[grhCfg.GrhUtility.DEF_grh__key_assign] = grhCfg.GrhPortAssignQuery.inport
                nodeAttrLis.append(attrDic)

            nodeDic[grhCfg.GrhUtility.DEF_grh__key_port] = nodeAttrLis
            dic[typepathString] = nodeDic
        return dic

