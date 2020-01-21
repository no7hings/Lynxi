# coding=utf-8
import uuid
#
import hashlib
#
import struct

from LxBasic import bscMethods, bscObjects, bscCommands

from LxPreset import prsVariants

from LxDatabase import dtbCore
#
backupExtLabel = prsVariants.Util.dbHistoryUnitKey
mayaAsciiExtLabel = '.ma'
#
keyLabel = 'key'
versionLabel = 'version'
#
updateLabel = 'update'
userLabel = 'user'
hostNameLabel = 'hostName'
hostLabel = 'host'
#
DbKey_Data = 'data'
#
lockLabel = 'lock'
modelLinkLabel = 'modelLink'
astModelProductFileLabel = 'modelAsset'
modelUpdaterLabel = 'modelUpdater'
modelStateLabel = 'modelState'
#
cfxLinkLabel = 'cfxLink'
astCfxProductFileLabel = 'cfxAsset'
cfxUpdaterLabel = 'cfxUpdater'
cfxStateLabel = 'cfxState'
#
rigLinkLabel = 'rigLink'
rigAssetLabel = 'rigAsset'
rigUpdaterLabel = 'rigUpdater'
rigStateLabel = 'rigState'
#
noneExistsLabel = 'Non - Exists'
#
_defaultVariant = prsVariants.Util.astDefaultVariant
_defaultVersion = prsVariants.Util.astDefaultVersion
#
none = ''


def getDatabaseSubIndex(dbIndex, queryString=none):
    if dbIndex:
        subDatabaseCode = dbIndex
        if queryString:
            codeString = none
            #
            if isinstance(queryString, str) or isinstance(queryString, unicode):
                codeString = str(queryString)
            #
            if isinstance(queryString, list):
                codeString = str(none.join(queryString))
            #
            subDatabaseCode = none.join([str(ord(i) + seq).zfill(4) for seq, i in enumerate(codeString)])
        subDatabaseIndex = uuid.uuid3(uuid.UUID(dbIndex), subDatabaseCode)
        databaseIndex = str(dbIndex) + '.var/' + str(subDatabaseIndex)
        return databaseIndex.upper()


#
def getDatabaseCompIndex(dbIndex, compIndex):
    databaseIndex = str(dbIndex) + '.comp/' + str(compIndex)
    return databaseIndex.upper()


#
def getPackFormat(maxValue):
    outType = 'q'
    if maxValue < 128:
        outType = 'b'
    elif maxValue < 32768:
        outType = 'h'
    elif maxValue < 4294967296:
        outType = 'i'
    return outType


# Get Data Hash Key
def getHashValue(data):
    strData = str(data)
    packArray = [ord(i) for i in strData]
    string = hashlib.md5(
        struct.pack('%s%s' % (len(packArray), getPackFormat(max(packArray))), *packArray)
    ).hexdigest()
    return string.upper()


#
def readDbData():
    pass


# Get Lock Data
def getDbInfo(hashValue, dbVersion):
    dic = bscCommands.orderedDict()
    dic[updateLabel] = bscMethods.OsTime.activeTimestamp()
    dic[userLabel] = bscMethods.OsSystem.username()
    dic[hostNameLabel] = bscMethods.OsSystem.hostname()
    dic[hostLabel] = bscMethods.OsSystem.host()
    dic[keyLabel] = hashValue
    dic[versionLabel] = dbVersion
    return dic


#
def getDbFile(directory, dbIndex):
    return directory + '/' + dbIndex


#
def getDbBackupFile(directory, dbIndex, dbVersion):
    return directory + backupExtLabel + '/' + dbIndex + '_' + dbVersion


#
def getData(data, hashValue, dbVersion):
    dic = bscCommands.orderedDict()
    dic[updateLabel] = bscMethods.OsTime.activeTimestamp()
    dic[userLabel] = bscMethods.OsSystem.username()
    dic[hostNameLabel] = bscMethods.OsSystem.hostname()
    dic[hostLabel] = bscMethods.OsSystem.host()
    dic[keyLabel] = hashValue
    dic[versionLabel] = dbVersion
    dic[DbKey_Data] = data
    return dic


#
def dbGetHashKey(dbFile):
    dbData = bscMethods.OsJsonGzip.read(dbFile)
    if dbData:
        return dbData[keyLabel]


#
def dbDatumRead(dbFile):
    dbData = bscMethods.OsJsonGzip.read(dbFile)
    if dbData:
        return dbData[DbKey_Data]


# Sub method
def dbCompDatumWrite(dbCompIndex, data, directory, dbVersion):
    if data is not None:
        hashValue = getHashValue(data)
        #
        dbFile = getDbFile(directory, dbCompIndex)
        dbBackupFile = getDbBackupFile(directory, dbCompIndex, dbVersion)
        #
        isUpdate = True
        # Check is Update
        serverKey = dbGetHashKey(dbFile)
        #
        if serverKey:
            if hashValue == serverKey:
                isUpdate = False
        #
        if isUpdate:
            dbData = getData(data, hashValue, dbVersion)

            bscMethods.OsJsonGzip.write(dbFile, dbData)
            bscMethods.OsFile.copyTo(dbFile, dbBackupFile)


#
def dbCompDatumDicWrite(dic, dbIndex, directory, dbVersion):
    def getMain():
        lis = []
        # View Progress
        explain = '''Contrasting Data - Base'''
        maxValue = len(dic)
        progressBar = bscObjects.If_Progress(explain, maxValue)
        for compIndex, data in dic.items():
            progressBar.update()
            dbCompIndex = getDatabaseCompIndex(dbIndex, compIndex)
            if data is not None:
                hashValue = getHashValue(data)
                #
                dbFile = getDbFile(directory, dbCompIndex)
                dbBackupFile = getDbBackupFile(directory, dbCompIndex, dbVersion)
                #
                isUpdate = True
                # Check is Update
                serverKey = dbGetHashKey(dbFile)
                #
                if serverKey:
                    if hashValue == serverKey:
                        isUpdate = False
                #
                if isUpdate:
                    lis.append((dbCompIndex, data, hashValue, dbFile, dbBackupFile))
        return lis
    #
    def writeMain(lis):
        if lis:
            # View Progress
            explain = '''Write Datum(s)'''
            maxValue = len(lis)
            progressBar = bscObjects.If_Progress(explain, maxValue)
            for dbCompIndex, data, hashValue, dbFile, dbBackupFile in lis:
                progressBar.update()
                dbData = getData(data, hashValue, dbVersion)
                bscMethods.OsJsonGzip.write(dbFile, dbData)
                bscMethods.OsFile.copyTo(dbFile, dbBackupFile)
    #
    if dic:
        writeMain(getMain())


#
def dbCompDatumRead(dbCompIndex, directory):
    dbFile = getDbFile(directory, dbCompIndex)
    data = dbDatumRead(dbFile)
    return data


@dtbCore.fncThreadSemaphoreModifier
def readDbCompDataThreadMethod(dbIndex, directory):
    dbFile = getDbFile(directory, dbIndex)
    data = dbDatumRead(dbFile)
    return data


# Sub Method
def dbCompDatumDicRead(compIndexes, dbIndex, directory):
    dic = bscCommands.orderedDict()
    if compIndexes:
        if isinstance(compIndexes, list):
            splitCompIndexes = bscMethods.List.splitTo(compIndexes, 250)
        elif isinstance(compIndexes, dict):
            splitCompIndexes = bscMethods.List.splitTo(compIndexes.keys(), 250)
        else:
            splitCompIndexes = None
        #
        if splitCompIndexes:
            # View Progress
            explain = '''Read Datum(s)'''
            maxValue = len(compIndexes)
            progressBar = bscObjects.If_Progress(explain, maxValue)
            for subCompIndexes in splitCompIndexes:
                readThreadLis = []
                for compIndex in subCompIndexes:
                    dbCompIndex = getDatabaseCompIndex(dbIndex, compIndex)
                    t = dtbCore.DtbThread(readDbCompDataThreadMethod, dbCompIndex, directory)
                    readThreadLis.append((compIndex, t))
                    t.start()
                #
                if readThreadLis:
                    for index, thread in readThreadLis:
                        progressBar.update()
                        thread.join()
                        data = thread.getData()
                        if data:
                            dic[index] = data
    return dic


#
def writeJsonGzipDic(osFile, dicKey, value):
    dic = bscCommands.orderedDict()
    #
    gzFile = osFile
    if bscCommands.isOsExistsFile(gzFile):
        dic = bscMethods.OsJsonGzip.read(osFile)
    dic[dicKey] = value
    bscMethods.OsJsonGzip.write(osFile, dic)


#
def readJsonGzipDic(osFile, dicKey):
    string = none
    data = bscMethods.OsJsonGzip.read(osFile)
    if data:
        if dicKey in data:
            value = data[dicKey]
            if value:
                string = value
    return string


# noinspection PyUnresolvedReferences
def saveDbMayaAscii(dbSubIndex, directory):
    import maya.cmds as cmds
    #
    asciiFile = directory + '/' + dbSubIndex
    #
    tempAsciiFile = bscMethods.OsFile.temporaryFilename(asciiFile) + mayaAsciiExtLabel
    cmds.file(rename=tempAsciiFile)
    cmds.file(save=1, type='mayaAscii')
    #
    bscMethods.OsFile.copyTo(tempAsciiFile, asciiFile)


# noinspection PyUnresolvedReferences
def importDbMayaAscii(dbSubIndex, directory, namespace=':'):
    import maya.cmds as cmds
    asciiFile = directory + '/' + dbSubIndex
    if bscCommands.isOsExistsFile(asciiFile):
        cmds.file(
            asciiFile,
            i=1,
            options='v=0;',
            type='mayaAscii',
            ra=1,
            mergeNamespacesOnClash=1,
            namespace=namespace,
            preserveReferences=1
        )


#
def writeDbHistory(dbIndex, directory, dicKey, value):
    if dbIndex:
        osFile = '%s/%s' % (directory, dbIndex)
        writeJsonGzipDic(osFile, dicKey, value)


#
def readDbHistory(dbIndex, directory, dicKey):
    string = none
    if dbIndex:
        osFile = '%s/%s' % (directory, dbIndex)
        value = readJsonGzipDic(osFile, dicKey)
        if value:
            string = value
    return string


#
def readDbAssetHistory(dbIndex, dicKey):
    directory = prsVariants.Database.assetHistory
    return readDbHistory(dbIndex, directory, dicKey)


#
def readDbSceneryHistory(dbIndex, dicKey):
    directory = prsVariants.Database.sceneryHistory
    return readDbHistory(dbIndex, directory, dicKey)


#
def writeDbAssetHistory(dbIndex, sourceFile):
    directory = prsVariants.Database.assetHistory
    writeDbHistory(dbIndex, directory, prsVariants.Util.infoUpdaterLabel, bscMethods.OsSystem.username())
    writeDbHistory(dbIndex, directory, prsVariants.Util.infoUpdateLabel, bscMethods.OsTime.activeTimestamp())
    writeDbHistory(dbIndex, directory, prsVariants.Util.infoSourceLabel, sourceFile)


#
def writeDbSceneryUnitHistory(dbIndex, sourceFile):
    directory = prsVariants.Database.sceneryHistory
    writeDbHistory(dbIndex, directory, prsVariants.Util.infoUpdaterLabel, bscMethods.OsSystem.username())
    writeDbHistory(dbIndex, directory, prsVariants.Util.infoUpdateLabel, bscMethods.OsTime.activeTimestamp())
    writeDbHistory(dbIndex, directory, prsVariants.Util.infoSourceLabel, sourceFile)

