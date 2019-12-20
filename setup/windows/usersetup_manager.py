# coding:utf-8
import os
#
import sys
#
productPath = 'L:/tdAsset/lynxi'


#
def isLxDevelop():
    boolean = False
    key = 'LYNXI_DEVELOP'
    envData = os.environ.get(key)
    if envData:
        if envData.lower() == 'true':
            boolean = True
    return boolean


#
def _getLxDevelopPath():
    key = 'LYNXI_DEVELOP_PATH'
    envData = os.environ.get(key)
    if envData:
        if envData:
            return envData


# Set Pipeline Environ
def setPipelinePath(osPath):
    key = 'LYNXI_PATH'
    envData = os.environ.get(key)
    if envData:
        traceMessage = 'Exists - Environ [ %s ] : %s' % (key, osPath)
        print traceMessage
    elif not envData:
        os.environ[key] = osPath
        traceMessage = 'Set Environ [ %s ] : %s' % (key, osPath)
        print traceMessage


# Set Pipeline Environ
def setProductPath(osPath):
    key = 'LYNXI_PRODUCT_PATH'
    envData = os.environ.get(key)
    if envData:
        traceMessage = 'Exists - Environ [ %s ] : %s' % (key, osPath)
        print traceMessage
    elif not envData:
        os.environ[key] = osPath
        traceMessage = 'Set Environ [ %s ] : %s' % (key, osPath)
        print traceMessage


# Set Python Environ
def setModulePath(osPath):
    # System Path
    key = 'PATH'
    sysData = sys.path
    if os.path.exists(osPath):
        if not osPath in sysData:
            sys.path.insert(0, osPath)
            traceMessage = 'Set Path [ %s ] : %s' % (key, osPath)
            print traceMessage
        elif osPath in sysData:
            traceMessage = 'Exists - Path [ %s ] : %s' % (key, osPath)
            print traceMessage
    elif not os.path.exists(osPath):
        traceMessage = 'Non - Exists [ %s ] : %s' % (key, osPath)
        print traceMessage


# Setup Pipeline
def setupPipeline():
    from LxCore.setup import appSetup
    #
    appSetup.setLynxiSetup()


#
def openUi():
    import sys
    #
    from PyQt5 import QtWidgets
    #
    from LxInterface.qt.ifWidgets import ifProductWindow
    #
    app = QtWidgets.QApplication(sys.argv)
    w = ifProductWindow.IfProductManagerWindow()
    w.windowShow()
    sys.exit(app.exec_())


#
def setup():
    traceMessage = '>>>> [ Set Environ ]'
    print traceMessage
    #
    setProductPath(productPath)
    #
    isDevelopBoolean = isLxDevelop()
    # Step 01
    if isDevelopBoolean is True:
        pipelinePath = _getLxDevelopPath()
    else:
        pipelinePath = productPath
    #
    if os.path.isdir(pipelinePath):
        setPipelinePath(pipelinePath)
        # Step 02
        if isDevelopBoolean:
            modulePath = pipelinePath + '/module'
        else:
            modulePath = pipelinePath + '/module.pyc'
        # Step 03
        setModulePath(modulePath)
        # Step 04
        setupPipeline()
        #
        openUi()

#
setup()
