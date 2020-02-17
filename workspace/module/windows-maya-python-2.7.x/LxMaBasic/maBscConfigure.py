# coding:utf-8


class Utility(object):
    DEF_separator_node = '|'
    DEF_separator_set = '>'
    DEF_separator_namespace = ':'
    DEF_separator_attribute = '.'
    # Nde_Node Type
    DEF_type_transform = 'transform'
    DEF_type_shading_engine = 'shadingEngine'
    DEF_type_shading_mesh = 'mesh'
    DEF_type_assembly_reference = 'assemblyReference'
    DEF_type_assembly_definition = 'assemblyDefinition'
    #
    DEF_type_group_id = 'groupId'
    DEF_type_set = 'set'
    #
    DEF_type_light = 'light'
    #
    DEF_attribute_message = 'message'
    DEF_attribute_inst_obj_groups = 'instObjGroups'
    DEF_attribute_dag_set_members = 'dagSetMembers'
    #
    DEF_key_mesh_vertex = 'vtx'
    DEF_key_mesh_edge = 'e'
    DEF_key_mesh_face = 'f'
    DEF_matrix_default = [1.0, .0, .0, .0, .0, 1.0, .0, .0, .0, .0, 1.0, .0, .0, .0, .0, 1.0]

    DEF_camera_default_list = ['persp', 'top', 'front', 'side']

    DEF_shading_engine_default_list = ['initialShadingGroup', 'initialParticleSE', 'defaultLightSet', 'defaultObjectSet']
