# coding:utf-8
import cgitb
#
from LxBasic import bscCfg, bscMethods
#
from LxPreset import prsOutputs

#
cgitb.enable(format='text')


#
class LxAttributeConfig(object):
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
class LxNodeConfig(object):
    LynxiKeyword_Rename = 'rename'
    #
    LynxiNamePrefix_Asset = 'ast'
    LynxiNamePrefix_scenery = 'scn'
    LynxiNamePrefix_scene = 'sc'
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
    LynxiNameFormat_NodeStack = '<nameLabel>_<typeLabel>_<setLabel>'
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

            command = bscMethods.Variant.covertTo('var', cls.LynxiNameFormat_Group)
        else:
            command = bscMethods.Variant.covertTo('var', cls.LynxiNameFormat_SubGroup)
        exec command
        return var
    # noinspection PyUnusedLocal
    @classmethod
    def lxSetName(cls, nameLabel, seq=None):
        setLabel = cls.LynxiNamePostfix_Set
        var = str
        if seq is None:
            command = bscMethods.Variant.covertTo('var', cls.LynxiNameFormat_Set)
        else:
            command = bscMethods.Variant.covertTo('var', cls.LynxiNameFormat_SubSet)
        exec command
        return var
    # noinspection PyUnusedLocal
    @classmethod
    def lxNodeName(cls, nameLabel, typeLabel, seq=None):
        objectLabel = cls.LynxiNamePostfix_Object
        var = str
        if seq is None:
            command = bscMethods.Variant.covertTo('var', cls.LynxiNameFormat_Node)
        else:
            command = bscMethods.Variant.covertTo('var', cls.LynxiNameFormat_SubNode)
        exec command
        return var
    # noinspection PyUnusedLocal
    @classmethod
    def lxNodeGroupName(cls, nameLabel, typeLabel, seq=None):
        groupLabel = cls.LynxiNamePostfix_Group
        var = str
        if seq is None:
            command = bscMethods.Variant.covertTo('var', cls.LynxiNameFormat_NodeGroup)
        else:
            command = bscMethods.Variant.covertTo('var', cls.LynxiNameFormat_NodeSubGroup)
        exec command
        return var
    # noinspection PyUnusedLocal
    @classmethod
    def lxNodeStackName(cls, nameLabel, typeLabel, seq=None):
        setLabel = cls.LynxiNamePostfix_Set
        var = str
        if seq is None:
            command = bscMethods.Variant.covertTo('var', cls.LynxiNameFormat_NodeStack)
        else:
            command = bscMethods.Variant.covertTo('var', cls.LynxiNameFormat_NodeSubSet)
        exec command
        return var

