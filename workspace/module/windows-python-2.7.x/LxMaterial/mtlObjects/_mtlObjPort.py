# coding:utf-8
from LxMaterial import mtlAbstract

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet


# maya: shader engine
class ShadersetPort(mtlAbstract.Abc_ShaderPort):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    STR_mtlx_key_element = 'bindinput'
    STR_mtlx_key_attribute = 'context'

    def __init__(self, *args):
        self._initAbcPort(*args)


class ShaderPort(mtlAbstract.Abc_ShaderPort):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    STR_mtlx_key_element = 'bindinput'
    STR_mtlx_key_attribute = 'member'

    def __init__(self, *args):
        self._initAbcPort(*args)


class NodePort(mtlAbstract.Abc_NodePort):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    STR_mtlx_key_element = 'input'
    STR_mtlx_key_attribute = 'member'

    def __init__(self, *args):
        self._initAbcPort(*args)


class GeometryPort(mtlAbstract.Abc_NodePort):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    STR_mtlx_key_element = 'property'
    STR_mtlx_key_attribute = 'member'

    def __init__(self, *args):
        self._initAbcPort(*args)


class ShaderOutput(mtlAbstract.Abc_ShaderOutput):
    CLS_raw_name = _mtlObjRaw.Raw_Name

    STR_mtlx_key_attribute = 'context'

    def __init__(self, *args):
        self._initAbcShaderOutput(*args)


class NodeOutput(mtlAbstract.Abc_ShaderOutput):
    CLS_raw_name = _mtlObjRaw.Raw_Name

    STR_mtlx_key_attribute = 'output'

    def __init__(self, *args):
        self._initAbcShaderOutput(*args)
