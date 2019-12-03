# encoding: utf-8
from LxUi.qt import qtChart_, qtWidgets

#
#
win = qtWidgets.UiDialogWindow()
win.setDefaultSize(720, 720)
win.setNameText('Color Manager')
#
w = qtChart_.QtColorchart_()
#
win.addWidget(w)
#
win.uiShow()
