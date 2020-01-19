# coding:utf-8
from LxCore.config import appConfig

from LxCore.method.basic import _methodBasic


class Mtd_DbUnit(appConfig.LxDbConfig):
    plf_file_method = _methodBasic.Mtd_PlfFile
    database_method = _methodBasic.Mtd_Database
    
    @classmethod
    def dbUpdateOsUnit(cls, osPath, extFilter, dbClass, dbUnitType, dbUnitBranch=None, note=None):
        if cls.plf_file_method.isOsExist(osPath):
            dbUnitId = cls.database_method.getUniqueId(osPath.lower())
            # Index
            cls.database_method._lxDbUpdateUnitIndexSub(
                dbClass,
                dbUnitType, dbUnitId
            )
            if dbUnitBranch is None:
                dbUnitBranch = cls.database_method.LxDb_Include_Branch_Main
            # Branch
            cls.database_method._lxDbUpdateUnitBranchFileSub(
                dbClass,
                dbUnitType, dbUnitBranch, dbUnitId
            )
            # Definition
            dbDefinitionDatum = cls.database_method._lxDbOsFileUnitDefDatum(osPath)
            cls.database_method._lxDbUpdateUnitDefinitionFileSub(
                dbClass,
                dbUnitType, dbUnitId,
                dbDefinitionDatum
            )
            # Include File
            dbUnitIncludeType = cls.database_method.LxDb_Type_Unit_Include_File
            osRelativeFileLis = cls.plf_file_method.getOsFileLisFilter(osPath, extFilter, useRelative=True)
            dbDatumType = cls.database_method._lxDbUnitDatumType(dbUnitType)
            dbUnitIncludeDatum = []
            if osRelativeFileLis:
                osRelativeFileLis.sort()
                for osRelativeFile in osRelativeFileLis:
                    osFile = cls.plf_file_method.toOsFile(osPath, osRelativeFile)
                    dbDatumId = cls.plf_file_method.getOsFileHashString(osFile)
                    dbUnitIncludeIndex = cls.database_method._lxDbOsUnitIncludeIndex(dbDatumType, dbDatumId, osRelativeFile)
                    dbUnitIncludeDatum.append(dbUnitIncludeIndex)
                    #
                    dbDatumUnitId = cls.database_method.getUniqueId(osRelativeFile.lower())
                    #
                    cls.database_method._lxDbUpdateOsFileDatumSub(osFile, dbClass, dbDatumType, dbDatumUnitId, dbDatumId, dbUnitBranch, note)
            #
            dbDatumType = cls.database_method.LxDb_Type_Datum_Json
            #
            cls.database_method._lxDbUpdateUnitIncludeDatumSub(
                dbClass,
                dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitIncludeDatum, dbUnitId,
                dbDatumType,
                note
            )
    @classmethod
    def dbGetOsUnitIncludeFileVersionLis(cls, dbClass, dbUnitType, dbUnitBranch, dbUnitId):
        dbUnitIncludeType = cls.database_method.LxDb_Type_Unit_Include_File
        return cls.database_method._lxDbGetUnitIncludeVersionLis(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
    @classmethod
    def dbGetOsUnitIncludeFileIndexUiDic(cls, osPath, dbClass, dbUnitType, dbUnitBranch):
        dbUnitIncludeType = cls.database_method.LxDb_Type_Unit_Include_File
        dbUnitId = cls.database_method.getUniqueId(osPath.lower())
        return cls.database_method._lxDbGetUnitIncludeVersionUiDic(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
    @classmethod
    def _dbGetOsUnitIncludeFileIndexUiDic(cls, dbClass, dbUnitType, dbUnitBranch, dbUnitId):
        dbUnitIncludeType = cls.database_method.LxDb_Type_Unit_Include_File
        return cls.database_method._lxDbGetUnitIncludeVersionUiDic(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
    @classmethod
    def dbGetOsUnitIncludeFileIndexLis(cls, osPath, dbClass, dbUnitType, dbUnitBranch=None, dbUnitIncludeIndex=None):
        dbUnitId = cls.database_method.getUniqueId(osPath.lower())
        return cls.database_method._lxDbGetUnitIncludeFileIndexLis(
            dbClass,
            dbUnitType, dbUnitId, dbUnitBranch, dbUnitIncludeIndex
        )
    @classmethod
    def dbGetOsUnitIncludeFileDic(cls, dbClass, dbUnitType, dbUnitBranch=None):
        dic = cls.database_method.orderedDict()
        dbUnitIdLis = cls.database_method._lxDbGetUnitIdLis(dbClass, dbUnitType)
        if dbUnitIdLis:
            for dbUnitId in dbUnitIdLis:
                dbUnitDefinitionFile = cls.database_method._lxDbUnitDefinitionFile(dbClass, dbUnitType, dbUnitId)
                osPath = cls.plf_file_method.readOsJsonDic(dbUnitDefinitionFile, cls.database_method.LxDb_Key_Source)
                dic[osPath] = cls._dbGetOsUnitIncludeFileIndexUiDic(dbClass, dbUnitType, dbUnitBranch, dbUnitId)
        return dic


class Mtd_DbProdUnit(appConfig.LxDbConfig):
    database_method = _methodBasic.Mtd_Database

    @classmethod
    def dbUpdateProductUnit(cls, jsonDatum, dbUnitType, dbUnitId, dbUnitBranch=None, enable=True, description=None, note=None):
        dbClass = cls.database_method.LxDb_Class_Product
        # Index
        cls.database_method._lxDbUpdateUnitIndexSub(
            dbClass,
            dbUnitType, dbUnitId
        )
        # Branch
        cls.database_method._lxDbUpdateUnitBranchFileSub(
            dbClass,
            dbUnitType, dbUnitBranch, dbUnitId
        )
        # Definition
        dbDefinitionDatum = cls.database_method._lxDbJsonUnitDefDatum(enable, description)
        cls.database_method._lxDbUpdateUnitDefinitionFileSub(
            dbClass,
            dbUnitType, dbUnitId,
            dbDefinitionDatum
        )
        # Raw
        if jsonDatum:
            dbUnitIncludeType = cls.database_method.LxDb_Type_Unit_Include_Set
            dbUnitRawIncludeDatum = jsonDatum
            dbDatumType = cls.database_method.LxDb_Type_Datum_Json
            cls.database_method._lxDbUpdateUnitIncludeDatumSub(
                dbClass,
                dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitRawIncludeDatum, dbUnitId,
                dbDatumType,
                note
            )

    @classmethod
    def dbGetProductUnitIdLis(cls, dbUnitType):
        dbClass = cls.database_method.LxDb_Class_Product
        return cls.database_method._lxDbGetUnitIdLis(dbClass, dbUnitType)

    @classmethod
    def dbGetProductUnitCount(cls, dbUnitType):
        return len(cls.dbGetProductUnitIdLis(dbUnitType))

    @classmethod
    def dbGetProductUnitDefinition(cls, dbUnitType, dbUnitId):
        dbClass = cls.database_method.LxDb_Class_Product
        return cls.database_method._lxDbGetUnitDefinition(dbClass, dbUnitType, dbUnitId)

    @classmethod
    def dbGetProductUnitName(cls, dbUnitType, dbUnitId):
        dic = cls.dbGetProductUnitDefinition(dbUnitType, dbUnitId)
        return dic.get(cls.database_method.LxDb_Key_Name, None)

    @classmethod
    def dbGetProductUnitSet(cls, dbUnitType, dbUnitId, dbUnitBranch=None):
        dbClass = cls.database_method.LxDb_Class_Product
        return cls.database_method._lxDbGetUnitIncludeSet(dbClass, dbUnitType, dbUnitId, dbUnitBranch)

    @classmethod
    def dbGetProductUnitUiDic(cls):
        pass


class Mtd_DbUser(appConfig.LxDbConfig):
    database_method = _methodBasic.Mtd_Database
    
    @classmethod
    def dbWriteUserJsonUnit(cls, nameString, jsonDatum, dbUnitType, dbUnitBranch=None, note=None):
        cls.database_method._lxDbUpdateJsonUnit(
            nameString, jsonDatum,
            cls.database_method.LxDb_Class_User,
            dbUnitType, dbUnitBranch,
            note
        )
    @classmethod
    def dbReadUserJsonUnit(cls, nameString, dbUnitType, dbUnitBranch=None):
        return cls.database_method._lxDbLoadJsonUnit(
            nameString,
            cls.database_method.LxDb_Class_User,
            dbUnitType, dbUnitBranch
        )
    @classmethod
    def dbGetUserJsonUnitDic(cls, dbUnitType):
        return cls.database_method._lxDbGetUnitDic(
            cls.database_method.LxDb_Class_User,
            dbUnitType
        )
    @classmethod
    def dbGetUserJsonUnitNameLis(cls, dbUnitType):
        return cls.database_method._lxDbGetUnitNameLis(
            cls.database_method.LxDb_Class_User,
            dbUnitType
        )
    @classmethod
    def dbUserLocalUnitBranchLis(cls):
        return [
            cls.database_method.LxDb_Include_Branch_Main,
            cls.database_method.plf_file_method.getOsUser()
        ]
    @classmethod
    def dbGetUserServerJsonUnitBranchLis(cls, nameString, dbUnitType):
        return cls.database_method._lxDbGetJsonUnitBranchLis(
            nameString,
            cls.database_method.LxDb_Class_User,
            dbUnitType
        )
    @classmethod
    def dbGetUserServerJsonUnitIncludeVersionLis(cls, nameString, dbUnitType, dbUnitBranch):
        return cls.database_method._lxDbGetJsonUnitIncludeVersionLis(
            nameString,
            cls.database_method.LxDb_Class_User, dbUnitType,
            dbUnitBranch
        )
    @classmethod
    def dbGetUserServerJsonUnitIncludeVersionUiDic(cls, nameString, dbUnitType, dbUnitBranch):
        return cls.database_method._lxDbGetJsonUnitIncludeVersionUiDic(
            nameString,
            cls.database_method.LxDb_Class_User, dbUnitType,
            dbUnitBranch
        )
