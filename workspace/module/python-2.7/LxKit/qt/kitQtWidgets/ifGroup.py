# coding:utf-8
from LxBasic import bscObjects

from LxScheme import shmOutput

from LxPreset import prsConfigure, prsMethods
#
from .. import kitQtWgtAbs
#
from ..kitQtWidgets import ifUnit, _kitQtWgtUtilityUnit
#
none = ''


#
class QtIf_ProjectGroup(kitQtWgtAbs.AbsKitQtWgtGroup):
    def __init__(self, mainWindow=None):
        super(QtIf_ProjectGroup, self).__init__(mainWindow)
        self._initAbsKitQtWgtGroup()
        self._mainWindow = mainWindow
        #
        self.setupGroup()
    #
    def setupGroup(self):
        def setupOverviewUnitFnc_():
            unit = ifUnit.QtIf_ProjectOverviewUnit()
            unit.setConnectObject(self)
            #
            self.addTab(
                unit, 'Overview', 'svg_basic/project', u'Project Overview （项目总览）'
            )
            unit.refreshMethod()
            #
            self._mainWindow.confirmClicked.connect(unit.confirmCmd)
        #
        self._shelfTabWgtObj = self.chooseTab()
        self._shelfTabWgtObj.setDatumLis(
            [prsConfigure.Utility.VAR_value_pipeline_default]
        )
        #
        guiBuildFncList = [
            setupOverviewUnitFnc_
        ]
        if self._mainWindow:
            explain = '''Build Project Unit(s)'''
            maxValue = len(guiBuildFncList)
            progressBar = bscObjects.ProgressWindow(explain, maxValue)
            for i in guiBuildFncList:
                progressBar.update()
                i()


#
class IfPersonnelGroup(kitQtWgtAbs.AbsKitQtWgtGroup):
    userLevel = prsMethods.Personnel.userLevel()
    def __init__(self, mainWindow=None):
        super(IfPersonnelGroup, self).__init__(mainWindow)
        self._initAbsKitQtWgtGroup()
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
                unit, 'Register', 'svg_basic/personnel', u'Personnel Register （人员登记）'
            )
            unit.refreshMethod()
        #
        def setupOverviewUnitFnc_():
            unit = ifUnit.IfPersonnelOverviewUnit()
            unit.setConnectObject(self)
            self.addTab(
                unit, 'Overview', 'svg_basic/personnel', u'Personnel Overview （人员总览）'
            )
            unit.refreshMethod()
        #
        self._shelfTabWgtObj = self.chooseTab()
        self._shelfTabWgtObj.setDatumLis(
            [prsConfigure.Utility.VAR_value_pipeline_default]
        )
        #
        guiBuildFncList = [
            setupRegisterUnit,
            setupOverviewUnitFnc_
        ]
        if self._mainWindow:
            explain = '''Build Personnel Unit(s)'''
            maxValue = len(guiBuildFncList)
            progressBar = bscObjects.ProgressWindow(explain, maxValue)
            for i in guiBuildFncList:
                progressBar.update()
                i()


#
class IfToolkitGroup(kitQtWgtAbs.AbsKitQtWgtGroup):
    VAR_kit__qt_wgt__group__name = 'toolkit_group'
    VAR_kit__qt_wgt__group__uiname = 'Toolkit Group'
    VAR_kit__qt_wgt__group__icon = 'svg_basic/toolshelf'
    VAR_kit__qt_wgt__group__tip = u'Toolkit Group （工具组件）'

    def __init__(self, mainWindow=None):
        super(IfToolkitGroup, self).__init__(mainWindow)
        self._initAbsKitQtWgtGroup()
        self._mainWindow = mainWindow
        #
        self.setupGroup()
    #
    def setupGroup(self):
        def setupOverviewUnitFnc_():
            _unitWgtObj = _kitQtWgtUtilityUnit.IfToolkitOverviewUnit()
            _unitWgtObj.setConnectObject(self)
            #
            self.addTab(
                _unitWgtObj,
                _unitWgtObj.VAR_kit__qt_wgt__unit__uiname,
                _unitWgtObj.VAR_kit__qt_wgt__unit__icon,
                _unitWgtObj.VAR_kit__qt_wgt__unit__tip
            )
            _unitWgtObj.refreshMethod()
        #
        self._shelfTabWgtObj = self.chooseTab()

        self._shelfTabWgtObj.setIcon('svg_basic/setting')

        self._shelfTabWgtObj.setDatumLis(
            [shmOutput.Scheme().toString()]
        )
        #
        guiBuildFncList = [
            setupOverviewUnitFnc_
        ]
        if self._mainWindow:
            explain = '''Build Toolkit Unit(s)'''
            maxValue = len(guiBuildFncList)
            progressBar = bscObjects.ProgressWindow(explain, maxValue)
            for i in guiBuildFncList:
                progressBar.update()
                i()
