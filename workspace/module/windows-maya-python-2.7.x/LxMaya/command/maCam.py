# coding=utf-8
import math

from LxBasic import bscCommands
#
from LxCore import lxConfigure
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.OpenMaya as OpenMaya
# noinspection PyUnresolvedReferences
import maya.OpenMayaUI as OpenMayaUI
#
from fractions import Fraction
#
from LxPreset import prsMethods
#
from LxCore.preset.prod import projectPr, scenePr
#
from LxMaya.command import maUtils, maRender
#
from LxMaya.product.data import datScene

#
currentProjectName = projectPr.getMayaProjectName()
#
timeConfig = dict(
    game='15 FPS',
    film='24 FPS',
    pal='25 FPS',
    ntsc='30 FPS',
    sho='48 FPS',
    palf='50 FPS',
    ntscf='60 FPS'
)
#
none = ''


# Clean Camera's HUD
def setCameraCloseHud():
    hud = cmds.headsUpDisplay(listHeadsUpDisplays=1)
    if hud:
        for i in hud:
            cmds.headsUpDisplay(i, remove=1)


# Get View's Camera Name
def getActiveCameraShape():
    cameraView = OpenMayaUI.M3dView.active3dView()
    cameraDag = OpenMaya.MDagPath()
    cameraView.getCamera(cameraDag)
    cameraName = cameraDag.fullPathName()
    return cameraName


# Project Information
def getProjectInfo():
    projectInfo = lxConfigure.LynxiValue_Unspecified
    projectName = currentProjectName
    #
    infos = datScene.getSceneInfo()
    if infos:
        sceneIndex, sceneClass, sceneName, sceneVariant, sceneStage = infos[0]
        projectInfo = '%s ( %s )' % (projectName, sceneStage.capitalize())
    return projectInfo


# Get Camera Information
def getCameraInfo():
    cameraShape = getActiveCameraShape()
    focalLength = cmds.camera(cameraShape, query=1, focalLength=1)
    return float(focalLength)


# Get Scene Information
def getSceneInfo():
    sceneInfo = u'N/a'
    #
    infos = datScene.getSceneInfo()
    if infos:
        sceneIndex, sceneClass, sceneName, sceneVariant, sceneStage = infos[0]
        sceneInfo = scenePr.getSceneViewInfo(sceneIndex, sceneClass, sceneName)
    return sceneInfo


# Get Frame Information
def getFrameInfo():
    startFrame = cmds.playbackOptions(query=1, min=1)
    endFrame = cmds.playbackOptions(query=1, max=1)
    currentFrame = cmds.currentTime(query=1)
    zfillCount = len(str(endFrame))
    frame = currentFrame - startFrame
    maxFrame = endFrame - startFrame
    frameInfo = '%s / %s | %s / ( %s - %s )' % (
        str(frame).zfill(zfillCount), str(maxFrame).zfill(zfillCount), str(currentFrame).zfill(zfillCount), str(startFrame).zfill(zfillCount),
        str(endFrame).zfill(zfillCount))
    return frameInfo


# Get Time Information
def getTimeInfo():
    mayaTimeUnit = maUtils.getTimeUnit()
    #
    startFrame = cmds.playbackOptions(query=1, min=1)
    endFrame = cmds.playbackOptions(query=1, max=1)
    currentFrame = cmds.currentTime(query=1)
    timeRange = '%.2f' % ((endFrame - startFrame) / int(timeConfig[mayaTimeUnit][:2]))
    frame = currentFrame - startFrame
    time = '%.2f' % (frame / int(timeConfig[mayaTimeUnit][:2]))
    zfillCount = len(str(timeRange))
    timeInfo = '%s / %s' % (str(time).zfill(zfillCount), str(timeRange).zfill(zfillCount))
    return timeInfo


# Set Camera's Gate
def setCameraView(cameraShape=none, displayResolution=0, displaySafeTitle=0):
    if not cameraShape:
        cameraShape = getActiveCameraShape()

    cmds.camera(
        cameraShape,
        edit=1,
        displayFilmGate=0,
        displayResolution=displayResolution,
        displayGateMask=displayResolution,
        displaySafeAction=0,
        displaySafeTitle=displaySafeTitle,
        displayFieldChart=0,
        filmFit=1,
        overscan=1
    )
    cmds.setAttr(cameraShape + '.displayGateMaskOpacity', 1)
    cmds.setAttr(cameraShape + '.displayGateMaskColor', 0, 0, 0, type='double3')


# Get Render Size
def getRenderSize():
    width, height = maRender.getRenderSize()
    sizeInfo = '%s*%spx( %s )' % (width, height, Fraction(width, height))
    return sizeInfo


# Get Fps Information
def getFpsInfo():
    mayaTimeUnit = maUtils.getTimeUnit()
    cameraShape = getActiveCameraShape()
    focalLength = cmds.camera(cameraShape, query=1, focalLength=1)
    fpsInfo = '%s ( %s mm )' % (timeConfig[mayaTimeUnit], focalLength)
    return fpsInfo


#
def getArtistInfo():
    string = '%s ( %s ) @ %s' % (
        prsMethods.Personnel.userChnname(),
        prsMethods.Personnel.userEngname(),
        prsMethods.Personnel.userTeam()
    )
    return string


# Set Camera's HUD Color
def setHudColor(labelColor=19, valueColor=16):
    isExists = cmds.displayColor("headsUpDisplayLabels", q=1, dormant=1)
    if isExists:
        try:
            cmds.displayColor('headsUpDisplayLabels', labelColor, dormant=1)
        except:
            pass
    isExists = cmds.displayColor('headsUpDisplayValues', q=1, dormant=1)
    if isExists:
        try:
            cmds.displayColor('headsUpDisplayValues', valueColor, dormant=1)
        except:
            pass


#
def hudConfig(fontSize='large'):
    dic = bscCommands.orderedDict()
    dic['Time Config Info'] = dict(
        section=0, block=0,
        blockAlignment='center',
        labelFontSize=fontSize,
        dataFontSize=fontSize,
        blockSize=fontSize,
        label='Fps ( Focal ) : ',
        labelWidth=96,
        command=lambda: getFpsInfo(),
        attachToRefresh=1
    )
    dic['Frame Info'] = dict(
        section=2, block=0,
        blockAlignment='center',
        labelFontSize=fontSize,
        dataFontSize=fontSize,
        blockSize=fontSize,
        label='Frame : ',
        labelWidth=96,
        command=lambda: getFrameInfo(),
        attachToRefresh=1
    )
    dic['Time Info'] = dict(
        section=4, block=0,
        blockAlignment='center',
        labelFontSize=fontSize,
        dataFontSize=fontSize,
        blockSize=fontSize,
        label='Time : ',
        labelWidth=48,
        command=lambda: getTimeInfo(),
        attachToRefresh=1
    )
    #
    dic['Artist Info'] = dict(
        section=5, block=0,
        blockAlignment='center',
        labelFontSize=fontSize,
        dataFontSize=fontSize,
        blockSize=fontSize,
        label='Artist : ',
        labelWidth=48,
        command=lambda: getArtistInfo(),
        attachToRefresh=1
    )
    dic['Scene Info'] = dict(
        section=7, block=0,
        blockAlignment='center',
        labelFontSize=fontSize,
        dataFontSize=fontSize,
        blockSize=fontSize,
        label='Name : ',
        labelWidth=48,
        command=lambda: getSceneInfo(),
        attachToRefresh=1
    )
    dic['Date Info'] = dict(
        section=9, block=0,
        blockAlignment='center',
        labelFontSize=fontSize,
        dataFontSize=fontSize,
        blockSize=fontSize,
        label='Date : ',
        labelWidth=48,
        command=lambda: bscCommands.getCnViewDate(),
        attachToRefresh=1
    )
    return dic


#
def setCameraHud(fontSize='large'):
    config = hudConfig(fontSize)
    for k, v in config.items():
        cmds.headsUpDisplay(
            k,
            section=v['section'],
            block=v['block'],
            blockAlignment=v['blockAlignment'],
            labelFontSize=v['labelFontSize'],
            dataFontSize=v['dataFontSize'],
            blockSize=v['blockSize'],
            label=v['label'],
            labelWidth=v['labelWidth'],
            command=v['command'],
            attachToRefresh=v['attachToRefresh']
        )
    #
    setHudColor()


#
def setCameraLook(cameraObject, objectLis):
    cameraShape = maUtils.getNodeShape(cameraObject)
    #
    cmds.setAttr('{}.rotate'.format(cameraObject), -45, 45, 0)
    sx, sy, xz = cmds.getAttr('{}.rotate'.format(cameraObject))[0]
    #
    b = cmds.getAttr('{}.focalLength'.format(cameraShape))
    filmFit = cmds.getAttr('{}.filmFit'.format(cameraShape))
    if filmFit in [1, 3]:
        a = 17.9999906718
    else:
        a = 11.9552358666
    #
    angle = math.degrees(math.atan(a / b))
    #
    (x0, x1), (y0, y1), (z0, z1) = cmds.polyEvaluate(objectLis, boundingBox=1)
    wx, wy, wz = x1 - x0, y1 - y0, z1 - z0
    #
    r = max(wx, wy)
    #
    tx, ty, tz = wx / 2 + x0, wy / 2 + y0, (r / 2) / math.tan(math.radians(angle)) + wz + z0
    #
    tx_ = math.sin(math.radians(sy))*tz
    tz_ = math.cos(math.radians(sy))*tz
    ty_ = math.sin(math.radians(-sx))*tz
    tz_ = math.cos(math.radians(-sx))*tz_
    #
    cmds.setAttr('{}.translate'.format(cameraObject), tx_, ty_, tz_)
