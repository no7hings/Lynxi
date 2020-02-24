# coding:utf-8
from LxMaBasic import maBscMtdCore


class Attribute(maBscMtdCore.Mtd_MaBasic):
    @classmethod
    def hasSource(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeHasSource(attributeString)

    @classmethod
    def isSource(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsSource(attributeString)

    @classmethod
    def source(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeSource(attributeString)

    @classmethod
    def hasTarget(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeHasTarget(attributeString)

    @classmethod
    def target(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeTarget(attributeString)

    @classmethod
    def isTarget(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsTarget(attributeString)

    @classmethod
    def nodeString(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeNodeString(attributeString)

    @classmethod
    def fullpathPortname(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeFullpathPortname(attributeString)

    @classmethod
    def porttype(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributePorttype(attributeString)

    @classmethod
    def datatype(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeDatatype(attributeString)

    @classmethod
    def name(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributePortname(attributeString)

    @classmethod
    def data(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeData(attributeString)

    @classmethod
    def isCompound(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsCompound(attributeString)

    @classmethod
    def isMultichannel(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsMultichannel(attributeString)

    @classmethod
    def isMessage(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsMessage(attributeString)

    @classmethod
    def value(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeData(attributeString)

    @classmethod
    def defaultValue(cls, attributeString):
        pass

    @classmethod
    def parent(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeParentFullpathPortname_(attributeString)

    @classmethod
    def hasChildren(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeHasChild(attributeString)

    @classmethod
    def children(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeChildFullpathPortnameList(attributeString)

    @classmethod
    def composeBy(cls, *args):
        return cls.DEF_mya_port_separator.join(list(args))
