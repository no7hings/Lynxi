# coding=utf-8
from LxCore import lxBasic, lxConfigure
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
    lxConfigure.Message().trace(traceMessage)
    #
    osPaths = pipePr.env_basic_python_package_lis()
    for osPath in osPaths:
        envOp.setSysPath(osPath)


#
def setLynxiSetup(showProgress=False, isCloseMaya=False):
    lxConfigure.Lynxi_Module_Python().setLocalRefresh()
    if lxBasic.isMayaApp():
        isEnable = False
        #
        mayaVersion = lxBasic.getMayaAppVersion()
        projectName = projectPr.getMayaProjectName()
        if lxConfigure.Basic().isDevelop():
            isEnable = True
        else:
            mayaProjectNameLis = projectPr.getMayaProjectNames(mayaVersion)
            if projectName in mayaProjectNameLis:
                isEnable = True
            else:
                errorMessage = 'Invalid Maya Project Name : {}'.format(projectName)
                lxConfigure.Message().traceError(errorMessage)
                #
                lxConfigure.Log().addError(errorMessage)
        #
        if isEnable is True:
            maSetup.setMayaSetup(projectName=projectName, showProgress=showProgress, isCloseMaya=isCloseMaya)
    else:
        setBasicPythonPackageSetup()
