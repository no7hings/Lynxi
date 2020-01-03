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
class AEcurveToMeshTemplate(nodeTemplate.attributeTemplate):
    @staticmethod
    def selectCurve(nodeName):
        curve = ctomcmds.getCtomCurve(nodeName)
        if curve:
            cmds.select(curve)
            ctomcmds.setAddToModelPanel(curve)
    #
    def selectCurveNew(self, attrName):
        tokens = attrName.split('.')
        nodeName = tokens[0]
        cmds.button(
            'ctomSelCurveButton', label='Select Curve', backgroundColor=(1, .5, .25),
            command=lambda arg=None, x=nodeName: self.selectCurve(x)
        )
    #
    def selectCurveReplace(self, attrName):
        tokens = attrName.split('.')
        nodeName = tokens[0]
        cmds.button(
            'ctomSelCurveButton', edit=True,
            command=lambda arg=None, x=nodeName: self.selectCurve(x)
        )
    @staticmethod
    def resetModify(nodeName):
        ctomcmds.setResetCtomNodeModify(nodeName)
    #
    def resetModifyNew(self, attrName):
        tokens = attrName.split('.')
        nodeName = tokens[0]
        cmds.button(
            'ctomResetModifyButton', label='Reset Modify', backgroundColor=(1, 0, .25),
            command=lambda arg=None, x=nodeName: self.resetModify(x)
        )
    #
    def resetModifyReplace(self, attrName):
        tokens = attrName.split('.')
        nodeName = tokens[0]
        cmds.button(
            'ctomResetModifyButton', edit=True,
            command=lambda arg=None, x=nodeName: self.resetModify(x)
        )
    #
    def setup(self):
        self.beginScrollLayout()
        #
        self.beginLayout('Custom', collapse=False)
        self.addControl('uniformEnable', label='Uniform Enable')
        self.addControl('vDivision', label='V Division')
        self.addControl('uDivision', label='U Division')
        self.addControl('width', label='Width')
        self.endLayout()
        #
        self.addCustom('selectCurve', self.selectCurveNew, self.selectCurveReplace)
        #
        self.beginLayout('Modify', collapse=False)
        self.addControl('spin', label='Spin')
        self.addControl('twist', label='Twist')
        self.addControl('taper', label='Taper')
        self.addSeparator()
        self.addControl('archAttachCurveEnable', label='Arch Attach Curve Enable')
        self.addControl('arch', label='Arch')
        self.addSeparator()
        self.addControl('minPercent', label='Minimum Percent')
        self.addControl('maxPercent', label='Maximum Percent')
        self.endLayout()
        #
        self.addCustom('resetModify', self.resetModifyNew, self.resetModifyReplace)
        #
        self.beginLayout('Parameter', collapse=False)
        self.addControl('sample', label='Sample')
        self.addControl('smoothDepth', label='Smooth Depth')
        self.endLayout()
        #
        self.beginLayout('Extra', collapse=True)
        mel.eval('AEaddRampControl ' + self.nodeName + '.widthExtra')
        mel.eval('AEaddRampControl ' + self.nodeName + '.spinExtra')
        mel.eval('AEaddRampControl ' + self.nodeName + '.angleOffset')
        self.endLayout()
        #
        mel.eval('AEdependNodeTemplate ' + self.nodeName)
        self.addExtraControls()
        #
        self.endScrollLayout()

