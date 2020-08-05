# coding=utf-8
from subprocess import Popen, PIPE
#
from LxBasic import bscMtdCore, bscMethods
#
#
none = ''


#
def getDdlCommand():
    deadLineBinPath = bscMethods.OsEnviron.getAsPath(
        'DEADLINE_PATH',
        'C:/Program Files/Thinkbox/Deadline10/bin'
    )
    bscMethods.OsEnviron.addSystemPath(deadLineBinPath)
    return 'deadlinecommand.exe'


#
def runDdlCommand(command):
    deadLineCommand = getDdlCommand()
    deadlineCommandString = '''"{0}" {1}'''.format(deadLineCommand, command)
    return Popen(deadlineCommandString, shell=True, stdout=PIPE, stderr=PIPE).stdout.readlines()


#
def getDdlJobs():
    command = '-JSON -GetJobs'
    result = runDdlCommand(command)
    if result:
        data = bscMethods.OsJsonFile.load(result[0])
        if isinstance(data, dict):
            return data['result']


#
def getDdlSubmitInfo(*keys):
    command = '-JSON -GetSubmissionInfo ' + ' '.join([i for i in keys])
    #
    result = runDdlCommand(command)
    lis = []
    if result:
        data = bscMethods.OsJsonFile.load(result[0])
        if isinstance(data, dict):
            for key in keys:
                if 'result' in data:
                    resultData = data['result']
                    if isinstance(resultData, dict):
                        lis.append(resultData[key])
                    else:
                        bscMethods.PyMessage.traceError(resultData)
    #
    return lis


#
def getDdlPools():
    infoKey = 'Pools'
    info = getDdlSubmitInfo(infoKey)
    if info:
        return info[0]


#
def getDdlTaskLimit():
    infoKey = 'TaskLimit'
    info = getDdlSubmitInfo(infoKey)
    if info:
        return info[0]


#
def getDdlGroups():
    infoKey = 'Groups'
    info = getDdlSubmitInfo(infoKey)
    if info:
        return info[0]


#
def getDdlMaxPriority():
    infoKey = 'MaxPriority'
    info = getDdlSubmitInfo(infoKey)
    if info:
        return info[0]


#
def getPlugEvn(projectName):
    pass


#
def getDdlFrameArg(frameLis):
    return u'Frames={}'.format(','.join([str(i) for i in frameLis]))


#
def getDdlCameraArgs(cameraLis):
    return [(u'Camera{}={}'.format(seq, i)) for seq, i in enumerate(cameraLis)]


#
def getDdlComposeFileArgLis(composeFileLis):
    return [u'AWSAssetFile{}={}'.format(seq, i) for seq, i in enumerate(composeFileLis)]


#
def getDdlImageFileArgLis(imageFileLis):
    return [u'OutputFilename{}={}'.format(seq, i) for seq, i in enumerate(imageFileLis)]


#
def getDdlInfoRaw(
        batchName, jobName, batchType,
        frames,
        pool,
        jobPriority,
        taskTimeout,
        machineLimit,
        composeFiles,
        imageFiles
):
    lis = [
        u'BatchName={}'.format(batchName),
        u'Name={}'.format(jobName),
        u'Plugin={}'.format(batchType),
        u'Comment=',
        u'Pool={}'.format(pool),
        u'SecondaryPool=none',
        u'Priority={}'.format(jobPriority),
        u'OnJobComplete=Nothing',
        u'TaskTimeoutMinutes={}'.format(taskTimeout),
        u'MinRenderTimeMinutes=0',
        u'EnableAutoTimeout=0',
        u'ConcurrentTasks=1',
        u'Department=',
        u'Group=none',
        u'MachineLimit={}'.format(machineLimit),
        u'LimitGroups=',
        u'JobDependencies=',
        u'IsFrameDependent=0',
        u'ChunkSize=1',
        u'Whitelist=',
        getDdlFrameArg(frames)
    ]
    lis.extend(getDdlComposeFileArgLis(composeFiles))
    lis.extend(getDdlImageFileArgLis(imageFiles))
    return '\r\n'.join(lis)


#
def getDdlJobRaw(
        isAnimationEnable,
        isRenderLayerEnable, isRenderSetupEnable,
        renderer,
        sceneFile, scenePath, imagePath,
        mayaVersion, is64,
        width, height,
        imagePrefix,
        currentCamera, cameras, renderableCameras,
        currentRenderLayer,
        arnoldVerbose,
        melCommand
):
    lis = [
        u'Animation={}'.format([0, 1][isAnimationEnable]),
        u'Renderer={}'.format(renderer),
        u'UsingRenderLayers={}'.format([0, 1][isRenderLayerEnable]),
        u'UseLegacyRenderLayers={}'.format([1, 0][isRenderSetupEnable]),
        u'RenderLayer={}'.format(currentRenderLayer),
        u'RenderHalfFrames=0',
        u'FrameNumberOffset=0',
        u'LocalRendering=0',
        u'StrictErrorChecking=1',
        u'MaxProcessors=0',
        u'ArnoldVerbose={}'.format(arnoldVerbose),
        u'Version={}'.format(mayaVersion),
        u'Build={}'.format(['32bit', '64bit'][is64]),
        u'ProjectPath={}'.format(scenePath),
        u'StartupScript=',
        u'ImageWidth={}'.format(width),
        u'ImageHeight={}'.format(height),
        u'OutputFilePath={}'.format(imagePath),
        u'OutputFilePrefix={}'.format(imagePrefix),
        u'SceneFile={}'.format(sceneFile),
        u'IgnoreError211=0',
        u'UseLocalAssetCaching=0',
        u'Camera={}'.format(currentCamera),
        u'CountRenderableCameras={}'.format(len(renderableCameras)),
        u'CommandLineOptions={}'.format(melCommand)
    ]
    lis.extend(getDdlCameraArgs(cameras))
    return '\r\n'.join(lis)


# Get Deadline's Data
def getDdlMayaBatchData(
        scenePath, sceneFile, batchName,
        composeFiles,
        imagePath, imageFiles,
        imagePrefix,
        isAnimationEnable,
        isRenderLayerEnable, isRenderSetupEnable,
        renderer,
        frames,
        width, height,
        mayaVersion, is64,
        jobName, batchType, pool, jobPriority, taskTimeout, machineLimit,
        currentCamera, cameras, renderableCameras,
        currentRenderLayer,
        arnoldVerbose,
        melCommand
):
    infoData = getDdlInfoRaw(
        batchName=batchName,
        jobName=jobName,
        batchType=batchType,
        frames=frames,
        pool=pool,
        jobPriority=jobPriority,
        taskTimeout=taskTimeout,
        machineLimit=machineLimit,
        composeFiles=composeFiles,
        imageFiles=imageFiles
    )
    jobData = getDdlJobRaw(
        isAnimationEnable=isAnimationEnable,
        isRenderLayerEnable=isRenderLayerEnable,
        isRenderSetupEnable=isRenderSetupEnable,
        renderer=renderer,
        sceneFile=sceneFile,
        scenePath=scenePath,
        imagePath=imagePath,
        mayaVersion=mayaVersion,
        is64=is64,
        width=width,
        height=height,
        imagePrefix=imagePrefix,
        currentCamera=currentCamera,
        cameras=cameras,
        renderableCameras=renderableCameras,
        currentRenderLayer=currentRenderLayer,
        arnoldVerbose=arnoldVerbose,
        melCommand=melCommand
    )
    return infoData, jobData


#
def runDdlJob(infoFile, jobFile):
    command = '''"{}" "{}"'''.format(infoFile, jobFile)
    result = runDdlCommand(command)
    return result
