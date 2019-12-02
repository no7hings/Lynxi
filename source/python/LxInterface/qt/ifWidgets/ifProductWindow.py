# coding=utf-8
from LxCore import lxBasic, lxConfigure, lxTip
#
from LxCore.preset import pipePr, personnelPr
#
from LxCore.preset.prod import projectPr
#
from LxUi import uiCore
#
from LxUi.qt import uiWidgets
#
from LxInterface.qt.ifWidgets import ifProductGroup
#
from LxInterface.qt.ifWidgets import ifShelf


#
class IfProjectWindow(uiWidgets.UiDialogWindow):
    _Title = 'Project'
    _Version = lxConfigure.Version().active()
    def __init__(self):
        super(IfProjectWindow, self).__init__()
        #
        self.setDefaultSize(*lxConfigure.LynxiWindow_Size_Default)
        self.setMargins(0, 0, 0, 0)
        #
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setupWindow()
    @uiCore.uiShowMethod_
    def windowShow(self):
        self.uiShow()
    #
    def setupWindow(self):
        shelf = ifShelf.IfProjectShelf(self)
        self.addWidget(shelf)


# Artist Panel
class IfPersonnelWindow(uiWidgets.UiDialogWindow):
    user = personnelPr.getUser()
    #
    tips = [
        u"提示：",
        u"1：输入 中文名（ CH - Name ） ；",
        u"2：输入 英文名（ EN - Name ） ；",
        u"3：输入 邮箱（ e - Mail ） ；",
        u"4：选择 工作组（ Team ） ；",
        u"4：点击 Confirm 确认设置...",
    ]
    #
    subTips01 = [
        u"提示：请输入 中文名（ CH - Name ）...",
    ]
    subTips02 = [
        u"提示：请输入 英文名（ EN - Name ）...",
    ]
    subTips03 = [
        u"提示：请输入 邮箱（ e - Mail ）...",
    ]
    subTips04 = [
        u"提示：请输入 工作组（ Team ）...",
    ]
    _Title = 'Personnel'
    _Version = lxConfigure.Version().active()
    def __init__(self, parent=uiCore.getAppWindow()):
        super(IfPersonnelWindow, self).__init__(parent)
        #
        self.setDefaultSize(960, 480)
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        self.setMargins(0, 0, 0, 0)
        #
        self.setupWindow()
        self.getPersonnelUserInfo()
        #
        self.confirmClicked.connect(self.setArtist)
    #
    def setupLeftToolUiBox(self, layout):
        w = 100
        # User Name
        self._userNameLabel = uiWidgets.UiEnterlabel()
        self._userNameLabel.setNameText('User')
        self._userNameLabel.setNameTextWidth(w)
        layout.addWidget(self._userNameLabel, 0, 0, 1, 1)
        #
        self._chNameLabel = uiWidgets.UiEnterlabel()
        self._chNameLabel.setNameText('CH - Name')
        self._chNameLabel.setNameTextWidth(w)
        self._chNameLabel.setEnterEnable(True)
        layout.addWidget(self._chNameLabel, 1, 0, 1, 1)
        #
        self._enNameLabel = uiWidgets.UiEnterlabel()
        self._enNameLabel.setNameText('EN - Name')
        self._enNameLabel.setNameTextWidth(w)
        self._enNameLabel.setEnterEnable(True)
        layout.addWidget(self._enNameLabel, 2, 0, 1, 1)
        #
        self._mailLabel = uiWidgets.UiEnterlabel()
        self._mailLabel.setNameText('E - Mail')
        self._mailLabel.setNameTextWidth(w)
        self._mailLabel.setEnterEnable(True)
        layout.addWidget(self._mailLabel, 3, 0, 1, 1)
        #
        self._teamLabel = uiWidgets.UiEnterlabel()
        self._teamLabel.setNameText('Team')
        self._teamLabel.setNameTextWidth(w)
        self._teamLabel.setChooseEnable(True)
        layout.addWidget(self._teamLabel, 4, 0, 1, 1)
        #
        self._postLabel = uiWidgets.UiEnterlabel()
        self._postLabel.setNameText('Post')
        self._postLabel.setNameTextWidth(w)
        layout.addWidget(self._postLabel, 5, 0, 1, 1)
        #
        self._pcLabel = uiWidgets.UiEnterlabel()
        self._pcLabel.setNameText('PC')
        self._pcLabel.setNameTextWidth(w)
        layout.addWidget(self._pcLabel, 6, 0, 1, 1)
        #
        self._ipLabel = uiWidgets.UiEnterlabel()
        self._ipLabel.setNameText('IP')
        self._ipLabel.setNameTextWidth(w)
        layout.addWidget(self._ipLabel, 7, 0, 1, 1)
    #
    def setupRightToolUiBox(self, layout):
        self._tipLabel = uiWidgets.UiTextBrower()
        self._tipLabel.setEnterEnable(False)
        layout.addWidget(self._tipLabel)
    #
    def setArtistBoxShow(self):
        self._userNameLabel.setDatum(self.user)
        # Team Data
        teamData = personnelPr.getPersonnelTeamLis()
        self._teamLabel.setDatumLis(teamData)
        self._teamLabel.setChoose(lxConfigure.LynxiValue_Unspecified)
        self._postLabel.setDatum(lxConfigure.LynxiValue_Unspecified)
    #
    def getPersonnelUserInfo(self):
        self._userNameLabel.setDatum(self.user)
        teams = personnelPr.getPersonnelTeamLis()
        team = personnelPr.getPersonnelUserTeam(self.user)
        self._teamLabel.setDatumLis(teams)
        self._teamLabel.setChoose(team)
        post = personnelPr.getPersonnelUserPost(self.user)
        self._postLabel.setDatum(post)
        cnName = personnelPr.getPersonnelUserCnName(self.user)
        self._chNameLabel.setDatum(cnName)
        enName = personnelPr.getPersonnelUserEnName(self.user)
        self._enNameLabel.setDatum(enName)
        mail = personnelPr.getPersonnelUserMail(self.user)
        self._mailLabel.setDatum(mail)
        # PC Data
        self._pcLabel.setDatum(personnelPr.getHostName())
        # IP Data
        self._ipLabel.setDatum(personnelPr.getHost())
        # Tip Data
        self._tipLabel.setRule(self.tips)
    #
    def setArtist(self):
        isChecked = True
        user = self._userNameLabel.datum()
        cnName = self._chNameLabel.datum()
        if not cnName:
            isChecked = False
            self._tipLabel.setRule(self.subTips01)
        enName = self._enNameLabel.datum()
        if not enName:
            isChecked = False
            self._tipLabel.setRule(self.subTips02)
        mail = self._mailLabel.datum()
        if not mail:
            isChecked = False
            self._tipLabel.setRule(self.subTips03)
        team = self._teamLabel.datum()
        if team == lxConfigure.LynxiValue_Unspecified:
            isChecked = False
            self._tipLabel.setRule(self.subTips04)
        post = self._postLabel.datum()
        if post:
            pass
        if isChecked:
            personnelPr.setUpdatePersonnelUserSetData(user, cnName, enName, mail, team, post)
            if lxBasic.isMayaApp():
                w = IfToolFloatWindow()
                w.windowShow()
            #
            lxTip.viewMessage(u'提示：', u'设置用户信息成功')
            self.uiQuit()
    @uiCore.uiShowMethod_
    def windowShow(self):
        self.uiShow()
    #
    def setupWindow(self):
        group = uiWidgets.UiVShelfTabGroup()
        self.addWidget(group)
        #
        widget = uiCore.QWidget_()
        group.addTab(widget, 'personnelShelf', 'svg_basic@svg#personnel', u'User Panel （用户面板）')
        layout = uiCore.QHBoxLayout_(widget)
        layout.setAlignment(uiCore.QtCore.Qt.AlignTop)
        #
        leftWidget = uiCore.QWidget_()
        layout.addWidget(leftWidget)
        rightWidget = uiCore.QWidget_()
        layout.addWidget(rightWidget)
        rightWidget.setMaximumWidth(480)
        #
        userLeftLayout = uiCore.QGridLayout_(leftWidget)
        userLeftLayout.setContentsMargins(2, 2, 2, 2)
        userLeftLayout.setAlignment(uiCore.QtCore.Qt.AlignTop)
        self.setupLeftToolUiBox(userLeftLayout)
        #
        userRightLayout = uiCore.QVBoxLayout_(rightWidget)
        userRightLayout.setAlignment(uiCore.QtCore.Qt.AlignTop)
        userRightLayout.setContentsMargins(2, 2, 2, 2)
        self.setupRightToolUiBox(userRightLayout)


#
class IfToolFloatWindow(uiWidgets.UiFloatWindow):
    _Title = 'Lynxi'
    _Version = lxConfigure.Version().active()
    def __init__(self, parent=uiCore.getAppWindow()):
        super(IfToolFloatWindow, self).__init__(parent)
        #
        self.setDefaultSize(160, 320)
        self.setMargins(0, 0, 0, 0)
        #
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setupWindow()
    #
    def setupMenu(self):
        actionDatumLis = (
            ('Basic', ),
            ('Project Option', 'svg_basic@svg#project', True, "from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.IfProjectWindow();w.windowShow()"),
            ('Personnel Option', 'svg_basic@svg#personnel', True, "from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.IfPersonnelWindow();w.windowShow()")
        )
        #
        self.setActionData(actionDatumLis)
    #
    def setupShelf(self):
        presetDic = projectPr.getProjectMayaShelfDataDic()
        if presetDic:
            shelf = uiWidgets.UiVShelfTabGroup()
            self.addWidget(shelf)
            #
            shelfDic = {}
            for k, v in presetDic.items():
                if k.endswith('Shelf'):
                    shelfName = v['shelfName']
                    shelfIcon = v['shelfIcon']
                    shelfTip = v['shelfTip']
                    widget = uiCore.QWidget_()
                    shelf.addTab(widget, k, 'svg_basic@svg#{}'.format(k)[:-5], shelfTip)
                    layout = uiCore.QVBoxLayout_(widget)
                    layout.setContentsMargins(2, 2, 2, 2)
                    #
                    gridView = uiWidgets.UiGridView()
                    layout.addWidget(gridView)
                    gridView.setItemSize(48, 48)
                    shelfDic[k] = gridView
            #
            for k, v in presetDic.items():
                if k.endswith('Tool'):
                    shelfKey = v['shelf']
                    gridView = shelfDic[shelfKey]
                    #
                    toolName = v['toolName']
                    toolIcon = v['toolIcon_']
                    toolCommand = v['toolCommand']
                    toolTip = v['toolTip']
                    helpIcon = v['helpIcon_']
                    helpCommand = v['helpCommand']
                    helpTip = v['helpTip']
                    #
                    iconButton = uiWidgets.UiIconbutton()
                    gridView.addItem(iconButton)
                    iconButton.setName(toolName)
                    iconButton.setIcon(toolIcon, 32, 32, 48, 48)
                    iconButton.setExtendIcon(helpIcon, 16, 16, 24, 24)
                    iconButton.setPressCommand(toolCommand)
                    iconButton.setExtendPressCommand(helpCommand)
                    iconButton.setTooltip(toolTip)
    @uiCore.uiShowMethod_
    def windowShow(self):
        self.uiShow()
    #
    def setupWindow(self):
        self.setupMenu()
        self.setupShelf()


#
class IfToolkitWindow(uiWidgets.UiToolWindow):
    leftBoxWidth = 160
    #
    projectName = projectPr.getMayaProjectName()
    _Title = 'Tool Kit'
    _Version = lxConfigure.Version().active()
    def __init__(self, parent=uiCore.getAppWindow()):
        super(IfToolkitWindow, self).__init__(parent)
        #
        self.setDefaultSize(600, 800)
        self.setMargins(0, 0, 0, 0)
        self.widthSet = 60
        #
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setupWindow()
    @uiCore.uiSetupShowMethod_
    def windowShow(self):
        self.uiShow()
    @staticmethod
    def helpShow():
        helpDirectory = pipePr.mayaHelpDirectory('tool')
        lxBasic.setOsFolderOpen(helpDirectory)
    #
    def setupWindow(self):
        shelf = ifShelf.IfToolKitShelf(self)
        self.addWidget(shelf)


#
class IfProductManagerWindow(uiWidgets.UiWindow):
    _Title = 'Lynxi'
    _Version = lxConfigure.Version().active()
    def __init__(self, parent=uiCore.getAppWindow()):
        super(IfProductManagerWindow, self).__init__(parent)
        #
        self.setDefaultSize(*lxConfigure.LynxiWindow_Size_Default)
        self.setMargins(0, 0, 0, 0)
        #
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setupWindow()
    @uiCore.uiSetupShowMethod_
    def windowShow(self):
        self.uiShow()
    #
    def setupWindow(self):
        shelf = ifShelf.IfProductShelf(self)
        self.addWidget(shelf)


#
class IfAssetManagerWindow(uiWidgets.UiToolWindow):
    _Title = 'Asset Manager'
    _Version = lxConfigure.Version().active()
    def __init__(self, parent=uiCore.getAppWindow()):
        super(IfAssetManagerWindow, self).__init__(parent)
        #
        self.setDefaultSize(*lxConfigure.LynxiWindow_Size_Default)
        self.setMargins(0, 0, 0, 0)
        #
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setupWindow()
    @uiCore.uiSetupShowMethod_
    def windowShow(self):
        self.uiShow()
    @staticmethod
    def helpShow():
        helpDirectory = pipePr.mayaHelpDirectory(lxConfigure.LynxiProduct_Module_Asset)
        lxBasic.setOsFolderOpen(helpDirectory)
    #
    def setupWindow(self):
        shelf = uiWidgets.UiVShelfTabGroup()
        self.addWidget(shelf)
        #
        widget = ifProductGroup.IfAssetProductGroup(self)
        shelf.addTab(
            widget, 'assetGroup', 'svg_basic@svg#asset', u'Asset Manager Panel ( 资产管理面板 )'
        )


#
class IfSceneryManagerWindow(uiWidgets.UiToolWindow):
    _Title = 'Scenery Manager'
    _Version = lxConfigure.Version().active()
    def __init__(self, parent=uiCore.getAppWindow()):
        super(IfSceneryManagerWindow, self).__init__(parent)
        #
        self.setDefaultSize(*lxConfigure.LynxiWindow_Size_Default)
        self.setMargins(0, 0, 0, 0)
        #
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setupWindow()
    @uiCore.uiSetupShowMethod_
    def windowShow(self):
        self.uiShow()
    @staticmethod
    def helpShow():
        helpDirectory = pipePr.mayaHelpDirectory(lxConfigure.LynxiProduct_Module_Scenery)
        lxBasic.setOsFolderOpen(helpDirectory)
    #
    def setupWindow(self):
        shelf = uiWidgets.UiVShelfTabGroup()
        self.addWidget(shelf)
        #
        widget = ifProductGroup.IfSceneryProductGroup(self)
        shelf.addTab(
            widget, 'sceneryGroup', 'svg_basic@svg#scenery', u'Scenery Manager Panel ( 场景管理面板 )'
        )


#
class IfSceneManagerWindow(uiWidgets.UiToolWindow):
    _Title = 'Scene Manager'
    _Version = lxConfigure.Version().active()
    def __init__(self, parent=uiCore.getAppWindow()):
        super(IfSceneManagerWindow, self).__init__(parent)
        #
        self.setDefaultSize(*lxConfigure.LynxiWindow_Size_Default)
        self.setMargins(0, 0, 0, 0)
        #
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setupWindow()
    @uiCore.uiSetupShowMethod_
    def windowShow(self):
        self.uiShow()
    @staticmethod
    def helpShow():
        helpDirectory = pipePr.mayaHelpDirectory(lxConfigure.LynxiProduct_Module_Scene)
        lxBasic.setOsFolderOpen(helpDirectory)
    #
    def setupWindow(self):
        shelf = uiWidgets.UiVShelfTabGroup()
        self.addWidget(shelf)
        #
        widget = ifProductGroup.IfSceneProductGroup(self)
        shelf.addTab(
            widget, 'sceneGroup', 'svg_basic@svg#scene', u'Scene Manager Panel ( 镜头管理面板 )'
        )