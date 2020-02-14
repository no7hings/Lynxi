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
VAR_product_scene_category_scene = 'scene'
VAR_product_scene_category_act = 'act'
#
none = ''


#
def scBasicClass():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        VAR_product_scene_category_scene,
        VAR_product_scene_category_act
    ]
    return lis


@bscModifiers.fncDictSwitch
def scBasicViewLinkDic(*args):
    dic = bscCore.orderedDict()
    dic[lxConfigure.VAR_product_scene_link_layout] = 'Layout', u'预览'
    dic[lxConfigure.VAR_product_scene_link_animation] = 'Animation', u'动画'
    dic[lxConfigure.VAR_product_scene_link_simulation] = 'Simulation', u'解算'
    dic[lxConfigure.VAR_product_scene_link_solver] = 'Solver', u'模拟'
    dic[lxConfigure.VAR_product_scene_link_light] = 'Light', u'灯光'
    return dic


@bscModifiers.fncDictSwitch
def scBasicViewClassDic(*args):
    dic = bscCore.orderedDict()
    dic[VAR_product_scene_category_scene] = 'Scene', u'镜头'
    dic[VAR_product_scene_category_act] = 'Act', u'动作'
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
        lxConfigure.VAR_product_scene_link_layout,
        lxConfigure.VAR_product_scene_link_animation,
        lxConfigure.VAR_product_scene_link_solver,
        lxConfigure.VAR_product_scene_link_simulation,
        lxConfigure.VAR_product_scene_link_light,
    ]
    return lis
