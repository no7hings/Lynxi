# coding=utf-8
from LxBasic import bscCore, bscMethods

from LxCore import lxBasic
#
from LxCore.preset.prod import projectPr
#
from LxCore.setup import maSetup


def setLynxiToolSetup():
    if lxBasic.isMayaApp():
        maSetup.setMayaToolSetup()


def setLynxiSetup(showProgress=False, isCloseMaya=False):
    if lxBasic.isMayaApp():
        isEnable = False
        #
        mayaVersion = lxBasic.getMayaAppVersion()
        projectName = projectPr.getMayaProjectName()
        if bscCore.Basic()._isDevelop():
            isEnable = True
        else:
            mayaProjectNameLis = projectPr.getMayaProjectNames(mayaVersion)
            if projectName in mayaProjectNameLis:
                isEnable = True
            else:
                errorMessage = 'Invalid Maya Project Name : {}'.format(projectName)
                bscMethods.PythonMessage().traceError(errorMessage)
                #
                bscMethods.PythonLog().addError(errorMessage)
        #
        if isEnable is True:
            maSetup.setMayaProjectToolSetup(
                projectName=projectName,
                showProgress=showProgress,
                isCloseMaya=isCloseMaya
            )
