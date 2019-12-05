# coding=utf-8
import collections
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
none = ''


# Get Target Object's Box Data
def getBox(maObj):
    if cmds.objExists(maObj):
        _x, _y, _z, x, y, z = cmds.exactWorldBoundingBox(maObj)
        xValue = x - _x
        yValue = y - _y
        zValue = z - _z
        xPosition = x + _x
        yPosition = y + _y
        zPosition = z + _z
        return xValue / 2, yValue / 2, zValue / 2, xPosition / 2, yPosition / 2, zPosition / 2


# Dic For Create Box
def boxDic(maObj):
    x, y, z, X, Y, Z = [.5, .5, .5, 0, 0, 0]
    if cmds.objExists(maObj):
        x, y, z, X, Y, Z = getBox(maObj)
    dic = collections.OrderedDict()
    dic['x'] = dict(yz=[('.localPosition', X, Y+y, Z+z), ('.localScale', x, 0, 0)],
                    _yz=[('.localPosition', X, Y-y, Z+z), ('.localScale', x, 0, 0)],
                    _y_z=[('.localPosition', X, Y-y, Z-z), ('.localScale', x, 0, 0)],
                    y_z=[('.localPosition', X, Y+y, Z-z), ('.localScale', x, 0, 0)])
    dic['y'] = dict(xz=[('.localPosition', X+x, Y, Z+z), ('.localScale', 0, y, 0)],
                    _xz=[('.localPosition', X+x, Y, Z-z), ('.localScale', 0, y, 0)],
                    _x_z=[('.localPosition', X-x, Y, Z-z), ('.localScale', 0, y, 0)],
                    x_z=[('.localPosition', X-x, Y, Z+z), ('.localScale', 0, y, 0)])
    dic['z'] = dict(xy=[('.localPosition', X+x, Y+y, Z), ('.localScale', 0, 0, z)],
                    _xy=[('.localPosition', X-x, Y+y, Z), ('.localScale', 0, 0, z)],
                    _x_y=[('.localPosition', X-x, Y-y, Z), ('.localScale', 0, 0, z)],
                    x_y=[('.localPosition', X+x, Y-y, Z), ('.localScale', 0, 0, z)])
    return dic


# Create Boxs
def spaceBoxs(objects=none):
    if not objects:
        objects = cmds.ls(selection=True)
    #
    for maObj in objects:
        data = boxDic(maObj)
        box = maObj + '_box'
        if cmds.objExists(box):
            cmds.delete(box)
        if not cmds.objExists(box):
            cmds.createNode('transform', name=box)
            for k, v in data.items():
                for ik, iv in v.items():
                    border = box + ik
                    cmds.createNode('locator', name=border, parent=box)
                    cmds.setAttr(border + iv[0][0], iv[0][1], iv[0][2], iv[0][3])
                    cmds.setAttr(border + iv[1][0], iv[1][1], iv[1][2], iv[1][3])
    cmds.select(clear=1)


# Create Box
def spaceBox(name=none, maObj=none, position=none):
    if not name:
        name = 'null'
    data = boxDic(maObj)
    if cmds.objExists(name):
        cmds.delete(name)
    if not cmds.objExists(name):
        cmds.createNode('transform', name=name)
        for k, v in data.items():
            for ik, iv in v.items():
                border = name + ik
                cmds.createNode('locator', name=border, parent=name)
                cmds.setAttr(border + iv[0][0], iv[0][1], iv[0][2], iv[0][3])
                cmds.setAttr(border + iv[1][0], iv[1][1], iv[1][2], iv[1][3])
    cmds.select(clear=1)
