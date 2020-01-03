# coding=utf-8
from LxCore import lxBasic, lxCore_
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
        lxCore_.LynxiValue_Unspecified,
        LynxiProduct_Scene_Class_Scene,
        LynxiProduct_Scene_Class_Act
    ]
    return lis


@lxBasic.getDicMethod
def scBasicViewLinkDic(*args):
    dic = lxBasic.orderedDict()
    dic[lxCore_.LynxiProduct_Scene_Link_layout] = 'Layout', u'预览'
    dic[lxCore_.LynxiProduct_Scene_Link_Animation] = 'Animation', u'动画'
    dic[lxCore_.LynxiProduct_Scene_Link_Simulation] = 'Simulation', u'解算'
    dic[lxCore_.LynxiProduct_Scene_Link_Solver] = 'Solver', u'模拟'
    dic[lxCore_.LynxiProduct_Scene_Link_Light] = 'Light', u'灯光'
    return dic


@lxBasic.getDicMethod
def scBasicViewClassDic(*args):
    dic = lxBasic.orderedDict()
    dic[LynxiProduct_Scene_Class_Scene] = 'Scene', u'镜头'
    dic[LynxiProduct_Scene_Class_Act] = 'Act', u'动作'
    return dic


#
def basicScenePriorityLis():
    lis = [
        lxCore_.LynxiValue_Unspecified,
        'major',
        'minor',
        'util'
    ]
    return lis


#
def basicSceneLinkLis():
    lis = [
        lxCore_.LynxiProduct_Scene_Link_layout,
        lxCore_.LynxiProduct_Scene_Link_Animation,
        lxCore_.LynxiProduct_Scene_Link_Solver,
        lxCore_.LynxiProduct_Scene_Link_Simulation,
        lxCore_.LynxiProduct_Scene_Link_Light,
    ]
    return lis
