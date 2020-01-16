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
import time
#
import datetime
#
import shutil
#
import uuid
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
GzipExt = '.gz'
TarGZipExt = '.tar.gz'
UpdateExt = '.update'
InfoExt = '.info'
LogExt = '.log'
#
UpdateViewTimeFormat = '%Y - %m%d - [ %H:%M:%S ]'
MaUpdateViewTimeFormat = '%Y-%m-%d %H:%M:%S'
#
THREAD_MAX = threading.Semaphore(1024)
#
OsFilePathSep = '/'
Ma_Separator_Node = '|'
Ma_Separator_Namespace = ':'
#
none = ''


#
class DtbThread(threading.Thread):
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
def toStringList(data):
    lis = []
    if isinstance(data, str) or isinstance(data, unicode):
        lis = [data]
    elif isinstance(data, list) or isinstance(data, tuple):
        lis = list(data)
    return lis


#
def basicUniqueId():
    return '4908BDB4-911F-3DCE-904E-96E4792E75F1'


#
def getUniqueId(string=none):
    basicUuid = basicUniqueId()
    if string:
        return str(uuid.uuid3(uuid.UUID(basicUuid), str(string))).upper()
    elif not string:
        return str(uuid.uuid1()).upper()


#
def getUserUniqueId(user):
    basicUuid = basicUniqueId()
    return str(uuid.uuid5(uuid.UUID(basicUuid), str(user))).upper()


#
def getDbUniqueId(directory):
    basicUuid = basicUniqueId()
    return str(uuid.uuid5(uuid.UUID(basicUuid), str(directory))).upper()


#
def getSubUniqueId(strings):
    basicUuid = basicUniqueId()
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
def isOsExist(osPath):
    if osPath:
        return os.path.exists(osPath)
    return False


#
def getOsFileMtimestamp(osFile):
    if isOsExistsFile(osFile):
        return os.stat(osFile).st_mtime


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
            osFile = toOsFile(osPath, osFileBasename)
            lis.append(osFile)
    return lis


#
def getOsFileSize(osFile):
    return int(os.path.getsize(osFile))


#
def toOsFile(osPath, osFileBasename):
    return os.path.join(osPath, osFileBasename).replace('\\', '/')


#
def getOsFiles(osPath):
    lis = []
    for root, dirs, osFileBasenames in os.walk(osPath, topdown=0):
        for osFileBasename in osFileBasenames:
            osFile = toOsFile(root, osFileBasename)
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
    filterExts = toStringList(filterExts)
    getBranch(filePath)
    if lis:
        lis.sort()
    return lis


#
def getOsUniqueFile(osFile):
    osPath = getOsFileDirname(osFile)
    osFileBasename = getOsFileBasename(osFile)
    basicUuid = basicUniqueId()
    uniqueId = str(uuid.uuid3(uuid.UUID(basicUuid), str(osFileBasename))).upper()
    return toOsFile(osPath, uniqueId)


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
    osPath = toOsFile(basicFolder, mayaFolderName)
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
def getSubLabel(seq):
    subLabel = [none, '_' + str(seq).zfill(4)][seq > 0]
    return subLabel


#
def getOsSubFile(osFile, label):
    return label.join(os.path.splitext(osFile))


#
def getOsTempVedioFile(osFile):
    tempDirectory = 'D:/.lynxi.temporary/vedio'
    osFileBasename = getOsFileBasename(osFile)
    tempFile = toOsFile(tempDirectory, osFileBasename)
    return tempFile


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
def toVariantConvert(varName, string):
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


#
def setListExtendSubList(lis, subLis):
    [lis.append(i) for i in subLis if i not in lis]


# Get Update File
def getRecordFile(osFile):
    base = os.path.splitext(osFile)[0]
    return base + UpdateExt


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
def getAngleOfView(focalLength):
    b = focalLength
    a = 17.9999906718
    print math.degrees(math.atan(a / b)) * 2


#
def memberStrMethod(method):
    def subMethod(*args, **kwargs):
        dic = {}
        for attr in dir(args[0]):
            value = getattr(args[0], attr)
            if not callable(value) and not attr.startswith("__"):
                dic[attr] = value
        method(*args, **kwargs)
        return '\n'.join(['{} = {}'.format(k, v) for k, v in dic.items()])
    return subMethod


