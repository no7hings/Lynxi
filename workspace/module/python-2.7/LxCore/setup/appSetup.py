# coding=utf-8
from LxBasic import bscMtdCore, bscMethods
#
from LxPreset import prsMethods
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
        projectName = prsMethods.Project.mayaActiveName()
        if bscMtdCore.Mtd_BscUtility()._isDevelop():
            isEnable = True
        else:
            mayaProjectNameLis = prsMethods.Project.mayaNames(mayaVersion)
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
