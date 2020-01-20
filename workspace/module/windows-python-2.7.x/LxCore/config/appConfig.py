# coding:utf-8
import cgitb
#
import os
#
import collections
#
import uuid
#
import re
#
import time
#
from LxPreset import prsConfigure
#
from LxCore import lxConfigure
#
from LxCore.preset import prsVariant
#
cgitb.enable(format='text')


#
def orderedDict(*args):
    return collections.OrderedDict(*args)


#
class Cfg_Basic(object):
    Folder_Basic = '.lynxi'
    LynxiOsFolder_Database = '.database'
    LynxiOsFolder_History = '.lxHistory'
    LynxiOsExt_Version = '.lxVersion'
    #
    LynxiOsExt_Info = '.lxInfo'
    LynxiOsExt_Log = '.lxLog'
    LynxiOsExt_Record = '.lxRecord'
    #
    LynxiOsPath_LocalTemporary = 'd:/{}.temporary'.format(Folder_Basic)
    LynxiOsPath_Log_Local = 'd:/{}.log'.format(Folder_Basic)
    #
    LynxiOsPath_Log_Server = 'e:/{}.log'.format(Folder_Basic)
    #
    LynxiEnable_Log = False
    #
    LynxiLogType_Exception = 'exception'
    LynxiLogType_Function = 'function'
    LynxiLogType_OsFile = 'osFile'
    LynxiLogType_Database = 'database'
    #
    OsTimeTagFormat = '%Y_%m%d_%H%M%S'
    #
    OsFileSep = '/'
    #
    LynxiValue_Unspecified = 'Unspecified'
    #
    LynxiUiIndex_EnName = 0
    LynxiUiIndex_ChName = 1
    #
    LynxiUiIndex_Language = LynxiUiIndex_ChName
    #
    LynxiDatabaseKey_Index = '.index'
    LynxiDatabaseKey_Set = '.set'
    LynxiDatabaseKey_Link = '.link'
    #
    LynxiUniqueId_Basic = '4908BDB4-911F-3DCE-904E-96E4792E75F1'
    #
    Environ_Key_Value = 'LYNXI_PATH_PRODUCT'
    Environ_Key_Path_Develop = 'LYNXI_PATH_DEVELOP'
    Environ_Key_Path_Product = 'LYNXI_PATH_PRODUCT'
    #
    Lynxi_Key_Info_Namespace = 'namespace'
    #
    Lynxi_Key_Info_Artist = 'user'
    Lynxi_Key_Info_Update = 'time'
    #
    Lynxi_Key_Info_HostName = 'hostName'
    Lynxi_Key_Info_Host = 'host'
    #
    Lynxi_Key_Info_SourceFile = 'sourceFile'
    #
    Lynxi_Key_Info_Description = 'description'
    Lynxi_Key_Info_Note = 'note'
    #
    LynxiEnable_Trance = True
    MaEnable_Trance = True
    MaEnable_Trance_UseOutputWindow = False
    #
    LynxiApp_Maya = 'maya'
    @staticmethod
    def orderedDict(*args):
        return collections.OrderedDict(*args)
    @staticmethod
    def _toStringCapitalize(string):
        return string[0].upper() + string[1:] if string else string
    @classmethod
    def str_camelcase2prettify(cls, string):
        return ' '.join([cls._toStringCapitalize(x) for x in re.findall('[a-zA-Z][a-z]*[0-9]*', string)])
    @classmethod
    def _stringToUniqueId(cls, string):
        uniqueId = uuid.uuid3(uuid.UUID(cls.LynxiUniqueId_Basic), str(string))
        return str(uniqueId).upper()
    @staticmethod
    def getDicMethod(func):
        def subFunc(*args):
            dic = func(*args)
            if args:
                key = args[0]
                if key:
                    return dic[key]
                else:
                    return dic
            else:
                return dic
        return subFunc
    @staticmethod
    def toVariantConvert(varName, string):
        def getStringLis():
            # noinspection RegExpSingleCharAlternation
            return [i for i in re.split("<|>", string) if i]
        #
        def getVariantLis():
            # noinspection RegExpSingleCharAlternation
            varPattern = re.compile(r'[<](.*?)[>]', re.S)
            return re.findall(varPattern, string)
        #
        def getVarStringLis():
            lis = []
            for i in strings:
                if i in variants:
                    lis.append(i)
                else:
                    v = '''"%s"''' % i
                    lis.append(v)
            return lis
        #
        strings = getStringLis()
        variants = getVariantLis()
        #
        varStrings = getVarStringLis()
        #
        command = '''{0} = '{1}' % ({2})'''.format(varName, '%s' * len(strings), ', '.join(varStrings))
        return command
    @staticmethod
    def _toNumberIn(string):
        varPattern = re.compile(r'[\[](.*?)[\]]', re.S)
        return re.findall(varPattern, string)
    @staticmethod
    def _toNamespaceByPathString(pathString, pathsep, namespacesep):
        return namespacesep.join(pathString.split(pathsep)[-1].split(namespacesep)[:-1]) + namespacesep
    @staticmethod
    def _toNamespaceByNameString(nameString, namespacesep):
        return namespacesep.join(nameString.split(namespacesep)[:-1]) + namespacesep
    @staticmethod
    def _toNameByPathString(pathString, pathsep, namespacesep):
        return pathString.split(pathsep)[-1].split(namespacesep)[-1]
    @staticmethod
    def _toNameByNameString(nameString, namespacesep):
        return nameString.split(namespacesep)[-1]
    @classmethod
    def _isStringMatch(cls, string, keyword):
        if keyword.startswith('*'):
            return string.endswith(keyword[1:])
        elif keyword.endswith('*'):
            return string.startswith(keyword[:-1])
        else:
            return keyword in string
    @classmethod
    def _toPathRebuildDatum(cls, pathString, pathsep, namespacesep):
        if pathString.startswith(pathsep):
            pathLis = []
            namespaceLis = []
            #
            lis1 = pathString.split(pathsep)
            if lis1:
                for i in lis1:
                    if i:
                        namespace = cls._toNamespaceByNameString(i, namespacesep)
                        name = cls._toNameByNameString(i, namespacesep)
                        if namespace:
                            if not namespace in namespaceLis:
                                namespaceLis.append(namespace)
                            #
                            index = namespaceLis.index(namespace)
                            pathLis.append('{{{}}}{}'.format(index, name))
                        else:
                            pathLis.append(i)

            return pathLis, namespaceLis
        else:
            return cls._toNameByNameString(pathString, namespacesep), cls._toNamespaceByNameString(pathString, namespacesep)
    # noinspection PyUnusedLocal
    @classmethod
    def _toPathByPathRebuildDatum(cls, pathDatum, namespaceDatum, pathsep, namespacesep):
        if isinstance(pathDatum, list) or isinstance(pathDatum, tuple):
            return pathsep + pathsep.join(pathDatum).format(*['' if i == namespacesep else i for i in namespaceDatum])
        else:
            return ('' if namespaceDatum == namespacesep else namespaceDatum) + pathDatum
    # noinspection PyUnusedLocal
    @classmethod
    def _toNameStringBySearchDatum(cls, pathDatum, namespaceDatum, pathsep, namespacesep):
        if isinstance(pathDatum, list) or isinstance(pathDatum, tuple):
            return pathDatum[-1].format(*namespaceDatum)
        else:
            return namespaceDatum + pathDatum
    @staticmethod
    def _toOsPathConvert(string):
        return string.replace('\\', '/')
    @classmethod
    def _toOsPath(cls, stringLis):
        return cls._toOsPathConvert(cls.OsFileSep.join(stringLis))
    @staticmethod
    def getOsEnvironValue(osEnvironKey):
        return os.environ.get(osEnvironKey)
    @classmethod
    def getOsDocumentPath(cls):
        return cls.getOsEnvironValue('userprofile').replace('\\', '/') + '/Documents'
    @classmethod
    def listAllMember(cls):
        print dir(cls)
    @classmethod
    def getLxUserOsPath(cls):
        osUserDocument = cls.getOsDocumentPath()
        string = '{0}/{1}'.format(osUserDocument, cls.Folder_Basic)
        return string
    @classmethod
    def getUniqueId(cls, string=None):
        if string:
            return cls._stringToUniqueId(string)
        else:
            return str(uuid.uuid1()).upper()
    @staticmethod
    def _toShowNumber(number):
        showNumber = number
        #
        dv = 1000
        lis = [(dv ** 4, 'T'), (dv ** 3, 'B'), (dv ** 2, 'M'), (dv ** 1, 'K')]
        #
        if number >= dv:
            for i in lis:
                s = int(abs(number)) / i[0]
                if s:
                    showNumber = str(round(float(number) / float(i[0]), 2)) + i[1]
                    break
        else:
            showNumber = number
        #
        return str(showNumber)
    @staticmethod
    def getOsActiveViewTime():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    @classmethod
    def traceMessage(cls, text):
        if cls.LynxiEnable_Trance is True:
            print u'@lynxi <{}>'.format(cls.getOsActiveViewTime())
            print u'    {}'.format(text)
    @classmethod
    def traceResult(cls, text):
        cls.traceMessage(
            u'''@result {}'''.format(text)
        )
    @classmethod
    def traceWaning(cls, text):
        cls.traceMessage(
            u'''@warning {}'''.format(text)
        )
    @classmethod
    def traceError(cls, text):
        cls.traceMessage(
            u'''@error {}'''.format(text)
        )


#
class LxUiConfig(Cfg_Basic):
    LynxiUiName_ProjectMenu = 'lynxiProject'
    LynxiUiName_ToolMenu = 'lynxiTool'
    #
    LynxiUiName_ToolPanel = 'lynxiToolPanel'
    LynxiUiName_ToolKitPanel = 'lynxiToolKitPanel'
    #
    LynxiUiFolder_Filter = '.filter'
    # ff0040
    LynxiUi_ErrorRgba = 255, 0, 63, 255
    # fdff42
    LynxiUi_WarningRgba = 255, 255, 64, 255
    # 40FD7F
    LynxiUi_OnRgba = 63, 255, 127, 255
    # 7f7f7f
    LynxiUi_LineRgba = 127, 127, 127, 255
    # dfdfdf
    LynxiUi_TextRgba = 191, 191, 191, 255
    # dfdfdf
    LynxiUi_TextHoverRgba = 223, 223, 223, 255
    # 00dfdf
    LynxiUi_TextHoverRgba_ = 63, 255, 255, 255
    #
    LynxiEnable_Trance = False
    @classmethod
    def lxOsTagFilterFile(cls, unitName):
        userPath = cls.getLxUserOsPath()
        return '{}/{}/{}'.format(userPath, cls.LynxiUiFolder_Filter, unitName)
    @staticmethod
    def _lxMayaPngIconKeyword(nodeTypeString):
        return 'maya#out_{}'.format(nodeTypeString)
    @staticmethod
    def _lxMayaSvgIconKeyword(nodeTypeString):
        return 'maya@svg#{}'.format(nodeTypeString)
    @classmethod
    def traceMessage(cls, text):
        if cls.LynxiEnable_Trance is True:
            print u'@lynxi <{}>'.format(cls.getOsActiveViewTime())
            print u'    {}'.format(text)


#
class LxDbConfig(Cfg_Basic):
    DbAssetRoot = prsVariant.Util.dbAssetRoot
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
    LxDb_Ext_Version = '.version.json'
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
    #
    LynxiDbAttrKey_UiName = 'nameText'


#
class LxDbUserConfig(Cfg_Basic):
    pass


#
class LxDbProductUnitConfig(LxDbConfig):
    @classmethod
    def dbProductUnitIndexFile(cls, productModule):
        return '{0}/{1}/{2}/{3}'.format(
            cls.DbAssetRoot, prsVariant.Util.dbBasicFolderName, cls.LynxiDatabaseKey_Index,
            cls._stringToUniqueId(productModule)
        )
    @classmethod
    def dbProductUnitSetFile(cls, dbUnitId):
        return '{0}/{1}/{2}/{3}'.format(
            cls.DbAssetRoot, prsVariant.Util.dbBasicFolderName, cls.LynxiDatabaseKey_Set,
            dbUnitId
        )


#
class LxUnitConfig(Cfg_Basic):
    pass


#
class LxAttributeConfig(Cfg_Basic):
    LynxiAttrName_NodeId = 'lxNodeId'
    LynxiAttrName_NodeName = 'lxNodeName'
    #
    LynxiAttrName_NodeColor = 'lxNodeColor'
    LynxiAttrName_NodeColorEnable = 'lxNodeColorEnable'
    LynxiAttrName_NodeNameLabel = 'lxNodeNameLabel'
    #
    LynxiAttrName_ShapeName = 'lxShapeName'
    #
    LynxiAttrName_Artist = 'lxArtist'
    LynxiAttrName_Update = 'lxUpdate'


#
class LxNodeConfig(Cfg_Basic):
    LynxiKeyword_Rename = 'rename'
    #
    LynxiNamePrefix_Asset = 'ast'
    LynxiNamePrefix_Scenery = 'scn'
    LynxiNamePrefix_Scene = 'sc'
    #
    LynxiNamePostfix_Group = 'grp'
    LynxiNamePostfix_Set = 'set'
    LynxiNamePostfix_Object = 'obj'
    #
    LynxiNameLabel_HairOutputCurve = 'hairOutput'
    LynxiNameLabel_HairLocalCurve = 'hairLocal'
    LynxiNameLabel_HairSolver = 'hairSolver'
    #
    LynxiNameLabel_FurYeti = 'furYeti'
    LynxiNameLabel_FurSolver = 'furSolver'
    # Name Format
    LynxiNameFormat_Group = '<nameLabel>_<groupLabel>'
    LynxiNameFormat_SubGroup = '<nameLabel>_<seq>_<groupLabel>'
    #
    LynxiNameFormat_Set = '<nameLabel>_<setLabel>'
    LynxiNameFormat_SubSet = '<nameLabel>_<seq>_<setLabel>'
    #
    LynxiNameFormat_Node = '<nameLabel>_<typeLabel>'
    LynxiNameFormat_SubNode = '<nameLabel>_<typeLabel>_<seq>'
    #
    LynxiNameFormat_NodeGroup = '<nameLabel>_<typeLabel>_<groupLabel>'
    LynxiNameFormat_NodeSubGroup = '<nameLabel>_<typeLabel>_<seq>_<groupLabel>'
    #
    LynxiNameFormat_NodeSet = '<nameLabel>_<typeLabel>_<setLabel>'
    LynxiNameFormat_NodeSubSet = '<nameLabel>_<typeLabel>_<seq>_<setLabel>'
    #
    LynxiKeyword_Node_Visible = 'lxVisible'
    # noinspection PyUnusedLocal
    @classmethod
    def lxGroupName(cls, nameLabel, seq=None):
        # noinspection PyUnusedLocal
        groupLabel = cls.LynxiNamePostfix_Group
        var = str
        if seq is None:
            command = cls.toVariantConvert('var', cls.LynxiNameFormat_Group)
        else:
            command = cls.toVariantConvert('var', cls.LynxiNameFormat_SubGroup)
        exec command
        return var
    # noinspection PyUnusedLocal
    @classmethod
    def lxSetName(cls, nameLabel, seq=None):
        setLabel = cls.LynxiNamePostfix_Set
        var = str
        if seq is None:
            command = cls.toVariantConvert('var', cls.LynxiNameFormat_Set)
        else:
            command = cls.toVariantConvert('var', cls.LynxiNameFormat_SubSet)
        exec command
        return var
    # noinspection PyUnusedLocal
    @classmethod
    def lxNodeName(cls, nameLabel, typeLabel, seq=None):
        objectLabel = cls.LynxiNamePostfix_Object
        var = str
        if seq is None:
            command = cls.toVariantConvert('var', cls.LynxiNameFormat_Node)
        else:
            command = cls.toVariantConvert('var', cls.LynxiNameFormat_SubNode)
        exec command
        return var
    # noinspection PyUnusedLocal
    @classmethod
    def lxNodeGroupName(cls, nameLabel, typeLabel, seq=None):
        groupLabel = cls.LynxiNamePostfix_Group
        var = str
        if seq is None:
            command = cls.toVariantConvert('var', cls.LynxiNameFormat_NodeGroup)
        else:
            command = cls.toVariantConvert('var', cls.LynxiNameFormat_NodeSubGroup)
        exec command
        return var
    # noinspection PyUnusedLocal
    @classmethod
    def lxNodeSetName(cls, nameLabel, typeLabel, seq=None):
        setLabel = cls.LynxiNamePostfix_Set
        var = str
        if seq is None:
            command = cls.toVariantConvert('var', cls.LynxiNameFormat_NodeSet)
        else:
            command = cls.toVariantConvert('var', cls.LynxiNameFormat_NodeSubSet)
        exec command
        return var


#
class LxNodeGraphConfig(Cfg_Basic):
    pass
