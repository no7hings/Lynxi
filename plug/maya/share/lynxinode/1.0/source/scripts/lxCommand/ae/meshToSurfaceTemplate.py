# encoding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.mel as mel
#
import lxCommand.cmds as ctomcmds
#
from lxCommand.template import nodeTemplate


#
class AEmeshToSurfaceTemplate(nodeTemplate.attributeTemplate):
    @staticmethod
    def selectMesh(nodeName):
        mesh = ctomcmds.getMtosMesh(nodeName)
        if mesh:
            cmds.select(mesh)
            ctomcmds.setAddToModelPanel(mesh)
    #
    def selectMeshNew(self, attrName):
        tokens = attrName.split('.')
        nodeName = tokens[0]
        cmds.button(
            'mtosSelMeshButton', label='Select Mesh', backgroundColor=(1, .5, .25),
            command=lambda arg=None, x=nodeName: self.selectMesh(x)
        )
    #
    def selectMeshReplace(self, attrName):
        tokens = attrName.split('.')
        nodeName = tokens[0]
        cmds.button(
            'mtosSelMeshButton', edit=True,
            command=lambda arg=None, x=nodeName: self.selectMesh(x)
        )
    #
    def setup(self):
        self.beginScrollLayout()
        #
        self.addCustom('selectMesh', self.selectMeshNew, self.selectMeshReplace)
        #
        self.beginLayout('Modify', collapse=False)
        self.addControl('direction', label='Direction')
        self.endLayout()
        #
        mel.eval('AEdependNodeTemplate ' + self.nodeName)
        self.addExtraControls()
        #
        self.endScrollLayout()

