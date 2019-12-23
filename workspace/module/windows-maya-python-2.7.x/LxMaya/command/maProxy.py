# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxCore import lxConfigure
#
from LxMaya.command import maFile
#
none = ''


#
def setOutProxy(osFile, renderer, exportMode=0):
    temporaryFile = maFile.getTemporaryOsFile(osFile)
    # Export
    if renderer == lxConfigure.LynxiArnoldRendererValue:
        setOutArnoldProxy(temporaryFile, exportMode)
    elif renderer == lxConfigure.LynxiRedshiftRendererValue:
        setOutRedshiftProxy(temporaryFile, exportMode)
    #
    maFile.setMoveFile(temporaryFile, osFile)


#
def setOutArnoldProxy(osFile, exportMode=0):
    option = '-mask 255;-lightLinks 1;-shadowLinks 1;'
    if exportMode == 0:
        cmds.file(
            osFile,
            force=1,
            options=option,
            type='ASS Export',
            preserveReferences=0,
            constructionHistory=1,
            exportSelected=1
        )
    #
    elif exportMode == 1:
        cmds.file(
            osFile,
            force=1,
            options=option,
            type='ASS Export',
            preserveReferences=0,
            constructionHistory=1,
            exportAll=1
        )


#
def setOutRedshiftProxy(osFile, exportMode=0):
    option = 'exportConnectivity=1;enableCompression=1;'
    if exportMode == 0:
        cmds.file(
            osFile,
            force=1,
            options=option,
            type='Redshift Proxy',
            preserveReferences=0,
            constructionHistory=1,
            exportSelected=1
        )
    #
    elif exportMode == 1:
        cmds.file(
            osFile,
            force=1,
            options=option,
            type='Redshift Proxy',
            preserveReferences=0,
            constructionHistory=1,
            exportAll=1
        )


#
def getArnoldProxyFile(proxyNode):
    attr = proxyNode + '.dso'
    return cmds.getAttr(attr)
