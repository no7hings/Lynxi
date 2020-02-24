# coding:utf-8
from LxBasic import bscMtdCore, bscMethods
#
from LxUi import uiCore
#
from LxUi.qt import qtCore
#
from LxUi.qt.qtObjects import qtObjModel, qtObjWidget
#
from LxUi.qt._qtModels import _qtMdlItem

#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore
#
_families = uiCore.Lynxi_Ui_Family_Lis


#
class QtMessageWidget(qtCore.QWidget):
    TextMessageType = 0
    IconMessageType = 1
    ImageType = 2
    ImageExplainType = 3
    ImageExplainType2 = 4
    #
    IconColorMessageType = 5
    #
    DrawText = 0
    DrawIcon = 1
    DrawImage1 = 2
    DrawImage2 = 3
    DrawRect = 4
    #
    DrawColor = 5
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtMessageWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        #
        self.initUi()
    #
    def mousePressEvent(self, event):
        isPassThrough = True
        #
        if event.buttons() == QtCore.Qt.LeftButton:
            # Image Switch
            if self._imageSwitchArea is not None and self._imageSwitchData is not None:
                if self._imageSwitchArea.contains(event.pos()):
                    lis = []
                    for i in self._imageSwitchData:
                        rect, backgroundRgba, isSelected, imageDrawData, textDrawData = i
                        if rect.contains(event.pos()):
                            isSelected = True
                            self._imageDrawData = imageDrawData
                            self._topTextDrawData = textDrawData
                        else:
                            isSelected = False
                        #
                        lis.append((rect, backgroundRgba, isSelected, imageDrawData, textDrawData))
                    #
                    self._imageSwitchData = lis
                    #
                    self.update()
                    #
                    isPassThrough = False
            # Open Image
            if self._imageOpenArea is not None and self._imageDrawData is not None:
                if self._imageOpenArea.contains(event.pos()):
                    fileString_, osTempFile, isVedio, image = self._imageDrawData

                    bscMethods.OsFile.openAsTemporary(fileString_, osTempFile)
                    #
                    isPassThrough = False
        #
        if isPassThrough:
            event.ignore()
        else:
            event.accept()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            # Open Image
            if self._imageOpenArea is not None:
                if self._imageOpenArea.contains(event.pos()):
                    self._imageOpenBorderRgba = 255, 127, 63, 255
                    self._uiTextRgba = 255, 127, 63, 255
                    #
                    self._uiTextFrameBackgroundRgba = 71, 71, 71, 255
                    self._uiTextFrameBorderRgba = 255, 127, 63, 255
                else:
                    self._imageOpenBorderRgba = 223, 223, 223, 255
                    self._uiTextRgba = 223, 223, 223, 255
                    #
                    self._uiTextFrameBackgroundRgba = 0, 0, 0, 0
                    self._uiTextFrameBorderRgba = 0, 0, 0, 0
                #
                self.update()
        #
        event.ignore()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix

        borderWidth = 2
        borderRadius = 10
        #
        if self._messages:
            for drawAction, drawData in self._messages:
                if drawAction is self.DrawColor:
                    colorRect, rgba = drawData
                    painter.setBackgroundRgba(rgba)
                    painter.setBorderRgba(self._uiColorBorderRgba)
                    painter.drawRect(colorRect)
                # Icon
                elif drawAction is self.DrawIcon:
                    iconRect, icon = drawData
                    painter.setDrawImage(iconRect, icon)
                # Text
                elif drawAction is self.DrawText:
                    textRect, option, string, italic = drawData
                    #
                    painter.setBackgroundRgba(self._uiBackgroundRgba)
                    painter.setBorderRgba(self._uiNameRgba)
                    if italic is True:
                        painter.setBorderRgba((95, 95, 95, 255))
                    # noinspection PyArgumentEqualDefault
                    painter.setFont(
                        qtCore.qtFont(size=8, weight=50, italic=italic, family=_families[0])
                    )
                    painter.drawText(textRect, option, string)
                # Image1
                elif drawAction is self.DrawImage1:
                    painter.setBackgroundRgba(72, 72, 72, 0)
                    painter.setBorderRgba(self._uiBorderRgba)
                    imageRect, image = drawData
                    if image is not None:
                        painter.drawPixmap(imageRect, image)
                    else:
                        painter.setBackgroundRgba(255, 255, 255, 127)
                        painter.setBorderRgba(self._uiNameRgba)
                        #
                        rect = imageRect
                        x, y = rect.x(), rect.y()
                        w, h = rect.width(), rect.height()
                        r = min(w, h) * .75
                        _placeholderRect = QtCore.QRect(x + (w - r) / 2, y + (h - r) / 2, r, r)
                        painter.setDrawImage(_placeholderRect, qtCore._toLxOsIconFile('svg_basic@svg#empty'))
                    #
                    painter.setBackgroundRgba(72, 72, 72, 0)
                    painter.setBorderRgba(self._uiBorderRgba)
                    painter.drawRect(imageRect)
                # Image2
                elif drawAction is self.DrawImage2:
                    imageRect, image = drawData
                    if image is not None:
                        painter.drawPixmap(imageRect, image)
                    else:
                        painter.setBackgroundRgba(255, 255, 255, 127)
                        painter.setBorderRgba(self._uiNameRgba)
                        #
                        rect = imageRect
                        x, y = rect.x(), rect.y()
                        w, h = rect.width(), rect.height()
                        r = min(w, h) * .75
                        _placeholderRect = QtCore.QRect(x + (w - r) / 2, y + (h - r) / 2, r, r)
                        painter.setDrawImage(_placeholderRect, qtCore._toLxOsIconFile('svg_basic@svg#empty'))
                    #
                    painter.setBackgroundRgba(72, 72, 72, 0)
                    painter.setBorderRgba(self._uiBorderRgba)
                    painter.drawRect(imageRect)
        # Images
        if self._imageRect is not None:
            rect = self._imageRect
            imageDrawData = self._imageDrawData
            if imageDrawData:
                fileString_, osTempFile, isVedio, image = imageDrawData
                if image is not None:
                    painter.drawPixmap(rect, image)
                    # Vedio
                    if isVedio is True:
                        self._imageOpenArea = painter.setDrawPlayPattern(
                            rect,
                            .25,
                            self._uiTextFrameBackgroundRgba, self._imageOpenBorderRgba
                        )
                        #
                        if self._leftTextRect is not None:
                            rect = self._leftTextRect
                            textDrawData = self._leftTextDrawData
                            if textDrawData is not None:
                                painter.setDrawButtonBasic(
                                    rect,
                                    borderWidth, borderRadius,
                                    self._uiTextFrameBackgroundRgba, self._uiTextFrameBorderRgba, 'solid'
                                )
                                option, string, italic = textDrawData
                                painter.setBackgroundRgba(self._uiBackgroundRgba)
                                painter.setBorderRgba(self._uiTextRgba)
                                if italic is True:
                                    painter.setBorderRgba((95, 95, 95, 255))
                                painter.setFont(
                                    qtCore.qtFont(size=12, weight=70, italic=italic, family=_families[0])
                                )
                                painter.drawText(rect, option, string)
                        if self._rightTextRect is not None:
                            rect = self._rightTextRect
                            textDrawData = self._rightTextDrawData
                            if textDrawData is not None:
                                painter.setDrawButtonBasic(
                                    rect,
                                    borderWidth, borderRadius,
                                    self._uiTextFrameBackgroundRgba, self._uiTextFrameBorderRgba, 'solid'
                                )
                                option, string, italic = textDrawData
                                painter.setBackgroundRgba(self._uiBackgroundRgba)
                                painter.setBorderRgba(self._uiTextRgba)
                                if italic is True:
                                    painter.setBorderRgba((95, 95, 95, 255))
                                painter.setFont(
                                    qtCore.qtFont(size=12, weight=70, italic=italic, family=_families[0])
                                )
                                painter.drawText(rect, option, string)
                    else:
                        self._imageOpenArea = None
                else:
                    painter.setBackgroundRgba(255, 255, 255, 127)
                    painter.setBorderRgba(self._uiNameRgba)
                    x, y = rect.x(), rect.y()
                    w, h = rect.width(), rect.height()
                    r = min(w, h) * .75
                    _placeholderRect = QtCore.QRect(x + (w - r)/2, y + (h - r)/2, r, r)
                    painter.setDrawImage(_placeholderRect, qtCore._toLxOsIconFile('svg_basic@svg#empty'))
                #
                painter.setBackgroundRgba(63, 63, 63, 0)
                painter.setBorderRgba(self._uiBorderRgba)
                painter.drawRect(self._imageRect)
        # Image Texts
        if self._topTextRect is not None:
            rect = self._topTextRect
            textDrawData = self._topTextDrawData
            if textDrawData is not None:
                option, string, italic = textDrawData
                painter.setBackgroundRgba(self._uiBackgroundRgba)
                painter.setBorderRgba(self._uiNameRgba)
                if italic is True:
                    painter.setBorderRgba(self._uiBorderRgba)
                # noinspection PyArgumentEqualDefault
                painter.setFont(
                    qtCore.qtFont(size=8, weight=50, italic=italic, family=_families[1])
                )
                painter.drawText(rect, option, string)
        # Image Button
        if self._imageSwitchData is not None:
            painter.setRenderHint(painter.Antialiasing)
            for i in self._imageSwitchData:
                rect, backgroundRgba, isSelected = i[:3]
                painter.setBackgroundRgba(backgroundRgba)
                painter.setBorderRgba([self._uiImageSwitchBorderRgba, self._uiImageSwitchCurBorderRgba][isSelected])
                if isSelected:
                    painter.setPenWidth(2)
                painter.drawEllipse(rect)

        # painter.end()
    #
    def setDatumLis(self, messages, width=200, height=200):
        self._messages = self.getDrawDatum(messages, width, height)
    #
    def setExplainWidth(self, width):
        self._explainWidth = width
        self.update()
    #
    def getDrawDatum(self, messages, width, height):
        lis = []
        if messages:
            width -= 1
            height -= 1
            #
            gap = self._uiSpacing
            side = self._uiSide
            iconWidth, iconHeight = self._uiIconWidth, self._uiIconHeight
            frameWidth, frameHeight = self._uiFrameWidth, self._uiFrameHeight
            colorWidth, colorHeight = self._uiColorWidth, self._uiColorHeight
            #
            xPos = side
            yPos = side
            #
            explainWidth = self._explainWidth
            messageWidth = width - explainWidth - side
            messageHeight = frameHeight
            #
            imageWidth = width - side * 2 - 4
            imageHeight = height - side * 2 - 4
            for messageType, uiData in messages:
                xPos_ = side
                # Text + Text
                if messageType is self.TextMessageType:
                    explain, message = uiData
                    # Text
                    textRect = QtCore.QRect(
                        xPos_, yPos, explainWidth, frameHeight
                    )
                    textOption = QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
                    lis.append((self.DrawText, (textRect, textOption, bscMethods.StrCamelcase.toPrettify(explain) + ' : '), False))
                    xPos_ += explainWidth
                    # Text
                    textRect = QtCore.QRect(
                        xPos_, yPos, messageWidth, messageHeight
                    )
                    textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter | QtCore.Qt.TextWordWrap
                    lis.append((self.DrawText, (textRect, textOption, message, False)))
                    yPos += frameHeight + gap
                # Icon + Text
                elif messageType is self.IconMessageType:
                    iconKeyword, message = uiData
                    # Icon
                    iconRect = QtCore.QRect(
                        xPos_ + (frameWidth - iconWidth) / 2, yPos + (frameHeight - iconHeight) / 2,
                        iconWidth, iconHeight
                    )
                    # State
                    if isinstance(iconKeyword, tuple) or isinstance(iconKeyword, list):
                        iconKeyword, iconState = iconKeyword
                    else:
                        iconState = None
                    # Icon
                    if iconKeyword is None:
                        lis.append((
                            self.DrawIcon,
                            (iconRect, qtCore._toLxOsIconFile('svg_basic@svg#unused'))
                        ))
                    else:
                        if iconState is not None:
                            iconRect = QtCore.QRect(
                                xPos_ + 1, yPos + 1,
                                iconWidth, iconHeight
                            )
                        #
                        lis.append((
                            self.DrawIcon,
                            (iconRect, qtCore._toLxOsIconFile(iconKeyword))
                        ))
                    # State
                    if iconState is not None:
                        subIconRect = QtCore.QRect(
                            xPos_ + frameWidth - iconWidth*.75, yPos + frameWidth - iconWidth*.75,
                            iconWidth*.75, iconHeight*.75
                        )
                        lis.append((
                            self.DrawIcon,
                            (subIconRect, qtCore._toLxOsIconFile('state@svg#{}'.format(iconState)))
                        ))
                    #
                    xPos_ += frameHeight + gap
                    # Text
                    textRect = QtCore.QRect(
                        xPos_, yPos, messageWidth, messageHeight
                    )
                    textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter | QtCore.Qt.TextWordWrap
                    italic = [False, True][iconKeyword is None]
                    lis.append((
                        self.DrawText,
                        (textRect, textOption, message, italic)
                    ))
                    #
                    yPos += frameHeight
                # Icon + Color + Text
                elif messageType is self.IconColorMessageType:
                    rgba, iconKeyword, message = uiData
                    # Color
                    colorRect = QtCore.QRect(
                        xPos_ + (frameWidth - colorWidth) / 2, yPos + (frameHeight - colorHeight) / 2,
                        colorWidth, colorHeight
                    )
                    lis.append((
                        self.DrawColor,
                        (colorRect, rgba)
                    ))
                    xPos_ += frameHeight + gap
                    # Icon
                    iconRect = QtCore.QRect(
                        xPos_ + (frameWidth - iconWidth) / 2, yPos + (frameHeight - iconHeight) / 2,
                        iconWidth, iconHeight
                    )
                    # State
                    if isinstance(iconKeyword, tuple) or isinstance(iconKeyword, list):
                        iconKeyword, iconState = iconKeyword
                    else:
                        iconState = None
                    #
                    if iconKeyword is None:
                        lis.append((
                            self.DrawIcon,
                            (iconRect, qtCore._toLxOsIconFile('svg_basic@svg#unused'))
                        ))
                    else:
                        if iconState is not None:
                            iconRect = QtCore.QRect(
                                xPos_ + 1, yPos + 1,
                                iconWidth, iconHeight
                            )
                        #
                        lis.append((
                            self.DrawIcon,
                            (iconRect, qtCore._toLxOsIconFile(iconKeyword))
                        ))
                    if iconState is not None:
                        subIconRect = QtCore.QRect(
                            xPos_ + frameWidth - iconWidth*.75, yPos + frameWidth - iconWidth*.75,
                            iconWidth*.75, iconHeight*.75
                        )
                        lis.append((
                            self.DrawIcon,
                            (subIconRect, qtCore._toLxOsIconFile('state@svg#{}'.format(iconState)))
                        ))
                    #
                    xPos_ += frameHeight + gap
                    # Text
                    textRect = QtCore.QRect(
                        xPos_, yPos, messageWidth, messageHeight
                    )
                    textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter | QtCore.Qt.TextWordWrap
                    italic = [False, True][iconKeyword is None]
                    lis.append((
                        self.DrawText,
                        (textRect, textOption, message, italic)
                    ))
                    #
                    yPos += frameHeight
                # Image
                elif messageType is self.ImageType:
                    # Image
                    fileString_ = uiData
                    image = None
                    if bscMethods.OsFile.isExist(fileString_):
                        image = QtGui.QPixmap(fileString_)
                    #
                    imageRect = QtCore.QRect(
                        xPos, yPos, imageWidth, imageHeight
                    )
                    lis.append((self.DrawImage1, (imageRect, image)))
                    #
                    yPos += imageHeight + gap
                # Image + Text
                elif messageType is self.ImageExplainType:
                    fileString_, explain = uiData
                    # Image
                    if bscMethods.OsFile.isExist(fileString_):
                        image = QtGui.QPixmap(fileString_)
                    else:
                        image = None
                    #
                    if image:
                        imageRect = QtCore.QRect(
                            xPos, yPos, imageWidth, imageHeight
                        )
                        lis.append((self.DrawImage2, (imageRect, image)))
                    # Text
                    if isinstance(explain, tuple) or isinstance(explain, list):
                        explain = ' > '.join(explain)
                    #
                    textRect = QtCore.QRect(
                        xPos + side, yPos, imageWidth, messageHeight
                    )
                    textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
                    italic = [False, True][image is None]
                    lis.append((self.DrawText, (textRect, textOption, explain, italic)))
                    #
                    yPos += imageHeight + gap
                # Images + Texts
                elif messageType is self.ImageExplainType2:
                    self._imageSwitchData = []
                    xOffset = xPos + side
                    rectSize = self.cls_rectSize
                    count = len(uiData)
                    self._imageRect = QtCore.QRect(
                        xPos, yPos, imageWidth, imageHeight
                    )
                    self._topTextRect = QtCore.QRect(
                        xPos + side, yPos, imageWidth, messageHeight
                    )
                    #
                    self._leftTextRect = QtCore.QRect(
                        xPos + 8, yPos + (imageHeight - messageHeight) / 2,
                        imageWidth / 2 - imageHeight / 4, messageHeight
                    )
                    self._rightTextRect = QtCore.QRect(
                        xPos + imageWidth / 2 + imageHeight / 4 - 8, yPos + (imageHeight - messageHeight) / 2,
                        imageWidth / 2 - imageHeight / 4, messageHeight
                    )
                    for seq, i in enumerate(uiData):
                        fileString_, explain = i
                        # Temp File
                        if isinstance(fileString_, tuple) or isinstance(fileString_, list):
                            fileString_, osTempFile = fileString_
                        else:
                            osTempFile = None
                        # Image
                        existBoolean = bscMethods.OsFile.isExist(fileString_)
                        if existBoolean:
                            ext = bscMethods.OsFile.ext(fileString_)
                            isVedio = ext in ['.avi', '.mov']
                            if isVedio:
                                osFileBase = bscMethods.OsFile.base(fileString_)
                                osImageFile = osFileBase + '_0000' + '.jpg'
                            else:
                                osImageFile = fileString_
                            #
                            image = QtGui.QPixmap(osImageFile)
                        else:
                            isVedio = False
                            image = None
                        # Text
                        if isinstance(explain, tuple) or isinstance(explain, list):
                            strExplains = []
                            for j in explain:
                                if isinstance(j, str) or isinstance(j, unicode):
                                    strExplains.append(j)
                                elif isinstance(j, tuple) or isinstance(j, list):
                                    startFrame, endFrame = j
                                    leftExplain = bscMethods.Frame.toTimeString(
                                        frameValue=endFrame - startFrame,
                                        fpsValue=30
                                    )
                                    leftTextOption = QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
                                    self._leftTextDrawData = leftTextOption, leftExplain, False
                                    #
                                    rightExplain = '{} - {}'.format(str(startFrame).zfill(4), str(endFrame).zfill(4))
                                    rightTextOption = QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
                                    self._rightTextDrawData = rightTextOption, rightExplain, False
                            #
                            topExplain = ' > '.join(strExplains)
                        else:
                            topExplain = explain
                        #
                        topTextOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
                        topItalic = [False, True][image is None]
                        # Button
                        rect = QtCore.QRect(
                            xOffset + 2, imageHeight - rectSize + 2,
                            rectSize - 4, rectSize - 4
                        )
                        isSelected = [False, True][seq == self._imageIndex]
                        if isSelected:
                            self._imageDrawData = fileString_, osTempFile, isVedio, image
                            self._topTextDrawData = topTextOption, topExplain, topItalic
                        #
                        backgroundRgba = [(255, 255, 64, 255), (63, 255, 127, 255)][existBoolean]
                        self._imageSwitchData.append((
                            rect,
                            backgroundRgba,
                            isSelected,
                            (fileString_, osTempFile, isVedio, image),
                            (topTextOption, topExplain, topItalic)
                        ))
                        #
                        xOffset += rectSize
                    #
                    self._imageSwitchArea = QtCore.QRect(xPos + side, imageHeight - rectSize, rectSize*count, rectSize)
                    #
                    yPos += imageHeight + gap
        return lis
    #
    def delExtraWidget(self):
        pass
        # children = self.children()
        # if children:
        #     for i in children:
        #         if type(i) == xListItemExtraWidget:
        #             i.deleteLater()
    #
    def setDefaultHeight(self, height):
        self._uiDefaultHeight = height
    #
    def setImageIndex(self, value):
        self._imageIndex = value
    #
    def initUi(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # noinspection PyArgumentEqualDefault
        self.setFont(
            qtCore.qtFont(size=8, weight=50, family=_families[2])
        )
        #
        self._uiDefaultHeight = 200
        #
        self._uiBackgroundRgba = 71, 71, 71, 255
        #
        self._imageOpenBorderRgba = 223, 223, 223, 255
        self._uiTextRgba = 223, 223, 223, 255
        #
        self._uiTextFrameBackgroundRgba = 0, 0, 0, 0
        self._uiTextFrameBorderRgba = 0, 0, 0, 0
        #
        self._unselectedRectBackground = 95, 95, 95, 255
        self._selectedRectBackground = 223, 223, 223, 255
        #
        self._uiImageSwitchCurBackgroundRgba = 63, 127, 255, 255
        #
        self._uiImageSwitchBorderRgba = 95, 95, 95, 255
        self._uiImageSwitchCurBorderRgba = 223, 223, 223, 255
        #
        self._uiBorderRgba = 95, 95, 95, 255
        self._uiNameRgba = 223, 223, 223, 255
        #
        self._uiColorBackgroundRgba = 71, 71, 71, 255
        self._uiColorBorderRgba = 127, 127, 127, 255
        #
        self._uiSide = 2
        self._uiSpacing = 2
        #
        self._uiFrameWidth, self._uiFrameHeight = 20, 20
        #
        self._uiIconWidth, self._uiIconHeight = 16, 16
        #
        self._uiColorWidth, self._uiColorHeight = 12, 12
        #
        self._explainWidth = 96
        self.cls_rectSize = 16
        #
        self._imageSwitchArea = None
        self._imageOpenArea = None
        #
        self._imageSwitchData = None
        #
        self._imageRect = None
        self._imageDrawData = None
        self._topTextRect = None
        self._leftTextRect = None
        self._rightTextRect = None
        #
        self._topTextDrawData = None
        self._leftTextDrawData = None
        self._rightTextDrawData = None
        #
        self._extraEnabled = False
        #
        self._messages = None
        #
        self._imageIndex = 0


#
class QtFilterCheckbutton(qtObjWidget.QtAbcObj_Item):
    MODEL_ITEM_CLS = _qtMdlItem.QtFilterCheckviewItemModel

    itemSize = 20, 20
    def __init__(self, iconKeyword=None, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtFilterCheckbutton, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjItemWidget()
        #
        self.setupUi()
        #
        if iconKeyword:
            self.setIcon(iconKeyword)
        #
        self.setUiSize()
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.itemModel()._pressStartAction(event)
        elif event.button() == QtCore.Qt.RightButton:
            self._toolActionDropAction()
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix
        # Background
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        painter.setBorderRgba(self._uiBorderRgba)
        painter.drawRect(self.itemModel()._uiBasicRect)
        #
        if self.itemModel().isExpandEnable() is True:
            painter.setDrawImage(
                self.itemModel()._uiExpandRect,
                self.itemModel()._uiExpandIcon
            )
        #
        if self.itemModel().isCheckEnable() is True:
            painter.setDrawImage(
                self.itemModel()._uiCheckRect,
                self.itemModel()._uiCheckIcon
            )
        # Filter Color
        if self.itemModel().isColorEnable() is True:
            painter.setBackgroundRgba([(71, 71, 71, 255), self._uiColorBackgroundRgba][self.itemModel().isColorable()])
            painter.setBorderRgba(self._uiColorBorderRgba)
            painter.drawRect(self.itemModel()._uiColorRect)
        # Icon
        if self.itemModel()._uiIcon is not None:
            painter.setDrawImage(
                self.itemModel()._uiIconRect,
                self.itemModel()._uiIcon
            )
        # Name
        if self.itemModel()._uiNameText is not None:
            painter.setBorderRgba(self._uiNameRgba)
            # noinspection PyArgumentEqualDefault
            painter.setFont(
                qtCore.qtFont(size=8, weight=50, italic=self._uiFontItalic, family=_families[0])
            )
            textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            painter.drawText(
                self.itemModel()._uiNameTextRect,
                textOption,
                self.itemModel()._uiNameText
            )
        # Sub Name
        if self.itemModel().uiSubName() is not None:
            painter.setBorderRgba(self._uiSubNameColor)
            #
            textOption = QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
            # noinspection PyArgumentEqualDefault
            painter.setFont(qtCore.qtFont(size=8, weight=50, family=_families[0]))
            painter.drawText(
                self.itemModel()._uiSubNameRect,
                textOption, self.itemModel()._uiSubNameText
            )

        # painter.end()
    # noinspection PyUnusedLocal
    @qtObjWidget.actionviewEventFilterModifier
    def eventFilter(self, *args):
        return False
    @qtObjWidget.actionviewDropModifier
    def _toolActionDropAction(self):
        pass
    #
    def setItemFilterColumn(self, number):
        self.itemModel().setItemFilterColumn(number)
    #
    def setItemFilterRow(self, number):
        self.itemModel().setItemFilterRow(number)
    #
    def setUiSubName(self, string):
        self.itemModel().setUiSubName(string)
    #
    def uiSubName(self):
        return self.itemModel().uiSubName()
    #
    def setCheckedAlone(self):
        self.itemModel().setCheckedAlone()
    #
    def addFilterChild(self, widget):
        self.itemModel().addFilterChild(widget)
    #
    def setFilterViewWidget(self, widget):
        self.itemModel().setFilterViewWidget(widget)
    #
    def setViewFilterItemIndexes(self, indices):
        self.itemModel().setViewFilterItemIndexes(indices)
    #
    def setMaxFilterCount(self, number):
        self.itemModel().setMaxFilterCount(number)
    #
    def viewFilterItemIndexes(self):
        return self.itemModel().viewFilterItemIndexes()
    #
    def filterCount(self):
        return self.itemModel().viewFilterIndexCount()
    #
    def setTooltip(self, string):
        if string:
            self.uiTip = string
    #
    def setEventOverrideEnable(self, boolean):
        self.itemModel().setEventOverrideEnable(boolean)
    #
    def setRefresh(self):
        self.itemModel().setRefresh()
    #
    def setUiSize(self):
        # self.setMaximumSize(*self.itemSize)
        self.setMinimumSize(*self.itemSize)


#
class QtCheckbutton(qtObjWidget.QtAbcObj_Item):
    MODEL_ITEM_CLS = _qtMdlItem.QtCheckbuttonItemModel

    def __init__(self, iconKeyword=None, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtCheckbutton, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjItemWidget()
        #
        self._overrideUi()
        #
        self.setupUi()
        #
        if iconKeyword:
            self.setIcon(iconKeyword)
        else:
            self.setUiSize()
    #
    def _overrideUi(self):
        self._uiNameRgba = 127, 127, 127, 255
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix
        # Check
        if self.itemModel().isCheckEnable() is True:
            painter.setDrawImage(
                self.itemModel().checkRect(),
                self.itemModel()._uiCheckIcon
            )
        # Icon
        if self.itemModel().icon() is not None:
            painter.setDrawImage(
                self.itemModel().iconRect(),
                self.itemModel().icon()
            )
        # Name
        if self.itemModel().nameText() is not None:
            painter.setBorderRgba(self._uiNameRgba)
            # noinspection PyArgumentEqualDefault
            painter.setFont(
                qtCore.qtFont(size=8, weight=50, italic=self._uiFontItalic, family=_families[0])
            )
            #
            textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            painter.drawText(
                self.itemModel()._uiNameTextRect,
                textOption,
                self.itemModel().drawNameText()
            )

        # painter.end()
    #
    def setIcon(self, iconKeyword, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setIcon(iconKeyword, iconWidth, iconHeight, frameWidth, frameHeight)
        #
        self.setUiSize()
    #
    def setUiSize(self):
        w, h = self.itemModel().frameSize()
        self.setMaximumSize(166667, h)
        self.setMinimumSize(0, h)


#
class QtRadioCheckbutton(qtObjWidget.QtAbcObj_Item):
    MODEL_ITEM_CLS = _qtMdlItem.QtCheckbuttonItemModel

    def __init__(self, iconKeyword=None, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtRadioCheckbutton, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjItemWidget()
        #
        self._overrideAttr()
        self._overrideUi()
        #
        self.setupUi()
        #
        self.setAutoExclusive(True)
        #
        if iconKeyword:
            self.setIcon(iconKeyword)
        else:
            self.setUiSize()
    #
    def _overrideAttr(self):
        pass
    #
    def _overrideUi(self):
        self._uiNameRgba = 127, 127, 127, 255
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix
        # Check
        if self.itemModel().isCheckEnable() is True:
            painter.setDrawImage(
                self.itemModel().checkRect(),
                self.itemModel()._uiCheckIcon
            )
        # Icon
        if self.itemModel().icon() is not None:
            painter.setDrawImage(
                self.itemModel().iconRect(),
                self.itemModel().icon()
            )
        # Name
        if self.itemModel().nameText() is not None:
            painter.setBorderRgba(self._uiNameRgba)
            # noinspection PyArgumentEqualDefault
            painter.setFont(
                qtCore.qtFont(size=8, weight=50, italic=self._uiFontItalic, family=_families[0])
            )
            #
            textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            painter.drawText(
                self.itemModel()._uiNameTextRect,
                textOption,
                self.itemModel().drawNameText()
            )

        # painter.end()
    #
    def setIcon(self, iconKeyword, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setIcon(iconKeyword, iconWidth, iconHeight, frameWidth, frameHeight)
        #
        self.setUiSize()
    #
    def setUiSize(self):
        w, h = self.itemModel().frameSize()
        self.setMaximumSize(166667, h)
        self.setMinimumSize(0, h)


#
class QtEnablebutton(qtObjWidget.QtAbcObj_Item):
    MODEL_ITEM_CLS = _qtMdlItem.QtEnablebuttonItemModel

    def __init__(self, iconKeyword=None, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtEnablebutton, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjItemWidget()
        #
        self.setupUi()
        #
        if iconKeyword:
            self.setIcon(iconKeyword)
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix
        # Icon
        if self.itemModel().icon() is not None:
            painter.setDrawImage(
                self.itemModel().iconRect(),
                self.itemModel().icon()
            )
        # Check
        if self.itemModel().isCheckEnable() is True:
            painter.setDrawImage(
                self.itemModel().checkRect(),
                self.itemModel()._uiCheckIcon
            )

        # painter.end()
    #
    def setIcon(self, iconKeyword, iconWidth=16, iconHeight=16, frameWidth=24, frameHeight=24):
        self.itemModel().setIcon(iconKeyword, iconWidth, iconHeight, frameWidth, frameHeight)
        #
        self.setUiSize()
    #
    def setUiSize(self):
        self.setMaximumSize(*self.itemModel().frameSize())
        self.setMinimumSize(*self.itemModel().frameSize())


#
class QtValueEnterlabel(qtObjWidget.QtAbcObj_ValueEnterlabel):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtValueEnterlabel, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjValueEnterlabel()


#
class QtFilterEnterlabel(qtObjWidget.QtAbcObj_FilterEnterlabel):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtFilterEnterlabel, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjFilterEnterlabel()


#
class QtEnterlabel(qtObjWidget.QtAbcObj_Enterlabel):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtEnterlabel, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjEnterlabel()


#
class QtEnterbox(qtObjWidget.QtAbcObj_Enterlabel):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtEnterbox, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjEnterbox()


#
class QtIconbutton(qtObjWidget.QtAbcObj_QtIconbutton):
    def __init__(self, iconKeyword=None, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtIconbutton, self)
            self.clsSuper.__init__(*args, **kwargs)

        self._initAbcObjIconbutton(iconKeyword)


#
class QtMenuIconbutton(qtObjWidget.QtAbcObj_ActionIconbutton):
    def __init__(self, iconKeyword=None, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtMenuIconbutton, self)
            self.clsSuper.__init__(*args, **kwargs)

        self._initAbcObjActionIconbutton(iconKeyword)


#
class QtPressbutton(qtObjWidget.QtAbcObj_Item):
    MODEL_ITEM_CLS = qtObjModel._QtPressbuttonModel

    def __init__(self, iconKeyword=None, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtPressbutton, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjItemWidget()
        #
        self.setupUi()
        #
        self.__override()
        #
        if iconKeyword:
            self.setIcon(iconKeyword)
        #
        self.setUiSize()
    #
    def __override(self):
        self.__overrideUi()
        self.__overrideVar()
    #
    def __overrideUi(self):
        self._uiBackgroundRgba = 79, 79, 79, 255
        self._uiBorderRgba = 127, 127, 127, 255
    #
    def __overrideVar(self):
        self._itemModel._isPressButton = True
    @qtCore.uiTooltipClearMethod
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if self.isPressable():
                self._setQtPressStyle(qtCore.PressedState)
            #
            self.itemModel()._pressStartAction(event)
            #
            event.ignore()
        elif event.button() == QtCore.Qt.RightButton:
            self._toolActionDropAction()
        else:
            event.ignore()
    @qtCore.uiTooltipClearMethod
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if self.isPressable():
                self._setQtPressStyle(qtCore.PressedState)
            #
            self.itemModel()._pressStartAction(event)
            #
            event.ignore()
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            self.itemModel()._hoverExecuteAction(event)
        else:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.itemModel()._pressExecuteAction(event)
                #
                event.ignore()
            else:
                event.ignore()
    @qtCore.uiTooltipClearMethod
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.itemModel()._pressStopAction(event)
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix
        painter.setRenderHint(painter.Antialiasing)
        borderWidth = 1
        borderRadius = 4
        if self.itemModel().isPercentEnable():
            if self.itemModel().isPressable():
                painter.setDrawButtonBasic(
                    self.itemModel().basicRect(),
                    borderWidth, borderRadius,
                    self._uiBorderRgba, self._uiBorderRgba, self._uiBorderStyle
                )
                # Basic
                painter.setDrawButtonBasic(
                    self.itemModel().percentFrameRect(),
                    borderWidth, borderRadius,
                    self._uiBackgroundRgba, self._uiBorderRgba, 'solid'
                )
                # Percent
                painter.setBorderRgba((0, 0, 0, 0))
                painter.setBackgroundRgba(self._uiPercentValueRgba)
                painter.drawRoundedRect(
                    self.itemModel()._uiPercentValueRect,
                    borderRadius - 1, borderRadius - 1, QtCore.Qt.AbsoluteSize
                )
            else:
                painter.setDrawButtonBasic(
                    self.itemModel().basicRect(),
                    borderWidth, borderRadius,
                    self._uiBackgroundRgba, self._uiBorderRgba, self._uiBorderStyle
                )
        else:
            painter.setDrawButtonBasic(
                self.itemModel().basicRect(),
                borderWidth, borderRadius,
                self._uiBackgroundRgba, self._uiBorderRgba, self._uiBorderStyle
            )
        # Icon
        if self.itemModel().icon() is not None:
            painter.setDrawImage(
                self.itemModel().iconRect(),
                self.itemModel().icon()
            )
            if self.itemModel().subIcon() is not None:
                painter.setDrawImage(
                    self.itemModel().subIconRect(),
                    self.itemModel().subIcon()
                )
        if self.itemModel().extendIcon() is not None:
            painter.setDrawImage(
                self.itemModel().extendIconRect(),
                self.itemModel().extendIcon()
            )
        # Name
        if self.itemModel().nameText() is not None:
            painter.setBorderRgba(self._uiNameRgba)
            # noinspection PyArgumentEqualDefault
            painter.setFont(qtCore.qtFont(size=8, weight=50, italic=self._uiFontItalic, family=_families[0]))
            rect = self.itemModel().nameTextRect()
            textOption = self.itemModel()._uiTextAlignment
            string = self.itemModel().drawNameText()
            painter.drawText(
                rect,
                textOption,
                string
            )
            if self.itemModel().isPercentEnable():
                textOption = QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
                painter.drawText(
                    self.itemModel().percentTextRect(),
                    textOption,
                    self.itemModel().percentText()
                )

        # painter.end()
    # noinspection PyUnusedLocal
    @qtObjWidget.actionviewEventFilterModifier
    def eventFilter(self, *args):
        return False
    @qtObjWidget.actionviewDropModifier
    def _toolActionDropAction(self):
        pass
    #
    def setActionData(self, actionData):
        self.actionData = actionData
    #
    def setIcon(self, iconKeyword, iconWidth=16, iconHeight=16, frameWidth=24, frameHeight=24):
        self.itemModel().setIcon(iconKeyword, iconWidth, iconHeight, frameWidth, frameHeight)
        self.setUiSize()
    #
    def setTextAlignment(self, args):
        self.itemModel().setTextAlignment(args)
    #
    def setNameText(self, string):
        self.itemModel().setNameText(string)
        self._tempUiName = self.nameText()
    #
    def setTooltip(self, string):
        if string:
            self.uiTip = string
    #
    def setUiHeight(self, height):
        self.itemModel().setFrameSize(height, height)
        self.setUiSize()
    #
    def setUiSize(self):
        w, h = self.itemModel().frameSize()
        self.setMaximumSize(166667, h)
        self.setMinimumSize(0, h)
    #
    def setPercentEnable(self, boolean):
        self.itemModel().setPercentEnable(boolean)
        self.setIcon('svg_basic@svg#info')
    #
    def setPercent(self, maxValue, value):
        self.itemModel().setPercent(maxValue, value)
    #
    def setPercentRest(self):
        self.itemModel().setPercentRest()


#
class QtTreeviewItem(qtObjWidget.QtAbcObj_Treeitem):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtTreeviewItem, self)
            self.clsSuper.__init__(*args, **kwargs)

        self._initAbcObjTreeitem()


#
class QtGridviewItem(qtObjWidget.QtAbcObj_Item):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtGridviewItem, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjItemWidget()
        #
        self.setupUi()
        self.__overrideUi()
    #
    def __overrideUi(self):
        self._uiMenuBackgroundRgba = 0, 0, 0, 0
        self._uiMenuBorderRgba = 0, 0, 0, 0
        #
        self._uiCentralBackgroundRgba = 71, 71, 71, 255
        self._uiCentralBorderRgba = 95, 95, 95, 255
    @qtCore.uiTooltipClearMethod
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if self.itemModel()._isPressable:
                self.clicked.emit()
            #
            event.ignore()
        elif event.button() == QtCore.Qt.RightButton:
            if self.actionData:
                self._menuDropAction()
            #
            event.accept()
        else:
            event.ignore()
    @qtCore.uiTooltipClearMethod
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if self.itemModel()._isPressable:
                self.clicked.emit()
            #
            event.ignore()
        else:
            event.ignore()
    @qtCore.uiTooltipClearMethod
    def mouseReleaseEvent(self, event):
        event.ignore()
    #
    def mouseMoveEvent(self, event):
        event.ignore()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix
        # noinspection PyArgumentEqualDefault
        painter.setFont(qtCore.qtFont(size=8, weight=50, italic=False, family=_families[0]))
        # Shadow
        if self.itemModel()._itemMode is qtCore.IconMode:
            painter.setBorderRgba((0, 0, 0, 64))
            painter.setBackgroundRgba((0, 0, 0, 64))
            painter.drawRect(
                self.itemModel()._shadowRect
            )
            painter.setBackgroundRgba(self._uiCentralBackgroundRgba)
            painter.setBorderRgba(self._uiCentralBorderRgba)
            painter.drawRect(self.itemModel()._uiCentralRect)
        # Title & central
        painter.setBackgroundRgba(0, 0, 0, 0)
        painter.setBorderRgba(0, 0, 0, 0)
        painter.drawRect(self.itemModel()._titleRect)
        #
        startPos, endPos = self.itemModel()._uiBasicRect.topLeft(), self.itemModel()._uiBasicRect.bottomRight()
        painter.setDrawRimFrame(
            self.itemModel()._titleRect, self.itemModel()._uiCentralRect,
            startPos, endPos,
            self.itemModel()._isPressCurrent, self.itemModel()._isChecked, self.itemModel()._isPressHovered
        )
        # Check Box
        if self.itemModel().isCheckEnable():
            if self.itemModel()._uiCheckIcon is not None:
                painter.setDrawImage(
                    self.itemModel()._uiCheckRect,
                    self.itemModel()._uiCheckIcon
                )
        # Filter Color
        if self.itemModel().isColorEnable():
            painter.setBackgroundRgba(self._uiColorBackgroundRgba)
            painter.setBorderRgba(self._uiColorBorderRgba)
            painter.drawRect(self.itemModel().colorRect())
        # Icon
        if self.itemModel()._uiIcon is not None:
            painter.setDrawImage(
                self.itemModel()._uiIconRect,
                self.itemModel()._uiIcon
            )
        # Name
        if self.itemModel()._uiNameText is not None:
            rect = self.itemModel().nameTextRect()
            textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            string = self.itemModel().drawNameText()
            if self.itemModel()._filterKeyword is not None:
                painter.setDrawFilterString(
                    rect,
                    False,
                    string, self.itemModel()._filterKeyword,
                    self._uiNameRgba
                )
            else:
                painter.setBorderRgba(self._uiNameRgba)
                painter.drawText(
                    rect,
                    textOption,
                    string
                )
        # Index
        if self.itemModel()._uiIndexText is not None:
            painter.setBorderRgba(self._uiIndexRgba)
            painter.drawText(
                self.itemModel()._uiIndexTextRect,
                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter,
                str(self.itemModel()._uiIndexText)
            )
        #
        if self.itemModel()._uiImage is not None:
            image = QtGui.QPixmap(self.itemModel()._uiImage)
            painter.drawPixmap(self.itemModel()._imageRect, image)

        # painter.end()
    # noinspection PyUnusedLocal
    @qtObjWidget.actionviewEventFilterModifier
    def eventFilter(self, *args):
        return False
    @qtObjWidget.actionviewDropModifier
    def _menuDropAction(self):
        pass
    #
    def setActionData(self, actions, title=None):
        self.actionData = actions
        if title:
            self.actionTitle = title
    #
    def addWidget(self, widget, x, y, w, h):
        self._layout.addWidget(widget, x, y, w, h)
    #
    def setId(self, string):
        self.itemModel().setId(string)
    #
    def setImage(self, image):
        self.itemModel().setImage(image)
    #
    def setCheckHovered(self, boolean):
        self.itemModel().setCheckHovered(boolean)
    #
    def setSelectable(self, boolean):
        self.itemModel().setSelectable(boolean)
    #
    def setSelected(self, boolean):
        self.itemModel().setSelected(boolean)
    #
    def setFilterStatus(self, status):
        self.itemModel().setFilterStatus(status)
    #
    def isPressCurrent(self):
        return self.itemModel().isPressCurrent()
    #
    def id(self):
        return self.itemModel().id()
    #
    def setupUi(self):
        self._itemModel = _qtMdlItem.QtGridviewItemModel(self)
        #
        self._layout = qtCore.QGridLayout_(self)
        self._layout.setContentsMargins(
            0, self.itemModel()._uiFrameHeight,
            self.itemModel()._uiShadowRadius, self.itemModel()._uiShadowRadius
        )
        self._layout.setSpacing(0)


#
class QtPresetviewItem(qtObjWidget.QtAbcObj_Item):
    indexChanged = qtCore.qtSignal()
    setChanged = qtCore.qtSignal()
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtPresetviewItem, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjItemWidget()
        #
        self.setupUi()
        #
        self.__overrideAttr()
        self._initAttr()
    #
    def __overrideAttr(self):
        self._uiIndexRgba = 191, 191, 191, 255
        self._uiNameRgba = 95, 95, 95, 255
        # noinspection PyArgumentEqualDefault
        self.setFont(
            qtCore.qtFont(size=8, weight=50, family=_families[2])
        )
        #
        self._uiFontItalic = True
    #
    def _initAttr(self):
        self._messageWidth = 240
        self._describeWidth = 240
        #
        self._childItemDic = {}
        #
        self._defaultPresetSetDatum = None
    # noinspection PyArgumentList
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if self.itemModel()._isPressable:
                self.clicked.emit()
            #
            event.ignore()
        elif event.button() == QtCore.Qt.RightButton:
            if self.actionData:
                self._menuDropAction()
            #
            event.accept()
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        if self.itemModel().itemLevel() == 0:
            painter = qtCore.QPainter_(self)
            # painter.begin(self)  # fix
            # Background
            painter.setBackgroundRgba(self._uiBackgroundRgba)
            painter.setBorderRgba(self._uiBorderRgba)
            painter.drawRect(self.itemModel().basicRect())
            # Check
            if self.itemModel().isCheckEnable():
                painter.setDrawImage(self.itemModel()._uiCheckRect, self.itemModel()._uiCheckIcon)
            # Filter Color
            if self.itemModel().isColorEnable():
                painter.setBackgroundRgba(self._uiColorBackgroundRgba)
                painter.setBorderRgba(self._uiColorBorderRgba)
                painter.drawRect(self.itemModel()._uiColorRect)
            # Expand
            if self.itemModel().isExpandable() is True:
                painter.setDrawImage(self.itemModel()._uiExpandRect, self.itemModel()._uiExpandIcon)
            # Index
            if self.itemModel().indexText() is not None:
                painter.setBorderRgba(self._uiIndexRgba)
                painter.drawText(
                    self.itemModel().indexTextRect(),
                    QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter,
                    str(self.itemModel().indexText())
                )
            # Icon
            if self.itemModel().icon() is not None:
                painter.setDrawImage(self.itemModel()._uiIconRect, self.itemModel()._uiIcon)
            # Name
            if self.itemModel().nameText() is not None:
                font = painter.font()
                font.setItalic(self._uiFontItalic)
                painter.setFont(font)
                rect = self.itemModel()._uiNameTextRect
                textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
                #
                string = self.itemModel().drawNameText()
                if self.itemModel()._filterKeyword is not None:
                    painter.setDrawFilterString(
                        rect,
                        False,
                        string, self.itemModel()._filterKeyword,
                        self._uiNameRgba
                    )
                else:
                    painter.setBorderRgba(self._uiNameRgba)
                    painter.drawText(
                        rect,
                        textOption,
                        string
                    )

            # painter.end()
    # noinspection PyUnusedLocal
    @qtObjWidget.actionviewEventFilterModifier
    def eventFilter(self, *args):
        return False
    @qtObjWidget.actionviewDropModifier
    def _menuDropAction(self):
        pass
    #
    def setChangedEmit(self):
        self.setChanged.emit()
    #
    def setEnterEnable(self, boolean):
        self._descriptionLabel.setEnterEnable(boolean)
    #
    def setActionData(self, actions, title=None):
        self.actionData = actions
        if title:
            self.actionTitle = title
    #
    def setPresetIndex(self, uniqueId):
        self.setName(uniqueId)
    #
    def presetIndex(self):
        return self.name()
    #
    def setPresetNumber(self, value):
        self.setIndexText(value)
    #
    def presetNumber(self):
        return self.indexText()
    #
    def setEnable(self, boolean):
        self.itemModel().setChecked(boolean)
    #
    def isEnable(self):
        return self.itemModel().isChecked()
    #
    def setDescription(self, string):
        self._descriptionLabel.setDatum(string)
        self._descriptionLabel.setDefaultDatum(string)
    #
    def description(self):
        return self._descriptionLabel.datum()
    #
    def setDefaultPresetSetDatum(self, dic):
        self._defaultPresetSetDatum = dic
    #
    def defaultPresetSetDatum(self):
        return self._defaultPresetSetDatum
    #
    def isPresetSetDatumChanged(self):
        return self.presetSetDatum() != self._defaultPresetSetDatum
    #
    def setupPresetIndex(self, indexLis, useNiceName=False):
        if indexLis:
            index, enable, description = indexLis
            self.setPresetIndex(index), self.setEnable(enable), self.setDescription(description)
            if useNiceName:
                self.setNameText(self.str_camelcase2prettify(index))
    #
    def presetIndexDatum(self):
        key = self.name()
        enable = self.isChecked()
        description = self._descriptionLabel.datum()
        return [key, enable, description]
    #
    def setupPresetSet(self, setData):
        if setData:
            for i in setData:
                if i:
                    key, uiKey, value, defValue, uiValue = i
                    #
                    datumItem = QtEnterlabel()
                    datumItem.setName(key)
                    datumItem.setNameText(uiKey)
                    datumItem.setNameTextWidth(240)
                    datumItem.datumChanged.connect(self.setChangedEmit)
                    #
                    self._childItemDic[key] = datumItem
                    #
                    if isinstance(uiValue, bool):
                        datumItem.setCheckEnable(True)
                        datumItem.setDefaultDatum(defValue)
                        datumItem.setChecked(value)
                    elif isinstance(uiValue, int) or isinstance(uiValue, float):
                        datumItem.setEnterEnable(True)
                        datumItem.setDefaultDatum(defValue)
                        datumItem.setDatum(value)
                    elif isinstance(uiValue, str) or isinstance(uiValue, unicode):
                        datumItem.setEnterEnable(True)
                        datumItem.setDefaultDatum(defValue)
                        datumItem.setDatum(value)
                    # Use as List
                    elif isinstance(uiValue, tuple):
                        datumItem.setEnterEnable(True)
                        datumItem.setDefaultDatum(list(defValue))
                        datumItem.setDatum(value)
                    elif isinstance(uiValue, list):
                        datumItem.setChooseEnable(True)
                        datumItem.setDefaultDatum(defValue)
                        datumItem.setDatumLis(uiValue)
                        datumItem.setChoose(value)
                    elif isinstance(uiValue, dict):
                        datumItem.setChooseEnable(True)
                        datumItem.setDefaultDatum(defValue)
                        datumItem.setExtendDatumDic(uiValue)
                        datumItem.setChoose(value)
                    #
                    self.addChild(datumItem)
    #
    def refreshPresetSet(self, setDic):
        if setDic:
            for key, value in setDic.items():
                if key in self._childItemDic:
                    datumItem = self._childItemDic[key]
                    datum = datumItem.datum()
                    if not datum == value:
                        if datumItem.isCheckEnable():
                            datumItem.setChecked(value)
                        elif datumItem.isChooseEnable():
                            datumItem.setChoose(value)
                        elif datumItem.isEnterEnable():
                            datumItem.setDatum(value)
    #
    def presetSetDatum(self):
        dic = {}
        if self.childItems():
            for i in self.childItems():
                value = i.datum()
                key = i.name()
                dic[key] = value
        return dic
    #
    def setupUi(self):
        self._itemModel = _qtMdlItem.QtPresetviewItemModel(self)
        #
        self._descriptionLabel = QtEnterlabel()
        self._descriptionLabel.setParent(self)
        self._descriptionLabel.setEnterEnable(True)

        if qtCore.LOAD_INDEX is 0:
            self._descriptionLabel.setAttribute(QtCore.Qt.WA_TranslucentBackground | QtCore.Qt.WA_TransparentForMouseEvents)
        else:
            self._descriptionLabel.setAttribute(QtCore.Qt.WA_TranslucentBackground)


#
class QtRecordviewItemItem(qtObjWidget.QtAbcObj_Item):
    MODEL_ITEM_CLS = _qtMdlItem.QtRecordviewItemItemModel
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtRecordviewItemItem, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjItemWidget()
        #
        self.setupUi()

    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix
        # Background
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        painter.setBorderRgba(self._uiBorderRgba)
        painter.drawRect(self.itemModel().basicRect())
        # Check
        if self.itemModel().isCheckEnable():
            painter.setDrawImage(self.itemModel()._uiCheckRect, self.itemModel()._uiCheckIcon)
        # Filter Color
        if self.itemModel().isColorEnable():
            painter.setBackgroundRgba(self._uiColorBackgroundRgba)
            painter.setBorderRgba(self._uiColorBorderRgba)
            painter.drawRect(self.itemModel()._uiColorRect)
        # Expand
        if self.itemModel().isExpandable() is True:
            painter.setDrawImage(self.itemModel()._uiExpandRect, self.itemModel()._uiExpandIcon)
        # Index
        if self.itemModel().indexText() is not None:
            painter.setBorderRgba(self._uiIndexRgba)
            painter.drawText(
                self.itemModel().indexTextRect(),
                QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter,
                str(self.itemModel().indexText())
            )
        # Icon
        if self.itemModel().icon() is not None:
            painter.setDrawImage(
                self.itemModel().iconRect(),
                self.itemModel().icon()
            )
        elif self.itemModel().iconText() is not None:
            painter.setDrawIconText(
                self.itemModel().iconRect(),
                self.itemModel().iconText(),
                self._uiBackgroundRgba, self._uiNameRgba
            )
        # Name
        if self.itemModel().nameText() is not None:
            font = painter.font()
            font.setItalic(self._uiFontItalic)
            painter.setFont(font)
            rect = self.itemModel()._uiNameTextRect
            textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            #
            string = self.itemModel().drawNameText()
            if self.itemModel()._filterKeyword is not None:
                painter.setDrawFilterString(
                    rect,
                    False,
                    string, self.itemModel()._filterKeyword,
                    self._uiNameRgba
                )
            else:
                painter.setBorderRgba(self._uiNameRgba)
                painter.drawText(
                    rect,
                    textOption,
                    string
                )

        # painter.end()


#
class QtTextbrower(qtObjWidget.QtAbcObj_Textbrower):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtTextbrower, self)
            self.clsSuper.__init__(*args, **kwargs)

        self._initAbcObjTextbrower()
