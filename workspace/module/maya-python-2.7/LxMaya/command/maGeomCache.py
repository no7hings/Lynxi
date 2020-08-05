# coding=utf-8
import os
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.mel as mel
#
inCacheLabel = '_inCache'
#
cacheExtConfig = dict(mcc='.mc', mcx='.mcx')


#
def getGeomCacheNodeLis(geometryNode):
    cacheNodes = cmds.listConnections(geometryNode, destination=0, source=1, type='cacheFile')
    if cacheNodes:
        return cacheNodes[0]


#
def getGeomCacheFile(cacheNode):
    directory = cmds.getAttr(cacheNode + '.cachePath')
    fileName = cmds.getAttr(cacheNode + '.cacheName')
    if directory and fileName:
        directory = directory.replace('\\', '/')
        cacheBase = directory + fileName
        if not directory.endswith('/'):
            cacheBase = directory + '/' + fileName
        xmlFile = cacheBase + '.xml'
        if os.path.isfile(xmlFile):
            startFrame, endFrame, solverIndex, cacheType, cacheFormat = getGeometryCacheXmlData(xmlFile)
            if cacheType == 'OneFile':
                cacheExt = cacheExtConfig[cacheFormat]
                cacheFile = cacheBase + cacheExt
                if os.path.isfile(cacheFile):
                    cacheFiles = xmlFile, cacheFile
                    return cacheFiles


#
def getGeomCacheFiles(geometryNode):
    inputNodes = cmds.listConnections(geometryNode, destination=0, source=1, type='cacheFile')
    if inputNodes:
        cacheNode = inputNodes[0]
        return getGeomCacheFile(cacheNode)


#
def getGeometryCacheXmlData(xmlFile):
    cacheType = 'OneFile'
    cacheFormat = 'mcx'
    startFrame = 0
    endFrame = 0
    solverIndex = 0
    if os.path.isfile(xmlFile):
        with open(xmlFile, 'r') as f:
            lines = f.readlines()
            f.close()
            if lines:
                startTime = 0
                endTime = 0
                timePerFrame = 1
                for line in lines:
                    if '<cacheType' in line:
                        cacheType = line.split('=')[1][1:-8]
                        cacheFormat = line.split('=')[-1][1:-4]
                    if '<time Range' in line:
                        startTime, endTime = line.split('=')[-1][1:-4].split('-')
                    if '<cacheTimePerFrame' in line:
                        timePerFrame = line.split('=')[-1][1:-4]
                    if '.simulationMethod' in line:
                        solverIndex = line.split('=')[-1][:1]
                #
                startFrame = int(startTime) / int(timePerFrame)
                endFrame = int(endTime) / int(timePerFrame)
    #
    return startFrame, endFrame, solverIndex, cacheType, cacheFormat


#
def setOutGeometryCache(maObj, cachePath, cacheName, startFrame, endFrame, sample=1, format='OneFile', cacheFormat='mcx'):
    cmds.cacheFile(
        directory=cachePath, fileName=cacheName,
        startTime=startFrame, endTime=endFrame,
        cacheableNode=maObj,
        format=format, cacheFormat=cacheFormat, sampleMultiplier=sample)


#
def setGeometryObjectInCache(maObj, cachePath, cacheName, channelArray, attrArray):
    inCache = maObj + inCacheLabel
    # Check Exists
    existsCacheNode = getGeomCacheNodeLis(maObj)
    if existsCacheNode:
        cmds.delete(existsCacheNode)
    # Create
    createCommand = '''cacheFile -attachFile -fileName "%s" -directory "%s"''' % (cacheName, cachePath)
    channelCommand = ' '.join(['-channelName ' + attr for attr in channelArray])
    attrCommand = ' '.join(['-inAttr ' + attr for attr in attrArray])
    command = ' '.join([createCommand, channelCommand, attrCommand])
    cacheNode = mel.eval(command)
    # Connect
    cmds.connectAttr(cacheNode + '.inRange', maObj + '.playFromCache')
    # Rename
    cmds.rename(cacheNode, inCache)
    return inCache


#
def setRepathGeometryCache(cacheNode, cacheFile):
    cachePath = os.path.dirname(cacheFile)
    cachePathAttr = cacheNode + '.cachePath'
    currentCachePath = cmds.getAttr(cachePathAttr)
    if not currentCachePath == cachePath:
        cmds.setAttr(cachePathAttr, cachePath, type='string')