# coding:utf-8
from LxBasic import bscMethods

from LxGraphic import grhCfg, grhObjAbs

from LxMtx import mtxObjAbs

from . import hou2mtxCfg


class Abs_Hou2mtxBasic(hou2mtxCfg.Hou2mtxUtility):
    pass


class Abs_Hou2mtxTrsObjLoader(grhObjAbs.Abs_GrhTrsObjLoader):
    def _initAbsHou2mtxTrsObjLoader(self, *args):
        pass

    @classmethod
    def _trs_obj_loader_cls__set_node_raw_create_(cls, *args):
        (
            nodeRawDict,
            srcNodeQueryrawObj, tgtNodeQueryrawObj,
            orig_trs_obj_raw_dict, orig_trs_otport_raw_list_dict, orig_trs_child_port_raw_list_dict
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
            if _key in orig_trs_obj_raw_dict:
                nodeRawDict[_key] = orig_trs_obj_raw_dict[_key]

        _orig_trs_inport_raw_list = orig_trs_obj_raw_dict[cls.DEF_grh__key_source_port]
        cls._trs_obj_loader_cls__set_definition_port_raws_create_(
            _portRawList,
            srcNodeQueryrawObj, tgtNodeQueryrawObj,
            _orig_trs_inport_raw_list, orig_trs_child_port_raw_list_dict,
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
            # customize
            else:
                portRaw = grhCfg.GrhPortQuery.getPortRaw(
                    **{
                        grhCfg.GrhPortQuery.portpath: _srcPortpathStr
                    }
                )
                _srcPortQueryrawObj = srcNodeQueryrawObj.createPortQueryraw(portRaw)
            #
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
                # use as "inport" and/or "otport"
                elif isinstance(_, dict):
                    for _tgtAssignStr, _tgtPortpathStr in _.items():
                        _tgtPortQueryrawObj = tgtNodeQueryrawObj.portQueryraw(
                            _tgtPortpathStr, assign=_tgtAssignStr
                        )
                        cls._trs_obj_loader_cls__set_definition_port_raw_create_(
                            portRawList,
                            srcNodeQueryrawObj, tgtNodeQueryrawObj,
                            _srcPortQueryrawObj, _tgtPortQueryrawObj,
                            _orig_trs_port_raw, orig_trs_child_port_raw_list_dict
                        )

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


class Abs_Hou2mtxObjQueryrawCreator(grhObjAbs.Abs_GrhTrsObjQueryrawCreator):
    def _initAbsHou2mtxObjQueryrawCreator(self, *args):
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
            srcNodeQueryrawObj = self.IST_grh__trs_obj_queryraw_creator__source.nodeQueryraw(srcTypepathStr)
            origTrsObjRaw = self._origTrsNodeRawDict[srcTypepathStr]
            tgtTypepathStr = origTrsObjRaw[self.DEF_grh__key_target_typepath]
            tgtNodeQueryrawObj = self.IST_grh__trs_obj_queryraw_creator__target.nodeQueryraw(tgtTypepathStr)
            # _trs_grh__obj_loader_cls__get_definition_node_raw_
            return self.CLS_grh__trs_obj_queryraw_creator__obj_loader.getDefinitionTrsNodeRaw(
                srcNodeQueryrawObj, tgtNodeQueryrawObj,
                origTrsObjRaw, None, None
            )


# ******************************************************************************************************************** #
class Abs_Hou2mtxObjTranslator(grhObjAbs.Abs_GrhObjTranslator):
    def _initAbsHou2mtxObjTranslator(self, *args):
        self._initAbsGrhObjTranslator(*args)


class Abs_Hou2mtxNode(grhObjAbs.Abs_GrhTrsNode):
    def _initAbsHou2mtxNode(self, *args):
        self._initAbsGrhTrsNode(*args)


# node proxy ********************************************************************************************************* #
class Abs_Hou2mtxShaderProxy(grhObjAbs.Abs_GrhTrsShaderProxy):
    def _initAbsHou2mtxShaderProxy(self, *args, **kwargs):
        self._initAbsGrhTrsShaderProxy(*args, **kwargs)


class Abs_Hou2mtxMaterialProxy(grhObjAbs.Abs_GrhTrsMaterialProxy):
    def _initAbsHou2mtxMaterialProxy(self, *args, **kwargs):
        self._initAbsGrhTrsMaterialProxy(*args, **kwargs)


class Abs_Hou2mtxGeometryProxy(grhObjAbs.Abs_GrhTrsGeometryProxy):
    def _initAbsHou2mtxGeometryProxy(self, *args, **kwargs):
        self._initAbsGrhTrsGeometryProxy(*args, **kwargs)

    def _trs_geometry_proxy__get_src_binding_material_obj_list_(self):
        port = self._srcNodeObj.port(u'shop_materialpath')
        if port.hasSource():
            return [port.source().node()]
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
class Abs_Hou2mtxLook(mtxObjAbs.Abs_MtxTrsLook):
    def _initAbsHou2mtxLook(self, *args):
        self._initAbsMtxTrsLook(*args)

    def _mtx__trs_look__set_material_assign_add_(self, *args):
        materialAssignObj = args[0]
        srcGeometryObjList = materialAssignObj.geometries()
        for srcGeometryObj in srcGeometryObjList:
            srcGeometryPathStr = srcGeometryObj.pathString()
            self.addSrcGeometry(srcGeometryPathStr)


class Abs_Hou2mtxFile(mtxObjAbs.Abs_MtxTrsFile):
    def _initAbsHou2mtxFile(self, *args):
        self._initAbsMtxTrsFile(*args)
