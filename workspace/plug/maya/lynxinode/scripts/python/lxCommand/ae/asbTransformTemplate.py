# encoding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.mel as mel
# noinspection PyUnresolvedReferences
from lxCommand.template import nodeTemplate
# noinspection PyUnresolvedReferences
from lxCommand import asbCmds


#
def switchNew(*args):
    cmds.rowLayout(
        numberOfColumns=4, adjustableColumn=1,
        columnWidth4=[120] * 4,
        columnAttach4=['both'] * 4,
        columnAlign4=['center'] * 4,
        columnOffset4=[2] * 4
    )
    cmds.text(label='')
    cmds.nodeIconButton(
        'asbSwitchLod0', style='iconAndTextHorizontal', image1='QR_refresh.png', label='LOD - 0',
        command=lambda *args_: asbCmds.setSelAsbSwitchCmd(0)
    )
    cmds.nodeIconButton(
        'asbSwitchLod1', style='iconAndTextHorizontal', image1='QR_refresh.png', label='LOD - 1',
        command=lambda *args_: asbCmds.setSelAsbSwitchCmd(1)
    )
    cmds.nodeIconButton(
        'asbSwitchLod2', style='iconAndTextHorizontal', image1='QR_refresh.png', label='LOD - 2',
        command=lambda *args_: asbCmds.setSelAsbSwitchCmd(2)
    )
    cmds.setParent('..')


#
def switchReplace(*args):
    pass


#
def asbComposeNew(*args):
    tokens = args[0].split('.')
    nodePath = tokens[0]
    nodeName = nodePath.split('|')[-1]
    #
    cmds.columnLayout(adjustableColumn=2, rowSpacing=4)
    cmds.rowLayout(
        numberOfColumns=4, adjustableColumn=1,
        columnWidth4=[120] * 4,
        columnAttach4=['both'] * 4,
        columnAlign4=['center'] * 4,
        columnOffset4=[2] * 4
    )
    cmds.text(label='')
    cmds.nodeIconButton(
        'asbAddAsset0', style='iconAndTextHorizontal', image1='QR_add.png', label='Import',
        command=lambda *args_: asbCmds.setSelAsbImportAddCmd()
    )
    cmds.nodeIconButton(
        'asbAddAsset1', style='iconAndTextHorizontal', image1='QR_add.png', label='Reference',
        command=lambda *args_: asbCmds.setSelAsbRefsAddCmd()
    )
    cmds.nodeIconButton(
        'asbRemoveAsset', style='iconAndTextHorizontal', image1='QR_delete.png', label='Remove',
        command=lambda *args_: asbCmds.setSelAsbRemoveCmd()
    )
    cmds.setParent('..')
    #
    cmds.columnLayout(adjustableColumn=1, rowSpacing=4)
    #
    referenceNodeLis = []
    referenceAssetGroup = asbCmds.toImportAssetGroupName(nodeName)
    if cmds.objExists(referenceAssetGroup):
        referenceNodeLis.append(referenceAssetGroup)
        cmds.nodeIconButton('asbAddAsset0', edit=1, enable=0)
        cmds.nodeIconButton('asbAddAsset1', edit=1, enable=0)
        cmds.nodeIconButton('asbRemoveAsset', edit=1, enable=1)
    else:
        cmds.nodeIconButton('asbAddAsset0', edit=1, enable=1)
        cmds.nodeIconButton('asbAddAsset1', edit=1, enable=1)
        cmds.nodeIconButton('asbRemoveAsset', edit=1, enable=0)
    cmds.textScrollList('asbCompose', allowMultiSelection=True, height=64, append=referenceNodeLis)


#
def asbComposeReplace(*args):
    tokens = args[0].split('.')
    nodePath = tokens[0]
    nodeName = nodePath.split('|')[-1]
    #
    cmds.textScrollList('asbCompose', edit=1, removeAll=1)
    referenceNodeLis = []
    referenceAssetGroup = asbCmds.toImportAssetGroupName(nodeName)
    if cmds.objExists(referenceAssetGroup):
        referenceNodeLis.append(referenceAssetGroup)
        cmds.nodeIconButton('asbAddAsset0', edit=1, enable=0)
        cmds.nodeIconButton('asbAddAsset1', edit=1, enable=0)
        cmds.nodeIconButton('asbRemoveAsset', edit=1, enable=1)
    else:
        cmds.nodeIconButton('asbAddAsset0', edit=1, enable=1)
        cmds.nodeIconButton('asbAddAsset1', edit=1, enable=1)
        cmds.nodeIconButton('asbRemoveAsset', edit=1, enable=0)
    #
    cmds.textScrollList('asbCompose', edit=1, append=referenceNodeLis)


#
class AEasbTransformTemplate(nodeTemplate.attributeTemplate):
    def setup(self):
        self.beginScrollLayout()
        #
        self.beginLayout('Assembly Manager', collapse=False)
        #
        self.beginLayout('Attribute', collapse=False)
        self.addControl('namespace', label='Namespace')
        self.endLayout()
        #
        self.beginLayout('File', collapse=False)
        self.addControl('lod', label='LOD', changeCommand=asbCmds.setCurAsbLodSwitchCmd)
        self.addControl('proxyCacheFile', label='Proxy Cache File')
        self.addControl('gpuCacheFile', label='GPU Cache File')
        self.addControl('assetFile', label='Asset File')
        self.endLayout()
        #
        self.beginLayout('Switch', collapse=False)
        self.addCustom('switch', switchNew, switchReplace)
        self.endLayout()
        self.beginLayout('Compose', collapse=False)
        self.addCustom('compose', asbComposeNew, asbComposeReplace)
        self.endLayout()
        #
        self.endLayout()
        #
        mel.eval('AEtransformMain ' + self.nodeName)
        mel.eval('AEtransformNoScroll ' + self.nodeName)
        mel.eval('AEtransformSkinCluster ' + self.nodeName)
        #
        mel.eval('AEdependNodeTemplate ' + self.nodeName)
        #
        self.addExtraControls()
        self.endScrollLayout()
