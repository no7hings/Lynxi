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
def _toStringCapitalize(string):
    return string[0].upper() + string[1:] if string else string


#
def _toStringPrettify(string):
    return ' '.join([_toStringCapitalize(x) for x in re.findall(r'[a-zA-Z][a-z]*[0-9]*', string)])


#
def frameToTime(frame, mode=0):
    data = int(frame) / 24
    h = data / 3600
    m = data / 60 - 60 * h
    s = data - 3600 * h - 60 * m
    if mode == 0:
        if s < 1:
            s = 1
    return '%s:%s:%s' % (str(h).zfill(2), str(m).zfill(2), str(s).zfill(2))


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
def getFrameRange(numbers):
    lis = []
    if numbers:
        lenSet = 4
        splitSep = '|'
        subSplitSep = ','
        maxFrame = max(numbers)
        minFrame = min(numbers)
        numRange = range(minFrame, maxFrame + 1)
        frameDic = collections.OrderedDict()
        for numRange, i in enumerate(numRange):
            if i in numbers:
                frameDic[numRange] = i
            elif i not in numbers:
                frameDic[numRange] = none
        reduceLis = []
        for k, v in frameDic.items():
            if v:
                reduceLis.append(str(v).zfill(lenSet) + subSplitSep)
            elif not v:
                reduceLis.append(splitSep)
        #
        reduceString = none.join(reduceLis)
        for i in reduceString.split(splitSep):
            if i:
                if len(i) == lenSet + 1:
                    isFrame = int(i[:-1])
                    lis.append(isFrame)
                elif not len(i) == lenSet + 1:
                    seqData = [int(j) for j in i[:-1].split(subSplitSep)]
                    isRange = min(seqData), max(seqData)
                    lis.append(isRange)
    return lis


#
def getBasicUniqueId():
    return '4908BDB4-911F-3DCE-904E-96E4792E75F1'


#
def getUniqueId(string=none):
    basicUuid = getBasicUniqueId()
    if string:
        return str(uuid.uuid3(uuid.UUID(basicUuid), str(string))).upper()
    elif not string:
        return str(uuid.uuid1()).upper()


#
def getUserUniqueId(user):
    basicUuid = getBasicUniqueId()
    return str(uuid.uuid5(uuid.UUID(basicUuid), str(user))).upper()


#
def getDbUniqueId(directory):
    basicUuid = getBasicUniqueId()
    return str(uuid.uuid5(uuid.UUID(basicUuid), str(directory))).upper()


#
def getSubUniqueId(strings):
    basicUuid = getBasicUniqueId()
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
def getOsFileHashString(osFile):
    string = none
    if os.path.isfile(osFile):
        with open(osFile, 'rb') as f:
            md5Obj = hashlib.md5()
            md5Obj.update(f.read())
            hashValue = md5Obj.hexdigest()
            f.close()
            #
            string = str(hashValue).upper()
    return string


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
    else:
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
    basicUuid = getBasicUniqueId()
    uniqueId = str(uuid.uuid3(uuid.UUID(basicUuid), str(osFileBasename))).upper()
    return _toOsFile(osPath, uniqueId)


#
def setOsFilePathCreate(osFile):
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
        setOsFilePathCreate(targetOsFile)
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
        setOsFilePathCreate(targetOsFile)
        shutil.move(sourceOsFile, targetOsFile)


#
def setOsFileRename(osFile, osFileName):
    newOsFile = toOsFileReplaceFileName(osFile, osFileName)
    if not isOsSameFile(osFile, newOsFile):
        os.rename(osFile, newOsFile)


#
def setOsFileRename_(osFile, newOsFile):
    if not isOsSameFile(osFile, newOsFile):
        os.rename(osFile, newOsFile)


#
def setOsFolderCopy(sourceOsPath, targetOsPath, progressModule=None):
    osFiles = getOsFiles(sourceOsPath)
    if osFiles:
        progressBar = None
        if progressModule:
            explain = '''Copy Os File'''
            maxValue = len(osFiles)
            progressBar = progressModule.viewSubProgress(explain, maxValue)
        for sourceOsFile in osFiles:
            if progressBar:
                progressBar.updateProgress()
            targetOsFile = targetOsPath + sourceOsFile[len(sourceOsPath):]
            setOsFileCopy(sourceOsFile, targetOsFile)


#
def moveOsFolder(sourceOsPath, targetOsPath, progressModule=none):
    osFiles = getOsFiles(sourceOsPath)
    if osFiles:
        progressBar = none
        if progressModule:
            explain = '''Copy Os File'''
            maxValue = len(osFiles)
            progressBar = progressModule.viewSubProgress(explain, maxValue)
        for sourceOsFile in osFiles:
            if progressBar:
                progressBar.updateProgress()
            targetOsFile = targetOsPath + sourceOsFile[len(sourceOsPath):]
            setOsFileMove(sourceOsFile, targetOsFile)


#
def setOsFileRemove(osFile):
    if os.path.isfile(osFile):
        os.remove(osFile)


#
def deleteOsFolder(osPath):
    osFiles = getOsFiles(osPath)
    if osFiles:
        for osFile in osFiles:
            setOsFileRemove(osFile)
    #
    setOsFileRemove(osPath)


#
def setOsFolderOpen(osPath):
    if isOsPath(osPath):
        os.startfile(osPath.replace('/', os.sep))


#
def setOsFileOpen(osFile):
    if isOsExistsFile(osFile):
        os.startfile(osFile.replace('/', os.sep))


#
def setOsFileFolderOpen(osFile):
    osFolder = getOsFileDirname(osFile)
    if isOsExist(osFolder):
        os.startfile(osFolder.replace('/', os.sep))


#
def openOsVedioFile(osFile, tempOsFile=None):
    if isOsExistsFile(osFile):
        tempVedioFile = getOsTempVedioFile(osFile)
        if tempOsFile is not None:
            tempVedioFile = tempOsFile
        timestamp = str(getOsFileMtimestamp(osFile))
        if isOsExistsFile(tempVedioFile):
            tempTimestamp = str(getOsFileMtimestamp(tempVedioFile))
        else:
            tempTimestamp = None
        if not timestamp == tempTimestamp:
            setOsFileCopy(osFile, tempVedioFile)
        #
        if isOsExist(tempVedioFile):
            setOsFileOpen(tempVedioFile)


#
def openOsVedioFiles(osFiles):
    lis = []
    for osFile in osFiles:
        tempVedioFile = getOsTempVedioFile(osFile)
        timestamp = str(getOsFileMtimestamp(osFile))
        if isOsExistsFile(tempVedioFile):
            tempTimestamp = str(getOsFileMtimestamp(tempVedioFile))
        else:
            tempTimestamp = None
        if not timestamp == tempTimestamp:
            setOsFileCopy(osFile, tempVedioFile)
        #
        if isOsExist(tempVedioFile):
            lis.append(tempVedioFile)
    return lis


#
def getOsFileIsMtimeChanged(sourceOsFile, targetOsFile):
    boolean = False
    if isOsExistsFile(sourceOsFile) and isOsExistsFile(targetOsFile):
        sourceFileTimestamp = str(getOsFileMtimestamp(sourceOsFile))
        targetFileTimestamp = str(getOsFileMtimestamp(targetOsFile))
        if sourceFileTimestamp != targetFileTimestamp:
            boolean = True
    return boolean


#
def getOsFileIsHashChanged(sourceOsFile, targetOsFile):
    if isOsExistsFile(sourceOsFile):
        if isOsExistsFile(targetOsFile):
            sourceHash = getOsFileHashKey_(sourceOsFile)
            targetHash = getOsFileHashKey_(targetOsFile)
            if sourceHash != targetHash:
                boolean = True
            else:
                boolean = False
        else:
            boolean = True
    else:
        boolean = True
    return boolean


#
def getChangedOsFiles(sourceOsPath, targetOsPath):
    def getBranch(osPath):
        checkJson = osPath + '/timestamp.json'
        if not isOsExist(checkJson):
            dic = {}
            isAscii = False
            osFiles = getOsFiles(osPath)
            if osFiles:
                for osFile in osFiles:
                    osFileTimestamp = str(getOsFileMtimestamp(osFile))
                    localOsFile = osFile[len(osPath):]
                    #
                    if isinstance(localOsFile, unicode):
                        isAscii = True
                    #
                    dic[localOsFile] = osFileTimestamp
            writeOsJson(dic, checkJson, ensure_ascii=isAscii)
        else:
            dic = readOsJson(checkJson, encoding='gbk')
        return dic
    #
    def getChanged(sourceDic, targetDic):
        lis = []
        for localOsFile, sourceTime in sourceDic.items():
            if targetDic.__contains__(localOsFile):
                targetTime = targetDic[localOsFile]
                if sourceTime != targetTime:
                    lis.append(localOsFile)
            #
            elif not targetDic.__contains__(localOsFile):
                lis.append(localOsFile)
        return lis
    #
    return getChanged(getBranch(sourceOsPath), getBranch(targetOsPath))


#
def getSystemModuleData():
    return sys.modules


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
def osPathsep():
    return os.pathsep


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
def getLocaltime():
    timestamp = time.time()
    return [i for i in time.localtime(timestamp)]


#
def getViewLocalTime(localtime=none, mode=1):
    if not localtime:
        localtime = getLocaltime()
    year, month, date, hour, minute, second, week, dayCount, isDst = localtime
    viewDate = Dates[int(str(date - 1)[-1])][mode]
    if date > 10:
        viewDate = [Dates[int(str(date)[0]) - 1][0] + [u'十', ''][int(str(date)[-1]) == 0], str(date - 1)[0]][mode] \
                   + [Dates[int(str(date - 1)[-1])][0] + u'日', Dates[int(str(date - 1)[-1])][1][:-2] + 'th'][mode]
    viewMonth = (Months[month-1])[mode]
    viewYear = ([u'{}年'.format(year), str(year)])[mode]
    print viewDate, viewMonth, viewYear


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
def getCnViewTime(timestamp):
    if isinstance(timestamp, float):
        return cnViewTimeSet(time.localtime(timestamp))
    else:
        return u'无记录'


#
def cnViewTimeSet(timetuple, useMode=0):
    year, month, date, hour, minute, second, week, dayCount, isDst = timetuple
    if useMode == 0:
        timetuple_ = time.localtime(time.time())
        year_, month_, date_, hour_, minute_, second_, week_, dayCount_, isDst_ = timetuple_
        #
        monday_ = date_ - week_
        monday = date - week
        if year_ == year:
            dateString = u'{}月{}日'.format(str(month).zfill(2), str(date).zfill(2))
            weekString = none
            subString = none
            if timetuple_[:2] == timetuple[:2]:
                if monday_ == monday:
                    dateString = none
                    weekString = u'{0}'.format(Weeks[int(week)][0])
                    if date_ == date:
                        subString = u'（今天）'
                    elif date_ == date + 1:
                        subString = u'（昨天）'
            #
            timeString = u'{0}点{1}分'.format(str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2))
            #
            string = u'{0}{1}{2} {3}'.format(dateString, weekString, subString, timeString)
            return string
        else:
            return u'{}年{}月{}日'.format(str(year).zfill(4), str(month).zfill(2), str(date).zfill(2))
    else:
        dateString = u'{0}年{1}月{2}日'.format(str(year).zfill(4), str(month).zfill(2), str(date).zfill(2))
        timeString = u'{0}点{1}分{2}秒'.format(str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2))
        return u'{0} {1}'.format(dateString, timeString)


# Transform Update
def translateRecordViewTime(timeTag, useMode=0):
    if timeTag:
        if re.findall(r'[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]', timeTag):
            year = int(timeTag[:4])
            month = int(timeTag[5:7])
            date = int(timeTag[7:9])
            hour = int(timeTag[10:12])
            minute = int(timeTag[12:14])
            if year > 0:
                timetuple = datetime.datetime(year=year, month=month, day=date, hour=hour, minute=minute).timetuple()
                string = cnViewTimeSet(timetuple, useMode)
            else:
                string = u'{0}{0}年{0}月{0}日{0}点分'.format('??')
        else:
            string = u'无记录'
    else:
        string = u'无记录'
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


# Back up File
def backupOsFile(osFile, osBackFile, timeTag=none):
    if timeTag:
        if isOsExistsFile(osFile):
            backFileJoinUpdateTag = getOsFileJoinTimeTag(osBackFile, timeTag)
            #
            setOsFileCopy(osFile, backFileJoinUpdateTag)


#
def backupOsFile_(osFile, timeTag=none, useMode=0):
    if isOsExistsFile(osFile):
        osBackFile = getOsFileJoinTimeTag(osFile, timeTag, useMode)
        #
        setOsFileCopy(osFile, osBackFile)
        #
        return osBackFile


#
def toExceptionString():
    return traceback.format_exc()


# Get Upload Temp File
def getOsTempFolder(osFile):
    tempDirectory = 'D:/.lynxi.temporary/' + getOsActiveDateTag()
    osFileBasename = getOsFileBasename(osFile)
    tempFile = _toOsFile(tempDirectory, osFileBasename)
    #
    setOsFilePathCreate(tempFile)
    return tempFile


# Get Upload Temp File
def getOsTemporaryFile(osFile, timeTag=None):
    if not timeTag:
        timeTag = getOsActiveTimeTag()
    tempDirectory = 'D:/.lynxi.temporary/' + timeTag
    osFileBasename = getOsFileBasename(osFile)
    tempFile = _toOsFile(tempDirectory, osFileBasename)
    #
    setOsFilePathCreate(tempFile)
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
    setOsFilePathCreate(tempFile)
    return tempFile


class _AbcFile(object):
    def _initAbcFile(self, fileString):
        self._fileString = fileString

    def exist(self):
        return os.path.isfile(self.fileString())

    def fileString(self):
        return self._fileString

    def read(self, *args):
        pass

    def write(self, *args):
        pass


class File(_AbcFile):
    def __init__(self, fileString):
        self._initAbcFile(fileString)

    def read(self, osFile, readLines=False):
        if self.exist():
            with open(self.fileString(), 'r') as f:
                if readLines is False:
                    data = f.read()
                else:
                    data = f.readlines()
                f.close()
                return data

    def write(self, raw):
        if raw is not None:
            setOsFilePathCreate(self.fileString())
            with open(self.fileString(), 'wb') as f:
                if isinstance(raw, str) or isinstance(raw, unicode):
                    f.write(raw)
                elif isinstance(raw, tuple) or isinstance(raw, list):
                    f.writelines(raw)
                f.close()


class JsonFile(_AbcFile):
    def __init__(self, fileString):
        self._initAbcFile(fileString)

    def read(self, encoding=None):
        if self.exist():
            with open(self.fileString()) as j:
                data = json.load(j, encoding=encoding)
                return data

    def write(self, raw, ensure_ascii=True, indent=4):
        if raw is not None:
            tempFile = getOsTemporaryFile(self.fileString())
            #
            with open(tempFile, 'w') as j:
                json.dump(raw, j, ensure_ascii=ensure_ascii, indent=indent)
            #
            setOsFileCopy(tempFile, self.fileString())


#
def readOsJson(osFile, encoding=None):
    if os.path.isfile(osFile):
        with open(osFile) as j:
            data = json.load(j, encoding=encoding)
            return data


#
def readOsJsonDic(osFile, key):
    data = readOsJson(osFile)
    if data:
        if key in data:
            return data[key]


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
                setOsFilePathCreate(subOsFile)
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
def getJsonDumps(data):
    return json.dumps(data)


#
def getJsonLoads(data):
    return json.loads(data)


#
def readOsFileLines(osFile):
    if os.path.isfile(osFile):
        with open(osFile, 'r') as f:
            data = f.readlines()
            f.close()
            return data


#
def readOsFile(osFile):
    if os.path.isfile(osFile):
        with open(osFile, 'r') as f:
            data = f.read()
            f.close()
            return data


#
def readDataGzip(osFile):
    if isOsExistsFile(osFile):
        with gzip.GzipFile(mode='rb', fileobj=open(osFile, 'rb')) as g:
            data = g.read()
            g.close()
            return data


#
def writeOsData(data, osFile):
    if data is not None:
        setOsFilePathCreate(osFile)
        with open(osFile, 'wb') as f:
            if isinstance(data, str) or isinstance(data, unicode):
                f.write(data)
            elif isinstance(data, tuple) or isinstance(data, list):
                f.writelines(data)
            f.close()


#
def writeDataGzip(data, osFile):
    setOsFilePathCreate(osFile)
    #
    osFileBasename = getOsFileBasename(osFile)
    #
    with gzip.GzipFile(filename=osFileBasename, mode='wb', compresslevel=9, fileobj=open(osFile, 'wb')) as g:
        g.write(data)
        g.close()


#
def copyOsFileToGzip(sourceOsFile, targetOsFile):
    setOsFilePathCreate(targetOsFile)
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
            strings = _toStringPrettify(strings)
        string = strings
    elif isinstance(strings, list) or isinstance(strings, tuple):
        if isUseNiceName is True:
            strings = [_toStringPrettify(i) for i in strings]
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
def getPImage(textureFile):
    # noinspection PyUnresolvedReferences
    from PIL import Image
    #
    if isOsExistsFile(textureFile):
        return Image.open(str(textureFile))


#
def getImageSize(texture, useMode=0):
    size = 0, 0
    if texture:
        try:
            if useMode == 0:
                size = getPImage(texture).size
            elif useMode == 1:
                size = texture.size
        except:
            pass
    return size


#
def getComposeLabel(*labels):
    return labels[0] + ''.join([i.capitalize() for i in labels[1:]])


#
def isOsSameFile(sourceOsFile, targetOsFile):
    return os.path.normpath(sourceOsFile) == os.path.normpath(targetOsFile)


#
def hsvToRgb(h, s, v, maximum=255):
    h = float(h % 360.0)
    s = float(max(min(s, 1.0), 0.0))
    v = float(max(min(v, 1.0), 0.0))
    #
    c = v * s
    x = c * (1 - abs((h / 60.0) % 2 - 1))
    m = v - c
    if 0 <= h < 60:
        r_, g_, b_ = c, x, 0
    elif 60 <= h < 120:
        r_, g_, b_ = x, c, 0
    elif 120 <= h < 180:
        r_, g_, b_ = 0, c, x
    elif 180 <= h < 240:
        r_, g_, b_ = 0, x, c
    elif 240 <= h < 300:
        r_, g_, b_ = x, 0, c
    else:
        r_, g_, b_ = c, 0, x
    #
    if maximum == 255:
        r, g, b = int(round((r_ + m) * maximum)), int(round((g_ + m) * maximum)), int(round((b_ + m) * maximum))
    else:
        r, g, b = float((r_ + m)), float((g_ + m)), float((b_ + m))
    return r, g, b


#
def getRgbByString(string, maximum=255):
    a = int(''.join([str(ord(i)).zfill(3) for i in string]))
    b = a % 3
    i = int(a / 256) % 3
    n = int(a % 256)
    if a % 2:
        if i == 0:
            r, g, b = 64 + 64 * b, n, 0
        elif i == 1:
            r, g, b = 0, 64 + 64 * b, n
        else:
            r, g, b = 0, n, 64 + 64 * b
    else:
        if i == 0:
            r, g, b = 0, n, 64 + 64 * b
        elif i == 1:
            r, g, b = 64 + 64 * b, 0, n
        else:
            r, g, b = 64 + 64 * b, n, 0
    #
    return r / 255.0 * maximum, g / 255.0 * maximum, b / 255.0 * maximum


#
def getOsLanguage():
    return locale.getdefaultlocale()


#
def getAngleOfView(focalLength):
    b = focalLength
    a = 17.9999906718
    print math.degrees(math.atan(a / b)) * 2


#
def getBadNumberArray(numberArray, useMode=0):
    lis = []
    if numberArray:
        maxiNumber = max(numberArray)
        miniNumber = min(numberArray)
        if useMode == 1:
            miniNumber = 0
        for number in range(miniNumber, maxiNumber + 1):
            if not number in numberArray:
                lis.append(number)
    return lis


#
def setTranslateHelpToMd(helpOsFile, mdOsFile):
    lis = ['[TOC]\r\n']
    lineLis = readOsData(helpOsFile, readLines=True)
    if lineLis:
        for i in lineLis:
            if i.lstrip() == '':
                i = ''
            else:
                if i.lstrip().startswith('#'):
                    if i.rstrip().endswith('#'):
                        i = ''
                    else:
                        i = '> ' + i.lstrip()[1:].lstrip()
                elif i.lstrip().startswith('|'):
                    if i.rstrip().endswith('|'):
                        i = ''
                    else:
                        if (
                                i.lstrip().startswith('|  Method resolution order') or
                                i.lstrip().startswith('|  Methods defined') or
                                i.lstrip().startswith('|  Data descriptors defined') or
                                i.lstrip().startswith('|  Data and other attributes defined') or
                                i.lstrip().startswith('|  Methods inherited from') or
                                i.lstrip().startswith('|  Data descriptors inherited from') or
                                i.lstrip().startswith('|  Data and other attributes inherited from')
                        ):
                            if ' from ' in i:
                                i = '------\r\n*' + i.lstrip()[1:].split(' from ')[0].lstrip().rstrip() + ' from:*\r\n' + '**' + i.split('from')[-1].lstrip().rstrip()[:-1] + '**\r\n'
                            else:
                                i = '------\r\n*' + i.lstrip()[1:].lstrip().rstrip() + '*\r\n'
                        elif i.rstrip().endswith('|  ----------------------------------------------------------------------'):
                            i = ''
                        elif (
                                i.rstrip().endswith('__dict__') or
                                i.rstrip().endswith('__weakref__')
                        ):
                            i = '#### ' + i.lstrip()[1:].lstrip()

                        elif i.rstrip().endswith(')') and not ':param' in i and not ':return' in i and not ' -> ' in i:
                            if i.rstrip().endswith('(...)'):
                                i = '#### ' + i.lstrip()[1:].lstrip()
                            elif i.rstrip().endswith('if defined)'):
                                i = '> ' + i.lstrip()[1:].lstrip()
                            elif ' = ' in i:
                                i = '#### ' + i.split(' = ')[0].lstrip()[1:].lstrip() + '(...)\r\n**= ' + i.split(' = ')[-1].rstrip() + '**\r\n'
                            else:
                                i = '#### ' + i.lstrip()[1:].lstrip()
                        else:
                            if i.lstrip()[1:].lstrip().startswith('*'):
                                i = '> **' + i.lstrip()[1:].lstrip()[1:].lstrip().rstrip() + '**\r\n'
                            elif ' = ' in i:
                                if i.rstrip().endswith('>'):
                                    if '<class' in i:
                                        i = '- ' + i.lstrip()[1:].lstrip()
                                    else:
                                        i = '> ' + i.lstrip()[1:].lstrip()
                                else:
                                    i = '- ' + i.lstrip()[1:].lstrip()
                            else:
                                if ' -> ' in i:
                                    i = '- ' + i.split(' -> ')[0].lstrip()[1:].lstrip() + '\r\nreturn -> ' + i.split(' -> ')[-1]
                                elif ':param' in i:
                                    i = '- *' + i.split(':param')[-1].lstrip().rstrip() + '*\r\n'
                                elif ':return' in i:
                                    i = '- return -> **' + '<span style="color:#7f5fff;">{}</span>'.format(i.split(':return:')[-1].lstrip().rstrip()) + '**\r\n'
                                else:
                                    i = '> ' + i.lstrip()[1:].lstrip()
                elif (
                        i.rstrip().endswith('NAME') or
                        i.rstrip().endswith('FILE') or
                        i.rstrip().endswith('CLASSES') or
                        i.rstrip().endswith('DESCRIPTION') or
                        i.rstrip().endswith('DATA') or
                        i.rstrip().endswith('FUNCTIONS')
                ):
                    i = '# ' + i
                else:
                    if i.lstrip().startswith('class'):
                        i = '## ' + i.lstrip()[5:].lstrip()
                    else:
                        if i.rstrip().endswith(')'):
                            if i.rstrip().endswith('(...)'):
                                if ' = ' in i:
                                    i = '## ' + i.lstrip().split(' = ')[0] + '(...)\r\n>  = ' + i.split(' = ')[-1]
                                else:
                                    i = '## ' + i.lstrip()
                            else:
                                i = '## ' + i.lstrip()
                        else:
                            if ' -> ' in i:
                                i = '- ' + i.split(' -> ')[0].lstrip()[1:].lstrip() + '\r\nreturn -> ' + i.split(' -> ')[-1]
                            else:
                                i = '> ' + i
            #
            i = i.replace('_', '\\_')
            lis.append(i)
    #
    writeOsData(lis, mdOsFile)


#
def getAngle(x1, y1, x2, y2):
    radian = 0.0
    #
    r0 = 0.0
    r90 = math.pi / 2.0
    r180 = math.pi
    r270 = 3.0 * math.pi / 2.0
    #
    if x1 == x2:
        if y1 < y2:
            radian = r0
        elif y1 > y2:
            radian = r180
    elif y1 == y2:
        if x1 < x2:
            radian = r90
        elif x1 > x2:
            radian = r270
    elif x1 < x2 and y1 < y2:
        radian = math.atan2((-x1 + x2), (-y1 + y2))
    elif x1 < x2 and y1 > y2:
        radian = r90 + math.atan2((y1 - y2), (-x1 + x2))
    elif x1 > x2 and y1 > y2:
        radian = r180 + math.atan2((x1 - x2), (y1 - y2))
    elif x1 > x2 and y1 < y2:
        radian = r270 + math.atan2((-y1 + y2), (x1 - x2))
    #
    return radian * 180 / math.pi


#
def getLength(x1, y1, x2, y2):
    return math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))


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


class _EnvironString(str):
    def __init__(self, value):
        self._value = value

        self._key = ''
        self._parent = None

    def _add(self, value):
        if self._value:
            lis = [i.lstrip().rstrip() for i in self._value.split(os.pathsep)]
            lowerLis = [i.lstrip().rstrip().lower() for i in self._value.lower().split(os.pathsep)]
            if value.lower() not in lowerLis:
                lis.append(value)
                self._value = os.pathsep.join(lis)
        else:
            self._value = value

    def _sub(self, value):
        if self._value:
            lis = [i.lstrip().rstrip() for i in self._value.split(os.pathsep)]
            lowerLis = [i.lstrip().rstrip().lower() for i in self._value.lower().split(os.pathsep)]
            if value.lower() in lowerLis:
                i = lowerLis.index(value.lower())
                lis.remove(lis[i])
                self._value = os.pathsep.join(lis)

    def _update(self):
        os.environ[self._key] = self._value

        str_ = _EnvironString(self._value)
        str_.key = self._key
        str_.parent = self._parent

        self.parent.__dict__[self._key] = str_
        return str_

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

        os.environ[self._key] = self._value

    def __iadd__(self, value):
        if isinstance(value, list) or isinstance(value, tuple):
            [self._add(i) for i in list(value)]
        else:
            self._add(value)

        return self._update()

    def __isub__(self, value):
        if isinstance(value, list) or isinstance(value, tuple):
            [self._sub(i) for i in list(value)]
        else:
            self._sub(value)

        return self._update()

    def append(self, value):
        self._add(value)

    def remove(self, value):
        self._sub(value)

    def __str__(self):
        return self._value.replace(os.pathsep, os.pathsep + '\r\n')


class Environ(object):
    def __getattr__(self, key):
        key = key.upper()

        value = os.environ.get(key, '')
        if not key in self.__dict__:
            str_ = _EnvironString(value)
            str_.key = key
            str_.parent = self

            self.__dict__[key] = str_
            return str_

    def __setattr__(self, key, value):
        key = key.upper()

        str_ = _EnvironString(value)
        str_.key = key
        str_.parent = self

        self.__dict__[key] = str_

    @staticmethod
    def exist(key, value):
        value_ = os.environ.get(key)
        if value_ is not None:
            lowerLis = [i.lstrip().rstrip().lower() for i in value_.split(os.pathsep)]
            return value.lower() in lowerLis
        return False


