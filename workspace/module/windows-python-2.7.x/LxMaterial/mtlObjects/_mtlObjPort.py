# coding:utf-8
from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet


class Input(mtlObjCore.Abc_MtlInput):
    CLS_grh_porttype = _mtlObjRaw.PorttypeString
    CLS_grh_portpath = _mtlObjRaw.PortnameString

    VAR_mtl_file_element_key = u'input'
    VAR_mtl_file_attribute_attach_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlInput(*args)


class InputChannel(mtlObjCore.Abc_MtlInput):
    CLS_grh_porttype = _mtlObjRaw.PorttypeString
    CLS_grh_portpath = _mtlObjRaw.PortnameString

    VAR_mtl_file_element_key = u'input'
    VAR_mtl_file_attribute_attach_key = u'channels'

    def __init__(self, *args):
        self._initAbcMtlInput(*args)


class Output(mtlObjCore.Abc_MtlOutput):
    CLS_grh_porttype = _mtlObjRaw.PorttypeString
    CLS_grh_portpath = _mtlObjRaw.PortnameString

    VAR_mtl_file_element_key = u'output'
    VAR_mtl_file_attribute_attach_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlOutput(*args)


class OutputChannel(mtlObjCore.Abc_MtlOutput):
    CLS_grh_porttype = _mtlObjRaw.PorttypeString
    CLS_grh_portpath = _mtlObjRaw.PortnameString

    VAR_mtl_file_element_key = u'output'
    VAR_mtl_file_attribute_attach_key = u'channels'

    def __init__(self, *args):
        self._initAbcMtlOutput(*args)


class NodeGraphOutput(mtlObjCore.Abc_MtlNodeGraphOutput):
    CLS_mtl_name = _mtlObjRaw.NameString

    VAR_mtl_file_element_key = u'output'
    VAR_mtl_file_attribute_attach_key = u'output'

    def __init__(self, *args):
        self._initAbcMtlNodeGraphOutput(*args)


class BindInput(mtlObjCore.Abc_MtlBindInput):
    VAR_mtl_file_element_key = u'bindinput'

    def __init__(self, *args):
        self._initAbcMtlBindInput(*args)


class Property(mtlObjCore.Abc_MtlProperty):
    VAR_mtl_file_element_key = u'property'

    def __init__(self, *args):
        self._initAbcMtlProperty(*args)


class Visibility(mtlObjCore.Abc_MtlVisibility_):
    VAR_mtl_file_element_key = u'visibility'

    def __init__(self, *args):
        self._initAbcMtlVisibilityAssign(*args)


class Propertyset(mtlObjCore.Abc_MtlPropertyset):
    CLS_mtl_name = _mtlObjRaw.NameString

    CLS_grh_port_set = _mtlObjSet.PortSet

    VAR_mtl_file_element_key = u'propertyset'
    VAR_mtl_file_attribute_attach_key = u'propertyset'

    def __init__(self, *args):
        """
        :param args: str(geometry dagpath)
        """
        self._initAbcMtlPropertyset(*args)
