# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxCore import lxBasic
from LxUi.qt import qtProgress
#
from LxMaya.command import maUtils
#
from LxCore.config import assetCfg
#
none = ''


# Customized Check
def astMeshGeomCstCheck(meshObjects, customized):
    checkLis = []
    dataLis = []
    keyWord = 'Triangles Geometry'
    if keyWord in customized:
        cmds.select(meshObjects)
        cmds.polySelectConstraint(mode=3, type=8, size=1)
        cmds.polySelectConstraint(mode=0, type=8, size=0)
        data = cmds.ls(selection=True)
        dataLis.append(data)
    keyWord = 'Quads Geometry'
    if keyWord in customized:
        cmds.select(meshObjects)
        cmds.polySelectConstraint(mode=3, type=8, size=2)
        cmds.polySelectConstraint(mode=0, type=8, size=0)
        data = cmds.ls(selection=True)
        dataLis.append(data)
    keyWord = 'Hard Geometry Edges'
    if keyWord in customized:
        checkLis.append(keyWord)
        cmds.select(meshObjects)
        cmds.polySelectConstraint(mode=3, type=0x8000, smoothness=1)
        cmds.polySelectConstraint(mode=0, type=0x8000, smoothness=0)
        data = cmds.ls(selection=True)
        dataLis.append(data)
    keyWord = 'Soft Geometry Edges'
    if keyWord in customized:
        checkLis.append(keyWord)
        cmds.select(meshObjects)
        cmds.polySelectConstraint(mode=3, type=0x8000, smoothness=2)
        cmds.polySelectConstraint(mode=0, type=0x8000, smoothness=0)
        data = cmds.ls(selection=True)
        dataLis.append(data)
    #
    lis = [checkLis, dataLis]
    return lis


# Routine Check
def astMeshGeomDefCheck(meshObjects):
    # 1
    def nSideFace():
        cmds.select(meshObjects)
        cmds.polySelectConstraint(mode=3, type=8, size=3)
        cmds.polySelectConstraint(mode=0, type=8, size=0)
        return cmds.ls(selection=True)
    # 2
    def nonPlanarFace():
        cmds.select(meshObjects)
        cmds.polySelectConstraint(mode=3, type=8, planarity=1)
        cmds.polySelectConstraint(mode=0, type=8, planarity=0)
        return cmds.ls(selection=True)
    # 3
    def holedFace():
        cmds.select(meshObjects)
        cmds.polySelectConstraint(mode=3, type=8, holes=1)
        cmds.polySelectConstraint(mode=0, type=8, holes=0)
        return cmds.ls(selection=True)
    # 4
    def concaveFace():
        cmds.select(meshObjects)
        cmds.polySelectConstraint(mode=3, type=8, convexity=1)
        cmds.polySelectConstraint(mode=0, type=8, convexity=0)
        return cmds.ls(selection=True)
    # 5
    def sharedUv():
        cmds.select(meshObjects)
        cmds.polySelectConstraint(mode=3, type=16, textureshared=1)
        cmds.polySelectConstraint(mode=0, type=16, textureshared=0)
        return cmds.ls(selection=True)
    # 6
    def zeroAreaFace():
        miniValue = 0.000000
        maxiValue = 0.000000
        cmds.select(meshObjects)
        cmds.polySelectConstraint(mode=3, type=8, geometricarea=1, geometricareabound=(miniValue, maxiValue))
        cmds.polySelectConstraint(mode=0, type=8, geometricarea=0)
        return cmds.ls(selection=True)
    # 7
    def zeroLengthEdge():
        miniValue = 0.000000
        maxiValue = 0.000000
        cmds.select(meshObjects)
        cmds.polySelectConstraint(mode=3, type=0x8000, length=1, lengthbound=(miniValue, maxiValue))
        cmds.polySelectConstraint(mode=0, type=0x8000, length=0)
        return cmds.ls(selection=True)
    # 8
    def zeroAreaUv():
        miniValue = 0.000000
        maxiValue = 0.000000
        cmds.select(meshObjects)
        cmds.polySelectConstraint(mode=3, type=8, geometricarea=1, geometricareabound=(miniValue, 1000000))
        cmds.polySelectConstraint(mode=3, type=8, texturedarea=1, texturedareabound=(miniValue, maxiValue))
        cmds.polySelectConstraint(mode=0, type=8, texturedarea=0, geometricarea=0)
        return cmds.ls(selection=True)
    # 9
    def laminaFace():
        cmds.select(meshObjects)
        cmds.polySelectConstraint(mode=3, type=8, topology=2)
        cmds.polySelectConstraint(mode=0, type=8, topology=0)
        return cmds.ls(selection=True)
    # 10
    def nonTriangulableFace():
        cmds.select(meshObjects)
        cmds.polySelectConstraint(mode=3, type=8, topology=1)
        cmds.polySelectConstraint(mode=0, type=8, topology=0)
        return cmds.ls(selection=True)
    # 11
    def nonMappingFace():
        cmds.select(meshObjects)
        cmds.polySelectConstraint(mode=3, type=8, textured=2)
        cmds.polySelectConstraint(mode=0, type=8, textured=0)
        return cmds.ls(selection=True)
    # 12
    def nonManifoldVertex():
        cmds.select(meshObjects)
        return cmds.polyInfo(nonManifoldVertices=1)
    #
    checkMethodDic = {
        'meshFaceNSidedCheck': nSideFace,
        'meshFaceNonPlanarCheck': nonPlanarFace,
        'meshFaceHoledCheck': holedFace,
        'meshFaceConcaveCheck': concaveFace,
        'meshUvSharedCheck': sharedUv,
        'meshFaceZeroAreaCheck': zeroAreaFace,
        'meshEdgeZeroLengthCheck': zeroLengthEdge,
        'meshUvZeroAreaCheck': zeroAreaUv,
        'meshFaceLaminaCheck': laminaFace,
        'meshFaceNonTriangulableCheck': nonTriangulableFace,
        'meshFaceNonMappingCheck': nonMappingFace,
        'meshVertexNonManifoldCheck': nonManifoldVertex
    }
    #
    dic = lxBasic.orderedDict()
    config = assetCfg.astMeshGeomCheckConfig()
    if meshObjects:
        # View Progress
        progressExplain = u'''Mesh Geometry Check'''
        maxValue = len(config)
        progressBar = qtProgress.viewSubProgress(progressExplain, maxValue)
        for k, v in config.items():
            enable = v[0]
            subExplain = v[1]
            progressBar.updateProgress(subExplain)
            #
            subData = []
            if enable is True:
                if k in checkMethodDic:
                    checkMethod = checkMethodDic[k]
                    subData = checkMethod() or []
            #
            dic[k] = subData
        #
        cmds.select(clear=1)
    #
    return dic


#
def astMeshClean(meshObjects):
    pass


# Get Check Data
def getAstMeshGeomCheckDataDic(meshObjects):
    dic = lxBasic.orderedDict()
    #
    data = astMeshGeomDefCheck(meshObjects)
    if data:
        for k, v in data.items():
            subDic = lxBasic.orderedDict()
            if v:
                for i in v:
                    mesh = i.split('.')[0]
                    meshPath = maUtils._getNodePathString(mesh)
                    compPath = maUtils._getNodePathString(i)
                    subDic.setdefault(meshPath, []).append(compPath)
            #
            dic[k] = subDic
    #
    return dic
