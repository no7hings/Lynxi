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
from LxCore.preset import appVariant
#
cgitb.enable(format='text')


#
def orderedDict(*args):
    return collections.OrderedDict(*args)


#
class LxConfigBasic(object):
    Lynxi_Folder_Basic = '.lynxi'
    LynxiOsFolder_Database = '.database'
    LynxiOsFolder_History = '.lxHistory'
    LynxiOsExt_Version = '.lxVersion'
    #
    LynxiOsExt_Info = '.lxInfo'
    LynxiOsExt_Log = '.lxLog'
    LynxiOsExt_Record = '.lxRecord'
    #
    LynxiOsPath_LocalTemporary = 'd:/{}.temporary'.format(Lynxi_Folder_Basic)
    LynxiOsPath_Log_Local = 'd:/{}.log'.format(Lynxi_Folder_Basic)
    #
    LynxiOsPath_Log_Server = 'e:/{}.log'.format(Lynxi_Folder_Basic)
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
    Lynxi_Key_Environ_Path_Basic = 'LYNXI_PATH'
    Lynxi_Key_Environ_Path_Develop = 'LYNXI_DEVELOP_PATH'
    Lynxi_Key_Environ_Path_Product = 'LYNXI_PRODUCT_PATH'
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
    def _toStringPrettify(cls, string):
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
    def _toVariantConvert(varName, string):
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
        string = '{0}/{1}'.format(osUserDocument, cls.Lynxi_Folder_Basic)
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
    def _toShowFileSize(number):
        showNumber = number
        #
        dv = 1024
        lis = [(dv ** 4, 'T'), (dv ** 3, 'G'), (dv ** 2, 'M'), (dv ** 1, 'K')]
        #
        for i in lis:
            s = abs(number) / i[0]
            if s:
                showNumber = str(round(float(number) / float(i[0]), 2)) + i[1]
                break
        #
        return str(showNumber)
    @staticmethod
    def getOsActiveViewTime():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    @classmethod
    def traceMessage(cls, text):
        if cls.LynxiEnable_Trance is True:
            print u'# Lynxi {}'.format(cls.getOsActiveViewTime())
            print u'    {}'.format(text)
    @classmethod
    def traceResult(cls, text):
        cls.traceMessage(
            u'''# Result {}'''.format(text)
        )
    @classmethod
    def traceWaning(cls, text):
        cls.traceMessage(
            u'''# Warning {}'''.format(text)
        )
    @classmethod
    def traceError(cls, text):
        cls.traceMessage(
            u'''# Error {}'''.format(text)
        )


#
class LxUiConfig(LxConfigBasic):
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
            print u'# Lynxi {}'.format(cls.getOsActiveViewTime())
            print u'    {}'.format(text)


#
class LxDbConfig(LxConfigBasic):
    DbAssetRoot = appVariant.dbAssetRoot
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
class LxDbUserConfig(LxConfigBasic):
    pass


#
class LxProductConfig(LxConfigBasic):
    # Module
    LynxiProduct_Module_Asset = 'asset'
    LynxiProduct_Module_Prefix_Asset = 'ast'
    LynxiProduct_Module_Scenery = 'scenery'
    LynxiProduct_Module_Prefix_Scenery = 'scn'
    LynxiProduct_Module_Scene = 'scene'
    LynxiProduct_Module_Prefix_Scene = 'sc'
    #
    LynxiProduct_ModuleLis = [
        LynxiProduct_Module_Asset,
        LynxiProduct_Module_Scenery,
        LynxiProduct_Module_Scene
    ]
    #
    LynxiProduct_Module_PrefixDic = {
        LynxiProduct_Module_Asset: LynxiProduct_Module_Prefix_Asset,
        LynxiProduct_Module_Scenery: LynxiProduct_Module_Prefix_Scenery,
        LynxiProduct_Module_Scene: LynxiProduct_Module_Prefix_Scene
    }
    LynxiProduct_Module_UiDic = collections.OrderedDict(
        [
            (LynxiProduct_Module_Asset, ('Asset', u'资产')),
            (LynxiProduct_Module_Scenery, ('Scenery', u'场景')),
            (LynxiProduct_Module_Scene, ('Scene', u'镜头'))
        ]
    )
    # Asset
    LynxiProduct_Asset_Class_Character = 'character'
    LynxiProduct_Asset_Class_Prop = 'prop'
    #
    LynxiProduct_Asset_Class_Lis = [
        LynxiProduct_Asset_Class_Character,
        LynxiProduct_Asset_Class_Prop
    ]
    LynxiProduct_Asset_Class_UiSetDic = collections.OrderedDict(
        [
            (LynxiProduct_Asset_Class_Character, ('Character', u'角色')),
            (LynxiProduct_Asset_Class_Prop, ('Prop', u'道具'))
        ]
    )
    LynxiProduct_Asset_Class_UiDatumDic = collections.OrderedDict(
        [
            ('ast0', (LynxiProduct_Asset_Class_Character, u'角色')),
            ('ast1', (LynxiProduct_Asset_Class_Prop, u'道具'))
        ]
    )
    # Scenery
    LynxiProduct_Scenery_Class_Scenery = 'scenery'
    LynxiProduct_Scenery_Class_Group = 'group'
    LynxiProduct_Scenery_Class_Assembly = 'assembly'
    #
    LynxiProduct_Scenery_Class_Lis = [
        LynxiProduct_Scenery_Class_Scenery,
        LynxiProduct_Scenery_Class_Group,
        LynxiProduct_Scenery_Class_Assembly
    ]
    LynxiProduct_Scenery_Class_UiSetDic = collections.OrderedDict(
        [
            (LynxiProduct_Scenery_Class_Scenery, ('Scenery', u'场景')),
            (LynxiProduct_Scenery_Class_Group, ('Group', u'组合')),
            (LynxiProduct_Scenery_Class_Assembly, ('Assembly', u'组装'))
        ]
    )
    LynxiProduct_Scenery_Class_UiDatumDic = collections.OrderedDict(
        [
            ('scn0', (LynxiProduct_Scenery_Class_Scenery, u'场景')),
            ('scn1', (LynxiProduct_Scenery_Class_Group, u'组合')),
            ('scn2', (LynxiProduct_Scenery_Class_Assembly, u'组装'))
        ]
    )
    # Scene
    LynxiProduct_Scene_Class_Scene = 'scene'
    LynxiProduct_Scene_Class_Act = 'act'
    #
    LynxiProduct_Scene_Class_Lis = [
        LynxiProduct_Scene_Class_Scene,
        LynxiProduct_Scene_Class_Act
    ]
    LynxiProduct_Scene_Class_UiSetDic = collections.OrderedDict(
        [
            (LynxiProduct_Scene_Class_Scene, ('Scene', u'镜头')),
            (LynxiProduct_Scene_Class_Act, ('Act', u'动作'))
        ]
    )
    LynxiProduct_Scene_Class_UiDatumDic = collections.OrderedDict(
        [
            ('sc0', (LynxiProduct_Scene_Class_Scene, u'镜头')),
            ('sc1', (LynxiProduct_Scene_Class_Act, u'动作'))
        ]
    )
    # Priority
    LynxiUnit_Priority_Major = 'major'
    LynxiUnit_Priority_Minor = 'minor'
    LynxiUnit_Priority_Util = 'util'
    #
    LynxiUnit_Priority_Lis = [
        LynxiUnit_Priority_Major,
        LynxiUnit_Priority_Minor,
        LynxiUnit_Priority_Util
    ]
    LynxiUnit_Priority_UiSetDic = collections.OrderedDict(
        [
            (LynxiUnit_Priority_Major, ('Major', u'主要')),
            (LynxiUnit_Priority_Minor, ('Minor', u'次要')),
            (LynxiUnit_Priority_Util, ('Util', u'龙套'))
        ]
    )
    LynxiUnit_Priority_UiDatumDic = collections.OrderedDict(
        [
            ('prt0', (LynxiUnit_Priority_Major, u'主要')),
            ('prt1', (LynxiUnit_Priority_Minor, u'次要')),
            ('prt2', (LynxiUnit_Priority_Util, u'龙套'))
        ]
    )
    # Asset
    LynxiProduct_Asset_Link_Model = 'model'
    LynxiProduct_Asset_Link_Rig = 'rig'
    LynxiProduct_Asset_Link_Cfx = 'cfx'
    LynxiProduct_Asset_Link_Solver = 'solver'
    LynxiProduct_Asset_Link_Light = 'light'
    LynxiProduct_Asset_Link_Assembly = 'assembly'
    #
    LynxiProduct_Asset_Link_Lis = [
        LynxiProduct_Asset_Link_Model,
        LynxiProduct_Asset_Link_Rig,
        LynxiProduct_Asset_Link_Cfx,
        LynxiProduct_Asset_Link_Solver,
        LynxiProduct_Asset_Link_Light,
        LynxiProduct_Asset_Link_Assembly
    ]
    LynxiProduct_Asset_Link_UiSetDic = collections.OrderedDict(
        [
            (LynxiProduct_Asset_Link_Model, ('Model', u'模型')),
            (LynxiProduct_Asset_Link_Rig, ('Rig', u'绑定')),
            (LynxiProduct_Asset_Link_Cfx, ('Groom', u'毛发塑形')),
            (LynxiProduct_Asset_Link_Solver, ('Solver Rig', u'毛发绑定')),
            (LynxiProduct_Asset_Link_Light, ('Light', u'灯光')),
            (LynxiProduct_Asset_Link_Assembly, ('Assembly', u'组装'))
        ]
    )
    # Scenery
    LynxiProduct_Scenery_Link_Scenery = 'scenery'
    LynxiProduct_Scenery_Link_layout = 'layout'
    LynxiProduct_Scenery_Link_Animation = 'animation'
    LynxiProduct_Scenery_Link_Simulation = 'simulation'
    LynxiProduct_Scenery_Link_Solver = 'solver'
    LynxiProduct_Scenery_Link_Light = 'light'
    #
    LynxiProduct_Scenery_Link_Lis = [
        LynxiProduct_Scenery_Link_Scenery,
        LynxiProduct_Scenery_Link_layout,
        LynxiProduct_Scenery_Link_Animation,
        LynxiProduct_Scenery_Link_Simulation,
        LynxiProduct_Scenery_Link_Solver,
        LynxiProduct_Scenery_Link_Light
    ]
    LynxiProduct_Scenery_Link_UiSetDic = collections.OrderedDict(
        [
            (LynxiProduct_Scenery_Link_Scenery, ('Scenery', u'场景布景')),
            (LynxiProduct_Scenery_Link_layout, ('Layout', u'场景预览')),
            (LynxiProduct_Scenery_Link_Animation, ('Animation', u'场景动画')),
            (LynxiProduct_Scenery_Link_Simulation, ('Simulation', u'场景解算')),
            (LynxiProduct_Scenery_Link_Solver, ('Solver', u'场景模拟')),
            (LynxiProduct_Scenery_Link_Light, ('Light', u'场景灯光'))
        ]
    )
    # Scene
    LynxiProduct_Scene_Link_layout = 'layout'
    LynxiProduct_Scene_Link_Animation = 'animation'
    LynxiProduct_Scene_Link_Simulation = 'simulation'
    LynxiProduct_Scene_Link_Solver = 'solver'
    LynxiProduct_Scene_Link_Light = 'light'
    #
    LynxiProduct_Scene_Link_Lis = [
        LynxiProduct_Scene_Link_layout,
        LynxiProduct_Scene_Link_Animation,
        LynxiProduct_Scene_Link_Simulation,
        LynxiProduct_Scene_Link_Solver,
        LynxiProduct_Scene_Link_Light
    ]
    LynxiProduct_Scene_Link_UiSetDic = collections.OrderedDict(
        [
            (LynxiProduct_Scene_Link_layout, ('Layout', u'镜头预览')),
            (LynxiProduct_Scene_Link_Animation, ('Animation', u'镜头动画')),
            (LynxiProduct_Scene_Link_Simulation, ('Simulation', u'镜头解算')),
            (LynxiProduct_Scene_Link_Solver, ('Solver', u'镜头模拟')),
            (LynxiProduct_Scene_Link_Light, ('Light', u'镜头灯光'))
        ]
    )
    #
    LynxiProduct_Module_Class_Dic = {
        LynxiProduct_Module_Asset: LynxiProduct_Asset_Class_Lis,
        LynxiProduct_Module_Scenery: LynxiProduct_Scenery_Class_Lis,
        LynxiProduct_Module_Scene: LynxiProduct_Scene_Class_Lis
    }
    #
    LynxiUnit_Label_Root = 'unitRoot'
    #
    LynxiUnit_AttrName_ID = 'index'
    LynxiUnit_AttrName_Class = 'classification'
    LynxiUnit_AttrName_Name = 'name'
    LynxiUnit_AttrName_Variant = 'variant'
    LynxiUnit_AttrName_Stage = 'stage'
    #
    LynxiProduct_Unit_AttrNameLis = [
        LynxiUnit_AttrName_ID,
        LynxiUnit_AttrName_Class,
        LynxiUnit_AttrName_Name,
        LynxiUnit_AttrName_Variant,
        LynxiUnit_AttrName_Stage
    ]
    #
    LynxiProduct_Unit_Key_Project = 'project'
    LynxiProduct_Unit_Key_Class = 'classify'
    LynxiProduct_Unit_Key_Priority = 'priority'
    LynxiProduct_Unit_Key_Name = 'name'
    LynxiProduct_Unit_Key_Variant = 'variant'
    #
    LynxiProduct_Stage_Pending = 'pending'
    LynxiProduct_Stage_Wip = 'wip'
    LynxiProduct_Stage_Delivery = 'delivery'
    LynxiProduct_Stage_Refine = 'refine'
    LynxiProduct_Stage_Validated = 'validated'
    LynxiProduct_Stage_UiSetDic = {
        LynxiProduct_Stage_Pending: ('Pending', u'等待'),
        LynxiProduct_Stage_Wip: ('WIP', u'制作'),
        LynxiProduct_Stage_Delivery: ('Delivery', u'提交'),
        LynxiProduct_Stage_Refine: ('Refine', u'返修'),
        LynxiProduct_Stage_Validated: ('Validated', u'通过')
    }

    @staticmethod
    def _toProductUnitName(number):
        return 'ID{}'.format(str(number).zfill(6))
    @classmethod
    def isLxAssetClass(cls, unitClass):
        return unitClass in cls.LynxiProduct_Asset_Class_Lis
    @classmethod
    def isLxSceneryClass(cls, unitClass):
        return unitClass in cls.LynxiProduct_Scenery_Class_Lis
    @classmethod
    def isLxSceneClass(cls, unitClass):
        return unitClass in cls.LynxiProduct_Scene_Class_Lis
    @classmethod
    def getDbProductModule(cls, unitClass):
        if cls.isLxAssetClass(unitClass):
            return cls.LynxiProduct_Module_Asset
        elif cls.isLxSceneryClass(unitClass):
            return cls.LynxiProduct_Module_Scenery
        elif cls.isLxSceneClass(unitClass):
            return cls.LynxiProduct_Module_Scene
    @classmethod
    def getLxClassKeyLisByProductModule(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Asset_Class_Lis
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Scenery_Class_Lis
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Scene_Class_Lis
    @classmethod
    def _lxProductClassUiSetDic(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Asset_Class_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Scenery_Class_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Scene_Class_UiSetDic
    @classmethod
    def _lxProductClassUiDatumDic(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Asset_Class_UiDatumDic
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Scenery_Class_UiDatumDic
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Scene_Class_UiDatumDic
    @classmethod
    def _lxProductPriorityUiDatum(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiUnit_Priority_UiDatumDic
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiUnit_Priority_UiDatumDic
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiUnit_Priority_UiDatumDic
    @classmethod
    def _lxProductLinkLis(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Asset_Link_Lis
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Scenery_Link_Lis
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Scene_Link_Lis
    @classmethod
    def _lxProductLinkUiSetDic(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Asset_Link_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Scenery_Link_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Scene_Link_UiSetDic
    @classmethod
    def _lxProductStageUiSetDic(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiProduct_Stage_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiProduct_Stage_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiProduct_Stage_UiSetDic
    @classmethod
    def getLxPriorityKeyLisByProductModule(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiUnit_Priority_Lis
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiUnit_Priority_Lis
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiUnit_Priority_Lis
    @classmethod
    def _lxProductPriorityUiSetDic(cls, productModule):
        if productModule == cls.LynxiProduct_Module_Asset:
            return cls.LynxiUnit_Priority_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scenery:
            return cls.LynxiUnit_Priority_UiSetDic
        elif productModule == cls.LynxiProduct_Module_Scene:
            return cls.LynxiUnit_Priority_UiSetDic
    @classmethod
    def lxDbProductUnitDefaultSetConfig(cls, projectName, productModule, number):
        def addLinkDatum():
            linkUiDic = cls._lxProductLinkUiSetDic(productModule)
            if linkUiDic:
                for k, v in linkUiDic.items():
                    lis.append(
                        [(k, u'{} [ {} ]'.format(v[1], v[0])), False]
                    )
        #
        lis = [
            [(cls.LynxiProduct_Unit_Key_Project, u'项目 [ Project(s) ]'), (projectName,)],
            [(cls.LynxiProduct_Unit_Key_Name, u'名字 [ Name ]'), cls._toProductUnitName(number)],
            [(cls.LynxiProduct_Unit_Key_Variant, u'变体 [ Variant(s) ]'), (appVariant.astDefaultVariant,)],
            [(cls.LynxiProduct_Unit_Key_Class, u'类型 [ Classify ]'), cls._lxProductClassUiDatumDic(productModule)],
            [(cls.LynxiProduct_Unit_Key_Priority, u'优先级 [ Priority ]'), cls._lxProductPriorityUiDatum(productModule)]
        ]
        addLinkDatum()
        return lis
    @classmethod
    def lxProductUnitViewInfoSet(cls, productModule, unitClass, unitViewName, extendString=None):
        unitViewClass = cls._lxProductClassUiSetDic(productModule)[unitClass]
        if extendString is None:
            string = u'{} {}'.format(
                unitViewClass,
                unitViewName
            )
        else:
            string = u'{} {} ( {} )'.format(
                unitViewClass,
                unitViewName,
                extendString
            )
        return string


#
class LxDbProductUnitConfig(LxDbConfig, LxProductConfig):
    @classmethod
    def dbProductUnitIndexFile(cls, productModule):
        return '{0}/{1}/{2}/{3}'.format(
            cls.DbAssetRoot, appVariant.dbBasicFolderName, cls.LynxiDatabaseKey_Index,
            cls._stringToUniqueId(productModule)
        )
    @classmethod
    def dbProductUnitSetFile(cls, dbUnitId):
        return '{0}/{1}/{2}/{3}'.format(
            cls.DbAssetRoot, appVariant.dbBasicFolderName, cls.LynxiDatabaseKey_Set,
            dbUnitId
        )


#
class LxProductPresetConfig(LxProductConfig):
    pass


#
class LxUnitConfig(LxConfigBasic):
    pass


#
class LxAttributeConfig(LxConfigBasic):
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
class LxNodeConfig(LxConfigBasic):
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
            command = cls._toVariantConvert('var', cls.LynxiNameFormat_Group)
        else:
            command = cls._toVariantConvert('var', cls.LynxiNameFormat_SubGroup)
        exec command
        return var
    # noinspection PyUnusedLocal
    @classmethod
    def lxSetName(cls, nameLabel, seq=None):
        setLabel = cls.LynxiNamePostfix_Set
        var = str
        if seq is None:
            command = cls._toVariantConvert('var', cls.LynxiNameFormat_Set)
        else:
            command = cls._toVariantConvert('var', cls.LynxiNameFormat_SubSet)
        exec command
        return var
    # noinspection PyUnusedLocal
    @classmethod
    def lxNodeName(cls, nameLabel, typeLabel, seq=None):
        objectLabel = cls.LynxiNamePostfix_Object
        var = str
        if seq is None:
            command = cls._toVariantConvert('var', cls.LynxiNameFormat_Node)
        else:
            command = cls._toVariantConvert('var', cls.LynxiNameFormat_SubNode)
        exec command
        return var
    # noinspection PyUnusedLocal
    @classmethod
    def lxNodeGroupName(cls, nameLabel, typeLabel, seq=None):
        groupLabel = cls.LynxiNamePostfix_Group
        var = str
        if seq is None:
            command = cls._toVariantConvert('var', cls.LynxiNameFormat_NodeGroup)
        else:
            command = cls._toVariantConvert('var', cls.LynxiNameFormat_NodeSubGroup)
        exec command
        return var
    # noinspection PyUnusedLocal
    @classmethod
    def lxNodeSetName(cls, nameLabel, typeLabel, seq=None):
        setLabel = cls.LynxiNamePostfix_Set
        var = str
        if seq is None:
            command = cls._toVariantConvert('var', cls.LynxiNameFormat_NodeSet)
        else:
            command = cls._toVariantConvert('var', cls.LynxiNameFormat_NodeSubSet)
        exec command
        return var


#
class LxNodeGraphConfig(LxConfigBasic):
    pass
