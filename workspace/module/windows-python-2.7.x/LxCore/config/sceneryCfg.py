# coding=utf-8
from LxBasic import bscModifiers, bscCommands

from LxCore import lxConfigure
#
LynxiProduct_Scenery_Class_Scenery = 'scenery'
LynxiProduct_Scenery_Class_Group = 'group'
LynxiProduct_Scenery_Class_Assembly = 'unit'
#
none = ''


#
def scnBasicClass():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        LynxiProduct_Scenery_Class_Scenery,
        LynxiProduct_Scenery_Class_Group
    ]
    return lis


#
def scnBasicViewLinkDic():
    dic = bscCommands.orderedDict()
    dic[lxConfigure.LynxiProduct_Scenery_Link_Scenery] = 'Scenery', u'场景布景'
    dic[lxConfigure.LynxiProduct_Scene_Link_layout] = 'Layout', u'场景预览'
    dic[lxConfigure.LynxiProduct_Scene_Link_Animation] = 'Animation', u'场景动画'
    dic[lxConfigure.LynxiProduct_Scene_Link_Simulation] = 'Simulation', u'场景解算'
    dic[lxConfigure.LynxiProduct_Scene_Link_Light] = 'Light', u'场景灯光'
    return dic


@bscModifiers.fncDictSwitch
def scnBasicViewClassDic(*args):
    dic = bscCommands.orderedDict()
    dic[LynxiProduct_Scenery_Class_Scenery] = 'Scenery', u'场景'
    dic[LynxiProduct_Scenery_Class_Group] = 'Group', u'组合'
    return dic


#
def basicSceneryPriorities():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        'major',
        'minor',
        'util'
    ]
    return lis


#
def basicSceneryLinks():
    lis = [
        lxConfigure.LynxiProduct_Scenery_Link_Scenery,
        lxConfigure.LynxiProduct_Scene_Link_layout,
        lxConfigure.LynxiProduct_Scene_Link_Animation,
        lxConfigure.LynxiProduct_Scene_Link_Simulation,
        lxConfigure.LynxiProduct_Scene_Link_Light,
    ]
    return lis
