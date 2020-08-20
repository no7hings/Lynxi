# coding:utf-8
from LxCore.config import appConfig
#
from LxGui.qt import qtCore


#
class AbsKitQtShelfObj(object):
    def _initAbsKitQtShelfObj(self):
        self._initAbsKitQtShelfObjAttr()
    #
    def _initAbsKitQtShelfObjAttr(self):
        pass


#
class AbsKitQtGroupObj(object):
    VAR_kit__qt_wgt__group__name = None
    VAR_kit__qt_wgt__group__uiname = None
    VAR_kit__qt_wgt__group__icon = None
    VAR_kit__qt_wgt__group__tip = None

    def _initAbsKitQtGroupObj(self):
        self._initAbsGuiQtGroupObjAttr()
    #
    def _initAbsGuiQtGroupObjAttr(self):
        pass


# Unit Basic
class AbsKitQtUnitObj(object):
    VAR_kit__qt_wgt__unit__name = None
    VAR_kit__qt_wgt__unit__uiname = None
    VAR_kit__qt_wgt__unit__icon = None
    VAR_kit__qt_wgt__unit__tip = None

    UnitWidth = 400
    UnitHeight = 800
    #
    UnitActionDatumLis = []
    #
    UnitConnectLinks = []
    def _initAbsKitQtUnitObj(self):
        self._initUnitAbsAttr()
        self._initUnitAbsVar()
        self._initUnitAbsUi()
    #
    def _initUnitAbsAttr(self):
        self._connectObject = None
    #
    def _initUnitAbsVar(self):
        # Thread
        self._methodLis = []
        self._timerLis = []
        self._threadLis = []
        # Tag Filter
        self._tagLis = []
        self._tagFilterEnableDic = {}
        self._tagFilterIndexDic = {}
        self._tagFilterSubExplainDic = {}
        #
        self._userTagFilterFilepathStr = None
        self._userTagFilterEnableDic = {}
        #
        self._shareIconIndexFile = None
    #
    def _initUnitAbsUi(self):
        self._uiTitle = None
        self._uiIconKeyword = None
        self._uiIcon = None
        #
        self._wgt__frame_w_, self._wgt__frame_h_ = 0, 0
    @staticmethod
    def runPythonCommand(pythonCommand):
        exec pythonCommand
    #
    def setTitle(self, string):
        self._uiTitle = string
    #
    def title(self):
        return self._uiTitle
    #
    def setIcon(self, string):
        self._uiIconKeyword = string
        if self._uiIconKeyword is not None:
            self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword)
        else:
            self._uiIcon = None
    #
    def icon(self):
        return self._uiIcon
    #
    def setSize(self, width, height):
        self._wgt__frame_w_, self._wgt__frame_h_ = width, height
    #
    def size(self):
        return self._wgt__frame_w_, self._wgt__frame_h_
    #
    def setConnectObject(self, classObject):
        self._connectObject = classObject
    #
    def connectObject(self):
        return self._connectObject
    # For Override
    def refreshMethod(self):
        pass
    #
    def quitMethod(self):
        self.setTimerClear()
    #
    def setTimerClear(self):
        if self._timerLis:
            for i in self._timerLis:
                i.stop()
                i.deleteLater()
    #
    def setStartThread(self):
        def setBranch(index, method):
            def threadMethod():
                def timerMethod():
                    thread.setThreadEnable(True)
                    #
                    thread.start()
                    timer.stop()
                #
                if thread.isStarted() is False:
                    timer.start(10000 + index * 100)
                    timer.timeout.connect(timerMethod)
                else:
                    timer.start(10000)
                #
                thread.setStarted(True)
                #
                method()
                #
                thread.setThreadEnable(False)
                #
                thread.wait()
            #
            timer = qtCore.CLS_timer(self)
            self._timerLis.append(timer)
            #
            thread = qtCore.QThread_(self)
            self._threadLis.append(thread)
            #
            thread.setThreadIndex(index)
            thread.started.connect(threadMethod)
            thread.start()
        #
        self._threadLis = []
        self._timerLis = []
        #
        if self._methodLis:
            for seq, i in enumerate(self._methodLis):
                i()
                setBranch(seq, i)


# Maya Tool Unit Basic
class IfToolUnitAbs(AbsKitQtUnitObj):
    def _initToolUnitAbs(self):
        self._initAbsKitQtUnitObj()
        #
        self._initBasicToolUnitAbsAttr()
        self._initBasicToolUnitAbsVar()
        self._initBasicToolUnitAbsUi()
    #
    def _initBasicToolUnitAbsAttr(self):
        self._scriptJobWindowName = None
    #
    def _initBasicToolUnitAbsVar(self):
        pass
    #
    def _initBasicToolUnitAbsUi(self):
        pass
    #
    def setConnectObject(self, classObject):
        self._connectObject = classObject
        if hasattr(self.connectObject(), 'setQuitConnect'):
            self.connectObject().setQuitConnect(self.delScriptJob)
    #
    def setScriptJobWindowName(self, string):
        self._scriptJobWindowName = string
    #
    def UnitScriptJobWindowName(self):
        return self._scriptJobWindowName
    #
    def setScriptJob(self):
        pass
    #
    def delScriptJob(self):
        pass


# custom tool unit *************************************************************************************************** #
class AbsKitQtCustomToolUnitObj(object):
    def _initAbsKitCustomUnitObj(self, *args):
        pass
