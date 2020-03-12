# coding:utf-8
from LxMaBasic import maBscMtdCore


class Attribute(maBscMtdCore.Mtd_MaBasic):
    @classmethod
    def isAppExist(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsAppExist(attributeString)

    @classmethod
    def hasSource(cls, attributeString):
        if cls.isAppExist(attributeString):
            return maBscMtdCore.Mtd_MaAttribute._getAttributeHasSource(attributeString)
        return False

    @classmethod
    def isSource(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsSource(attributeString)

    @classmethod
    def source(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeSource(attributeString)

    @classmethod
    def hasTargets(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeHasTargets(attributeString)

    @classmethod
    def targets(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeTargetList(attributeString)

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
    def raw(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributePortdata(attributeString, asString=False)

    @classmethod
    def rawAsString(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributePortdata(attributeString, asString=True)

    @classmethod
    def arrayIndexes(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIndexes(attributeString)

    @classmethod
    def isCompound(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsCompound(attributeString)

    @classmethod
    def isMessage(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsMessage(attributeString)

    @classmethod
    def isColor(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsColor(attributeString)

    @classmethod
    def isFilename(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsFilename(attributeString)

    @classmethod
    def nicename(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeNicename(attributeString)

    @classmethod
    def defaultValue(cls, attributeString):
        pass

    @classmethod
    def parent(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeParentPortname(attributeString)

    @classmethod
    def hasChildren(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeHasChild(attributeString)

    @classmethod
    def children(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeChildPortnameList(attributeString)

    @classmethod
    def hasChannels(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeHasChannels(attributeString)

    @classmethod
    def channels(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeChannelnameList(attributeString)

    @classmethod
    def composeBy(cls, *args):
        return cls.DEF_mya_port_separator.join(list(args))
