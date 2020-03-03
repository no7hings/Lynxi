# coding:utf-8
import functools

import collections

import MaterialX

from LxBasic import bscMethods

from LxMaterial import mtlConfigure


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
            nodeDic[cls.DEF_mtl_key_datatype_string] = nodeType
            nodeAttrLis = []
            for input_ in i.getInputs():
                portname = input_.getName()
                valueTypeString = input_.getType()
                valueString = input_.getValueString()
                attrDic = collections.OrderedDict()
                attrDic[cls.DEF_mtl_key_port_string] = portname
                attrDic[cls.DEF_mtl_key_datatype_string] = valueTypeString
                attrDic[cls.DEF_mtl_key_value_string] = valueString
                nodeAttrLis.append(attrDic)

            nodeDic[cls.DEF_mtl_key_port] = nodeAttrLis
            dic[nodeCategory] = nodeDic
        return dic

