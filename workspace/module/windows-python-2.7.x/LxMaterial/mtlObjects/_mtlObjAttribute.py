# coding:utf-8
from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet


class Channel(mtlObjCore.Abc_MtlInput):
    CLS_mtl_port_dagpath = _mtlObjRaw.Raw_PortDagpath

    CLS_mtl_attribute_set = _mtlObjSet.Set_Attribute

    def __init__(self, *args):
        self._initAbcMtlInput(*args)


# maya: shader engine
class ShadersetInput(mtlObjCore.Abc_MtlInput):
    CLS_mtl_port_dagpath = _mtlObjRaw.Raw_PortDagpath

    CLS_mtl_attribute_set = _mtlObjSet.Set_Attribute

    VAR_mtl_file_element_key = u'bindinput'
    VAR_mtl_file_attribute_key = u'context'

    def __init__(self, *args):
        self._initAbcMtlInput(*args)


class ShaderInput(mtlObjCore.Abc_MtlShaderInput):
    CLS_mtl_port_dagpath = _mtlObjRaw.Raw_PortDagpath

    CLS_mtl_attribute_set = _mtlObjSet.Set_Attribute

    VAR_mtl_file_element_key = u'bindinput'
    VAR_mtl_file_attribute_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlShaderInput(*args)


class NodeInput(mtlObjCore.Abc_MtlNodeInput):
    CLS_mtl_port_dagpath = _mtlObjRaw.Raw_PortDagpath

    CLS_mtl_attribute_set = _mtlObjSet.Set_Attribute

    VAR_mtl_file_element_key = u'input'
    VAR_mtl_file_attribute_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlNodeInput(*args)


class GeometryProperty(mtlObjCore.Abc_MtlGeometryProperty):
    CLS_mtl_port_dagpath = _mtlObjRaw.Raw_PortDagpath

    CLS_mtl_attribute_set = _mtlObjSet.Set_Attribute

    VAR_mtl_file_element_key = u'property'
    VAR_mtl_file_attribute_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlGeometryProperty(*args)


class GeometryVisibility(mtlObjCore.Abc_MtlGeometryVisibility):
    CLS_mtl_port_dagpath = _mtlObjRaw.Raw_PortDagpath

    CLS_mtl_attribute_set = _mtlObjSet.Set_Attribute

    VAR_mtl_file_element_key = u'vistype'
    VAR_mtl_file_attribute_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlVisibility(*args)


class GeometryOutput(mtlObjCore.Abc_MtlShaderOutput):
    CLS_mtl_port_dagpath = _mtlObjRaw.Raw_PortDagpath

    CLS_mtl_attribute_set = _mtlObjSet.Set_Attribute

    VAR_mtl_file_attribute_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlShaderOutput(*args)


class ShaderOutput(mtlObjCore.Abc_MtlShaderOutput):
    CLS_mtl_port_dagpath = _mtlObjRaw.Raw_PortDagpath

    CLS_mtl_attribute_set = _mtlObjSet.Set_Attribute

    VAR_mtl_file_attribute_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlShaderOutput(*args)


class NodeOutput(mtlObjCore.Abc_MtlNodeOutput):
    CLS_mtl_port_dagpath = _mtlObjRaw.Raw_PortDagpath

    CLS_mtl_attribute_set = _mtlObjSet.Set_Attribute

    VAR_mtl_file_attribute_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlNodeOutput(*args)


class NodeGraphOutput(mtlObjCore.Abc_MtlNodeGraphOutput):
    CLS_mtl_name = _mtlObjRaw.Raw_Name

    VAR_mtl_file_element_key = u'output'
    VAR_mtl_file_attribute_key = u'output'

    def __init__(self, *args):
        self._initAbcMtlNodeGraphOutput(*args)
