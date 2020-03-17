# coding:utf-8
from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet


# maya: shader engine
class MaterialInput(mtlObjCore.Abc_MtlInput):
    CLS_mtl_port_string = _mtlObjRaw.PortName

    VAR_mtl_file_element_key = u'bindinput'
    VAR_mtl_file_attribute_key = u'context'

    def __init__(self, *args):
        self._initAbcMtlInput(*args)


class NodeInput(mtlObjCore.Abc_MtlNodeInput):
    CLS_mtl_port_string = _mtlObjRaw.PortName

    VAR_mtl_file_element_key = u'input'
    VAR_mtl_file_attribute_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlNodeInput(*args)


class NodeInputChannel(mtlObjCore.Abc_MtlNodeInput):
    CLS_mtl_port_string = _mtlObjRaw.PortName

    VAR_mtl_file_element_key = u'input'
    VAR_mtl_file_attribute_key = u'channels'

    def __init__(self, *args):
        self._initAbcMtlNodeInput(*args)


class ShaderInput(mtlObjCore.Abc_MtlShaderInput):
    CLS_mtl_port_string = _mtlObjRaw.PortName

    VAR_mtl_file_element_key = u'bindinput'
    VAR_mtl_file_attribute_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlShaderInput(*args)


class ShaderInputChannel(mtlObjCore.Abc_MtlShaderInput):
    CLS_mtl_port_string = _mtlObjRaw.PortName

    VAR_mtl_file_element_key = u'bindinput'
    VAR_mtl_file_attribute_key = u'channels'

    def __init__(self, *args):
        self._initAbcMtlShaderInput(*args)


class GeometryProperty(mtlObjCore.Abc_MtlGeometryProperty):
    CLS_mtl_port_string = _mtlObjRaw.PortName

    VAR_mtl_file_element_key = u'property'
    VAR_mtl_file_attribute_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlGeometryProperty(*args)


class GeometryVisibility(mtlObjCore.Abc_MtlGeometryVisibility):
    CLS_mtl_port_string = _mtlObjRaw.GeometryVisibilityName

    VAR_mtl_file_element_key = u'visibility'
    VAR_mtl_file_attribute_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlVisibility(*args)


class MaterialOutput(mtlObjCore.Abc_MtlNodeOutput):
    CLS_mtl_port_string = _mtlObjRaw.PortName

    VAR_mtl_file_element_key = u'output'
    VAR_mtl_file_attribute_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlNodeOutput(*args)


class ShaderOutput(mtlObjCore.Abc_MtlShaderOutput):
    CLS_mtl_port_string = _mtlObjRaw.PortName

    VAR_mtl_file_element_key = u'output'
    VAR_mtl_file_attribute_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlShaderOutput(*args)


class ShaderOutputChannel(mtlObjCore.Abc_MtlOutputChannel):
    CLS_mtl_port_string = _mtlObjRaw.PortName

    VAR_mtl_file_element_key = u'channel'
    VAR_mtl_file_attribute_key = u'channels'

    def __init__(self, *args):
        self._initAbcMtlOutputChannel(*args)


class NodeOutput(mtlObjCore.Abc_MtlNodeOutput):
    CLS_mtl_port_string = _mtlObjRaw.PortName

    VAR_mtl_file_element_key = u'output'
    VAR_mtl_file_attribute_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlNodeOutput(*args)


class NodeOutputChannel(mtlObjCore.Abc_MtlOutputChannel):
    CLS_mtl_port_string = _mtlObjRaw.PortName

    VAR_mtl_file_element_key = u'output'
    VAR_mtl_file_attribute_key = u'channels'

    def __init__(self, *args):
        self._initAbcMtlOutputChannel(*args)


class NodeGraphOutput(mtlObjCore.Abc_MtlNodeGraphOutput):
    CLS_mtl_name = _mtlObjRaw.NameString

    VAR_mtl_file_element_key = u'output'
    VAR_mtl_file_attribute_key = u'output'

    def __init__(self, *args):
        self._initAbcMtlNodeGraphOutput(*args)


class Propertyset(mtlObjCore.Abc_MtlPropertyset):
    CLS_mtl_name = _mtlObjRaw.NameString

    CLS_mtl_port_set = _mtlObjSet.PortSet

    VAR_mtl_file_element_key = u'propertyset'
    VAR_mtl_file_attribute_key = u'propertyset'

    def __init__(self, *args):
        """
        :param args: str(geometry dagpath)
        """
        self._initAbcMtlPropertyset(*args)