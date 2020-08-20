# coding:utf-8
from LxBasic import bscMethods

from LxGraphic import grhObjAbs

from LxMtx import mtxObjAbs

from . import ma2mtxCfg


class AbsMa2mtxBasic(ma2mtxCfg.Ma2mtxUtility):
    pass


class AbsMa2mtxTrsObjLoader(grhObjAbs.AbsGrhTrsObjLoader):
    def _initAbsMa2mtxTrsObjLoader(self, *args):
        pass

    @classmethod
    def _trs_obj_loader_cls__set_node_raw_create_(cls, *args):
        (
            nodeRawDict,
            srcNodeQueryrawObj, tgtNodeQueryrawObj,
            orig_trs_node_raw_dict, orig_trs_otport_raw_list_dict, orig_trs_child_port_raw_list_dict
        ) = args
        # node
        nodeRawDict[cls.DEF_grh__key_source] = srcNodeQueryrawObj
        nodeRawDict[cls.DEF_grh__key_source_typepath] = srcNodeQueryrawObj.typepath
        nodeRawDict[cls.DEF_grh__key_target] = tgtNodeQueryrawObj
        nodeRawDict[cls.DEF_grh__key_target_typepath] = tgtNodeQueryrawObj.typepath
        # port
        _portRawList = []
        # extend
        for _key in cls.VAR_grh__trs_obj_loader__node_property_key_list:
            if _key in orig_trs_node_raw_dict:
                nodeRawDict[_key] = orig_trs_node_raw_dict[_key]

        _orig_trs_inport_raw_list = orig_trs_node_raw_dict[cls.DEF_grh__key_source_port]
        cls._trs_obj_loader_cls__set_definition_port_raws_create_(
            _portRawList,
            srcNodeQueryrawObj, tgtNodeQueryrawObj,
            _orig_trs_inport_raw_list, orig_trs_child_port_raw_list_dict,
        )

        _orig_trs_otport_raw_list = orig_trs_otport_raw_list_dict.get(tgtNodeQueryrawObj.datatype, {})
        cls._trs_obj_loader_cls__set_definition_port_raws_create_(
            _portRawList,
            srcNodeQueryrawObj, tgtNodeQueryrawObj,
            _orig_trs_otport_raw_list, orig_trs_child_port_raw_list_dict
        )

        nodeRawDict[cls.DEF_grh__key_source_port] = _portRawList

    @classmethod
    def _trs_obj_loader_cls__set_definition_port_raws_create_(cls, *args):
        (
            portRawList,
            srcNodeQueryrawObj, tgtNodeQueryrawObj,
            orig_trs_port_raw_dict, orig_trs_child_port_raw_list_dict
        ) = args

        for _srcPortpathStr, _orig_trs_port_raw in orig_trs_port_raw_dict.items():
            # definition
            if srcNodeQueryrawObj.hasPortQueryraw(_srcPortpathStr):
                _srcPortQueryrawObj = srcNodeQueryrawObj.portQueryraw(_srcPortpathStr)
                if cls.DEF_grh__key_target_portpath in _orig_trs_port_raw:
                    _ = _orig_trs_port_raw[cls.DEF_grh__key_target_portpath]

                    if isinstance(_, (str, unicode)):
                        _tgtPortpathStr = _
                        _tgtPortQueryrawObj = tgtNodeQueryrawObj.portQueryraw(_tgtPortpathStr)
                        cls._trs_obj_loader_cls__set_definition_port_raw_create_(
                            portRawList,
                            srcNodeQueryrawObj, tgtNodeQueryrawObj,
                            _srcPortQueryrawObj, _tgtPortQueryrawObj,
                            _orig_trs_port_raw, orig_trs_child_port_raw_list_dict,
                        )
                    # use as "inport" and "otport"
                    elif isinstance(_, (tuple, list)):
                        for _tgtPortpathStr in _:
                            _tgtPortQueryrawObj = tgtNodeQueryrawObj.portQueryraw(_tgtPortpathStr)
                            cls._trs_obj_loader_cls__set_definition_port_raw_create_(
                                portRawList,
                                srcNodeQueryrawObj, tgtNodeQueryrawObj,
                                _srcPortQueryrawObj, _tgtPortQueryrawObj,
                                _orig_trs_port_raw, orig_trs_child_port_raw_list_dict
                            )
            # customize
            else:
                pass

    @classmethod
    def _trs_obj_loader_cls__set_definition_port_raw_create_(cls, *args):
        (
            portRawList,
            srcNodeQueryrawObj, tgtNodeQueryrawObj,
            srcPortQueryrawObj, tgtPortQueryrawObj,
            orig_trs_port_raw, orig_child_port_raw_list_dict
        ) = args
        if cls.DEF_grh__keyword_datatype_convert in orig_trs_port_raw:
            _trsDatatypeStr = orig_trs_port_raw[cls.DEF_grh__keyword_datatype_convert][cls.DEF_grh__key_source]
        else:
            _trsDatatypeStr = tgtPortQueryrawObj.datatype

        # add parent first
        cls._trs_obj_loader_cls__set_definition_port_raw_add_(
            portRawList,
            srcPortQueryrawObj, tgtPortQueryrawObj,
            orig_trs_port_raw,
        )

        if tgtPortQueryrawObj.parent is None:
            _origTrsChildPortRawList = orig_child_port_raw_list_dict.get(_trsDatatypeStr, [])
            for _origTrsChildPortRaw in _origTrsChildPortRawList:
                cls._trs_obj_loader_cls__set_definition_port_child_raw_create_(
                    portRawList,
                    srcNodeQueryrawObj, tgtNodeQueryrawObj,
                    srcPortQueryrawObj, tgtPortQueryrawObj,
                    _origTrsChildPortRaw, _trsDatatypeStr,
                )

    @classmethod
    def _trs_obj_loader_cls__set_definition_port_child_raw_create_(cls, *args):
        (
            portRawList,
            srcNodeQueryrawObj, tgtNodeQueryrawObj,
            srcParentPortQueryrawObj, tgtParentPortQueryrawObj,
            orig_trs_child_port_raw, trsDatatypeStr
        ) = args

        srcParentPortpathString = srcParentPortQueryrawObj.portpath
        tgtParentPortpathString = tgtParentPortQueryrawObj.portpath

        srcFormatString = orig_trs_child_port_raw[cls.DEF_grh__key_source_portpath][cls.DEF_grh__key_format]
        tgtFormatString = orig_trs_child_port_raw[cls.DEF_grh__key_target_portpath][cls.DEF_grh__key_format]

        if trsDatatypeStr == cls.DEF_grh__keyword__porttype_texturecoord2_1:
            _srcPortpathStr = srcFormatString.format(
                **{cls.DEF_grh__key_portpath: srcParentPortpathString[:-2]}
            )
        else:
            _srcPortpathStr = srcFormatString.format(
                **{cls.DEF_grh__key_portpath: srcParentPortpathString}
            )

        _tgtPortpathStr = tgtFormatString.format(**{cls.DEF_grh__key_portpath: tgtParentPortpathString})

        _srcChildQueryrawObject = srcNodeQueryrawObj.portQueryraw(_srcPortpathStr)
        _tgtChildQueryrawObject = tgtNodeQueryrawObj.portQueryraw(_tgtPortpathStr)

        cls._trs_obj_loader_cls__set_definition_port_raw_add_(
            portRawList,
            _srcChildQueryrawObject, _tgtChildQueryrawObject,
            orig_trs_child_port_raw
        )

    @classmethod
    def _trs_obj_loader_cls__set_definition_port_raw_add_(cls, *args):
        (
            portRawList,
            srcPortQueryrawObj, tgtPortQueryrawObj,
            orig_trs_port_raw
        ) = args
        _dic = cls.CLS_ordered_dict()

        _dic[cls.DEF_grh__key_source] = srcPortQueryrawObj
        _dic[cls.DEF_grh__key_source_portpath] = srcPortQueryrawObj.portpath

        _dic[cls.DEF_grh__key_target] = tgtPortQueryrawObj
        _dic[cls.DEF_grh__key_target_portpath] = tgtPortQueryrawObj.portpath

        # extend
        for i in cls.VAR_grh__trs_obj_loader__port_property_key_list:
            if i in orig_trs_port_raw:
                _dic[i] = orig_trs_port_raw[i]

        portRawList.append(_dic)

    @classmethod
    def _trs_grh__obj_loader_cls__get_definition_node_raw_(cls, *args):
        out_node_raw_dict = cls.CLS_ordered_dict()
        cls._trs_obj_loader_cls__set_node_raw_create_(
            out_node_raw_dict,
            *args
        )
        return out_node_raw_dict


class AbsMa2mtxObjQueryrawCreator(grhObjAbs.AbsGrhTrsObjQueryrawCreator):
    def _initAbsMa2mtxObjQueryrawCreator(self, *args):
        self._initAbsGrhTrsObjQueryrawCreator(*args)

    # **************************************************************************************************************** #
    def _trs_obj_queryraw_creator__set_orig_raw_build_(self, *args):
        origTrsNodeRawDict = args[0]
        # object
        _origTrsNodeRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh__trs_obj_queryraw_creator__node_file
        ) or {}
        _origTrsGeometryRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh__trs_obj_queryraw_creator__geometry_file
        ) or {}
        _origTrsMaterialRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh__trs_obj_queryraw_creator__material_file
        ) or {}
        _origTrsCustomCategoryRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh__trs_custom_node_file
        ) or {}

        self._origTrsOtportRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh__trs_output_file
        ) or {}
        self._origTrsPortChildRawDict = bscMethods.OsJsonFile.read(
            self.VAR_grh__trs_port_child_file
        ) or {}

        self._origTrsCustomCategoryRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh__trs_custom_category_file
        ) or {}

        for i in [
            _origTrsNodeRaws,
            _origTrsGeometryRaws,
            _origTrsMaterialRaws,
            _origTrsCustomCategoryRaws
        ]:
            origTrsNodeRawDict.update(i)

    def _trs_obj_queryraw_creator__get_node_raw_(self, *args):
        srcTypepathStr = args[0]
        if srcTypepathStr in self._origTrsNodeRawDict:
            _origTrsObjRaw = self._origTrsNodeRawDict[srcTypepathStr]
            _tgtCategoryStr = _origTrsObjRaw[self.DEF_grh__key_target_typepath]
            _srcNodeQueryrawObj = self.IST_grh__trs_obj_queryraw_creator__source.nodeQueryraw(srcTypepathStr)
            _tgtNodeQueryrawObj = self.IST_grh__trs_obj_queryraw_creator__target.nodeQueryraw(_tgtCategoryStr)

            _trsObjRaw = self.CLS_grh__trs_obj_queryraw_creator__obj_loader.getDefinitionTrsNodeRaw(
                _srcNodeQueryrawObj, _tgtNodeQueryrawObj,
                _origTrsObjRaw,
                self._origTrsOtportRaws, self._origTrsPortChildRawDict
            )
            return _trsObjRaw


class AbsMa2mtxObjTranslator(grhObjAbs.AbsGrhObjTranslator):
    def _initAbsMa2mtxObjTranslator(self, *args):
        self._initAbsGrhObjTranslator(*args)


class AbsMa2mtxNode(grhObjAbs.AbsGrhTrsNode):
    def _initAbsMa2mtxNode(self, *args):
        self._initAbsGrhTrsNode(*args)


class AbsMa2mtxGeometry(grhObjAbs.AbsGrhTrsNode):
    def _initAbsMa2mtxGeometry(self, *args):
        self._initAbsGrhTrsNode(*args)


# node proxy ********************************************************************************************************* #
class AbsMa2mtxShaderProxy(grhObjAbs.AbsGrhTrsShaderProxy):
    def _initAbsMa2mtxShaderProxy(self, *args, **kwargs):
        self._initAbsGrhTrsShaderProxy(*args, **kwargs)


class AbsMa2mtxMaterialProxy(grhObjAbs.AbsGrhTrsMaterialProxy):
    def _initAbsMa2mtxMaterialProxy(self, *args, **kwargs):
        self._initAbsGrhTrsMaterialProxy(*args, **kwargs)


class AbsMa2mtxGeometryProxy(grhObjAbs.AbsGrhTrsGeometryProxy):
    def _initAbsMa2mtxGeometryProxy(self, *args, **kwargs):
        self._initAbsGrhTrsGeometryProxy(*args, **kwargs)

    def _trs_geometry_proxy__get_src_binding_material_obj_list_(self):
        return self._srcNodeObj.materials()


# element ************************************************************************************************************ #
class AbsMa2mtxLook(mtxObjAbs.AbsMtxTrsLook):
    def _initAbsMa2mtxLook(self, *args):
        self._initAbsMtxTrsLook(*args)


class AbsMa2mtxFile(mtxObjAbs.AbsMtxTrsFile):
    def _initAbsMa2mtxFile(self, *args):
        self._initAbsMtxTrsFile(*args)
