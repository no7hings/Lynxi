# coding:utf-8
from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet


class Channel(mtlObjCore.Abc_MtlInput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    def __init__(self, *args):
        self._initAbcMtlInput(*args)


# maya: shader engine
class ShadersetInput(mtlObjCore.Abc_MtlInput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    VAR_mtlx_key_element = u'bindinput'
    VAR_mtlx_key_attribute = u'context'

    def __init__(self, *args):
        self._initAbcMtlInput(*args)


class ShaderInput(mtlObjCore.Abc_MtlShaderInput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    VAR_mtlx_key_element = u'bindinput'
    VAR_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcMtlShaderInput(*args)


class NodeInput(mtlObjCore.Abc_MtlNodeInput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    VAR_mtlx_key_element = u'input'
    VAR_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcMtlNodeInput(*args)


class GeometryProperty(mtlObjCore.Abc_MtlGeometryProperty):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    VAR_mtlx_key_element = u'property'
    VAR_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcMtlGeometryProperty(*args)


class GeometryVisibility(mtlObjCore.Abc_MtlGeometryVisibility):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    VAR_mtlx_key_element = u'vistype'
    VAR_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcMtlVisibility(*args)


class GeometryOutput(mtlObjCore.Abc_MtlShaderOutput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    VAR_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcMtlShaderOutput(*args)


class ShaderOutput(mtlObjCore.Abc_MtlShaderOutput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    VAR_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcMtlShaderOutput(*args)


class NodeOutput(mtlObjCore.Abc_MtlNodeOutput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    VAR_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcMtlNodeOutput(*args)


class NodeGraphOutput(mtlObjCore.Abc_MtlNodeGraphOutput):
    CLS_raw_name = _mtlObjRaw.Raw_Name

    VAR_mtlx_key_element = u'output'
    VAR_mtlx_key_attribute = u'output'

    def __init__(self, *args):
        self._initAbcMtlNodeGraphOutput(*args)
