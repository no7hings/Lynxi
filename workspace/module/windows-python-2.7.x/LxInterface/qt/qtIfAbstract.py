# coding:utf-8
from LxCore.config import appConfig
#
from LxUi.qt import qtCore


#
class IfShelfAbs(object):
    def _initShelfAbs(self):
        self._initShelfAbsAttr()
    #
    def _initShelfAbsAttr(self):
        pass


#
class IfAbcGroupModel(object):
    def _initAbcGroupModel(self):
        self._initAbcGroupModelAttr()
    #
    def _initAbcGroupModelAttr(self):
        pass


# Unit Basic
class IfUnitAbs(object):
    UnitName = None
    UnitTitle = None
    UnitIcon = None
    UnitTooltip = None
    UnitWidth = 400
    UnitHeight = 800
    #
    UnitActionDatumLis = []
    #
    UnitConnectLinks = []
    def _initUnitAbs(self):
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
        self._userTagFilterFile = None
        self._userTagFilterEnableDic = {}
        #
        self._shareIconIndexFile = None
    #
    def _initUnitAbsUi(self):
        self._uiTitle = None
        self._uiIconKeyword = None
        self._uiIcon = None
        #
        self._uiWidth, self._uiHeight = 0, 0
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
        self._uiWidth, self._uiHeight = width, height
    #
    def size(self):
        return self._uiWidth, self._uiHeight
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
class IfToolUnitAbs(IfUnitAbs):
    def _initToolUnitAbs(self):
        self._initUnitAbs()
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

