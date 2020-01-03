# coding=utf-8
from LxBasic import bscCore

from LxCore import lxBasic, lxCore_
#
from LxCore.preset import pipePr
#
from LxCore.preset.prod import projectPr
#
from LxCore.operation import envOp
#
from LxCore.setup import maSetup


#
def setBasicPythonPackageSetup():
    traceMessage = '''Setup Windows Python Package(s)'''
    bscCore.Py_Message().trace(traceMessage)
    #
    osPaths = pipePr.env_basic_python_package_lis()
    for osPath in osPaths:
        envOp.setSysPath(osPath)


def setLynxiToolSetup():
    if lxBasic.isMayaApp():
        maSetup.setMayaToolSetup()


def setLynxiSetup(showProgress=False, isCloseMaya=False):
    if lxBasic.isMayaApp():
        isEnable = False
        #
        mayaVersion = lxBasic.getMayaAppVersion()
        projectName = projectPr.getMayaProjectName()
        if lxCore_.Basic().isDevelop():
            isEnable = True
        else:
            mayaProjectNameLis = projectPr.getMayaProjectNames(mayaVersion)
            if projectName in mayaProjectNameLis:
                isEnable = True
            else:
                errorMessage = 'Invalid Maya Project Name : {}'.format(projectName)
                bscCore.Py_Message().traceError(errorMessage)
                #
                bscCore.Py_Log().addError(errorMessage)
        #
        if isEnable is True:
            maSetup.setMayaProjectToolSetup(
                projectName=projectName,
                showProgress=showProgress,
                isCloseMaya=isCloseMaya
            )
