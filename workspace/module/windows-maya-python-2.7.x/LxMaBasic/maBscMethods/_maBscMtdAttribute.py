# coding:utf-8
from LxMaBasic import maBscMtdCore


class Attribute(maBscMtdCore.Mtd_MaBasic):
    @classmethod
    def isAppExist(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsAppExist(attributeString)

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
    def raw(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributePortdata(attributeString, asString=False)

    @classmethod
    def rawAsString(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributePortdata(attributeString, asString=True)

    @classmethod
    def isArray(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeIsMultichannel(attributeString)

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

    @classmethod
    def _getPorttype_(cls, nodeString, portString, portDict):
        if maBscMtdCore.Mtd_MaAttribute._getAttributeIsNodeExist((nodeString, portString)):
            return maBscMtdCore.Mtd_MaAttribute._getAttributePorttype((nodeString, portString))
        else:
            if portString in portDict:
                _ = portDict[portString]
                if isinstance(_, (tuple, list)):
                    lis = []
                    count = len(_)
                    for i in _:
                        lis.append(
                            maBscMtdCore.Mtd_MaAttribute._getAttributePorttype((nodeString, i))
                        )
                    if lis == ['float']*count:
                        return 'floatArray'
                    elif lis == ['enum']*count:
                        return 'Int32Array'
                    return lis
                else:
                    return maBscMtdCore.Mtd_MaAttribute._getAttributePorttype((nodeString, _))

    @classmethod
    def _getPortdata_(cls, nodeString, portString, portDict):
        if portString in portDict:
            _ = portDict[portString]
            if isinstance(_, (tuple, list)):
                lis = []
                for i in _:
                    lis.append(
                        maBscMtdCore.Mtd_MaAttribute._getAttributePortdata((nodeString, i), asString=False)
                    )
                return lis
            else:
                return maBscMtdCore.Mtd_MaAttribute._getAttributePortdata((nodeString, _), asString=True)
        else:
            return maBscMtdCore.Mtd_MaAttribute._getAttributePortdata((nodeString, portString), asString=True)
