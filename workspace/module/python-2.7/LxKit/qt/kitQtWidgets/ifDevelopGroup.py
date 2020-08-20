# coding=utf-8
from LxBasic import bscObjects

from LxScheme import shmOutput
#
from LxPreset import prsMethods
#
from .. import kitQtWgtAbs
#
from ..kitQtWidgets import ifDevelopUnit


#
class IfDevelopGroup(kitQtWgtAbs.AbsKitQtWgtGroup):
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
        self._kit__unit__set_build_Group()
    #
    def _kit__unit__set_build_Group(self):
        def setupOverviewUnitFnc_():
            if self.userLevel > 0:
                unit = ifDevelopUnit.ifDevelopOverviewUnit()
                unit.setConnectObject(self)
                #
                self.addTab(
                    unit, 'Overview', 'svg_basic/pipeline', u'Develop Overview （开发预览）'
                )
                #
                unit.refreshMethod()
                unit._kit__unit__set_build_Action()
        #
        self._versionTab = self.chooseTab()
        #
        guiBuildFncList = [
            setupOverviewUnitFnc_
        ]
        if self.mainWindow:
            explain = u'''Build Develop Unit(s)'''
            maxValue = len(guiBuildFncList)
            progressBar = bscObjects.ProgressWindow(explain, maxValue)
            for i in guiBuildFncList:
                progressBar.update()
                i()
