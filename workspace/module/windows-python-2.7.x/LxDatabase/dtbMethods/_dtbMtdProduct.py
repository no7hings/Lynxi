# coding:utf-8
from LxBasic import bscMethods

from LxPreset import prsMethods

from LxDatabase import dtbMtdCore


class DtbProductUnit(dtbMtdCore.DtbMtdBasic):
    @classmethod
    def dbUpdateProductUnit(cls, jsonDatum, dbUnitType, dbUnitId, dbUnitBranch=None, enable=True, description=None, note=None):
        dbClass = cls.LxDb_Class_Product
        # Index
        cls._lxDbUpdateUnitIndexSub(
            dbClass,
            dbUnitType, dbUnitId
        )
        # Branch
        cls._lxDbUpdateUnitBranchFileSub(
            dbClass,
            dbUnitType, dbUnitBranch, dbUnitId
        )
        # Definition
        dbDefinitionDatum = cls._lxDbJsonUnitDefDatum(enable, description)
        cls._lxDbUpdateUnitDefinitionFileSub(
            dbClass,
            dbUnitType, dbUnitId,
            dbDefinitionDatum
        )
        # Raw
        if jsonDatum:
            dbUnitIncludeType = cls.LxDb_Type_Unit_Include_Set
            dbUnitRawIncludeDatum = jsonDatum
            dbDatumType = cls.LxDb_Type_Datum_Json
            cls._lxDbUpdateUnitIncludeDatumSub(
                dbClass,
                dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitRawIncludeDatum, dbUnitId,
                dbDatumType,
                note
            )

    @classmethod
    def dbGetProductUnitIdLis(cls, dbUnitType):
        dbClass = cls.LxDb_Class_Product
        return cls._lxDbGetUnitIdLis(dbClass, dbUnitType)

    @classmethod
    def dbGetProductUnitCount(cls, dbUnitType):
        return len(cls.dbGetProductUnitIdLis(dbUnitType))

    @classmethod
    def dbGetProductUnitDefinition(cls, dbUnitType, dbUnitId):
        dbClass = cls.LxDb_Class_Product
        return cls._lxDbGetUnitDefinition(dbClass, dbUnitType, dbUnitId)

    @classmethod
    def dbGetProductUnitName(cls, dbUnitType, dbUnitId):
        dic = cls.dbGetProductUnitDefinition(dbUnitType, dbUnitId)
        return dic.get(cls.LxDb_Key_Name, None)

    @classmethod
    def dbGetProductUnitSet(cls, dbUnitType, dbUnitId, dbUnitBranch=None):
        dbClass = cls.LxDb_Class_Product
        return cls._lxDbGetUnitIncludeSet(dbClass, dbUnitType, dbUnitId, dbUnitBranch)

    @classmethod
    def dbGetProductUnitUiDic(cls):
        pass

    @classmethod
    def getProductUnitViewName(cls, productModuleString, productUnitId):
        return cls.dbGetProductUnitName(productModuleString, productUnitId)

    @classmethod
    def getProductUnitViewInfo(cls, productModuleString, productUnitId):
        pass

    @classmethod
    def isDbProductUnitExists(cls, dbUnitId):

        fileString_ = cls._dbProductUnitSetFile(dbUnitId)
        return bscMethods.OsFile.isExist(fileString_)

    @classmethod
    def getDbProductUnitIndexDatumLis(cls, productModuleString):
        fileString_ = cls._dbProductUnitIndexFile(productModuleString)
        return bscMethods.OsJsonFile.read(fileString_)

    @classmethod
    def getDbProductUnitIndexLis(cls, productModuleString):
        data = cls.getDbProductUnitIndexDatumLis(productModuleString)
        if data:
            return zip(*data)[0]
        else:
            return []

    @classmethod
    def getDbProductUnitCount(cls, productModuleString):
        data = cls.getDbProductUnitIndexDatumLis(productModuleString)
        if data:
            return len(data)
        else:
            return 0

    @classmethod
    def getDbProductUnitSetDatum(cls, dbUnitId):
        fileString_ = cls._dbProductUnitSetFile(dbUnitId)
        return bscMethods.OsJsonFile.read(fileString_)

    @classmethod
    def getDbProductUnitSetUiDatum(cls, projectName, productModuleString, dbUnitId, number=0, overrideNumber=False):
        def getDefaultDatum():
            return prsMethods.Product.lxDbProductUnitDefaultSetConfig(projectName, productModuleString, number)

        #
        def getCustomDatum():
            fileString_ = cls._dbProductUnitSetFile(dbUnitId)
            return bscMethods.OsJsonFile.read(fileString_)

        #
        def getDatum(defaultLis, customDic):
            lis = []
            if defaultLis:
                for i in defaultLis:
                    key, uiValue = i
                    #
                    uiKey = None
                    if isinstance(key, str) or isinstance(key, unicode):
                        uiKey = bscMethods.StrCamelcase.toPrettify(key)
                    if isinstance(key, tuple):
                        key, uiKey = key
                    #
                    defValue = uiValue
                    value = uiValue
                    if isinstance(uiValue, list):
                        defValue = uiValue[0]
                        value = uiValue[0]
                    elif isinstance(uiValue, dict):
                        defValue = uiValue.values()[0][0]
                        value = uiValue.values()[0][0]
                    #
                    if customDic:
                        if key in customDic:
                            value = customDic[key]
                        else:
                            if key == 'name':
                                value = prsMethods.Product._toProductUnitName(number)
                        #
                        if overrideNumber is True:
                            if key == 'name':
                                value = prsMethods.Product._toProductUnitName(number)
                    lis.append(
                        (key, uiKey, value, defValue, uiValue)
                    )
            return lis

        #
        return getDatum(getDefaultDatum(), getCustomDatum())

    @classmethod
    def setDbProductUnitUpdate(cls, productModuleString, dbUnitId, unitIndexDatum, unitSetDatum):
        cls.setDbProductUnitIndexUpdate(productModuleString, unitIndexDatum)
        cls.setDbProductUnitSetUpdate(dbUnitId, unitSetDatum)

    @classmethod
    def setDbProductUnitIndexUpdate(cls, productModuleString, unitIndexDatum):
        indexFile = cls._dbProductUnitIndexFile(productModuleString)
        if bscMethods.OsFile.isExist(indexFile):
            data = bscMethods.OsJsonFile.read(indexFile)
            unitIndexLis = zip(*data)[0]
            dbUnitId = unitIndexDatum[0]
            if not dbUnitId in unitIndexLis:
                data += [unitIndexDatum]
                bscMethods.OsFile.backup(indexFile)
                bscMethods.OsJsonFile.write(indexFile, data)
            else:
                index = unitIndexLis.index(dbUnitId)
                serverUnitIndexDatum = data[index]
                if not unitIndexDatum == serverUnitIndexDatum:
                    data[index] = unitIndexDatum
                    bscMethods.OsFile.backup(indexFile)
                    bscMethods.OsJsonFile.write(indexFile, data)
        else:
            bscMethods.OsJsonFile.write(indexFile, [unitIndexDatum])

    @classmethod
    def setDbProductUnitSetUpdate(cls, dbUnitId, unitSetDatum):
        setFile = cls._dbProductUnitSetFile(dbUnitId)
        if bscMethods.OsFile.isExist(setFile):
            data = bscMethods.OsJsonFile.read(setFile)
            if not data == unitSetDatum:
                bscMethods.OsFile.backup(setFile)
                bscMethods.OsJsonFile.write(setFile, unitSetDatum)
        else:
            bscMethods.OsJsonFile.write(setFile, unitSetDatum)

    @classmethod
    def getDbProductUnitViewInfo(cls):
        pass
