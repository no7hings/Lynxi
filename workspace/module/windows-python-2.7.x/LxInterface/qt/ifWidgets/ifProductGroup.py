# coding:utf-8
from LxCore import lxBasic
from LxUi.qt import qtCommands
#
from LxCore.preset import personnelPr
#
from LxCore.preset.prod import projectPr
#
from LxInterface.qt.ifBasic import ifWidgetBasic
#
from LxInterface.qt.ifWidgets import ifUnit
#
from LxInterface.qt.ifWidgets import ifProductUnit
#
from LxCore.method import _presetMethod
#
none = ''


#
class IfAssetProductGroup(
    ifWidgetBasic.IfGroupBasic_,
    _presetMethod.LxPresetMethod
):
    userLevel = personnelPr.getPersonnelUserLevel()
    def __init__(self, mainWindow=None):
        super(IfAssetProductGroup, self).__init__(mainWindow)
        self._initBasicGroup()
        self._mainWindow = mainWindow
        #
        self.setupGroup()
    #
    def getProjectName(self):
        return self._projectChooseTab.datum()
    #
    def setupGroup(self):
        def updateAppProjectName():
            if self.mainWindow():
                if self.mainWindow().isVisible():
                    curProjectName = self.getProjectName()
                    #
                    projectPr.setLocalAppProjectPreset(curProjectName)
        #
        def overviewUnitMethod(*args):
            if self.userLevel > 0:
                name, iconkeyword, tooltip = args
                unit = ifProductUnit.IfAssetOverviewUnit()
                unit.setConnectObject(self)
                self.addTab(
                    unit, name, iconkeyword, tooltip
                )
                self._projectChooseTab.chooseChanged.connect(unit.refreshMethod)
                unit.setupUnitAction()
                #
                unit.refreshMethod()
        #
        def registerUnitMethod(*args):
            if self.userLevel > 1:
                name, iconkeyword, tooltip = args
                unit = ifUnit.IfProductUnitRegisterUnit()
                #
                unit.setProductModule(self.LynxiProduct_Module_Asset)
                unit.setConnectObject(self)
                #
                self.addTab(
                    unit, name, iconkeyword, tooltip
                )
                unit.refreshMethod()
        #
        def setMain():
            projectName = projectPr.getAppProjectName()
            #
            if lxBasic.isMayaApp():
                if self.userLevel > 1:
                    projectExtendDatumDic = projectPr.getProjectExtendDatumDic()
                else:
                    projectExtendDatumDic = projectPr.getProjectExtendDatumDic(projectName)
            else:
                projectExtendDatumDic = projectPr.getProjectExtendDatumDic()
            #
            self._projectChooseTab.setExtendDatumDic(projectExtendDatumDic)
            self._projectChooseTab.setChoose(projectName)
            self._projectChooseTab.chooseChanged.connect(updateAppProjectName)
            #
            buildMethodLis = [
                (overviewUnitMethod, ('Overview', 'svg_basic@svg#asset', u'Asset Overview （资产总览）'), True),
                (registerUnitMethod, ('Register', 'svg_basic@svg#asset', u'Asset Register ( 资产登记 )'), True)
            ]
            if self.mainWindow():
                explain = '''Build Asset Unit(s)'''
                maxValue = len(buildMethodLis)
                progressBar = qtCommands.setProgressWindowShow(explain, maxValue)
                for i in buildMethodLis:
                    progressBar.updateProgress()
                    #
                    method, args, autoLoad = i
                    method(*args)
        #
        self._projectChooseTab = self.chooseTab()
        setMain()


#
class IfSceneryProductGroup(
    ifWidgetBasic.IfGroupBasic_,
    _presetMethod.LxPresetMethod
):
    userLevel = personnelPr.getPersonnelUserLevel()
    def __init__(self, mainWindow=None):
        super(IfSceneryProductGroup, self).__init__(mainWindow)
        self._initBasicGroup()
        self._mainWindow = mainWindow
        #
        self.setupGroup()
    #
    def getProjectName(self):
        return self._projectChooseTab.datum()
    #
    def setupGroup(self):
        def updateAppProjectName():
            if self.mainWindow():
                if self.mainWindow().isVisible():
                    curProjectName = self.getProjectName()
                    #
                    projectPr.setLocalAppProjectPreset(curProjectName)
        #
        def overviewUnitMethod(*args):
            if self.userLevel > 0:
                name, iconkeyword, tooltip = args
                unit = ifProductUnit.IfSceneryOverviewUnit()
                unit.setConnectObject(self)
                #
                self.addTab(
                    unit, name, iconkeyword, tooltip
                )
                self._projectChooseTab.chooseChanged.connect(unit.refreshMethod)
                unit.setupUnitAction()
                #
                unit.refreshMethod()
        #
        def registerUnitMethod(*args):
            if self.userLevel > 1:
                name, iconkeyword, tooltip = args
                unit = ifUnit.IfProductUnitRegisterUnit()
                #
                unit.setProductModule(self.LynxiProduct_Module_Scenery)
                unit.setConnectObject(self)
                #
                self.addTab(
                    unit, name, iconkeyword, tooltip
                )
                unit.refreshMethod()
        #
        def setMain():
            projectName = projectPr.getAppProjectName()
            #
            if lxBasic.isMayaApp():
                if self.userLevel > 1:
                    projectExtendDatumDic = projectPr.getProjectExtendDatumDic()
                else:
                    projectExtendDatumDic = projectPr.getProjectExtendDatumDic(projectName)
            else:
                projectExtendDatumDic = projectPr.getProjectExtendDatumDic()
            #
            self._projectChooseTab.setExtendDatumDic(projectExtendDatumDic)
            self._projectChooseTab.setChoose(projectName)
            self._projectChooseTab.chooseChanged.connect(updateAppProjectName)
            #
            buildMethodLis = [
                (overviewUnitMethod, ('Overview', 'svg_basic@svg#scenery', u'Scenery Overview （场景总览）'), True),
                (registerUnitMethod, ('Register', 'svg_basic@svg#scenery', u'Scenery Register ( 场景登记 )'), True)
            ]
            if self.mainWindow():
                explain = '''Build Scenery Unit(s)'''
                maxValue = len(buildMethodLis)
                progressBar = qtCommands.setProgressWindowShow(explain, maxValue)
                for i in buildMethodLis:
                    progressBar.updateProgress()
                    #
                    method, args, autoLoad = i
                    method(*args)
        #
        self._projectChooseTab = self.chooseTab()
        setMain()


#
class IfSceneProductGroup(
    ifWidgetBasic.IfGroupBasic_,
    _presetMethod.LxPresetMethod
):
    userLevel = personnelPr.getPersonnelUserLevel()
    def __init__(self, mainWindow=None):
        super(IfSceneProductGroup, self).__init__(mainWindow)
        self._initBasicGroup()
        self._mainWindow = mainWindow
        #
        self.setupGroup()
    #
    def getProjectName(self):
        return self._projectChooseTab.datum()
    #
    def setupGroup(self):
        def updateAppProjectName():
            if self.mainWindow():
                if self.mainWindow().isVisible():
                    curProjectName = self.getProjectName()
                    #
                    projectPr.setLocalAppProjectPreset(curProjectName)
        #
        def overviewUnitMethod(*args):
            if self.userLevel > 0:
                name, iconkeyword, tooltip = args
                unit = ifProductUnit.IfSceneOverviewUnit()
                unit.setConnectObject(self)
                self.addTab(
                    unit, name, iconkeyword, tooltip
                )
                self._projectChooseTab.chooseChanged.connect(unit.refreshMethod)
                unit.setupUnitAction()
                #
                unit.refreshMethod()
        #
        def registerUnitMethod(*args):
            if self.userLevel > 1:
                name, iconkeyword, tooltip = args
                unit = ifUnit.IfProductUnitRegisterUnit()
                #
                unit.setProductModule(self.LynxiProduct_Module_Scene)
                unit.setConnectObject(self)
                #
                self.addTab(
                    unit, name, iconkeyword, tooltip
                )
                unit.refreshMethod()
        #
        def setMain():
            projectName = projectPr.getAppProjectName()
            if lxBasic.isMayaApp():
                if self.userLevel > 1:
                    projectExtendDatumDic = projectPr.getProjectExtendDatumDic()
                else:
                    projectExtendDatumDic = projectPr.getProjectExtendDatumDic(projectName)
            else:
                projectExtendDatumDic = projectPr.getProjectExtendDatumDic()
            #
            self._projectChooseTab.setExtendDatumDic(projectExtendDatumDic)
            self._projectChooseTab.setChoose(projectName)
            self._projectChooseTab.chooseChanged.connect(updateAppProjectName)
            #
            buildMethodLis = [
                (overviewUnitMethod, ('Overview', 'svg_basic@svg#scene', u'Scene Overview （镜头总览）'), True),
                (registerUnitMethod, ('Register', 'svg_basic@svg#scene', u'Scene Register ( 镜头登记 )'), True)
            ]
            if self.mainWindow():
                explain = '''Build Scene Unit(s)'''
                maxValue = len(buildMethodLis)
                progressBar = qtCommands.setProgressWindowShow(explain, maxValue)
                for i in buildMethodLis:
                    progressBar.updateProgress()
                    #
                    method, args, autoLoad = i
                    method(*args)
        #
        self._projectChooseTab = self.chooseTab()
        setMain()
