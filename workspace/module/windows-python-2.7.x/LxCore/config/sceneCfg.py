# coding=utf-8
from LxBasic import bscCore, bscModifiers

from LxCore import lxConfigure
#
CameraSep = ';'
#
SceneCameraAttr = 'camera'
#
MayaDefaultCameras = ['persp', 'top', 'front', 'side']
#
LynxiProduct_Scene_Class_Scene = 'scene'
LynxiProduct_Scene_Class_Act = 'act'
#
none = ''


#
def scBasicClass():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        LynxiProduct_Scene_Class_Scene,
        LynxiProduct_Scene_Class_Act
    ]
    return lis


@bscModifiers.fncDictSwitch
def scBasicViewLinkDic(*args):
    dic = bscCore.orderedDict()
    dic[lxConfigure.LynxiProduct_Scene_Link_layout] = 'Layout', u'预览'
    dic[lxConfigure.LynxiProduct_Scene_Link_Animation] = 'Animation', u'动画'
    dic[lxConfigure.LynxiProduct_Scene_Link_Simulation] = 'Simulation', u'解算'
    dic[lxConfigure.LynxiProduct_Scene_Link_Solver] = 'Solver', u'模拟'
    dic[lxConfigure.LynxiProduct_Scene_Link_Light] = 'Light', u'灯光'
    return dic


@bscModifiers.fncDictSwitch
def scBasicViewClassDic(*args):
    dic = bscCore.orderedDict()
    dic[LynxiProduct_Scene_Class_Scene] = 'Scene', u'镜头'
    dic[LynxiProduct_Scene_Class_Act] = 'Act', u'动作'
    return dic


#
def basicScenePriorityLis():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        'major',
        'minor',
        'util'
    ]
    return lis


#
def basicSceneLinkLis():
    lis = [
        lxConfigure.LynxiProduct_Scene_Link_layout,
        lxConfigure.LynxiProduct_Scene_Link_Animation,
        lxConfigure.LynxiProduct_Scene_Link_Solver,
        lxConfigure.LynxiProduct_Scene_Link_Simulation,
        lxConfigure.LynxiProduct_Scene_Link_Light,
    ]
    return lis
