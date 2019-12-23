# coding=utf-8
from subprocess import Popen, PIPE
#
from LxCore import lxBasic, lxConfigure
#
none = ''


#
def getDdlCommand():
    envData = lxBasic.getOsEnvironValue('DEADLINE_PATH')
    if envData:
        deadLineBinPath = envData
    else:
        deadLineBinPath = 'C:/Program Files/Thinkbox/Deadline10/bin'
    #
    sysPaths = lxBasic.getOsSystemPathLis()
    if not deadLineBinPath in sysPaths:
        lxBasic.setSystemPathInsert(deadLineBinPath)
    #
    deadlineCommand = (deadLineBinPath + '/' + 'deadlinecommand.exe').replace('\\', '/')
    return deadlineCommand


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
        data = lxBasic.getJsonLoads(result[0])
        if isinstance(data, dict):
            return data['result']


#
def getDdlSubmitInfo(*keys):
    command = '-JSON -GetSubmissionInfo ' + ' '.join([i for i in keys])
    #
    result = runDdlCommand(command)
    lis = []
    if result:
        data = lxBasic.getJsonLoads(result[0])
        if isinstance(data, dict):
            for key in keys:
                if 'result' in data:
                    resultData = data['result']
                    if isinstance(resultData, dict):
                        lis.append(resultData[key])
                    else:
                        lxConfigure.Message().traceError(resultData)
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
    return 'Frames={}'.format(','.join([str(i) for i in frameLis]))


#
def getDdlCameraArgs(cameraLis):
    return [('Camera{}={}'.format(seq, i)) for seq, i in enumerate(cameraLis)]


#
def getDdlComposeFileArgLis(composeFileLis):
    return ['AWSAssetFile{}={}'.format(seq, i) for seq, i in enumerate(composeFileLis)]


#
def getDdlImageFileArgLis(imageFileLis):
    return ['OutputFilename{}={}'.format(seq, i) for seq, i in enumerate(imageFileLis)]


#
def getDdlInfoData(
        batchName, jobName, batchType,
        frames,
        pool,
        jobPriority,
        taskTimeout,
        machineLimit,
        composeFiles,
        imageFiles
):
    args = [
        'BatchName={}'.format(batchName),
        'Name={}'.format(jobName),
        'Plugin={}'.format(batchType),
        'Comment=',
        'Pool={}'.format(pool),
        'SecondaryPool=none',
        'Priority={}'.format(jobPriority),
        'OnJobComplete=Nothing',
        'TaskTimeoutMinutes={}'.format(taskTimeout),
        'MinRenderTimeMinutes=0',
        'EnableAutoTimeout=0',
        'ConcurrentTasks=1',
        'Department=',
        'Group=none',
        'MachineLimit={}'.format(machineLimit),
        'LimitGroups=',
        'JobDependencies=',
        'IsFrameDependent=0',
        'ChunkSize=1',
        'Whitelist=',
        getDdlFrameArg(frames)
    ]
    args.extend(getDdlComposeFileArgLis(composeFiles))
    args.extend(getDdlImageFileArgLis(imageFiles))
    return '\r\n'.join(args)


#
def getDdlJobData(
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
    args = [
        'Animation={}'.format([0, 1][isAnimationEnable]),
        'Renderer={}'.format(renderer),
        'UsingRenderLayers={}'.format([0, 1][isRenderLayerEnable]),
        'UseLegacyRenderLayers={}'.format([1, 0][isRenderSetupEnable]),
        'RenderLayer={}'.format(currentRenderLayer),
        'RenderHalfFrames=0',
        'FrameNumberOffset=0',
        'LocalRendering=0',
        'StrictErrorChecking=1',
        'MaxProcessors=0',
        'ArnoldVerbose={}'.format(arnoldVerbose),
        'Version={}'.format(mayaVersion),
        'Build={}'.format(['32bit', '64bit'][is64]),
        'ProjectPath={}'.format(scenePath),
        'StartupScript=',
        'ImageWidth={}'.format(width),
        'ImageHeight={}'.format(height),
        'OutputFilePath={}'.format(imagePath),
        'OutputFilePrefix={}'.format(imagePrefix),
        'SceneFile={}'.format(sceneFile),
        'IgnoreError211=0',
        'UseLocalAssetCaching=0',
        'Camera={}'.format(currentCamera),
        'CountRenderableCameras={}'.format(len(renderableCameras)),
        'CommandLineOptions={}'.format(melCommand)
    ]
    #
    args.extend(getDdlCameraArgs(cameras))
    #
    return '\r\n'.join(args)


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
    infoData = getDdlInfoData(
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
    jobData = getDdlJobData(
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
