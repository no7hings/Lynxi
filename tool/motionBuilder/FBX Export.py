# Copyright 2009 Autodesk, Inc.  All rights reserved.
# Use of this software is subject to the terms of the Autodesk license agreement
# provided at the time of installation or download, or which otherwise accompanies
# this software in either electronic or hard copy form.
#
# Script description:
# FBX 2010/2011 Exporter
#
# Topic: FBApplication, FBFbxOptions, FBLabel, ShowTool, ToolL
#

from pyfbsdk import FBApplication, FBFbxOptions, FBLabel, ShowTool, FBAddRegionParam, FBAttachType, FBImageContainer, \
    FBList, FBFileFormatAndVersion, FBButton, FBButtonStyle, FBTextJustify, FBGetMultiLangText
from pyfbsdk_additions import FBToolList, FBDestroyToolByName, FBCreateUniqueTool, FBHBoxLayout


def tr(pKey):
    return FBGetMultiLangText("FBFbxExport", pKey, True)


# Global variables
gFbxVersionMenuList = ["FBX 2013", "FBX 2014/2015"]
gFbxVersionList = [FBFileFormatAndVersion.kFBFBX2013,
                   FBFileFormatAndVersion.kFBFBX2014_2015]
gFbxCommentList = ["Compatible with Autodesk 2013 applications, and MotionBuilder 2013",
                   "Compatible with Autodesk 2014/2015 applications, and MotionBuilder 2014/2015"]

gFbxVersionMenu = gFbxVersionMenuList[0]
gFileVersion = gFbxVersionList[0]
gFbxComment = gFbxCommentList[0]

gToolName = "FBX Export"
gSaveSelected = False
gFormatCommentLabel = FBLabel()
gFormatCommentLabel.WordWrap = True


#
# Function: callback on export selection checkbox
#
def ExportSelectedCallback(control, event):
    global gSaveSelected
    if control.State:
        gSaveSelected = True
        print "Export Selection only have been checked, exporting only selected object(s)"
    else:
        gSaveSelected = False
        print "Uncheck Selection only, exporting whole scene"


#
# Function: callback on file version change
#
def FileVersionChangeCallback(control, event):
    global gFbxVersionMenu
    global gFileVersion
    global gFbxComment

    lSelected = control.Items[control.ItemIndex]
    print lSelected, "has been selected!"

    for i in range(len(gFbxVersionMenuList)):
        if (gFbxVersionMenuList[i] == lSelected):
            gFbxVersionMenu = gFbxVersionMenuList[i]
            gFileVersion = gFbxVersionList[i]
            gFbxComment = gFbxCommentList[i]
            gFormatCommentLabel.Caption = tr(gFbxComment)
            print tr(gFbxComment)


def SaveButtonCallback(control, event):
    lApp = FBApplication()
    lFbxOptions = FBFbxOptions(False)

    # Initialize our variables
    lFbxOptions.SaveSelectedModelsOnly = gSaveSelected
    lFbxOptions.FileFormatAndVersion = gFileVersion
    lFbxOptions.ShowOptionsDialog = True
    lApp.FileSave("", lFbxOptions)

    del (lFbxOptions)
    del (lApp)


def BuildUI(mainLyt):
    #
    # Image
    #
    x = FBAddRegionParam(10, FBAttachType.kFBAttachLeft, "")
    y = FBAddRegionParam(10, FBAttachType.kFBAttachNone, "")
    w = FBAddRegionParam(50, FBAttachType.kFBAttachNone, "")
    h = FBAddRegionParam(50, FBAttachType.kFBAttachNone, "")
    mainLyt.AddRegion("image", "image", x, y, w, h)
    img = FBImageContainer()
    img.Filename = "browsing/template_fbx-l.png"
    mainLyt.SetControl("image", img)

    # Layout for the labels
    x = FBAddRegionParam(57, FBAttachType.kFBAttachLeft, "image")
    y = FBAddRegionParam(10, FBAttachType.kFBAttachNone, "")
    w = FBAddRegionParam(0, FBAttachType.kFBAttachRight, "")
    h = FBAddRegionParam(25, FBAttachType.kFBAttachNone, "")
    mainLyt.AddRegion("label", "label", x, y, w, h)
    lytLabel = FBHBoxLayout()
    mainLyt.SetControl("label", lytLabel)

    lFormatLabel = FBLabel()
    lFormatLabel.Caption = "FBX Version:"
    lytLabel.Add(lFormatLabel, 90)

    #
    # Layout for the controls
    #
    x = FBAddRegionParam(55, FBAttachType.kFBAttachLeft, "image")
    y = FBAddRegionParam(35, FBAttachType.kFBAttachNone, "")
    w = FBAddRegionParam(0, FBAttachType.kFBAttachRight, "")
    h = FBAddRegionParam(25, FBAttachType.kFBAttachNone, "")
    mainLyt.AddRegion("main", "main", x, y, w, h)
    lyt = FBHBoxLayout()
    mainLyt.SetControl("main", lyt)

    #
    # Add the format list
    #
    lFileFormat = FBList()
    for i in range(len(gFbxVersionMenuList)):
        lFileFormat.Items.append(gFbxVersionMenuList[i])
    lyt.Add(lFileFormat, 75)
    lFileFormat.OnChange.Add(FileVersionChangeCallback)

    #
    # Add the Export Selection control
    #
    lExportSelected = FBButton()
    lExportSelected.Caption = "Export Selection"
    lExportSelected.Style = FBButtonStyle.kFBCheckbox
    lExportSelected.Justify = FBTextJustify.kFBTextJustifyLeft
    lExportSelected.State = gSaveSelected
    lyt.Add(lExportSelected, 110)
    lExportSelected.OnClick.Add(ExportSelectedCallback)

    #
    # Add our Export button
    #
    x = FBAddRegionParam(-72, FBAttachType.kFBAttachRight, "")
    y = FBAddRegionParam(-30, FBAttachType.kFBAttachBottom, "")
    w = FBAddRegionParam(70, FBAttachType.kFBAttachNone, "")
    h = FBAddRegionParam(25, FBAttachType.kFBAttachNone, "")
    mainLyt.AddRegion("button", "button", x, y, w, h)

    lSaveButton = FBButton()
    lSaveButton.Caption = "Export..."
    lSaveButton.Justify = FBTextJustify.kFBTextJustifyCenter
    mainLyt.SetControl("button", lSaveButton)
    lSaveButton.OnClick.Add(SaveButtonCallback)

    #
    # Layout for the comments
    #
    x = FBAddRegionParam(5, FBAttachType.kFBAttachLeft, "")
    y = FBAddRegionParam(65, FBAttachType.kFBAttachNone, "")
    w = FBAddRegionParam(255, FBAttachType.kFBAttachNone, "")
    h = FBAddRegionParam(65, FBAttachType.kFBAttachNone, "")
    mainLyt.AddRegion("comment", "comment", x, y, w, h)
    lytComment = FBHBoxLayout()
    mainLyt.SetControl("comment", lytComment)

    #
    # Add our Format Comment
    #
    gFormatCommentLabel.Caption = tr(gFbxComment)
    lytComment.Add(gFormatCommentLabel, 250)


def CreateTool():
    # Tool creation will serve as the hub for all other controls
    t = FBCreateUniqueTool("FBX Export")
    t.StartSizeX = 350
    t.StartSizeY = 170
    BuildUI(t)
    return t


#
# main body
#
# Development? - need to recreate each time!!
gDEVELOPMENT = False

if gDEVELOPMENT:
    FBDestroyToolByName(gToolName)

if gToolName in FBToolList:
    tool = FBToolList[gToolName]
    ShowTool(tool)
else:
    tool = CreateTool()
    if gDEVELOPMENT:
        ShowTool(tool)




