# coding:utf-8
from LxBasic import bscCore


class OsJson(bscCore.Basic):
    @classmethod
    def read(cls, fileString, encoding=None):
        if cls.mtd_os_path.isfile(fileString):
            with open(fileString) as j:
                return cls.method_json.load(j, encoding=encoding)

    @classmethod
    def write(cls, fileString, raw, indent=4, ensure_ascii=True):
        if raw is not None:
            temporaryFileString = cls._getOsFileTemporary(fileString)
            with open(temporaryFileString, u'w') as j:
                cls.method_json.dump(raw, j, indent=indent, ensure_ascii=ensure_ascii)

            cls._setOsFileCopy(temporaryFileString, fileString)

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
        return cls.method_json.loads(raw)

    @classmethod
    def dump(cls, raw):
        return cls.method_json.dumps(raw)


class OsImage(bscCore.Basic):
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
        try:
            pImage = cls._toPImage(fileString)
            if pImage is not None:
                return pImage.size
        except:
            pass
        return size
