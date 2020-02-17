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
        cls._setOsJsonWrite(fileString, raw, indent, ensure_ascii)

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
        temporaryName = cls._getOsFileTemporaryName(fileString)
        with cls.MOD_gzip.GzipFile(
                filename=cls._getOsFileBasename(fileString),
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
        cls._setOsFileCopy(temporaryName, fileString)


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


class OsMultifile(bscCore.UtilityBasic):
    LST_placeholder_multifile = ['<udim>', '%04d', '<f>', '####']
    VAR_padding_multifile = 4

    @classmethod
    def _getOsFileFrame(cls, fileString, paddingValue):
        lis = cls.MOD_re.findall(
            '[0-9]'*paddingValue,
            cls._getOsFileBasename(fileString)
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
                subFileString = (a + str(i + startFrame).zfill(paddingValue) + b).replace('\\', cls.DEF_separator_os)
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
                    lis.append(i.replace('\\', cls.DEF_separator_os))
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
        return [cls._getOsFileSize(i) for i in cls._getOsMultifileFileList(fileString, frameRange, placeholderString, paddingValue)]

    @classmethod
    def _getOsMultifileExistFileSizeList(cls, fileString, placeholderString, paddingValue):
        return [cls._getOsFileSize(i) for i in cls._getOsMultifileExistFileList(fileString, placeholderString, paddingValue)]

    @classmethod
    def isExist(cls, fileString):
        if cls._isOsFileExist(fileString):
            return True
        else:
            for i in cls.LST_placeholder_multifile:
                if i in cls._getOsFileBasename(fileString).lower():
                    if cls._getOsMultifileExistFileList(fileString, i, cls.VAR_padding_multifile):
                        return True
        return False

    @classmethod
    def files(cls, fileString, frameRange):
        for i in cls.LST_placeholder_multifile:
            if i in cls._getOsFileBasename(fileString).lower():
                return cls._getOsMultifileFileList(fileString, frameRange, i, cls.VAR_padding_multifile)
        return []

    @classmethod
    def existFiles(cls, fileString):
        if cls._isOsFileExist(fileString):
            return [fileString.replace('\\', cls.DEF_separator_os)]
        else:
            for i in cls.LST_placeholder_multifile:
                if i in cls._getOsFileBasename(fileString).lower():
                    return cls._getOsMultifileExistFileList(fileString, i, cls.VAR_padding_multifile)
        return []

    @classmethod
    def existFrames(cls, fileString):
        if cls._isOsFileExist(fileString):
            return [cls._getOsFileFrame(fileString, cls.VAR_padding_multifile)]
        else:
            for i in cls.LST_placeholder_multifile:
                if i in cls._getOsFileBasename(fileString).lower():
                    return cls._getOsMultifileExistFrameList(fileString, i, cls.VAR_padding_multifile)
        return []

    @classmethod
    def fileSizes(cls, fileString, frameRange):
        for i in cls.LST_placeholder_multifile:
            if i in cls._getOsFileBasename(fileString).lower():
                return cls._getOsMultifileFileSizeList(fileString, frameRange, i, cls.VAR_padding_multifile)
        return []
    
    @classmethod
    def existFileSizes(cls, fileString):
        if cls._isOsFileExist(fileString):
            return cls._getOsFileSize(fileString)
        for i in cls.LST_placeholder_multifile:
            if i in cls._getOsFileBasename(fileString).lower():
                return cls._getOsMultifileExistFileSizeList(fileString, i, cls.VAR_padding_multifile)

        return []
