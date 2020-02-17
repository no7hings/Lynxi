# coding=utf-8
from LxBasic import bscObjects

from LxScheme import shmOutput
#
from LxPreset import prsMethods
#
from LxInterface.qt.qtIfBasic import _qtIfAbcWidget
#
from LxInterface.qt.ifWidgets import ifDevelopUnit


#
class IfDevelopGroup(_qtIfAbcWidget.QtIfAbc_Group):
    publishConfig = [
        ('Python Module', ('.pyc', 'module', 'module.pyc')),
        ('Python Tool', ('.py', 'tool', 'tool')),
        ('Icon', ('.png', 'icon', 'icon'))
    ]
    publishComposeKeyConfig = [
        'Python Module',
        'Python Tool',
        'Icon'
    ]
    publishDevelopComposeFolderConfig = [
        'module',
        'tool',
        'icon'
    ]
    publishProductFolderConfig = [
        'module.pyc',
        'tool',
        'icon'
    ]
    publishDevelopExtsConfig = [
        ['.py', '.pyc'],
        ['.py', '.tip'],
        ['.png']
    ]
    #
    developPath = shmOutput.Root().basic.develop

    backupPath = developPath + '/.bck'
    versionPath = backupPath + '/.version'
    filePath = backupPath + '/' + '.file'
    indexPath = backupPath + '/' + '.index'
    historyPath = backupPath + '/' + '.history'
    infoPath = backupPath + '/' + '.info'
    #
    userLevel = prsMethods.Personnel.userLevel()
    def __init__(self, mainWindow=None):
        super(IfDevelopGroup, self).__init__(mainWindow)
        #
        self._mainWindow = mainWindow
        #
        self.setupUnitGroup()
    #
    def setupUnitGroup(self):
        def setupOverviewUnit():
            if self.userLevel > 0:
                unit = ifDevelopUnit.ifDevelopOverviewUnit()
                unit.setConnectObject(self)
                #
                self.addTab(
                    unit, 'Overview', 'svg_basic@svg#pipeline', u'Develop Overview （开发预览）'
                )
                #
                unit.refreshMethod()
                unit.setupUnitAction()
        #
        self._versionTab = self.chooseTab()
        #
        buildMethodLis = [
            setupOverviewUnit
        ]
        if self.mainWindow:
            explain = u'''Build Develop Unit(s)'''
            maxValue = len(buildMethodLis)
            progressBar = bscObjects.ProgressWindow(explain, maxValue)
            for i in buildMethodLis:
                progressBar.update()
                i()
