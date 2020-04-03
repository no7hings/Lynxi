# coding:utf-8
from LxGraphic.grhObjects import _grhObjSet

from .. import mtlObjAbs

from ..mtlObjects import _mtlObjRaw


class Input(mtlObjAbs.Abc_MtlInput):
    CLS_grh_porttype = _mtlObjRaw.Porttype
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_mtl_file_element_key = u'input'
    VAR_mtl_file_attribute_attach_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlInput(*args)


class InputChannel(mtlObjAbs.Abc_MtlInput):
    CLS_grh_porttype = _mtlObjRaw.Porttype
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_mtl_file_element_key = u'input'
    VAR_mtl_file_attribute_attach_key = u'channels'

    def __init__(self, *args):
        self._initAbcMtlInput(*args)


class Output(mtlObjAbs.Abc_MtlOutput):
    CLS_grh_porttype = _mtlObjRaw.Porttype
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_mtl_file_element_key = u'output'
    VAR_mtl_file_attribute_attach_key = u'member'

    def __init__(self, *args):
        self._initAbcMtlOutput(*args)


class OutputChannel(mtlObjAbs.Abc_MtlOutput):
    CLS_grh_porttype = _mtlObjRaw.Porttype
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_mtl_file_element_key = u'output'
    VAR_mtl_file_attribute_attach_key = u'channels'

    def __init__(self, *args):
        self._initAbcMtlOutput(*args)


class NodeGraphOutput(mtlObjAbs.Abc_MtlNodeGraphOutput):
    CLS_mtl_name = _mtlObjRaw.Name

    VAR_mtl_file_element_key = u'output'
    VAR_mtl_file_attribute_attach_key = u'output'

    def __init__(self, *args):
        self._initAbcMtlNodeGraphOutput(*args)


class BindInput(mtlObjAbs.Abc_MtlBindInput):
    CLS_mtl_name = _mtlObjRaw.Name

    VAR_mtl_file_element_key = u'bindinput'

    def __init__(self, *args):
        self._initAbcMtlBindInput(*args)


class Property(mtlObjAbs.Abc_MtlProperty):
    CLS_mtl_name = _mtlObjRaw.Name

    VAR_mtl_file_element_key = u'property'

    def __init__(self, *args):
        self._initAbcMtlProperty(*args)


class Visibility(mtlObjAbs.Abc_MtlVisibility_):
    CLS_mtl_name = _mtlObjRaw.Name

    VAR_mtl_file_element_key = u'visibility'

    def __init__(self, *args):
        self._initAbcMtlVisibilityAssign(*args)


class Propertyset(mtlObjAbs.Abc_MtlPropertyset):
    CLS_mtl_name = _mtlObjRaw.Name

    CLS_grh_port_set = _grhObjSet.ObjSet

    VAR_mtl_file_element_key = u'propertyset'
    VAR_mtl_file_attribute_attach_key = u'propertyset'

    def __init__(self, *args):
        """
        :param args: str(geometry dagpath)
        """
        self._initAbcMtlPropertyset(*args)
