# coding=utf-8
from LxCore import lxBasic, lxCore_
#
LynxiProduct_Scenery_Class_Scenery = 'scenery'
LynxiProduct_Scenery_Class_Group = 'group'
LynxiProduct_Scenery_Class_Assembly = 'unit'
#
none = ''


#
def scnBasicClass():
    lis = [
        lxCore_.LynxiValue_Unspecified,
        LynxiProduct_Scenery_Class_Scenery,
        LynxiProduct_Scenery_Class_Group
    ]
    return lis


#
def scnBasicViewLinkDic():
    dic = lxBasic.orderedDict()
    dic[lxCore_.LynxiProduct_Scenery_Link_Scenery] = 'Scenery', u'场景布景'
    dic[lxCore_.LynxiProduct_Scene_Link_layout] = 'Layout', u'场景预览'
    dic[lxCore_.LynxiProduct_Scene_Link_Animation] = 'Animation', u'场景动画'
    dic[lxCore_.LynxiProduct_Scene_Link_Simulation] = 'Simulation', u'场景解算'
    dic[lxCore_.LynxiProduct_Scene_Link_Light] = 'Light', u'场景灯光'
    return dic


@lxBasic.getDicMethod
def scnBasicViewClassDic(*args):
    dic = lxBasic.orderedDict()
    dic[LynxiProduct_Scenery_Class_Scenery] = 'Scenery', u'场景'
    dic[LynxiProduct_Scenery_Class_Group] = 'Group', u'组合'
    return dic


#
def basicSceneryPriorities():
    lis = [
        lxCore_.LynxiValue_Unspecified,
        'major',
        'minor',
        'util'
    ]
    return lis


#
def basicSceneryLinks():
    lis = [
        lxCore_.LynxiProduct_Scenery_Link_Scenery,
        lxCore_.LynxiProduct_Scene_Link_layout,
        lxCore_.LynxiProduct_Scene_Link_Animation,
        lxCore_.LynxiProduct_Scene_Link_Simulation,
        lxCore_.LynxiProduct_Scene_Link_Light,
    ]
    return lis
