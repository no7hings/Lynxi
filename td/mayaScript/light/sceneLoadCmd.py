# coding=utf-8
import maya.cmds as cmds
#
print 'Scene Light Load Command'
#
def connectAssetBride():
    #
    rigBridgeLis = cmds.ls('*:*_rigBridge_grp')
    #
    if rigBridgeLis:
        for rigBridge in rigBridgeLis:
            modelBridge = rigBridge.replace('_extra', '_model').replace('_rigBridge', '_mdlBridge')
            if cmds.objExists(modelBridge):
                attrNameLis = cmds.listAttr(rigBridge, userDefined=1)
                if attrNameLis:
                    for attrName in attrNameLis:
                        sourceAttr = rigBridge + '.' + attrName
                        targetAttr = modelBridge + '.' + attrName
                        if cmds.objExists(sourceAttr) and cmds.objExists(targetAttr):
                            if not cmds.isConnected(sourceAttr, targetAttr):
                                cmds.connectAttr(sourceAttr, targetAttr)
                                print '{} > {}'.format(sourceAttr, targetAttr)
#
def run():
    connectAssetBride()
#
run()
