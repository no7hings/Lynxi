# encoding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxBasic import bscMtdCore,bscObjects
#
from LxMaya.command import maUtils
#
MaAttrTypes = [
    'message',
    'bool',
    'byte',
    'enum',
    'typed',
    'short',
    'float',
    'float3',
    'compound',
    'double',
    'time',
    'generic',
    'doubleLinear',
    'doubleAngle',
    'matrix',
    'long',
    'double3',
    'lightData',
    'addr',
    'float2',
    'double2',
    'double4',
    'fltMatrix',
    'char',
    'floatAngle',
    'floatLinear',
    'long3',
    'short2',
    'polyFaces',
    'long2'
]
#
MaUserAttrTypeDic = {
    'bool': 'attributeType',
    'byte': 'attributeType',
    'enum': 'attributeType',
    'typed': 'dataType',
    'short': 'attributeType',
    'float': 'attributeType',
    'double': 'attributeType',
    'time': 'attributeType',
    'doubleLinear': 'attributeType',
    'doubleAngle': 'attributeType',
    'long': 'attributeType',
    'char': 'attributeType'
}
#
MaAttrTypeLis_Readable = [
    'bool',
    'byte',
    'enum',
    'string',
    'short',
    'float',
    'double',
    'time',
    'doubleLinear',
    'doubleAngle',
    'matrix',
    'long',
    'lightData',
    'addr',
    'fltMatrix',
    'char',
    'floatAngle',
    'floatLinear'
]
#
MaAttrNameLis_ShaderExcept = [
    'computedFileTextureNamePattern',
    'expression'
]
#
MaAttrNameDic_Convert = {
    'internalExpression': 'expression'
}
#
MaAttrTypeLis_NonDefaultValue = [
    'string'
]
#
bugAttrNames = [
    'anisotropy_orientation'
]
#
MaCommonRenderAttrNameLis = [
    'castsShadows',
    'receiveShadows',
    'holdOut',
    'motionBlur',
    'primaryVisibility',
    'smoothShading',
    'visibleInReflections',
    'visibleInRefractions',
    'doubleSided',
    'opposite',
    'geometryAntialiasingOverride',
    'antialiasingLevel',
    'shadingSamplesOverride',
    'shadingSamples',
    'maxShadingSamples'
]
#
MaCommonRenderEnableAttrNameLis = [
    'castsShadows',
    'receiveShadows',
    'motionBlur',
    'primaryVisibility',
    'smoothShading',
    'visibleInReflections',
    'visibleInRefractions',
    'doubleSided',
    'opposite',
]
#
MaCommonArnoldRenderEnableAttrNameLis = [
    'aiOpaque',
    'aiMatte',
    'primaryVisibility',
    'castsShadows',
    'aiVisibleInDiffuseReflection',
    'aiVisibleInSpecularReflection',
    'aiVisibleInDiffuseTransmission',
    'aiVisibleInSpecularTransmission',
    'aiVisibleInVolume',
    'aiSelfShadows',
]
#
MaObjectDisplayAttrNameLis = [
    'visibility',
    'template',
    'lodVisibility',
    'hideOnPlayback',
    'hiddenInOutliner',
    'useOutlinerColor',
    'outlinerColor'
]
#
none = ''


#
def _getAttributeQueryNameString(attrName):
    guessName = attrName.split('.')[-1]
    attrName = guessName
    if guessName.endswith(']'):
        attrName = guessName.split('[')[0]
    return attrName


#
def getAttrType(attr):
    attrType = cmds.getAttr(attr, type=1)
    return attrType


#
def getAttrDefaultValueLis(node, attrName, attrType):
    defaultValues = []
    if not attrType in MaAttrTypeLis_NonDefaultValue:
        attrQueryName = _getAttributeQueryNameString(attrName)
        guessData = cmds.attributeQuery(attrQueryName, node=node, listDefault=1)
        if guessData:
            defaultValues = guessData
    return defaultValues


#
def isAttrExists(node, attrQueryName):
    return cmds.attributeQuery(attrQueryName, node=node, exists=1)


#
def isAttrHasMaximum(node, attrName):
    attrQueryName = _getAttributeQueryNameString(attrName)
    if isAttrExists(node, attrQueryName):
        return cmds.attributeQuery(attrQueryName, node=node, maxExists=1)


#
def isAttrHasMinimum(node, attrName):
    attrQueryName = _getAttributeQueryNameString(attrName)
    if isAttrExists(node, attrQueryName):
        return cmds.attributeQuery(attrQueryName, node=node, minExists=1)


#
def getAttrMaximum(node, attrName):
    value = 1
    attrQueryName = _getAttributeQueryNameString(attrName)
    values = cmds.attributeQuery(attrQueryName, node=node, maximum=1)
    if values:
        value = max(values)
    return value


#
def getAttrMinimum(node, attrName):
    value = 0
    attrQueryName = _getAttributeQueryNameString(attrName)
    values = cmds.attributeQuery(attrQueryName, node=node, minimum=1)
    if values:
        value = min(values)
    return value


#
def isAttrDestination(attr):
    return cmds.connectionInfo(attr, isDestination=1)


#
def isAttrExactDestination(attr):
    return cmds.connectionInfo(attr, isExactDestination=1)


#
def isAttrSource(attr):
    return cmds.connectionInfo(attr, isSource=1)


#
def isAttrSettable(attr):
    return cmds.getAttr(attr, settable=1)


#
def isAttrKeyable(attr):
    return cmds.getAttr(attr, keyable=1)


#
def isAttrLocked(attr):
    return cmds.getAttr(attr, lock=1)


#
def setAttrKeyable(attr, boolean):
    cmds.setAttr(attr, keyable=boolean)


#
def setAttrLocked(attr, boolean):
    cmds.setAttr(attr, lock=boolean)


#
def getNodeAttrDatum(nodeString, attrName):
    tup = ()
    if not attrName in MaAttrNameLis_ShaderExcept:
        attr = nodeString + '.' + attrName
        attrType = getAttrType(attr)
        if attrType in MaAttrTypeLis_Readable:
            # Filter Exists
            if cmds.objExists(attr):
                # Debug ( Filter Connected is Unused with Mult Attribute )
                if not isAttrExactDestination(attr):
                    value = cmds.getAttr(attr)
                    if value is not None:
                        # Value
                        if value is True:
                            value = 1
                        elif value is False:
                            value = 0
                        # Lock
                        lock = isAttrLocked(attr)
                        if lock is True:
                            lock = 1
                        elif lock is False:
                            lock = 0
                        # Filter Default Value
                        defaultValues = getAttrDefaultValueLis(nodeString, attrName, attrType)
                        # Debug ( Error Attr )
                        isBugAttrName = attrName in bugAttrNames
                        if isBugAttrName:
                            if attrName == 'anisotropy_orientation':
                                if value == 0:
                                    value = 2
                        #
                        if not value in defaultValues:
                            tup = attrName, value, attrType, lock
                        else:
                            if attrName.endswith('_Position') or attrName.endswith('_FloatValue') or attrName.endswith('_Interp'):
                                tup = attrName, value, attrType, lock
    return tup


#
def getNodeAttrDatumLis(nodeString, attrNames):
    lis = []
    #
    if attrNames:
        for attrName in attrNames:
            attrData = getNodeAttrDatum(nodeString, attrName)
            if attrData:
                lis.append(attrData)
    return lis


#
def getAttrDataForce(nodeString, attrName):
    tup = ()
    if not attrName in MaAttrNameLis_ShaderExcept:
        attr = nodeString + '.' + attrName
        attrType = getAttrType(attr)
        if attrType in MaAttrTypeLis_Readable:
            # Filter Exists
            if cmds.objExists(attr):
                value = cmds.getAttr(attr)
                lock = isAttrLocked(attr)
                #
                if value is True:
                    value = 1
                elif value is False:
                    value = 0
                if lock is True:
                    lock = 1
                elif lock is False:
                    lock = 0
                #
                tup = attrName, value, attrType, lock
    return tup


#
def getAttrDataLisForce(nodeString, attrNames):
    lis = []
    #
    if attrNames:
        for attrName in attrNames:
            attrData = getAttrDataForce(nodeString, attrName)
            if attrData:
                lis.append(attrData)
    return lis


#
def getNodeDefAttrNameLis(nodeString):
    return cmds.listAttr(nodeString, read=1, write=1, inUse=1, multi=1) or []


#
def getNodeAttrLis(nodeString):
    return cmds.listAttr(nodeString) or []


#
def getNodeDefAttrDatumLis(nodeString):
    attrNameLis = getNodeDefAttrNameLis(nodeString)
    return getNodeAttrDatumLis(nodeString, attrNameLis)


#
def getNodeUserDefAttrNameLis(nodeString):
    return cmds.listAttr(nodeString, userDefined=1) or []


#
def getNodeUserDefAttrData(nodeString):
    attrNameLis = getNodeUserDefAttrNameLis(nodeString)
    return getAttrDataLisForce(nodeString, attrNameLis)


#
def getObjectDisplayAttrData(objectString):
    attrNameLis = MaObjectDisplayAttrNameLis
    return getNodeAttrDatumLis(objectString, attrNameLis)


#
def getNodePlugAttrData(nodeString):
    attrNameLis = cmds.listAttr(nodeString, read=1, write=1, fromPlugin=1)
    return getAttrDataLisForce(nodeString, attrNameLis)


#
def setNodeUnrenderable(nodeString):
    def setBranch(attrNames):
        for attrName in attrNames:
            attr = nodeString + '.' + attrName
            if cmds.objExists(attr):
                cmds.setAttr(attr, 0)
    #
    setBranch(MaCommonRenderEnableAttrNameLis)
    setBranch(MaCommonArnoldRenderEnableAttrNameLis)


#
def getNodeRenderAttrData(nodeString):
    return getAttrDataLisForce(nodeString, MaCommonRenderAttrNameLis)


# Set nodeString Attribute Main Method
def setAttrStringDatum(nodeString, attrName, attrType, data, lock, lockAttribute):
    if attrName in MaAttrNameDic_Convert:
        attrName = MaAttrNameDic_Convert[attrName]
    #
    attr = nodeString + '.' + attrName
    if cmds.objExists(attr):
        if not isAttrDestination(attr):
            # Filter String
            isString = attrType == 'string'
            isMatrix = attrType == 'matrix'
            #
            if cmds.connectionInfo(attr, isLocked=1):
                cmds.setAttr(attr, lock=0)
            #
            if isString:
                if data is not None:
                    cmds.setAttr(attr, data, type='string')
            elif isMatrix:
                cmds.setAttr(attr, data, type='matrix')
            #
            else:
                # Debug ( Clamp Maximum or Minimum Value )
                cmds.setAttr(attr, data, clamp=1)
            # Lock Attr
            if lockAttribute:
                cmds.setAttr(attr, lock=lock)


#
def setNodeCompoundAttrClear(nodeString):
    compoundAttrNameLis = []
    attrNameLis = cmds.listAttr(nodeString)
    if attrNameLis:
        for attrName in attrNameLis:
            if attrName.endswith('_Position') or attrName.endswith('_FloatValue') or attrName.endswith('_Interp'):
                mainAttrName = attrName.split('.')[0]
                if not mainAttrName in compoundAttrNameLis:
                    compoundAttrNameLis.append(mainAttrName)
    #
    if compoundAttrNameLis:
        for compoundAttrName in compoundAttrNameLis:
            for i in range(5):
                attrName = '{}[{}]'.format(compoundAttrName, i)
                attr = nodeString + '.' + attrName
                if cmds.objExists(attr):
                    cmds.removeMultiInstance(attr)
                    print '// Result : Remove Attr > {} //'.format(attr)


#
def setNodeDefAttrByData(nodeString, attrDataArray, lockAttribute=True):
    colorAttrDic = {}
    #
    if attrDataArray:
        setNodeCompoundAttrClear(nodeString)
        #
        for attrData in attrDataArray:
            if attrData:
                attrName, value, attrType, lock = attrData
                if not attrName in MaAttrNameLis_ShaderExcept:
                    setAttrStringDatum(nodeString, attrName, attrType, value, lock, lockAttribute)
                # Color
                if attrName.endswith('R') or attrName.endswith('G') or attrName.endswith('B'):
                    mainAttr = attrName[:-1]
                    colorAttrDic.setdefault(mainAttr, []).append(value)
        #
        if colorAttrDic:
            for k, v in colorAttrDic.items():
                if len(v) == 3:
                    attrName = k
                    attr = nodeString + '.' + attrName
                    if not isAttrDestination(attr):
                        if cmds.objExists(attr):
                            cmds.setAttr(attr, *v, type='float3')


#
def setObjectUserDefinedAttrs(nodeString, attrDataArray, lockAttribute=True):
    for attrData in attrDataArray:
        if attrData:
            attrName, data, attrType, lock = attrData
            attr = nodeString + '.' + attrName
            # Filter String
            isString = attrType == 'string'
            if not cmds.objExists(attr):
                if isString:
                    cmds.addAttr(nodeString, longName=attrName, dataType='string')
                elif not isString:
                    cmds.addAttr(nodeString, longName=attrName, attributeType=attrType)
            #
            setAttrStringDatum(nodeString, attrName, attrType, data, lock, lockAttribute)


#
def getNodeConnectionsDataArray(nodeString):
    connectionArray = []
    connections = cmds.listConnections(nodeString, destination=0, source=1, connections=1, plugs=1)
    if connections:
        for seq, connection in enumerate(connections):
            if seq % 2:
                sourceAttr = connection
                targetAttr = connections[seq - 1]
                connectionArray.append((sourceAttr, targetAttr))
    return connectionArray


#
def getObjectConnectionDataArray(maObj):
    if maUtils._getNodeIsTransform(maObj):
        nodeString = maUtils._getNodeShapeNodeString(maObj)
    else:
        nodeString = maObj
    return getNodeConnectionsDataArray(nodeString)


#
def setCreateConnections(connections):
    if connections:
        for sourceAttr, targetAttr in connections:
            # Filter Exists
            if maUtils._isAppExist(sourceAttr) and maUtils._isAppExist(targetAttr):
                # Filter Connected
                if not maUtils.isAttrConnected(sourceAttr, targetAttr):
                    cmds.connectAttr(sourceAttr, targetAttr, force=1)


#
def getConnectionFilterByNamespace(namespace):
    lis = []
    nodes = maUtils.getDependNodesByNamespace(namespace)
    if nodes:
        nodes.sort()
        for node in nodes:
            inputConnections = maUtils.getInputConnectionsFilterByNamespace(
                node, namespace
            )
            if inputConnections:
                lis.extend(inputConnections)
            #
            outputConnections = maUtils.getOutputConnectionsFilterByNamespace(
                node, namespace
            )
            if outputConnections:
                lis.extend(outputConnections)
    return lis


#
def setConnectionsReconnect(connections):
    lis = []
    if connections:
        explain = '''Connect Attribute(s)'''
        maxValue = len(connections)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for sourceAttr, targetAttr in connections:
            progressBar.update()
            # Filter Exists
            if maUtils._isAppExist(sourceAttr) and maUtils._isAppExist(targetAttr):
                # Filter Connected
                if not maUtils.isAttrConnected(sourceAttr, targetAttr):
                    if not maUtils.isAttrSource(sourceAttr):
                        cmds.connectAttr(sourceAttr, targetAttr, force=1)
                        lis.append((sourceAttr, targetAttr))
    return lis


#
def setDelAttrs(node, attrNames):
    if not maUtils.isNodeLocked(node):
        for attrName in attrNames:
            attr = node + '.' + attrName
            if maUtils._isAppExist(attr):
                if not maUtils.isReferenceNode(attr):
                    cmds.deleteAttr(attr)


#
def setNodeAttrTransfer(sourceNode, targetNode):
    sourceAttrData = getNodeDefAttrDatumLis(sourceNode)
    if sourceAttrData:
        for attrData in sourceAttrData:
            attrName, value, attrType, lock = attrData
            if not attrName in MaAttrNameLis_ShaderExcept:
                setAttrStringDatum(targetNode, attrName, attrType, value, lock, lockAttribute=False)


#
def setNodeRenderAttrTransfer(sourceNode, targetNode):
    attrDatumLis = getNodeRenderAttrData(sourceNode)
    if attrDatumLis:
        for attrDatum in attrDatumLis:
            attrName, value, attrType, lock = attrDatum
            setAttrStringDatum(targetNode, attrName, attrType, value, lock, lockAttribute=False)


#
def setNodePlugAttrTransfer(sourceNode, targetNode):
    attrDatumLis = getNodePlugAttrData(sourceNode)
    if attrDatumLis:
        for attrDatum in attrDatumLis:
            attrName, value, attrType, lock = attrDatum
            setAttrStringDatum(targetNode, attrName, attrType, value, lock, lockAttribute=False)
