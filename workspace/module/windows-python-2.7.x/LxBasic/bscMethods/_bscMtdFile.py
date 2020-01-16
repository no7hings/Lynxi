# coding:utf-8
from LxBasic import bscCore


class OsFile(bscCore.FileBasic):
    @classmethod
    def write(cls, fileString, raw):
        cls._setOsFileDirectoryCreate(fileString)
        with open(fileString, u'w') as f:
            if isinstance(raw, str) or isinstance(raw, unicode):
                f.write(raw)
            elif isinstance(raw, tuple) or isinstance(raw, list):
                f.writelines(raw)

            f.close()

    @classmethod
    def read(cls, fileString):
        if cls._isOsFileExist(fileString):
            with open(fileString, u'r') as f:
                raw = f.read()
                f.close()
                return raw

    @classmethod
    def readlines(cls, fileString):
        if cls._isOsFileExist(fileString):
            with open(fileString, u'r') as f:
                raw = f.readlines()
                f.close()
                return raw


class OsFileGzip(bscCore.FileBasic):
    @classmethod
    def write(cls, fileString, raw):
        cls._setOsFileDirectoryCreate(fileString)
        #
        osFileBasename = cls._getOsFileBasename(fileString)
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
        if cls._isOsFileExist(fileString):
            with cls.MOD_gzip.GzipFile(
                    mode=u'rb',
                    fileobj=open(fileString, u'rb')
            ) as g:
                raw = g.read()
                g.close()
                return raw

    @classmethod
    def readlines(cls, fileString):
        if cls._isOsFileExist(fileString):
            with cls.MOD_gzip.GzipFile(
                    mode=u'rb',
                    fileobj=open(fileString, u'rb')
            ) as g:
                raw = g.readlines()
                g.close()
                return raw


class OsJson(bscCore.FileBasic):
    @classmethod
    def read(cls, fileString, encoding=None):
        if cls.MTD_os_path.isfile(fileString):
            with open(fileString) as j:
                raw = cls.MOD_json.load(j, encoding=encoding)
                j.close()
                return raw

    @classmethod
    def write(cls, fileString, raw, indent=4, ensure_ascii=True):
        temporaryFilename = cls._getOsFileTemporaryName(fileString)
        with open(temporaryFilename, u'w') as j:
            cls.MOD_json.dump(
                raw,
                j,
                indent=indent,
                ensure_ascii=ensure_ascii
            )

        cls._setOsFileCopy(temporaryFilename, fileString)

    @classmethod
    def getValue(cls, fileString, key, failobj=None):
        raw = cls.read(fileString)
        if raw:
            if isinstance(raw, dict):
                return raw.get(key, failobj)

    @classmethod
    def setValue(cls, fileString, dic):
        if cls._isOsFileExist(fileString):
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


class OsJsonGzip(bscCore.FileBasic):
    @classmethod
    def read(cls, fileString, encoding=None):
        if cls._isOsFileExist(fileString):
            with cls.MOD_gzip.GzipFile(
                    mode=u'rb',
                    fileobj=open(fileString, u'rb')
            ) as g:
                raw = cls.MOD_json.load(g, encoding=encoding)
                g.close()
                return raw

    @classmethod
    def write(cls, fileString, raw, indent=4, ensure_ascii=True):
        temporaryFilename = cls._getOsFileTemporaryName(fileString)
        with cls.MOD_gzip.GzipFile(
                filename=cls._getOsFileBasename(fileString),
                mode=u'wb',
                compresslevel=9,
                fileobj=open(temporaryFilename, u'wb')
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
        cls._setOsFileCopy(temporaryFilename, fileString)


class OsImage(bscCore.FileBasic):
    module_fullpath_name = 'PIL.Image'
    @classmethod
    def _toPImage(cls, fileString):
        module = cls._setLoadPythonModule(cls.module_fullpath_name)
        if module:
            if cls._isOsFileExist(fileString):
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


class OsMultifile(bscCore.Basic):
    placeholder_frame = '####'
    padding_frame = 4

    @classmethod
    def _getOsFileFrame(cls, fileString):
        lis = cls.MOD_re.findall(
            '[0-9]'*cls.padding_frame,
            cls._getOsFileBasename(fileString)
        )
        if lis:
            return int(lis[0])
    
    @classmethod
    def _getOsMultifileFileList(cls, fileString, frameRange):
        lis = []

        startFrame, endFrame = frameRange
        for i in xrange(endFrame - startFrame + 1):
            subOsFile = fileString.replace(
                cls.placeholder_frame,
                str(i + startFrame).zfill(cls.padding_frame)
            )
            lis.append(subOsFile)
        return lis
    
    @classmethod
    def _getOsMultifileExistFileList(cls, fileString):
        lis = []

        globData = cls.MOD_glob.glob(
            fileString.replace(
                cls.placeholder_frame,
                '[0-9]' * cls.padding_frame
            )
        )
        if globData:
            for i in globData:
                lis.append(i.replace('\\', '/'))
        return lis
    
    @classmethod
    def _getOsMultifileExistFrameList(cls, fileString):
        lis = []

        fileStringLis = cls._getOsMultifileExistFileList(fileString)
        if fileStringLis:
            for i in fileStringLis:
                number = cls._getOsFileFrame(i)
                if number is not None:
                    lis.append(number)
        return lis

    @classmethod
    def _getOsMultifileFileSizeList(cls, fileString, frameRange):
        return [cls._getOsFileSize(i) for i in cls._getOsMultifileFileList(fileString, frameRange)]

    @classmethod
    def _getOsMultifileExistFileSizeList(cls, fileString):
        return [cls._getOsFileSize(i) for i in cls._getOsMultifileExistFileList(fileString)]

    @classmethod
    def files(cls, fileString, frameRange):
        return cls._getOsMultifileFileList(fileString, frameRange)

    @classmethod
    def existFiles(cls, fileString):
        return cls._getOsMultifileExistFileList(fileString)

    @classmethod
    def existFrames(cls, fileString):
        return cls._getOsMultifileExistFrameList(fileString)

    @classmethod
    def fileSizes(cls, fileString, frameRange):
        return cls._getOsMultifileFileSizeList(fileString, frameRange)
    
    @classmethod
    def existFileSizes(cls, fileString):
        return cls._getOsMultifileExistFileSizeList(fileString)
