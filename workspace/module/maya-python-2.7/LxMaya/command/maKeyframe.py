# coding=utf-8
import collections
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxBasic import bscObjects, bscMethods
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
    typeFilters = bscMethods.String.toList(typeFilter)
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
def getKeyDataArray(nodepathString, attrName):
    indices = cmds.keyframe(
        nodepathString, query=True,
        attribute=attrName,
        keyframeCount=True
    )
    keyData = []
    for seq in range(indices):
        timeData = cmds.keyframe(
            nodepathString,
            query=True,
            attribute=attrName,
            index=(seq, seq),
            timeChange=True)
        if timeData:
            time = timeData[0]
            value = cmds.keyframe(
                nodepathString,
                query=True,
                attribute=attrName,
                index=(seq, seq),
                valueChange=True)[0]
            #
            inAngle = cmds.keyTangent(nodepathString, query=1, attribute=attrName, index=(seq, seq), inAngle=1)
            if inAngle:
                inAngle = inAngle[0]
            outAngle = cmds.keyTangent(nodepathString, query=1, attribute=attrName, index=(seq, seq), outAngle=1)
            if outAngle:
                outAngle = outAngle[0]
            inWeight = cmds.keyTangent(nodepathString, query=1, attribute=attrName, index=(seq, seq), inWeight=1)
            if inWeight:
                inWeight = inWeight[0]
            outWeight = cmds.keyTangent(nodepathString, query=1, attribute=attrName, index=(seq, seq), outWeight=1)
            if outWeight:
                outWeight = outWeight[0]
            inTangentType = cmds.keyTangent(nodepathString, query=1, attribute=attrName, index=(seq, seq), inTangentType=1)
            if inTangentType:
                inTangentType = inTangentType[0]
            outTangentType = cmds.keyTangent(nodepathString, query=1, attribute=attrName, index=(seq, seq), outTangentType=1)
            if outTangentType:
                outTangentType = outTangentType[0]
            #
            keyData.append((time, value, inAngle, outAngle, inWeight, outWeight, inTangentType, outTangentType))
    return keyData


#
def getKeyData(nodepathString, namespace=none):
    objectReduce = nodepathString
    #
    attrDataArray = []
    if namespace:
        objectReduce = nodepathString.replace(namespace + ':', none)
    keyableAttrs = maUtils.getKeyableAttr(nodepathString)
    if keyableAttrs:
        for attrName in keyableAttrs:
            animCurve = maUtils.getAnimCurve(nodepathString, attrName)
            if animCurve:
                keyDataArray = getKeyDataArray(nodepathString, attrName)
                if keyDataArray:
                    animCurveType = maUtils._getNodeCategoryString(animCurve)
                    preInfinity = maUtils.getAttrDatum(animCurve, 'preInfinity')
                    postInfinity = maUtils.getAttrDatum(animCurve, 'postInfinity')
                    attrDataArray.append((attrName, animCurve, animCurveType, (preInfinity, postInfinity), keyDataArray))
            if not animCurve:
                data = maUtils.getAttrDatum(nodepathString, attrName)
                attrDataArray.append((attrName, data))
    return objectReduce, attrDataArray


#
def getNumAttrKeyFrames(nodepathString):
    lis = []
    keyableAttrs = maUtils.getKeyableAttr(nodepathString)
    if keyableAttrs:
        for attrName in keyableAttrs:
            animCurve = maUtils.getAnimCurve(nodepathString, attrName)
            if animCurve:
                keyDataArray = getKeyDataArray(nodepathString, attrName)
                if keyDataArray:
                    animCurveType = maUtils._getNodeCategoryString(animCurve)
                    preInfinity = maUtils.getAttrDatum(animCurve, 'preInfinity')
                    postInfinity = maUtils.getAttrDatum(animCurve, 'postInfinity')
                    lis.append(
                        (attrName, animCurve, animCurveType, (preInfinity, postInfinity), keyDataArray))
            if not animCurve:
                data = maUtils.getAttrDatum(nodepathString, attrName)
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
    progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
    for nodepathString in maObjs:
        # In Progress
        progressBar.update(maUtils._nodeString2nodename_(nodepathString, 1))
        namespace = none
        if ':' in nodepathString:
            namespace = maUtils._toNamespaceByNodePath(nodepathString)
        keyData = getKeyData(nodepathString, namespace)
        lis.append(keyData)
    return lis


#
def setKey(nodepathString, attrData, seq, label='temp', frameOffset=0):
    if maUtils._isAppExist(nodepathString):
        if attrData:
            if len(attrData) == 5:
                attrName, animCurve, animCurveType, (preInfinity, postInfinity), keyDataArray = attrData
                objectName = nodepathString.split('|')[-1]
                inputAnimCurve = objectName + '_' + attrName + '_' + animCurveType + '_' + str(seq).zfill(4)
                sourceAttr = inputAnimCurve + '.output'
                targetAttr = nodepathString + '.' + attrName
                if maUtils._isAppExist(targetAttr):
                    #
                    if not maUtils._isAppExist(inputAnimCurve):
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
                                    nodepathString, attribute=attrName,
                                    time=(time, time),
                                    value=value)
                            #
                            if inAngle:
                                cmds.keyTangent(
                                    nodepathString, attribute=attrName,
                                    time=(time, time),
                                    inAngle=inAngle)
                            #
                            if outAngle:
                                cmds.keyTangent(
                                    nodepathString, attribute=attrName,
                                    time=(time, time),
                                    outAngle=outAngle)
                            #
                            if inWeight:
                                cmds.keyTangent(
                                    nodepathString, attribute=attrName,
                                    time=(time, time),
                                    inWeight=inWeight)
                            #
                            if outWeight:
                                cmds.keyTangent(
                                    nodepathString, attribute=attrName,
                                    time=(time, time),
                                    outWeight=outWeight)
                            #
                            if inTangentType:
                                cmds.keyTangent(
                                    nodepathString, attribute=attrName,
                                    time=(time, time),
                                    inTangentType=inTangentType)
                            #
                            if outTangentType:
                                cmds.keyTangent(
                                    nodepathString, attribute=attrName,
                                    time=(time, time),
                                    outTangentType=outTangentType)
                    #
                    maUtils.setAttrDatumForce_(inputAnimCurve, 'preInfinity', preInfinity)
                    maUtils.setAttrDatumForce_(inputAnimCurve, 'postInfinity', postInfinity)
            if len(attrData) == 2:
                attrName, data = attrData
                targetData = maUtils.getAttrDatum(nodepathString, attrName)
                if not maUtils.isAttrDestination(nodepathString, attrName):
                    if targetData != data:
                        maUtils.setKeyAttr(nodepathString, attrName, data)


#
def setKeys(root, keyDatas, frameOffset=0):
    if maUtils._isAppExist(root):
        namespace = none
        if ':' in root:
            namespace = root.split('|')[-1].split(':')[0]
        if keyDatas:
            progressExplain = '''Load Key'''
            maxValue = len(keyDatas)
            progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
            for seq, keyData in enumerate(keyDatas):
                # In Progress
                progressBar.update()
                if keyData:
                    nodepathString, attrDataArray = keyData
                    objectReduce = nodepathString
                    if namespace:
                        objectReduce = nodepathString.replace('|', '|' + namespace + ':')
                    if maUtils._isAppExist(objectReduce):
                        for attrData in attrDataArray:
                            setKey(objectReduce, attrData, seq, namespace, frameOffset)


#
def setKeyframeOffset(nodepathString, attrName, value):
    indexCount = cmds.keyframe(
        nodepathString, query=True,
        attribute=attrName, keyframeCount=True
    )
    if indexCount > 0:
        for seq in range(indexCount):
            keyDatum = cmds.keyframe(
                nodepathString,
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
                    nodepathString,
                    attribute=attrName,
                    time=(f, f),
                    value=v_
                )
    else:
        attr = nodepathString + '.' + attrName
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