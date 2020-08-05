# coding:utf-8
import collections

from LxBasic import bscMethods

from LxGraphic import grhCfg

from .. import mtxObjects


def createHou2mtxNodeRawJson(filepathString):
    queryrawCache = mtxObjects.GRH_OBJ_QUERYRAW_CREATOR
    dic = collections.OrderedDict()
    typepathStrList = queryrawCache.typepaths()
    for tgtTypepathStr in typepathStrList:
        tgtNodeQueryraw = queryrawCache.nodeQueryraw(tgtTypepathStr)

        nodeDic = collections.OrderedDict()

        srcTypepathStr = u'arnold::Vop/{}'.format(tgtTypepathStr)

        dic[srcTypepathStr] = nodeDic

        nodeDic[grhCfg.GrhUtility.DEF_grh__key_target_typepath] = tgtTypepathStr

        sourcePortDic = collections.OrderedDict()
        nodeDic[grhCfg.GrhUtility.DEF_grh__key_source_port] = sourcePortDic
        for tgtPortQueryrawObject in tgtNodeQueryraw.portQueryraws():
            tgtAssignStr = tgtPortQueryrawObject.assign
            tgtPortpathStr = tgtPortQueryrawObject.portpath

            if tgtAssignStr in [grhCfg.GrhUtility.DEF_grh__keyword__property]:
                srcPortpathStr = u'ar_{}'.format(tgtPortQueryrawObject.portpath)
            elif tgtAssignStr in [grhCfg.GrhUtility.DEF_grh__keyword__visibility]:
                srcPortpathStr = u'ar_visibility_{}'.format(tgtPortQueryrawObject.portpath)
            else:
                srcPortpathStr = tgtPortQueryrawObject.portpath
            if grhCfg.GrhPortAssignQuery.isOtchannel(tgtAssignStr):
                srcPortpathStr = tgtPortQueryrawObject.portpath.split('.')[-1]

            if srcPortpathStr in sourcePortDic:
                portDic = sourcePortDic[srcPortpathStr]
            else:
                portDic = collections.OrderedDict()
                sourcePortDic[srcPortpathStr] = portDic

            if grhCfg.GrhUtility.DEF_grh__key_target_portpath in portDic:
                targetRaw = portDic[grhCfg.GrhUtility.DEF_grh__key_target_portpath]
            else:
                targetRaw = collections.OrderedDict()
                portDic[grhCfg.GrhUtility.DEF_grh__key_target_portpath] = targetRaw

            targetRaw[tgtAssignStr] = tgtPortpathStr

    bscMethods.OsJsonFile.write(filepathString, dic)


def createUsd2mtxNodeRawJson(filepathString):
    queryrawCache = mtxObjects.GRH_OBJ_QUERYRAW_CREATOR
    dic = collections.OrderedDict()
    typepathStrList = queryrawCache.typepaths()
    for tgtTypepathStr in typepathStrList:
        tgtNodeQueryraw = queryrawCache.nodeQueryraw(tgtTypepathStr)

        nodeDic = collections.OrderedDict()

        srcTypepathStr = u'Shader/arnold:{}'.format(tgtTypepathStr)

        dic[srcTypepathStr] = nodeDic

        nodeDic[grhCfg.GrhUtility.DEF_grh__key_target_typepath] = tgtTypepathStr

        sourcePortDic = collections.OrderedDict()
        nodeDic[grhCfg.GrhUtility.DEF_grh__key_source_port] = sourcePortDic
        for tgtPortQueryrawObject in tgtNodeQueryraw.portQueryraws():
            tgtAssignStr = tgtPortQueryrawObject.assign

            portDic = collections.OrderedDict()
            tgtPortpathStr = tgtPortQueryrawObject.portpath
            if tgtAssignStr in [grhCfg.GrhUtility.DEF_grh__keyword__inport]:
                srcPortpathStr = 'inputs:{}'.format(tgtPortQueryrawObject.portpath)
            elif tgtAssignStr in [grhCfg.GrhUtility.DEF_grh__keyword__otport]:
                srcPortpathStr = 'outputs:{}'.format(tgtPortQueryrawObject.portpath)
            elif tgtAssignStr in [grhCfg.GrhUtility.DEF_grh__keyword__otport_channel]:
                srcPortpathStr = 'outputs:{}'.format(tgtPortQueryrawObject.portpath.split(u'.')[-1])
            elif tgtAssignStr in [grhCfg.GrhUtility.DEF_grh__keyword__property]:
                srcPortpathStr = 'primvars:arnold:{}'.format(tgtPortQueryrawObject.portpath)
            elif tgtAssignStr in [grhCfg.GrhUtility.DEF_grh__keyword__visibility]:
                srcPortpathStr = 'primvars:arnold:visibility:{}'.format(tgtPortQueryrawObject.portpath)
            else:
                srcPortpathStr = None
            if srcPortpathStr is not None:
                sourcePortDic[srcPortpathStr] = portDic
                portDic[grhCfg.GrhUtility.DEF_grh__key_target_portpath] = tgtPortpathStr

    bscMethods.OsJsonFile.write(filepathString, dic)
