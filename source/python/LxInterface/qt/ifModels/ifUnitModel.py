# coding:utf-8
from LxCore import lxProgress
#
from LxUi import uiCore
#
from LxCore.method import _presetMethod
#
from LxUi.qt import uiWidgets


#
class IfProductPresetViewModel(_presetMethod.LxPresetMethod):
    def __init__(self, widget, presetView, productModule):
        self._initProductPreset()
        #
        self._widget = widget
        self._presetView = presetView
        self._productModule = productModule
    #
    def widget(self):
        return self._widget
    #
    def _initProductPreset(self):
        self._initProductPresetAttr()
        self._initProductPresetVar()
    #
    def _initProductPresetAttr(self):
        pass
    #
    def _initProductPresetVar(self):
        self._unitItemLis = []
        #
        self._localUnitItemLis = []
        self._localUnitIndexLis = []
        self._localUnitIndexCount = 0
        #
        self._maxUnitNumber = 0
    #
    def _uploadUnit(self, unitItem):
        dbUnitId = unitItem.presetIndex()
        unitIndexDatum = unitItem.presetIndexDatum()
        unitSetDatum = unitItem.presetSetDatum()
        #
        self.setDbProductUnitUpdate(
            self._productModule, dbUnitId,
            unitIndexDatum, unitSetDatum
        )
        # Server Index
        # Local Index
        self._subLocalUnitIndex(dbUnitId)
        #
        self.setUnitStatus(unitItem, uiCore.NormalStatus)
        self.setUnitAction(unitItem)
        # Update Default Set
        self.updateUnitDefaultSet(unitItem, unitSetDatum)
    #
    def _updateUnit(self, unitItem):
        dbUnitId = unitItem.presetIndex()
        unitIndexDatum = unitItem.presetIndexDatum()
        unitSetDatum = unitItem.presetSetDatum()
        #
        self.setDbProductUnitUpdate(
            self._productModule, dbUnitId,
            unitIndexDatum, unitSetDatum
        )
        #
        self.setUnitStatus(unitItem, uiCore.NormalStatus)
        # Update Default Set
        self.updateUnitDefaultSet(unitItem, unitSetDatum)
    #
    def _addLocalUnitIndex(self, dbUnitId):
        if not dbUnitId in self._localUnitIndexLis:
            self._localUnitIndexLis.append(dbUnitId)
            self._localUnitIndexCount += 1
    #
    def _subLocalUnitIndex(self, dbUnitId):
        if dbUnitId in self._localUnitIndexLis:
            self._localUnitIndexLis.remove(dbUnitId)
            self._localUnitIndexCount -= 1
    #
    def _cleanUnitItems(self):
        self._initProductPresetVar()
        self._presetView.cleanItems()
    #
    def _initUnitItems(self):
        self._cleanUnitItems()
        #
        indexDatumLis = self.getDbProductUnitIndexDatumLis(self._productModule)
        if indexDatumLis:
            maxValue = len(indexDatumLis)
            mainWindow = self.widget().connectObject().mainWindow()
            mainWindow.setMaxProgressValue(maxValue)
            for dbUnitId, enable, description in indexDatumLis:
                mainWindow.updateProgress()
                #
                self.addUnitItem(dbUnitId, enable, description)
            #
            self._presetView.setRefresh()
    #
    def setMainAction(self, ui):
        def showAllCmd():
            self._initUnitItems()
        #
        def hideAllCmd():
            self._cleanUnitItems()
        #
        def saveAllCmd():
            if self._unitItemLis:
                progressExplain = '''Update Unit(s)'''
                maxValue = len(self._unitItemLis)
                progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
                for unitItem in self._unitItemLis:
                    progressBar.updateProgress()
                    dbUnitId = unitItem.presetIndex()
                    unitIndexDatum = unitItem.presetIndexDatum()
                    unitSetDatum = unitItem.presetSetDatum()
                    #
                    self.setDbProductUnitUpdate(
                        self._productModule, dbUnitId,
                        unitIndexDatum, unitSetDatum
                    )
                    #
                    unitItem.setDefaultPresetSetDatum(unitSetDatum)
                    self.setUnitStatus(unitItem, uiCore.NormalStatus)
        #
        def reloadAllCmd():
            if self._unitItemLis:
                progressExplain = '''Reload Unit(s)'''
                maxValue = len(self._unitItemLis)
                progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
                for unitItem in self._unitItemLis:
                    progressBar.updateProgress()
                    dbUnitId = unitItem.presetIndex()
                    unitItem.refreshPresetSet(
                        self.getDbProductUnitSetDatum(dbUnitId)
                    )
        #
        def addCmd():
            self.addUnitItem()
            self._presetView.setRefresh()
        #
        actionDatumLis = [
            ('Basic',),
            ('Add Unit', 'svg_basic@svg#addFile', True, addCmd),
            (),
            ('Show All Unit(s)', 'svg_basic@svg#show', True, showAllCmd),
            ('Hide All Unit(s)', 'svg_basic@svg#hide', True, hideAllCmd),
            (),
            ('Save Unit(s)', 'svg_basic@svg#save', True, saveAllCmd),
            ('Reload Unit(s)', 'svg_basic@svg#refresh', True, reloadAllCmd)
        ]
        #
        ui.setActionData(actionDatumLis)
    #
    def setUnitAction(self, unitItem):
        def updateCmd():
            self._updateUnit(unitItem)
        #
        def reloadCmd():
            unitSetDatum = self.getDbProductUnitSetDatum(dbUnitId)
            unitItem.refreshPresetSet(unitSetDatum)
            # Update Default Set
            self.updateUnitDefaultSet(unitItem, unitSetDatum)
        #
        def copyCmd():
            copyUnitDescription = unitItem.description() + ' - Copy'
            #
            copyUnitSetDatum = unitItem.presetSetDatum()
            serverUnitCount = self.getDbProductUnitCount(self._productModule)
            copyUnitSetDatum['name'] = self._toProductUnitName(serverUnitCount + 1)
            #
            self.addUnitItem(
                description=copyUnitDescription, overrideSetDatum=copyUnitSetDatum
            )
            #
            self._presetView.setRefresh()
        #
        dbUnitId = unitItem.presetIndex()
        #
        actionDatumLis = [
            ('Basic',),
            ('Copy Unit', 'svg_basic@svg#copy', True, copyCmd),
            (),
            ('Update Unit', 'svg_basic@svg#update', True, updateCmd),
            ('Reload Unit', 'svg_basic@svg#refresh', True, reloadCmd),
        ]
        unitItem.setActionData(actionDatumLis)
    #
    def setUnitSubAction(self, unitItem):
        def uploadCmd():
            self._uploadUnit(unitItem)
        #
        actionDatumLis = [
            ('Basic',),
            ('Upload Unit', 'svg_basic@svg#upload_action', True, uploadCmd)
        ]
        unitItem.setActionData(actionDatumLis)
    #
    def addUnitItem(self, dbUnitId=None, enable=True, description=u'xxx - A01', overrideSetDatum=None):
        def updateSetChangedCmd():
            if not unitItem in self._localUnitItemLis:
                if unitItem.isPresetSetDatumChanged():
                    unitItem.setFilterColor((255, 0, 63, 255))
                else:
                    unitItem.setFilterColor((95, 95, 95, 255))
        #
        if dbUnitId is None:
            dbUnitId = self.getUniqueId()
        #
        unitItem = uiWidgets.UiPresetItem()
        self.presetView().addItem(unitItem)
        #
        unitItem.setName(dbUnitId), unitItem.setEnable(enable), unitItem.setDescription(description)
        #
        unitItem.setDefaultPresetSetDatum(self.getDbProductUnitSetDatum(dbUnitId))
        #
        self.updateUnitIndex(unitItem)
        self.updateUnitSet(unitItem, overrideSetDatum)
        #
        unitItem.setChanged.connect(updateSetChangedCmd)
    #
    def updateUnitIndex(self, unitItem):
        serverUnitIndexLis = self.getDbProductUnitIndexLis(self._productModule)
        serverUnitCount = len(serverUnitIndexLis)
        #
        dbUnitId = unitItem.presetIndex()
        #
        if dbUnitId in serverUnitIndexLis:
            unitNumber = serverUnitIndexLis.index(dbUnitId) + 1
            #
            self.setUnitStatus(unitItem, uiCore.NormalStatus)
            #
            self.setUnitAction(unitItem)
            #
            if unitItem in self._localUnitItemLis:
                self._localUnitItemLis.remove(unitItem)
        else:
            self._addLocalUnitIndex(dbUnitId)
            #
            unitNumber = serverUnitCount + self._localUnitIndexLis.index(dbUnitId) + 1
            #
            self.setUnitStatus(unitItem, uiCore.OnStatus)
            #
            self.setUnitSubAction(unitItem)
            #
            if not unitItem in self._localUnitItemLis:
                self._localUnitItemLis.append(unitItem)
        #
        if not unitItem in self._unitItemLis:
            self._maxUnitNumber += 1
            self._unitItemLis.append(unitItem)
        # Number
        unitItem.setIndexText(unitNumber)
    #
    def updateUnitSet(self, unitItem, overrideSetDatum=None):
        projectName = self.widget().connectObject().getProjectName()
        dbUnitId = unitItem.presetIndex()
        unitNumber = unitItem.presetNumber()
        unitSetDatum = self.getDbProductUnitSetUiDatum(
            projectName, self._productModule,
            dbUnitId, unitNumber
        )
        unitItem.setupPresetSet(unitSetDatum)
        if overrideSetDatum is not None:
            unitItem.refreshPresetSet(overrideSetDatum)
    @staticmethod
    def setUnitStatus(unitItem, status):
        if status is uiCore.NormalStatus:
            iconKeyword = 'svg_basic@svg#document'
            rgba = 95, 95, 95, 255
        elif status is uiCore.WarningStatus:
            iconKeyword = 'svg_basic@svg#document'
            rgba = 255, 255, 97, 255
        elif status is uiCore.ErrorStatus:
            iconKeyword = 'svg_basic@svg#document'
            rgba = 255, 0, 63, 255
        elif status is uiCore.OnStatus:
            iconKeyword = 'svg_basic@svg#addFile'
            rgba = 63, 255, 127, 255
        else:
            iconKeyword = 'svg_basic@svg#document'
            rgba = 95, 95, 95, 255
        #
        unitItem.setIcon(iconKeyword)
        unitItem.setFilterColor(rgba)
    @staticmethod
    def updateUnitDefaultSet(unitItem, unitSetDatum):
        unitItem.setDefaultPresetSetDatum(unitSetDatum)
        unitItem.setChangedEmit()
    #
    def presetView(self):
        return self._presetView


#
class IfProductUnitRegisterModel(_presetMethod.LxPresetMethod):
    def __init__(self, widget, presetView, productModule):
        self._initProductPreset()
        #
        self._widget = widget
        self._presetView = presetView
        self._productModule = productModule
    #
    def widget(self):
        return self._widget
    #
    def _initProductPreset(self):
        self._initProductPresetAttr()
        self._initProductPresetVar()
    #
    def _initProductPresetAttr(self):
        pass
    #
    def _initProductPresetVar(self):
        self._unitItemLis = []
        #
        self._localUnitItemLis = []
        self._localUnitIndexLis = []
        self._localUnitIndexCount = 0
        #
        self._maxUnitNumber = 0
    #
    def _uploadUnit(self, unitItem):
        dbUnitId = unitItem.presetIndex()
        unitIndexDatum = unitItem.presetIndexDatum()
        unitSetDatum = unitItem.presetSetDatum()
        #
        self.setDbProductUnitUpdate(
            self._productModule, dbUnitId,
            unitIndexDatum, unitSetDatum
        )
        # Server Index
        # Local Index
        self._subLocalUnitIndex(dbUnitId)
        #
        self.setUnitStatus(unitItem, uiCore.NormalStatus)
        self.setUnitAction(unitItem)
        # Update Default Set
        self.updateUnitDefaultSet(unitItem, unitSetDatum)
    #
    def _updateUnit(self, unitItem):
        dbUnitId = unitItem.presetIndex()
        unitIndexDatum = unitItem.presetIndexDatum()
        unitSetDatum = unitItem.presetSetDatum()
        #
        self.setDbProductUnitUpdate(
            self._productModule, dbUnitId,
            unitIndexDatum, unitSetDatum
        )
        #
        self.setUnitStatus(unitItem, uiCore.NormalStatus)
        # Update Default Set
        self.updateUnitDefaultSet(unitItem, unitSetDatum)
    #
    def _addLocalUnitIndex(self, dbUnitId):
        if not dbUnitId in self._localUnitIndexLis:
            self._localUnitIndexLis.append(dbUnitId)
            self._localUnitIndexCount += 1
    #
    def _subLocalUnitIndex(self, dbUnitId):
        if dbUnitId in self._localUnitIndexLis:
            self._localUnitIndexLis.remove(dbUnitId)
            self._localUnitIndexCount -= 1
    #
    def _cleanUnitItems(self):
        self._initProductPresetVar()
        self._presetView.cleanItems()
    #
    def _initUnitItems(self):
        self._cleanUnitItems()
        #
        indexDatumLis = self.getDbProductUnitIndexDatumLis(self._productModule)
        if indexDatumLis:
            maxValue = len(indexDatumLis)
            mainWindow = self.widget().connectObject().mainWindow()
            mainWindow.setMaxProgressValue(maxValue)
            for dbUnitId, enable, description in indexDatumLis:
                mainWindow.updateProgress()
                self.addUnitItem(dbUnitId, enable, description)
            #
            self._presetView.setRefresh()
    #
    def setMainAction(self, ui):
        def showAllCmd():
            self._initUnitItems()
        #
        def hideAllCmd():
            self._cleanUnitItems()
        #
        def saveAllCmd():
            if self._unitItemLis:
                progressExplain = '''Update Unit(s)'''
                maxValue = len(self._unitItemLis)
                progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
                for unitItem in self._unitItemLis:
                    progressBar.updateProgress()
                    dbUnitId = unitItem.presetIndex()
                    unitIndexDatum = unitItem.presetIndexDatum()
                    unitSetDatum = unitItem.presetSetDatum()
                    #
                    self.setDbProductUnitUpdate(
                        self._productModule, dbUnitId,
                        unitIndexDatum, unitSetDatum
                    )
                    #
                    unitItem.setDefaultPresetSetDatum(unitSetDatum)
                    self.setUnitStatus(unitItem, uiCore.NormalStatus)
        #
        def reloadAllCmd():
            if self._unitItemLis:
                progressExplain = '''Reload Unit(s)'''
                maxValue = len(self._unitItemLis)
                progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
                for unitItem in self._unitItemLis:
                    progressBar.updateProgress()
                    dbUnitId = unitItem.presetIndex()
                    unitItem.refreshPresetSet(
                        self.getDbProductUnitSetDatum(dbUnitId)
                    )
        #
        def addCmd():
            self.addUnitItem()
            self._presetView.setRefresh()
        #
        actionDatumLis = [
            ('Basic',),
            ('Add Unit', 'svg_basic@svg#addFile', True, addCmd),
            (),
            ('Show All Unit(s)', 'svg_basic@svg#show', True, showAllCmd),
            ('Hide All Unit(s)', 'svg_basic@svg#hide', True, hideAllCmd),
            (),
            ('Save Unit(s)', 'svg_basic@svg#save', True, saveAllCmd),
            ('Reload Unit(s)', 'svg_basic@svg#refresh', True, reloadAllCmd)
        ]
        #
        ui.setActionData(actionDatumLis)
    #
    def setUnitAction(self, unitItem):
        def updateCmd():
            self._updateUnit(unitItem)
        #
        def reloadCmd():
            unitSetDatum = self.getDbProductUnitSetDatum(dbUnitId)
            unitItem.refreshPresetSet(unitSetDatum)
            # Update Default Set
            self.updateUnitDefaultSet(unitItem, unitSetDatum)
        #
        def copyCmd():
            copyUnitDescription = unitItem.description() + ' - Copy'
            #
            copyUnitSetDatum = unitItem.presetSetDatum()
            serverUnitCount = self.getDbProductUnitCount(self._productModule)
            copyUnitSetDatum['name'] = self._toProductUnitName(serverUnitCount + 1)
            #
            self.addUnitItem(
                description=copyUnitDescription, overrideSetDatum=copyUnitSetDatum
            )
            #
            self._presetView.setRefresh()
        #
        dbUnitId = unitItem.presetIndex()
        #
        actionDatumLis = [
            ('Basic',),
            ('Copy Unit', 'svg_basic@svg#copy', True, copyCmd),
            (),
            ('Update Unit', 'svg_basic@svg#update', True, updateCmd),
            ('Reload Unit', 'svg_basic@svg#refresh', True, reloadCmd),
        ]
        unitItem.setActionData(actionDatumLis)
    #
    def setUnitSubAction(self, unitItem):
        def uploadCmd():
            self._uploadUnit(unitItem)
        #
        actionDatumLis = [
            ('Basic',),
            ('Upload Unit', 'svg_basic@svg#upload_action', True, uploadCmd)
        ]
        unitItem.setActionData(actionDatumLis)
    #
    def addUnitItem(self, dbUnitId=None, enable=True, description=u'xxx - A01', overrideSetDatum=None):
        def updateSetChangedCmd():
            if not unitItem in self._localUnitItemLis:
                if unitItem.isPresetSetDatumChanged():
                    unitItem.setFilterColor((255, 0, 63, 255))
                else:
                    unitItem.setFilterColor((95, 95, 95, 255))
        #
        if dbUnitId is None:
            dbUnitId = self.getUniqueId()
        #
        unitItem = uiWidgets.UiPresetItem()
        self.presetView().addItem(unitItem)
        #
        unitItem.setName(dbUnitId), unitItem.setEnable(enable), unitItem.setDescription(description)
        #
        unitItem.setDefaultPresetSetDatum(self.getDbProductUnitSetDatum(dbUnitId))
        #
        self.updateUnitIndex(unitItem)
        self.updateUnitSet(unitItem, overrideSetDatum)
        #
        unitItem.setChanged.connect(updateSetChangedCmd)
    #
    def updateUnitIndex(self, unitItem):
        serverUnitIndexLis = self.getDbProductUnitIndexLis(self._productModule)
        serverUnitCount = len(serverUnitIndexLis)
        #
        dbUnitId = unitItem.presetIndex()
        #
        if dbUnitId in serverUnitIndexLis:
            unitNumber = serverUnitIndexLis.index(dbUnitId) + 1
            #
            self.setUnitStatus(unitItem, uiCore.NormalStatus)
            #
            self.setUnitAction(unitItem)
            #
            if unitItem in self._localUnitItemLis:
                self._localUnitItemLis.remove(unitItem)
        else:
            self._addLocalUnitIndex(dbUnitId)
            #
            unitNumber = serverUnitCount + self._localUnitIndexLis.index(dbUnitId) + 1
            #
            self.setUnitStatus(unitItem, uiCore.OnStatus)
            #
            self.setUnitSubAction(unitItem)
            #
            if not unitItem in self._localUnitItemLis:
                self._localUnitItemLis.append(unitItem)
        #
        if not unitItem in self._unitItemLis:
            self._maxUnitNumber += 1
            self._unitItemLis.append(unitItem)
        # Number
        unitItem.setIndexText(unitNumber)
    #
    def updateUnitSet(self, unitItem, overrideSetDatum=None):
        projectName = self.widget().connectObject().getProjectName()
        dbUnitId = unitItem.presetIndex()
        unitNumber = unitItem.presetNumber()
        unitSetDatum = self.getDbProductUnitSetUiDatum(
            projectName, self._productModule,
            dbUnitId, unitNumber
        )
        unitItem.setupPresetSet(unitSetDatum)
        if overrideSetDatum is not None:
            unitItem.refreshPresetSet(overrideSetDatum)
    @staticmethod
    def setUnitStatus(unitItem, status):
        if status is uiCore.NormalStatus:
            iconKeyword = 'svg_basic@svg#document'
            rgba = 95, 95, 95, 255
        elif status is uiCore.WarningStatus:
            iconKeyword = 'svg_basic@svg#document'
            rgba = 255, 255, 97, 255
        elif status is uiCore.ErrorStatus:
            iconKeyword = 'svg_basic@svg#document'
            rgba = 255, 0, 63, 255
        elif status is uiCore.OnStatus:
            iconKeyword = 'svg_basic@svg#addFile'
            rgba = 63, 255, 127, 255
        else:
            iconKeyword = 'svg_basic@svg#document'
            rgba = 95, 95, 95, 255
        #
        unitItem.setIcon(iconKeyword)
        unitItem.setFilterColor(rgba)
    @staticmethod
    def updateUnitDefaultSet(unitItem, unitSetDatum):
        unitItem.setDefaultPresetSetDatum(unitSetDatum)
        unitItem.setChangedEmit()
    #
    def presetView(self):
        return self._presetView