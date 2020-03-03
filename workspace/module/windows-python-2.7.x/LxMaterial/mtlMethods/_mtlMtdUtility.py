# coding:utf-8
from LxBasic import bscMethods

from LxMaterial import mtlConfigure


class ArnoldNodedefs(mtlConfigure.Utility):
    @classmethod
    def raw(cls):
        return bscMethods.OsJsonFile.read(cls.DEF_mtl_arnold_nodedefs_file) or {}

    @classmethod
    def categoryRaw(cls):
        return cls.raw().keys()


class MayaArnoldNodedefs(mtlConfigure.Utility):
    @classmethod
    def raw(cls):
        return bscMethods.OsJsonFile.read(cls.DEF_mtl_maya_arnold_nodedefs_file) or {}

    @classmethod
    def categoryRaw(cls):
        return cls.raw().keys()


class ArnoldNodedef(mtlConfigure.Utility):
    @classmethod
    def raw(cls, categoryString):
        raw = ArnoldNodedefs.raw()
        assert categoryString in raw, u'Category "{}" is Non-Definition'.format(categoryString)
        return raw.get(categoryString, {})
    
    @classmethod
    def typeString(cls, categoryString):
        return cls.raw(categoryString).get(
            cls.DEF_mtl_key_type_string,
            []
        )

    @classmethod
    def inputRaw(cls, categoryString):
        return cls.raw(categoryString).get(
            cls.DEF_mtl_key_port,
            []
        )

    @classmethod
    def outputRaw(cls, categoryString):
        return mtlConfigure.Utility.DEF_mtl_output_def_dict.get(
            cls.typeString(categoryString), []
        )


class ArnoldPortdef(mtlConfigure.Utility):

    @classmethod
    def channelRaw(cls, typeString):
        return mtlConfigure.Utility.DEF_mtl_channel_def_dict.get(
            typeString, []
        )


class MayaArnoldNodedef(mtlConfigure.Utility):
    @classmethod
    def raw(cls, categoryString):
        raw = MayaArnoldNodedefs.raw()
        assert categoryString in raw, u'Category "{}" is Non-Definition'.format(categoryString)
        return raw.get(categoryString, {})
