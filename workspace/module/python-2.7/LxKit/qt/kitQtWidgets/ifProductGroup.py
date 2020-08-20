# coding:utf-8
from LxBasic import bscObjects, bscMethods
#
from LxPreset import prsMethods
#
from .. import kitQtWgtAbs
#
from ..kitQtWidgets import ifUnit, ifProductUnit
#
none = ''


#
class IfAssetProductGroup(kitQtWgtAbs.AbsKitQtWgtGroup):
    userLevel = prsMethods.Personnel.userLevel()
    def __init__(self, mainWindow=None):
        super(IfAssetProductGroup, self).__init__(mainWindow)
        self._initAbsKitQtWgtGroup()
        self._mainWindow = mainWindow
        #
        self.setupGroup()
    #
    def activeName(self):
        return self._projectChooseTab.datum()
    #
    def setupGroup(self):
        def updateAppProjectName():
            if self.mainWindow():
                if self.mainWindow().isVisible():
                    curProjectName = self.activeName()
                    #
                    prsMethods.Project._setAppLocalConfig(curProjectName)
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
                unit._kit__unit__set_build_Action()
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
            projectName = prsMethods.Project.appActiveName()
            #
            if bscMethods.MayaApp.isActive():
                if self.userLevel > 1:
                    projectExtendDatumDic = prsMethods.Project.uidatumDict()
                else:
                    projectExtendDatumDic = prsMethods.Project.uidatumDict(projectName)
            else:
                projectExtendDatumDic = prsMethods.Project.uidatumDict()
            #
            self._projectChooseTab.setExtendDatumDic(projectExtendDatumDic)
            self._projectChooseTab.setChoose(projectName)
            self._projectChooseTab.chooseChanged.connect(updateAppProjectName)
            #
            guiBuildFncList = [
                (overviewUnitMethod, ('Overview', 'svg_basic/asset', u'Asset Overview （资产总览）'), True),
                (registerUnitMethod, ('Register', 'svg_basic/asset', u'Asset Register ( 资产登记 )'), True)
            ]
            if self.mainWindow():
                explain = '''Build Asset Unit(s)'''
                maxValue = len(guiBuildFncList)
                progressBar = bscObjects.ProgressWindow(explain, maxValue)
                for i in guiBuildFncList:
                    progressBar.update()
                    #
                    method, args, autoLoad = i
                    method(*args)
        #
        self._projectChooseTab = self.chooseTab()
        setMain()


#
class IfSceneryProductGroup(kitQtWgtAbs.AbsKitQtWgtGroup):
    userLevel = prsMethods.Personnel.userLevel()
    def __init__(self, mainWindow=None):
        super(IfSceneryProductGroup, self).__init__(mainWindow)
        self._initAbsKitQtWgtGroup()
        self._mainWindow = mainWindow
        #
        self.setupGroup()
    #
    def activeName(self):
        return self._projectChooseTab.datum()
    #
    def setupGroup(self):
        def updateAppProjectName():
            if self.mainWindow():
                if self.mainWindow().isVisible():
                    curProjectName = self.activeName()
                    #
                    prsMethods.Project._setAppLocalConfig(curProjectName)
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
                unit._kit__unit__set_build_Action()
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
            projectName = prsMethods.Project.appActiveName()
            #
            if bscMethods.MayaApp.isActive():
                if self.userLevel > 1:
                    projectExtendDatumDic = prsMethods.Project.uidatumDict()
                else:
                    projectExtendDatumDic = prsMethods.Project.uidatumDict(projectName)
            else:
                projectExtendDatumDic = prsMethods.Project.uidatumDict()
            #
            self._projectChooseTab.setExtendDatumDic(projectExtendDatumDic)
            self._projectChooseTab.setChoose(projectName)
            self._projectChooseTab.chooseChanged.connect(updateAppProjectName)
            #
            guiBuildFncList = [
                (overviewUnitMethod, ('Overview', 'svg_basic/scenery', u'Scenery Overview （场景总览）'), True),
                (registerUnitMethod, ('Register', 'svg_basic/scenery', u'Scenery Register ( 场景登记 )'), True)
            ]
            if self.mainWindow():
                explain = '''Build Scenery Unit(s)'''
                maxValue = len(guiBuildFncList)
                progressBar = bscObjects.ProgressWindow(explain, maxValue)
                for i in guiBuildFncList:
                    progressBar.update()
                    #
                    method, args, autoLoad = i
                    method(*args)
        #
        self._projectChooseTab = self.chooseTab()
        setMain()


#
class IfSceneProductGroup(kitQtWgtAbs.AbsKitQtWgtGroup):
    userLevel = prsMethods.Personnel.userLevel()
    def __init__(self, mainWindow=None):
        super(IfSceneProductGroup, self).__init__(mainWindow)
        self._initAbsKitQtWgtGroup()
        self._mainWindow = mainWindow
        #
        self.setupGroup()
    #
    def activeName(self):
        return self._projectChooseTab.datum()
    #
    def setupGroup(self):
        def updateAppProjectName():
            if self.mainWindow():
                if self.mainWindow().isVisible():
                    curProjectName = self.activeName()
                    #
                    prsMethods.Project._setAppLocalConfig(curProjectName)
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
                unit._kit__unit__set_build_Action()
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
            projectName = prsMethods.Project.appActiveName()
            if bscMethods.MayaApp.isActive():
                if self.userLevel > 1:
                    projectExtendDatumDic = prsMethods.Project.uidatumDict()
                else:
                    projectExtendDatumDic = prsMethods.Project.uidatumDict(projectName)
            else:
                projectExtendDatumDic = prsMethods.Project.uidatumDict()
            #
            self._projectChooseTab.setExtendDatumDic(projectExtendDatumDic)
            self._projectChooseTab.setChoose(projectName)
            self._projectChooseTab.chooseChanged.connect(updateAppProjectName)
            #
            guiBuildFncList = [
                (overviewUnitMethod, ('Overview', 'svg_basic/scene', u'Scene Overview （镜头总览）'), True),
                (registerUnitMethod, ('Register', 'svg_basic/scene', u'Scene Register ( 镜头登记 )'), True)
            ]
            if self.mainWindow():
                explain = '''Build Scene Unit(s)'''
                maxValue = len(guiBuildFncList)
                progressBar = bscObjects.ProgressWindow(explain, maxValue)
                for i in guiBuildFncList:
                    progressBar.update()
                    #
                    method, args, autoLoad = i
                    method(*args)
        #
        self._projectChooseTab = self.chooseTab()
        setMain()
