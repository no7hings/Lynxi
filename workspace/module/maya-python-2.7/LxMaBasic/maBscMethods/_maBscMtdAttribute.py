# coding:utf-8
from .. import maBscMtdCore


class Attribute(maBscMtdCore.Mtd_MaBasic):
    @classmethod
    def isAppExist(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsAppExist(attrpathString)

    @classmethod
    def hasSource(cls, attrpathString):
        if cls.isAppExist(attrpathString):
            return maBscMtdCore.Mtd_MaAttribute._getAttributeHasSource(attrpathString)
        return False

    @classmethod
    def isSource(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsSource(attrpathString)

    @classmethod
    def source(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeSource(attrpathString)

    @classmethod
    def hasTargets(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeHasTargets(attrpathString)

    @classmethod
    def targets(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeTargetList(attrpathString)

    @classmethod
    def isTarget(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsTarget(attrpathString)

    @classmethod
    def nodepathString(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeNodeString(attrpathString)

    @classmethod
    def portpathString(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeFullpathPortname(attrpathString)

    @classmethod
    def porttype(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributePorttype(attrpathString)

    @classmethod
    def datatype(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeDatatype(attrpathString)

    @classmethod
    def name(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributePortname(attrpathString)

    @classmethod
    def raw(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributePortdata(attrpathString, asString=False)

    @classmethod
    def rawAsString(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributePortdata(attrpathString, asString=True)

    @classmethod
    def indexes(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIndexes(attrpathString)

    @classmethod
    def isCompound(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsCompound(attrpathString)

    @classmethod
    def isMessage(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsMessage(attrpathString)

    @classmethod
    def isColorport(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsColor(attrpathString)

    @classmethod
    def isFilename(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsFilename(attrpathString)

    @classmethod
    def nicename(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeNicename(attrpathString)

    @classmethod
    def defaultValue(cls, attrpathString):
        pass

    @classmethod
    def parent(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeParentPortname(attrpathString)

    @classmethod
    def hasChildren(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeHasChild(attrpathString)

    @classmethod
    def children(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeChildPortnameList(attrpathString)

    @classmethod
    def hasChannels(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeHasChannels(attrpathString)

    @classmethod
    def channels(cls, attrpathString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeChannelnameList(attrpathString)

    @classmethod
    def composeBy(cls, *args):
        return cls.DEF_mya_node_port_pathsep.join(list(args))
