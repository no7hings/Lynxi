# coding:utf-8
from LxBasic import bscObjects, bscMethods
#
from LxPreset import prsMethods
#
from LxCore.preset.prod import projectPr
#
from LxInterface.qt.qtIfBasic import _qtIfAbcWidget
#
from LxInterface.qt.ifWidgets import ifUnit
#
from LxInterface.qt.ifWidgets import ifProductUnit
#
none = ''


#
class IfAssetProductGroup(_qtIfAbcWidget.QtIfAbc_Group):
    userLevel = prsMethods.Personnel.userLevel()
    def __init__(self, mainWindow=None):
        super(IfAssetProductGroup, self).__init__(mainWindow)
        self._initIfAbcGroup()
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
                unit.setProductModule(prsMethods.Asset.moduleName())
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
            if bscMethods.MayaApp.isActive():
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
                progressBar = bscObjects.If_Progress(explain, maxValue)
                for i in buildMethodLis:
                    progressBar.update()
                    #
                    method, args, autoLoad = i
                    method(*args)
        #
        self._projectChooseTab = self.chooseTab()
        setMain()


#
class IfSceneryProductGroup(_qtIfAbcWidget.QtIfAbc_Group):
    userLevel = prsMethods.Personnel.userLevel()
    def __init__(self, mainWindow=None):
        super(IfSceneryProductGroup, self).__init__(mainWindow)
        self._initIfAbcGroup()
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
                unit.setProductModule(prsMethods.Scenery.moduleName())
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
            if bscMethods.MayaApp.isActive():
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
                progressBar = bscObjects.If_Progress(explain, maxValue)
                for i in buildMethodLis:
                    progressBar.update()
                    #
                    method, args, autoLoad = i
                    method(*args)
        #
        self._projectChooseTab = self.chooseTab()
        setMain()


#
class IfSceneProductGroup(_qtIfAbcWidget.QtIfAbc_Group):
    userLevel = prsMethods.Personnel.userLevel()
    def __init__(self, mainWindow=None):
        super(IfSceneProductGroup, self).__init__(mainWindow)
        self._initIfAbcGroup()
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
                unit.setProductModule(prsMethods.Scene.moduleName())
                unit.setConnectObject(self)
                #
                self.addTab(
                    unit, name, iconkeyword, tooltip
                )
                unit.refreshMethod()
        #
        def setMain():
            projectName = projectPr.getAppProjectName()
            if bscMethods.MayaApp.isActive():
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
                progressBar = bscObjects.If_Progress(explain, maxValue)
                for i in buildMethodLis:
                    progressBar.update()
                    #
                    method, args, autoLoad = i
                    method(*args)
        #
        self._projectChooseTab = self.chooseTab()
        setMain()
