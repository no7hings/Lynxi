# coding:utf-8
from LxBasic import bscMethods

from LxMaBasic import maBscMethods

from LxMaya.method.basic import _maMethodBasic

from LxMaya import method


#
class MaAlembicCacheExport(object):
    app_method = _maMethodBasic.Mtd_AppMaya
    app_animation_method = method.Mtd_MaAnimation
    app_fle_cache_method = method.Mtd_MaAbcCache

    def __init__(self, fileString, groupString=None, frame=None, step=None, attributeString=None, optionDic=None, dataFormat=None):
        self._fileString = fileString
        self._groupString = groupString
        self._frame = frame
        self._step = step
        self._attributeString = attributeString
        self._optionDic = optionDic
        self._dataFormat = dataFormat
    @classmethod
    def _toFileArgString(cls, fileString):
        return '{0} {1}'.format(cls.app_fle_cache_method.FileKey, fileString.replace('\\', '/'))
    @classmethod
    def _toOptionArgString(cls, optionDic):
        lis = [k for k, v in optionDic.items() if v is True]
        #
        if lis:
            argString = ' '.join(lis)
        else:
            argString = None
        return argString
    @classmethod
    def _toDataFormatArgString(cls, dataFormat):
        if isinstance(dataFormat, str) or isinstance(dataFormat, unicode):
            if dataFormat in cls.app_fle_cache_method.DataFormats:
                argString = '{0} {1}'.format(cls.app_fle_cache_method.DataFormatKey, dataFormat)
            else:
                argString = '{0} {1}'.format(cls.app_fle_cache_method.DataFormatKey, cls.app_fle_cache_method.OgawaDataFormat)
        else:
            argString = '{0} {1}'.format(cls.app_fle_cache_method.DataFormatKey, cls.app_fle_cache_method.OgawaDataFormat)
        return argString
    @classmethod
    def _toFrameArgString(cls, frame):
        if isinstance(frame, tuple) or isinstance(frame, list):
            startFrame, endFrame = frame
        elif isinstance(frame, int):
            startFrame = endFrame = frame
        else:
            startFrame = endFrame = cls.app_animation_method.getCurrentFrame()
        #
        argString = '{0} {1} {2}'.format(cls.app_fle_cache_method.FrameRangeKey, startFrame, endFrame)
        return argString
    @classmethod
    def _toStepArgString(cls, step):
        if isinstance(step, float) or isinstance(step, int):
            argString = '{0} {1}'.format(cls.app_fle_cache_method.StepKey, step)
        else:
            argString = None
        return argString
    @classmethod
    def _toRootArgString(cls, groupString):
        lis = cls.app_method._toAppExistStringList(groupString)
        #
        if lis:
            argString = ' '.join(['{0} {1}'.format(cls.app_fle_cache_method.RootKey, i) for i in lis])
        else:
            argString = None
        return argString
    @classmethod
    def _toAttributeArgString(cls, attrName):
        lis = bscMethods.String.toList(attrName)
        #
        if lis:
            argString = ' '.join(['{0} {1}'.format(cls.app_fle_cache_method.AttributeKey, i) for i in lis])
        else:
            argString = None
        return argString
    @staticmethod
    def _toExportArgString(argLis):
        usefulArgLis = [i for i in argLis if i is not None]
        if usefulArgLis:
            return ' '.join(usefulArgLis)
    #
    def export(self):
        temporaryOsFile = bscMethods.OsFile.temporaryName(self._fileString)
        argLis = [
            self._toFrameArgString(self._frame),
            self._toStepArgString(self._step),
            self._toAttributeArgString(self._attributeString),
            self._toOptionArgString(self._optionDic),
            self._toDataFormatArgString(self._dataFormat),
            self._toRootArgString(self._groupString),
            self._toFileArgString(temporaryOsFile)
        ]
        #
        exportArgString = self._toExportArgString(argLis)
        #
        if exportArgString:
            # Export
            self.app_fle_cache_method.abcCacheExportCommand(exportArgString)
            #
            bscMethods.OsFile.copyTo(temporaryOsFile, self._fileString)


#
class MaGpuCacheExport(object):
    app_animation_method = method.Mtd_MaAnimation
    app_fle_cache_method = method.MaGpuCacheMethod
    def __init__(self, fileString, groupString=None, frame=None, optionKwargs=None):
        self._fileString = fileString
        self._groupString = groupString
        self._frame = frame
        self._optionKwargs = optionKwargs
        #
        self._commandOptionKwargs = self.app_fle_cache_method.MaDefGpuCacheExportKwargs.copy()
    #
    def _updateFrameOptionKwargs(self):
        startFrame, endFrame = self.app_animation_method.toFrameRange(self._frame)
        #
        self._commandOptionKwargs['startTime'] = startFrame
        self._commandOptionKwargs['endTime'] = endFrame
    #
    def _updateOverrideKwargs(self):
        if isinstance(self._optionKwargs, dict):
            for k, v in self._optionKwargs.items():
                self._commandOptionKwargs[k] = v
    #
    def run(self):
        self._updateFrameOptionKwargs()
        self._updateOverrideKwargs()
        #
        self.app_fle_cache_method.gpuCacheExportCommand(
            self._fileString,
            self._groupString,
            self._commandOptionKwargs
        )


#
class MaProxyCacheExport(object):
    app_animation_method = method.Mtd_MaAnimation
    app_fle_cache_method = method.MaProxyCacheMethod
    def __init__(self, fileString, groupString=None, frame=None, step=None, optionKwargs=None):
        self._fileString = fileString
        self._groupString = groupString
        self._frame = frame
        self._step = step
        self._optionKwargs = optionKwargs
        #
        self._commandOptionKwargs = self.app_fle_cache_method.MaDefArnoldProxyExportKwargs.copy()
    #
    def _updateFrameOptionKwargs(self):
        if self._frame is not None:
            startFrame, endFrame = self.app_animation_method.toFrameRange(self._frame)
            #
            optionsString = self._commandOptionKwargs['options']
            #
            argString = '-startFrame {};-endFrame {};'.format(float(startFrame), float(endFrame))
            optionsString += argString
            #
            self._commandOptionKwargs['options'] = optionsString
    #
    def _updateStepOptionKwargs(self):
        if self._frame is not None:
            optionsString = self._commandOptionKwargs['options']
            if isinstance(self._step, int) or isinstance(self._step, float):
                step = self._step
            else:
                step = 1.0
            #
            argString = '-frameStep {}'.format(float(step))
            optionsString += argString
            #
            self._commandOptionKwargs['options'] = optionsString
    #
    def run(self):
        self._updateFrameOptionKwargs()
        self._updateStepOptionKwargs()
        #
        self.app_fle_cache_method.arnoldProxyExportCommand(
            self._fileString,
            self._groupString,
            self._commandOptionKwargs
        )


#
class MaYetiGraphExport(method.MaYetiGraphObjectMethod):

    def __init__(self, fileString, groupString=None, setString=None):
        self._fileString = fileString
        self._groupString = groupString
        self._setString = setString
        #
        self._commandOptionKwargs = maBscMethods.File.VAR_file_export_kwarg_dic.copy()
    #
    def _updateObjectOptionKwargs(self):
        objectLis = self._toAppExistStringList([self._groupString, self._setString])
        if objectLis:
            self._commandOptionKwargs.pop(maBscMethods.File.MaFileExportAllOption)
            self._commandOptionKwargs[maBscMethods.File.MaFileExportSelectedOption] = True
            #
            self.setNodeSelect(objectLis, noExpand=True)
    #
    def run(self):
        self._updateObjectOptionKwargs()
        # Export
        temporaryOsFile = bscMethods.OsFile.temporaryName(self._fileString)
        maBscMethods.File._maFileExportCommand(temporaryOsFile, self._commandOptionKwargs)
        bscMethods.OsFile.copyTo(temporaryOsFile, self._fileString)


#
class MaYetiTextureExport(method.MaYetiTextureFileMethod):
    def __init__(self, folderString, groupString=None):
        self._folderString = folderString
        self._groupString = groupString
        #
        self._yetiObjectLis = []
    #
    def _updateYetiObjectLis(self):
        self._yetiObjectLis = self.getYetiObjectLis(self._groupString)
    #
    def run(self):
        self._updateYetiObjectLis()
        #
        self.setYetiTextureCollection(self._folderString, self._yetiObjectLis)
        self.setYetiTextureRepath(self._folderString, self._yetiObjectLis)
