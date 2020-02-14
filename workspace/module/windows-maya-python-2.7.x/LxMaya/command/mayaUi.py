# coding=utf-8
from LxBasic import bscMethods

from LxScheme import shmOutput
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# Shelf
mainShelfLayoutName = 'MainShelfLayout'
subShelfFormName = 'mainShelfForm'
mainShelfTabLayoutName = 'mainShelfTabLayout'
# Status
mainStatusLineLayoutName = 'MainStatusLineLayout'
statusLineLayoutName = 'statusLineLayout'
#
_uiBackgroundRgba = (.267, .267, .267)
shelfWidth = 480
statusWidth = 480
#
_iconRoot = shmOutput.Directory().icon.server
#
none = ''


#
def mayaOptionVar(name, dv=None, v=None):
    vm = {str: '', int: 0, float: 0.0, list: []}
    dvt = type(dv)
    vt = type(v)
    if cmds.optionVar(exists=name):
        value = cmds.optionVar(q=name)
        if v is not None:
            if vt not in vm:
                return None
            value = v
            if vt == list and vt != []:
                vtt = type(v[0])
                for i in v:
                    if type(i) != vtt and not ((type(i) in [str, unicode]) and (vtt in [str, unicode])):
                        print v, 'is not a list with same type element.'
                if vtt == int:
                    cmds.optionVar(iv=(name, v[0]))
                    for i in range(1, len(v)):
                        cmds.optionVar(iva=(name, v[i]))
                    cmds.optionVar(iva=(name, 0))
                    value.append(0)
                if vtt == float:
                    cmds.optionVar(fv=(name, v[0]))
                    for i in range(1, len(v)):
                        cmds.optionVar(fva=(name, v[i]))
                    cmds.optionVar(fva=(name, 0.0))
                    value.append(0.0)
                if vtt in [str, unicode]:
                    cmds.optionVar(sv=(name, v[0]))
                    for i in range(1, len(v)):
                        cmds.optionVar(sva=(name, v[i]))
                    cmds.optionVar(sva=(name, ''))
                    value.append('')
            if vt == int:
                cmds.optionVar(iv=(name, v))
            if vt == float:
                cmds.optionVar(fv=(name, v))
            if vt in [str, unicode]:
                cmds.optionVar(sv=(name, v))
        if type(value) in [list, tuple]:
            return value[0:-1]
        return value
    elif (dv is not None and dvt in vm) or (v is not None and vt in vm):
        if v is not None and vt in vm:
            dv = v
            dvt = vt
        if dvt == list and dvt != []:
            vtt = type(dv[0])
            for i in dv:
                if type(i) != vtt:
                    print i, type(i)
                    print dv, 'is not a list with same type element.'
            if vtt == int:
                cmds.optionVar(iv=(name, dv[0]))
                for i in range(1, len(dv)):
                    cmds.optionVar(iva=(name, dv[i]))
                cmds.optionVar(iva=(name, 0))
            if vtt == float:
                cmds.optionVar(fv=(name, dv[0]))
                for i in range(1, len(dv)):
                    cmds.optionVar(fva=(name, dv[i]))
                cmds.optionVar(fva=(name, 0.0))
            if vtt in [str, unicode]:
                cmds.optionVar(sv=(name, dv[0]))
                for i in range(1, len(dv)):
                    cmds.optionVar(sva=(name, dv[i]))
                cmds.optionVar(sva=(name, ''))
        if dvt == int:
            cmds.optionVar(iv=(name, dv))
        if dvt == float:
            cmds.optionVar(fv=(name, dv))
        if dvt in [str, unicode]:
            cmds.optionVar(sv=(name, dv))
        return dv
    else:
        return None


#
def mayaFormLayout(nameText, parent, width=none, height=none):
    if cmds.formLayout(nameText, query=1, exists=1):
        cmds.deleteUI(nameText)
    formLayout = cmds.formLayout(
        nameText, parent=parent, noBackground=1)
    if width:
        cmds.formLayout(
            formLayout, edit=1, width=width
        )
    if height:
        cmds.formLayout(
            formLayout, edit=1, height=height
        )
    return formLayout


#
def mayaRowColumnLayout(nameText, parent, numberOfColumns):
    if cmds.rowColumnLayout(nameText, query=1, exists=1):
        cmds.deleteUI(nameText)
    rowColumnLayout = cmds.rowColumnLayout(
        nameText,
        parent=parent,
        numberOfColumns=numberOfColumns,
        noBackground=1
    )
    return rowColumnLayout


#
def setMayaFormLayout(nameText, child, left, right, opposite=0):
    cmds.formLayout(
        nameText,
        edit=1,
        attachForm=[
            (child, 'top', 0), (child, 'bottom', 0),
            (child, 'left', left), (child, 'right', right)
        ]
    )
    parent = getMayaFormLayout(nameText)
    if opposite:
        cmds.formLayout(
            nameText,
            edit=1,
            attachOppositeForm=[
                (parent, 'left', -getMayaFormWidth(nameText)),
                (parent, 'right', -left)
            ]
        )


# Button
def mayaButton(nameText, parent, label, command, width, height):
    button = cmds.button(
        nameText,
        parent=parent,
        label=label,
        command=command,
        actOnPress=1,
        width=width,
        height=height,
        noBackground=1
    )
    return button


# Icon Button
def mayaIconTextButton(style, label, image, highlightImage, annotation, width, height, command):
    iconTextButton = cmds.shelfButton(
        style=style,
        label=label,
        image=image,
        highlightImage=highlightImage,
        width=width,
        height=height,
        flat=1,
        command=command,
        annotation=annotation,
        noBackground=1
    )
    return iconTextButton


# Shelf Button
def mayaShelfButton(style, label, image, highlightImage, annotation, width, height, command):
    shelfButton = cmds.iconTextButton(
        enable=1,
        manage=1,
        font="plainLabelFont",
        commandRepeatable=1,
        style=style,
        label=label,
        image=image,
        highlightImage=highlightImage,
        annotation=annotation,
        width=width,
        height=height,
        flat=1,
        command=command,
        overlayLabelBackColor=(0, 0, 0, 0)
    )
    return shelfButton


#
def mayaOptionMenu(label, changeCommand, width, height):
    optionMenu = cmds.optionMenu(
        label=label,
        changeCommand=changeCommand,
        width=width,
        height=height
    )
    return optionMenu


#
def mayaShelfTabLayout(nameText, parent):
    if cmds.shelfTabLayout(nameText, query=1, exists=1):
        cmds.deleteUI(nameText)
    shelfTabLayout = cmds.shelfTabLayout(
        nameText,
        parent=parent,
        childResizable=1,
        noBackground=1
    )
    return shelfTabLayout


#
def mayaShelfLayout(nameText, parent, annotation, backgroundRgba):
    if cmds.shelfLayout(nameText, query=1, exists=1):
        cmds.deleteUI(nameText)
    shelfLayout = cmds.shelfLayout(
        nameText,
        parent=parent,
        annotation=annotation,
        backgroundColor=backgroundRgba
    )
    return shelfLayout


#
def getMayaFormLayout(nameText):
    formLayout = cmds.formLayout(nameText, query=1, childArray=1)[0]
    return formLayout


#
def getMayaFormWidth(nameText):
    width = cmds.formLayout(nameText, query=1, width=1)
    return width


#
def getMayaFormHeight(nameText):
    height = cmds.formLayout(nameText, query=1, height=1)
    return height


#
def getMayaShelfHeight(nameText):
    height = cmds.shelfLayout(nameText, query=1, height=1)
    return height


#
def setMayaShelfLayout(shelfLayout, spacing):
    cmds.shelfLayout(shelfLayout, edit=1, height=spacing)


#
def setMayaTabLayout(shelfTabLayout, tabLabel, image, annotation):
    cmds.tabLayout(shelfTabLayout, edit=1, tabLabel=tabLabel, image=image, annotation=annotation)


# Set Shelf
def setupMayaShelf(data):
    if data:
        # Main Shelf Layout
        mainShelfWidth = getMayaFormWidth(mainShelfLayoutName)
        # Main Shelf Form
        subShelfLayout = mayaFormLayout(subShelfFormName, mainShelfLayoutName)
        setMayaFormLayout(mainShelfLayoutName, subShelfLayout, mainShelfWidth - shelfWidth, 0, opposite=1)
        # Main Shelf Tab Layout
        mainShelfTabLayout = mayaShelfTabLayout(mainShelfTabLayoutName, subShelfFormName)
        setMayaFormLayout(subShelfFormName, mainShelfTabLayout, 0, 0)
        #
        count = 18
        shelfDic = {}
        # Shelf
        for k, v in data.items():
            if k.endswith('Shelf'):
                shelfName = v['shelfName']
                shelfTip = v['shelfTip']
                shelfBackgroundRgba = bscMethods.Color.mapToFloat(68, 68, 68)
                #
                spacer = (count - len(shelfName)) * ' '
                shelfShowName = spacer + shelfName + spacer
                subShelfTabLayout = mayaShelfLayout(shelfShowName, mainShelfTabLayout, shelfTip, shelfBackgroundRgba)
                shelfDic[k] = subShelfTabLayout
        # Shelf Tool
        for k, v in data.items():
            if k.endswith('Tool'):
                shelfKey = v['shelf']
                if shelfKey in shelfDic:
                    buttonStyle = 'iconOnly'
                    buttonName = v['toolName']
                    buttonIcon = _iconRoot + v['toolIcon']
                    buttonIconHover = _iconRoot + v['toolIconHover']
                    buttonTip = v['toolTip']
                    buttonWidth = 35
                    buttonHeight = 35
                    buttonCommand = v['toolCommand']
                    #
                    helpButtonStyle = 'iconOnly'
                    helpButtonName = v['helpName']
                    helpButtonIcon = _iconRoot + v['helpIcon']
                    helpButtonIconHover = _iconRoot + v['helpIconHover']
                    helpButtonTip = v['helpTip']
                    helpButtonWidth = 15
                    helpButtonHeight = 15
                    helpButtonCommand = v['helpCommand']
                    #
                    shelf = shelfDic[shelfKey]
                    mayaFormLayout(buttonName, shelf, buttonWidth, buttonHeight)
                    #
                    mayaShelfButton(buttonStyle, buttonName, buttonIcon, buttonIconHover, buttonTip, buttonWidth, buttonHeight, buttonCommand)
                    #
                    mayaIconTextButton(helpButtonStyle, helpButtonName, helpButtonIcon, helpButtonIconHover, helpButtonTip, helpButtonWidth, helpButtonHeight, helpButtonCommand)


# Set Status
def setupMayaStatus(data):
    if data:
        statusLineLayout = mayaRowColumnLayout(statusLineLayoutName, mainStatusLineLayoutName, 3)
        mainStatusWidth = getMayaFormWidth(mainStatusLineLayoutName)
        setMayaFormLayout(mainStatusLineLayoutName, statusLineLayout, mainStatusWidth - statusWidth, 240)
        for statusKey, statusData in data.items():
            enabled = statusData['enable']
            if enabled is True:
                mayaShelfButton(
                    statusData['style'],
                    statusData['label'],
                    statusData['image'],
                    statusData['highlightImage'],
                    statusData['annotation'],
                    statusData['width'], statusData['height'],
                    statusData['command']
                )
