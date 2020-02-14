# coding:utf-8
from LxMaterial import mtlObjAbstract

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet


class Channel(mtlObjAbstract.Abc_Input):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    def __init__(self, *args):
        self._initAbcInput(*args)


# maya: shader engine
class ShadersetInput(mtlObjAbstract.Abc_Input):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    DEF_mtlx_key_element = u'bindinput'
    DEF_mtlx_key_attribute = u'context'

    def __init__(self, *args):
        self._initAbcInput(*args)


class ShaderInput(mtlObjAbstract.Abc_ShaderInput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    DEF_mtlx_key_element = u'bindinput'
    DEF_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcShaderInput(*args)


class NodeInput(mtlObjAbstract.Abc_NodeInput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    DEF_mtlx_key_element = u'input'
    DEF_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcNodeInput(*args)


class GeometryProperty(mtlObjAbstract.Abc_GeometryProperty):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    DEF_mtlx_key_element = u'property'
    DEF_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcGeometryProperty(*args)


class GeometryVisibility(mtlObjAbstract.Abc_GeometryVisibility):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    DEF_mtlx_key_element = u'vistype'
    DEF_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcVisibility(*args)


class GeometryOutput(mtlObjAbstract.Abc_ShaderOutput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    DEF_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcShaderOutput(*args)


class ShaderOutput(mtlObjAbstract.Abc_ShaderOutput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    DEF_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcShaderOutput(*args)


class NodeOutput(mtlObjAbstract.Abc_NodeOutput):
    CLS_portpath = _mtlObjRaw.Raw_PortPath

    CLS_set_channel = _mtlObjSet.Set_Port

    DEF_mtlx_key_attribute = u'member'

    def __init__(self, *args):
        self._initAbcNodeOutput(*args)


class NodeGraphOutput(mtlObjAbstract.Abc_NodeGraphOutput):
    CLS_raw_name = _mtlObjRaw.Raw_Name

    DEF_mtlx_key_element = u'output'
    DEF_mtlx_key_attribute = u'output'

    def __init__(self, *args):
        self._initAbcNodeGraphOutput(*args)
