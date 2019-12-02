# coding:utf-8
import os
import sys
#
from PySide import QtCore, QtGui, shiboken


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
    labelWidth = 120
    def __init__(self, parent=None):
        super(mainWin, self).__init__(parent)
        #
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setMinimumWidth(120)
        self.setMinimumHeight(120)
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
        self.setSaveFile()
    #
    def getDesktopFile(self):
        import _winreg
        #
        key = _winreg.OpenKey(
            _winreg.HKEY_CURRENT_USER,
            'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        )
        saveFile = _winreg.QueryValueEx(key, "Desktop")[0].replace('\\', '/') + '/temp.fbx'
        #
        return saveFile
    #
    def getCurrentFile(self):
        command = 'saveFile = FBApplication().FBXFileName'
        exec command
        return saveFile
    #
    def setSaveFile(self):
        if isMb():
            saveFile = self.getCurrentFile()
        else:
            saveFile = self.getDesktopFile()
        #
        if saveFile:
            saveFilePath = os.path.dirname(saveFile)
            #
            self._defFilePath = saveFilePath
            #
            self.fileStringLabel.setText(saveFile)
    #
    def getFilePath(self):
        saveFile = QtGui.QFileDialog.getSaveFileName(self, "Save Fbx", self._defFilePath, "*.fbx")[0]
        if saveFile:
            saveFilePath = os.path.dirname(saveFile)
            #
            self._defFilePath = saveFilePath
            #
            self.fileStringLabel.setText(saveFile)
    #
    def setListExportObject(self):
        treeBox = self.treeWidget
    #
    def setupUi(self):
        mainLayout = QtGui.QVBoxLayout(self)
        mainLayout.setAlignment(QtCore.Qt.AlignTop)
        #
        topWidget = QtGui.QWidget()
        mainLayout.addWidget(topWidget)
        #
        topLayout = QtGui.QGridLayout(topWidget)
        topLayout.setContentsMargins(0, 0, 0, 0)
        topLayout.setSpacing(4)
        #
        self.fileStringLabel = QtGui.QLineEdit()
        topLayout.addWidget(self.fileStringLabel, 0, 0, 1, 1)
        #
        self.openFolderButton = QtGui.QPushButton()
        topLayout.addWidget(self.openFolderButton, 0, 1, 1, 1)
        self.openFolderButton.setText('Fbx')
        self.openFolderButton.setMinimumWidth(48)
        self.openFolderButton.setMaximumWidth(48)
        self.openFolderButton.clicked.connect(self.getFilePath)
        #
        self._refreshButton = QtGui.QPushButton()
        topLayout.addWidget(self._refreshButton, 1, 0, 1, 2)
        self._refreshButton.setText('Refresh')
        self._refreshButton.clicked.connect(self.refresh)
        #
        splitterLayout = QtGui.QSplitter()
        mainLayout.addWidget(splitterLayout)
        #
        leftWidget = QtGui.QWidget()
        splitterLayout.addWidget(leftWidget)
        leftWidget.setMinimumWidth(240)
        leftWidget.setMaximumWidth(240)
        #
        leftLayout = QtGui.QGridLayout(leftWidget)
        leftLayout.setContentsMargins(0, 0, 0, 0)
        leftLayout.setSpacing(4)
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
        splitterLayout.addWidget(rightWidget)
        rightLayout = QtGui.QHBoxLayout(rightWidget)
        rightLayout.setContentsMargins(0, 0, 0, 0)
        rightLayout.setSpacing(4)
        #
        self.treeWidget = QtGui.QTreeWidget()
        rightLayout.addWidget(self.treeWidget)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setColumnWidth(0, 240)
        self.treeWidget.setHeaderLabels(['Root'])



app = QtGui.QApplication(sys.argv)

a = mainWin()
a.refresh()
a.show()

sys.exit(app.exec_())