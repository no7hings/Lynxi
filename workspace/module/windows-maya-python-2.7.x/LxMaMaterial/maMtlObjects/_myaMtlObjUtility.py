# coding:utf-8
from LxBasic import bscMethods

from LxMaBasic import maBscObjects

from LxMaMaterial import maMtlObjCore


class Asset(maMtlObjCore.Abc_MyaMtlBasic):
    DEF_option_dict = {
        '-noNormals': False,
        '-ro': False,
        '-stripNamespaces': False,
        '-uvWrite': True,
        '-writeFaceSets': False,
        '-wholeFrameGeo': False,
        '-worldSpace': True,
        '-writeVisibility': True,
        '-eulerFilter': False,
        '-writeCreases': False,
        '-writeUVSets': True,
    }

    def __init__(self, groupString):
        self._groupString = groupString
    #
    def exportGeometry(self, fileString):
        maBscObjects.AlembicCache(
            fileString, self._groupString,
            optionDic=self.DEF_option_dict
        ).export()
        
    def exportMaterial(self, fileString, lookString):
        _Material(
            fileString, self._groupString,
            lookString
        ).export()
    

class _Material(maMtlObjCore.Abc_MyaMtlBasic):
    PropertyAttrNameDic = {
        'visibility': True,
        'sidedness': False,
        #
        'receive_shadows': True,
        'self_shadows': True,
        #
        'invert_normals': False,
        'ray_bias': False,
        #
        'matrix': False,
        'transform_type': False,
        #
        'opaque': True,
        'matte': True,
        #
        'use_light_group': True,
        'light_group': True,
        'use_shadow_group': True,
        'shadow_group': True,
        #
        'trace_sets': False,
        #
        'motion_start': False,
        'motion_end': False,
        #
        'id': False,
        #
        'polygon_holes': False,
        #
        'crease_idxs': False,
        'crease_sharpness': False,
        #
        'shader': True,
        'shidxs': True,
        #
        'nsides': False,
        'vidxs': True,
        'vlist': False,
        #
        'nidxs': False,
        'nlist': False,
        #
        'uvidxs': True,
        'uvlist': True,
        #
        'smoothing': False,
        #
        'subdiv_type': True,
        'subdiv_iterations': True,
        'subdiv_adaptive_error': True,
        'subdiv_adaptive_metric': True,
        'subdiv_adaptive_space': True,
        'subdiv_frustum_ignore': True,
        'subdiv_uv_smoothing': True,
        'subdiv_smooth_derivs': True,
        #
        'disp_map': True,
        'disp_padding': True,
        'disp_height': True,
        'disp_zero_value': True,
        'disp_autobump': True,
        'autobump_visibility': True,
        'step_size': False,
        'volume_padding': False,
        'name': False,
    }
    PropertySep = ','

    def __init__(self, fileString, groupString, lookString):
        self._fileString = fileString
        self._groupString = groupString
        #
        self._shaderVariant = lookString
        self._attributeName = self.PropertySep.join([k for k, v in self.PropertyAttrNameDic.items() if v is True])
        #
        self._relativeEnable = True
        self._fullPathEnable = True
        self._objectPathsep = '/'
    #
    def _debug(self):
        lis = []

        data = bscMethods.OsFile.readlines(self._fileString)
        if data:
            for i in data:
                if 'type=""' in i:
                    i = i.replace('type=""', 'type="closure"')
                #
                lis.append(i)
        #
        bscMethods.OsFile.write(self._fileString, lis)
    #
    def export(self):
        self.MOD_maya_cmds.arnoldExportToMaterialX(
            self._groupString, filename=self._fileString,
            look=self._shaderVariant, properties=self._attributeName,
            relative=self._relativeEnable, fullPath=self._fullPathEnable,
            separator=self._objectPathsep
        )
        #
        self._debug()
