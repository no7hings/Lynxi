# coding:utf-8
from LxMaterial import mtlConfigure, mtlObjCore, mtlMethods


class BasicDef(mtlObjCore.Abc_MtlBasicDef):
    VAR_geometry_category_string = mtlConfigure.Utility.DEF_mtl_category_geometry
    VAR_material_category_string = mtlConfigure.Utility.DEF_mtl_category_material

    def __init__(self, *args):
        self._initAbcMtlBasicDef(*args)


class TypeDef(mtlObjCore.Abc_MtlTypeDef):
    def __init__(self):
        pass


class GeometryDef(mtlObjCore.Abc_MtlGeometryDef):
    CLS_mtl_basic_def = BasicDef

    def __init__(self, *args):
        self._initAbcMtlGeometryDef(*args)


class MaterialDef(mtlObjCore.Abc_MtlMaterialDef):
    CLS_mtl_basic_def = BasicDef

    def __init__(self, *args):
        self._initAbcMtlMaterialDef(*args)


class NodeDef(mtlObjCore.Abc_MtlNodeDef):
    CLS_mtl_basic_def = BasicDef

    def __init__(self, *args):
        self._initAbcMtlNodeDef(*args)


class MayaBasicDef(mtlObjCore.Abc_DccMtlBasicDef):
    CLS_mtl_basic_def = BasicDef

    def __init__(self, *args):
        self._initAbcDccMtlBasicDef(*args)


class MayaGeometryDef(mtlObjCore.Abc_DccMtlGeometryDef):
    CLS_mtl_dcc_basic_def = MayaBasicDef
    CLS_mtl_object_def = GeometryDef

    def __init__(self, *args):
        self._initAbcDccMtlGeometryDef(*args)


class MayaMaterialDef(mtlObjCore.Abc_DccMtlMaterialDef):
    CLS_mtl_dcc_basic_def = MayaBasicDef
    CLS_mtl_object_def = MaterialDef

    def __init__(self, *args):
        self._initAbcDccMtlMaterialDef(*args)


class MayaNodeDef(mtlObjCore.Abc_DccMtlNodeDef):
    CLS_mtl_dcc_basic_def = MayaBasicDef
    CLS_mtl_object_def = NodeDef

    def __init__(self, *args):
        self._initAbcDccMtlNodeDef(*args)
