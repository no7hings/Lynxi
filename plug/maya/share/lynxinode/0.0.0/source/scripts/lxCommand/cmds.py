# encoding=utf-8
import math
#
import json
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.api.OpenMaya as OpenMaya
#
CtomAttrName = 'curveToMesh'
CtomMeshName = 'ctom_mesh_0'
CtomMeshGroupName = 'ctom_mesh_grp_0'
#
MtosAttrName = 'meshToSurface'
MtosSurfaceName = 'mtos_surface_0'
MtosSurfaceGroupName = 'mtos_surface_grp_0'


#
def setMeshCreateByCurve(isAutoVDvn=True):
    cmds.loadPlugin('lxConvertNode', quiet=1)
    #
    meshObjects = []
    selCurves = cmds.ls(type='nurbsCurve', selection=1, dagObjects=1, noIntermediate=1, long=1)
    if selCurves:
        for curve in selCurves:
            ts = cmds.listRelatives(curve, parent=1, fullPath=1)
            transform = ts[0]
            ctomAttr = transform + '.' + CtomAttrName
            nodeAttrDic = {}
            if cmds.objExists(ctomAttr):
                attrData = cmds.getAttr(ctomAttr)
                nodeAttrDic = json.loads(attrData)
            node, mesh = setCreateCtomCmd(curve)
            if isAutoVDvn is True:
                setAutoVDivision(node, curve)
            #
            if nodeAttrDic:
                setCtomNodeAttrs(node, mesh, nodeAttrDic)
            #
            meshObjects.append(mesh)
    #
    if len(meshObjects) > 1:
        group = cmds.group(empty=1, name=CtomMeshGroupName)
        cmds.parent(meshObjects, group)
        #
        setOutlinerColor(group, 1, .5, .25)


#
def setSurfaceCreateByMesh():
    cmds.loadPlugin('lxConvertNode', quiet=1)
    surfaces = []
    selMeshes = cmds.ls(type='mesh', selection=1, dagObjects=1, noIntermediate=1, long=1)
    if selMeshes:
        for mesh in selMeshes:
            node, surface = setCreateMtosCmd(mesh)
            surfaces.append(surface)
    #
    if len(surfaces):
        group = cmds.group(empty=1, name=MtosSurfaceGroupName)
        cmds.parent(surfaces, group)
        #
        setOutlinerColor(group, 1, .5, .25)


#
def setOutlinerColor(maObj, r, g, b):
    cmds.setAttr(maObj + '.useOutlinerColor', 1)
    cmds.setAttr(maObj + '.outlinerColor', r, g, b)


#
def getRealAngle(angle):
    r = angle % 180
    if r > 0:
        if r > 90:
            angle_ = r - 180
        else:
            angle_ = r
    else:
        angle_ = r
    return angle_


#
def setCtomNodeAttrs(node, mesh, nodeAttrDic):
    ribbonMesh = nodeAttrDic['ribbonMesh']
    orientationAttr = ribbonMesh + '.' + 'orientation'
    orientation = cmds.getAttr(orientationAttr)
    cmds.setAttr(orientationAttr, 1)
    differAngle = getDifferAngle(ribbonMesh, mesh)
    cmds.setAttr(orientationAttr, orientation)
    for k, v in nodeAttrDic.items():
        attr = node + '.' + k
        if cmds.objExists(attr):
            # Fix Spin
            if k == 'spin':
                r = (v + differAngle) % 180
                if r > 0:
                    if r > 90:
                        v_ = r - 180
                    else:
                        v_ = r
                else:
                    v_ = r
                #
                v = v_
            #
            cmds.setAttr(attr, v)


#
def setCreateCtomCmd(curve):
    node = setCreateCtomNode(curve)
    mesh = setCreateCtomMesh(node)
    return node, mesh


#
def setCreateMtosCmd(mesh):
    node = setCreateMtosNode(mesh)
    surface = setCreateMtosSurface(node)
    return node, surface


#
def setCreateCtomNode(curve):
    existsNodes = cmds.listConnections(curve, destination=1, source=0, type='curveToMesh', shapes=1)
    if not existsNodes:
        node = cmds.createNode('curveToMesh')
        setInitCtomNode(node)
        #
        outputAttr = curve + '.worldSpace[0]'
        inputAttr = node + '.inputCurve'
        cmds.connectAttr(outputAttr, inputAttr)
    else:
        node = existsNodes[0]
    return node


#
def setCreateCtomMesh(node):
    existsMeshes = cmds.listConnections(node, destination=1, source=0, type='mesh', shapes=1)
    if not existsMeshes:
        meshCreate = cmds.polyPlane(name=CtomMeshName, constructionHistory=0)
        mesh = meshCreate[0]
        outputAttr = node + '.outputMesh'
        inputAttr = mesh + '.inMesh'
        cmds.connectAttr(outputAttr, inputAttr)
        #
        setOutlinerColor(mesh, .25, 1, .5)
    else:
        mesh = existsMeshes[0]
    #
    setAddToModelPanel(mesh)
    return mesh


#
def setCreateMtosNode(mesh):
    existsNodes = cmds.listConnections(mesh, destination=1, source=0, type='meshToSurface', shapes=1)
    if not existsNodes:
        node = cmds.createNode('meshToSurface')
        setInitMtosNode(node)
        #
        outputAttr = mesh + '.outMesh'
        inputAttr = node + '.inputMesh'
        cmds.connectAttr(outputAttr, inputAttr)
    else:
        node = existsNodes[0]
    return node


#
def setCreateMtosSurface(node):
    existsSurfaces = cmds.listConnections(node, destination=1, source=0, type='surface', shapes=1)
    if not existsSurfaces:
        surfaceCreate = cmds.nurbsPlane(name=MtosSurfaceName, constructionHistory=0)
        surface = surfaceCreate[0]
        outputAttr = node + '.outputSurface'
        inputAttr = surface + '.create'
        cmds.connectAttr(outputAttr, inputAttr)
        #
        setOutlinerColor(surface, .25, 1, .5)
    else:
        surface = existsSurfaces[0]
    #
    setAddToModelPanel(surface)
    return surface


#
def getCtomCurve(node):
    existsCurves = cmds.listConnections(node, destination=0, source=1, type='nurbsCurve', shapes=1)
    if existsCurves:
        return existsCurves[0]


#
def getMtosMesh(node):
    existsMeshes = cmds.listConnections(node, destination=0, source=1, type='mesh', shapes=1)
    if existsMeshes:
        return existsMeshes[0]


#
def setResetCtomNodeModify(node):
    resetDic = {
        'spin': 0,
        'twist': 0,
        'taper': 1,
        'arch': 0,
        'minPercent': 0,
        'maxPercent': 1
    }
    for k, v in resetDic.items():
        attr = node + '.' + k
        cmds.setAttr(attr, v)


#
def setAutoVDivision(node, curve):
    mCurvePath = OpenMaya.MGlobal.getSelectionListByName(curve).getDagPath(0)
    mCurve = OpenMaya.MFnNurbsCurve(mCurvePath)
    sample = cmds.getAttr(node + '.sample')
    length = mCurve.length()
    count = int(length * sample)
    vDivision = 2**int(math.log(count, 2))
    cmds.setAttr(node + '.vDivision', vDivision)


#
def setAddToModelPanel(maObj):
    cmds.isolateSelect('modelPanel4', addDagObject=maObj)


#
def setInitCtomNode(node):
    cmds.setAttr(node + '.widthExtra[0].widthExtra_Position', 0)
    cmds.setAttr(node + '.widthExtra[0].widthExtra_FloatValue', 0.5)
    cmds.setAttr(node + '.widthExtra[1].widthExtra_Position', 1)
    cmds.setAttr(node + '.widthExtra[1].widthExtra_FloatValue', 0.5)
    #
    cmds.setAttr(node + '.spinExtra[0].spinExtra_Position', 0)
    cmds.setAttr(node + '.spinExtra[0].spinExtra_FloatValue', .5)
    cmds.setAttr(node + '.spinExtra[1].spinExtra_Position', 1)
    cmds.setAttr(node + '.spinExtra[1].spinExtra_FloatValue', .5)
    #
    cmds.setAttr(node + '.angleOffset[0].angleOffset_Position', 0)
    cmds.setAttr(node + '.angleOffset[0].angleOffset_FloatValue', .5)
    cmds.setAttr(node + '.angleOffset[1].angleOffset_Position', 1.0)
    cmds.setAttr(node + '.angleOffset[1].angleOffset_FloatValue', .5)


#
def setInitMtosNode(node):
    pass


#
def setCreateByBonusCurve():
    group = setCopyBonusCurve()
    if group:
        cmds.select(group)
        setMeshCreateByCurve()


#
def getDifferAngle(mesh1, mesh2):
    def toM2Vector(mesh, vertexId1, vertexId2):
        mMeshPath = OpenMaya.MGlobal.getSelectionListByName(mesh).getDagPath(0)
        mMesh = OpenMaya.MFnMesh(mMeshPath)
        #
        p1, p2 = mMesh.getPoint(vertexId1, space=4), mMesh.getPoint(vertexId2, space=4)
        mVector = OpenMaya.MVector()
        mVector.x, mVector.y, mVector.z = (p2.x - p1.x), (p2.y - p1.y), (p2.z - p1.z)
        return mVector
    #
    iVector1 = toM2Vector(mesh1, 0, 1)
    iVector2 = toM2Vector(mesh2, 0, 1)
    #
    axisAngle = iVector2.rotateTo(iVector1).asAxisAngle()
    x = iVector2.x
    a = math.degrees(axisAngle[1])
    if x < 0:
        return -a
    elif x >= 0:
        return a


#
def getBonusCurveDic():
    attrNames = [
        'width',
        'orientation',
        'taper',
        'twist',
        'lengthDivisions'
    ]
    #
    dic = {}
    ribbonMeshes = []
    selCurves = cmds.ls(type='nurbsCurve', selection=1, dagObjects=1)
    if selCurves:
        for c in selCurves:
            t = cmds.listRelatives(c, parent=1, fullPath=1)
            css = cmds.listConnections(t, destination=1, source=0, type='orientConstraint', shapes=1)
            if css:
                for cs in css:
                    ms = cmds.listConnections(cs, destination=1, source=0, type='transform', shapes=1)
                    if ms:
                        ribbonMesh = ms[0]
                        attrDatas = []
                        for a in attrNames:
                            attr = ribbonMesh + '.' + a
                            attrData = cmds.getAttr(attr)
                            attrDatas.append(attrData)
                        #
                        attrDatas.append(ribbonMesh)
                        #
                        if not ribbonMesh in ribbonMeshes:
                            dic.setdefault(c, []).append(attrDatas)
                        #
                        ribbonMeshes.append(ribbonMesh)
    #
    return dic


#
def setCopyBonusCurve():
    attrNames = [
        'width',
        'spin',
        'taper',
        'twist',
        'vDivision',
        'ribbonMesh'
    ]
    #
    dic = getBonusCurveDic()
    copyCurves = []
    if dic:
        for k, v in dic.items():
            for seq, i in enumerate(v):
                ts = cmds.listRelatives(k, parent=1, fullPath=1)
                transform = ts[0]
                copyPath = '|'.join(transform.split('|')[:-1])
                copyCurveName = transform.split('|')[-1] + '_copy_%s' % seq
                copyCurvePath = copyPath + '|' + copyCurveName
                if not cmds.objExists(copyCurveName):
                    cmds.duplicate(transform, name=copyCurveName, returnRootsOnly=1)
                    #
                    cmds.addAttr(copyCurvePath, longName=CtomAttrName, dataType='string')
                    #
                    nodeAttrDic = {}
                    for subSeq, j in enumerate(i):
                        nodeAttrDic[attrNames[subSeq]] = j
                    #
                    cmds.setAttr(copyCurvePath + '.' + CtomAttrName, json.dumps(nodeAttrDic), type='string')
                #
                copyCurves.append(copyCurvePath)
    #
    if copyCurves:
        group = cmds.group(empty=1, name='ctom_curve_copy_grp_0')
        cmds.parent(copyCurves, group)
        return group
