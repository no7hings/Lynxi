# coding:utf-8
import os
# noinspection PyUnresolvedReferences
import hou
# noinspection PyUnresolvedReferences
import _alembic_hom_extensions as abc

from LxBasic import bscMethods

from LxMtx import mtxObjects

from LxHouBasic import houBscObjects

from LxHouBasic.houBscMethods import _houBscMtdMtx

from LxHou2mtx import hou2mtxObjects


class Hou2MtxFnc(_houBscMtdMtx._Fnc):
    DEF_attrname__asset = 'asset_configure'
    DEF_attrname__asset_enable = 'asset_enable_{}'
    DEF_attrname__asset_file_path = 'asset_file_path_{}'
    DEF_attrname__asset_node_path = 'asset_node_path_{}'

    DEF_attrname__look = 'look_configure_{}'
    DEF_attrname__look_enable = 'look_enable_{}_{}'
    DEF_attrname__look_name = 'look_name_{}_{}'
    DEF_attrname__look_node_path = 'look_node_path_{}_{}'

    def __init__(self, *args):
        self._exportRaw = {}
        self._hoObj = args[0]

    def getParm(self, *args):
        return self._hoObj.parm(args[0])

    def getAssetObjs(self):
        return self.getInputObjsFnc(self._hoObj)

    def setAssetFileOpen(self, *args):
        nodeObj, parmObj = args
        parmNameStr = parmObj.name()
        index = int(parmNameStr[-1])
        assetFileParm = self.getParm(
            self.DEF_attrname__asset_file_path.format(
                index
            )
        )
        assetFilePathStr = assetFileParm.eval()
        osCmdExe = 'sublime_text'
        osCmd = '''"{}" "{}"'''.format(osCmdExe, assetFilePathStr)
        bscMethods.OsPlatform.runCommand(osCmd)

    def setAssetAnalysis(self):
        name = self._hoObj.name()
        # asset configure
        assetParm = self.getParm(self.DEF_attrname__asset)
        assetObjList = self.getAssetObjs()
        assetCount = len(assetObjList)
        assetParm.set(assetCount)
        for assetSeq, assetObj in enumerate(assetObjList):
            assetIndex = assetSeq + 1
            # asset enable
            assetEnableParm = self.getParm(
                self.DEF_attrname__asset_enable.format(assetIndex)
            )
            assetEnableParm.set(True)
            # asset file
            assetFileParm = self.getParm(
                self.DEF_attrname__asset_file_path.format(assetIndex)
            )
            if not assetFileParm.eval():
                _filepathStr = u'{}/{}_{}.mtlx'.format(os.path.splitext(self.getHipFilepathString())[0], name, assetIndex)
                assetFileParm.set(_filepathStr)

            # asset node
            assetNodeParm = self.getParm(
                self.DEF_attrname__asset_node_path.format(assetIndex)
            )
            assetNodeParm.set(assetObj.path())

            materialAssignSopList = _houBscMtdMtx._AssetFnc(assetObj).getMaterialAssignSops()
            lookCount = len(materialAssignSopList)
            # look configure
            lookParm = self.getParm(
                self.DEF_attrname__look.format(assetIndex)
            )
            lookParm.set(lookCount)

            for lookSeq, materialAssignSop in enumerate(materialAssignSopList):
                lookIndex = lookSeq + 1
                lookFormatArgs = assetIndex, lookIndex
                # look enable
                lookEnableParm = self.getParm(
                    self.DEF_attrname__look_enable.format(
                        *lookFormatArgs
                    )
                )
                lookEnableParm.set(True)
                # look name
                lookNameParm = self.getParm(
                    self.DEF_attrname__look_name.format(
                        *lookFormatArgs
                    )
                )
                if not lookNameParm.eval():
                    lookNameParm.set(
                        'look_{}'.format(materialAssignSop.name())
                    )
                # look node
                lookNodeParm = self.getParm(
                    self.DEF_attrname__look_node_path.format(
                        *lookFormatArgs
                    )
                )
                if not lookNodeParm.eval():
                    lookNodeParm.set(
                        materialAssignSop.path()
                    )

    def setAssetExport(self):
        # restore
        mtxObjects.GRH_OBJ_QUEUE.restore()
        houBscObjects.GRH_OBJ_QUEUE.restore()
        hou2mtxObjects.GRH_TRS_OBJ_QUEUE.restore()
        #
        assetParm = self.getParm(self.DEF_attrname__asset)
        assetCount = assetParm.eval()

        filepathStrList = []
        for assetSeq in range(assetCount):
            assetIndex = assetSeq + 1
            assetEnableParm = self.getParm(
                self.DEF_attrname__asset_enable.format(assetIndex)
            )
            if assetEnableParm.eval():
                # asset file
                assetFileParm = self.getParm(
                    self.DEF_attrname__asset_file_path.format(assetIndex)
                )
                assetFilepathStr = assetFileParm.eval()
                # asset node
                assetNodeParm = self.getParm(
                    self.DEF_attrname__asset_node_path.format(assetIndex)
                )
                assetNodePathStr = assetNodeParm.eval()

                _file = hou2mtxObjects.File(assetFilepathStr)

                lookParm = self.getParm(
                    self.DEF_attrname__look.format(assetIndex)
                )
                lookCount = lookParm.eval()
                for lookSeq in range(lookCount):
                    lookIndex = lookSeq + 1
                    lookFormatArgs = assetIndex, lookIndex
                    # look enable
                    lookEnableParm = self.getParm(
                        self.DEF_attrname__look_enable.format(
                            *lookFormatArgs
                        )
                    )
                    if lookEnableParm.eval():
                        lookNameParm = self.getParm(
                            self.DEF_attrname__look_name.format(
                                *lookFormatArgs
                            )
                        )
                        lookNodeParm = self.getParm(
                            self.DEF_attrname__look_node_path.format(
                                *lookFormatArgs
                            )
                        )
                        lookNodePathStr = lookNodeParm.eval()
                        _look = _file.addLook(lookNameParm.eval())
                        if _houBscMtdMtx._MaterialSopFnc(lookNodePathStr).hasGeometry() is True:
                            _ga = houBscObjects.GeomAssign(assetNodePathStr, lookNodePathStr)
                            _look.addAssign(_ga)

                filepathStrList.append(assetFilepathStr)
                _file.save()

        if len(filepathStrList) == 1:
            messageStr = filepathStrList[0]
        else:
            messageStr = u', '.join(filepathStrList)

        hou.ui.displayMessage(
            u'''result: export materialx file "{}".'''.format(
                messageStr
            )
        )


def hou2mtx_set_asset_analysis_cmd(kwargs):
    hou_node_obj = kwargs['node']
    fnc = Hou2MtxFnc(hou_node_obj)
    fnc.setAssetAnalysis()


def hou2mtx_set_asset_export_cmd(kwargs):
    hou_node_obj = kwargs['node']
    fnc = Hou2MtxFnc(hou_node_obj)
    fnc.setAssetExport()


def hou2mtx_set_asset_file_open_cmd(kwargs):
    hou_node_obj = kwargs['node']
    hou_parm_obj = kwargs['parm']
    fnc = Hou2MtxFnc(hou_node_obj)
    fnc.setAssetFileOpen(hou_node_obj, hou_parm_obj)
