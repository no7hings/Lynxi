# coding=utf-8
from LxBasic import bscCore, bscMethods
#
from LxCore.preset.prod import projectPr
#
from LxCore.setup import maSetup


def setLynxiToolSetup():
    if bscMethods.MayaApp.isActive():
        maSetup.setMayaToolSetup()


def setLynxiSetup(showProgress=False, isCloseMaya=False):
    if bscMethods.MayaApp.isActive():
        isEnable = False
        #
        mayaVersion = bscMethods.MayaApp.version()
        projectName = projectPr.getMayaProjectName()
        if bscCore.BscMtdBasic()._isDevelop():
            isEnable = True
        else:
            mayaProjectNameLis = projectPr.getMayaProjectNames(mayaVersion)
            if projectName in mayaProjectNameLis:
                isEnable = True
            else:
                errorMessage = 'Invalid Maya Project Name : {}'.format(projectName)
                bscMethods.PyMessage.traceError(errorMessage)
                #
                bscMethods.OsLog.addError(errorMessage)
        #
        if isEnable is True:
            maSetup.setMayaProjectToolSetup(
                projectName=projectName,
                showProgress=showProgress,
                isCloseMaya=isCloseMaya
            )
