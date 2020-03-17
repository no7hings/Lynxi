# coding:utf-8
from LxMaterial import mtlObjCore, mtlConfigure


class Raw_Closure(mtlObjCore.Abc_MtlRaw):
    def __init__(self, *args):
        self._initAbcMtlRaw(*args)


class NameString(mtlObjCore.Abc_MtlString):
    VAR_mtl_file_element_key = u'string'
    VAR_mtl_file_attribute_key = u'name'

    def __init__(self, *args):
        self.Abc_initAbcMtlString(*args)


class TypeString(mtlObjCore.Abc_MtlString):
    VAR_mtl_file_element_key = u'string'
    VAR_mtl_file_attribute_key = u'type'

    def __init__(self, *args):
        self.Abc_initAbcMtlString(*args)


class VistypeString(mtlObjCore.Abc_MtlString):
    VAR_mtl_file_element_key = u'string'
    VAR_mtl_file_attribute_key = u'vistype'

    def __init__(self, *args):
        self.Abc_initAbcMtlString(*args)


class VersionString(mtlObjCore.Abc_MtlString):
    VAR_mtl_file_element_key = u'string'
    VAR_mtl_file_attribute_key = u'version'

    def __init__(self, *args):
        self.Abc_initAbcMtlString(*args)


class DatatypeString(mtlObjCore.Abc_MtlString):
    VAR_mtl_file_element_key = u'datatype'
    VAR_mtl_file_attribute_key = u'type'

    def __init__(self, *args):
        self.Abc_initAbcMtlString(*args)


class ShaderCategoryString(mtlObjCore.Abc_MtlString):
    VAR_mtl_file_element_key = u'string'
    VAR_mtl_file_attribute_key = u'node'

    def __init__(self, *args):
        self.Abc_initAbcMtlString(*args)


class NodeCategoryString(mtlObjCore.Abc_MtlString):
    VAR_mtl_file_element_key = u'string'
    VAR_mtl_file_attribute_key = u'category'

    def __init__(self, *args):
        self.Abc_initAbcMtlString(*args)


class Raw_NamespacePath(mtlObjCore.Abc_MtlNodeName):
    CLS_mtl_raw = NameString

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_namespace_separator

    def __init__(self, *args):
        self._initAbcMtlNodeName(*args)


class FileName(mtlObjCore.Abc_MtlFileName):
    CLS_mtl_raw = NameString

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_file_separator

    VAR_mtl_file_attribute_key = u'filepath'

    def __init__(self, *args):
        self._initAbcMtlFileName(*args)


class ReferenceFileName(mtlObjCore.Abc_MtlFileName):
    CLS_mtl_raw = NameString

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_file_separator

    VAR_mtl_file_attribute_key = u'href'

    def __init__(self, *args):
        self._initAbcMtlFileName(*args)


class Raw_MaterialDagpath(mtlObjCore.Abc_MtlMaterialName):
    CLS_mtl_raw = NameString

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_node_separator

    VAR_mtl_file_attribute_key = u'name'

    def __init__(self, *args):
        self._initAbcMtlNodeName(*args)


class NodeName(mtlObjCore.Abc_MtlNodeName):
    CLS_mtl_raw = NameString

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_node_separator

    VAR_mtl_file_attribute_key = u'name'

    def __init__(self, *args):
        self._initAbcMtlNodeName(*args)


class PortName(mtlObjCore.Abc_MtlPortName):
    CLS_mtl_raw = NameString

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_port_separator

    VAR_mtl_file_attribute_key = u'name'

    def __init__(self, *args):
        self._initAbcMtlPortName(*args)


class GeometryVisibilityName(mtlObjCore.Abc_MtlPortName):
    CLS_mtl_raw = NameString

    VAR_mtl_raw_separator = mtlConfigure.Utility.DEF_mtl_port_separator

    VAR_mtl_file_attribute_key = u'vistype'

    def __init__(self, *args):
        self._initAbcMtlPortName(*args)
