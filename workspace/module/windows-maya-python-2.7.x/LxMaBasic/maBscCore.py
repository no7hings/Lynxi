# coding:utf-8
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMaya, OpenMayaUI


class MaBasic(object):
    Ma_Separator_Node = '|'
    Ma_Separator_Set = '>'
    Ma_Separator_Namespace = ':'
    Ma_Separator_Attribute = '.'
    # Nde_Node Type
    MaNodeType_Transform = 'transform'
    MaNodeType_ShadingEngine = 'shadingEngine'
    MaNodeType_Mesh = 'mesh'
    MaNodeType_AssemblyReference = 'assemblyReference'
    MaNodeType_AssemblyDefinition = 'assemblyDefinition'
    #
    MaNodeType_GroupId = 'groupId'
    MaNodeType_Set = 'set'
    #
    MaNodeType_Light = 'light'
    #
    MaAttrName_Message = 'message'
    MaAttrName_ObjectGroup = 'instObjGroups'
    MaAttrName_SetMember = 'dagSetMembers'
    #
    MaCompName_Mesh_Vertex = 'vtx'
    MaCompName_Mesh_Edge = 'e'
    MaCompName_Mesh_Face = 'f'
    MaDefaultMatrix = [1.0, .0, .0, .0, .0, 1.0, .0, .0, .0, .0, 1.0, .0, .0, .0, .0, 1.0]

    MOD_maya_cmds = cmds
