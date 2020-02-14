# coding=utf-8
from LxBasic import bscCore, bscModifiers

from LxCore import lxConfigure
#
VAR_product_scenery_category_scenery = 'scenery'
VAR_product_scenery_category_Group = 'group'
VAR_product_scenery_category_Assembly = 'unit'
#
none = ''


#
def scnBasicClass():
    lis = [
        lxConfigure.LynxiValue_Unspecified,
        VAR_product_scenery_category_scenery,
        VAR_product_scenery_category_Group
    ]
    return lis


#
def scnBasicViewLinkDic():
    dic = bscCore.orderedDict()
    dic[lxConfigure.VAR_product_scenery_link_scenery] = 'Scenery', u'场景布景'
    dic[lxConfigure.VAR_product_scene_link_layout] = 'Layout', u'场景预览'
    dic[lxConfigure.VAR_product_scene_link_animation] = 'Animation', u'场景动画'
    dic[lxConfigure.VAR_product_scene_link_simulation] = 'Simulation', u'场景解算'
    dic[lxConfigure.VAR_product_scene_link_light] = 'Light', u'场景灯光'
    return dic


@bscModifiers.fncDictSwitch
def scnBasicViewClassDic(*args):
    dic = bscCore.orderedDict()
    dic[VAR_product_scenery_category_scenery] = 'Scenery', u'场景'
    dic[VAR_product_scenery_category_Group] = 'Group', u'组合'
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
        lxConfigure.VAR_product_scenery_link_scenery,
        lxConfigure.VAR_product_scene_link_layout,
        lxConfigure.VAR_product_scene_link_animation,
        lxConfigure.VAR_product_scene_link_simulation,
        lxConfigure.VAR_product_scene_link_light,
    ]
    return lis
