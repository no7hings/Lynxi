# coding:utf-8
from LxBasic import bscMtdCore, bscMethods

from LxDatabase import dtbMtdCore


class DtbData(dtbMtdCore.DtbMtdDataBasic):
    pass


class DtbUnit(dtbMtdCore.DtbMtdBasic):
    @classmethod
    def dbUpdateOsUnit(cls, osPath, extFilter, dbClass, dbUnitType, dbUnitBranch=None, note=None):
        if bscMethods.OsPath.isExist(osPath):
            dbUnitId = bscMethods.UniqueId.getByString(osPath.lower())
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

            osRelativeFileLis = bscMethods.OsDirectory.allFileRelativenames(osPath, extFilter)
            dbDatumType = cls._lxDbUnitDatumType(dbUnitType)
            dbUnitIncludeDatum = []
            if osRelativeFileLis:
                osRelativeFileLis.sort()
                for osRelativeFile in osRelativeFileLis:
                    fileString_ = bscMethods.OsPath.composeBy(osPath, osRelativeFile)
                    dbDatumId = bscMethods.OsFile.raw2hash(fileString_)
                    dbUnitIncludeIndex = cls._lxDbOsUnitIncludeIndex(dbDatumType, dbDatumId, osRelativeFile)
                    dbUnitIncludeDatum.append(dbUnitIncludeIndex)
                    #
                    dbDatumUnitId = bscMethods.UniqueId.getByString(osRelativeFile.lower())
                    #
                    cls._lxDbUpdateOsFileDatumSub(fileString_, dbClass, dbDatumType, dbDatumUnitId, dbDatumId, dbUnitBranch, note)
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
        dbUnitId = bscMethods.UniqueId.getByString(osPath.lower())
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
        dbUnitId = bscMethods.UniqueId.getByString(osPath.lower())
        return cls._lxDbGetUnitIncludeFileIndexLis(
            dbClass,
            dbUnitType, dbUnitId, dbUnitBranch, dbUnitIncludeIndex
        )

    @classmethod
    def dbGetOsUnitIncludeFileDic(cls, dbClass, dbUnitType, dbUnitBranch=None):
        dic = bscMtdCore.orderedDict()
        dbUnitIdLis = cls._lxDbGetUnitIdLis(dbClass, dbUnitType)
        if dbUnitIdLis:
            for dbUnitId in dbUnitIdLis:
                dbUnitDefinitionFile = cls._lxDbUnitDefinitionFile(dbClass, dbUnitType, dbUnitId)
                osPath = bscMethods.OsJsonFile.getValue(dbUnitDefinitionFile, cls.LxDb_Key_Source)
                dic[osPath] = cls._dbGetOsUnitIncludeFileIndexUiDic(dbClass, dbUnitType, dbUnitBranch, dbUnitId)
        return dic


class DtbUser(dtbMtdCore.DtbMtdBasic):
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
            bscMethods.OsPlatform.username()
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
