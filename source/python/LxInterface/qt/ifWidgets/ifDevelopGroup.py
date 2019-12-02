# coding=utf-8
from LxCore import lxConfigure, lxProgress
#
from LxCore.preset import personnelPr
#
from LxCore.method import _dbMethod
#
from LxInterface.qt.ifBasic import ifWidgetBasic
#
from LxInterface.qt.ifWidgets import ifDevelopUnit


#
class IfDevelopGroup(ifWidgetBasic.IfGroupBasic_):
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
    developPath = lxConfigure._getLxDevelopPath()
    backupPath = developPath + '/.bck'
    versionPath = backupPath + '/.version'
    filePath = backupPath + '/' + '.file'
    indexPath = backupPath + '/' + '.index'
    historyPath = backupPath + '/' + '.history'
    infoPath = backupPath + '/' + '.info'
    #
    _dbMethod = _dbMethod.DbOsUnitMethod
    #
    userLevel = personnelPr.getPersonnelUserLevel()
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
            explain = '''Build Develop Unit(s)'''
            maxValue = len(buildMethodLis)
            progressBar = lxProgress.viewSubProgress(explain, maxValue)
            for i in buildMethodLis:
                progressBar.updateProgress()
                i()