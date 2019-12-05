# coding:utf-8
from LxMaya import method


#
class MaAlembicCacheExport(method.MaAnimationMethod, method.MaAlembicCacheMethod):
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
        return '{0} {1}'.format(cls.FileKey, fileString.replace('\\', '/'))
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
            if dataFormat in cls.DataFormats:
                argString = '{0} {1}'.format(cls.DataFormatKey, dataFormat)
            else:
                argString = '{0} {1}'.format(cls.DataFormatKey, cls.OgawaDataFormat)
        else:
            argString = '{0} {1}'.format(cls.DataFormatKey, cls.OgawaDataFormat)
        return argString
    @classmethod
    def _toFrameArgString(cls, frame):
        if isinstance(frame, tuple) or isinstance(frame, list):
            startFrame, endFrame = frame
        elif isinstance(frame, int):
            startFrame = endFrame = frame
        else:
            startFrame = endFrame = cls.getCurrentFrame()
        #
        argString = '{0} {1} {2}'.format(cls.FrameRangeKey, startFrame, endFrame)
        return argString
    @classmethod
    def _toStepArgString(cls, step):
        if isinstance(step, float) or isinstance(step, int):
            argString = '{0} {1}'.format(cls.StepKey, step)
        else:
            argString = None
        return argString
    @classmethod
    def _toRootArgString(cls, groupString):
        lis = cls._toNodeLis(groupString)
        #
        if lis:
            argString = ' '.join(['{0} {1}'.format(cls.RootKey, i) for i in lis])
        else:
            argString = None
        return argString
    @classmethod
    def _toAttributeArgString(cls, attrName):
        lis = cls._toStringList(attrName)
        #
        if lis:
            argString = ' '.join(['{0} {1}'.format(cls.AttributeKey, i) for i in lis])
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
        temporaryOsFile = self.getOsTemporaryFile(self._fileString)
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
            self.abcCacheExportCommand(exportArgString)
            #
            self.setOsFileCopy(temporaryOsFile, self._fileString)


#
class MaGpuCacheExport(method.MaAnimationMethod, method.MaGpuCacheMethod):
    def __init__(self, fileString, groupString=None, frame=None, optionKwargs=None):
        self._fileString = fileString
        self._groupString = groupString
        self._frame = frame
        self._optionKwargs = optionKwargs
        #
        self._commandOptionKwargs = self.MaDefGpuCacheExportKwargs.copy()
    #
    def _updateFrameOptionKwargs(self):
        startFrame, endFrame = self.toFrameRange(self._frame)
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
        self.gpuCacheExportCommand(
            self._fileString,
            self._groupString,
            self._commandOptionKwargs
        )


#
class MaProxyCacheExport(method.MaAnimationMethod, method.MaProxyCacheMethod):
    def __init__(self, fileString, groupString=None, frame=None, step=None, optionKwargs=None):
        self._fileString = fileString
        self._groupString = groupString
        self._frame = frame
        self._step = step
        self._optionKwargs = optionKwargs
        #
        self._commandOptionKwargs = self.MaDefArnoldProxyExportKwargs.copy()
    #
    def _updateFrameOptionKwargs(self):
        if self._frame is not None:
            startFrame, endFrame = self.toFrameRange(self._frame)
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
        self.arnoldProxyExportCommand(
            self._fileString,
            self._groupString,
            self._commandOptionKwargs
        )


#
class MaYetiGraphExport(method.MaYetiGraphObjectMethod, method.MaFileMethod):
    def __init__(self, fileString, groupString=None, setString=None):
        self._fileString = fileString
        self._groupString = groupString
        self._setString = setString
        #
        self._commandOptionKwargs = self.MaDefFileExportKwargs.copy()
    #
    def _updateObjectOptionKwargs(self):
        objectLis = self._toNodeLis([self._groupString, self._setString])
        if objectLis:
            self._commandOptionKwargs.pop(self.MaFileExportAllOption)
            self._commandOptionKwargs[self.MaFileExportSelectedOption] = True
            #
            self.setNodeSelect(objectLis, noExpand=True)
    #
    def run(self):
        self._updateObjectOptionKwargs()
        # Export
        temporaryOsFile = self.getOsTemporaryFile(self._fileString)
        self.fileExportCommand(temporaryOsFile, self._commandOptionKwargs)
        self.setOsFileCopy(temporaryOsFile, self._fileString)


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
