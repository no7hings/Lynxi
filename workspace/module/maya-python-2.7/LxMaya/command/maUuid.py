# coding=utf-8
import uuid
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxPreset import prsOutputs, prsMethods

#
assetUniqueIdLabel = prsOutputs.Util.astUniqueIdAttrLabel
#
none = ''


#
def getUuid():
    return str(uuid.uuid1()).upper()


#
def setAttrUniqueId(nodepathString):
    uniqueId = _getNodeUniqueIdString(nodepathString)
    attr = nodepathString + '.' + assetUniqueIdLabel
    if not cmds.objExists(attr):
        cmds.addAttr(nodepathString, longName=assetUniqueIdLabel, dataType='string')
    #
    cmds.setAttr(attr, lock=0)
    cmds.setAttr(attr, uniqueId, type='string', lock=1)


#
def setAttrUniqueIds(objects):
    for nodepathString in objects:
        setAttrUniqueId(nodepathString)


#
def getAttrUniqueId(nodepathString):
    attr = nodepathString + '.' + assetUniqueIdLabel
    if cmds.objExists(attr):
        return cmds.getAttr(attr)


#
def _getNodeUniqueIdString(nodepathString):
    if cmds.objExists(nodepathString):
        uniqueIds = cmds.ls(nodepathString, uuid=1)
        if uniqueIds:
            return uniqueIds[0]


#
def getSelUniqueIds():
    lis = []
    selectedObjects = cmds.ls(selection=1, long=1)
    if selectedObjects:
        for i in selectedObjects:
            uniqueIds = cmds.ls(i, uuid=1)
            if uniqueIds:
                lis.append(uniqueIds[0])
    return lis


#
def setSelObject(uniqueId, add=False):
    objectPath = getObject(uniqueId)
    cmds.select(objectPath, add=add)


#
def setMayaUniqueId(nodepathString, uniqueId=none):
    if cmds.objExists(nodepathString):
        if not uniqueId:
            uniqueId = getAttrUniqueId(nodepathString)
        if uniqueId:
            cmds.rename(nodepathString, uniqueId, uuid=1)


#
def setUniqueIdForce(nodepathString, uniqueId):
    if cmds.objExists(nodepathString):
        objectPaths = getObjects(uniqueId)
        if objectPaths:
            [cmds.rename(i, getUuid(), uuid=1) for i in objectPaths]
        #
        cmds.rename(nodepathString, uniqueId, uuid=1)


#
def setRefreshMayaUniqueId(sourceUniqueId, targetUniqueId):
    nodepathString = getObject(sourceUniqueId, fullPath=1)
    if nodepathString:
        setMayaUniqueId(nodepathString, targetUniqueId)


#
def isUsable(string):
    boolean = False
    if len(string) == 36:
        if string[8] == '-' and string[13] == '-' and string[18] == '-' and string[23] == '-':
            boolean = True
    return boolean


#
def getObjects(uniqueId, fullPath=True):
    return cmds.ls(uniqueId, long=fullPath)


#
def getObject(uniqueId, fullPath=True):
    string = none
    data = cmds.ls(uniqueId, long=fullPath)
    if data:
        string = data[0]
    return string
