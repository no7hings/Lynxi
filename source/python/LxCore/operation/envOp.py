# coding=utf-8
from LxCore import lxBasic, lxConfigure


# Set Environ Path
def setOsEnviron(osEnvironKey, path):
    envData = lxBasic.getOsEnvironValue(osEnvironKey)
    if envData:
        if lxBasic.isOsExist(path):
            if not path in envData:
                lxBasic.setAddOsEnvironData(osEnvironKey, path)
                traceMessage = 'Add Path "{}" : {}'.format(osEnvironKey, path)
                lxConfigure.traceResult(traceMessage)
            else:
                traceMessage = 'Exists Path "{}" : {}'.format(osEnvironKey, path)
                lxConfigure.traceResult(traceMessage)
        else:
            traceMessage = 'Non - Exists Path "{}" : {}'.format(osEnvironKey, path)
            lxConfigure.traceWarning(traceMessage)
    else:
        lxBasic.setOsEnvironValue(osEnvironKey, path)
        traceMessage = 'Set Path "{}" : {}'.format(osEnvironKey, path)
        lxConfigure.traceResult(traceMessage)


# Set System Path
def setSysPath(path):
    osEnvironKey = 'PATH'
    sysData = lxBasic.getOsSystemPathLis()
    if lxBasic.isOsExist(path):
        if not path in sysData:
            lxBasic.setInsertSystemPath(path)
            traceMessage = 'Add Path "{}" : {}'.format(osEnvironKey, path)
            lxConfigure.traceResult(traceMessage)
        else:
            traceMessage = 'Exists Path "{}" : {}'.format(osEnvironKey, path)
            lxConfigure.traceResult(traceMessage)
    else:
        traceMessage = 'Non - Exists Path "{}" : {}'.format(osEnvironKey, path)
        lxConfigure.traceWarning(traceMessage)


#
def setPipeEnviron(osEnvironKey, path):
    envData = lxBasic.getOsEnvironValue(osEnvironKey)
    if envData:
        traceMessage = 'Exists Path "{}" : {}'.format(osEnvironKey, path)
        lxConfigure.traceResult(traceMessage)
    else:
        lxBasic.setOsEnvironValue(osEnvironKey, path)
        traceMessage = 'Set Path "{}" : {}'.format(osEnvironKey, path)
        lxConfigure.traceResult(traceMessage)


#
def setMayaScriptEnviron(path):
    osEnvironKey = 'MAYA_SCRIPT_PATH'
    setOsEnviron(osEnvironKey, path)


#
def getOsEnvironStatisticsData():
    def getBranch(osEnvironKey):
        lis = lxBasic.getOsEnvironPathLis(osEnvironKey)
        lis.sort()
        dic[osEnvironKey] = lis
    #
    dic = lxBasic.orderedDict()
    envKeys = lxBasic.getOsEnvironKeys()
    if envKeys:
        envKeys.sort()
        for envKey in envKeys:
            getBranch(envKey)
    #
    dic['PATH'] = lxBasic.getOsSystemPathLis()
    #
    return dic
