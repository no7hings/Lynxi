# coding=utf-8
from LxBasic import bscCore, bscMethods, bscObjects

from LxCore import lxConfigure
#
from LxCore.preset.prod import scenePr
#
from LxUi.qt import qtWidgets_, qtChart_, qtWidgets

#
none = ''


#
def setListScRenderImageCustomize(
        parentUi,
        customizes,
        projectName,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame
):
    def setBranch(customize):
        def setActionData():
            def openRenderFileToLocalCmd():
                if bscMethods.OsFile.isExist(serverRenderFile):
                    from LxMaya.command import maFile
                    maFile.openMayaFileToLocal(serverRenderFile, localRenderFile)
            #
            def openRenderFileCmd():
                if bscMethods.OsFile.isExist(serverRenderFile):
                    from LxMaya.command import maFile
                    maFile.fileOpen(serverRenderFile)
            #
            def openRenderFolder():
                bscMethods.OsDirectory.open(renderFolder)
            #
            renderFolder = scenePr.scUnitRenderFolder(
                lxConfigure.LynxiRootIndex_Server,
                projectName,
                sceneCategory, sceneName, sceneVariant, sceneStage,
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
        progressBar.update()
        #
        data = scenePr.getScRenderImageData(
            projectName,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            customize
        )
        if data:
            iconKeyword = 'svg_basic@svg#name'
            stateLabel = none
            treeItem = qtWidgets_.QTreeWidgetItem_()
            #
            if hasattr(parentUi, 'addItem'):
                parentUi.addItem(treeItem)
            elif hasattr(parentUi, 'addChild'):
                parentUi.addChild(treeItem)
                parentUi.setExpanded(True)
            #
            serverRenderFile = scenePr.scUnitRenderFile(
                lxConfigure.LynxiRootIndex_Server,
                projectName, sceneCategory, sceneName, sceneVariant, sceneStage, customize
            )[1]
            localRenderFile = scenePr.scUnitRenderFile(
                lxConfigure.LynxiRootIndex_Local,
                projectName, sceneCategory, sceneName, sceneVariant, sceneStage, customize
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
            showTimeTag = bscMethods.OsFile.mtimeChnPrettify(serverRenderFile)
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
        progressBar = bscObjects.If_Progress(explain, maxValue)
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
        dic = bscCore.orderedDict()
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
        treeItem = qtWidgets_.QTreeWidgetItem_()
        #
        if type(parentUi) == qtWidgets_.QTreeWidget_:
            parentUi.addItem(treeItem)
        elif type(parentUi) == qtWidgets_.QTreeWidgetItem_:
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
                bscMethods.OsDirectory.open(imageFolder)
            #
            def openImageFolderEnabled():
                return bscMethods.OsDirectory.isExist(imageFolder)
            #
            def openImage():
                osCmdExe = 'pdplayer64.exe'
                subOsFiles = bscMethods.OsMultifile.existFiles(imageFile)
                if subOsFiles:
                    subOsFile = subOsFiles[0]
                    osCmd = '''"{}" "{}"'''.format(osCmdExe, subOsFile)
                    bscMethods.OsSystem.runCommand(osCmd)
            #
            def showSizeHistogramWindow():
                win = qtWidgets.QtDialogWindow()
                win.setNameText('Image Size Histogram')
                chart = qtChart_.QtHistogramchart_()
                win.addWidget(chart)

                chart.setDrawData(
                    bscMethods.OsMultifile.fileSizes(
                        fileString=imageFile,
                        frameRange=(startFrame, endFrame)
                    ),
                    (startFrame, 0),
                    ('Frame', 'Size')
                )
                win.uiShow()
            #
            def openImageEnabled():
                pass
            #
            imageFolder = bscMethods.OsFile.dirname(imageFile)
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
            frames = bscMethods.OsMultifile.existFrames(imageFile)
            numRangeArray = bscMethods.Array.toRangecase(frames)
            lineChart.setDrawData(numRangeArray, startFrame, endFrame)
        #
        if index == 0:
            treeItem = parentItem
        else:
            treeItem = qtWidgets_.QTreeWidgetItem_()
            parentItem.addChild(treeItem)
        #
        iconKeyword = 'svg_basic@svg#image'
        #
        explain = imageFile.split('/images')[-1][1:]
        htmlExplain = bscMethods.TxtHtml.toHtmlMayaRenderImage(imagePrefix, explain)
        itemWidget = treeItem.setItemIconWidget(0, iconKeyword, htmlExplain)
        # Action
        setActionData()
        #
        lineChart = qtChart_.QtSequencechart_()
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
