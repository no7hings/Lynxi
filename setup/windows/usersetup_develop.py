# coding:utf-8
import os
#
import sys
#
import time
#
productPath = 'L:/tdAsset/lynxi'


#
def getOsActiveViewTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


#
def traceMessage(text):
    print u'# Lynxi {}'.format(getOsActiveViewTime())
    print u'    {}'.format(text)


#
def traceResult(text):
    traceMessage(
        u'''# Result {}'''.format(text)
    )


#
def traceWarning(text):
    traceMessage(
        u'''# Warning {}'''.format(text)
    )


#
def traceError(text):
    traceMessage(
        u'''# Error {}'''.format(text)
    )


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
    envDatum = os.environ.get(key)
    if envDatum:
        message = 'Exists Environ "{}" : {}'.format(key, osPath)
        traceResult(message)
    else:
        os.environ[key] = osPath
        message = 'Set Environ "{}" : {}'.format(key, osPath)
        traceResult(message)


# Set Pipeline Environ
def setProductPath(osPath):
    key = 'LYNXI_PRODUCT_PATH'
    envDatum = os.environ.get(key)
    if envDatum:
        message = 'Exists Environ "{}" : {}'.format(key, osPath)
        traceResult(message)
    else:
        os.environ[key] = osPath
        message = 'Set Environ "{}" : {}'.format(key, osPath)
        traceResult(message)


# Set Python Environ
def setModulePath(osPath):
    # System Path
    key = 'PATH'
    # System Path
    sysData = sys.path
    if os.path.exists(osPath):
        if not osPath in sysData:
            sys.path.insert(0, osPath)
            message = 'Add Path "{}" : {}'.format(key, osPath)
            traceResult(message)
        else:
            message = 'Exists Path "{}" : {}'.format(key, osPath)
            traceResult(message)
    else:
        message = 'Non - Exists Path"{}" : {}'.format(key, osPath)
        traceWarning(message)


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
    from LxInterface.qt.ifWidgets import ifWindow
    #
    app = QtWidgets.QApplication(sys.argv)
    #
    w = ifWindow.IfDevelopWindow()
    w.uiShow()
    #
    sys.exit(app.exec_())


#
def setup():
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
            modulePath = pipelinePath + '/source/python'
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

