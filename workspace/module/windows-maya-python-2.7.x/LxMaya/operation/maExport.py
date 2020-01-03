# coding:utf-8
from LxCore.method import _osMethod

from LxMaya.method.basic import _maMethodBasic

from LxMaya.method import _maMethod


#
class MaFileExport(object):
    app_method = _maMethodBasic.Mtd_AppMaya
    plf_file_method = _osMethod.OsFileMethod
    app_file_method = _maMethod.MaFileMethod
    def __init__(self, fileString, objectString=None, optionKwargs=None):
        """
        :param fileString: str or list
        :param objectString: str or list
        :param optionKwargs: dict
        """
        self._fileString = fileString
        self._objectString = objectString
        self._optionKwargs = optionKwargs
        #
        self._commandOptionKwargs = self.app_file_method.MaDefFileExportKwargs.copy()
    #
    def _updateObjectOptionKwargs(self):
        objectLis = self.app_method._toNodeLis(self._objectString)
        if objectLis:
            self._commandOptionKwargs.pop(self.app_file_method.MaFileExportAllOption)
            self._commandOptionKwargs[self.app_file_method.MaFileExportSelectedOption] = True
            #
            self.app_method.setNodeSelect(objectLis, noExpand=True)
    #
    def _updateOverrideOptionKwargs(self):
        if isinstance(self._optionKwargs, dict):
            if self._commandOptionKwargs.get(self.app_file_method.MaFileExportSelectedOption, None) is True:
                for k, v in self._optionKwargs.items():
                    if k in self.app_file_method.MaFileExportSelectedOptions:
                        self._commandOptionKwargs[k] = v
            else:
                for k, v in self._optionKwargs.items():
                    self._commandOptionKwargs[k] = v
    #
    def run(self):
        self._updateObjectOptionKwargs()
        self._updateOverrideOptionKwargs()
        # Export
        temporaryOsFile = self.plf_file_method.getOsTemporaryFile(self._fileString)
        self.app_file_method.fileExportCommand(temporaryOsFile, self._commandOptionKwargs)
        self.plf_file_method.setOsFileCopy(temporaryOsFile, self._fileString)


#
class MaMaterialExport(object):
    app_nod_graph_method = _maMethod.MaShaderNodeGraphMethod
    plf_file_method = _osMethod.OsFileMethod
    app_file_method = _maMethod.MaFileMethod
    def __init__(self, fileString, groupString=None, nodeTypeString=None, optionKwargs=None):
        """
        :param fileString: str or list
        :param groupString: str or list
        :param nodeTypeString: str or list
        :param optionKwargs: dict
        """
        self._fileString = fileString
        self._groupString = groupString
        self._typeString = nodeTypeString
        self._optionKwargs = optionKwargs
        #
        self._shaderObjectLis = []
        self._shadingEngineLis = []
    #
    def _updateShaderObjectLis(self):
        self._shaderObjectLis = self.app_nod_graph_method.getObjectLisByGroup(self._groupString, self._typeString)
    #
    def _updateShadingEngineLis(self):
        if self._shaderObjectLis:
            self._shadingEngineLis = self.app_nod_graph_method.getShadingEngineLisByObject(self._shaderObjectLis)
        else:
            self._shadingEngineLis = self.app_nod_graph_method.getShadingEngineLis()
    #
    def run(self):
        self._updateShaderObjectLis()
        self._updateShadingEngineLis()
        #
        if self._shadingEngineLis:
            self.app_nod_graph_method.setNodeSelect(self._shadingEngineLis, noExpand=True)
            exportArgDic = {
                'force': True,
                'options': 'v=0',
                'defaultExtensions': True,
                'preserveReferences': False,
                'type': self.app_file_method.getFileType(self._fileString),
                self.app_file_method.MaFileExportSelectedOption: True,
                self.app_file_method.MaFileShaderOption: True
            }
            # Export
            temporaryOsFile = self.plf_file_method.getOsTemporaryFile(self._fileString)
            self.app_file_method.fileExportCommand(temporaryOsFile, exportArgDic)
            self.plf_file_method.setOsFileCopy(temporaryOsFile, self._fileString)
            #
            self.app_nod_graph_method.setSelectClear()


#
class MaMaterialObjSetExport(_maMethod.MaShaderNodeGraphMethod, _osMethod.OsYamlFileMethod):
    app_nod_graph_method = _maMethod.MaShaderNodeGraphMethod
    plf_file_method = _osMethod.OsFileMethod
    def __init__(self, fileString, groupString=None, nodeTypeString=None, optionKwargs=None):
        """
        :param fileString: str or list
        :param groupString: str or list
        :param nodeTypeString: str or list
        :param optionKwargs: dict
        """
        self._fileString = fileString
        self._groupString = groupString
        self._typeString = nodeTypeString
        self._optionKwargs = optionKwargs
        #
        self._shaderObjectLis = []
        self._shadingEngineLis = []
        self._shaderUvLinkLis = []
        self._shadingEngineObjSetDic = {}
    #
    def _updateShaderObjectLis(self):
        self._shaderObjectLis = self.getObjectLisByGroup(self._groupString, self._typeString)
    #
    def _updateShadingEngineLis(self):
        if self._shaderObjectLis:
            self._shadingEngineLis = self.getShadingEngineLisByObject(self._shaderObjectLis)
        else:
            self._shadingEngineLis = self.getShadingEngineLis()
    #
    def _updateShaderUvLinkLis(self):
        if self._shadingEngineLis:
            pass
    #
    def _updateShadingEngineObjSetDic(self):
        self._shadingEngineObjSetDic = {}
        if self._shadingEngineLis:
            for shadingEngine in self._shadingEngineLis:
                uniqueId = self.getNodeUniqueId(shadingEngine)
                self._shadingEngineObjSetDic[(shadingEngine, uniqueId)] = self.getShadingEngineObjSet(shadingEngine)
    #
    def run(self):
        self._updateShaderObjectLis()
        self._updateShadingEngineLis()
        self._updateShadingEngineObjSetDic()
        #
        if self._shadingEngineLis:
            if self._shadingEngineObjSetDic:
                self.writeOsYaml(self._shadingEngineObjSetDic, self._fileString)
            #
            self.setSelectClear()


#
class MaPreviewExport(_maMethod.MaWindowMethod, _maMethod.MaCameraNodeMethod, _maMethod.MaRenderNodeMethod, _maMethod.MaPreviewFileMethod):
    app_animation_method = _maMethod.Mtd_MaAnimation
    app_viewport_method = _maMethod.Mtd_MaViewport

    PreviewWindowName = 'previewWindow'
    PreviewViewportName = 'previewViewport'

    def __init__(self, fileString, cameraString=None, groupString=None, size=None, frame=None, displayMode=5):
        """
        :param fileString: str
        :param cameraString: str
        :param groupString: str
        :param size: int or tuple
        :param frame: int or float or tuple
        :param displayMode: 4, 5, 5, 7
        """
        self._fileString = fileString
        self._cameraString = cameraString
        self._groupString = groupString
        self._size = size
        self._frame = frame
        self._displayMode = displayMode
        #
        self._fileFormat = None
        #
        self._cameraOptionKwargs = self.MaDefCameraOptionKwargs.copy()
        self._playblastOptionKwargs = self.MaDefPreviewOptionKwargs.copy()
        #
        self._isCameraDefaultPosEnable = False
        self._isVp2RendererEnable = False
        self._isDefaultBackgroundColorEnable = False
        self._isShowHudEnable = False
        self._isDisplayResolutionEnable = False
        #
        self._viewport = None
        #
    #
    def setRootString(self, objectString):
        self._groupString = objectString
    #
    def setCameraDefaultPosEnable(self, boolean):
        self._isCameraDefaultPosEnable = boolean
    #
    def setDefaultBackgroundColorEnable(self, boolean):
        self._isDefaultBackgroundColorEnable = boolean
    #
    def setVp2RendererEnable(self, boolean):
        self._isVp2RendererEnable = boolean
    #
    def setDisplayResolutionEnable(self, boolean):
        self._isDisplayResolutionEnable = boolean
    #
    def setViewPanelDisplayMode(self, displayMode):
        self._displayMode = displayMode
    #
    def _updateFileFormat(self):
        self._fileFormat = self.getOsFileExt(self._fileString)
    #
    def _updateWindow(self):
        if self._cameraString is None:
            self._camera = self.getActiveCameraObject()
        else:
            self._camera = self._cameraString
        #
        windowLayout = self.setCreateWindow(self.PreviewWindowName, self._width, self._height)
        self._viewport = self.app_viewport_method.setCreateViewPanel(self.PreviewViewportName, windowLayout, self._camera)
        # Viewport
        self.app_viewport_method.setViewportView(self._viewport)
        self.app_viewport_method.setViewportObjectDisplay(self._viewport)
        # Display Mode
        if self._displayMode == 4:
            self.setDefaultShaderColor(*self.MaDefShaderRgb)
            self.app_viewport_method.setViewportDefaultDisplayMode(self._viewport)
        elif self._displayMode == 5:
            self.app_viewport_method.setViewportShaderDisplayMode(self._viewport)
        elif self._displayMode == 6:
            self.app_viewport_method.setViewportTextureDisplayMode(self._viewport)
        elif self._displayMode == 7:
            self.app_viewport_method.setViewportLightDisplayMode(self._viewport)
        # Camera
        if self._isCameraDefaultPosEnable is True:
            self.setCameraDefPos(self._camera)
        # Root
        if self._groupString is not None:
            self.setNodeSelect(self._groupString)
            self.app_viewport_method.setViewportSelectObjectIsolate(self._viewport)
            self.setCameraViewFit(self._camera)
            #
            self.setSelectClear()

        # Default Background Color
        if self._isDefaultBackgroundColorEnable is True:
            self.setBackgroundColor(*self.MaDefBackgroundRgb)
    #
    def _updateCamera(self):
        self._cameraOptionKwargs['displayResolution'] = self._isDisplayResolutionEnable
        #
        self.setCameraView(self._camera, self._cameraOptionKwargs)
    #
    def _updatePlayblast(self):
        width, height = self._toSizeRemap(self._width, self._height, maximum=self.MaDefWindowMaximum)
        #
        self._playblastOptionKwargs['widthHeight'] = (width, height)
        self._playblastOptionKwargs['startTime'] = self._startFrame
        self._playblastOptionKwargs['endTime'] = self._endFrame
        self._playblastOptionKwargs['showOrnaments'] = self._isShowHudEnable
        #
        self.previewExportCommand(self._fileString, self._playblastOptionKwargs)
    #
    def _updateImageFile(self):
        if self._fileFormat == '.jpg':
            imageFileLis = self.getOutputImageFileLis()
            if imageFileLis:
                imageFile = imageFileLis[0]
                if self.isOsExistsFile(imageFile):
                    self.setOsFileMove(imageFile, self._fileString)
    #
    def _closeWindow(self):
        self.app_viewport_method.setViewportSelectObjectIsolate(self._viewport, False)
        #
        self.setWindowDelete(self.PreviewWindowName)
        self.setWindowDelete(self.PreviewViewportName)
    #
    def getOutputImageFileLis(self):
        startFrame, endFrame = self.app_animation_method.toFrameRange(self._frame)
        #
        lis = []
        #
        base, ext = self.toOsFileSplitByExt(self._fileString)
        #
        if not startFrame == endFrame:
            for i in range(startFrame, endFrame + 1):
                image = base + '.' + str(int(i)).zfill(4) + '.jpg'
                lis.append(image)
        else:
            lis = [base + '.' + str(int(startFrame)).zfill(4) + '.jpg']
        return lis
    #
    def run(self):
        self._startFrame, self._endFrame = self.app_animation_method.toFrameRange(self._frame)
        self._width, self._height = self._toSizeRange(self._size)
        #
        self._updateFileFormat()
        self._updateWindow()
        self._updateCamera()
        #
        self._updatePlayblast()
        #
        self._updateImageFile()
        #
        self._closeWindow()
