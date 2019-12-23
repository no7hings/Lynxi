# coding=utf-8
import collections
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxMaya.command import maUtils


#
def setReduce(meshObject, percentage):
    cmds.polyReduce(
        meshObject,
        version=1,
        termination=0,
        percentage=percentage,
        symmetryPlaneX=0,
        symmetryPlaneY=1,
        symmetryPlaneZ=0,
        symmetryPlaneW=0,
        keepQuadsWeight=0,
        vertexCount=0,
        triangleCount=0,
        sharpness=0,
        keepColorBorder=0,
        keepFaceGroupBorder=0,
        keepHardEdge=1,
        keepCreaseEdge=1,
        keepBorderWeight=0.5,
        keepMapBorderWeight=1,
        keepColorBorderWeight=0.5,
        keepFaceGroupBorderWeight=0.5,
        keepHardEdgeWeight=0.5,
        keepCreaseEdgeWeight=0.5,
        useVirtualSymmetry=0,
        symmetryTolerance=0.01,
        vertexMapName='',
        replaceOriginal=1,
        cachingReduce=1,
        constructionHistory=0
    )
    cmds.polyTriangulate(meshObject, constructionHistory=0)
    cmds.delete(meshObject, constructionHistory=1)
    cmds.select(clear=1)


#
def setMeshesReduce(meshObjects, percentage):
    # View Progress
    progressExplain = '''Reducing Mesh'''
    maxValue = len(meshObjects)
    progressBar = maUtils.MaProgressBar().viewProgress(progressExplain, maxValue)
    for mesh in meshObjects:
        progressBar.updateProgress()
        try:
            setReduce(mesh, percentage)
        except:
            pass


#
def getFaceData(meshObject):
    dic = collections.OrderedDict()
    maxValue = cmds.polyEvaluate(meshObject, face=1)
    if maxValue:
        for seq, i in enumerate(range(0, maxValue)):
            face = '%s.f[%s]' % (meshObject, seq)
            if cmds.objExists(face):
                coordData = cmds.getAttr(face)
                dic[face] = coordData
    return dic
