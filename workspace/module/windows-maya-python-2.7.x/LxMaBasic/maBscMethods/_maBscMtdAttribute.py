# coding:utf-8
from LxMaBasic import myaBscMtdCore


class ObjectPort(myaBscMtdCore.Mtd_MaBasic):
    @classmethod
    def indexes(cls, nodepathString, portpathString):
        return myaBscMtdCore.Mtd_MaObjectPort._dcc_getObjectPortIndexes(nodepathString, portpathString)


class Attribute(myaBscMtdCore.Mtd_MaBasic):
    @classmethod
    def isAppExist(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeIsAppExist(attrpathString)

    @classmethod
    def hasSource(cls, attrpathString):
        if cls.isAppExist(attrpathString):
            return myaBscMtdCore.Mtd_MaAttribute._getAttributeHasSource(attrpathString)
        return False

    @classmethod
    def isSource(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeIsSource(attrpathString)

    @classmethod
    def source(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeSource(attrpathString)

    @classmethod
    def hasTargets(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeHasTargets(attrpathString)

    @classmethod
    def targets(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeTargetList(attrpathString)

    @classmethod
    def isTarget(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeIsTarget(attrpathString)

    @classmethod
    def nodepathString(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeNodeString(attrpathString)

    @classmethod
    def portpathString(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeFullpathPortname(attrpathString)

    @classmethod
    def porttype(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributePorttype(attrpathString)

    @classmethod
    def datatype(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeDatatype(attrpathString)

    @classmethod
    def name(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributePortname(attrpathString)

    @classmethod
    def raw(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributePortdata(attrpathString, asString=False)

    @classmethod
    def rawAsString(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributePortdata(attrpathString, asString=True)

    @classmethod
    def indexes(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeIndexes(attrpathString)

    @classmethod
    def isCompound(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeIsCompound(attrpathString)

    @classmethod
    def isMessage(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeIsMessage(attrpathString)

    @classmethod
    def isColor(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeIsColor(attrpathString)

    @classmethod
    def isFilename(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeIsFilename(attrpathString)

    @classmethod
    def nicename(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeNicename(attrpathString)

    @classmethod
    def defaultValue(cls, attrpathString):
        pass

    @classmethod
    def parent(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeParentPortname(attrpathString)

    @classmethod
    def hasChildren(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeHasChild(attrpathString)

    @classmethod
    def children(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeChildPortnameList(attrpathString)

    @classmethod
    def hasChannels(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeHasChannels(attrpathString)

    @classmethod
    def channels(cls, attrpathString):
        return myaBscMtdCore.Mtd_MaAttribute._getAttributeChannelnameList(attrpathString)

    @classmethod
    def composeBy(cls, *args):
        return cls.DEF_mya_port_separator.join(list(args))
