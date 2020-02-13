# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxBasic import bscCore, bscMethods
#
from LxCore import lxConfigure
#
none = ''


#
def setOutProxy(fileString_, renderer, exportMode=0):
    temporaryFile = bscMethods.OsFile.temporaryName(fileString_)
    # Export
    if renderer == lxConfigure.LynxiArnoldRendererValue:
        setOutArnoldProxy(temporaryFile, exportMode)
    elif renderer == lxConfigure.LynxiRedshiftRendererValue:
        setOutRedshiftProxy(temporaryFile, exportMode)
    #
    bscMethods.OsFile.copyTo(temporaryFile, fileString_)


#
def setOutArnoldProxy(fileString_, exportMode=0):
    option = '-mask 255;-lightLinks 1;-shadowLinks 1;'
    if exportMode == 0:
        cmds.file(
            fileString_,
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
            fileString_,
            force=1,
            options=option,
            type='ASS Export',
            preserveReferences=0,
            constructionHistory=1,
            exportAll=1
        )


#
def setOutRedshiftProxy(fileString_, exportMode=0):
    option = 'exportConnectivity=1;enableCompression=1;'
    if exportMode == 0:
        cmds.file(
            fileString_,
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
            fileString_,
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
