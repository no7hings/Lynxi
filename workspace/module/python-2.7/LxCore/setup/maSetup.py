# coding=utf-8
from LxBasic import bscMethods

from LxScheme import shmOutput

from LxPreset import prsMethods
#
serverBasicPath = shmOutput.Root().basic.server
#
none = ''


#
def setMaScriptSetup(projectName):
    if bscMethods.MayaApp.isActive():
        from LxMaya.command import maUtils
        traceMessage = '''Setup Maya Script(s)'''
        bscMethods.PyMessage.trace(traceMessage)
        #
        data = prsMethods.Project.mayaScriptDatumDict(projectName)
        if data:
            for k, v in data.items():
                for i in v:
                    osFileLis = bscMethods.OsDirectory.fileFullpathnames(i)
                    if osFileLis:
                        traceMessage = '''Add Maya Script(s) "{}" : {}'''.format(bscMethods.StrCamelcase.toPrettify(k), i)
                        bscMethods.PyMessage.traceResult(traceMessage)
                        for fileString_ in osFileLis:
                            command = bscMethods.OsFile.read(fileString_)
                            if fileString_.endswith('.py'):
                                pythonCommand = 'python(' + bscMethods.OsJsonFile.dump(command) + ');'
                                maUtils.runMelCommand(pythonCommand)
                            elif fileString_.endswith('.mel'):
                                melCommand = command
                                #
                                maUtils.runMelCommand(melCommand)
                            #
                            traceMessage = '''Add Maya Script : {}'''.format(fileString_)
                            bscMethods.PyMessage.traceResult(traceMessage)


#
def setMaTdPackageSetup(projectName):
    traceMessage = '''Setup Maya TD Package(s)'''
    bscMethods.PyMessage.trace(traceMessage)
    #
    osPathLis = prsMethods.Project.mayaTdPackageDirectories(projectName)
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
    if bscMethods.MayaApp.isActive():
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
    if bscMethods.MayaApp.isActive():
        # noinspection PyUnresolvedReferences
        import maya.utils as utils
        commandLis = [
            'from LxCore.setup import maSetup;maSetup.setMaMenuSetup()'
        ]
        [utils.executeDeferred(i) for i in commandLis]
