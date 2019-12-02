# coding:utf-8
import os
#
import sys
#
from pyfbsdk import *
#
from PySide import QtCore, QtGui, shiboken
#
from pyfbsdk_additions import *
#
toolName = 'Export to Maya'



#
def isMb():
    if os.path.basename(sys.argv[0]) == 'motionbuilder.exe':
        return True
    else:
        return False


#
class mainWin(QtGui.QWidget):
    valueUiData = [
        ('starFrame', 'Start Frame', 'FBSystem().CurrentTake.LocalTimeSpan.GetStart().GetFrame()'),
        ('endFrame', 'End Frame', 'FBSystem().CurrentTake.LocalTimeSpan.GetStop().GetFrame()'),
        ('fps', 'FPS', 'FBPlayerControl().GetTransportFpsValue()')
    ]
    #
    labelWidth = 100
    def __init__(self, parent=None):
        super(mainWin, self).__init__(parent)
        #
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setMinimumWidth(200)
        self.setMinimumHeight(200)
        #
        self.setWindowTitle('Export to Maya')
        #
        self.setupUi()
    #
    def refresh(self):
        for seq, i in enumerate(self.valueUiData):
            key, explain, valueMethod = i
            if isMb():
                command = "value={1};\
                        self.{0}ValueLabel.setValue(value);".format(
                    key, valueMethod
                )
                exec command
    #
    def getDesktop(self):
        import _winreg
        key = _winreg.OpenKey(
            _winreg.HKEY_CURRENT_USER,
            'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        )
        filePath = _winreg.QueryValueEx(key, "Desktop")[0].replace('\\', '/') + '/temp.fbx'
        #
        self._defFilePath = filePath
        return filePath
    #
    def getFilePath(self):
        saveFile = QtGui.QFileDialog.getSaveFileName(self, "Save Folder", self._defFilePath, "*.fbx")[0]
        if saveFile:
            saveFilePath = os.path.dirname(saveFile)
            self._defFilePath = saveFilePath
            #
            self.fileStringLabel.setText(saveFile)
    #
    def setupUi(self):
        mainLayout = QtGui.QGridLayout(self)
        #
        topWidget = QtGui.QWidget()
        mainLayout.addWidget(topWidget, 0, 0, 1, 2)
        #
        topLayout = QtGui.QHBoxLayout(topWidget)
        #
        self.fileStringLabel = QtGui.QLineEdit()
        topLayout.addWidget(self.fileStringLabel)
        self.fileStringLabel.setText(self.getDesktop())
        #
        self.openFolderButton = QtGui.QPushButton()
        topLayout.addWidget(self.openFolderButton)
        self.openFolderButton.setText('File')
        self.openFolderButton.setMinimumWidth(48)
        self.openFolderButton.setMaximumWidth(48)
        self.openFolderButton.clicked.connect(self.getFilePath)
        #
        leftWidget = QtGui.QWidget()
        mainLayout.addWidget(leftWidget, 1, 0, 1, 1)
        #
        leftLayout = QtGui.QGridLayout(leftWidget)
        leftLayout.setAlignment(QtCore.Qt.AlignTop)
        #
        for seq, i in enumerate(self.valueUiData):
            key, explain, valueMethod = i
            command = "{0}Label = QtGui.QLabel();\
            leftLayout.addWidget({0}Label, {3}, 0, 1, 1);\
            {0}Label.setText('{1}' + ' : ');\
            {0}Label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignHCenter);\
            {0}Label.setMinimumWidth({2});\
            {0}Label.setMaximumWidth({2});\
            self.{0}ValueLabel = QtGui.QSpinBox();\
            leftLayout.addWidget(self.{0}ValueLabel, {3}, 1, 1, 1);\
            self.{0}ValueLabel.setMinimum({4});\
            self.{0}ValueLabel.setMaximum({5})".format(
                key, explain, self.labelWidth, seq, -9999, 9999
            )
            exec command
        #
        rightWidget = QtGui.QWidget()
        mainLayout.addWidget(rightWidget, 1, 1, 1, 1)
        rightLayout = QtGui.QVBoxLayout(rightWidget)
        #
        self.treeWidget = QtGui.QTreeWidget()
        rightLayout.addWidget(self.treeWidget)


#
class NativeWidgetHolder(FBWidgetHolder):
    def WidgetCreate(self, pWidgetParent):
        self.mNativeQtWidget = QtGui.QWidget(shiboken.wrapInstance(pWidgetParent, QtGui.QWidget))
        #
        layout = QtGui.QVBoxLayout(self.mNativeQtWidget)
        widget = mainWin()
        layout.addWidget(widget)
        #
        return shiboken.getCppPointer(self.mNativeQtWidget)[0]


#
class NativeQtWidgetTool(FBTool):
    def BuildLayout(self):
        x = FBAddRegionParam(0,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(0,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(0,FBAttachType.kFBAttachBottom,"")
        self.AddRegion("main", "main", x, y, w, h)
        self.SetControl("main", self.mNativeWidgetHolder)
    #
    def __init__(self, name):
        FBTool.__init__(self, name)
        self.mNativeWidgetHolder = NativeWidgetHolder()
        #
        self.BuildLayout()
        #
        self.StartSizeX = 640
        self.StartSizeY = 640



#
FBDestroyToolByName(toolName)
#
if toolName in FBToolList:
    tool = FBToolList[toolName]
    #
    ShowTool(tool)
else:
    tool=NativeQtWidgetTool(toolName)
    FBAddTool(tool)
    #
    ShowTool(tool)