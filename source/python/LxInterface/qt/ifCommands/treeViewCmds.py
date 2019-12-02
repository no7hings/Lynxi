# coding=utf-8
from LxCore import lxBasic, lxConfigure, lxProgress
#
from LxCore.preset.prod import scenePr
#
from LxUi.command import uiHtml
#
from LxUi.qt import uiWidgets_, uiChart_, uiWidgets
#
none = ''


#
def setListScRenderImageCustomize(
        parentUi,
        customizes,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame
):
    def setBranch(customize):
        def setActionData():
            def openRenderFileToLocalCmd():
                if lxBasic.isOsExistsFile(serverRenderFile):
                    from LxMaya.command import maFile
                    maFile.openMayaFileToLocal(serverRenderFile, localRenderFile)
            #
            def openRenderFileCmd():
                if lxBasic.isOsExistsFile(serverRenderFile):
                    from LxMaya.command import maFile
                    maFile.fileOpen(serverRenderFile)
            #
            def openRenderFolder():
                lxBasic.setOsFolderOpen(renderFolder)
            #
            renderFolder = scenePr.scUnitRenderFolder(
                lxConfigure.LynxiRootIndex_Server,
                projectName,
                sceneClass, sceneName, sceneVariant, sceneStage,
                customize
            )
            #
            actions = [
                ('Basic', ),
                ('Open Render File ( Local )', 'svg_basic@svg#fileOpen', True, openRenderFileToLocalCmd),
                ('Open Render File ( Server )', 'svg_basic@svg#fileOpen', True, openRenderFileCmd),
                ('Extend', ),
                ('Open Render Folder', 'svg_basic@svg#folder', True, openRenderFolder)
            ]
            itemWidget.setActionData(actions)
        #
        progressBar.updateProgress()
        #
        data = scenePr.getScRenderImageData(
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage,
            customize
        )
        if data:
            iconKeyword = 'svg_basic@svg#name'
            stateLabel = none
            treeItem = uiWidgets_.QTreeWidgetItem_()
            #
            if hasattr(parentUi, 'addItem'):
                parentUi.addItem(treeItem)
            elif hasattr(parentUi, 'addChild'):
                parentUi.addChild(treeItem)
                parentUi.setExpanded(True)
            #
            serverRenderFile = scenePr.scUnitRenderFile(
                lxConfigure.LynxiRootIndex_Server,
                projectName, sceneClass, sceneName, sceneVariant, sceneStage, customize
            )[1]
            localRenderFile = scenePr.scUnitRenderFile(
                lxConfigure.LynxiRootIndex_Local,
                projectName, sceneClass, sceneName, sceneVariant, sceneStage, customize
            )[1]
            #
            imagePrefix, imageFiles = data
            #
            if not imageFiles:
                stateLabel = 'off'
            #
            showExplain = '{0} ( {1} )'.format(customize, len(imageFiles))
            itemWidget = treeItem.setItemIconWidget(0, iconKeyword, showExplain, stateLabel)
            setActionData()
            #
            showTimeTag = lxBasic.getCnViewTime(lxBasic.getOsFileMtimestamp(serverRenderFile))
            treeItem.setText(1, showTimeTag)
            #
            treeItem.imageFiles = imageFiles
            treeItem.startFrame = startFrame
            treeItem.endFrame = endFrame
            treeItem.customize = customize
            #
            subMethods = setListRenderImages(
                treeItem,
                imagePrefix,
                imageFiles,
                startFrame, endFrame
            )
            methods.extend(subMethods)
    #
    methods = []
    #
    if customizes:
        explain = '''List Scene Render ( Customizes )'''
        maxValue = len(customizes)
        progressBar = lxProgress.viewSubProgress(explain, maxValue)
        [setBranch(i) for i in customizes]
    #
    return methods


#
def setListRenderImages(
        parentUi,
        imagePrefix,
        imageFiles,
        startFrame, endFrame
):
    #
    def getDic(data):
        dic = lxBasic.orderedDict()
        findKey = '<RenderLayer>'
        splitPrefix = imagePrefix.split(pathSep)
        if findKey in splitPrefix:
            index = splitPrefix.index('<RenderLayer>')
        else:
            index = None
        #
        for j in data:
            string = j.split('/images')[-1][1:]
            splitString = string.split(pathSep)
            if index is not None:
                renderLayer = splitString[index]
                #
                dic.setdefault(renderLayer, []).append(j)
            else:
                dic.setdefault('None', []).append(j)
        #
        return dic
    #
    def setLayerBranch(layer):
        treeItem = uiWidgets_.QTreeWidgetItem_()
        #
        if type(parentUi) == uiWidgets_.QTreeWidget_:
            parentUi.addItem(treeItem)
        elif type(parentUi) == uiWidgets_.QTreeWidgetItem_:
            parentUi.addChild(treeItem)
            #
            parentUi.setExpanded(True)
        #
        treeItem.layer = layer
        return treeItem
    #
    def setImageBranch(index, parentItem, imageFile):
        def setActionData():
            def openImageFolder():
                lxBasic.setOsFolderOpen(imageFolder)
            #
            def openImageFolderEnabled():
                return lxBasic.isOsExist(imageFolder)
            #
            def openImage():
                osCmdExe = '{}/exe/windows/Pdplayer 64/pdplayer64.exe'.format(lxConfigure._getLxBasicPath())
                if lxBasic.isOsExistsFile(osCmdExe):
                    subOsFiles = lxBasic.getOsSeqFiles(imageFile)
                    if subOsFiles:
                        subOsFile = subOsFiles[0]
                        osCmd = '''"{}" "{}"'''.format(osCmdExe, subOsFile)
                        lxBasic.setOsCommandRun_(osCmd)
            #
            def showSizeHistogramWindow():
                win = uiWidgets.UiDialogWindow()
                win.setNameText('Image Size Histogram')
                chart = uiChart_.xHistogramChart()
                win.addWidget(chart)
                chart.setDrawData(lxBasic.getOsSeqFileSizes(imageFile, startFrame, endFrame), (startFrame, 0), ('Frame', 'Size'))
                win.uiShow()
            #
            def openImageEnabled():
                pass
            #
            imageFolder = lxBasic.getOsFileDirname(imageFile)
            #
            actions = [
                ('Basic', ),
                ('Open Image', 'svg_basic@svg#fileOpen', openImageFolderEnabled, openImage),
                ('Open Image Folder', 'svg_basic@svg#folder', openImageFolderEnabled, openImageFolder),
                ('Extend', ),
                ('Show Image Size Histogram Window', 'svg_basic@svg#subWindow', openImageFolderEnabled, showSizeHistogramWindow),
            ]
            itemWidget.setActionData(actions)
        #
        def updateCompletion():
            numbers = lxBasic.getOsSeqFileNumbers(imageFile)
            #
            numRangeArray = lxBasic.getFrameRange(numbers)
            #
            lineChart.setDrawData(numRangeArray, startFrame, endFrame)
        #
        if index == 0:
            treeItem = parentItem
        else:
            treeItem = uiWidgets_.QTreeWidgetItem_()
            parentItem.addChild(treeItem)
        #
        iconKeyword = 'svg_basic@svg#image'
        #
        explain = imageFile.split('/images')[-1][1:]
        htmlExplain = uiHtml.getHtmlRenderImage(imagePrefix, explain)
        itemWidget = treeItem.setItemIconWidget(0, iconKeyword, htmlExplain)
        # Action
        setActionData()
        #
        lineChart = uiChart_.xSequenceChart()
        treeItem.setItemWidget(2, lineChart)
        #
        methods.append(updateCompletion)
    #
    pathSep = '/'
    #
    methods = []
    #
    if imageFiles:
        imageDic = getDic(imageFiles)
        for k, v in imageDic.items():
            layerItem = setLayerBranch(k)
            [setImageBranch(seq, layerItem, i) for seq, i in enumerate(v)]
    #
    return methods
