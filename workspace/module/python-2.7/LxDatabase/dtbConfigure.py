# coding:utf-8
from LxBasic import bscCfg, bscMethods

from LxPreset import prsOutputs


class DtbBasic(object):
    DbAssetRoot = prsOutputs.Util.dbAssetRoot

    DbRoot_Basic = 'e:/myproject'
    #
    LxDb_Folder_Basic = '.lynxi.database'
    #
    LxDb_Folder_Unit = '.unit'
    LxDb_Folder_Datum = '.datum'
    LxDb_Folder_File = '.file'
    #
    LxDb_Class_Basic = 'basic'
    LxDb_Class_Preset = 'preset'
    LxDb_Class_Product = 'product'
    LxDb_Class_Maya = 'maya'
    LxDb_Class_User = 'user'
    #
    LxDb_Unit_Type_LightLink = 'lightLink'
    LxDb_Unit_Type_RenderOption = 'renderOption'
    #
    LxDb_Type_Unit_Include_Raw = 'raw'
    LxDb_Type_Unit_Include_Set = 'set'
    LxDb_Type_Unit_Include_Attribute = 'attribute'
    LxDb_Type_Unit_Include_Config = 'config'
    LxDb_Type_Unit_Include_Compose = 'compose'
    LxDb_Type_Unit_Include_File = 'file'
    #
    LxDb_Type_Unit_Json = 'json'
    LxDb_Type_Unit_Python = 'python'
    LxDb_Type_Unit_Image = 'image'
    LxDb_Type_Unit_Default = 'default'
    #
    LxDb_Type_Datum_Json = 'json'
    LxDb_Type_Datum_Python = 'python'
    LxDb_Type_Datum_File = 'file'
    #
    LxDb_Datum_Type_Dic = {
        LxDb_Type_Unit_Json: LxDb_Type_Datum_Json,
        LxDb_Type_Unit_Python: LxDb_Type_Datum_Python
    }
    #
    LxDb_Include_Branch_Main = 'main'
    #
    LxDb_Ext_Unit_Include_Definition = '.definition.json'
    LxDb_Ext_Unit_Include_Branch = '.branch.json'
    #
    LxDb_Ext_Unit_Include_Raw = '.raw.json'
    LxDb_Ext_Unit_Include_Set = '.set.json'
    LxDb_Ext_Unit_Include_Attribute = '.attribute.json'
    LxDb_Ext_Unit_Include_Config = '.config.json'
    LxDb_Ext_Unit_Include_Compose = '.compose.json'
    LxDb_Ext_Unit_Include_File = '.file.json'
    #
    LxDb_Ext_Unit_Include_Dic = {
        LxDb_Type_Unit_Include_Raw: LxDb_Ext_Unit_Include_Raw,
        LxDb_Type_Unit_Include_Set: LxDb_Ext_Unit_Include_Set,
        LxDb_Type_Unit_Include_Attribute: LxDb_Ext_Unit_Include_Attribute,
        LxDb_Type_Unit_Include_Config: LxDb_Ext_Unit_Include_Config,
        LxDb_Type_Unit_Include_Compose: LxDb_Ext_Unit_Include_Compose,
        LxDb_Type_Unit_Include_File: LxDb_Ext_Unit_Include_File
    }
    #
    LxDb_ExtVAR_kit__window__version = '.version.json'
    LxDb_Ext_Unit_Include_Info = '.info.json'
    #
    LxDb_Ext_Index = '.index.json'
    #
    LxDb_Ext_Json = '.json'
    LxDb_Ext_Info = '.info.json'
    #
    LxDb_Key_Enable = 'enable'
    LxDb_Key_Name = 'name'
    LxDb_Key_Source = 'source'

    DEF_key_info_username = 'user'
    DEF_key_info_timestamp = 'time'
    #
    DEF_key_info_hostname = 'hostName'
    DEF_key_info_host = 'host'

    DEF_key_info_description = 'description'
    DEF_key_info_note = 'note'

    @classmethod
    def _dbProductUnitIndexFile(cls, productModuleString):
        return u'{0}/{1}/{2}/{3}'.format(
            cls.DbAssetRoot, prsOutputs.Util.dbBasicFolderName, bscCfg.BscUtility.LynxiDatabaseKey_Index,
            bscMethods.String.toUniqueId(productModuleString)
        )

    @classmethod
    def _dbProductUnitSetFile(cls, dbUnitId):
        return u'{0}/{1}/{2}/{3}'.format(
            cls.DbAssetRoot, prsOutputs.Util.dbBasicFolderName, bscCfg.BscUtility.LynxiDatabaseKey_Set,
            dbUnitId
        )
