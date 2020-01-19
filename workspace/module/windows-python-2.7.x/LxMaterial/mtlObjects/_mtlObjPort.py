# coding:utf-8
from LxMaterial import mtlAbstract

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet


class Channel(mtlAbstract.Abc_Input):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    def __init__(self, *args):
        self._initAbcInput(*args)


# maya: shader engine
class ShadersetInput(mtlAbstract.Abc_Input):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    STR_mtlx_key_element = u'bindinput'
    STR_mtlx_key_attribute = u'context'

    def __init__(self, *args):
        self._initAbcInput(*args)


class ShaderInput(mtlAbstract.Abc_ShaderInput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    STR_mtlx_key_element = u'bindinput'
    STR_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcShaderInput(*args)


class NodeInput(mtlAbstract.Abc_NodeInput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    STR_mtlx_key_element = u'input'
    STR_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcNodeInput(*args)


class GeometryProperty(mtlAbstract.Abc_GeometryProperty):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    STR_mtlx_key_element = u'property'
    STR_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcGeometryProperty(*args)


class GeometryVisibility(mtlAbstract.Abc_GeometryVisibility):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    STR_mtlx_key_element = u'vistype'
    STR_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcVisibility(*args)


class GeometryOutput(mtlAbstract.Abc_ShaderOutput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    STR_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcShaderOutput(*args)


class ShaderOutput(mtlAbstract.Abc_ShaderOutput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    STR_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcShaderOutput(*args)


class NodeOutput(mtlAbstract.Abc_NodeOutput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    STR_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcNodeOutput(*args)


class NodeGraphOutput(mtlAbstract.Abc_NodeGraphOutput):
    CLS_raw_name = _mtlObjRaw.Raw_Name

    STR_mtlx_key_element = u'output'
    STR_mtlx_key_attribute = u'output'

    def __init__(self, *args):
        self._initAbcNodeGraphOutput(*args)
