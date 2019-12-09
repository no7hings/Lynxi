# coding=utf-8
from LxCore import lxBasic, lxConfigure
#
from LxCore.preset import pipePr
#
from LxCore.preset.prod import projectPr
#
from LxCore.operation import envOp
#
from LxCore.setup import appPush
#
serverBasicPath = lxConfigure.LynxiRoot().serverDirectory()
#
none = ''


#
def setMaPythonPackageSetup(mayaVersion):
    traceMessage = '''Setup Maya Python Package(s)'''
    lxConfigure.Message().trace(traceMessage)
    #
    osPathLis = pipePr.env_app_maya_python_package_lis(serverBasicPath, mayaVersion)
    for osPath in osPathLis:
        envOp.setSysPath(osPath)


#
def setMaScriptSetup(projectName):
    if lxBasic.isMayaApp():
        from LxMaya.command import maUtils
        traceMessage = '''Setup Maya Script(s)'''
        lxConfigure.Message().trace(traceMessage)
        #
        data = projectPr.getProjectMayaScriptDatumDic(projectName)
        if data:
            for k, v in data.items():
                for i in v:
                    osFileLis = lxBasic.getOsFilesByPath(i)
                    if osFileLis:
                        traceMessage = '''Add Maya Script(s) "{}" : {}'''.format(lxBasic._toStringPrettify(k), i)
                        lxConfigure.Message().traceResult(traceMessage)
                        for osFile in osFileLis:
                            command = lxBasic.readOsFile(osFile)
                            if osFile.endswith('.py'):
                                pythonCommand = 'python(' + lxBasic.getJsonDumps(command) + ');'
                                maUtils.runMelCommand(pythonCommand)
                            elif osFile.endswith('.mel'):
                                melCommand = command
                                #
                                maUtils.runMelCommand(melCommand)
                            #
                            traceMessage = '''Add Maya Script : {}'''.format(osFile)
                            lxConfigure.Message().traceResult(traceMessage)


#
def setMaTdPackageSetup(projectName):
    traceMessage = '''Setup Maya TD Package(s)'''
    lxConfigure.Message().trace(traceMessage)
    #
    osPathLis = projectPr.getProjectMayaTdPackagePathLis(projectName)
    for osPath in osPathLis:
        envOp.setSysPath(osPath)


#
def setMaMenuSetup():
    from LxMaya.ui import maMenu
    maMenu.setMayaMenu()


#
def setMaHotkeySetup():
    from LxMaya.maSetup import maScriptSetup
    #
    traceMessage = '''Setup Maya Hotkey(s)'''
    lxConfigure.Message().trace(traceMessage)
    #
    maScriptSetup.initHideShowCmd()


# noinspection PyUnresolvedReferences
def setMayaPreference():
    from LxMaya.command import maUtils, maPreference
    # Debug ( Open File by Windows )
    currentFile = maUtils.getCurrentFile()
    if not currentFile.endswith('untitled'):
        pass
    maPreference.setAnimationTimeUnit()
    maPreference.setAnimationTime()


# noinspection PyUnresolvedReferences
def setMayaSetup(projectName, showProgress, isCloseMaya):
    if lxBasic.isMayaApp():
        traceMessage = '''Setup Maya Project : {}'''.format(projectName)
        lxConfigure.Message().trace(traceMessage)
        #
        projectMayaVersion = projectPr.getProjectMayaVersion(projectName)
        # Step >>>> 01
        setMaPythonPackageSetup(projectMayaVersion)
        #
        setMaScriptSetup(projectName)
        setMaTdPackageSetup(projectName)
        # Step >>>> 02
        appPush.MayaPlug(projectName).push()
        # Step >>>> 03
        import maya.utils as utils
        commandLis = [
            'from LxCore.setup import maSetup;maSetup.setMaMenuSetup()',
            'from LxCore.setup import maSetup;maSetup.setMayaPreference()',
            'from LxCore.setup import maSetup;maSetup.setMaHotkeySetup()'
        ]
        [utils.executeDeferred(i) for i in commandLis]
