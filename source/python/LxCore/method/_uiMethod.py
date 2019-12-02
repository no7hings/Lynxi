# coding:utf-8
import types
#
from LxUi import uiCore
#
from LxCore.config import appConfig
#
from LxUi.qt import uiWidgets
#
from LxCore.method import _osMethod
#
from LxCore.method.basic import _methodBasic


#
class UiSvgMethod(_osMethod.OsFileMethod):
    LynxiOsCompPath_SvgIcon = 'icon/svg_basic'
    LynxiOsExt_Svg = '.svg'
    @classmethod
    def covertSvgSubFile(cls, osSvgFile, data):
        defFillString = '.st0{fill:#DFDFDF;}'
        onFillString = '.st0{fill:#00DFDF;}'
        offFillString = '.st0{fill:#7F7F7F;}'
        curFillString = '.st0{fill:#427FFF;}'
        if defFillString in data:
            osSvgOnFile = osSvgFile[:-len(cls.LynxiOsExt_Svg)] + 'On.svg'
            osSvgOffFile = osSvgFile[:-len(cls.LynxiOsExt_Svg)] + 'Off.svg'
            osSvgCurFile = osSvgFile[:-len(cls.LynxiOsExt_Svg)] + 'Cur.svg'
            #
            if not cls.isOsExistsFile(osSvgOnFile):
                onData = data.replace(defFillString, onFillString)
                cls.writeOsData(onData, osSvgOnFile)
            #
            if not cls.isOsExistsFile(osSvgOffFile):
                offData = data.replace(defFillString, offFillString)
                cls.writeOsData(offData, osSvgOffFile)
            #
            if not cls.isOsExistsFile(osSvgCurFile):
                curData = data.replace(defFillString, curFillString)
                cls.writeOsData(curData, osSvgCurFile)
    @classmethod
    def covertSvgSubFile__(cls, osSvgFile, data):
        defFillString = '.st0{fill:#DFDFDF;}'
        _defFillString = '.st0{fill:#BFBFBF;}'
        if defFillString in data:
            _defData = data.replace(defFillString, _defFillString)
            cls.writeOsData(_defData, osSvgFile)
    @classmethod
    def covertSvgSubFile_(cls, osSvgFile, data):
        defFillString = '.st0{fill:#BFBFBF;}'
        onFillString = '.st0{fill:#FFFFFF;}'
        offFillString = '.st0{fill:#5F5F5F;}'
        curFillString = '.st0{fill:#427FFF;}'
        if defFillString in data:
            osSvgOnFile = osSvgFile[:-len(cls.LynxiOsExt_Svg)] + 'On.svg'
            osSvgOffFile = osSvgFile[:-len(cls.LynxiOsExt_Svg)] + 'Off.svg'
            osSvgCurFile = osSvgFile[:-len(cls.LynxiOsExt_Svg)] + 'Cur.svg'
            #
            if not cls.isOsExistsFile(osSvgOnFile):
                onData = data.replace(defFillString, onFillString)
                cls.writeOsData(onData, osSvgOnFile)
            #
            if not cls.isOsExistsFile(osSvgOffFile):
                offData = data.replace(defFillString, offFillString)
                cls.writeOsData(offData, osSvgOffFile)
            #
            if not cls.isOsExistsFile(osSvgCurFile):
                curData = data.replace(defFillString, curFillString)
                cls.writeOsData(curData, osSvgCurFile)
    @classmethod
    def getOsSvgFileLis(cls):
        developPath = cls._lxDevelopPath()
        osPath = cls._toOsPath([developPath, cls.LynxiOsCompPath_SvgIcon])
        #
        stringLis = cls.getOsFileBasenameLisByPath(osPath)
        if stringLis:
            for i in stringLis:
                if i.endswith('.svg'):
                    if not i.endswith('On.svg') and not i.endswith('Off.svg') and not i.endswith('Cur.svg'):
                        osSvgFile = cls._toOsPath([osPath, i])
                        data = cls.readOsData(osSvgFile)
                        if '<!-- Generator: Adobe Illustrator 22.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->' in data:
                            cls.covertSvgSubFile(osSvgFile, data)
                        else:
                            print 'Error File {}'.format(i)
    @classmethod
    def getOsSvgFileLis_(cls):
        developPath = cls._lxDevelopPath()
        osPath = cls._toOsPath([developPath, cls.LynxiOsCompPath_SvgIcon])
        #
        stringLis = cls.getOsFileBasenameLisByPath(osPath)
        if stringLis:
            for i in stringLis:
                if i.endswith('.svg'):
                    if not i.endswith('On.svg') and not i.endswith('Off.svg') and not i.endswith('Cur.svg'):
                        osSvgFile = cls._toOsPath([osPath, i])
                        data = cls.readOsData(osSvgFile)
                        if '<!-- Generator: Adobe Illustrator 22.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->' in data:
                            cls.covertSvgSubFile_(osSvgFile, data)
                        else:
                            print 'Error File {}'.format(i)
    @classmethod
    def getOsSvgFileLis__(cls):
        developPath = cls._lxDevelopPath()
        osPath = cls._toOsPath([developPath, cls.LynxiOsCompPath_SvgIcon])
        #
        stringLis = cls.getOsFileBasenameLisByPath(osPath)
        if stringLis:
            for i in stringLis:
                if i.endswith('.svg'):
                    if not i.endswith('On.svg') and not i.endswith('Off.svg') and not i.endswith('Cur.svg'):
                        osSvgFile = cls._toOsPath([osPath, i])
                        data = cls.readOsData(osSvgFile)
                        if '<!-- Generator: Adobe Illustrator 22.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->' in data:
                            cls.covertSvgSubFile__(osSvgFile, data)
                        else:
                            print 'Error File {}'.format(i)


#
class UiViewMethod(_methodBasic.LxUiMethodBasic, _methodBasic.LxPathMethodBasic, appConfig.LxUiConfig):
    @classmethod
    def setTreeView(cls, treeBox, treeViewBuildDic, branchViewMethod=None, expandedDic=None):
        def setBranch(parentData):
            parent, parentPath = parentData
            if parentData in treeViewBuildDic:
                branchArray = treeViewBuildDic[parentData]
                for branchData in branchArray:
                    nameString, pathString = branchData
                    treeItem = uiWidgets.UiTreeItem()
                    treeItem.path = pathString
                    treeItem.name = nameString
                    #
                    isExistsParent = parent is not None
                    if isExistsParent:
                        parentItem = treeItemDic[parentPath]
                        parentItem.addChild(treeItem)
                        if parentPath in expandedDic:
                            isExpand = expandedDic[parentPath]
                            parentItem.setExpanded(isExpand)
                    else:
                        if hasattr(treeBox, 'addItem'):
                            treeBox.addItem(treeItem)
                        elif hasattr(treeBox, 'addChild'):
                            treeBox.addChild(treeItem)
                    #
                    treeItemDic[pathString] = treeItem
                    if isinstance(branchViewMethod, types.FunctionType) or isinstance(branchViewMethod, types.ClassType):
                        # noinspection PyCallingNonCallable
                        branchViewMethod(treeItem)
                    #
                    setBranch(branchData)
        #
        treeItemDic = {}
        #
        if not isinstance(expandedDic, dict):
            expandedDic = {}
        #
        rootData = treeViewBuildDic.keys()[0]
        if rootData:
            setBranch(rootData)
    @classmethod
    def setTreeViewListOsFile(cls, treeView, pathString):
        def branchViewMethod(*args):
            treeItem = args[0]
            osPath = treeItem.path[1:]
            osName = treeItem.name
            #
            if cls.isOsExist(osPath):
                if cls.isOsPath(osPath):
                    if ':' in osName:
                        iconKeyword = 'svg_basic@svg#server_root'
                    else:
                        iconKeyword = 'svg_basic@svg#folder'
                else:
                    iconKeyword = 'svg_basic@svg#file'
            else:
                treeItem._setUiPressStatus(uiCore.OffStatus)
                iconKeyword = 'object#unknown'
            #
            treeItem.setName(osName)
            treeItem.setIcon(iconKeyword)
        #
        pathsep = cls.OsFileSep
        #
        treeViewPathLis = cls._toTreeViewPathLis(pathString, pathsep)
        treeViewBuildDic = cls.getTreeViewBuildDic(treeViewPathLis, pathsep)
        #
        if treeViewBuildDic:
            cls.setTreeView(treeView, treeViewBuildDic, branchViewMethod)

    @classmethod
    def setTreeViewListInspection(cls, treeView, checkConfigDic, methodDic, checkObjectLis):
        def setBranch(seq, key, value):
            def setErrorObject():
                pass
            #
            enable, enExplain, chExplain = value
            treeItem = uiWidgets.UiTreeItem()
            treeView.addItem(treeItem)
            #
            treeItem.setName(key)
            treeItem.setNameText(u'{} ( {} )'.format(chExplain, enExplain))
            #
            if enable is True:
                iconKeyword = 'check#check'
                method = methodDic[k]
                errorDic = method(checkObjectLis)
                print errorDic
            else:
                treeItem.setPressable(False)
                iconKeyword = 'check#checkOff'
            #
            treeItem.setIcon(iconKeyword)
            # treeItem.setIcon(cls._lxMayaSvgIconKeyword('mesh'), iconWidth=20, iconHeight=20)
        #
        def setAction():
            actionDatumLis = [
                ('Extend', ),
                ('Recheck Inspection(s)', 'action#refreshMain', True),
                ('Fix Inspection(s)', 'action#fix', True)
            ]
            #
            treeView.setActionData(actionDatumLis)
        #
        treeView.setColorEnable(True)
        #
        for s, (k, v) in enumerate(checkConfigDic.items()):
            setBranch(s, k, v)
        #
        setAction()
