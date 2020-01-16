# coding:utf-8
#
from LxCore.preset import appVariant


#
def dbAssetBasicDirectory():
    directory = '%s/%s/%s' % (appVariant.dbAssetRoot, appVariant.dbBasicFolderName, appVariant.dbAssetBasicKey)
    return directory


#
def dbSceneryBasicDirectory():
    directory = '%s/%s/%s' % (appVariant.dbAssetRoot, appVariant.dbBasicFolderName, appVariant.dbSceneryBasicKey)
    return directory


# Asset Index
def dbAstIndexSubDirectory():
    directory = dbAssetBasicDirectory() + '/%s' % appVariant.dbIndexSubKey
    return directory


# Scenery Index
def dbSceneryIndexSubDirectory():
    directory = dbSceneryBasicDirectory() + '/%s' % appVariant.dbIndexSubKey
    return directory


#
def dbAstProductSubDirectory():
    directory = dbAssetBasicDirectory() + '/%s' % appVariant.dbIntegrationSubKey
    return directory


#
def dbAstModelProductDirectory():
    directory = dbAstProductSubDirectory() + '/%s' % appVariant.dbModelLinkUnitKey
    return directory


#
def dbAstMeshProductDirectory():
    directory = dbAstProductSubDirectory() + '/%s' % appVariant.dbMeshUnitKey
    return directory


#
def dbAstCfxProductDirectory():
    directory = dbAstProductSubDirectory() + '/%s' % appVariant.dbCfxLinkUnitKey
    return directory


#
def dbAstCfxFurProductDirectory():
    directory = dbAstProductSubDirectory() + '/%s' % appVariant.dbFurUnitKey
    return directory


#
def dbAstRigProductDirectory():
    directory = dbAstProductSubDirectory() + '/%s' % appVariant.dbRigLinkUnitKey
    return directory


#
def dbAstRigSolProductDirectory():
    directory = dbAstProductSubDirectory() + '/%s' % appVariant.dbSolverLinkUnitKey
    return directory


# Nde_Geometry
def dbAstGeometrySubDirectory():
    directory = dbAssetBasicDirectory() + '/%s' % appVariant.dbGeometrySubKey
    return directory


# Mesh
def dbAstMeshSubDirectory():
    directory = dbAssetBasicDirectory() + '/%s' % appVariant.dbMeshSubKey
    return directory


def dbAstNurbsCurveSubDirectory():
    directory = dbAssetBasicDirectory() + '/%s' % appVariant.dbNurbsCurveSubKey
    return directory


#
def dbAstFurSubDirectory():
    directory = dbAssetBasicDirectory() + '/%s' % appVariant.dbSubFurKey
    return directory


#
def dbAstGraphSubDirectory():
    directory = dbAssetBasicDirectory() + '/%s' % appVariant.dbGraphSubKey
    return directory


# Db Material Path
def dbAstMaterialSubDirectory():
    directory = dbAssetBasicDirectory() + '/%s' % appVariant.dbMaterialSubKey
    return directory


# Gz AOV Path
def dbAstAovSubDirectory():
    directory = dbAssetBasicDirectory() + '/%s' % appVariant.dbAovSubKey
    return directory


#
def dbAstPictureSubDirectory():
    directory = dbAssetBasicDirectory() + '/%s' % appVariant.dbPictureSubKey
    return directory


#
def dbScnPictureSubDirectory():
    directory = dbAssetBasicDirectory() + '/%s' % appVariant.dbPictureSubKey
    return directory


#
def dbAstTextureDirectory():
    directory = dbAstPictureSubDirectory() + '/%s' % appVariant.dbTextureUnitKey
    return directory


#
def dbAstMapDirectory():
    directory = dbAstPictureSubDirectory() + '/%s' % appVariant.dbMapUnitKey
    return directory


#
def dbAstPreviewDirectory():
    directory = dbAstPictureSubDirectory() + '/%s' % appVariant.dbPreviewUnitKey
    return directory


#
def dbScnUnitPreviewDirectory():
    directory = dbScnPictureSubDirectory() + '/%s' % appVariant.dbPreviewUnitKey
    return directory


#
def dbAstRecordSubDirectory():
    directory = dbAssetBasicDirectory() + '/%s' % appVariant.dbRecordSubKey
    return directory


#
def dbScnRecordSubDirectory():
    directory = dbSceneryBasicDirectory() + '/%s' % appVariant.dbRecordSubKey
    return directory


#
def dbAstHistoryDirectory():
    directory = dbAstRecordSubDirectory() + '/%s' % appVariant.dbHistoryUnitKey
    return directory


#
def dbScnHistoryDirectory():
    directory = dbScnRecordSubDirectory() + '/%s' % appVariant.dbHistoryUnitKey
    return directory


#
def dbAstLockDirectory():
    directory = dbAstRecordSubDirectory() + '/%s' % appVariant.dbLockUnitKey
    return directory


#
def dbAstFilterIndexDirectory():
    directory = dbAstIndexSubDirectory() + '/%s' % appVariant.dbFilterUnitKey
    return directory


#
def dbAstNameIndexDirectory():
    directory = dbAstIndexSubDirectory() + '/%s' % appVariant.dbNameUnitKey
    return directory


#
def dbAstVariantIndexDirectory():
    directory = dbAstIndexSubDirectory() + '/%s' % appVariant.dbVariantUnitKey
    return directory


#
def dbAstAssemblyIndexDirectory():
    directory = dbAstIndexSubDirectory() + '/%s' % appVariant.dbAssemblyUnitKey
    return directory


# Asset Nde_Geometry Index
def dbAstGeometryIndexDirectory():
    directory = dbAstIndexSubDirectory() + '/%s' % appVariant.dbGeometryUnitKey
    return directory


# Asset Nurbs Surface Index
def dbAstNurbsSurfaceIndexDirectory():
    directory = dbAstIndexSubDirectory() + '/%s' % appVariant.dbNurbsSurfaceUnitKey
    return directory


# Asset Nurbs Curve Index
def dbAstNurbsCurveIndexDirectory():
    directory = dbAstIndexSubDirectory() + '/%s' % appVariant.dbNurbsCurveUnitKey
    return directory


# Fur Index
def dbAstFurIndexDirectory():
    directory = dbAstIndexSubDirectory() + '/%s' % appVariant.dbFurUnitKey
    return directory


#
def dbAstGraphIndexDirectory():
    directory = dbAstIndexSubDirectory() + '/%s' % appVariant.dbGraphUnitKey
    return directory


# Texture Index
def dbAstTextureIndexDirectory():
    directory = dbAstIndexSubDirectory() + '/%s' % appVariant.dbTextureUnitKey
    return directory


# Material File
def dbAstMaterialIndexDirectory():
    directory = dbAstIndexSubDirectory() + '/%s' % appVariant.dbMaterialUnitKey
    return directory


# Material's AOV
def dbAstAovIndexDirectory():
    directory = dbAstIndexSubDirectory() + '/%s' % appVariant.dbAovUnitKey
    return directory


# Mesh Constant
def dbAstGeometryConstantDirectory():
    directory = dbAstIndexSubDirectory() + '/%s' % appVariant.dbContrastUnitKey
    return directory


# Nde_Geometry
def dbAstGeometryTransformUnitDirectory():
    directory = dbAstGeometrySubDirectory() + '/%s' % appVariant.dbTransformUnitKey
    return directory


#
def dbAstGeometryGeomTopoUnitDirectory():
    directory = dbAstGeometrySubDirectory() + '/%s' % appVariant.dbGeomTopoUnitKey
    return directory


#
def dbAstGeometryGeomShapeUnitDirectory():
    directory = dbAstGeometrySubDirectory() + '/%s' % appVariant.dbGeomShapeUnitKey
    return directory


#
def dbAstGeometryMapUnitDirectory():
    directory = dbAstGeometrySubDirectory() + '/%s' % appVariant.dbMapUnitKey
    return directory


#
def dbAstGeometryVertexNormalUnitDirectory():
    directory = dbAstGeometrySubDirectory() + '/%s' % appVariant.dbVertexNormalUnitKey
    return directory


#
def dbAstGeometryEdgeSmoothUnitDirectory():
    directory = dbAstGeometrySubDirectory() + '/%s' % appVariant.dbEdgeSmoothUnitKey
    return directory


#
def dbAstNurbsCurveTransformUnitDirectory():
    directory = dbAstNurbsCurveSubDirectory() + '/%s' % appVariant.dbTransformUnitKey
    return directory


#
def dbAstNurbsCurveGeomTopoUnitDirectory():
    directory = dbAstNurbsCurveSubDirectory() + '/%s' % appVariant.dbGeomTopoUnitKey
    return directory


#
def dbAstNurbsCurveGeomShapeUnitDirectory():
    directory = dbAstNurbsCurveSubDirectory() + '/%s' % appVariant.dbGeomShapeUnitKey
    return directory


# Fur Path
def dbAstFurPathUnitDirectory():
    directory = dbAstFurSubDirectory() + '/%s' % appVariant.dbPathUnitKey
    return directory


# Graph
def dbAstObjectGraphNodeUnitDirectory():
    directory = dbAstGraphSubDirectory() + '/%s' % appVariant.dbNodeUnitKey
    return directory


#
def dbAstObjectGraphGeometryUnitDirectory():
    directory = dbAstGraphSubDirectory() + '/%s' % appVariant.dbGeometryUnitKey
    return directory


#
def dbAstObjectGraphRelationUnitDirectory():
    directory = dbAstGraphSubDirectory() + '/%s' % appVariant.dbRelationUnitKey
    return directory


# Material Nde_Node
def dbAstMaterialNodeUnitDirectory():
    directory = dbAstMaterialSubDirectory() + '/%s' % appVariant.dbNodeUnitKey
    return directory


# Material Shape
def dbAstMaterialObjectUnitDirectory():
    directory = dbAstMaterialSubDirectory() + '/%s' % appVariant.dbObjectUnitKey
    return directory


# Material's Connections
def dbAstMaterialRelationUnitDirectory():
    directory = dbAstMaterialSubDirectory() + '/%s' % appVariant.dbRelationUnitKey
    return directory


# Mesh Attribute File
def dbAstMaterialObjAttrUnitDirectory():
    directory = dbAstMaterialSubDirectory() + '/%s' % appVariant.dbAttributeUnitKey
    return directory


# Material's Link
def dbAstMaterialObjSetUnitDirectory():
    directory = dbAstMaterialSubDirectory() + '/%s' % appVariant.dbObjectSetUnitKey
    return directory


# Material's AOV
def dbAstAovNodeUnitDirectory():
    directory = dbAstAovSubDirectory() + '/%s' % appVariant.dbNodeUnitKey
    return directory


# Material's Connections
def dbAstAovRelationUnitDirectory():
    directory = dbAstAovSubDirectory() + '/%s' % appVariant.dbRelationUnitKey
    return directory
