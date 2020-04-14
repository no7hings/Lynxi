# coding=utf-8
from LxBasic import bscMethods, bscObjects

from LxScheme import shmOutput
#
from LxPreset import prsConfigure, prsMethods
#
from LxUi import guiCore
#
from LxUi.qt import qtModifiers, qtWidgets, qtCore
#
from LxInterface.qt.ifWidgets import ifProductGroup
#
from LxInterface.qt.ifWidgets import ifShelf


#
class QtIf_ProjectWindow(qtWidgets.QtToolWindow):
    _Title = 'Project'
    _Version = shmOutput.Resource().version
    def __init__(self):
        super(QtIf_ProjectWindow, self).__init__()

        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Default)
        self.setMargins(0, 0, 0, 0)
        #
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setupWindow()
    @qtModifiers.mtdInterfaceShowExclusive
    def windowShow(self):
        self.uiShow()

    def setupWindow(self):
        shelf = ifShelf.QtIf_ProjectShelf(self)
        self.addWidget(shelf)


# Artist Panel
class QtIf_PersonnelWindow(qtWidgets.QtDialogWindow):
    user = bscMethods.OsSystem.username()

    tips = [
        u"提示：",
        u"1：输入 中文名（ CH - Name ） ；",
        u"2：输入 英文名（ EN - Name ） ；",
        u"3：输入 邮箱（ e - Mail ） ；",
        u"4：选择 工作组（ Team ） ；",
        u"4：点击 Confirm 确认设置...",
    ]

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
    _Version = shmOutput.Resource().version
    def __init__(self, parent=qtCore.getAppWindow()):
        super(QtIf_PersonnelWindow, self).__init__(parent)

        self.setDefaultSize(960, 480)
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        self.setMargins(0, 0, 0, 0)

        self.setupWindow()
        self.getPersonnelUserInfo()

        self.confirmClicked.connect(self.setArtist)

    def setupLeftToolUiBox(self, layout):
        w = 100
        # User Name
        self._userNameLabel = qtWidgets.QtEnterlabel()
        self._userNameLabel.setNameText('User')
        self._userNameLabel.setNameTextWidth(w)
        layout.addWidget(self._userNameLabel, 0, 0, 1, 1)

        self._chNameLabel = qtWidgets.QtEnterlabel()
        self._chNameLabel.setNameText('CH - Name')
        self._chNameLabel.setNameTextWidth(w)
        self._chNameLabel.setEnterEnable(True)
        layout.addWidget(self._chNameLabel, 1, 0, 1, 1)

        self._enNameLabel = qtWidgets.QtEnterlabel()
        self._enNameLabel.setNameText('EN - Name')
        self._enNameLabel.setNameTextWidth(w)
        self._enNameLabel.setEnterEnable(True)
        layout.addWidget(self._enNameLabel, 2, 0, 1, 1)

        self._mailLabel = qtWidgets.QtEnterlabel()
        self._mailLabel.setNameText('E - Mail')
        self._mailLabel.setNameTextWidth(w)
        self._mailLabel.setEnterEnable(True)
        layout.addWidget(self._mailLabel, 3, 0, 1, 1)

        self._teamLabel = qtWidgets.QtEnterlabel()
        self._teamLabel.setNameText('Team')
        self._teamLabel.setNameTextWidth(w)
        self._teamLabel.setChooseEnable(True)
        layout.addWidget(self._teamLabel, 4, 0, 1, 1)

        self._postLabel = qtWidgets.QtEnterlabel()
        self._postLabel.setNameText('Post')
        self._postLabel.setNameTextWidth(w)
        layout.addWidget(self._postLabel, 5, 0, 1, 1)

        self._pcLabel = qtWidgets.QtEnterlabel()
        self._pcLabel.setNameText('PC')
        self._pcLabel.setNameTextWidth(w)
        layout.addWidget(self._pcLabel, 6, 0, 1, 1)

        self._ipLabel = qtWidgets.QtEnterlabel()
        self._ipLabel.setNameText('IP')
        self._ipLabel.setNameTextWidth(w)
        layout.addWidget(self._ipLabel, 7, 0, 1, 1)

    def setupRightToolUiBox(self, layout):
        self._tipLabel = qtWidgets.QtTextbrower()
        self._tipLabel.setEnterEnable(False)
        layout.addWidget(self._tipLabel)

    def setArtistBoxShow(self):
        self._userNameLabel.setDatum(self.user)
        # Team Data
        teamData = prsMethods.Personnel.teams()
        self._teamLabel.setDatumLis(teamData)
        self._teamLabel.setChoose(prsConfigure.Utility.DEF_value_preset_unspecified)
        self._postLabel.setDatum(prsConfigure.Utility.DEF_value_preset_unspecified)

    def getPersonnelUserInfo(self):
        self._userNameLabel.setDatum(self.user)
        teams = prsMethods.Personnel.teams()
        team = prsMethods.Personnel.userTeam(self.user)
        self._teamLabel.setDatumLis(teams)
        self._teamLabel.setChoose(team)
        post = prsMethods.Personnel.userPost(self.user)
        self._postLabel.setDatum(post)
        cnName = prsMethods.Personnel.userChnname(self.user)
        self._chNameLabel.setDatum(cnName)
        enName = prsMethods.Personnel.userEngname(self.user)
        self._enNameLabel.setDatum(enName)
        mail = prsMethods.Personnel.userMail(self.user)
        self._mailLabel.setDatum(mail)
        # PC Data
        self._pcLabel.setDatum(bscMethods.OsSystem.hostname())
        # IP Data
        self._ipLabel.setDatum(bscMethods.OsSystem.host())
        # Tip Data
        self._tipLabel.setRule(self.tips)

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
        if team == prsConfigure.Utility.DEF_value_preset_unspecified:
            isChecked = False
            self._tipLabel.setRule(self.subTips04)
        post = self._postLabel.datum()
        if post:
            pass

        if isChecked:
            prsMethods.Personnel.updateUserDatum(user, cnName, enName, mail, team, post)
            if bscMethods.MayaApp.isActive():
                w = QtIf_ToolFloatWindow()
                w.windowShow()
            #
            bscObjects.MessageWindow(u'提示：', u'设置用户信息成功')
            self.uiQuit()
    @qtModifiers.mtdInterfaceShowExclusive
    def windowShow(self):
        self.uiShow()

    def setupWindow(self):
        group = qtWidgets.QtVShelfTabgroup()
        self.addWidget(group)
        #
        widget = qtCore.QWidget_()
        group.addTab(widget, 'personnelShelf', 'svg_basic@svg#personnel', u'User Panel （用户面板）')
        layout = qtCore.QHBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        #
        leftWidget = qtCore.QWidget_()
        layout.addWidget(leftWidget)
        rightWidget = qtCore.QWidget_()
        layout.addWidget(rightWidget)
        rightWidget.setMaximumWidth(480)
        #
        userLeftLayout = qtCore.QGridLayout_(leftWidget)
        userLeftLayout.setContentsMargins(2, 2, 2, 2)
        userLeftLayout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupLeftToolUiBox(userLeftLayout)
        #
        userRightLayout = qtCore.QVBoxLayout_(rightWidget)
        userRightLayout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        userRightLayout.setContentsMargins(2, 2, 2, 2)
        self.setupRightToolUiBox(userRightLayout)


#
class QtIf_ToolFloatWindow(qtWidgets.QtFloatWindow):
    _Title = 'Lynxi'
    _Version = shmOutput.Resource().version
    def __init__(self, parent=qtCore.getAppWindow()):
        super(QtIf_ToolFloatWindow, self).__init__(parent)

        self.setDefaultSize(480, 640)
        self.setMargins(0, 0, 0, 0)

        self.setNameText(self._Title)
        self.setIndexText(self._Version)

        self.setupWindow()

    def setupMenu(self):
        actionDatumLis = (
            ('Basic', ),
            ('Project Option', 'svg_basic@svg#project', True, "from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.QtIf_ProjectWindow();w.windowShow()"),
            ('Personnel Option', 'svg_basic@svg#personnel', True, "from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.QtIf_PersonnelWindow();w.windowShow()")
        )

        self.setActionData(actionDatumLis)

    def setupShelf(self):
        presetDic = prsMethods.Project.mayaShelfDatumDict()
        if presetDic:
            shelf = qtWidgets.QtVShelfTabgroup()
            self.addWidget(shelf)
            #
            shelfDic = {}
            for k, v in presetDic.items():
                if k.endswith('Shelf'):
                    shelfName = v['shelfName']
                    shelfIcon = v['shelfIcon']
                    shelfTip = v['shelfTip']
                    widget = qtCore.QWidget_()
                    shelf.addTab(widget, k, 'svg_basic@svg#{}'.format(k)[:-5], shelfTip)
                    layout = qtCore.QVBoxLayout_(widget)
                    layout.setContentsMargins(2, 2, 2, 2)
                    #
                    gridView = qtWidgets.QtGridview()
                    layout.addWidget(gridView)
                    gridView.setItemSize(56, 56)
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
                    iconButton = qtWidgets.QtIconbutton()
                    gridView.addItem(iconButton)
                    iconButton.setName(toolName)
                    iconButton.setIcon(toolIcon, 40, 40, 56, 56)
                    iconButton.setExtendIcon(helpIcon, 16, 16, 24, 24)
                    iconButton.setPressCommand(toolCommand)
                    iconButton.setExtendPressCommand(helpCommand)
                    iconButton.setTooltip(toolTip)

    def windowShow(self):
        self.uiShow()

    def setupWindow(self):
        self.setupMenu()
        self.setupShelf()


#
class QtIf_ToolkitWindow(qtWidgets.QtToolWindow):
    leftBoxWidth = 160
    #
    projectName = prsMethods.Project.mayaActiveName()
    _Title = 'Toolkit'
    _Version = shmOutput.Resource().version
    def __init__(self, parent=qtCore.getAppWindow()):
        super(QtIf_ToolkitWindow, self).__init__(parent)

        self.setDefaultSize(600, 800)
        self.setMargins(0, 0, 0, 0)
        self.widthSet = 60

        self.setNameText(self._Title)
        self.setIndexText(self._Version)

        self.setupWindow()
    @qtModifiers.mtdAppInterfaceShowExclusive
    def windowShow(self):
        self.uiShow()
    @staticmethod
    def helpShow():
        pass
    #
    def setupWindow(self):
        shelf = ifShelf.IfToolKitShelf(self)
        self.addWidget(shelf)


#
class If_QtProductManagerWindow(qtWidgets.QtWindow):
    _Title = 'Lynxi'
    _Version = shmOutput.Resource().version
    def __init__(self):
        self._initWindow()
        #
        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Default)
        self.setMargins(0, 0, 0, 0)
        #
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setupWindow()
    @qtModifiers.mtdAppInterfaceShowExclusive
    def windowShow(self):
        self.uiShow()
    #
    def setupWindow(self):
        shelf = ifShelf.IfProductShelf(self)
        self.addWidget(shelf)


#
class If_QtAssetManagerWindow(qtWidgets.QtToolWindow):
    _Title = 'Asset Manager'
    _Version = shmOutput.Resource().version
    def __init__(self, parent=qtCore.getAppWindow()):
        super(If_QtAssetManagerWindow, self).__init__(parent)

        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Default)
        self.setMargins(0, 0, 0, 0)
        #
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setupWindow()
    @qtModifiers.mtdAppInterfaceShowExclusive
    def windowShow(self):
        self.uiShow()
    @staticmethod
    def helpShow():
        pass
    #
    def setupWindow(self):
        shelf = qtWidgets.QtVShelfTabgroup()
        self.addWidget(shelf)
        #
        widget = ifProductGroup.IfAssetProductGroup(self)
        shelf.addTab(
            widget, 'assetGroup', 'svg_basic@svg#asset', u'Asset Manager Panel ( 资产管理面板 )'
        )


#
class If_QtSceneryManagerWindow(qtWidgets.QtToolWindow):
    _Title = 'Scenery Manager'
    _Version = shmOutput.Resource().version
    def __init__(self, parent=qtCore.getAppWindow()):
        super(If_QtSceneryManagerWindow, self).__init__(parent)

        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Default)
        self.setMargins(0, 0, 0, 0)
        #
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setupWindow()
    @qtModifiers.mtdAppInterfaceShowExclusive
    def windowShow(self):
        self.uiShow()
    @staticmethod
    def helpShow():
        pass
    #
    def setupWindow(self):
        shelf = qtWidgets.QtVShelfTabgroup()
        self.addWidget(shelf)
        #
        widget = ifProductGroup.IfSceneryProductGroup(self)
        shelf.addTab(
            widget, 'sceneryGroup', 'svg_basic@svg#scenery', u'Scenery Manager Panel ( 场景管理面板 )'
        )


#
class If_QtSceneManagerWindow(qtWidgets.QtToolWindow):
    _Title = 'Scene Manager'
    _Version = shmOutput.Resource().version
    def __init__(self, parent=qtCore.getAppWindow()):
        super(If_QtSceneManagerWindow, self).__init__(parent)

        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Default)
        self.setMargins(0, 0, 0, 0)
        #
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setupWindow()
    @qtModifiers.mtdAppInterfaceShowExclusive
    def windowShow(self):
        self.uiShow()
    @staticmethod
    def helpShow():
        pass
    #
    def setupWindow(self):
        shelf = qtWidgets.QtVShelfTabgroup()
        self.addWidget(shelf)
        #
        widget = ifProductGroup.IfSceneProductGroup(self)
        shelf.addTab(
            widget, 'sceneGroup', 'svg_basic@svg#scene', u'Scene Manager Panel ( 镜头管理面板 )'
        )
