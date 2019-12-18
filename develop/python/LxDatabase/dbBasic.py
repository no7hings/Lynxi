# coding=utf-8
import uuid
#
import hashlib
#
import struct
#
from LxCore import lxBasic
from LxUi.qt import qtProgress
#
from LxCore.preset import appVariant, databasePr
#
backupExtLabel = appVariant.dbHistoryUnitKey
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
_tempDirectory = appVariant.localTemporaryDirectory()
_defaultVariant = appVariant.astDefaultVariant
_defaultVersion = appVariant.astDefaultVersion
#
none = ''


# Get Upload Temp File
def getTemporaryOsFile(osFile):
    osFileBasename = lxBasic.getOsFileBasename(osFile)
    tempFile = lxBasic._toOsFile(_tempDirectory, osFileBasename)
    #
    lxBasic.setOsFilePathCreate(tempFile)
    return tempFile


#
def getDatabaseMainIndex(queryString):
    basicUniqueId = lxBasic.getBasicUniqueId()
    codeString = none
    if isinstance(queryString, str) or isinstance(queryString, unicode):
        codeString = str(queryString)
    if isinstance(queryString, list):
        codeString = str(none.join(queryString))
    #
    queryCode = none.join([str(ord(i) + seq).zfill(4) for seq, i in enumerate(codeString)])
    mainIndex = uuid.uuid3(uuid.UUID(basicUniqueId), str(queryCode))
    return str(mainIndex).upper()


#
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
    dic = lxBasic.orderedDict()
    dic[updateLabel] = lxBasic.getOsActiveTimestamp()
    dic[userLabel] = lxBasic.getOsUser()
    dic[hostNameLabel] = lxBasic.getOsHostName()
    dic[hostLabel] = lxBasic.getOsHost()
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
def writeMayaAsciiGzip(mayaAscii, osFile):
    data = lxBasic.readOsFileLines(mayaAscii)
    lxBasic.writeDataGzip(data, osFile)


#
def getData(data, hashValue, dbVersion):
    dic = lxBasic.orderedDict()
    dic[updateLabel] = lxBasic.getOsActiveTimestamp()
    dic[userLabel] = lxBasic.getOsUser()
    dic[hostNameLabel] = lxBasic.getOsHostName()
    dic[hostLabel] = lxBasic.getOsHost()
    dic[keyLabel] = hashValue
    dic[versionLabel] = dbVersion
    dic[DbKey_Data] = data
    return dic


#
def dbGetHashKey(dbFile):
    dbData = lxBasic.readJsonGzip(dbFile)
    if dbData:
        return dbData[keyLabel]


#
def dbDatumRead(dbFile):
    dbData = lxBasic.readJsonGzip(dbFile)
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
            lxBasic.writeJsonGzip(dbData, dbFile)
            lxBasic.setOsFileCopy(dbFile, dbBackupFile)


#
def dbCompDatumDicWrite(dic, dbIndex, directory, dbVersion):
    def getMain():
        lis = []
        # View Progress
        explain = '''Contrasting Data - Base'''
        maxValue = len(dic)
        progressBar = qtProgress.viewSubProgress(explain, maxValue)
        for compIndex, data in dic.items():
            progressBar.updateProgress()
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
            progressBar = qtProgress.viewSubProgress(explain, maxValue)
            for dbCompIndex, data, hashValue, dbFile, dbBackupFile in lis:
                progressBar.updateProgress()
                dbData = getData(data, hashValue, dbVersion)
                lxBasic.writeJsonGzip(dbData, dbFile)
                lxBasic.setOsFileCopy(dbFile, dbBackupFile)
    #
    if dic:
        writeMain(getMain())


#
def dbCompDatumRead(dbCompIndex, directory):
    dbFile = getDbFile(directory, dbCompIndex)
    data = dbDatumRead(dbFile)
    return data


@lxBasic.threadSemaphoreMethod
def readDbCompDataThreadMethod(dbIndex, directory):
    dbFile = getDbFile(directory, dbIndex)
    data = dbDatumRead(dbFile)
    return data


# Sub Method
def dbCompDatumDicRead(compIndexes, dbIndex, directory):
    dic = lxBasic.orderedDict()
    if compIndexes:
        if isinstance(compIndexes, list):
            splitCompIndexes = lxBasic._toListSplit(compIndexes, 250)
        elif isinstance(compIndexes, dict):
            splitCompIndexes = lxBasic._toListSplit(compIndexes.keys(), 250)
        else:
            splitCompIndexes = None
        #
        if splitCompIndexes:
            # View Progress
            explain = '''Read Datum(s)'''
            maxValue = len(compIndexes)
            progressBar = qtProgress.viewSubProgress(explain, maxValue)
            for subCompIndexes in splitCompIndexes:
                readThreadLis = []
                for compIndex in subCompIndexes:
                    dbCompIndex = getDatabaseCompIndex(dbIndex, compIndex)
                    t = lxBasic.dbThread(readDbCompDataThreadMethod, dbCompIndex, directory)
                    readThreadLis.append((compIndex, t))
                    t.start()
                #
                if readThreadLis:
                    for index, thread in readThreadLis:
                        progressBar.updateProgress()
                        thread.join()
                        data = thread.getData()
                        if data:
                            dic[index] = data
    return dic


#
def writeJsonGzipDic(osFile, dicKey, value):
    dic = lxBasic.orderedDict()
    #
    gzFile = osFile
    if lxBasic.isOsExistsFile(gzFile):
        dic = lxBasic.readJsonGzip(osFile)
    dic[dicKey] = value
    lxBasic.writeJsonGzip(dic, osFile)


#
def readJsonGzipDic(osFile, dicKey):
    string = none
    data = lxBasic.readJsonGzip(osFile)
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
    tempAsciiFile = getTemporaryOsFile(asciiFile) + mayaAsciiExtLabel
    cmds.file(rename=tempAsciiFile)
    cmds.file(save=1, type='mayaAscii')
    #
    lxBasic.setOsFileCopy(tempAsciiFile, asciiFile)


# noinspection PyUnresolvedReferences
def importDbMayaAscii(dbSubIndex, directory, namespace=':'):
    import maya.cmds as cmds
    asciiFile = directory + '/' + dbSubIndex
    if lxBasic.isOsExistsFile(asciiFile):
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


# noinspection PyUnresolvedReferences
def writeDbMayaAsciiData(dbSubIndex, directory):
    import maya.cmds as cmds
    #
    osFile = directory + '/' + dbSubIndex
    mayaAscii = getTemporaryOsFile(osFile) + mayaAsciiExtLabel
    cmds.file(rename=mayaAscii)
    cmds.file(save=1, type='mayaAscii')
    writeMayaAsciiGzip(mayaAscii, osFile)


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
    directory = databasePr.dbAstHistoryDirectory()
    return readDbHistory(dbIndex, directory, dicKey)


#
def readDbSceneryHistory(dbIndex, dicKey):
    directory = databasePr.dbScnHistoryDirectory()
    return readDbHistory(dbIndex, directory, dicKey)


#
def writeDbAssetHistory(dbIndex, sourceFile):
    directory = databasePr.dbAstHistoryDirectory()
    writeDbHistory(dbIndex, directory, appVariant.infoUpdaterLabel, lxBasic.getOsUser())
    writeDbHistory(dbIndex, directory, appVariant.infoUpdateLabel, lxBasic.getOsActiveTimestamp())
    writeDbHistory(dbIndex, directory, appVariant.infoSourceLabel, sourceFile)


#
def writeDbSceneryUnitHistory(dbIndex, sourceFile):
    directory = databasePr.dbScnHistoryDirectory()
    writeDbHistory(dbIndex, directory, appVariant.infoUpdaterLabel, lxBasic.getOsUser())
    writeDbHistory(dbIndex, directory, appVariant.infoUpdateLabel, lxBasic.getOsActiveTimestamp())
    writeDbHistory(dbIndex, directory, appVariant.infoSourceLabel, sourceFile)

