# coding:utf-8
from LxCore.method.basic import _methodBasic


#


#
class LxDbProductUnitMethod(_methodBasic.LxDbMethodBasic):
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


#
class DbOsUnitMethod(_methodBasic.LxDbMethodBasic):
    @classmethod
    def dbUpdateOsUnit(cls, osPath, extFilter, dbClass, dbUnitType, dbUnitBranch=None, note=None):
        if cls.isOsExist(osPath):
            dbUnitId = cls.getUniqueId(osPath.lower())
            # Index
            cls._lxDbUpdateUnitIndexSub(
                dbClass,
                dbUnitType, dbUnitId
            )
            if dbUnitBranch is None:
                dbUnitBranch = cls.LxDb_Include_Branch_Main
            # Branch
            cls._lxDbUpdateUnitBranchFileSub(
                dbClass,
                dbUnitType, dbUnitBranch, dbUnitId
            )
            # Definition
            dbDefinitionDatum = cls._lxDbOsFileUnitDefDatum(osPath)
            cls._lxDbUpdateUnitDefinitionFileSub(
                dbClass,
                dbUnitType, dbUnitId,
                dbDefinitionDatum
            )
            # Include File
            dbUnitIncludeType = cls.LxDb_Type_Unit_Include_File
            osRelativeFileLis = cls.getOsFileLisFilter(osPath, extFilter, useRelative=True)
            dbDatumType = cls._lxDbUnitDatumType(dbUnitType)
            dbUnitIncludeDatum = []
            if osRelativeFileLis:
                osRelativeFileLis.sort()
                for osRelativeFile in osRelativeFileLis:
                    osFile = cls._toOsFile(osPath, osRelativeFile)
                    dbDatumId = cls.getOsFileHashString(osFile)
                    dbUnitIncludeIndex = cls._lxDbOsUnitIncludeIndex(dbDatumType, dbDatumId, osRelativeFile)
                    dbUnitIncludeDatum.append(dbUnitIncludeIndex)
                    #
                    dbDatumUnitId = cls.getUniqueId(osRelativeFile.lower())
                    #
                    cls._lxDbUpdateOsFileDatumSub(osFile, dbClass, dbDatumType, dbDatumUnitId, dbDatumId, dbUnitBranch, note)
            #
            dbDatumType = cls.LxDb_Type_Datum_Json
            #
            cls._lxDbUpdateUnitIncludeDatumSub(
                dbClass,
                dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitIncludeDatum, dbUnitId,
                dbDatumType,
                note
            )
    @classmethod
    def dbGetOsUnitIncludeFileVersionLis(cls, dbClass, dbUnitType, dbUnitBranch, dbUnitId):
        dbUnitIncludeType = cls.LxDb_Type_Unit_Include_File
        return cls._lxDbGetUnitIncludeVersionLis(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
    @classmethod
    def dbGetOsUnitIncludeFileIndexUiDic(cls, osPath, dbClass, dbUnitType, dbUnitBranch):
        dbUnitIncludeType = cls.LxDb_Type_Unit_Include_File
        dbUnitId = cls.getUniqueId(osPath.lower())
        return cls._lxDbGetUnitIncludeVersionUiDic(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
    @classmethod
    def _dbGetOsUnitIncludeFileIndexUiDic(cls, dbClass, dbUnitType, dbUnitBranch, dbUnitId):
        dbUnitIncludeType = cls.LxDb_Type_Unit_Include_File
        return cls._lxDbGetUnitIncludeVersionUiDic(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
    @classmethod
    def dbGetOsUnitIncludeFileIndexLis(cls, osPath, dbClass, dbUnitType, dbUnitBranch=None, dbUnitIncludeIndex=None):
        dbUnitId = cls.getUniqueId(osPath.lower())
        return cls._lxDbGetUnitIncludeFileIndexLis(
            dbClass,
            dbUnitType, dbUnitId, dbUnitBranch, dbUnitIncludeIndex
        )
    @classmethod
    def dbGetOsUnitIncludeFileDic(cls, dbClass, dbUnitType, dbUnitBranch=None):
        dic = cls.orderedDict()
        dbUnitIdLis = cls._lxDbGetUnitIdLis(dbClass, dbUnitType)
        if dbUnitIdLis:
            for dbUnitId in dbUnitIdLis:
                dbUnitDefinitionFile = cls._lxDbUnitDefinitionFile(dbClass, dbUnitType, dbUnitId)
                osPath = cls.readOsJsonDic(dbUnitDefinitionFile, cls.LxDb_Key_Source)
                dic[osPath] = cls._dbGetOsUnitIncludeFileIndexUiDic(dbClass, dbUnitType, dbUnitBranch, dbUnitId)
        return dic


#
class DbUserMethod(_methodBasic.LxDbMethodBasic):
    @classmethod
    def dbWriteUserJsonUnit(cls, nameString, jsonDatum, dbUnitType, dbUnitBranch=None, note=None):
        cls._lxDbUpdateJsonUnit(
            nameString, jsonDatum,
            cls.LxDb_Class_User,
            dbUnitType, dbUnitBranch,
            note
        )
    @classmethod
    def dbReadUserJsonUnit(cls, nameString, dbUnitType, dbUnitBranch=None):
        return cls._lxDbLoadJsonUnit(
            nameString,
            cls.LxDb_Class_User,
            dbUnitType, dbUnitBranch
        )
    @classmethod
    def dbGetUserJsonUnitDic(cls, dbUnitType):
        return cls._lxDbGetUnitDic(
            cls.LxDb_Class_User,
            dbUnitType
        )
    @classmethod
    def dbGetUserJsonUnitNameLis(cls, dbUnitType):
        return cls._lxDbGetUnitNameLis(
            cls.LxDb_Class_User,
            dbUnitType
        )
    @classmethod
    def dbUserLocalUnitBranchLis(cls):
        return [
            cls.LxDb_Include_Branch_Main,
            cls.getOsUser()
        ]
    @classmethod
    def dbGetUserServerJsonUnitBranchLis(cls, nameString, dbUnitType):
        return cls._lxDbGetJsonUnitBranchLis(
            nameString,
            cls.LxDb_Class_User,
            dbUnitType
        )
    @classmethod
    def dbGetUserServerJsonUnitIncludeVersionLis(cls, nameString, dbUnitType, dbUnitBranch):
        return cls._lxDbGetJsonUnitIncludeVersionLis(
            nameString,
            cls.LxDb_Class_User, dbUnitType,
            dbUnitBranch
        )
    @classmethod
    def dbGetUserServerJsonUnitIncludeVersionUiDic(cls, nameString, dbUnitType, dbUnitBranch):
        return cls._lxDbGetJsonUnitIncludeVersionUiDic(
            nameString,
            cls.LxDb_Class_User, dbUnitType,
            dbUnitBranch
        )
