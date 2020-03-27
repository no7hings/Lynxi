# coding:utf-8
from LxMaterial import mtlConfigure, mtlObjDef


class MtlRawTranslator(mtlObjDef.Abc_MtlRawTranslator):
    def __init__(self, objectRaw, outputRaw, portChildRaw):
        self._initAbcMtlRawTranslator(objectRaw, outputRaw, portChildRaw)


class MtlPortDef(mtlObjDef.Abc_MtlPortDef):
    def __init__(self, portnameString, portRaw):
        self._initAbcMtlPortDef(portnameString, portRaw)


class MtlObjectDef(mtlObjDef.Abc_MtlObjectDef):
    CLS_mtl_port_def = MtlPortDef

    CLS_mtl_raw_translator = MtlRawTranslator

    def __init__(self, categoryString, objectRaw, outputRaw, childRaw):
        self._initAbcMtlObjectDef(categoryString, objectRaw, outputRaw, childRaw)


class MtlQueryCache(mtlObjDef.Abc_MtlQueryCache):
    VAR_mtl_node_defs_file = mtlConfigure.Utility.DEF_mtl_arnold_node_defs_file
    VAR_mtl_geometry_def_file = mtlConfigure.Utility.DEF_mtl_arnold_geometry_def_file
    VAR_mtl_material_def_file = mtlConfigure.Utility.DEF_mtl_arnold_material_def_file
    VAR_mtl_output_defs_file = mtlConfigure.Utility.DEF_mtl_arnold_output_defs_file
    VAR_mtl_port_child_defs_file = mtlConfigure.Utility.DEF_mtl_arnold_port_child_defs_file

    CLS_mtl_object_def = MtlObjectDef

    def __init__(self, *args):
        self._initAbcMtlQueryCache(*args)


OBJ_mtl_query_cache = MtlQueryCache()


class MtlDccRawTranslator(mtlObjDef.Abc_MtlDccRawTranslator):
    OBJ_mtl_query_cache = OBJ_mtl_query_cache

    VAR_mtl_def_key_list = [
        mtlConfigure.Utility.DEF_mtl_key_mtl_port,
        mtlConfigure.Utility.DEF_mtl_key_mtl_portdata,
        mtlConfigure.Utility.DEF_mtl_key_custom_node,
        mtlConfigure.Utility.DEF_mtl_key_create_expression,
        mtlConfigure.Utility.DEF_mtl_key_after_expression
    ]

    def __init__(self, dccObjectRaw, dccOutputRaw, dccPortChildRaw):
        self._initMtlDccRawTranslator(dccObjectRaw, dccOutputRaw, dccPortChildRaw)


class MtlDccPortDef(mtlObjDef.Abc_MtlDccPortDef):
    def __init__(self, dccPortString, portRaw):
        self._initAbcMtlDccPortDef(dccPortString, portRaw)


class MtlDccObjectDef(mtlObjDef.Abc_MtlDccObjectDef):
    CLS_mtl_dcc_port_def = MtlDccPortDef

    CLS_mtl_dcc_raw_translator = MtlDccRawTranslator

    VAR_mtl_def_key_list = [
        mtlConfigure.Utility.DEF_mtl_key_mtl_port,
        mtlConfigure.Utility.DEF_mtl_key_custom_node,
        mtlConfigure.Utility.DEF_mtl_key_create_expression,
        mtlConfigure.Utility.DEF_mtl_key_after_expression
    ]

    def __init__(self, dccCategoryString, objectRaw, outputRaw, childRaw):
        self._initAbcMtlDccObjectDef(dccCategoryString, objectRaw, outputRaw, childRaw)


class MyaMtlQueryCache(mtlObjDef.Abc_MtlDccQueryCache):
    VAR_mtl_dcc_node_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_node_defs_file
    VAR_mtl_dcc_geometry_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_geometry_def_file
    VAR_mtl_dcc_material_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_material_def_file
    VAR_mtl_dcc_output_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_output_defs_file
    VAR_mtl_dcc_port_child_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_port_child_defs_file

    VAR_mtl_dcc_custom_category_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_custom_category_file
    VAR_mtl_dcc_custom_node_file = mtlConfigure.Utility.DEF_mtl_maya_arnold_custom_node_file

    CLS_mtl_dcc_object_def = MtlDccObjectDef

    OBJ_mtl_query_cache = OBJ_mtl_query_cache

    def __init__(self, *args):
        self._initAbcMtlDccQueryCache(*args)


class MtlObjCache(mtlObjDef.Abc_MtlObjCache):
    def __init__(self):
        self._initAbcMtlObjCache()


OBJ_mtl_obj_cache = MtlObjCache()


class MtlTrsObjectCache(mtlObjDef.Abc_MtlObjCache):
    def __init__(self):
        self._initAbcMtlObjCache()


OBJ_mtl_trs_obj_cache = MtlTrsObjectCache()

