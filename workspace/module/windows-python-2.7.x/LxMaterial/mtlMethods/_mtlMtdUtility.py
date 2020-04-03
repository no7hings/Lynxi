# coding:utf-8
from LxBasic import bscMethods

from .. import mtlConfigure


class ArnoldDefs(mtlConfigure.Utility):
    @classmethod
    def raw(cls):
        return bscMethods.OsJsonFile.read(
            cls.DEF_mtl_arnold_node_defs_file
        ) or {}

    @classmethod
    def objectDef(cls, categoryString):
        raw = cls.raw()
        assert categoryString in raw, u'Category "{}" is Non-Definition'.format(categoryString)
        return raw.get(
            categoryString, {}
        )

    @classmethod
    def materialDef(cls):
        return bscMethods.OsJsonFile.read(
            cls.DEF_mtl_arnold_material_def_file
        ) or {}

    @classmethod
    def geometryDef(cls):
        return bscMethods.OsJsonFile.read(
            cls.DEF_mtl_arnold_geometry_def_file
        ) or {}

    @classmethod
    def outputDefs(cls):
        return bscMethods.OsJsonFile.read(
            cls.DEF_mtl_arnold_output_defs_file
        ) or {}

    @classmethod
    def portChildDefs(cls):
        return bscMethods.OsJsonFile.read(
            cls.DEF_mtl_arnold_port_child_defs_file
        ) or {}


class MayaArnoldDefs(mtlConfigure.Utility):
    @classmethod
    def raw(cls):
        return bscMethods.OsJsonFile.read(cls.DEF_mtl_maya_arnold_node_defs_file) or {}

    @classmethod
    def objectDef(cls, categoryString):
        raw = cls.raw()
        assert categoryString in raw, u'Category "{}" is Non-Definition'.format(categoryString)
        return raw.get(
            categoryString, {}
        )

    @classmethod
    def materialDef(cls):
        return bscMethods.OsJsonFile.read(
            cls.DEF_mtl_maya_arnold_material_def_file
        ) or {}

    @classmethod
    def geometryDef(cls):
        return bscMethods.OsJsonFile.read(
            cls.DEF_mtl_maya_arnold_geometry_def_file
        ) or {}

    @classmethod
    def outputDefs(cls):
        return {}

    @classmethod
    def portChildDefs(cls):
        return bscMethods.OsJsonFile.read(
            cls.DEF_mtl_maya_arnold_port_child_defs_file
        ) or {}
