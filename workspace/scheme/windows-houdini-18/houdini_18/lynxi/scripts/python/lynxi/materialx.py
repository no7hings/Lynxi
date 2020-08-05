# coding:utf-8
# noinspection PyUnresolvedReferences
import hou
# noinspection PyUnresolvedReferences
import _alembic_hom_extensions as abc

from LxHouBasic import houBscMethods


def hou2mtx_set_look_find_cmd(hou_node_obj):
    inputNodeList = hou_node_obj.inputs()
    print houBscMethods.HoAlembicFile.getDagTreeObj('', '')
    for nodeObj in inputNodeList:
        nodeTypeStr = nodeObj.type().nameWithCategory()
        if nodeTypeStr == u'Object/geo':
            geoObjList = [nodeObj]
            geoObjList.extend(
                houBscMethods.HouObj.findAllChildNodeObjPaths(nodeObj, include=u'Object/geo')
            )
        else:
            geoObjList = houBscMethods.HouObj.findAllChildNodeObjPaths(nodeObj, include=u'Object/geo')

        for geoObj in geoObjList:
            renderNodeObj = geoObj.renderNode()
            if renderNodeObj:
                print renderNodeObj.__class__.__name__
                print renderNodeObj.isMaterialManager()
                geometryObj = renderNodeObj.geometry()
                print geometryObj.attributeCaptureObjectPaths()


def hou2mtx_set_file_export_cmd(hou_node_obj):
    pass
