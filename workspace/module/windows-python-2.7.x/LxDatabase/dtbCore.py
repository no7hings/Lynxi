# coding:utf-8
import threading

from LxBasic import bscCore, bscMethods

from LxDatabase import dtbConfigure

THREAD_MAX = threading.Semaphore(1024)


class DtbThread(threading.Thread):
    def __init__(self, *args):
        threading.Thread.__init__(self)
        # noinspection PyUnresolvedReferences
        self._fn = args[0]
        self._args = args[1:]
        #
        self._data = None
    #
    def setData(self, data):
        self._data = data
    #
    def data(self):
        return self._data
    #
    def run(self):
        self.setData(self._fn(*self._args))
    #
    def getData(self):
        return self._data


def fncThreadSemaphoreModifier(fn):
    def subMethod(*args, **kw):
        THREAD_MAX.acquire()
        method = fn(*args, **kw)
        THREAD_MAX.release()
        return method
    return subMethod


class DtbMtdBasic(dtbConfigure.DtbBasic):
    @classmethod
    def _lxDbInfoDic(cls, description=None, note=None):
        return bscCore.orderedDict(
            [
                (cls.DEF_key_info_timestamp, bscMethods.OsTimestamp.active()),
                (cls.DEF_key_info_username, bscMethods.OsSystem.username()),
                #
                (cls.DEF_key_info_host, bscMethods.OsSystem.host()),
                (cls.DEF_key_info_hostname, bscMethods.OsSystem.hostname()),
                #
                (cls.DEF_key_info_description, description),
                (cls.DEF_key_info_note, note)
            ]
        )

    @classmethod
    def _lxDbUnitDatumType(cls, dbUnitType):
        if dbUnitType in cls.LxDb_Datum_Type_Dic:
            return cls.LxDb_Datum_Type_Dic[dbUnitType]
        else:
            return cls.LxDb_Type_Datum_File

    @classmethod
    def _lxDbUnitIncludeIndex(cls, dbDatumType, dbDatumId):
        return str((dbDatumType, dbDatumId)).replace('"', "'")

    @classmethod
    def _lxDbOsUnitIncludeIndex(cls, dbDatumType, dbDatumId, osRelativeFile):
        return str((dbDatumType, dbDatumId, osRelativeFile)).replace('"', "'")

    @classmethod
    def _lxDbOsUnitDatumIndex(cls, dbDatumType, dbDatumId):
        return str((dbDatumType, dbDatumId)).replace('"', "'")

    @classmethod
    def _lxDbDirectory(cls):
        
        return bscMethods.OsPath.composeBy(
            [
                cls.DbRoot_Basic, cls.LxDb_Folder_Basic
            ]
        )

    @classmethod
    def _lxDbUnitDirectory(cls, dbClass):
        return bscMethods.OsPath.composeBy(
            [
                cls._lxDbDirectory(),
                dbClass + cls.LxDb_Folder_Unit
            ]
        )

    @classmethod
    def _lxDbDatumDirectory(cls, dbClass):
        return bscMethods.OsPath.composeBy(
            [
                cls._lxDbDirectory(),
                dbClass + cls.LxDb_Folder_Datum
            ]
        )

    @classmethod
    def _lxDbFileDirectory(cls, dbClass):
        return bscMethods.OsPath.composeBy(
            [
                cls._lxDbDirectory(),
                dbClass + cls.LxDb_Folder_File
            ]
        )

    @classmethod
    def _lxDbUnitIndexFile(cls, dbClass, dbUnitType):
        return bscMethods.OsPath.composeBy(
            [
                cls._lxDbUnitDirectory(dbClass),
                dbUnitType + cls.LxDb_Ext_Index,
            ]
        )

    # Unit Branch File
    @classmethod
    def _lxDbUnitBranchFile(cls, dbClass, dbUnitType, dbUnitId):
        return bscMethods.OsPath.composeBy(
            [
                cls._lxDbUnitDirectory(dbClass),
                dbUnitType, dbUnitId + cls.LxDb_Ext_Unit_Include_Branch
            ]
        )

    # Unit Definition File
    @classmethod
    def _lxDbUnitDefinitionFile(cls, dbClass, dbUnitType, dbUnitId):
        return bscMethods.OsPath.composeBy(
            [
                cls._lxDbUnitDirectory(dbClass),
                dbUnitType, dbUnitId + cls.LxDb_Ext_Unit_Include_Definition
            ]
        )

    @classmethod
    def _lxDbUnitIncludeFile(cls, dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId):
        return bscMethods.OsPath.composeBy(
            [
                cls._lxDbUnitDirectory(dbClass),
                dbUnitType, dbUnitBranch, dbUnitId + cls.LxDb_Ext_Unit_Include_Dic[dbUnitIncludeType]
            ]
        )

    # Unit Include Version File
    @classmethod
    def _lxDbUnitIncludeVersionFile(cls, dbUnitIncludeFile):
        base, ext = bscMethods.OsFile.toExtSplit(dbUnitIncludeFile)
        return base + cls.LxDb_Ext_Version

    @classmethod
    def _lxDbUnitIncludeInfoFile(cls, dbUnitIncludeFile):
        base, ext = bscMethods.OsFile.toExtSplit(dbUnitIncludeFile)
        return base + cls.LxDb_Ext_Unit_Include_Info

    # Json Datum File
    @classmethod
    def _lxDbJsonDatumFile(cls, dbClass, dbDatumType, dbDatumId):
        return bscMethods.OsPath.composeBy(
            [
                cls._lxDbDatumDirectory(dbClass),
                dbDatumType, dbDatumId + cls.LxDb_Ext_Json
            ]
        )

    @classmethod
    def _lxDbDatumInfoFile(cls, datumFile):
        base, ext = bscMethods.OsFile.toExtSplit(datumFile)
        return base + cls.LxDb_Ext_Info

    @classmethod
    def _lxDbOsUnitDatumFile(cls, dbClass, dbDatumType, dbDatumId, ext):
        return bscMethods.OsPath.composeBy(
            [
                cls._lxDbDatumDirectory(dbClass),
                dbDatumType, dbDatumId + ext
            ]
        )

    @classmethod
    def _lxDbOsDatumUnitVersionFile(cls, dbClass, dbDatumType, dbDatumUnitId):
        return bscMethods.OsPath.composeBy(
            [
                cls._lxDbFileDirectory(dbClass),
                dbDatumType, dbDatumUnitId + cls.LxDb_Ext_Version
            ]
        )

    @classmethod
    def _lxDbOsDatumUnitInfoFile(cls, dbClass, dbDatumType, dbDatumUnitId):
        return bscMethods.OsPath.composeBy(
            [
                cls._lxDbFileDirectory(dbClass),
                dbDatumType, dbDatumUnitId + cls.LxDb_Ext_Info
            ]
        )

    # Unit Index ( Update )
    @classmethod
    def _lxDbUpdateUnitIndexSub(cls, dbClass, dbUnitType, dbUnitId):
        dbUnitIndexFile = cls._lxDbUnitIndexFile(dbClass, dbUnitType)
        if bscMethods.OsFile.isExist(dbUnitIndexFile):
            dbUnitIdLis = bscMethods.OsJson.read(dbUnitIndexFile)
            if not dbUnitId in dbUnitIdLis:
                dbUnitIdLis += [dbUnitId]

                bscMethods.OsJson.write(dbUnitIndexFile, dbUnitIdLis)

                bscMethods.PyMessage.traceResult(
                    'Update Unit(s) Index File ( {} )'.format(dbUnitIndexFile)
                )
                bscMethods.PyMessage.traceResult(
                    'Add Unit ( {} > {} > {} )'.format(dbClass, dbUnitType, dbUnitId)
                )
        else:
            bscMethods.OsJson.write(dbUnitIndexFile, [dbUnitId])
            bscMethods.PyMessage.traceResult(
                'Add Unit(s) Index File ( {} )'.format(dbUnitIndexFile)
            )

    # Unit Branch ( Update )
    @classmethod
    def _lxDbUpdateUnitBranchFileSub(cls, dbClass, dbUnitType, dbUnitBranch, dbUnitId):
        # Branch
        if dbUnitBranch is None:
            dbUnitBranch = cls.LxDb_Include_Branch_Main
        #
        dbUnitBranchFile = cls._lxDbUnitBranchFile(
            dbClass,
            dbUnitType, dbUnitId
        )
        data = bscMethods.OsJson.read(dbUnitBranchFile)
        if data:
            if not dbUnitBranch in data:
                data.append(dbUnitBranch)
                bscMethods.OsJson.write(
                    dbUnitBranchFile, data
                )
                bscMethods.PyMessage.traceResult(
                    'Update Unit Branch File ( {} )'.format(dbUnitBranchFile)
                )
                bscMethods.PyMessage.traceResult(
                    'Add Unit ( {} > {} > {} ) Branch ( {} )'.format(dbClass, dbUnitType, dbUnitId, dbUnitBranch)
                )
        else:
            bscMethods.OsJson.write(
                dbUnitBranchFile, [dbUnitBranch]
            )
            bscMethods.PyMessage.traceResult(
                'Add Unit Branch File ( {} )'.format(dbUnitBranchFile)
            )

    # Unit Definition ( Update )
    @classmethod
    def _lxDbUpdateUnitDefinitionFileSub(cls, dbClass, dbUnitType, dbUnitId, dbDefinitionDatum):
        dbUnitDefinitionFile = cls._lxDbUnitDefinitionFile(
            dbClass,
            dbUnitType, dbUnitId
        )
        #
        bscMethods.OsJson.write(
            dbUnitDefinitionFile, dbDefinitionDatum
        )

    # Include File
    @classmethod
    def _lxDbUpdateUnitIncludeSub(cls, dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId, dbDatumType, dbDatumId, note=None):
        dbUnitIncludeIndex = cls._lxDbUnitIncludeIndex(dbDatumType, dbDatumId)
        # Include
        cls._lxDbUpdateUnitIncludeFileSub(
            dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId, dbUnitIncludeIndex, note
        )
        # Version
        cls._lxDbUpdateUnitIncludeVersionFileSub(
            dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId, dbUnitIncludeIndex, note
        )

    # Unit Include ( Update )
    # noinspection PyUnusedLocal
    @classmethod
    def _lxDbUpdateUnitIncludeFileSub(cls, dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId, dbUnitIncludeIndex, note=None):
        dbUnitIncludeFile = cls._lxDbUnitIncludeFile(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
        jsonDatum = bscMethods.OsJson.read(dbUnitIncludeFile)
        if jsonDatum:
            if not jsonDatum == dbUnitIncludeIndex:
                bscMethods.OsJson.write(
                    dbUnitIncludeFile, dbUnitIncludeIndex
                )
        else:
            bscMethods.OsJson.write(
                dbUnitIncludeFile, dbUnitIncludeIndex
            )

    # Unit Include Version ( Update )
    @classmethod
    def _lxDbUpdateUnitIncludeVersionFileSub(cls, dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId, dbUnitIncludeIndex, note=None):
        dbUnitIncludeFile = cls._lxDbUnitIncludeFile(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
        #
        dbIncludeInfo = cls._lxDbInfoDic(dbUnitBranch, note)
        #
        dbUnitIncludeVersionFile = cls._lxDbUnitIncludeVersionFile(dbUnitIncludeFile)
        dbUnitIncludeInfoFile = cls._lxDbUnitIncludeInfoFile(dbUnitIncludeFile)
        if bscMethods.OsFile.isExist(dbUnitIncludeVersionFile):
            dbUnitIncludeVersionLis = bscMethods.OsJson.read(dbUnitIncludeVersionFile)
            dbUnitIncludeInfoLis = bscMethods.OsJson.read(dbUnitIncludeInfoFile)
            if not dbUnitIncludeIndex in dbUnitIncludeVersionLis:
                dbUnitIncludeVersionLis.append(dbUnitIncludeIndex)
                dbUnitIncludeInfoLis.append(dbIncludeInfo)
                bscMethods.OsJson.write(dbUnitIncludeVersionFile, dbUnitIncludeVersionLis)
                bscMethods.OsJson.write(dbUnitIncludeInfoFile, dbUnitIncludeInfoLis)
        else:
            bscMethods.OsJson.write(dbUnitIncludeVersionFile, [dbUnitIncludeIndex])
            bscMethods.OsJson.write(dbUnitIncludeInfoFile, [dbIncludeInfo])

    # Unit Include Datum ( Update )
    @classmethod
    def _lxDbUpdateUnitIncludeDatumSub(cls, dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitIncludeDatum, dbUnitId, dbDatumType, note):
        dbDatumId = bscMethods.Raw.toHash(dbUnitIncludeDatum)
        # Branch
        if dbUnitBranch is None:
            dbUnitBranch = cls.LxDb_Include_Branch_Main
        # Include
        cls._lxDbUpdateUnitIncludeSub(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId,
            dbDatumType, dbDatumId
        )
        # Data
        cls._lxDbUpdateJsonFileDatumSub(
            dbClass,
            dbDatumType, dbDatumId, dbUnitIncludeDatum,
            dbUnitBranch,
            note
        )

    # Json Datum File
    @classmethod
    def _lxDbUpdateJsonFileDatumSub(cls, dbClass, dbDatumType, dbDatumId, datum, description, note):
        dbDatumFile = cls._lxDbJsonDatumFile(dbClass, dbDatumType, dbDatumId)
        if not bscMethods.OsFile.isExist(dbDatumFile):
            # Datum
            if dbDatumType == cls.LxDb_Type_Datum_Json:
                bscMethods.OsJson.write(dbDatumFile, datum)
            else:
                bscMethods.OsFile.write(dbDatumFile, datum)
            # Info
            dbDatumInfoFile = cls._lxDbDatumInfoFile(dbDatumFile)
            bscMethods.OsJson.write(dbDatumInfoFile, cls._lxDbInfoDic(description, note))
            #
            bscMethods.PyMessage.traceResult(
                'Add Os Datum File ( {} )'.format(dbDatumFile)
            )

    # Os Datum File
    @classmethod
    def _lxDbUpdateOsFileDatumSub(cls, fileString_, dbClass, dbDatumType, dbDatumUnitId, dbDatumId, description, note):
        ext = bscMethods.OsFile.ext(fileString_)
        #
        dbOsUnitDatumFile = cls._lxDbOsUnitDatumFile(dbClass, dbDatumType, dbDatumId, ext)
        if not bscMethods.OsFile.isExist(dbOsUnitDatumFile):
            # Datum File
            bscMethods.OsFile.copyTo(fileString_, dbOsUnitDatumFile)
            # Version and Info File
            dbOsDatumUnitVersionFile = cls._lxDbOsDatumUnitVersionFile(dbClass, dbDatumType, dbDatumUnitId)
            dbOsDatumUnitInfoFile = cls._lxDbOsDatumUnitInfoFile(dbClass, dbDatumType, dbDatumUnitId)
            #
            dbOsUnitIndex = cls._lxDbOsUnitDatumIndex(dbDatumType, dbDatumId)
            dbOsUnitInfo = cls._lxDbInfoDic(description, note)
            if bscMethods.OsFile.isExist(dbOsDatumUnitVersionFile):
                dbOsUnitVersionLis = bscMethods.OsJson.read(dbOsDatumUnitVersionFile)
                dbOsUnitInfoLis = bscMethods.OsJson.read(dbOsDatumUnitInfoFile)
                #
                dbOsUnitVersionLis.append(dbOsUnitIndex)
                dbOsUnitInfoLis.append(dbOsUnitInfo)
                #
                bscMethods.OsJson.write(dbOsDatumUnitVersionFile, dbOsUnitVersionLis)
                bscMethods.OsJson.write(dbOsDatumUnitInfoFile, dbOsUnitInfoLis)
            else:
                bscMethods.OsJson.write(dbOsDatumUnitVersionFile, [dbOsUnitIndex])
                bscMethods.OsJson.write(dbOsDatumUnitInfoFile, [dbOsUnitInfo])
            #
            bscMethods.PyMessage.traceResult(
                'Add Os Datum File ( {} > {} )'.format(fileString_, dbOsUnitDatumFile)
            )

    @classmethod
    def _lxDbOsUnitDefDatum(cls, enable, nameString, osPath):
        return {
            cls.LxDb_Key_Enable: enable,
            cls.LxDb_Key_Name: nameString,
            cls.LxDb_Key_Source: osPath
        }

    @classmethod
    def _lxDbOsFileUnitDefDatum(cls, fileString_):
        return {
            cls.LxDb_Key_Source: fileString_
        }

    @classmethod
    def _lxDbJsonUnitDefDatum(cls, enable, nameString):
        return {
            cls.LxDb_Key_Enable: enable,
            cls.LxDb_Key_Name: nameString
        }

    @classmethod
    def _lxDbLoadUnitIncludeSub(cls, dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId):
        if dbUnitBranch is None:
            dbUnitBranch = cls.LxDb_Include_Branch_Main
        #
        return cls._lxDbLoadUnitIncludeFileSub(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )

    @classmethod
    def _lxDbLoadUnitIncludeFileSub(cls, dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId):
        dbUnitIncludeFile = cls._lxDbUnitIncludeFile(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
        if bscMethods.OsFile.isExist(dbUnitIncludeFile):
            dbUnitIncludeIndex = bscMethods.OsJson.read(dbUnitIncludeFile)
            #
            dbDatumType, dbDatumId = eval(dbUnitIncludeIndex)
            return cls._lxDbLoadJsonDatumFileSub(
                dbClass,
                dbDatumType, dbDatumId
            )

    @classmethod
    def _lxDbLoadJsonDatumFileSub(cls, dbClass, dbDatumType, dbDatumId):
        dbDatumFile = cls._lxDbJsonDatumFile(dbClass, dbDatumType, dbDatumId)
        if bscMethods.OsFile.isExist(dbDatumFile):
            if dbDatumType == cls.LxDb_Type_Datum_Json:
                return bscMethods.OsJson.read(dbDatumFile)
            else:
                return bscMethods.OsFile.read(dbDatumFile)

    # Unit Index ( Get )
    @classmethod
    def _lxDbGetUnitIdLis(cls, dbClass, dbUnitType):
        dbUnitIndexFile = cls._lxDbUnitIndexFile(dbClass, dbUnitType)
        return bscMethods.OsJson.read(dbUnitIndexFile) or []

    @classmethod
    def _lxDbGetUnitDefinition(cls, dbClass, dbUnitType, dbUnitId):
        dbUnitDefinitionFile = cls._lxDbUnitDefinitionFile(
            dbClass,
            dbUnitType, dbUnitId
        )
        #
        return bscMethods.OsJson.read(dbUnitDefinitionFile) or {}

    # Unit Branch ( Get )
    @classmethod
    def _lxDbGetUnitBranchLis(cls, dbClass, dbUnitType, dbUnitId):
        dbUnitBranchFile = cls._lxDbUnitBranchFile(
            dbClass,
            dbUnitType, dbUnitId
        )
        if bscMethods.OsFile.isExist(dbUnitBranchFile):
            return bscMethods.OsJson.read(dbUnitBranchFile)
        else:
            return []

    # Unit Include Set ( Get )
    @classmethod
    def _lxDbGetUnitIncludeSet(cls, dbClass, dbUnitType, dbUnitId, dbUnitBranch=None):
        dbUnitIncludeType = cls.LxDb_Type_Unit_Include_Set
        if dbUnitBranch is None:
            dbUnitBranch = cls.LxDb_Include_Branch_Main
        #
        return cls._lxDbLoadUnitIncludeFileSub(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        ) or {}

    @classmethod
    def _lxDbGetUnitIncludeFileIndexLis(cls, dbClass, dbUnitType, dbUnitId, dbUnitBranch, dbUnitIncludeIndex):
        dbUnitIncludeType = cls.LxDb_Type_Unit_Include_File
        if dbUnitBranch is None:
            dbUnitBranch = cls.LxDb_Include_Branch_Main
        #
        if dbUnitIncludeIndex is None:
            return cls._lxDbLoadUnitIncludeFileSub(
                dbClass,
                dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
            ) or []
        else:
            dbDatumType, dbDatumId = eval(dbUnitIncludeIndex)
            return cls._lxDbLoadJsonDatumFileSub(
                dbClass,
                dbDatumType, dbDatumId
            )

    # Unit Include Version Lis ( Get )
    @classmethod
    def _lxDbGetUnitIncludeVersionLis(cls, dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId):
        lis = []
        currentIndex = 0
        #
        if dbUnitBranch is None:
            dbUnitBranch = cls.LxDb_Include_Branch_Main
        #
        dbUnitIncludeFile = cls._lxDbUnitIncludeFile(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
        if bscMethods.OsFile.isExist(dbUnitIncludeFile):
            currentData = bscMethods.OsJson.read(dbUnitIncludeFile)
            dbUnitIncludeVersionFile = cls._lxDbUnitIncludeVersionFile(dbUnitIncludeFile)
            data = bscMethods.OsJson.read(dbUnitIncludeVersionFile)
            if data:
                currentIndex = data.index(currentData)
                lis = data
        return lis, currentIndex

    @classmethod
    def _lxDbGetUnitIncludeVersionUiDic(cls, dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId):
        dic = bscCore.orderedDict()
        #
        if dbUnitBranch is None:
            dbUnitBranch = cls.LxDb_Include_Branch_Main
        #
        versionLis, currentIndex = cls._lxDbGetUnitIncludeVersionLis(
            dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
        if versionLis:
            for seq, i in enumerate(versionLis):
                dic[seq] = i, 'Version.{}'.format(seq)
        #
        return dic, currentIndex

    @classmethod
    def _lxDbGetUnitDic(cls, dbClass, dbUnitType):
        dic = bscCore.orderedDict()
        dbUnitIdLis = cls._lxDbGetUnitIdLis(dbClass, dbUnitType)
        if dbUnitIdLis:
            for dbUnitId in dbUnitIdLis:
                dbUnitDefinitionFile = cls._lxDbUnitDefinitionFile(
                    dbClass,
                    dbUnitType, dbUnitId
                )
                data = bscMethods.OsJson.read(dbUnitDefinitionFile)
                dic[dbUnitId] = data
        return dic

    @classmethod
    def _lxDbGetUnitNameLis(cls, dbClass, dbUnitType):
        lis = []
        dbUnitIdLis = cls._lxDbGetUnitIdLis(dbClass, dbUnitType)
        if dbUnitIdLis:
            for dbUnitId in dbUnitIdLis:
                dbUnitDefinitionFile = cls._lxDbUnitDefinitionFile(
                    dbClass,
                    dbUnitType, dbUnitId
                )
                data = bscMethods.OsJson.read(dbUnitDefinitionFile)
                if data:
                    name = data.get(cls.LxDb_Key_Name, 'N/a')
                    lis.append(name)
        return lis

    # Json Unit
    @classmethod
    def _lxDbUpdateJsonUnit(cls, nameString, jsonDatum, dbClass, dbUnitType, dbUnitBranch=None, note=None):

        dbUnitId = bscMethods.UniqueId.getByString(nameString)
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
        dbDefinitionDatum = cls._lxDbJsonUnitDefDatum(True, nameString)
        cls._lxDbUpdateUnitDefinitionFileSub(
            dbClass,
            dbUnitType, dbUnitId,
            dbDefinitionDatum
        )
        # Raw Include
        if jsonDatum:
            dbUnitIncludeType = cls.LxDb_Type_Unit_Include_Raw
            dbUnitRawIncludeDatum = jsonDatum
            dbDatumType = cls.LxDb_Type_Datum_Json
            cls._lxDbUpdateUnitIncludeDatumSub(
                dbClass,
                dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitRawIncludeDatum, dbUnitId,
                dbDatumType,
                note
            )

    @classmethod
    def _lxDbLoadJsonUnit(cls, nameString, dbClass, dbUnitType, dbUnitBranch=None):
        dbUnitId = bscMethods.UniqueId.getByString(nameString)
        dbUnitIncludeType = cls.LxDb_Type_Unit_Include_Raw
        #
        return cls._lxDbLoadUnitIncludeSub(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )

    @classmethod
    def _lxDbGetJsonUnitBranchLis(cls, nameString, dbClass, dbUnitType):
        dbUnitId = bscMethods.UniqueId.getByString(nameString)
        return cls._lxDbGetUnitBranchLis(
            dbClass,
            dbUnitType, dbUnitId
        )

    @classmethod
    def _lxDbGetJsonUnitIncludeVersionLis(cls, nameString, dbClass, dbUnitType, dbUnitBranch):
        dbUnitIncludeType = cls.LxDb_Type_Unit_Include_Raw
        dbUnitId = bscMethods.UniqueId.getByString(nameString)
        return cls._lxDbGetUnitIncludeVersionLis(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )

    @classmethod
    def _lxDbGetJsonUnitIncludeVersionUiDic(cls, nameString, dbClass, dbUnitType, dbUnitBranch):
        dbUnitIncludeType = cls.LxDb_Type_Unit_Include_Raw
        dbUnitId = bscMethods.UniqueId.getByString(nameString)
        return cls._lxDbGetUnitIncludeVersionUiDic(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )


class DtbMtdDataBasic(DtbMtdBasic):
    @classmethod
    def osUnitDatumFile(cls, dbClass, dbDatumType, dbDatumId, ext):
        return cls._lxDbOsUnitDatumFile(dbClass, dbDatumType, dbDatumId, ext)
