# coding:utf-8
# noinspection PyUnresolvedReferences
from maya import cmds
# noinspection PyUnresolvedReferences,PyPep8Naming
from maya.api import OpenMaya as om2


class Source(object):
    def __init__(self, path):
        self._path = path

    def path(self):
        return self._path

    def curves(self):
        return [Curve(i) for i in cmds.ls(self._path, dagObjects=1, noIntermediate=1, long=1, type='nurbsCurve')]


class Groom(object):
    def __init__(self, path):
        self._path = path

    def path(self):
        return self._path

    def groups(self):
        return [Group(i) for i in cmds.listRelatives(self._path, children=1, fullPath=1, type='transform')]

    def setup(self):
        for group_id, group in enumerate(self.groups()):
            group.attribute('groom_group_id').add(type='long', value=group_id)
            group.attribute('groom_group_id_AbcGeomScope').add(type='string', value='con')

    def curves(self):
        return [Curve(i) for i in cmds.ls(self._path, dagObjects=1, noIntermediate=1, long=1, type='nurbsCurve')]


class Group(object):
    def __init__(self, path):
        self._path = path

    def path(self):
        return self._path

    def attribute(self, name):
        return Attribute(name, self)

    def curves(self):
        return [Curve(i) for i in cmds.ls(self._path, dagObjects=1, noIntermediate=1, long=1, type='nurbsCurve')]


class Curve(object):
    def __init__(self, path):
        self._path = path
        self._om2_curve = om2.MFnNurbsCurve(
            om2.MGlobal.getSelectionListByName(self._path).getDagPath(0)
        )

    def cvs_count(self):
        return self._om2_curve.numCVs

    def path(self):
        return self._path

    def attribute(self, name):
        return Attribute(name, self)

    def width(self):
        return cmds.getAttr('{}.width'.format(self._path))

    def set_width(self, value):
        attr = '{}.width'.format(self.path())
        if cmds.objExists(attr) is False:
            cmds.addAttr(self.path(), longName='width', dataType='doubleArray', keyable=True)
        cmds.setAttr(attr, value, type='doubleArray')

    def __str__(self):
        return '{}(path="{}")'.format(
            self.__class__.__name__,
            self._path
        )

    def __repr__(self):
        return self.__str__()


class Attribute(object):
    def __init__(self, name, node):
        self._name = name
        self._node = node
        self._path = '{}.{}'.format(self._node.path(), self._name)

    def path(self):
        return self._path

    def name(self):
        return self._name

    # noinspection PyShadowingBuiltins
    def add(self, type, value):
        if cmds.objExists(self.path()) is False:
            if type in ['string', 'doubleArray']:
                cmds.addAttr(self._node.path(), longName=self.name(), dataType=type, keyable=True)
                cmds.setAttr(self._path, value, type=type)
            else:
                cmds.addAttr(
                    self._node.path(), longName=self.name(), attributeType=type, keyable=True
                )
                cmds.setAttr(self._path, value)
