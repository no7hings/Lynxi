# coding:utf-8
import sys
#
import os
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
import json
#
import gzip
#
import re
#
import hashlib
#
import glob
#
import math
#
from LxCore import lxConfigure
#
from LxCore.config import appConfig


#
def orderedDict(*args):
    return collections.OrderedDict(*args)


#
class LxMethodBasic(appConfig.LxConfigBasic):
    @staticmethod
    def _toSizeRemap(width, height, maximum):
        widthReduce, heightReduce = width, height
        maxValue = max([width, height])
        if maxValue > maximum:
            if width > height:
                widthReduce, heightReduce = maximum, maximum*(float(height)/float(width))
            elif width < height:
                widthReduce, heightReduce = maximum*(float(width)/float(height)), maximum
        return widthReduce, heightReduce
    # noinspection PyUnusedLocal
    @staticmethod
    def _toGeometryRemap(size0, size1):
        w0, h0 = size0
        w1, h1 = size1
        if h0 > 0 and h1 > 0:
            pr0 = float(w0)/float(h0)
            pr1 = float(w1)/float(h1)
            smax1 = max(w1, h1)
            smin1 = min(w1, h1)
            if pr0 > 1:
                w, h = smin1, smin1/pr0
            elif pr0 < 1:
                w, h = smin1, smin1*pr0
            else:
                w, h = smin1, smin1
            x, y = (w1 - w)/2, (h1 - h)/2
            return x, y, w, h
        else:
            return 0, 0, w0, h0
    @staticmethod
    def _toStringList(string, stringLimits=None):
        lis = []
        if isinstance(string, str) or isinstance(string, unicode):
            if stringLimits:
                if string in stringLimits:
                    lis = [string]
            else:
                lis = [string]
        elif isinstance(string, tuple) or isinstance(string, list):
            for i in string:
                if stringLimits:
                    if i in stringLimits:
                        lis.append(i)
                else:
                    lis.append(i)
        return lis
    @staticmethod
    def _setLisNonrep(lis):
        addr_to = list(set(lis))
        addr_to.sort(key=lis.index)
    @classmethod
    def _toUniqueIdLis(cls, uniqueId):
        lis = []
        if isinstance(uniqueId, str) or isinstance(uniqueId, unicode):
            if cls.isUniqueId(uniqueId):
                lis = [uniqueId]
        elif isinstance(uniqueId, tuple) or isinstance(uniqueId, list):
            for i in uniqueId:
                if cls.isUniqueId(i):
                    lis.append(i)
        return lis
    @classmethod
    def _toOsFile(cls, osPath, osFileBasename):
        return cls._toOsPathConvert(os.path.join(osPath, osFileBasename))
    @staticmethod
    def getOsUser():
        return getpass.getuser()
    @staticmethod
    def getOsHostName():
        hostName = socket.getfqdn(socket.gethostname())
        return hostName
    @staticmethod
    def getOsHost():
        host = socket.gethostbyname(socket.gethostname())
        return host
    @staticmethod
    def getOsActiveTimestamp():
        return time.time()
    @staticmethod
    def getOsActiveViewTime():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    @staticmethod
    def getOsActiveDateTag():
        return time.strftime('%Y_%m%d', time.localtime(time.time()))
    @staticmethod
    def getOsActiveTimeTag():
        return time.strftime('%Y_%m%d_%H%M', time.localtime(time.time()))
    @staticmethod
    def isOsPath(string):
        return os.path.isdir(string)
    @staticmethod
    def isOsExist(osPath):
        return os.path.exists(osPath)
    @staticmethod
    def isOsFile(osFile):
        return os.path.isfile(osFile)
    @staticmethod
    def isOsExistsFile(osFile):
        if osFile:
            return os.path.isfile(osFile)
        else:
            return False
    @classmethod
    def getOsFileMtimestamp(cls, osFile):
        if cls.isOsExistsFile(osFile):
            return os.stat(osFile).st_mtime
    @classmethod
    def getOsFileMtimeTag(cls, osFile):
        timestamp = cls.getOsFileMtimestamp(osFile)
        return datetime.datetime.fromtimestamp(timestamp).strftime('%Y_%m%d_%H%M_%S%f')
    @classmethod
    def setOsFilePathCreate(cls, osFile):
        osPath = os.path.dirname(osFile)
        if not cls.isOsExist(osPath):
            os.makedirs(osPath)
    @classmethod
    def setOsDirectoryCreate(cls, osPath):
        if not cls.isOsExist(osPath):
            os.makedirs(osPath)
    @staticmethod
    def getOsFileBasename(osFile):
        return os.path.basename(osFile)
    @staticmethod
    def getOsFileBasenameLisByPath(osPath):
        lis = []
        if os.path.isdir(osPath):
            lis = os.listdir(osPath)
        return lis
    @staticmethod
    def toExceptionString():
        return traceback.format_exc()
    @staticmethod
    def isUniqueId(string):
        boolean = False
        if string is not None:
            pattern = re.compile(r'[0-9A-F]' * 8 + '-' + (r'[0-9A-F]' * 4 + '-') * 3 + r'[0-9A-F]' * 12)
            match = pattern.match(string)
            if match:
                boolean = True
        return boolean
    @staticmethod
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
    @staticmethod
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
    @classmethod
    def setLogAdd(cls, string, logType=None):
        logOsPath = cls.LynxiOsPath_Log_Server
        if logType is not None:
            osLogFile = logOsPath + '/{}.{}.log'.format(cls.getOsActiveDateTag(), logType)
        else:
            osLogFile = logOsPath + '/{}.log'.format(cls.getOsActiveDateTag())
        #
        cls.lxWriteLog(string, osLogFile)
    @classmethod
    def lxWriteLog(cls, string, osLogFile):
        cls.setOsFilePathCreate(osLogFile)
        with open(osLogFile, 'a') as log:
            log.writelines(u'{} @ {}'.format(cls.getOsActiveViewTime(), cls.getOsUser()) + u'\r\n')
            log.writelines(string + u'\r\n')
            log.close()
    @classmethod
    def addLynxiLog_exception(cls, string):
        if cls.LynxiEnable_Log is True:
            cls.setLogAdd(string, cls.LynxiLogType_Exception)
    @classmethod
    def addLynxiLog_function(cls, string):
        if cls.LynxiEnable_Log is True:
            cls.setLogAdd(string, cls.LynxiLogType_Function)
    @classmethod
    def addLynxiLog_osFile(cls, string):
        if cls.LynxiEnable_Log is True:
            cls.setLogAdd(string, cls.LynxiLogType_OsFile)
    @staticmethod
    def getDataHashString(datum):
        if datum:
            datum = str(datum)
            md5Obj = hashlib.md5()
            md5Obj.update(datum)
            hashValue = md5Obj.hexdigest()
            return str(hashValue).upper()
    @staticmethod
    def _toIntArrayReduce(array):
        lis = []
        #
        maximum, minimum = max(array), min(array)
        #
        start, end = None, None
        count = len(array)
        index = 0
        #
        array.sort()
        for seq in array:
            if index > 0:
                pre = array[index - 1]
            else:
                pre = None
            #
            if index < (count - 1):
                nex = array[index + 1]
            else:
                nex = None
            #
            if pre is None and nex is not None:
                start = minimum
                if seq - nex != -1:
                    lis.append(start)
            elif pre is not None and nex is None:
                end = maximum
                if seq - pre == 1:
                    lis.append((start, end))
                else:
                    lis.append(end)
            elif pre is not None and nex is not None:
                if seq - pre != 1 and seq - nex != -1:
                    lis.append(seq)
                elif seq - pre == 1 and seq - nex != -1:
                    end = seq
                    lis.append((start, end))
                elif seq - pre != 1 and seq - nex == -1:
                    start = seq
            #
            index += 1
        #
        return lis
    @classmethod
    def _lxIconRoot(cls):
        return lxConfigure.IconSubRoot()._serverDirectory()
    @classmethod
    def _lxDevelopRoot(cls):
        return lxConfigure.Root()._developDirectory()


#
class LxPathMethodBasic(LxMethodBasic):
    @classmethod
    def _toTreeViewPathLis(cls, pathString, pathsep):
        def addItem(item):
            if not item in lis:
                lis.append(item)
        #
        def getBranch(subPathString):
            if not subPathString in lis:
                stringLis = subPathString.split(pathsep)
                #
                dataCount = len(stringLis)
                for seq, data in enumerate(stringLis):
                    if data:
                        if seq + 1 < dataCount:
                            subPath = pathsep.join(stringLis[:seq + 1])
                            addItem(subPath)
                #
                addItem(subPathString)
        #
        lis = []
        pathStringLis = cls._toStringList(pathString)
        for i in pathStringLis:
            # Debug add root
            if not i.startswith(pathsep):
                i = pathsep + i
            #
            getBranch(i)
        return lis
    @classmethod
    def _toTreeViewPathDic(cls, dic, lis):
        [dic.setdefault(parent, []).append(child) for parent, child in lis]
    @classmethod
    def getTreeViewBuildDic(cls, pathString, pathsep):
        def addItem(item):
            if not item in lis:
                lis.append(item)
        #
        def getRootBranch(subPathString, nodeArray):
            node = nodeArray[-1]
            dic.setdefault((None, None), []).append((node, subPathString))
        #
        def getBranch(subPathString, nodeArray):
            parent = nodeArray[-2]
            parentPath = pathsep.join(nodeArray[:-1])
            node = nodeArray[-1]
            addItem(((parent, parentPath), (node, subPathString)))
        #
        def getMain():
            # Get Dict
            pathStringLis = cls._toStringList(pathString)
            if pathStringLis:
                for i in pathStringLis:
                    nodeArray = i.split(pathsep)
                    isRoot = len(nodeArray) == 2
                    # Filter is Root
                    if isRoot:
                        getRootBranch(i, nodeArray)
                    else:
                        getBranch(i, nodeArray)
            # Reduce Dict
            if lis:
                cls._toTreeViewPathDic(dic, lis)
        #
        lis = []
        dic = orderedDict()
        #
        getMain()
        return dic


#
class LxThreadMethodBasic(LxMethodBasic):
    pass


#
class LxAppMethodBasic(LxMethodBasic):
    @staticmethod
    def getAppName():
        return os.path.basename(sys.argv[0])
    @staticmethod
    def isMayaApp():
        boolean = False
        data = os.path.basename(sys.argv[0])
        if data.lower() == 'maya.exe':
            boolean = True
        return boolean


#
class LxOsMethodBasic(LxMethodBasic):
    @classmethod
    def getOsFileInfoDic(cls, osSourceFile, description=None, note=None):
        return orderedDict(
            [
                (cls.Lynxi_Key_Info_Update, cls.getOsActiveTimestamp()),
                (cls.Lynxi_Key_Info_Artist, cls.getOsUser()),
                #
                (cls.Lynxi_Key_Info_Host, cls.getOsHost()),
                (cls.Lynxi_Key_Info_HostName, cls.getOsHostName()),
                #
                (cls.Lynxi_Key_Info_SourceFile, osSourceFile),
                #
                (cls.Lynxi_Key_Info_Description, description),
                (cls.Lynxi_Key_Info_Note, note)
            ]
        )


#
class LxOsFileMethodBasic(LxOsMethodBasic):
    @staticmethod
    def getOsFileHashString(osFile):
        string = None
        if os.path.isfile(osFile):
            with open(osFile, 'rb') as f:
                md5Obj = hashlib.md5()
                while True:
                    d = f.read(8096)
                    if not d:
                        break
                    md5Obj.update(d)
                #
                hashValue = md5Obj.hexdigest()
                f.close()
                string = str(hashValue).upper()
        return string
    @classmethod
    def _toLxOsInfoFile(cls, osFile):
        base = cls.getOsFileBase(osFile)
        string = base + cls.LynxiOsExt_Info
        return string
    @classmethod
    def getOsTemporaryFile(cls, osFile, timeTag=None):
        if timeTag is None:
            timeTag = cls.getOsActiveTimeTag()
        #
        tempDirectory = cls._toOsFile(cls.LynxiOsPath_LocalTemporary, timeTag)
        osFileBasename = cls.getOsFileBasename(osFile)
        string = cls._toOsFile(tempDirectory, osFileBasename)
        #
        cls.setOsFilePathCreate(string)
        return string
    @classmethod
    def getOsTempFolder(cls, osFile):
        tempDirectory = 'D:/.lynxi.temporary/' + cls.getOsActiveDateTag()
        osFileBasename = cls.getOsFileBasename(osFile)
        string = cls._toOsFile(tempDirectory, osFileBasename)
        #
        cls.setOsFilePathCreate(string)
        return string
    @staticmethod
    def toOsFileSplitByExt(osFile):
        return os.path.splitext(osFile)
    @staticmethod
    def getOsFileExt(osFile):
        return os.path.splitext(osFile)[-1]
    @classmethod
    def getOsFileDirname(cls, osFile):
        return cls._toOsPathConvert(os.path.dirname(osFile))
    @staticmethod
    def getOsFileBase(osFile):
        return os.path.splitext(osFile)[0]
    @staticmethod
    def getOsFileName(osFile):
        return os.path.splitext(os.path.basename(osFile))[0]
    @classmethod
    def getOsTargetFile(cls, osFile, targetOsPath):
        osFileBasename = cls.getOsFileBasename(osFile)
        targetTexture = cls._toOsFile(targetOsPath, osFileBasename)
        return targetTexture
    @classmethod
    def getOsTargetFileLis(cls, osFile, targetOsPath):
        lis = []
        #
        osFileLis = cls._toStringList(osFile)
        if osFileLis:
            [lis.append(cls.getOsTargetFile(i, targetOsPath)) for i in osFileLis]
        return lis
    @classmethod
    def toOsFileReplaceFileName(cls, osFile, fileNameString):
        osPath, osExt = cls.getOsFileDirname(osFile), cls.getOsFileExt(osFile)
        newOsFile = u'{0}/{1}{2}'.format(osPath, fileNameString, osExt)
        return newOsFile
    @classmethod
    def setOsFileCopy(cls, sourceOsFile, targetOsFile, force=True):
        if os.path.isfile(sourceOsFile):
            cls.setOsFilePathCreate(targetOsFile)
            # Check Same File
            if not os.path.normpath(sourceOsFile) == os.path.normpath(targetOsFile):
                if force is True:
                    shutil.copy2(sourceOsFile, targetOsFile)
                else:
                    try:
                        shutil.copy2(sourceOsFile, targetOsFile)
                    except IOError:
                        print sourceOsFile, targetOsFile
    @classmethod
    def getOsFileIsMtimeChanged(cls, sourceOsFile, targetOsFile):
        boolean = False
        if not os.path.normpath(sourceOsFile) == os.path.normpath(targetOsFile):
            if cls.isOsExistsFile(sourceOsFile) and cls.isOsExistsFile(targetOsFile):
                sourceFileTimestamp, targetFileTimestamp = str(cls.getOsFileMtimestamp(sourceOsFile)), str(cls.getOsFileMtimestamp(targetOsFile))
                if sourceFileTimestamp != targetFileTimestamp:
                    boolean = True
        return boolean
    @classmethod
    def getOsFileCollectionDatumLis(cls, osFile, targetOsPath, ignoreMtimeChanged=False, ignoreExists=False):
        def getBranch(sourceOsFile):
            targetOsFile = cls.getOsTargetFile(sourceOsFile, targetOsPath)
            #
            enable = False
            if cls.isOsExistsFile(targetOsFile):
                if ignoreExists is True:
                    enable = False
                else:
                    if ignoreMtimeChanged is True:
                        enable = True
                    else:
                        isMtimeChanged = cls.getOsFileIsMtimeChanged(sourceOsFile, targetOsFile)
                        if isMtimeChanged:
                            enable = True
            else:
                enable = True
            #
            if enable is True:
                lis.append((sourceOsFile, targetOsFile))
        #
        lis = []
        #
        osFileLis = cls._toStringList(osFile)
        if osFileLis:
            [getBranch(i) for i in osFileLis]
        return lis
    @classmethod
    def setOsFileCollection(cls, osFile, targetOsPath, ignoreMtimeChanged=False, ignoreExists=False, backupExists=False):
        def setBranch(sourceOsFile, targetOsFile):
            cls.setOsFileCopy(sourceOsFile, targetOsFile)
            cls.addLynxiLog_osFile(u'//Result : Copy {} > {}//'.format(sourceOsFile, targetOsFile))
        #
        if backupExists is True:
            pass
        #
        osFileCollectionDatumLis = cls.getOsFileCollectionDatumLis(osFile, targetOsPath, ignoreMtimeChanged, ignoreExists)
        if osFileCollectionDatumLis:
            if osFileCollectionDatumLis:
                [setBranch(i, j) for i, j in osFileCollectionDatumLis]
                cls.addLynxiLog_osFile(u'//Result : Complete Copy//'.format(targetOsPath))
            else:
                cls.addLynxiLog_osFile(u'//Warning : Nothing to Copy//'.format(targetOsPath))
    @classmethod
    def getOsFileBackupDatum(cls, osFile):
        hashKey = cls.getOsFileHashString(osFile)
        dirname, filename, ext = cls.getOsFileDirname(osFile), cls.getOsFileName(osFile), cls.getOsFileExt(osFile)
        #
        targetOsFile = cls.OsFileSep.join([cls.getOsFileDirname(osFile),  cls.LynxiOsFolder_History, filename + ext, hashKey])
        osVersionFile = cls.OsFileSep.join([cls.getOsFileDirname(osFile),  cls.LynxiOsFolder_History, filename + cls.LynxiOsExt_Version])
        return targetOsFile, osVersionFile
    @classmethod
    def setOsFileBackup(cls, osFile):
        if cls.isOsExistsFile(osFile):
            targetOsFile, osVersionFile = cls.getOsFileBackupDatum(osFile)
            if not cls.isOsExistsFile(targetOsFile):
                cls.setOsFileBackupSub(osFile, targetOsFile)
            #
            cls.writeOsJsonDic({cls.getOsActiveTimestamp(): cls.getOsFileBasename(targetOsFile)}, osVersionFile)
    @classmethod
    def setOsFileBackupSub(cls, sourceOsFile, targetOsFile):
        cls.setOsFileCopy(sourceOsFile, targetOsFile)
        #
        info = cls.getOsFileInfoDic(sourceOsFile)
        infoFile = cls._toLxOsInfoFile(targetOsFile)
        cls.writeOsJson(info, infoFile)
    @staticmethod
    def isOsSameFile(sourceOsFile, targetOsFile):
        return os.path.normpath(sourceOsFile) == os.path.normpath(targetOsFile)
    @classmethod
    def setOsFileRename(cls, osFile, fileNameString):
        newOsFile = cls.toOsFileReplaceFileName(osFile, fileNameString)
        if not cls.isOsSameFile(osFile, newOsFile):
            os.rename(osFile, newOsFile)
    @classmethod
    def setOsFileMove(cls, sourceOsFile, targetOsFile):
        if cls.isOsExistsFile(sourceOsFile):
            if not cls.isOsSameFile(sourceOsFile, targetOsFile):
                cls.setOsFilePathCreate(targetOsFile)
                #
                shutil.move(sourceOsFile, targetOsFile)
    @classmethod
    def writeOsData(cls, data, osFile):
        cls.setOsFilePathCreate(osFile)
        with open(osFile, 'wb') as f:
            if isinstance(data, str) or isinstance(data, unicode):
                f.write(data)
            elif isinstance(data, tuple) or isinstance(data, list):
                f.writelines(data)
            #
            f.close()
    @staticmethod
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
    @classmethod
    def getOsMultiFileLisSub(cls, osFile, keyword, padding=4):
        lis = []
        #
        osDirname, osBasename = cls.getOsFileDirname(osFile), cls.getOsFileBasename(osFile)
        osFile = cls._toOsFile(osDirname, osBasename.lower())
        subOsFileLis = glob.glob(osFile.replace(keyword.lower(), '[0-9]'*padding))
        if subOsFileLis:
            # Use for Repath
            for subOsFile in subOsFileLis:
                subOsFile = subOsFile.replace('\\', '/')
                lis.append(subOsFile)
        return lis
    @classmethod
    def getOsTextureUdimLis(cls, texture):
        lis = []
        texture = texture.replace('<UDIM>', '<udim>')
        #
        subOsFileLis = glob.glob(texture.replace('<udim>', '[0-9][0-9][0-9][0-9]'))
        if subOsFileLis:
            for subOsFile in subOsFileLis:
                if cls.isOsExistsFile(subOsFile):
                    lis.append(cls._toOsPathConvert(subOsFile))
        return lis
    @classmethod
    def getOsTextureSequenceLis(cls, texture):
        lis = []
        texture = texture.replace('<F>', '<f>')
        subOsFileLis = glob.glob(texture.replace('<f>', '[0-9][0-9][0-9][0-9]'))
        if subOsFileLis:
            for subOsFile in subOsFileLis:
                if cls.isOsExistsFile(subOsFile):
                    lis.append(cls._toOsPathConvert(subOsFile))
        return lis
    @classmethod
    def getOsTextureCompLis(cls, texture):
        lis = []
        if texture:
            lis = [texture]
            if '<udim>' in texture.lower():
                subTextures = cls.getOsTextureUdimLis(texture)
                lis.extend(subTextures)
            elif '<f>' in texture.lower():
                subTextures = cls.getOsTextureSequenceLis(texture)
                lis.extend(subTextures)
        return lis
    @classmethod
    def readOsJson(cls, osJsonFile):
        if cls.isOsExistsFile(osJsonFile):
            with open(osJsonFile) as f:
                data = json.load(f)
                return data
    @classmethod
    def writeOsJson(cls, data, osJsonFile, indent=4):
        cls.setOsFilePathCreate(osJsonFile)
        #
        with open(osJsonFile, 'w') as f:
            json.dump(data, f, indent=indent)
    @classmethod
    def readOsJsonDic(cls, osJsonFile, key):
        data = cls.readOsJson(osJsonFile)
        if data:
            if key in data:
                return data[key]
    @classmethod
    def writeOsJsonDic(cls, data, osFile, indent=4):
        dic = {}
        #
        gzFile = osFile
        if cls.isOsExistsFile(gzFile):
            dic = cls.readOsJson(osFile)
        for k, v in data.items():
            dic[k] = v
        #
        cls.writeOsJson(dic, osFile, indent)
    @classmethod
    def readJsonGzip(cls, osFile):
        if cls.isOsExistsFile(osFile):
            with gzip.GzipFile(mode='rb', fileobj=open(osFile, 'rb')) as g:
                data = json.load(g)
                #
                g.close()
                return data
    @classmethod
    def writeJsonGzip(cls, data, osFile, indent=4):
        if data:
            tempFile = cls.getOsTemporaryFile(osFile)
            #
            osFileBasename = cls.getOsFileBasename(osFile)
            # noinspection PyArgumentEqualDefault
            with gzip.GzipFile(filename=osFileBasename, mode='wb', compresslevel=9, fileobj=open(tempFile, 'wb')) as g:
                # noinspection PyArgumentEqualDefault
                json.dump(data, g, ensure_ascii=True, indent=indent)
                #
                g.close()
            #
            cls.setOsFileCopy(tempFile, osFile)
    @classmethod
    def getOsFilesByPath(cls, osPath):
        lis = []
        data = cls.getOsFileBasenameLisByPath(osPath)
        if data:
            for osFileBasename in data:
                osFile = cls._toOsFile(osPath, osFileBasename)
                lis.append(osFile)
        return lis
    @classmethod
    def getOsFileLisFilter(cls, filePath, filterExt, useRelative=False):
        # Sub Method
        def getBranch(osPath):
            osFiles = cls.getOsFilesByPath(osPath)
            for i in osFiles:
                if cls.isOsFile(i):
                    ext = cls.getOsFileExt(i)
                    if ext.lower() in filterExtLis:
                        if useRelative:
                            i = i[len(filePath) + 1:]
                        lis.append(i)
                elif cls.isOsPath(i):
                    getBranch(i)
        #
        lis = []
        filterExtLis = cls._toStringList(filterExt)
        getBranch(filePath)
        if lis:
            lis.sort()
        return lis


#
class LxDbMethodBasic(LxOsFileMethodBasic, appConfig.LxDbConfig):
    @classmethod
    def _lxDbInfoDic(cls, description=None, note=None):
        return orderedDict(
            [
                (cls.Lynxi_Key_Info_Update, cls.getOsActiveTimestamp()),
                (cls.Lynxi_Key_Info_Artist, cls.getOsUser()),
                #
                (cls.Lynxi_Key_Info_Host, cls.getOsHost()),
                (cls.Lynxi_Key_Info_HostName, cls.getOsHostName()),
                #
                (cls.Lynxi_Key_Info_Description, description),
                (cls.Lynxi_Key_Info_Note, note)
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
        return cls._toOsPath(
            [
                cls.DbRoot_Basic, cls.LxDb_Folder_Basic
            ]
        )
    @classmethod
    def _lxDbUnitDirectory(cls, dbClass):
        return cls._toOsPath(
            [
                cls._lxDbDirectory(),
                dbClass + cls.LxDb_Folder_Unit
            ]
        )
    @classmethod
    def _lxDbDatumDirectory(cls, dbClass):
        return cls._toOsPath(
            [
                cls._lxDbDirectory(),
                dbClass + cls.LxDb_Folder_Datum
            ]
        )
    @classmethod
    def _lxDbFileDirectory(cls, dbClass):
        return cls._toOsPath(
            [
                cls._lxDbDirectory(),
                dbClass + cls.LxDb_Folder_File
            ]
        )
    @classmethod
    def lxDbUnitIndexFile(cls, dbClass, dbUnitType):
        return cls._toOsPath(
            [
                cls._lxDbUnitDirectory(dbClass),
                dbUnitType + cls.LxDb_Ext_Index,
            ]
        )
    # Unit Branch File
    @classmethod
    def lxDbUnitBranchFile(cls, dbClass, dbUnitType, dbUnitId):
        return cls._toOsPath(
            [
                cls._lxDbUnitDirectory(dbClass),
                dbUnitType, dbUnitId + cls.LxDb_Ext_Unit_Include_Branch
            ]
        )
    # Unit Definition File
    @classmethod
    def _lxDbUnitDefinitionFile(cls, dbClass, dbUnitType, dbUnitId):
        return cls._toOsPath(
            [
                cls._lxDbUnitDirectory(dbClass),
                dbUnitType, dbUnitId + cls.LxDb_Ext_Unit_Include_Definition
            ]
        )
    @classmethod
    def _lxDbUnitIncludeFile(cls, dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId):
        return cls._toOsPath(
            [
                cls._lxDbUnitDirectory(dbClass),
                dbUnitType, dbUnitBranch, dbUnitId + cls.LxDb_Ext_Unit_Include_Dic[dbUnitIncludeType]
            ]
        )
    # Unit Include Version File
    @classmethod
    def _lxDbUnitIncludeVersionFile(cls, dbUnitIncludeFile):
        base, ext = cls.toOsFileSplitByExt(dbUnitIncludeFile)
        return base + cls.LxDb_Ext_Version
    @classmethod
    def _lxDbUnitIncludeInfoFile(cls, dbUnitIncludeFile):
        base, ext = cls.toOsFileSplitByExt(dbUnitIncludeFile)
        return base + cls.LxDb_Ext_Unit_Include_Info
    # Json Datum File
    @classmethod
    def lxDbJsonDatumFile(cls, dbClass, dbDatumType, dbDatumId):
        return cls._toOsPath(
            [
                cls._lxDbDatumDirectory(dbClass),
                dbDatumType, dbDatumId + cls.LxDb_Ext_Json
            ]
        )
    @classmethod
    def lxDbDatumInfoFile(cls, datumFile):
        base, ext = cls.toOsFileSplitByExt(datumFile)
        return base + cls.LxDb_Ext_Info
    @classmethod
    def _lxDbOsUnitDatumFile(cls, dbClass, dbDatumType, dbDatumId, ext):
        return cls._toOsPath(
            [
                cls._lxDbDatumDirectory(dbClass),
                dbDatumType, dbDatumId + ext
            ]
        )
    @classmethod
    def _lxDbOsDatumUnitVersionFile(cls, dbClass, dbDatumType, dbDatumUnitId):
        return cls._toOsPath(
            [
                cls._lxDbFileDirectory(dbClass),
                dbDatumType, dbDatumUnitId + cls.LxDb_Ext_Version
            ]
        )
    @classmethod
    def _lxDbOsDatumUnitInfoFile(cls, dbClass, dbDatumType, dbDatumUnitId):
        return cls._toOsPath(
            [
                cls._lxDbFileDirectory(dbClass),
                dbDatumType, dbDatumUnitId + cls.LxDb_Ext_Info
            ]
        )
    # Unit Index ( Update )
    @classmethod
    def _lxDbUpdateUnitIndexSub(cls, dbClass, dbUnitType, dbUnitId):
        dbUnitIndexFile = cls.lxDbUnitIndexFile(dbClass, dbUnitType)
        if cls.isOsExistsFile(dbUnitIndexFile):
            dbUnitIdLis = cls.readOsJson(dbUnitIndexFile)
            if not dbUnitId in dbUnitIdLis:
                dbUnitIdLis += [dbUnitId]
                cls.writeOsJson(dbUnitIdLis, dbUnitIndexFile)
                cls.traceResult(
                    'Update Unit(s) Index File ( {} )'.format(dbUnitIndexFile)
                )
                cls.traceResult(
                    'Add Unit ( {} > {} > {} )'.format(dbClass, dbUnitType, dbUnitId)
                )
        else:
            cls.writeOsJson([dbUnitId], dbUnitIndexFile)
            cls.traceResult(
                'Add Unit(s) Index File ( {} )'.format(dbUnitIndexFile)
            )
    # Unit Branch ( Update )
    @classmethod
    def _lxDbUpdateUnitBranchFileSub(cls, dbClass, dbUnitType, dbUnitBranch, dbUnitId):
        # Branch
        if dbUnitBranch is None:
            dbUnitBranch = cls.LxDb_Include_Branch_Main
        #
        dbUnitBranchFile = cls.lxDbUnitBranchFile(
            dbClass,
            dbUnitType, dbUnitId
        )
        data = cls.readOsJson(dbUnitBranchFile)
        if data:
            if not dbUnitBranch in data:
                data.append(dbUnitBranch)
                cls.writeOsJson(
                    data, dbUnitBranchFile
                )
                cls.traceResult(
                    'Update Unit Branch File ( {} )'.format(dbUnitBranchFile)
                )
                cls.traceResult(
                    'Add Unit ( {} > {} > {} ) Branch ( {} )'.format(dbClass, dbUnitType, dbUnitId, dbUnitBranch)
                )
        else:
            cls.writeOsJson(
                [dbUnitBranch], dbUnitBranchFile
            )
            cls.traceResult(
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
        cls.writeOsJson(
            dbDefinitionDatum, dbUnitDefinitionFile
        )
    # Include File
    @classmethod
    def _lxDbUpdateUnitIncludeSub(cls, dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId, dbDatumType, dbDatumId, note=None):
        dbUnitIncludeFile = cls._lxDbUnitIncludeFile(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
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
    @classmethod
    def _lxDbUpdateUnitIncludeFileSub(cls, dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId, dbUnitIncludeIndex, note=None):
        dbUnitIncludeFile = cls._lxDbUnitIncludeFile(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
        jsonDatum = cls.readOsJson(dbUnitIncludeFile)
        if jsonDatum:
            if not jsonDatum == dbUnitIncludeIndex:
                cls.writeOsJson(
                    dbUnitIncludeIndex, dbUnitIncludeFile
                )
        else:
            cls.writeOsJson(
                dbUnitIncludeIndex, dbUnitIncludeFile
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
        if cls.isOsExistsFile(dbUnitIncludeVersionFile):
            dbUnitIncludeVersionLis = cls.readOsJson(dbUnitIncludeVersionFile)
            dbUnitIncludeInfoLis = cls.readOsJson(dbUnitIncludeInfoFile)
            if not dbUnitIncludeIndex in dbUnitIncludeVersionLis:
                dbUnitIncludeVersionLis.append(dbUnitIncludeIndex)
                dbUnitIncludeInfoLis.append(dbIncludeInfo)
                cls.writeOsJson(
                    dbUnitIncludeVersionLis,
                    dbUnitIncludeVersionFile
                )
                cls.writeOsJson(
                    dbUnitIncludeInfoLis,
                    dbUnitIncludeInfoFile
                )
        else:
            cls.writeOsJson(
                [dbUnitIncludeIndex],
                dbUnitIncludeVersionFile
            )
            cls.writeOsJson(
                [dbIncludeInfo],
                dbUnitIncludeInfoFile
            )
    # Unit Include Datum ( Update )
    @classmethod
    def _lxDbUpdateUnitIncludeDatumSub(cls, dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitIncludeDatum, dbUnitId, dbDatumType, note):
        dbDatumId = cls.getDataHashString(dbUnitIncludeDatum)
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
        dbDatumFile = cls.lxDbJsonDatumFile(dbClass, dbDatumType, dbDatumId)
        if not cls.isOsExistsFile(dbDatumFile):
            # Datum
            if dbDatumType == cls.LxDb_Type_Datum_Json:
                cls.writeOsJson(
                    datum, dbDatumFile
                )
            else:
                cls.writeOsData(
                    datum, dbDatumFile
                )
            # Info
            dbDatumInfoFile = cls.lxDbDatumInfoFile(dbDatumFile)
            cls.writeOsJson(
                cls._lxDbInfoDic(description, note),
                dbDatumInfoFile
            )
            #
            cls.traceResult(
                'Add Os Datum File ( {} )'.format(dbDatumFile)
            )
    # Os Datum File
    @classmethod
    def _lxDbUpdateOsFileDatumSub(cls, osFile, dbClass, dbDatumType, dbDatumUnitId, dbDatumId, description, note):
        ext = cls.getOsFileExt(osFile)
        #
        dbOsUnitDatumFile = cls._lxDbOsUnitDatumFile(dbClass, dbDatumType, dbDatumId, ext)
        if not cls.isOsExistsFile(dbOsUnitDatumFile):
            # Datum File
            cls.setOsFileCopy(osFile, dbOsUnitDatumFile)
            # Version and Info File
            dbOsDatumUnitVersionFile = cls._lxDbOsDatumUnitVersionFile(dbClass, dbDatumType, dbDatumUnitId)
            dbOsDatumUnitInfoFile = cls._lxDbOsDatumUnitInfoFile(dbClass, dbDatumType, dbDatumUnitId)
            #
            dbOsUnitIndex = cls._lxDbOsUnitDatumIndex(dbDatumType, dbDatumId)
            dbOsUnitInfo = cls._lxDbInfoDic(description, note)
            if cls.isOsExistsFile(dbOsDatumUnitVersionFile):
                dbOsUnitVersionLis = cls.readOsJson(dbOsDatumUnitVersionFile)
                dbOsUnitInfoLis = cls.readOsJson(dbOsDatumUnitInfoFile)
                #
                dbOsUnitVersionLis.append(dbOsUnitIndex)
                dbOsUnitInfoLis.append(dbOsUnitInfo)
                #
                cls.writeOsJson(
                    dbOsUnitVersionLis,
                    dbOsDatumUnitVersionFile
                )
                cls.writeOsJson(
                    dbOsUnitInfoLis,
                    dbOsDatumUnitInfoFile
                )
            else:
                cls.writeOsJson(
                    [dbOsUnitIndex],
                    dbOsDatumUnitVersionFile
                )
                cls.writeOsJson(
                    [dbOsUnitInfo],
                    dbOsDatumUnitInfoFile
                )
            #
            cls.traceResult(
                'Add Os Datum File ( {} > {} )'.format(osFile, dbOsUnitDatumFile)
            )
    @classmethod
    def _lxDbOsUnitDefDatum(cls, enable, nameString, osPath):
        return {
            cls.LxDb_Key_Enable: enable,
            cls.LxDb_Key_Name: nameString,
            cls.LxDb_Key_Source: osPath
        }
    @classmethod
    def _lxDbOsFileUnitDefDatum(cls, osFile):
        return {
            cls.LxDb_Key_Source: osFile
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
        if cls.isOsExistsFile(dbUnitIncludeFile):
            dbUnitIncludeIndex = cls.readOsJson(dbUnitIncludeFile)
            #
            dbDatumType, dbDatumId = eval(dbUnitIncludeIndex)
            return cls._lxDbLoadJsonDatumFileSub(
                dbClass,
                dbDatumType, dbDatumId
            )
    @classmethod
    def _lxDbLoadJsonDatumFileSub(cls, dbClass, dbDatumType, dbDatumId):
        dbDatumFile = cls.lxDbJsonDatumFile(dbClass, dbDatumType, dbDatumId)
        if cls.isOsExistsFile(dbDatumFile):
            if dbDatumType == cls.LxDb_Type_Datum_Json:
                return cls.readOsJson(dbDatumFile)
            else:
                return cls.readOsData(dbDatumFile)
    # Unit Index ( Get )
    @classmethod
    def _lxDbGetUnitIdLis(cls, dbClass, dbUnitType):
        dbUnitIndexFile = cls.lxDbUnitIndexFile(dbClass, dbUnitType)
        return cls.readOsJson(dbUnitIndexFile) or []
    @classmethod
    def _lxDbGetUnitDefinition(cls, dbClass, dbUnitType, dbUnitId):
        dbUnitDefinitionFile = cls._lxDbUnitDefinitionFile(
            dbClass,
            dbUnitType, dbUnitId
        )
        #
        return cls.readOsJson(dbUnitDefinitionFile) or {}
    # Unit Branch ( Get )
    @classmethod
    def _lxDbGetUnitBranchLis(cls, dbClass, dbUnitType, dbUnitId):
        dbUnitBranchFile = cls.lxDbUnitBranchFile(
            dbClass,
            dbUnitType, dbUnitId
        )
        if cls.isOsExistsFile(dbUnitBranchFile):
            return cls.readOsJson(dbUnitBranchFile)
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
        if cls.isOsExistsFile(dbUnitIncludeFile):
            currentData = cls.readOsJson(dbUnitIncludeFile)
            dbUnitIncludeVersionFile = cls._lxDbUnitIncludeVersionFile(dbUnitIncludeFile)
            data = cls.readOsJson(dbUnitIncludeVersionFile)
            if data:
                currentIndex = data.index(currentData)
                lis = data
        return lis, currentIndex
    @classmethod
    def _lxDbGetUnitIncludeVersionUiDic(cls, dbClass, dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId):
        dic = cls.orderedDict()
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
        dic = cls.orderedDict()
        dbUnitIdLis = cls._lxDbGetUnitIdLis(dbClass, dbUnitType)
        if dbUnitIdLis:
            for dbUnitId in dbUnitIdLis:
                dbUnitDefinitionFile = cls._lxDbUnitDefinitionFile(
                    dbClass,
                    dbUnitType, dbUnitId
                )
                data = cls.readOsJson(dbUnitDefinitionFile)
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
                data = cls.readOsJson(dbUnitDefinitionFile)
                if data:
                    name = data.get(cls.LxDb_Key_Name, 'N/a')
                    lis.append(name)
        return lis
    # Json Unit
    @classmethod
    def _lxDbUpdateJsonUnit(cls, nameString, jsonDatum, dbClass, dbUnitType, dbUnitBranch=None, note=None):
        dbUnitId = cls.getUniqueId(nameString)
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
        dbUnitId = cls.getUniqueId(nameString)
        dbUnitIncludeType = cls.LxDb_Type_Unit_Include_Raw
        #
        return cls._lxDbLoadUnitIncludeSub(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
    @classmethod
    def _lxDbGetJsonUnitBranchLis(cls, nameString, dbClass, dbUnitType):
        dbUnitId = cls.getUniqueId(nameString)
        return cls._lxDbGetUnitBranchLis(
            dbClass,
            dbUnitType, dbUnitId
        )
    @classmethod
    def _lxDbGetJsonUnitIncludeVersionLis(cls, nameString, dbClass, dbUnitType, dbUnitBranch):
        dbUnitIncludeType = cls.LxDb_Type_Unit_Include_Raw
        dbUnitId = cls.getUniqueId(nameString)
        return cls._lxDbGetUnitIncludeVersionLis(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
    @classmethod
    def _lxDbGetJsonUnitIncludeVersionUiDic(cls, nameString, dbClass, dbUnitType, dbUnitBranch):
        dbUnitIncludeType = cls.LxDb_Type_Unit_Include_Raw
        dbUnitId = cls.getUniqueId(nameString)
        return cls._lxDbGetUnitIncludeVersionUiDic(
            dbClass,
            dbUnitType, dbUnitIncludeType, dbUnitBranch, dbUnitId
        )
    @classmethod
    def lxAddDatabaseLog(cls, string):
        cls.setLogAdd(string, cls.LynxiLogType_Database)
    @classmethod
    def traceResult(cls, string):
        cls.traceMessage(
            u'//Lynxi Database Result : {}//'.format(string)
        )
        cls.lxAddDatabaseLog(string)


#
class LxProductMethodBasic(appConfig.LxProductConfig):
    pass


#
class LxUpdateMethod(LxMethodBasic):
    @classmethod
    def _getPythonModuleLisMethod(cls, modulePath, moduleLimitStrings=None):
        def getBranch(directory, keywordFilterString=None):
            osFileBasenameLis = cls.getOsFileBasenameLisByPath(directory)
            if osFileBasenameLis:
                keywordFilterStringLis = cls._toStringList(keywordFilterString)
                # Filter
                if keywordFilterString:
                    osFileBasenameLis = [i for i in osFileBasenameLis if i in keywordFilterStringLis] + ['__init__' + ext]
                #
                if '__init__' + ext in osFileBasenameLis:
                    for osFileBasename in osFileBasenameLis:
                        osFile = cls._toOsFile(directory, osFileBasename)
                        if osFile.endswith(ext):
                            timestamp = cls.getOsFileMtimestamp(osFile)
                            pythonModule = osFile[len(modulePath) + 1:-len(ext)].replace('/', '.')
                            timeLis.append(timestamp)
                            moduleDic[timestamp] = pythonModule
                        #
                        getBranch(osFile)
        #
        def getMain():
            getBranch(modulePath, moduleLimitStrings)
            #
            if timeLis:
                timeLis.sort()
                timeLis.reverse()
                for i in timeLis:
                    module = moduleDic[i]
                    if not module.endswith('__init__'):
                        lis.append(module)
        #
        ext = '.py'
        #
        lis = []
        #
        timeLis = []
        moduleDic = {}
        #
        getMain()
        #
        return lis
    @classmethod
    def setPythonModuleUpdate(cls, modulePath, moduleLimitStrings=None):
        moduleLis = cls._getPythonModuleLisMethod(modulePath, moduleLimitStrings)
        if moduleLis:
            for module in moduleLis:
                stringLis = module.split('.')
                #
                modulePath = '.'.join(stringLis[:-1])
                moduleName = stringLis[-1]
                #
                command = '''from {0} import {1}\r\nreload({1})'''.format(modulePath, moduleName)
                exec command


#
class LxDebugMethod(LxMethodBasic):
    @classmethod
    def viewTimeMethod(cls, func):
        def subFunc(*args, **kwargs):
            startTime = cls.getOsActiveTimestamp()
            traceMessage = 'Start [ %s ] in %s' % (func.__name__, (cls.getOsActiveViewTime()))
            cls.addLynxiLog_function(traceMessage)
            #
            subFn = func(*args, **kwargs)
            #
            endTime = cls.getOsActiveTimestamp()
            traceMessage = 'Call [ %s ] in %fs' % (func.__name__, (endTime - startTime))
            cls.addLynxiLog_function(traceMessage)
            return subFn
        return subFunc
    @classmethod
    def viewExceptionMethod(cls, func):
        def subFunc(*args, **kw):
            # noinspection PyBroadException
            try:
                _connectObject = func(*args, **kw)
                return _connectObject
            except Exception:
                functionName = func.__name__
                exceptionString = cls.toExceptionString()
                message = functionName + '(%s) is Error ' % ', '.join(func.__code__.co_varnames) + exceptionString.split('func(*args, **kw)')[-1]
                return cls.setLogAdd(message, cls.LynxiLogType_Exception)
        return subFunc
