# coding:utf-8
from LxBasic import bscMethods

from LxMaBasic import maBscMethods


class AlembicCache(object):
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
        return '{0} {1}'.format(maBscMethods.AlembicCache.FileKey, fileString.replace('\\', '/'))

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
            if dataFormat in maBscMethods.AlembicCache.DataFormats:
                argString = '{0} {1}'.format(maBscMethods.AlembicCache.DataFormatKey, dataFormat)
            else:
                argString = '{0} {1}'.format(maBscMethods.AlembicCache.DataFormatKey, maBscMethods.AlembicCache.OgawaDataFormat)
        else:
            argString = '{0} {1}'.format(maBscMethods.AlembicCache.DataFormatKey, maBscMethods.AlembicCache.OgawaDataFormat)
        return argString

    @classmethod
    def _toFrameArgString(cls, frame):
        if isinstance(frame, tuple) or isinstance(frame, list):
            startFrame, endFrame = frame
        elif isinstance(frame, int):
            startFrame = endFrame = frame
        else:
            startFrame = endFrame = maBscMethods.Frame.getCurrentFrame()
        #
        argString = '{0} {1} {2}'.format(maBscMethods.AlembicCache.FrameRangeKey, startFrame, endFrame)
        return argString

    @classmethod
    def _toStepArgString(cls, step):
        if isinstance(step, float) or isinstance(step, int):
            argString = '{0} {1}'.format(maBscMethods.AlembicCache.StepKey, step)
        else:
            argString = None
        return argString

    @classmethod
    def _toRootArgString(cls, groupString):
        lis = maBscMethods.NodeName.toExistList(groupString)
        #
        if lis:
            argString = ' '.join(['{0} {1}'.format(maBscMethods.AlembicCache.RootKey, i) for i in lis])
        else:
            argString = None
        return argString

    @classmethod
    def _toAttributeArgString(cls, attrName):
        lis = bscMethods.String.toList(attrName)
        #
        if lis:
            argString = ' '.join(['{0} {1}'.format(maBscMethods.AlembicCache.AttributeKey, i) for i in lis])
        else:
            argString = None
        return argString

    @staticmethod
    def _toExportArgString(argLis):
        usefulArgLis = [i for i in argLis if i is not None]
        if usefulArgLis:
            return ' '.join(usefulArgLis)

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
            maBscMethods.AlembicCache.abcCacheExportCommand(exportArgString)
            #
            bscMethods.OsFile.copyTo(temporaryOsFile, self._fileString)
