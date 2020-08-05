# coding=utf-8
from LxBasic import bscMethods, bscObjects

from LxScheme import shmOutput
#
from LxPreset import prsConfigure, prsMethods
#
from LxGui import guiCore
#
from LxGui.qt import qtModifiers, guiQtWidgets, qtCore
#
from ..kitQtWidgets import ifProductGroup, ifShelf


#
class LynxiMainWindow(guiQtWidgets.QtFloatWindow):
    VAR_gui_qt__window_wgt__title = 'Lynxi'
    VAR_kit__window__version = shmOutput.Scheme().version
    def __init__(self, parent=qtCore.getAppWindow()):
        super(LynxiMainWindow, self).__init__(parent)

        self.setDefaultSize(480, 640)
        self.setWidgetMargins(0, 0, 0, 0)

        self.setNameString(self.VAR_gui_qt__window_wgt__title)
        self.setIndexString(self.VAR_kit__window__version)

        self.setupWindow()

    def setupMenu(self):
        actionDatumLis = (
            ('Basic', ),
            ('Project Option', 'svg_basic/project', True, "from LxKit.qt.kitQtWidgets import ifProductWindow;w=ifProductWindow.QtIf_ProjectWindow();w.windowShow()"),
            ('Personnel Option', 'svg_basic/personnel', True, "from LxKit.qt.kitQtWidgets import ifProductWindow;w=ifProductWindow.QtIf_PersonnelWindow();w.windowShow()")
        )

        self.setActionData(actionDatumLis)

    def setupShelf(self):
        presetDic = prsMethods.Project.mayaShelfDatumDict()
        if presetDic:
            shelf = guiQtWidgets.QtVShelfTabgroup()
            self.addWidget(shelf)
            #
            shelfDic = {}
            for k, v in presetDic.items():
                if k.endswith('Shelf'):
                    shelfName = v['shelfName']
                    shelfIcon = v['shelfIcon']
                    shelfTip = v['shelfTip']
                    widget = qtCore.QWidget_()
                    shelf.addTab(widget, k, 'svg_basic/{}'.format(k)[:-5], shelfTip)
                    layout = qtCore.QVBoxLayout_(widget)
                    layout.setContentsMargins(2, 2, 2, 2)
                    #
                    gridView = guiQtWidgets.QtGridview()
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
                    iconButton = guiQtWidgets.QtIconbutton()
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
class QtIf_ProjectWindow(guiQtWidgets.QtToolWindow):
    VAR_gui_qt__window_wgt__title = 'Project'
    VAR_kit__window__version = shmOutput.Scheme().version
    def __init__(self):
        super(QtIf_ProjectWindow, self).__init__()

        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Default)
        self.setWidgetMargins(0, 0, 0, 0)
        #
        self.setNameString(self.VAR_gui_qt__window_wgt__title)
        self.setIndexString(self.VAR_kit__window__version)
        #
        self.setupWindow()
    @qtModifiers.gui_qt__mdf__set_gui_exclusive_show
    def windowShow(self):
        self.uiShow()

    def setupWindow(self):
        shelf = ifShelf.QtIf_ProjectShelf(self)
        self.addWidget(shelf)


# Artist Panel
class QtIf_PersonnelWindow(guiQtWidgets.QtDialogWindow):
    user = bscMethods.OsPlatform.username()

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
    VAR_gui_qt__window_wgt__title = 'Personnel'
    VAR_kit__window__version = shmOutput.Scheme().version
    def __init__(self, parent=qtCore.getAppWindow()):
        super(QtIf_PersonnelWindow, self).__init__(parent)

        self.setDefaultSize(960, 480)
        self.setNameString(self.VAR_gui_qt__window_wgt__title)
        self.setIndexString(self.VAR_kit__window__version)
        self.setWidgetMargins(0, 0, 0, 0)

        self.setupWindow()
        self.getPersonnelUserInfo()

        self.confirmClicked.connect(self.setArtist)

    def setupLeftToolUiBox(self, layout):
        w = 100
        # User Name
        self._userNameLabel = guiQtWidgets.QtValueLine()
        self._userNameLabel.setNameString('User')
        self._userNameLabel.setNameTextWidth(w)
        layout.addWidget(self._userNameLabel, 0, 0, 1, 1)

        self._chNameLabel = guiQtWidgets.QtValueLine()
        self._chNameLabel.setNameString('CH - Name')
        self._chNameLabel.setNameTextWidth(w)
        self._chNameLabel.setEnterEnable(True)
        layout.addWidget(self._chNameLabel, 1, 0, 1, 1)

        self._enNameLabel = guiQtWidgets.QtValueLine()
        self._enNameLabel.setNameString('EN - Name')
        self._enNameLabel.setNameTextWidth(w)
        self._enNameLabel.setEnterEnable(True)
        layout.addWidget(self._enNameLabel, 2, 0, 1, 1)

        self._mailLabel = guiQtWidgets.QtValueLine()
        self._mailLabel.setNameString('E - Mail')
        self._mailLabel.setNameTextWidth(w)
        self._mailLabel.setEnterEnable(True)
        layout.addWidget(self._mailLabel, 3, 0, 1, 1)

        self._teamLabel = guiQtWidgets.QtValueLine()
        self._teamLabel.setNameString('Team')
        self._teamLabel.setNameTextWidth(w)
        self._teamLabel.setChooseEnable(True)
        layout.addWidget(self._teamLabel, 4, 0, 1, 1)

        self._postLabel = guiQtWidgets.QtValueLine()
        self._postLabel.setNameString('Post')
        self._postLabel.setNameTextWidth(w)
        layout.addWidget(self._postLabel, 5, 0, 1, 1)

        self._pcLabel = guiQtWidgets.QtValueLine()
        self._pcLabel.setNameString('PC')
        self._pcLabel.setNameTextWidth(w)
        layout.addWidget(self._pcLabel, 6, 0, 1, 1)

        self._ipLabel = guiQtWidgets.QtValueLine()
        self._ipLabel.setNameString('IP')
        self._ipLabel.setNameTextWidth(w)
        layout.addWidget(self._ipLabel, 7, 0, 1, 1)

    def setupRightToolUiBox(self, layout):
        self._tipLabel = guiQtWidgets.QtTextbrower()
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
        self._pcLabel.setDatum(bscMethods.OsPlatform.hostname())
        # IP Data
        self._ipLabel.setDatum(bscMethods.OsPlatform.host())
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
                w = LynxiMainWindow()
                w.windowShow()
            #
            bscObjects.MessageWindow(u'提示：', u'设置用户信息成功')
            self.uiQuit()
    @qtModifiers.gui_qt__mdf__set_gui_exclusive_show
    def windowShow(self):
        self.uiShow()

    def setupWindow(self):
        group = guiQtWidgets.QtVShelfTabgroup()
        self.addWidget(group)
        #
        widget = qtCore.QWidget_()
        group.addTab(widget, 'personnelShelf', 'svg_basic/personnel', u'User Panel （用户面板）')
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
class KitQtToolkitWindow(guiQtWidgets.QtToolWindow):
    leftBoxWidth = 160
    #
    projectName = prsMethods.Project.mayaActiveName()
    VAR_gui_qt__window_wgt__title = 'Toolkit'
    VAR_kit__window__version = shmOutput.Scheme().version
    def __init__(self, parent=qtCore.getAppWindow()):
        super(KitQtToolkitWindow, self).__init__(parent)

        self.setDefaultSize(600, 800)
        self.setWidgetMargins(0, 0, 0, 0)
        self.widthSet = 60

        self.setNameString(self.VAR_gui_qt__window_wgt__title)
        self.setIndexString(self.VAR_kit__window__version)

        self.setupWindow()

    @qtModifiers.gui_qt__mdf__set_app_gui_exclusive_show
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
class If_QtProductManagerWindow(guiQtWidgets.QtWindow):
    VAR_gui_qt__window_wgt__title = 'Lynxi'
    VAR_kit__window__version = shmOutput.Scheme().version
    def __init__(self):
        self._initWindow()
        #
        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Default)
        self.setWidgetMargins(0, 0, 0, 0)
        #
        self.setNameString(self.VAR_gui_qt__window_wgt__title)
        self.setIndexString(self.VAR_kit__window__version)
        #
        self.setupWindow()

    @qtModifiers.gui_qt__mdf__set_app_gui_exclusive_show
    def windowShow(self):
        self.uiShow()
    #
    def setupWindow(self):
        shelf = ifShelf.IfProductShelf(self)
        self.addWidget(shelf)


#
class If_QtAssetManagerWindow(guiQtWidgets.QtToolWindow):
    VAR_gui_qt__window_wgt__title = 'Asset Manager'
    VAR_kit__window__version = shmOutput.Scheme().version
    def __init__(self, parent=qtCore.getAppWindow()):
        super(If_QtAssetManagerWindow, self).__init__(parent)

        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Default)
        self.setWidgetMargins(0, 0, 0, 0)
        #
        self.setNameString(self.VAR_gui_qt__window_wgt__title)
        self.setIndexString(self.VAR_kit__window__version)
        #
        self.setupWindow()

    @qtModifiers.gui_qt__mdf__set_app_gui_exclusive_show
    def windowShow(self):
        self.uiShow()

    @staticmethod
    def helpShow():
        pass
    #
    def setupWindow(self):
        shelf = guiQtWidgets.QtVShelfTabgroup()
        self.addWidget(shelf)
        #
        widget = ifProductGroup.IfAssetProductGroup(self)
        shelf.addTab(
            widget, 'assetGroup', 'svg_basic/asset', u'Asset Manager Panel ( 资产管理面板 )'
        )


#
class If_QtSceneryManagerWindow(guiQtWidgets.QtToolWindow):
    VAR_gui_qt__window_wgt__title = 'Scenery Manager'
    VAR_kit__window__version = shmOutput.Scheme().version
    def __init__(self, parent=qtCore.getAppWindow()):
        super(If_QtSceneryManagerWindow, self).__init__(parent)

        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Default)
        self.setWidgetMargins(0, 0, 0, 0)
        #
        self.setNameString(self.VAR_gui_qt__window_wgt__title)
        self.setIndexString(self.VAR_kit__window__version)
        #
        self.setupWindow()

    @qtModifiers.gui_qt__mdf__set_app_gui_exclusive_show
    def windowShow(self):
        self.uiShow()

    @staticmethod
    def helpShow():
        pass
    #
    def setupWindow(self):
        shelf = guiQtWidgets.QtVShelfTabgroup()
        self.addWidget(shelf)
        #
        widget = ifProductGroup.IfSceneryProductGroup(self)
        shelf.addTab(
            widget, 'sceneryGroup', 'svg_basic/scenery', u'Scenery Manager Panel ( 场景管理面板 )'
        )


#
class If_QtSceneManagerWindow(guiQtWidgets.QtToolWindow):
    VAR_gui_qt__window_wgt__title = 'Scene Manager'
    VAR_kit__window__version = shmOutput.Scheme().version
    def __init__(self, parent=qtCore.getAppWindow()):
        super(If_QtSceneManagerWindow, self).__init__(parent)

        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Default)
        self.setWidgetMargins(0, 0, 0, 0)
        #
        self.setNameString(self.VAR_gui_qt__window_wgt__title)
        self.setIndexString(self.VAR_kit__window__version)
        #
        self.setupWindow()

    @qtModifiers.gui_qt__mdf__set_app_gui_exclusive_show
    def windowShow(self):
        self.uiShow()

    @staticmethod
    def helpShow():
        pass
    #
    def setupWindow(self):
        shelf = guiQtWidgets.QtVShelfTabgroup()
        self.addWidget(shelf)
        #
        widget = ifProductGroup.IfSceneProductGroup(self)
        shelf.addTab(
            widget, 'sceneGroup', 'svg_basic/scene', u'Scene Manager Panel ( 镜头管理面板 )'
        )
