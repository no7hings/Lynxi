# coding=utf-8
from LxBasic import bscMethods

from LxCore import lxBasic, lxScheme
#
from LxCore.preset.prod import projectPr
#
serverBasicPath = lxScheme.Root().basic.server
#
none = ''


#
def setMaScriptSetup(projectName):
    if lxBasic.isMayaApp():
        from LxMaya.command import maUtils
        traceMessage = '''Setup Maya Script(s)'''
        bscMethods.PyMessage.trace(traceMessage)
        #
        data = projectPr.getProjectMayaScriptDatumDic(projectName)
        if data:
            for k, v in data.items():
                for i in v:
                    osFileLis = lxBasic.getOsFilesByPath(i)
                    if osFileLis:
                        traceMessage = '''Add Maya Script(s) "{}" : {}'''.format(lxBasic.str_camelcase2prettify(k), i)
                        bscMethods.PyMessage.traceResult(traceMessage)
                        for osFile in osFileLis:
                            command = bscMethods.OsFile.read(osFile)
                            if osFile.endswith('.py'):
                                pythonCommand = 'python(' + bscMethods.OsJson.dump(command) + ');'
                                maUtils.runMelCommand(pythonCommand)
                            elif osFile.endswith('.mel'):
                                melCommand = command
                                #
                                maUtils.runMelCommand(melCommand)
                            #
                            traceMessage = '''Add Maya Script : {}'''.format(osFile)
                            bscMethods.PyMessage.traceResult(traceMessage)


#
def setMaTdPackageSetup(projectName):
    traceMessage = '''Setup Maya TD Package(s)'''
    bscMethods.PyMessage.trace(traceMessage)
    #
    osPathLis = projectPr.getProjectMayaTdPackagePathLis(projectName)
    for osPath in osPathLis:
        bscMethods.OsEnviron.addSystemPath(osPath)


#
def setMaMenuSetup():
    from LxMaya.ui import maMenu
    maMenu.setMayaMenu()


#
def setMaHotkeySetup():
    from LxMaya.maSetup import maScriptSetup
    #
    traceMessage = '''Setup Maya Hotkey(s)'''
    bscMethods.PyMessage.trace(traceMessage)
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
def setMayaProjectToolSetup(projectName, showProgress, isCloseMaya):
    if lxBasic.isMayaApp():
        traceMessage = '''Setup Maya Project : {}'''.format(projectName)
        bscMethods.PyMessage.trace(traceMessage)
        #
        setMaScriptSetup(projectName)
        setMaTdPackageSetup(projectName)
        # Step >>>> 02
        # appPush.MayaPlug(projectName).push()
        # Step >>>> 03
        import maya.utils as utils
        commandLis = [
            'from LxCore.setup import maSetup;maSetup.setMaMenuSetup()',
            'from LxCore.setup import maSetup;maSetup.setMayaPreference()',
            'from LxCore.setup import maSetup;maSetup.setMaHotkeySetup()'
        ]
        [utils.executeDeferred(i) for i in commandLis]


def setMayaToolSetup():
    if lxBasic.isMayaApp():
        # noinspection PyUnresolvedReferences
        import maya.utils as utils
        commandLis = [
            'from LxCore.setup import maSetup;maSetup.setMaMenuSetup()'
        ]
        [utils.executeDeferred(i) for i in commandLis]
