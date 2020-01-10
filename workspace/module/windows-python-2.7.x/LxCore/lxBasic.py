# coding:utf-8
import sys
#
import os
#
import platform
#
import math
#
import collections
#
import getpass
#
import socket
#
import time
#
import datetime
#
import traceback
#
import shutil
#
import uuid
#
import json
#
import gzip
#
import tarfile
#
import re
#
import threading
#
import hashlib
#
import glob
#
import subprocess
#
import locale
#
from LxBasic import bscObjects
#
Months = [
    (u'一月', 'January'),
    (u'二月', 'February'),
    (u'三月', 'March'),
    (u'四月', 'April'),
    (u'五月', 'May'),
    (u'六月', 'June'),
    (u'七月', 'July'),
    (u'八月', 'August'),
    (u'九月', 'September'),
    (u'十月', 'October'),
    (u'十一月', 'November'),
    (u'十二月', 'December')
]
Weeks = [
    (u'周一', 'Monday'),
    (u'周二', 'Tuesday'),
    (u'周三', 'Wednesday'),
    (u'周四', 'Thursday'),
    (u'周五', 'Friday'),
    (u'周六', 'Saturday'),
    (u'周天', 'Sunday'),
]
Dates = [
    (u'一', '1st'),
    (u'二', '2nd'),
    (u'三', '3rd'),
    (u'四', '4th'),
    (u'五', '5th'),
    (u'六', '6th'),
    (u'七', '7th'),
    (u'八', '8th'),
    (u'九', '9th'),
    (u'十', '10th'),
]
#
GzipExt = '.gz'
TarGZipExt = '.tar.gz'
UpdateExt = '.update'
InfoExt = '.info'
LogExt = '.log'
#
UpdateViewTimeFormat = '%Y - %m%d - [ %H:%M:%S ]'
MaUpdateViewTimeFormat = '%Y-%m-%d %H:%M:%S'
#
maxThread = threading.Semaphore(1024)
#
OsFilePathSep = '/'
Ma_Separator_Node = '|'
Ma_Separator_Namespace = ':'
#
none = ''


#
class runThread(threading.Thread):
    def __init__(self, *args):
        threading.Thread.__init__(self)
        self.fn = args[0]
        self.args = args[1:]
    #
    def run(self):
        self.fn(*self.args)


#
class dbThread(threading.Thread):
    def __init__(self, *args):
        threading.Thread.__init__(self)
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


#
def threadSemaphoreMethod(fn):
    def subMethod(*args, **kw):
        maxThread.acquire()
        method = fn(*args, **kw)
        maxThread.release()
        return method
    return subMethod


#
def _toListSplit(lis, splitCount):
    lis_ = []
    count = len(lis)
    cutCount = int(count / splitCount)
    for i in range(cutCount + 1):
        subLis = lis[i * splitCount:min((i + 1) * splitCount, count)]
        if subLis:
            lis_.append(subLis)
    return lis_


#
def getDicMethod(fn):
    def subMethod(*args):
        dic = fn(*args)
        if args:
            key = args[0]
            if key:
                return dic[key]
            else:
                return dic
        else:
            return dic
    return subMethod


#
def str_camelcase2prettify(string):
    return bscObjects.Str_Camelcase(string).toPrettify()


#
def int_frame2time(frame):
    return bscObjects.Int_Frame(frame).toTimeString()


def lis_frame2range(array):
    return bscObjects.Lis_Frame(array).toRange()


# Get List's Reduce
def getReduceList(sourceLis):
    lis = []
    [lis.append(i) for i in sourceLis if i not in lis]
    return lis


#
def readOsData(osFile, readLines=False):
    if os.path.isfile(osFile):
        # noinspection PyArgumentEqualDefault
        with open(osFile, 'r') as f:
            if readLines is False:
                data = f.read()
            else:
                data = f.readlines()
            f.close()
            return data


#
def _toStringList(data):
    lis = []
    if isinstance(data, str) or isinstance(data, unicode):
        lis = [data]
    elif isinstance(data, list) or isinstance(data, tuple):
        lis = list(data)
    return lis


#
def _basicUniqueId():
    return '4908BDB4-911F-3DCE-904E-96E4792E75F1'


#
def getUniqueId(string=none):
    basicUuid = _basicUniqueId()
    if string:
        return str(uuid.uuid3(uuid.UUID(basicUuid), str(string))).upper()
    elif not string:
        return str(uuid.uuid1()).upper()


#
def getUserUniqueId(user):
    basicUuid = _basicUniqueId()
    return str(uuid.uuid5(uuid.UUID(basicUuid), str(user))).upper()


#
def getDbUniqueId(directory):
    basicUuid = _basicUniqueId()
    return str(uuid.uuid5(uuid.UUID(basicUuid), str(directory))).upper()


#
def getSubUniqueId(strings):
    basicUuid = _basicUniqueId()
    #
    codeString = strings
    if isinstance(strings, str) or isinstance(strings, unicode):
        codeString = str(strings)
    elif isinstance(strings, tuple) or isinstance(strings, list):
        codeString = str(none.join(strings))
    #
    subCode = none.join([str(ord(i) + seq).zfill(4) for seq, i in enumerate(codeString)])
    subUuid = uuid.uuid3(uuid.UUID(basicUuid), subCode)
    return str(subUuid).upper()


#
def getDataHashString(data):
    string = none
    if data:
        data = str(data)
        md5Obj = hashlib.md5()
        md5Obj.update(data)
        hashValue = md5Obj.hexdigest()
        string = str(hashValue).upper()
    return string


#
def getDataUniqueId(data):
    return getSubUniqueId(getDataHashString(data))


#
def getOsFileHashKey_(osFile):
    string = none
    if os.path.isfile(osFile):
        with open(osFile, 'rb') as f:
            md5Obj = hashlib.md5()
            while True:
                d = f.read(8096)
                if not d:
                    break
                md5Obj.update(d)
            hashValue = md5Obj.hexdigest()
            f.close()
            string = str(hashValue).upper()
    return string


#
def getOsFileUniqueId(osFile):
    return getSubUniqueId(getOsFileHashKey_(osFile))


#
def getKeyEnabled(dic, key):
    boolean = False
    if key in dic:
        boolean = dic[key]
    return boolean


#
def getKeyData(dic, key):
    data = None
    if key in dic:
        data = dic[key]
    return data


#
def isOsPath(osPath):
    return os.path.isdir(osPath)


#
def isOsFile(osFile):
    return os.path.isfile(osFile)


#
def isOsExistsFile(osFile):
    if osFile:
        return os.path.isfile(osFile)
    else:
        return False


#
def getOsMultFileLis(osFile, useMode=0):
    lis = []
    def getSubFiles(keyword):
        osFiles = []
        subFiles = glob.glob(osFile.replace(keyword, '[0-9][0-9][0-9][0-9]'))
        if subFiles:
            # Use for Repath
            osFiles = [osFile]
            for subOsFile in subFiles:
                subOsFile = subOsFile.replace('\\', '/')
                osFiles.append(subOsFile)
        #
        return osFiles
    # Single File
    if isOsExistsFile(osFile):
        lis = [osFile]
    # Mult File
    else:
        if '<udim>' in osFile.lower():
            # Debug Yeti's UDIM
            osFile = osFile.replace('<UDIM>', '<udim>')
            lis = getSubFiles('<udim>')
        elif '%04d' in osFile.lower():
            lis = getSubFiles('%04d')
        elif '####' in osFile.lower():
            lis = getSubFiles('####')
        elif '<f>' in osFile.lower():
            lis = getSubFiles('<f>')
    #
    if useMode == 1:
        if lis:
            lis = [[lis[0]], lis[1:]][len(lis) > 1]
    #
    return lis


#
def getOsSeqFileNumber(osFile):
    number = -1
    osFileBasename = getOsFileBasename(osFile)
    findKeys = re.findall('[0-9][0-9][0-9][0-9]', osFileBasename)
    if findKeys:
        number = int(findKeys[0])
    return number


#
def getSeqFiles(osFile, startFrame, endFrame):
    lis = []
    for i in range(endFrame - startFrame + 1):
        subOsFile = osFile.replace('####', str(i + startFrame).zfill(4))
        lis.append(subOsFile)
    return lis


#
def getOsSeqFiles(osFile):
    lis = []
    globData = glob.glob(osFile.replace('####', '[0-9][0-9][0-9][0-9]'))
    if globData:
        for i in globData:
            subOsFile = i.replace('\\', '/')
            lis.append(subOsFile)
    return lis


#
def getOsSeqFileNumbers(osFile):
    lis = []
    osSeqFiles = getOsSeqFiles(osFile)
    if osSeqFiles:
        for subOsFile in osSeqFiles:
            number = getOsSeqFileNumber(subOsFile)
            lis.append(number)
    return lis


#
def getOsSeqFileSizes(osFile, startFrame, endFrame):
    lis = []
    osSeqFiles = getSeqFiles(osFile, startFrame, endFrame)
    if osSeqFiles:
        for subOsFile in osSeqFiles:
            # Check is File
            if isOsExistsFile(subOsFile):
                fileSize = getOsFileSize(subOsFile)
            else:
                fileSize = 0
            lis.append(fileSize)
    return lis


#
def isOsExist(osPath):
    if osPath:
        return os.path.exists(osPath)
    return False


#
def getOsFileMtimestamp(osFile):
    if isOsExistsFile(osFile):
        return os.stat(osFile).st_mtime


#
def getOsFileUpdateViewTime(osFile):
    string = none
    if os.path.isfile(osFile):
        timestamp = os.stat(osFile).st_mtime
        string = time.strftime(UpdateViewTimeFormat, time.localtime(timestamp))
    return string


#
def getViewTime(timestamp, timeFormat=UpdateViewTimeFormat):
    return time.strftime(timeFormat, time.localtime(timestamp))


#
def getOsFileDirname(osFile):
    return os.path.dirname(osFile)


#
def getOsFileBase(osFile):
    return os.path.splitext(osFile)[0]


#
def getOsFileExt(osFile):
    return os.path.splitext(osFile)[1]


#
def toOsFileSplitByExt(osFile):
    return os.path.splitext(osFile)


#
def getOsFileSplitFileNameData(osFile):
    osPath = getOsFileDirname(osFile)
    basename = getOsFileBasename(osFile)
    return osPath, basename


#
def getOsFileReplaceExt(osFile, osExt):
    return os.path.splitext(osFile)[0] + osExt


#
def toOsFileReplaceFileName(osFile, fileName):
    osPath = getOsFileDirname(osFile)
    osExt = getOsFileExt(osFile)
    newOsFile = u'{0}/{1}{2}'.format(osPath, fileName, osExt)
    return newOsFile


#
def getOsFileName(osFile):
    return os.path.splitext(os.path.basename(osFile))[0]


#
def getOsFileBasename(osFile):
    return os.path.basename(osFile)


#
def getOsFileBasenameLisByPath(osPath):
    lis = []
    if os.path.isdir(osPath):
        lis = os.listdir(osPath)
    return lis


#
def isOsAbsPath(osPath):
    return os.path.isabs(osPath)


#
def getOsFilesByPath(osPath):
    lis = []
    data = getOsFileBasenameLisByPath(osPath)
    if data:
        for osFileBasename in data:
            osFile = _toOsFile(osPath, osFileBasename)
            lis.append(osFile)
    return lis


#
def getOsFileSize(osFile):
    return int(os.path.getsize(osFile))


#
def _toOsFile(osPath, osFileBasename):
    return os.path.join(osPath, osFileBasename).replace('\\', '/')


#
def getOsFiles(osPath):
    lis = []
    for root, dirs, osFileBasenames in os.walk(osPath, topdown=0):
        for osFileBasename in osFileBasenames:
            osFile = _toOsFile(root, osFileBasename)
            lis.append(osFile)
    return lis


#
def getOsFilesFilter(filePath, filterExts, useRelative=False):
    # Sub Method
    def getBranch(osPath):
        osFiles = getOsFilesByPath(osPath)
        for i in osFiles:
            if isOsFile(i):
                ext = getOsFileExt(i)
                if ext.lower() in filterExts:
                    if useRelative:
                        i = i[len(filePath) + 1:]
                    lis.append(i)
            elif isOsPath(i):
                getBranch(i)
    #
    lis = []
    filterExts = _toStringList(filterExts)
    getBranch(filePath)
    if lis:
        lis.sort()
    return lis


#
def getOsUniqueFile(osFile):
    osPath = getOsFileDirname(osFile)
    osFileBasename = getOsFileBasename(osFile)
    basicUuid = _basicUniqueId()
    uniqueId = str(uuid.uuid3(uuid.UUID(basicUuid), str(osFileBasename))).upper()
    return _toOsFile(osPath, uniqueId)


#
def setOsFileDirectoryCreate(osFile):
    osPath = os.path.dirname(osFile)
    if not isOsExist(osPath):
        os.makedirs(osPath)


#
def createOsPath(osPath):
    try:
        os.makedirs(osPath)
    except WindowsError:
        return False


#
def hideOsFolder(osPath):
    if os.path.isdir(osPath):
        if 'Windows' in platform.system():
            command = 'attrib +h "' + osPath + '"'
            command = command.encode(locale.getdefaultlocale()[1])
            os.popen(command).close()


#
def setOsFileCopy(sourceOsFile, targetOsFile, force=True):
    if os.path.isfile(sourceOsFile):
        setOsFileDirectoryCreate(targetOsFile)
        # Check Same File
        if not os.path.normpath(sourceOsFile) == os.path.normpath(targetOsFile):
            if force is True:
                shutil.copy2(sourceOsFile, targetOsFile)
            elif force is False:
                try:
                    shutil.copy2(sourceOsFile, targetOsFile)
                except IOError:
                    print sourceOsFile, targetOsFile


#
def setOsFileMove(sourceOsFile, targetOsFile):
    if os.path.isfile(sourceOsFile):
        setOsFileDirectoryCreate(targetOsFile)
        shutil.move(sourceOsFile, targetOsFile)


#
def setOsFolderCopy(sourceOsPath, targetOsPath, progressModule=None):
    osFiles = getOsFiles(sourceOsPath)
    if osFiles:
        progressBar = None
        if progressModule:
            explain = '''Copy Os File'''
            maxValue = len(osFiles)
            progressBar = progressModule.setProgressWindowShow(explain, maxValue)
        for sourceOsFile in osFiles:
            if progressBar:
                progressBar.update()
            targetOsFile = targetOsPath + sourceOsFile[len(sourceOsPath):]
            setOsFileCopy(sourceOsFile, targetOsFile)


#
def moveOsFolder(sourceOsPath, targetOsPath):
    osFiles = getOsFiles(sourceOsPath)
    if osFiles:
        for sourceOsFile in osFiles:
            targetOsFile = targetOsPath + sourceOsFile[len(sourceOsPath):]
            setOsFileMove(sourceOsFile, targetOsFile)


#
def getOsSystemPathLis():
    return sys.path


#
def setSystemPathInsert(osPath):
    return sys.path.insert(0, osPath)


#
def getOsEnvironKeys():
    return os.environ.keys()


#
def getOsEnvironValue(osEnvironKey):
    return os.environ.get(osEnvironKey)


#
def getOsEnvironPathLis(osEnvironKey):
    lis = []
    environData = os.environ.get(osEnvironKey)
    if environData:
        splitStringLis = environData.split(os.pathsep)
        if splitStringLis:
            for i in splitStringLis:
                if i:
                    if i not in lis:
                        lis.append(i)
    return lis


#
def setOsCommandRun(command):
    return os.system(command)


#
def setOsCommandRun_(command):
    subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


#
def openOsFileByNotePad(osFile):
    if isOsExist(osFile):
        commandExe = 'C:/Windows/write.exe'
        command = '''"{}" "{}'''.format(commandExe, osFile)
        setOsCommandRun_(command)


#
def setOsEnvironValue(osEnvironKey, environData):
    os.environ[osEnvironKey] = environData


#
def setAddOsEnvironData(osEnvironKey, environData):
    os.environ[osEnvironKey] += '%s%s' % (os.pathsep, environData)


#
def orderedDict(*args):
    return collections.OrderedDict(*args)


#
def getOsUser():
    return getpass.getuser()


#
def getOsHostName():
    hostName = socket.getfqdn(socket.gethostname())
    return hostName


#
def getOsHost():
    host = socket.gethostbyname(socket.gethostname())
    return host


#
def getAppName():
    return os.path.basename(sys.argv[0])


#
def isMayaApp():
    boolean = False
    data = os.path.basename(sys.argv[0])
    if data.lower() == 'maya.exe':
        boolean = True
    elif data.lower() == 'maya':
        boolean = True
    return boolean


#
def getOsDocumentPath():
    return getOsEnvironValue('userprofile').replace('\\', '/') + '/Documents'


#
def getMayaAppOsDocPath(mayaVersion=None):
    basicFolder = getOsDocumentPath() + '/maya'
    # Custom Version
    if mayaVersion is None or mayaVersion == 'Unspecified':
        mayaVersion = getMayaAppVersion()
    #
    mayaFolderName = mayaVersion
    if int(mayaVersion) < 2016:
        mayaFolderName = mayaVersion + 'x64'
    #
    osPath = _toOsFile(basicFolder, mayaFolderName)
    return osPath


#
def getMayaAppsEnvFile(mayaVersion=None):
    mayaEnvFile = getMayaAppOsDocPath(mayaVersion) + '/Maya.env'
    return mayaEnvFile


#
def getMayaAppOsModPath(mayaVersion=None):
    mayaDocPath = getMayaAppOsDocPath(mayaVersion)
    osPath = mayaDocPath + '/modules'
    return osPath


# noinspection PyUnresolvedReferences
def getMayaAppVersion():
    string = none
    if isMayaApp():
        # noinspection PyUnresolvedReferences
        import maya.cmds as cmds
        # Str <Maya Version>
        string = str(cmds.about(apiVersion=1))[:4]
    return string


# noinspection PyUnresolvedReferences
def getMayaAppFullVersion():
    string = none
    if isMayaApp():
        # noinspection PyUnresolvedReferences
        import maya.cmds as cmds
        # Str <Maya Version>
        string = str(cmds.about(apiVersion=1))
    return string


# 00.0, 00.0, 00.0
def getFloatColor(inR, inG, inB):
    outR = round(float(inR) / float(255), 3)
    outG = round(float(inG) / float(255), 3)
    outB = round(float(inB) / float(255), 3)
    return outR, outG, outB


#
def getCnViewDate():
    currentTime = time.localtime(time.time())
    year, month, date, hour, minute, second, week, dayCount, isDst = currentTime
    #
    dateString = u'{0}年{1}月{2}日'.format(str(year).zfill(4), str(month).zfill(2), str(date).zfill(2))
    #
    timeString = u'{0}点{1}分'.format(str(hour).zfill(2), str(minute).zfill(2))
    #
    string = u'{0} {1}'.format(dateString, timeString)
    return string


#
def getOsActiveTimestamp():
    return time.time()


#
def getOsActiveViewTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


#
def getUpdateViewTime():
    return time.strftime(UpdateViewTimeFormat, time.localtime(time.time()))


#
def getOsActiveDateTag():
    return time.strftime('%Y_%m%d', time.localtime(time.time()))


#
def getOsActiveTimeTag():
    return time.strftime('%Y_%m%d_%H%M', time.localtime(time.time()))


#
def getOsFileTimeTag(osFile):
    if osFile:
        stringLis = re.findall('[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]', osFile)
        if stringLis:
            return stringLis[-1]


#
def getOsMultFileTimeTag(osFile):
    if osFile:
        stringLis = re.findall('[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]', osFile)
        if stringLis:
            return stringLis[-1]


#
def getOsFileJoinTimeTag(osFile, timeTag=none, useMode=0):
    if not timeTag:
        timeTag = getOsActiveTimeTag()
    string = osFile
    if useMode == 0:
        string = ('_%s' % timeTag).join(os.path.splitext(osFile))
    elif useMode == 1:
        string = getOsFileDirname(osFile) + '/' + timeTag + '/' + getOsFileBasename(osFile)
    return string


# Get File's Update Label
def getOsFileMtimeTag(osFile):
    if isOsExistsFile(osFile):
        timestamp = getOsFileMtimestamp(osFile)
        return datetime.datetime.fromtimestamp(timestamp).strftime('%Y_%m%d_%H%M%S')


#
def getOsFileBackupDatum(osFile, useMode=0):
    string = osFile
    timeTag = getOsFileMtimeTag(osFile)
    if useMode == 0:
        string = '%s.%s' % (osFile, timeTag)
    elif useMode == 1:
        string = getOsFileDirname(osFile) + '/' + timeTag + '/' + getOsFileBasename(osFile)
    return string


#
def getSubLabel(seq):
    subLabel = [none, '_' + str(seq).zfill(4)][seq > 0]
    return subLabel


#
def getOsSubFile(osFile, label):
    return label.join(os.path.splitext(osFile))


#
def toExceptionString():
    return traceback.format_exc()


# Get Upload Temp File
def getOsTempFolder(osFile):
    tempDirectory = 'D:/.lynxi.temporary/' + getOsActiveDateTag()
    osFileBasename = getOsFileBasename(osFile)
    tempFile = _toOsFile(tempDirectory, osFileBasename)
    #
    setOsFileDirectoryCreate(tempFile)
    return tempFile


# Get Upload Temp File
def getOsTemporaryFile(osFile, timeTag=None):
    if not timeTag:
        timeTag = getOsActiveTimeTag()
    tempDirectory = 'D:/.lynxi.temporary/' + timeTag
    osFileBasename = getOsFileBasename(osFile)
    tempFile = _toOsFile(tempDirectory, osFileBasename)
    #
    setOsFileDirectoryCreate(tempFile)
    return tempFile


#
def getOsTempVedioFile(osFile):
    tempDirectory = 'D:/.lynxi.temporary/vedio'
    osFileBasename = getOsFileBasename(osFile)
    tempFile = _toOsFile(tempDirectory, osFileBasename)
    return tempFile


#
def getDbBasename(dbFile):
    return '/'.join(dbFile.split('/')[-2:])


#
def getDbTempFile(dbFile):
    tempDirectory = 'D:/.lynxi.temporary/' + getOsActiveTimeTag()
    osFileBasename = getDbBasename(dbFile)
    tempFile = _toOsFile(tempDirectory, osFileBasename)
    #
    setOsFileDirectoryCreate(tempFile)
    return tempFile


#
def readOsJson(osFile, encoding=None):
    if os.path.isfile(osFile):
        with open(osFile) as j:
            data = json.load(j, encoding=encoding)
            return data


#
def readJsonGzip(osFile):
    if isOsExistsFile(osFile):
        with gzip.GzipFile(mode='rb', fileobj=open(osFile, 'rb')) as g:
            data = json.load(g)
            #
            g.close()
            return data


#
def readJsonTarGzip(osFile):
    osTarGzFile = osFile + ''
    if isOsExistsFile(osTarGzFile) and tarfile.is_tarfile(osTarGzFile):
        with tarfile.open(osTarGzFile, mode='r:gz') as t:
            for tarinfo in t:
                osFileBasename = tarinfo.name
                j = gzip.GzipFile(filename=osFileBasename, mode='rb', fileobj=open(osTarGzFile, 'rb'))
                data = j.readlines()
            #
            t.close()


#
def writeOsJson(data, osFile, indent=4, ensure_ascii=True):
    if data is not None:
        tempFile = getOsTemporaryFile(osFile)
        #
        with open(tempFile, 'w') as j:
            json.dump(data, j, ensure_ascii=ensure_ascii, indent=indent)
        #
        setOsFileCopy(tempFile, osFile)


#
def writeOsJsonDic(dataDic, osFile, indent=4):
    dic = orderedDict()
    #
    gzFile = osFile
    if isOsExistsFile(gzFile):
        dic = readOsJson(osFile)
    for k, v in dataDic.items():
        dic[k] = v
    #
    writeOsJson(dic, osFile, indent)


# Write Json and Compress
def writeJsonGzip(data, osFile, indent=4):
    if data:
        tempFile = getOsTemporaryFile(osFile)
        #
        osFileBasename = getOsFileBasename(osFile)
        with gzip.GzipFile(filename=osFileBasename, mode='wb', compresslevel=9, fileobj=open(tempFile, 'wb')) as g:
            json.dump(data, g, ensure_ascii=True, indent=indent)
            #
            g.close()
        #
        setOsFileCopy(tempFile, osFile)


#
def writeJsonTarGzip(datas, osFile):
    if datas:
        utilsTemporaryFolder = getOsTempFolder(osFile)
        osTarGzFile = osFile + TarGZipExt
        packDatas = []
        with tarfile.open(osTarGzFile, "w:gz") as t:
            #
            for i in datas:
                subOsFileBasename, data = i
                subOsFile = _toOsFile(utilsTemporaryFolder, subOsFileBasename)
                setOsFileDirectoryCreate(subOsFile)
                packDatas.append((subOsFile, subOsFileBasename))
                j = open(subOsFile, 'w')
                json.dump(data, j, ensure_ascii=True)
            #
            for packData in packDatas:
                subOsFile, subOsFileBasename = packData
                t.add(subOsFile, arcname=subOsFileBasename)
            #
            t.close()


#
def readDataGzip(osFile):
    if isOsExistsFile(osFile):
        with gzip.GzipFile(mode='rb', fileobj=open(osFile, 'rb')) as g:
            data = g.read()
            g.close()
            return data


#
def writeDataGzip(data, osFile):
    setOsFileDirectoryCreate(osFile)
    #
    osFileBasename = getOsFileBasename(osFile)
    #
    with gzip.GzipFile(filename=osFileBasename, mode='wb', compresslevel=9, fileobj=open(osFile, 'wb')) as g:
        g.write(data)
        g.close()


#
def copyOsFileToGzip(sourceOsFile, targetOsFile):
    setOsFileDirectoryCreate(targetOsFile)
    osFileBasename = getOsFileBasename(targetOsFile)
    #
    with open(sourceOsFile, 'rb') as f:
        data = f.read()
        f.close()
        with gzip.GzipFile(filename=osFileBasename, mode='wb', compresslevel=9, fileobj=open(targetOsFile, 'wb')) as g:
            g.write(data)
            g.close()


#
def getUiStringPath(strings, pathsep, isUseNiceName=False):
    string = none
    if isinstance(strings, str) or isinstance(strings, unicode):
        if isUseNiceName is True:
            strings = str_camelcase2prettify(strings)
        string = strings
    elif isinstance(strings, list) or isinstance(strings, tuple):
        if isUseNiceName is True:
            strings = [str_camelcase2prettify(i) for i in strings]
        string = pathsep.join(strings)
    return string


#
def getStringPathItems(stringPath, pathsep):
    return stringPath.split(pathsep)


#
def getPathArray(stringPath, pathsep):
    # List [ <Path> ]
    lis = []
    #
    splitData = stringPath.split(pathsep)
    #
    dataCount = len(splitData)
    for seq, data in enumerate(splitData):
        if data:
            if seq + 1 < dataCount:
                subPath = pathsep.join(splitData[:seq + 1])
                lis.append(subPath)
    #
    lis.append(stringPath)
    return lis


#
def getPathsArray(stringPaths, pathsep):
    # List [ <Path> ]
    lis = []
    for stringPath in stringPaths:
        pathArray = getPathArray(stringPath, pathsep)
        for subPath in pathArray:
            if not subPath in lis:
                lis.append(subPath)
    return lis


#
def getPathReduce(stringPath, pathsep):
    return re.sub('{0}|{1}'.format(pathsep*2, pathsep*3), pathsep, stringPath)


#
def _toVariantConvert(varName, string):
    def getStringLis():
        # noinspection RegExpSingleCharAlternation
        return [i for i in re.split("<|>", string) if i]
    #
    def getVariantLis():
        varPattern = re.compile(r'[<](.*?)[>]', re.S)
        return re.findall(varPattern, string)
    #
    def getVarStringLis():
        lis = []
        for i in strings:
            if i in variants:
                lis.append(i)
            else:
                v = '''"%s"''' % i
                lis.append(v)
        return lis
    #
    strings = getStringLis()
    variants = getVariantLis()
    #
    varStrings = getVarStringLis()
    #
    command = '''{0} = '{1}' % ({2})'''.format(varName, '%s'*len(strings), ', '.join(varStrings))
    return command


#
def getNumberByString(string):
    varPattern = re.compile(r'[[](.*?)[]]', re.S)
    return re.findall(varPattern, string)


#
def embeddedNumberLis(string):
    re_digits = re.compile(r'(\d+)')
    pieces = re_digits.split(unicode(string))
    pieces[1::2] = map(int, pieces[1::2])
    return pieces


#
def getMayaPathDic(dic):
    def getBranch(parent):
        if parent in dic:
            parentPath = parent
            if parent in pathDic:
                parentPath = pathDic[parent]
            #
            children = dic[parent]
            if children:
                for child in children:
                    childPath = parentPath + pathsep + child
                    pathDic[child] = childPath
                    getBranch(child)
    pathsep = '|'
    #
    pathDic = orderedDict()
    root = dic.keys()[0]
    pathDic[root] = root
    getBranch(root)
    return pathDic


#
def getDateData(dateString):
    return [i for i in datetime.datetime.strptime(dateString, "%Y-%m-%d").timetuple()]


#
def getTodayData():
    return getDateData(datetime.date.today().strftime("%Y-%m-%d"))


#
def getDateDatas(startDateString, endDateString):
    lis = []
    date = datetime.datetime.strptime(startDateString, "%Y-%m-%d")
    endDate = datetime.datetime.strptime(endDateString, "%Y-%m-%d")
    while date <= endDate:
        dateString = date.strftime("%Y-%m-%d")
        lis.append(getDateData(dateString))
        #
        date += datetime.timedelta(days=1)
    return lis


# Get Md5 Key
def getHashKey(data):
    if isinstance(data, str) or isinstance(data, unicode):
        packData = str(data)
        return hashlib.md5(packData).hexdigest()
    elif isinstance(data, tuple) or isinstance(data, list):
        packData = []
        for i in data:
            packData.append(str(i))
        return hashlib.md5(none.join(packData)).hexdigest()


# Get Scene Key
def getSceneKey(sceneIndex):
    user = getOsUser()
    host = getOsHost()
    return getHashKey([sceneIndex, user, host])


#
def setListExtendSubList(lis, subLis):
    [lis.append(i) for i in subLis if i not in lis]


# Get Update File
def getRecordFile(osFile):
    base = os.path.splitext(osFile)[0]
    return base + UpdateExt


# Get Info File
def getInfoFile(osFile):
    base = os.path.splitext(osFile)[0]
    return base + InfoExt


# Get Log File
def getLogFile(osFile):
    base = os.path.splitext(osFile)[0]
    return base + LogExt


# Get File's History
def getOsFileRecordDic(osFile):
    # Dict { <Update>:
    #        <File> }
    dic = orderedDict()
    if osFile:
        path = os.path.dirname(osFile)
        if os.path.exists(path):
            osFile = getPathReduce(osFile, '/')
            base, ext = os.path.splitext(osFile)
            osFiles = glob.glob(base + '_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]' + ext)
            if osFiles:
                for osFile in osFiles:
                    update = osFile[len(base) + 1:-len(ext)]
                    dic[update] = osFile.replace('\\', '/')
    return dic


#
def getOsFileByKeyVars(keyVars):
    return '/'.join([i for i in keyVars if i != none and i is not None])


#
def getLimitValue(value, maximum, minimum):
    if value >= maximum:
        return maximum
    elif value <= minimum:
        return minimum
    else:
        return value


#
def getStrPathName(pathString, pathSep, namespaceSep):
    string = pathString.split(pathSep)[-1].split(namespaceSep)[-1]
    return string


#
def getStrPathNamespace(pathString, pathSep, namespaceSep):
    if namespaceSep in pathString:
        string = namespaceSep.join(pathString.split(pathSep)[-1].split(namespaceSep)[:-1])
    else:
        string = none
    return string


#
def _toAttrString(attrString, attributeSep):
    attrName = attributeSep.join(attrString.split(attributeSep)[1:])
    return attrName


#
def getMayaObjectName(objectPath):
    return getStrPathName(objectPath, Ma_Separator_Node, Ma_Separator_Namespace)


#
def getPathJoinNamespace(pathString, namespace, pathSep, namespaceSep):
    isFullPath = pathString.startswith(pathSep)
    if isFullPath:
        return (pathSep + namespace + namespaceSep).join(pathString.split(pathSep))
    else:
        return namespace + namespaceSep + (pathSep + namespace + namespaceSep).join(pathString.split(pathSep))


#
def getMayaObjectPathJoinNamespace(objectPath, namespace):
    return getPathJoinNamespace(objectPath, namespace, Ma_Separator_Node, Ma_Separator_Namespace)


#
def getShowNumber(number, useMode=0):
    showNumber = number
    #
    dv = 1000
    lis = [(dv ** 4, 'T'), (dv ** 3, 'B'), (dv ** 2, 'M'), (dv ** 1, 'K')]
    if useMode == 1:
        dv = 1024
        lis = [(dv ** 4, 'T'), (dv ** 3, 'G'), (dv ** 2, 'M'), (dv ** 1, 'K')]
    #
    for i in lis:
        s = abs(number) / i[0]
        if s:
            showNumber = str(round(float(number) / float(i[0]), 2)) + i[1]
            break
    #
    return str(showNumber)


#
def getRegionPos(xPos, yPos, maxWidth, maxHeight, width, height, xOffset=0, yOffset=0):
    def getRegion(x, y, w, h):
        if 0 <= x < w/2 and 0 <= y < h/2:
            value = 0
        elif w/2 <= x < w and 0 <= y < h/2:
            value = 1
        elif 0 <= x < w/2 and h/2 <= y < h:
            value = 2
        else:
            value = 3
        return value
    #
    region = getRegion(xPos, yPos, maxWidth, maxHeight)
    #
    if region == 0:
        xp = xPos + xOffset
        yp = yPos + yOffset
    elif region == 1:
        xp = xPos - width - xOffset
        yp = yPos + yOffset
    elif region == 2:
        xp = xPos + xOffset
        yp = yPos - height - yOffset
    else:
        xp = xPos - width - xOffset
        yp = yPos - height - yOffset
    #
    return xp, yp, region


#
def mapRangeValue(range1, range2, value1):
    assert isinstance(range1, tuple) or isinstance(range1, list), 'Argument Error, "range1" Must "tuple" or "list".'
    assert isinstance(range2, tuple) or isinstance(range2, list), 'Argument Error, "range2" Must "tuple" or "list".'
    min1, max1 = range1
    min2, max2 = range2
    #
    if max1 - min1 > 0:
        percent = float(value1 - min1) / float(max1 - min1)
        #
        value2 = (max2 - min2) * percent + min2
        return value2
    else:
        return min2


#
def mapStepValue(value, delta, step, maximum, minimum):
    _max = maximum - step
    _min = minimum + step
    if value < _min:
        if 0 < delta:
            value += step
        else:
            value = minimum
    elif _min <= value <= _max:
        value += [-step, step][delta > 0]
    elif _max < value:
        if delta < 0:
            value -= step
        else:
            value = maximum
    return value


#
def getAngleOfView(focalLength):
    b = focalLength
    a = 17.9999906718
    print math.degrees(math.atan(a / b)) * 2


#
def _memberStrMethod(method):
    def subMethod(*args, **kwargs):
        dic = {}
        for attr in dir(args[0]):
            value = getattr(args[0], attr)
            if not callable(value) and not attr.startswith("__"):
                dic[attr] = value
        method(*args, **kwargs)
        return '\n'.join(['{} = {}'.format(k, v) for k, v in dic.items()])
    return subMethod


