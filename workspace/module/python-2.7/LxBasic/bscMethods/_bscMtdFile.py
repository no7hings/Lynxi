# coding:utf-8
from LxBasic import bscMtdCore


class _FileBasic(bscMtdCore.Mtd_BscBasic):
    @classmethod
    def isExist(cls, fileString):
        return bscMtdCore.Mtd_BscUtility._isOsFileExist(fileString)

    @classmethod
    def createDirectory(cls, fileString):
        bscMtdCore.Mtd_BscUtility._bsc_mtd__os_path__set_file_directory_create_(fileString)

    @classmethod
    def name(cls, fileString):
        return bscMtdCore.Mtd_BscUtility._getOsFileName(fileString)

    @classmethod
    def dirname(cls, fileString):
        return bscMtdCore.Mtd_BscUtility._getOsFileDirname(fileString)

    @classmethod
    def basename(cls, fileString):
        return bscMtdCore.Mtd_BscUtility._getOsFileBasename(fileString)

    @classmethod
    def base(cls, fileString):
        return bscMtdCore.Mtd_BscUtility._getOsFileBase(fileString)

    @classmethod
    def ext(cls, fileString):
        return cls.MTD_os_path.splitext(fileString)[1]

    @classmethod
    def isSame(cls, fileString, targetFileString):
        return bscMtdCore.Mtd_BscUtility._isOsSameFile(fileString, targetFileString)

    @classmethod
    def copyTo(cls, fileString, targetFileString, force=True):
        if cls.isExist(fileString):
            bscMtdCore.Mtd_BscUtility._setOsFileCopy(fileString, targetFileString, force)

    @classmethod
    def backupTo(cls, fileString, backupFileString, timetag=None):
        if cls.isExist(fileString):
            bscMtdCore.Mtd_BscUtility._setOsFileBackup(fileString, backupFileString, timetag)

    @classmethod
    def renameDirnameTo(cls, fileString, newDirnameString):
        basenameString = cls.basename(fileString)
        targetTexture = bscMtdCore.Mtd_BscUtility._toOsFilename(newDirnameString, basenameString)
        return targetTexture

    @classmethod
    def renameBasenameTo(cls, fileString, newBasenameString):
        bscMtdCore.Mtd_BscUtility._setOsFileRename(fileString, newBasenameString)

    @classmethod
    def renameTo(cls, fileString, newFileString):
        bscMtdCore.Mtd_BscUtility._setOsFileRename_(fileString, newFileString)

    @classmethod
    def renameExtTo(cls, fileString, extString):
        return cls.base(fileString) + extString

    @classmethod
    def remove(cls, fileString):
        bscMtdCore.Mtd_BscUtility._setOsPathRemove(fileString)

    @classmethod
    def open(cls, fileString):
        bscMtdCore.Mtd_BscUtility._setOsFileOpen(fileString)

    @classmethod
    def moveTo(cls, fileString, targetFileString):
        bscMtdCore.Mtd_BscUtility._setOsFileMove(fileString, targetFileString)

    @classmethod
    def openDirectory(cls, fileString):
        if bscMtdCore.Mtd_BscUtility._isOsFileExist(fileString):
            directoryString = bscMtdCore.Mtd_BscUtility._getOsFileDirname(fileString)
            bscMtdCore.Mtd_BscUtility._setOsDirectoryOpen(directoryString)

    @classmethod
    def openAsTemporary(cls, fileString, temporaryFileString):
        if bscMtdCore.Mtd_BscUtility._isOsFileExist(fileString):
            timestamp = str(bscMtdCore.Mtd_BscUtility._getOsFileMtimestamp(fileString))
            if bscMtdCore.Mtd_BscUtility._isOsFileExist(temporaryFileString):
                tempTimestamp = str(bscMtdCore.Mtd_BscUtility._getOsFileMtimestamp(temporaryFileString))
            else:
                tempTimestamp = None

            if not timestamp == tempTimestamp:
                bscMtdCore.Mtd_BscUtility._setOsFileCopy(fileString, temporaryFileString)
            #
            bscMtdCore.Mtd_BscUtility._setOsFileOpen(temporaryFileString)

    @classmethod
    def openAsBackup(cls, fileString):
        pass

    @classmethod
    def isFileTimeChanged(cls, fileString, targetFileString):
        return bscMtdCore.Mtd_BscUtility._isOsFileTimeChanged(fileString, targetFileString)

    @classmethod
    def mtimestamp(cls, fileString):
        return bscMtdCore.Mtd_BscUtility._getOsFileMtimestamp(fileString)

    @classmethod
    def mtimetag(cls, fileString):
        return bscMtdCore.Mtd_BscUtility._getOsFileMtimetag(fileString)

    @classmethod
    def mtimeChnPrettify(cls, fileString, useMode=0):
        return bscMtdCore.Mtd_BscUtility._timestampToChnPrettify(bscMtdCore.Mtd_BscUtility._getOsFileMtimestamp(fileString), useMode)

    @classmethod
    def temporaryName(cls, fileString, timetag=None):
        return bscMtdCore.Mtd_BscUtility._getOsFileTemporaryName(fileString, timetag)

    @classmethod
    def temporaryVedioName(cls, fileString):
        tempDirectory = u'{}/vedio'.format(cls.DEF_path_temporary_local)
        basenameString = bscMtdCore.Mtd_BscUtility._getOsFileBasename(fileString)
        return bscMtdCore.Mtd_BscUtility._toOsFilename(tempDirectory, basenameString)

    @classmethod
    def backupName(cls, fileString, timetag=None, useMode=0):
        return bscMtdCore.Mtd_BscUtility._toOsFileJoinTimetag(fileString, timetag, useMode)

    @classmethod
    def uniqueName(cls, fileString):
        directoryString = bscMtdCore.Mtd_BscUtility._getOsFileDirname(fileString)
        uniqueId = bscMtdCore.Mtd_BscUtility._stringToUniqueId(bscMtdCore.Mtd_BscUtility._getOsFileBasename(fileString))
        return bscMtdCore.Mtd_BscUtility._toOsFilename(directoryString, uniqueId)

    @classmethod
    def infoJsonName(cls, fileString):
        return bscMtdCore.Mtd_BscUtility._toOsFileInfoJsonFileString(fileString)

    @classmethod
    def resultName(cls, fileString):
        return bscMtdCore.Mtd_BscUtility._toOsFileResultFileString(fileString)

    @classmethod
    def backupNameDict(cls, fileString):
        return bscMtdCore.Mtd_BscUtility._getOsFileBackupNameDict(fileString)

    @classmethod
    def toJoinTimetag(cls, fileString, timetag=None, useMode=0):
        return bscMtdCore.Mtd_BscUtility._toOsFileJoinTimetag(fileString, timetag, useMode)

    @classmethod
    def findTimetag(cls, fileString):
        return bscMtdCore.Mtd_BscUtility._getOsFileTimetag(fileString)

    @classmethod
    def infoDict(cls, fileString):
        return bscMtdCore.Mtd_BscUtility._infoDict(fileString)

    @classmethod
    def productInfoDict(cls, fileString, stage=None, description=None, note=None):
        dic = bscMtdCore.Mtd_BscUtility._infoDict(fileString)
        dic[cls.DEF_key_stage] = stage
        dic[cls.DEF_key_description] = description
        dic[cls.DEF_key_note] = note
        return dic

    @classmethod
    def size(cls, fileString):
        return bscMtdCore.Mtd_BscUtility._getOsFileSize(fileString)

    @classmethod
    def seqLabel(cls, seq):
        return ['', '_' + str(seq).zfill(4)][seq > 0]

    @classmethod
    def subFilename(cls, fileString, labelString):
        return labelString.join(cls.MTD_os_path.splitext(fileString))

    @classmethod
    def reduceFilename(cls, fileString):
        pathsep = cls.DEF_bsc__python__pathsep
        return cls.MOD_re.sub(
            r'{0}|{1}'.format(pathsep*2, pathsep*3),
            pathsep, fileString
        )

    @classmethod
    def toExtSplit(cls, fileString):
        return cls.MTD_os_path.splitext(fileString)

    @classmethod
    def raw2hash(cls, fileString):
        bscMtdCore.Mtd_BscUtility._getOsFileHash(fileString)

    @classmethod
    def collectionDatum(cls, fileString, targetDirectoryString, ignoreMtimeChanged=False, ignoreExists=False):
        def getBranch(sourceFileString):
            targetFileString = cls.renameDirnameTo(sourceFileString, targetDirectoryString)
            #
            enable = False
            if cls.isExist(targetFileString):
                if ignoreExists is True:
                    enable = False
                else:
                    if ignoreMtimeChanged is True:
                        enable = True
                    else:
                        isMtimeChanged = bscMtdCore.Mtd_BscUtility._isOsFileTimeChanged(sourceFileString, targetFileString)
                        if isMtimeChanged:
                            enable = True
            else:
                enable = True
            #
            if enable is True:
                lis.append((sourceFileString, targetFileString))

        #
        lis = []
        #
        osFileLis = bscMtdCore.Mtd_BscUtility._string2list(fileString)
        if osFileLis:
            [getBranch(i) for i in osFileLis]
        return lis

    @classmethod
    def composeBy(cls, directoryString, basenameString):
        return bscMtdCore.Mtd_BscUtility._toOsFilename(directoryString, basenameString)

    @classmethod
    def _getOsFileInfoDic(cls, osSourceFile, description=None, note=None):
        return bscMtdCore.orderedDict(
            [
                (cls.DEF_key_info_timestamp, bscMtdCore.Mtd_BscUtility._getSystemActiveTimestamp()),
                (cls.DEF_key_info_username, bscMtdCore.Mtd_BscUtility._getSystemUsername()),
                #
                (cls.DEF_key_info_host, bscMtdCore.Mtd_BscUtility._getSystemHost()),
                (cls.DEF_key_info_hostname, bscMtdCore.Mtd_BscUtility._getSystemHostname()),
                #
                (cls.DEF_key_info_sourcefile, osSourceFile),
                #
                (cls.DEF_key_info_description, description),
                (cls.DEF_key_info_note, note)
            ]
        )

    @classmethod
    def _getOsFileBackupDatum(cls, fileString):
        hashKey = bscMtdCore.Mtd_BscUtility._getOsFileHash(fileString)
        dirname, filename, ext = bscMtdCore.Mtd_BscUtility._getOsFileDirname(fileString), bscMtdCore.Mtd_BscUtility._getOsFileName(fileString), bscMtdCore.Mtd_BscUtility._getOsFileExt(
            fileString)
        #
        targetFileString = cls.DEF_bsc__os__pathsep.join(
            [bscMtdCore.Mtd_BscUtility._getOsFileDirname(fileString), cls.LynxiOsFolder_History, filename + ext, hashKey])
        osVersionFile = cls.DEF_bsc__os__pathsep.join(
            [bscMtdCore.Mtd_BscUtility._getOsFileDirname(fileString), cls.LynxiOsFolder_History, filename + cls.LynxiOsExtVAR_kit__window__version])
        return targetFileString, osVersionFile

    @classmethod
    def _setOsFileBackupTo(cls, sourceFileString, targetFileString):
        bscMtdCore.Mtd_BscUtility._setOsFileCopy(sourceFileString, targetFileString)
        #
        info = cls._getOsFileInfoDic(sourceFileString)
        infoFile = bscMtdCore.Mtd_BscUtility._toOsFileInfoJsonFileString(targetFileString)
        bscMtdCore.Mtd_BscUtility._setOsJsonWrite(infoFile, info)

    @classmethod
    def backup(cls, fileString):
        if bscMtdCore.Mtd_BscUtility._isOsFileExist(fileString):
            targetFileString, osVersionFile = cls._getOsFileBackupDatum(fileString)
            if not bscMtdCore.Mtd_BscUtility._isOsFileExist(targetFileString):
                cls._setOsFileBackupTo(fileString, targetFileString)
            #
            bscMtdCore.Mtd_BscUtility._setOsJsonWrite(
                osVersionFile,
                {
                    bscMtdCore.Mtd_BscUtility._getSystemActiveTimestamp(): bscMtdCore.Mtd_BscUtility._getOsFileBasename(targetFileString)
                }
            )


class OsFile(_FileBasic):
    @classmethod
    def write(cls, fileString, raw):
        bscMtdCore.Mtd_BscUtility._bsc_mtd__os_path__set_file_directory_create_(fileString)
        with open(fileString, u'wb') as f:
            if isinstance(raw, (str, unicode)):
                f.write(raw)
            elif isinstance(raw, (tuple, list)):
                f.writelines(raw)

            f.close()

    @classmethod
    def read(cls, fileString):
        if bscMtdCore.Mtd_BscUtility._isOsFileExist(fileString):
            with open(fileString, u'rb') as f:
                raw = f.read()
                f.close()
                return raw

    @classmethod
    def readlines(cls, fileString):
        if bscMtdCore.Mtd_BscUtility._isOsFileExist(fileString):
            with open(fileString, u'rb') as f:
                raw = f.readlines()
                f.close()
                return raw


class OsFileGzip(_FileBasic):
    @classmethod
    def write(cls, fileString, raw):
        bscMtdCore.Mtd_BscUtility._bsc_mtd__os_path__set_file_directory_create_(fileString)
        #
        osFileBasename = bscMtdCore.Mtd_BscUtility._getOsFileBasename(fileString)
        #
        with cls.MOD_gzip.GzipFile(
                filename=osFileBasename,
                mode=u'wb',
                compresslevel=9,
                fileobj=open(fileString, u'wb')
        ) as g:
            g.write(raw)
            g.close()

    @classmethod
    def read(cls, fileString):
        if bscMtdCore.Mtd_BscUtility._isOsFileExist(fileString):
            with cls.MOD_gzip.GzipFile(
                    mode=u'rb',
                    fileobj=open(fileString, u'rb')
            ) as g:
                raw = g.read()
                g.close()
                return raw

    @classmethod
    def readlines(cls, fileString):
        if bscMtdCore.Mtd_BscUtility._isOsFileExist(fileString):
            with cls.MOD_gzip.GzipFile(
                    mode=u'rb',
                    fileobj=open(fileString, u'rb')
            ) as g:
                raw = g.readlines()
                g.close()
                return raw


class OsJsonFile(_FileBasic):
    @classmethod
    def read(cls, fileString, encoding=None):
        if cls.MTD_os_path.isfile(fileString):
            with open(fileString) as j:
                raw = cls.MOD_json.load(j, encoding=encoding)
                j.close()
                return raw

    @classmethod
    def write(cls, fileString, raw, indent=4, ensure_ascii=True):
        bscMtdCore.Mtd_BscUtility._setOsJsonWrite(
            fileString,
            raw,
            indent,
            ensure_ascii
        )

    @classmethod
    def getValue(cls, fileString, key, failobj=None):
        raw = cls.read(fileString)
        if raw:
            if isinstance(raw, dict):
                return raw.get(key, failobj)

    @classmethod
    def setValue(cls, fileString, dic):
        if bscMtdCore.Mtd_BscUtility._isOsFileExist(fileString):
            dic_ = cls.read(fileString)
        else:
            dic_ = {}

        for k, v in dic.items():
            dic_[k] = v
        #
        cls.write(fileString, dic)

    @classmethod
    def load(cls, raw):
        return cls.MOD_json.loads(raw)

    @classmethod
    def dump(cls, raw):
        return cls.MOD_json.dumps(raw)


class OsJsonGzip(_FileBasic):
    @classmethod
    def read(cls, fileString, encoding=None):
        if bscMtdCore.Mtd_BscUtility._isOsFileExist(fileString):
            with cls.MOD_gzip.GzipFile(
                    mode=u'rb',
                    fileobj=open(fileString, u'rb')
            ) as g:
                raw = cls.MOD_json.load(g, encoding=encoding)
                g.close()
                return raw

    @classmethod
    def write(cls, fileString, raw, indent=4, ensure_ascii=True):
        temporaryName = bscMtdCore.Mtd_BscUtility._getOsFileTemporaryName(fileString)
        with cls.MOD_gzip.GzipFile(
                filename=bscMtdCore.Mtd_BscUtility._getOsFileBasename(fileString),
                mode=u'wb',
                compresslevel=9,
                fileobj=open(temporaryName, u'wb')
        ) as g:
            cls.MOD_json.dump(
                raw,
                g,
                indent=indent,
                ensure_ascii=ensure_ascii
            )
            #
            g.close()
        #
        bscMtdCore.Mtd_BscUtility._setOsFileCopy(temporaryName, fileString)


class OsImage(_FileBasic):
    module_fullpath_name = 'PIL.Image'
    @classmethod
    def _toPImage(cls, fileString):
        module = bscMtdCore.Mtd_BscUtility._bsc_mtd__set_python_module_load_(cls.module_fullpath_name)
        if module:
            if bscMtdCore.Mtd_BscUtility._isOsFileExist(fileString):
                return module.open(fileString)

    @classmethod
    def pixelSize(cls, fileString):
        size = 0, 0
        # noinspection PyBroadException
        try:
            pImage = cls._toPImage(fileString)
            if pImage is not None:
                return pImage.size
        except:
            pass
        return size


class OsMultifile(bscMtdCore.Mtd_BscBasic):
    DEF_placeholder_multifile_list = ['<udim>', '%04d', '<f>', '####']
    VAR_padding_multifile = 4

    @classmethod
    def _getOsFileFrame(cls, fileString, paddingValue):
        lis = cls.MOD_re.findall(
            '[0-9]'*paddingValue,
            bscMtdCore.Mtd_BscUtility._getOsFileBasename(fileString)
        )
        if lis:
            return int(lis[0])

    @classmethod
    def _getOsMultifileFileList(cls, fileString, frameRange, placeholderString, paddingValue):
        lis = []

        if placeholderString.lower() in fileString.lower():
            startFrame, endFrame = frameRange

            index = fileString.lower().index(placeholderString.lower())
            a, b = fileString[:index], fileString[index + len(placeholderString):]
            for i in xrange(endFrame - startFrame + 1):
                subFileString = (a + str(i + startFrame).zfill(paddingValue) + b).replace('\\', cls.DEF_bsc__os__pathsep)
                lis.append(subFileString)
        return lis

    @classmethod
    def _getOsMultifileExistFileList(cls, fileString, placeholderString, paddingValue):
        lis = []

        if placeholderString.lower() in fileString.lower():
            index = fileString.lower().index(placeholderString.lower())
            a, b = fileString[:index], fileString[index + len(placeholderString):]
            globString = a + '[0-9]' * paddingValue + b

            globData = cls.MOD_glob.glob(globString)
            if globData:
                for i in globData:
                    lis.append(i.replace('\\', cls.DEF_bsc__os__pathsep))
        return lis

    @classmethod
    def _getOsMultifileExistFrameList(cls, fileString, placeholderString, paddingValue):
        lis = []

        fileStringLis = cls._getOsMultifileExistFileList(fileString, placeholderString, paddingValue)
        if fileStringLis:
            for i in fileStringLis:
                number = cls._getOsFileFrame(i, cls.VAR_padding_multifile)
                if number is not None:
                    lis.append(number)
        return lis

    @classmethod
    def _getOsMultifileFileSizeList(cls, fileString, frameRange, placeholderString, paddingValue):
        return [bscMtdCore.Mtd_BscUtility._getOsFileSize(i) for i in cls._getOsMultifileFileList(fileString, frameRange, placeholderString, paddingValue)]

    @classmethod
    def _getOsMultifileExistFileSizeList(cls, fileString, placeholderString, paddingValue):
        return [bscMtdCore.Mtd_BscUtility._getOsFileSize(i) for i in cls._getOsMultifileExistFileList(fileString, placeholderString, paddingValue)]

    @classmethod
    def isExist(cls, fileString):
        if bscMtdCore.Mtd_BscUtility._isOsFileExist(fileString):
            return True
        else:
            for i in cls.DEF_placeholder_multifile_list:
                if i in bscMtdCore.Mtd_BscUtility._getOsFileBasename(fileString).lower():
                    if cls._getOsMultifileExistFileList(fileString, i, cls.VAR_padding_multifile):
                        return True
        return False

    @classmethod
    def files(cls, fileString, frameRange):
        for i in cls.DEF_placeholder_multifile_list:
            if i in bscMtdCore.Mtd_BscUtility._getOsFileBasename(fileString).lower():
                return cls._getOsMultifileFileList(fileString, frameRange, i, cls.VAR_padding_multifile)
        return []

    @classmethod
    def existFiles(cls, fileString):
        if bscMtdCore.Mtd_BscUtility._isOsFileExist(fileString):
            return [fileString.replace('\\', cls.DEF_bsc__os__pathsep)]
        else:
            for i in cls.DEF_placeholder_multifile_list:
                if i in bscMtdCore.Mtd_BscUtility._getOsFileBasename(fileString).lower():
                    return cls._getOsMultifileExistFileList(fileString, i, cls.VAR_padding_multifile)
        return []

    @classmethod
    def existFrames(cls, fileString):
        if bscMtdCore.Mtd_BscUtility._isOsFileExist(fileString):
            return [cls._getOsFileFrame(fileString, cls.VAR_padding_multifile)]
        else:
            for i in cls.DEF_placeholder_multifile_list:
                if i in bscMtdCore.Mtd_BscUtility._getOsFileBasename(fileString).lower():
                    return cls._getOsMultifileExistFrameList(fileString, i, cls.VAR_padding_multifile)
        return []

    @classmethod
    def fileSizes(cls, fileString, frameRange):
        for i in cls.DEF_placeholder_multifile_list:
            if i in bscMtdCore.Mtd_BscUtility._getOsFileBasename(fileString).lower():
                return cls._getOsMultifileFileSizeList(fileString, frameRange, i, cls.VAR_padding_multifile)
        return []
    
    @classmethod
    def existFileSizes(cls, fileString):
        if bscMtdCore.Mtd_BscUtility._isOsFileExist(fileString):
            return bscMtdCore.Mtd_BscUtility._getOsFileSize(fileString)
        for i in cls.DEF_placeholder_multifile_list:
            if i in bscMtdCore.Mtd_BscUtility._getOsFileBasename(fileString).lower():
                return cls._getOsMultifileExistFileSizeList(fileString, i, cls.VAR_padding_multifile)

        return []
