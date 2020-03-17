# coding:utf-8
from LxMaterial import mtlConfigure, mtlObjDefCore


class MtlPortDef(mtlObjDefCore.Abc_MtlPortDef):
    def __init__(self, portnameString, portRaw):
        self._initAbcMtlPortDef(portnameString, portRaw)


class MtlObjectDef(mtlObjDefCore.Abc_MtlObjectDef):
    CLS_mtl_port_def = MtlPortDef

    def __init__(self, categoryString, objectRaw, outputRaw, childRaw):
        self._initAbcMtlObjectDef(categoryString, objectRaw, outputRaw, childRaw)


class MtlQueryCache(mtlObjDefCore.Abc_MtlQueryCache):
    VAR_mtl_node_defs_file = mtlConfigure.Utility.DEF_mtl_arnold_node_defs_file
    VAR_mtl_geometry_def_file = mtlConfigure.Utility.DEF_mtl_arnold_geometry_def_file
    VAR_mtl_material_def_file = mtlConfigure.Utility.DEF_mtl_arnold_material_def_file
    VAR_mtl_output_defs_file = mtlConfigure.Utility.DEF_mtl_arnold_output_defs_file
    VAR_mtl_port_child_defs_file = mtlConfigure.Utility.DEF_mtl_arnold_port_child_defs_file

    CLS_mtl_object_def = MtlObjectDef

    def __init__(self, *args):
        self._initAbcMtlQueryCache(*args)


OBJ_mtl_query_cache = MtlQueryCache()


class MtlDccPortDef(mtlObjDefCore.Abc_MtlDccPortDef):
    def __init__(self, dccPortString, portRaw):
        self._initAbcMtlDccPortDef(dccPortString, portRaw)


class MtlDccObjectDef(mtlObjDefCore.Abc_MtlDccObjectDef):
    CLS_mtl_dcc_port_def = MtlDccPortDef

    OBJ_mtl_query_cache = OBJ_mtl_query_cache

    def __init__(self, dccCategoryString, objectRaw, outputRaw, childRaw):
        self._initAbcMtlDccObjectDef(dccCategoryString, objectRaw, outputRaw, childRaw)


class MyaMtlQueryCache(mtlObjDefCore.Abc_MtlDccQueryCache):
    VAR_mtl_dcc_node_defs_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_node_defs_file
    VAR_mtl_dcc_geometry_def_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_geometry_def_file
    VAR_mtl_dcc_material_def_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_material_def_file
    VAR_mtl_dcc_custom_def_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_custom_def_file
    VAR_mtl_dcc_output_defs_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_output_defs_file
    VAR_mtl_dcc_port_child_defs_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_port_child_defs_file

    CLS_mtl_dcc_object_def = MtlDccObjectDef

    OBJ_mtl_query_cache = OBJ_mtl_query_cache

    def __init__(self, *args):
        self._initAbcMtlDccQueryCache(*args)


class MtlObjCache(mtlObjDefCore.Abc_MtlObjCache):
    def __init__(self):
        self._initAbcMtlObjCache()


OBJ_mtl_obj_cache = MtlObjCache()

