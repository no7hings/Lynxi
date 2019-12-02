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
    lxConfigure.traceMessage(traceMessage)
    #
    osPaths = pipePr.env_basic_python_package_lis()
    for osPath in osPaths:
        envOp.setSysPath(osPath)


#
def setLynxiSetup(showProgress=False, isCloseMaya=False):
    if lxBasic.isMayaApp():
        isEnable = False
        #
        mayaVersion = lxBasic.getMayaAppVersion()
        projectName = projectPr.getMayaProjectName()
        if lxConfigure.isLxDevelop():
            isEnable = True
        else:
            mayaProjectNameLis = projectPr.getMayaProjectNames(mayaVersion)
            if projectName in mayaProjectNameLis:
                isEnable = True
            else:
                errorMessage = 'Invalid Maya Project Name : {}'.format(projectName)
                lxConfigure.traceError(errorMessage)
                #
                lxConfigure.setErrorLogAdd(errorMessage)
        #
        if isEnable is True:
            maSetup.setMayaSetup(projectName=projectName, showProgress=showProgress, isCloseMaya=isCloseMaya)
    else:
        setBasicPythonPackageSetup()
