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
        return maBscMtdCore.Mtd_MaAttribute._getAttributeRaw(attributeString, asString=False)

    @classmethod
    def rawAsString(cls, attributeString):
        return maBscMtdCore.Mtd_MaAttribute._getAttributeRaw(attributeString, asString=True)

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
        def getFnc_(portname_):
            def recursionFnc__(portname__):
                if portname__ in portDict:
                    v__ = portDict[portname__]
                    if isinstance(v__, (tuple, list)):
                        for j in v__:
                            recursionFnc__(j)
                else:
                    lis_.append(
                        maBscMtdCore.Mtd_MaAttribute._getAttributePorttype((nodeString, portname__))
                    )

            lis_ = []
            recursionFnc__(portname_)
            return lis_

        if portString in portDict:
            _ = portDict[portString]
            if isinstance(_, (tuple, list)):
                return getFnc_(portString)
            else:
                return maBscMtdCore.Mtd_MaAttribute._getAttributePorttype((nodeString, _))

    @classmethod
    def _getPortdata_(cls, nodeString, portString, portDict):
        def getFnc_(portname_):
            def recursionFnc__(portname__):
                if portname__ in portDict:
                    v__ = portDict[portname__]
                    if isinstance(v__, (tuple, list)):
                        lis__ = [[]] * len(v__)
                        for index, j in enumerate(v__):
                            raw__ = recursionFnc__(j)
                            lis__[index] = raw__
                        return lis__
                else:
                    return maBscMtdCore.Mtd_MaAttribute._getAttributeRaw((nodeString, portname__), asString=False)

            return recursionFnc__(portname_)

        if portString in portDict:
            _ = portDict[portString]
            if isinstance(_, (tuple, list)):
                return getFnc_(portString)
            else:
                return maBscMtdCore.Mtd_MaAttribute._getAttributeRaw((nodeString, _), asString=True)
        else:
            return maBscMtdCore.Mtd_MaAttribute._getAttributeRaw((nodeString, portString), asString=True)
