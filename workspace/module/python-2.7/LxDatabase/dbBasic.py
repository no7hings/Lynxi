# coding=utf-8
import uuid
#
import hashlib
#
import struct

from LxBasic import bscMtdCore, bscMethods, bscObjects

from LxPreset import prsOutputs

from LxDatabase import dtbMtdCore
#
backupExtLabel = prsOutputs.Util.dbHistoryUnitKey
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
_defaultVariant = prsOutputs.Util.astDefaultVariant
_defaultVersion = prsOutputs.Util.astDefaultVersion
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
    dic = bscMtdCore.orderedDict()
    dic[updateLabel] = bscMethods.OsTimestamp.active()
    dic[userLabel] = bscMethods.OsPlatform.username()
    dic[hostNameLabel] = bscMethods.OsPlatform.hostname()
    dic[hostLabel] = bscMethods.OsPlatform.host()
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
    dic = bscMtdCore.orderedDict()
    dic[updateLabel] = bscMethods.OsTimestamp.active()
    dic[userLabel] = bscMethods.OsPlatform.username()
    dic[hostNameLabel] = bscMethods.OsPlatform.hostname()
    dic[hostLabel] = bscMethods.OsPlatform.host()
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
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
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
            progressBar = bscObjects.ProgressWindow(explain, maxValue)
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


@dtbMtdCore.fncThreadSemaphoreModifier
def readDbCompDataThreadMethod(dbIndex, directory):
    dbFile = getDbFile(directory, dbIndex)
    data = dbDatumRead(dbFile)
    return data


# Sub Method
def dbCompDatumDicRead(compIndexes, dbIndex, directory):
    dic = bscMtdCore.orderedDict()
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
            progressBar = bscObjects.ProgressWindow(explain, maxValue)
            for subCompIndexes in splitCompIndexes:
                readThreadLis = []
                for compIndex in subCompIndexes:
                    dbCompIndex = getDatabaseCompIndex(dbIndex, compIndex)
                    t = dtbMtdCore.DtbThread(readDbCompDataThreadMethod, dbCompIndex, directory)
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
def writeJsonGzipDic(fileString_, dicKey, value):
    dic = bscMtdCore.orderedDict()
    #
    gzFile = fileString_
    if bscMethods.OsFile.isExist(gzFile):
        dic = bscMethods.OsJsonGzip.read(fileString_)
    dic[dicKey] = value
    bscMethods.OsJsonGzip.write(fileString_, dic)


#
def readJsonGzipDic(fileString_, dicKey):
    string = none
    data = bscMethods.OsJsonGzip.read(fileString_)
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
    tempAsciiFile = bscMethods.OsFile.temporaryName(asciiFile) + mayaAsciiExtLabel
    cmds.file(rename=tempAsciiFile)
    cmds.file(save=1, type='mayaAscii')
    #
    bscMethods.OsFile.copyTo(tempAsciiFile, asciiFile)


# noinspection PyUnresolvedReferences
def importDbMayaAscii(dbSubIndex, directory, namespace=':'):
    import maya.cmds as cmds
    asciiFile = directory + '/' + dbSubIndex
    if bscMethods.OsFile.isExist(asciiFile):
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
        fileString_ = '%s/%s' % (directory, dbIndex)
        writeJsonGzipDic(fileString_, dicKey, value)


#
def readDbHistory(dbIndex, directory, dicKey):
    string = none
    if dbIndex:
        fileString_ = '%s/%s' % (directory, dbIndex)
        value = readJsonGzipDic(fileString_, dicKey)
        if value:
            string = value
    return string


#
def readDbAssetHistory(dbIndex, dicKey):
    directory = prsOutputs.Database.assetHistory
    return readDbHistory(dbIndex, directory, dicKey)


#
def readDbSceneryHistory(dbIndex, dicKey):
    directory = prsOutputs.Database.sceneryHistory
    return readDbHistory(dbIndex, directory, dicKey)


#
def writeDbAssetHistory(dbIndex, sourceFile):
    directory = prsOutputs.Database.assetHistory
    writeDbHistory(dbIndex, directory, prsOutputs.Util.infoUpdaterLabel, bscMethods.OsPlatform.username())
    writeDbHistory(dbIndex, directory, prsOutputs.Util.infoUpdateLabel, bscMethods.OsTimestamp.active())
    writeDbHistory(dbIndex, directory, prsOutputs.Util.infoSourceLabel, sourceFile)


#
def writeDbSceneryUnitHistory(dbIndex, sourceFile):
    directory = prsOutputs.Database.sceneryHistory
    writeDbHistory(dbIndex, directory, prsOutputs.Util.infoUpdaterLabel, bscMethods.OsPlatform.username())
    writeDbHistory(dbIndex, directory, prsOutputs.Util.infoUpdateLabel, bscMethods.OsTimestamp.active())
    writeDbHistory(dbIndex, directory, prsOutputs.Util.infoSourceLabel, sourceFile)

