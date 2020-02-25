# coding:utf-8
from LxBasic import bscMethods

from LxMaterial import mtlConfigure, mtlObjects

from LxMaBasic import maBscConfigure, maBscObjects

from LxMaMaterial import maMtlConfigure


class Mtd_MaMtlBasic(maMtlConfigure.Utility):
    pass


class Mtd_MaMtlTranslator(Mtd_MaMtlBasic):
    @classmethod
    def _setNodeCategoryCovert(cls, string):
        if string.startswith('ai'):
            return bscMethods.StrCamelcase.toUnderline(string[2:])
        return cls.DEF_category_node_covert_dict[string]

    @classmethod
    def _setNodeStringCovert(cls, nodeString):
        return nodeString.replace(
            maBscConfigure.Utility.DEF_mya_node_separator,
            mtlConfigure.Utility.DEF_mtl_node_separator
        )

    @classmethod
    def _setPortnameConvert(cls, portString):
        return bscMethods.StrCamelcase.toUnderline(portString)

    @classmethod
    def _setAttributeObjectConvert(cls, attributeString):
        pass

    @classmethod
    def _setNodeObjectConvert(cls, nodeString):
        nodeObject = maBscObjects.Node(nodeString)

        mtlCategory = cls._setNodeCategoryCovert(nodeObject.category())
        mtlNodeString = cls._setNodeStringCovert(nodeObject.fullpathName())

        mtlNodeObject = mtlObjects.Node(mtlCategory, mtlNodeString)
        for i in mtlNodeObject.attributes():
            j = i.portname().toCamelcaseString()
            if nodeObject.hasAttribute(j):
                attribute = nodeObject.attribute(j)
                print j, i.value(), attribute.raw()




