# coding=utf-8
import uuid
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxPreset import prsVariants, prsMethods

#
assetUniqueIdLabel = prsVariants.Util.astUniqueIdAttrLabel
#
none = ''


#
def getUuid():
    return str(uuid.uuid1()).upper()


#
def setAttrUniqueId(objectString):
    uniqueId = getNodeUniqueId(objectString)
    attr = objectString + '.' + assetUniqueIdLabel
    if not cmds.objExists(attr):
        cmds.addAttr(objectString, longName=assetUniqueIdLabel, dataType='string')
    #
    cmds.setAttr(attr, lock=0)
    cmds.setAttr(attr, uniqueId, type='string', lock=1)


#
def setAttrUniqueIds(objects):
    for objectString in objects:
        setAttrUniqueId(objectString)


#
def getAttrUniqueId(objectString):
    attr = objectString + '.' + assetUniqueIdLabel
    if cmds.objExists(attr):
        return cmds.getAttr(attr)


#
def getNodeUniqueId(objectString):
    if cmds.objExists(objectString):
        uniqueIds = cmds.ls(objectString, uuid=1)
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
def setMayaUniqueId(objectString, uniqueId=none):
    if cmds.objExists(objectString):
        if not uniqueId:
            uniqueId = getAttrUniqueId(objectString)
        if uniqueId:
            cmds.rename(objectString, uniqueId, uuid=1)


#
def setUniqueIdForce(objectString, uniqueId):
    if cmds.objExists(objectString):
        objectPaths = getObjects(uniqueId)
        if objectPaths:
            [cmds.rename(i, getUuid(), uuid=1) for i in objectPaths]
        #
        cmds.rename(objectString, uniqueId, uuid=1)


#
def setRefreshMayaUniqueId(sourceUniqueId, targetUniqueId):
    objectString = getObject(sourceUniqueId, fullPath=1)
    if objectString:
        setMayaUniqueId(objectString, targetUniqueId)


#
def isUniqueId(string):
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
