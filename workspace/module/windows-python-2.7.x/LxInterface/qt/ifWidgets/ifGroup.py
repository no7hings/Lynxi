# coding:utf-8
from LxCore import lxConfigure
from LxUi.qt import qtProgress
#
from LxCore.preset import personnelPr
#
from LxInterface.qt.ifBasic import ifWidgetBasic
#
from LxInterface.qt.ifWidgets import ifUnit
#
none = ''


#
class IfProjectGroup(ifWidgetBasic.IfGroupBasic_):
    def __init__(self, mainWindow=None):
        super(IfProjectGroup, self).__init__(mainWindow)
        self._initBasicGroup()
        self._mainWindow = mainWindow
        #
        self.setupGroup()
    #
    def setupGroup(self):
        def setupOverviewUnit():
            unit = ifUnit.IfProjectOverviewUnit()
            unit.setConnectObject(self)
            #
            self.addTab(
                unit, 'Overview', 'svg_basic@svg#project', u'Project Overview （项目总览）'
            )
            unit.refreshMethod()
            #
            self._mainWindow.confirmClicked.connect(unit.confirmCmd)
        #
        self._pipelineTab = self.chooseTab()
        self._pipelineTab.setDatumLis(
            [lxConfigure.LynxiDefaultPipelineValue]
        )
        #
        buildMethodLis = [
            setupOverviewUnit
        ]
        if self._mainWindow:
            explain = '''Build Project Unit(s)'''
            maxValue = len(buildMethodLis)
            progressBar = qtProgress.viewSubProgress(explain, maxValue)
            for i in buildMethodLis:
                progressBar.updateProgress()
                i()


#
class IfPersonnelGroup(ifWidgetBasic.IfGroupBasic_):
    userLevel = personnelPr.getPersonnelUserLevel()
    def __init__(self, mainWindow=None):
        super(IfPersonnelGroup, self).__init__(mainWindow)
        self._initBasicGroup()
        self._mainWindow = mainWindow
        #
        self.setupGroup()
    #
    def setupGroup(self):
        def setupRegisterUnit():
            unit = ifUnit.IfPersonnelRegisterUnit()
            unit.setConnectObject(self)
            #
            self.addTab(
                unit, 'Register', 'svg_basic@svg#personnel', u'Personnel Register （人员登记）'
            )
            unit.refreshMethod()
        #
        def setupOverviewUnit():
            unit = ifUnit.IfPersonnelOverviewUnit()
            unit.setConnectObject(self)
            self.addTab(
                unit, 'Overview', 'svg_basic@svg#personnel', u'Personnel Overview （人员总览）'
            )
            unit.refreshMethod()
        #
        self._pipelineTab = self.chooseTab()
        self._pipelineTab.setDatumLis(
            [lxConfigure.LynxiDefaultPipelineValue]
        )
        #
        buildMethodLis = [
            setupRegisterUnit,
            setupOverviewUnit
        ]
        if self._mainWindow:
            explain = '''Build Personnel Unit(s)'''
            maxValue = len(buildMethodLis)
            progressBar = qtProgress.viewSubProgress(explain, maxValue)
            for i in buildMethodLis:
                progressBar.updateProgress()
                i()


#
class IfToolkitGroup(ifWidgetBasic.IfGroupBasic_):
    def __init__(self, mainWindow=None):
        super(IfToolkitGroup, self).__init__(mainWindow)
        self._initBasicGroup()
        self._mainWindow = mainWindow
        #
        self.setupGroup()
    #
    def setupGroup(self):
        def setupOverviewUnit():
            unit = ifUnit.IfToolkitUnit()
            unit.setConnectObject(self)
            #
            self.addTab(
                unit, 'Overview', 'svg_basic@svg#toolkit', u'Toolkit Overview Unit ( 工具总览 )'
            )
            unit.refreshMethod()
        #
        self._pipelineTab = self.chooseTab()
        self._pipelineTab.setDatumLis(
            [lxConfigure.LynxiDefaultPipelineValue]
        )
        #
        buildMethodLis = [
            setupOverviewUnit
        ]
        if self._mainWindow:
            explain = '''Build ToolKit Unit(s)'''
            maxValue = len(buildMethodLis)
            progressBar = qtProgress.viewSubProgress(explain, maxValue)
            for i in buildMethodLis:
                progressBar.updateProgress()
                i()
