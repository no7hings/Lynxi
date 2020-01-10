# coding=utf-8
import collections
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxBasic import bscObjects
#
from LxMaya.command import maUtils
#
none = ''


#
def getControlHir(root):
    dic = collections.OrderedDict()
    def getChild(parent):
        children = maUtils.getNodeChildLis(parent, 1)
        if children:
            for child in children:
                if maUtils.getTransformType(child) == 'nurbsCurve':
                    dic.setdefault(parent, []).append(child)
                getChild(child)
    getChild(root)
    return dic


#
def getControls(root):
    typeFilter = 'nurbsCurve'
    typeFilters = maUtils._toStringList(typeFilter)
    return maUtils.getChildObjectsByRoot(root, typeFilters)


#
def getNamingOverlapping(root):
    lis = []
    def getChild(parent):
        children = maUtils.getNodeChildLis(parent, 1)
        if children:
            for child in children:
                childShortName = child.split('|')[-1]
                if maUtils.isNamingOverlapping(childShortName):
                    lis.append(child)
                getChild(child)
    getChild(root)
    return lis


#
def getKeyDataArray(objectString, attrName):
    indices = cmds.keyframe(
        objectString, query=True,
        attribute=attrName,
        keyframeCount=True)
    keyData = []
    for seq in range(indices):
        timeData = cmds.keyframe(
            objectString,
            query=True,
            attribute=attrName,
            index=(seq, seq),
            timeChange=True)
        if timeData:
            time = timeData[0]
            value = cmds.keyframe(
                objectString,
                query=True,
                attribute=attrName,
                index=(seq, seq),
                valueChange=True)[0]
            #
            inAngle = cmds.keyTangent(objectString, query=1, attribute=attrName, index=(seq, seq), inAngle=1)
            if inAngle:
                inAngle = inAngle[0]
            outAngle = cmds.keyTangent(objectString, query=1, attribute=attrName, index=(seq, seq), outAngle=1)
            if outAngle:
                outAngle = outAngle[0]
            inWeight = cmds.keyTangent(objectString, query=1, attribute=attrName, index=(seq, seq), inWeight=1)
            if inWeight:
                inWeight = inWeight[0]
            outWeight = cmds.keyTangent(objectString, query=1, attribute=attrName, index=(seq, seq), outWeight=1)
            if outWeight:
                outWeight = outWeight[0]
            inTangentType = cmds.keyTangent(objectString, query=1, attribute=attrName, index=(seq, seq), inTangentType=1)
            if inTangentType:
                inTangentType = inTangentType[0]
            outTangentType = cmds.keyTangent(objectString, query=1, attribute=attrName, index=(seq, seq), outTangentType=1)
            if outTangentType:
                outTangentType = outTangentType[0]
            #
            keyData.append((time, value, inAngle, outAngle, inWeight, outWeight, inTangentType, outTangentType))
    return keyData


#
def getKeyData(objectString, namespace=none):
    objectReduce = objectString
    #
    attrDataArray = []
    if namespace:
        objectReduce = objectString.replace(namespace + ':', none)
    keyableAttrs = maUtils.getKeyableAttr(objectString)
    if keyableAttrs:
        for attrName in keyableAttrs:
            animCurve = maUtils.getAnimCurve(objectString, attrName)
            if animCurve:
                keyDataArray = getKeyDataArray(objectString, attrName)
                if keyDataArray:
                    animCurveType = maUtils.getNodeType(animCurve)
                    preInfinity = maUtils.getAttrDatum(animCurve, 'preInfinity')
                    postInfinity = maUtils.getAttrDatum(animCurve, 'postInfinity')
                    attrDataArray.append((attrName, animCurve, animCurveType, (preInfinity, postInfinity), keyDataArray))
            if not animCurve:
                data = maUtils.getAttrDatum(objectString, attrName)
                attrDataArray.append((attrName, data))
    return objectReduce, attrDataArray


#
def getNumAttrKeyFrames(objectString):
    lis = []
    keyableAttrs = maUtils.getKeyableAttr(objectString)
    if keyableAttrs:
        for attrName in keyableAttrs:
            animCurve = maUtils.getAnimCurve(objectString, attrName)
            if animCurve:
                keyDataArray = getKeyDataArray(objectString, attrName)
                if keyDataArray:
                    animCurveType = maUtils.getNodeType(animCurve)
                    preInfinity = maUtils.getAttrDatum(animCurve, 'preInfinity')
                    postInfinity = maUtils.getAttrDatum(animCurve, 'postInfinity')
                    lis.append(
                        (attrName, animCurve, animCurveType, (preInfinity, postInfinity), keyDataArray))
            if not animCurve:
                data = maUtils.getAttrDatum(objectString, attrName)
                lis.append((attrName, data))
    #
    return lis


#
def getKeyDatas(root):
    lis = []
    maObjs = getControls(root)
    # View Progress
    progressExplain = '''Read Key(s)'''
    maxValue = len(maObjs)
    progressBar = bscObjects.If_Progress(progressExplain, maxValue)
    for objectString in maObjs:
        # In Progress
        progressBar.update(maUtils._toNodeName(objectString, 1))
        namespace = none
        if ':' in objectString:
            namespace = maUtils._toNamespaceByNodePath(objectString)
        keyData = getKeyData(objectString, namespace)
        lis.append(keyData)
    return lis


#
def setKey(objectString, attrData, seq, label='temp', frameOffset=0):
    if maUtils.isAppExist(objectString):
        if attrData:
            if len(attrData) == 5:
                attrName, animCurve, animCurveType, (preInfinity, postInfinity), keyDataArray = attrData
                objectName = objectString.split('|')[-1]
                inputAnimCurve = objectName + '_' + attrName + '_' + animCurveType + '_' + str(seq).zfill(4)
                sourceAttr = inputAnimCurve + '.output'
                targetAttr = objectString + '.' + attrName
                if maUtils.isAppExist(targetAttr):
                    #
                    if not maUtils.isAppExist(inputAnimCurve):
                        cmds.createNode(animCurveType, name=inputAnimCurve)
                    #
                    if not maUtils.isAttrDestination(targetAttr):
                        if not maUtils.isAttrConnected(sourceAttr, targetAttr):
                            maUtils.setAttrConnect(sourceAttr, targetAttr)
                    #
                    if keyDataArray:
                        for seq, keyData in enumerate(keyDataArray):
                            time, value, inAngle, outAngle, inWeight, outWeight, inTangentType, outTangentType = keyData
                            #
                            time += frameOffset
                            #
                            if value:
                                cmds.setKeyframe(
                                    objectString, attribute=attrName,
                                    time=(time, time),
                                    value=value)
                            #
                            if inAngle:
                                cmds.keyTangent(
                                    objectString, attribute=attrName,
                                    time=(time, time),
                                    inAngle=inAngle)
                            #
                            if outAngle:
                                cmds.keyTangent(
                                    objectString, attribute=attrName,
                                    time=(time, time),
                                    outAngle=outAngle)
                            #
                            if inWeight:
                                cmds.keyTangent(
                                    objectString, attribute=attrName,
                                    time=(time, time),
                                    inWeight=inWeight)
                            #
                            if outWeight:
                                cmds.keyTangent(
                                    objectString, attribute=attrName,
                                    time=(time, time),
                                    outWeight=outWeight)
                            #
                            if inTangentType:
                                cmds.keyTangent(
                                    objectString, attribute=attrName,
                                    time=(time, time),
                                    inTangentType=inTangentType)
                            #
                            if outTangentType:
                                cmds.keyTangent(
                                    objectString, attribute=attrName,
                                    time=(time, time),
                                    outTangentType=outTangentType)
                    #
                    maUtils.setAttrDatumForce_(inputAnimCurve, 'preInfinity', preInfinity)
                    maUtils.setAttrDatumForce_(inputAnimCurve, 'postInfinity', postInfinity)
            if len(attrData) == 2:
                attrName, data = attrData
                targetData = maUtils.getAttrDatum(objectString, attrName)
                if not maUtils.isAttrDestination(objectString, attrName):
                    if targetData != data:
                        maUtils.setKeyAttr(objectString, attrName, data)


#
def setKeys(root, keyDatas, frameOffset=0):
    if maUtils.isAppExist(root):
        namespace = none
        if ':' in root:
            namespace = root.split('|')[-1].split(':')[0]
        if keyDatas:
            progressExplain = '''Load Key'''
            maxValue = len(keyDatas)
            progressBar = bscObjects.If_Progress(progressExplain, maxValue)
            for seq, keyData in enumerate(keyDatas):
                # In Progress
                progressBar.update()
                if keyData:
                    objectString, attrDataArray = keyData
                    objectReduce = objectString
                    if namespace:
                        objectReduce = objectString.replace('|', '|' + namespace + ':')
                    if maUtils.isAppExist(objectReduce):
                        for attrData in attrDataArray:
                            setKey(objectReduce, attrData, seq, namespace, frameOffset)


#
def setKeyframeOffset(objectString, attrName, value):
    indexCount = cmds.keyframe(
        objectString, query=True,
        attribute=attrName, keyframeCount=True
    )
    if indexCount > 0:
        for seq in range(indexCount):
            keyDatum = cmds.keyframe(
                objectString,
                query=True,
                attribute=attrName,
                index=(seq, seq),
                timeChange=True, valueChange=True
            )
            if keyDatum:
                f, v = keyDatum
                v_ = v + value
                #
                cmds.setKeyframe(
                    objectString,
                    attribute=attrName,
                    time=(f, f),
                    value=v_
                )
    else:
        attr = objectString + '.' + attrName
        v = cmds.getAttr(attr)
        v_ = v + value
        cmds.setAttr(attr, v_)


#
def getRigInformationData(root):
    pass


#
def setTransferConnections(sourceObject, targetObject):
    sourceInputConnections = maUtils.getNodeInputConnectionLis(sourceObject)
    sourceOutputConnections = maUtils.getNodeOutputConnectionLis(sourceObject)
    #
    for sourceConnection, targetConnection in sourceInputConnections:
        attrName = '.'.join(targetConnection.split('.')[1:])
        newTargetConnection = targetObject + '.' + attrName
        cmds.connectAttr(sourceConnection, newTargetConnection, force=1)
    #
    for sourceConnection, targetConnection in sourceOutputConnections:
        attrName = '.'.join(sourceConnection.split('.')[1:])
        newSourceConnection = targetObject + '.' + attrName
        cmds.connectAttr(newSourceConnection, targetConnection, force=1)


#
def setBakeKeyframeByRoot(root, startFrame, endFrame, keyframeOffset=0):
    maObjs = getControls(root)
    if maObjs:
        maUtils.setObjectBakeKey(maObjs, startFrame, endFrame, keyframeOffset)