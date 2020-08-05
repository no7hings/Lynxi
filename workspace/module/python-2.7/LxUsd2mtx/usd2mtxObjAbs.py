# coding:utf-8
from LxBasic import bscMethods

from LxGraphic import grhCfg, grhObjAbs

from LxMtx import mtxObjAbs


class Abs_Usd2mtxBasic(object):
    pass


class Abs_Usd2mtxTrsObjLoader(grhObjAbs.Abs_GrhTrsObjLoader):
    def _initAbsUsd2mtxTrsObjLoader(self, *args):
        pass

    @classmethod
    def _trs_obj_loader_cls__set_node_raw_create_(cls, *args):
        (
            nodeRawDict,
            srcTypepathStr, tgtNodeQueryrawObj,
            orig_trs_node_raw_dict, orig_trs_otport_raw_list_dict, orig_trs_child_port_raw_list_dict
        ) = args
        # node
        nodeRawDict[cls.DEF_grh__key_source] = None
        nodeRawDict[cls.DEF_grh__key_source_typepath] = srcTypepathStr
        nodeRawDict[cls.DEF_grh__key_target] = tgtNodeQueryrawObj
        nodeRawDict[cls.DEF_grh__key_target_typepath] = tgtNodeQueryrawObj.typepath
        # port
        _portRawList = []
        # extend
        for _key in cls.VAR_grh__trs_obj_loader__node_property_key_list:
            if _key in orig_trs_node_raw_dict:
                nodeRawDict[_key] = orig_trs_node_raw_dict[_key]

        _orig_trs_port_raw_list = orig_trs_node_raw_dict[cls.DEF_grh__key_source_port]
        cls._trs_obj_loader_cls__set_customize_port_raws_create_(
            _portRawList,
            srcTypepathStr, tgtNodeQueryrawObj,
            _orig_trs_port_raw_list, orig_trs_child_port_raw_list_dict,
        )

        nodeRawDict[cls.DEF_grh__key_source_port] = _portRawList

    @classmethod
    def _trs_obj_loader_cls__set_customize_port_raws_create_(cls, *args):
        (
            portRawList,
            srcTypepathStr, tgtNodeQueryrawObj,
            orig_trs_port_raw_dict, orig_trs_child_port_raw_list_dict
        ) = args

        for _srcPortpathStr, _orig_trs_port_raw in orig_trs_port_raw_dict.items():
            _tgtPortpathStr = _orig_trs_port_raw[cls.DEF_grh__key_target_portpath]
            _tgtPortQueryrawObj = tgtNodeQueryrawObj.portQueryraw(_tgtPortpathStr)
            cls._trs_obj_loader_cls__set_customize_port_raw_create_(
                portRawList,
                srcTypepathStr, tgtNodeQueryrawObj,
                _srcPortpathStr, _tgtPortQueryrawObj,
                _orig_trs_port_raw, orig_trs_child_port_raw_list_dict
            )

    @classmethod
    def _trs_obj_loader_cls__set_customize_port_raw_create_(cls, *args):
        (
            portRawList,
            srcTypepathStr, tgtNodeQueryrawObj,
            srcPortpathStr, tgtPortQueryrawObj,
            orig_trs_port_raw, orig_child_port_raw_list_dict
        ) = args

        # add parent first
        cls._trs_obj_loader_cls__set_definition_port_raw_add_(
            portRawList,
            srcPortpathStr, tgtPortQueryrawObj, orig_trs_port_raw
        )

    @classmethod
    def _trs_obj_loader_cls__set_definition_port_raw_add_(cls, *args):
        (
            portRawList,
            srcPortpathStr, tgtPortQueryrawObj,
            orig_trs_port_raw
        ) = args
        _dic = cls.CLS_ordered_dict()

        _dic[cls.DEF_grh__key_source] = None
        _dic[cls.DEF_grh__key_source_portpath] = srcPortpathStr

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


class Abs_Usd2mtxObjQueryrawCreator(grhObjAbs.Abs_GrhTrsObjQueryrawCreator):
    def _initAbsUsd2mtxObjQueryrawCreator(self, *args):
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

        for i in [
            _origTrsNodeRaws,
            _origTrsGeometryRaws,
            _origTrsMaterialRaws
        ]:
            origTrsNodeRawDict.update(i)

    def _trs_obj_queryraw_creator__get_node_raw_(self, *args):
        srcTypepathStr = args[0]
        if srcTypepathStr in self._origTrsNodeRawDict:
            _origTrsObjRaw = self._origTrsNodeRawDict[srcTypepathStr]
            _tgtTypepathStr = _origTrsObjRaw[self.DEF_grh__key_target_typepath]
            _tgtNodeQueryrawObj = self.IST_grh__trs_obj_queryraw_creator__target.nodeQueryraw(_tgtTypepathStr)

            _trsObjRaw = self.CLS_grh__trs_obj_queryraw_creator__obj_loader.getDefinitionTrsNodeRaw(
                srcTypepathStr, _tgtNodeQueryrawObj,
                _origTrsObjRaw,
                None, None
            )
            return _trsObjRaw


class Abs_Usd2mtxObjTranslator(grhObjAbs.Abs_GrhObjTranslator):
    def _initAbsUsd2mtxObjTranslator(self, *args):
        self._initAbsGrhObjTranslator(*args)


class Abs_Usd2mtxNode(grhObjAbs.Abs_GrhTrsNode):
    def _initAbsUsd2mtxNode(self, *args):
        self._initAbsGrhTrsNode(*args)


# node proxy ********************************************************************************************************* #
class Abs_Usd2mtxShaderProxy(grhObjAbs.Abs_GrhTrsShaderProxy):
    def _initAbsUsd2mtxShaderProxy(self, *args, **kwargs):
        self._initAbsGrhTrsShaderProxy(*args, **kwargs)


class Abs_Usd2mtxMaterialProxy(grhObjAbs.Abs_GrhTrsMaterialProxy):
    def _initAbsUsd2mtxMaterialProxy(self, *args, **kwargs):
        self._initAbsGrhTrsMaterialProxy(*args, **kwargs)


class Abs_Usd2mtxGeometryProxy(grhObjAbs.Abs_GrhTrsGeometryProxy):
    def _initAbsUsd2mtxGeometryProxy(self, *args, **kwargs):
        self._initAbsGrhTrsGeometryProxy(*args, **kwargs)

    def _trs_geometry_proxy__get_src_binding_material_obj_list_(self):
        p = self._srcNodeObj.overridePort(
            self.VAR_grh__trs_src_material_portpath, grhCfg.GrhPortAssignQuery.asport
        )
        if p:
            _ = p.portraw()
            if _:
                return [self._srcNodeObj._node_cls__get_node_cache_obj_(i) for i in p.portraw()]
        return []

    def _trs_geometry_proxy__get_src_port_obj_list_(self):
        lis = []
        trsNodeQueryObj = self.trsNodeQuery()
        for i in trsNodeQueryObj.trsInportQueries():
            srcPortpathStr = i.source_portpath
            srcPortObj = self.srcNode().overrideInport(srcPortpathStr)
            if srcPortObj is not None:
                lis.append(srcPortObj)
        return lis


# element ************************************************************************************************************ #
class Abs_Usd2mtxLook(mtxObjAbs.Abs_MtxTrsLook):
    def _initAbsUsd2mtxLook(self, *args):
        self._initAbsMtxTrsLook(*args)


class Abs_Usd2mtxFile(mtxObjAbs.Abs_MtxTrsFile):
    def _initAbsUsd2mtxFile(self, *args):
        self._initAbsMtxTrsFile(*args)
