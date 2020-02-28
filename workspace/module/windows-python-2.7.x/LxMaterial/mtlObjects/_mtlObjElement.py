# coding:utf-8
from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet, _mtlObjAttribute, _mtlObjObject, _mtlObjDefinition


class Reference(mtlObjCore.Abc_MtlFileReference):
    CLS_mtl_file = _mtlObjRaw.Raw_Reference

    VAR_mtl_file_element_key = u'xi:include'

    def __init__(self, *args):
        self._initAbcMtlFileReference(*args)


class Look(mtlObjCore.Abc_MtlLook):
    CLS_mtl_name = _mtlObjRaw.Raw_Name
    CLS_set_assign = _mtlObjSet.Set_Assign

    CLS_set_assign_shaderset = _mtlObjSet.Set_Assign
    ClS_set_assign_propertyset = _mtlObjSet.Set_Assign
    CLS_mtl_visibility_assign = _mtlObjSet.Set_Visibility

    VAR_mtl_file_element_key = u'look'
    VAR_mtl_file_attribute_key = u'look'

    def __init__(self, *args):
        self._initAbcMtlLook(*args)


class Material(mtlObjCore.Abc_MtlMaterial):
    CLS_mtl_node_dagpath = _mtlObjRaw.Raw_MaterialDagpath

    CLS_mtl_attribute_set = _mtlObjSet.Set_Attribute

    CLS_mtl_input = _mtlObjAttribute.ShadersetInput

    CLS_mtl_material_def = _mtlObjDefinition.MtlMaterialDef

    VAR_mtl_value_class_dict = _mtlObjObject.DEF_CLS_VALUE

    VAR_mtl_file_element_key = u'material'
    VAR_mtl_file_attribute_key = u'material'

    def __init__(self, *args):
        """
        * 1.maya: shading engine name
        :param args: str(shader set name)
        """
        self._initAbcMtlMaterial(*args)


class GeometryPortset(mtlObjCore.Abc_MtlPropertyset):
    CLS_mtl_name = _mtlObjRaw.Raw_Name

    CLS_mtl_attribute_set = _mtlObjSet.Set_Attribute
    
    VAR_mtl_file_element_key = u'propertyset'
    VAR_mtl_file_attribute_key = u'propertyset'

    def __init__(self, *args):
        """
        :param args: str(geometry dagpath)
        """
        self._initAbcMtlPropertyset(*args)


class NodeGraph(mtlObjCore.Abc_MtlNodeGraph):
    CLS_mtl_name = _mtlObjRaw.Raw_Name

    CLS_mtl_node_set = _mtlObjSet.Set_Dag
    CLS_mtl_output_set = _mtlObjSet.Set_Attribute

    CLS_mtl_node = _mtlObjObject.Node
    CLS_mtl_output = _mtlObjAttribute.NodeGraphOutput

    VAR_mtl_file_element_key = u'nodegraph'
    VAR_mtl_file_attribute_key = u'nodegraph'

    def __init__(self, *args):
        self._initAbcMtlNodeGraph(*args)


class Collection(mtlObjCore.Abc_MtlGeometryCollection):
    CLS_mtl_name = _mtlObjRaw.Raw_Name

    CLS_set_geometry = _mtlObjSet.Set_Geometry
    CLS_set_collection = _mtlObjSet.Set_Collection

    DEF_geometry_separator = u','

    VAR_mtl_file_element_key = u'collection'
    VAR_mtl_file_attribute_key = u'collection'

    def __init__(self, *args):
        self._initAbcMtlGeometryCollection(*args)
