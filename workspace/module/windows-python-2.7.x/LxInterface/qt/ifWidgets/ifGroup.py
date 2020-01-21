# coding:utf-8
from LxBasic import bscObjects

from LxCore import lxConfigure

from LxPreset import prsMethods
#
from LxInterface.qt.qtIfBasic import _qtIfAbcWidget
#
from LxInterface.qt.ifWidgets import ifUnit
#
none = ''


#
class QtIf_ProjectGroup(_qtIfAbcWidget.QtIfAbc_Group):
    def __init__(self, mainWindow=None):
        super(QtIf_ProjectGroup, self).__init__(mainWindow)
        self._initIfAbcGroup()
        self._mainWindow = mainWindow
        #
        self.setupGroup()
    #
    def setupGroup(self):
        def setupOverviewUnit():
            unit = ifUnit.QtIf_ProjectOverviewUnit()
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
            [lxConfigure.Lynxi_Def_Value_Pipeline]
        )
        #
        buildMethodLis = [
            setupOverviewUnit
        ]
        if self._mainWindow:
            explain = '''Build Project Unit(s)'''
            maxValue = len(buildMethodLis)
            progressBar = bscObjects.If_Progress(explain, maxValue)
            for i in buildMethodLis:
                progressBar.update()
                i()


#
class IfPersonnelGroup(_qtIfAbcWidget.QtIfAbc_Group):
    userLevel = prsMethods.Personnel.userLevel()
    def __init__(self, mainWindow=None):
        super(IfPersonnelGroup, self).__init__(mainWindow)
        self._initIfAbcGroup()
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
            [lxConfigure.Lynxi_Def_Value_Pipeline]
        )
        #
        buildMethodLis = [
            setupRegisterUnit,
            setupOverviewUnit
        ]
        if self._mainWindow:
            explain = '''Build Personnel Unit(s)'''
            maxValue = len(buildMethodLis)
            progressBar = bscObjects.If_Progress(explain, maxValue)
            for i in buildMethodLis:
                progressBar.update()
                i()


#
class IfToolkitGroup(_qtIfAbcWidget.QtIfAbc_Group):
    def __init__(self, mainWindow=None):
        super(IfToolkitGroup, self).__init__(mainWindow)
        self._initIfAbcGroup()
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
            [lxConfigure.Lynxi_Def_Value_Pipeline]
        )
        #
        buildMethodLis = [
            setupOverviewUnit
        ]
        if self._mainWindow:
            explain = '''Build Toolkit Unit(s)'''
            maxValue = len(buildMethodLis)
            progressBar = bscObjects.If_Progress(explain, maxValue)
            for i in buildMethodLis:
                progressBar.update()
                i()
