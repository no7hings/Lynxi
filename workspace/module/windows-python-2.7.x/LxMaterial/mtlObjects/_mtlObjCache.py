# coding:utf-8
from LxMaterial import mtlConfigure, mtlObjCore


class MtlDefCache(mtlObjCore.Abc_MtlDefCache):
    VAR_mtl_node_defs_file = mtlConfigure.Utility.DEF_mtl_arnold_node_defs_file
    VAR_mtl_geometry_def_file = mtlConfigure.Utility.DEF_mtl_arnold_geometry_def_file
    VAR_mtl_material_def_file = mtlConfigure.Utility.DEF_mtl_arnold_material_def_file
    VAR_mtl_output_defs_file = mtlConfigure.Utility.DEF_mtl_arnold_output_defs_file
    VAR_mtl_port_child_defs_file = mtlConfigure.Utility.DEF_mtl_arnold_port_child_defs_file

    def __init__(self, *args):
        self._initAbcMtlDefCache(*args)


OBJ_mtl_def_cache = MtlDefCache()


class MyaMtlDefCache(mtlObjCore.Abc_DccMtlDefCache):
    VAR_mtl_dcc_node_defs_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_node_defs_file
    VAR_mtl_dcc_geometry_def_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_geometry_def_file
    VAR_mtl_dcc_material_def_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_material_def_file
    VAR_mtl_dcc_output_defs_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_output_defs_file
    VAR_mtl_dcc_port_child_defs_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_port_child_defs_file

    OBJ_mtl_def_cache = OBJ_mtl_def_cache

    def __init__(self, *args):
        self._initAbcDccMtlDefCache(*args)


class MtlObjCache(mtlObjCore.Abc_MtlObjCache):
    def __init__(self):
        self._initAbcMtlObjCache()


OBJ_mtl_obj_cache = MtlObjCache()

