# encoding: utf-8
from LxUi.qt import uiChart_, uiWidgets

#
#
win = uiWidgets.UiDialogWindow()
win.setDefaultSize(720, 720)
win.setNameText('Color Manager')
#
w = uiChart_.xColorChart()
#
win.addWidget(w)
#
win.uiShow()
