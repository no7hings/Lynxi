# coding:utf-8
import os
#
import sys
#
import time
# noinspection PyUnresolvedReferences
import pymel.core as core
# noinspection PyUnresolvedReferences
import maya.utils as utils
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
    envDatum = os.environ.get(key)
    if envDatum:
        if envDatum.lower() == 'true':
            boolean = True
    return boolean


#
def _getLxDevelopPath():
    key = 'LYNXI_DEVELOP_PATH'
    envDatum = os.environ.get(key)
    if envDatum:
        if envDatum:
            return envDatum


# Set Pipeline Environ
def setBasicPath(osPath):
    key = 'LYNXI_PATH'
    envDatum = os.environ.get(key)
    if envDatum:
        message = 'Exists Environ "{}" : {}'.format(key, osPath)
        traceResult(message)
    else:
        os.environ[key] = osPath
        message = 'Set Environ "{}" : {}'.format(key, osPath)
        traceResult(message)


# Set Product Environ
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
def setup():
    isLxDevelop_ = isLxDevelop()
    # Step 01
    if isLxDevelop_ is True:
        basicPath = _getLxDevelopPath()
    else:
        basicPath = productPath
    #
    if os.path.isdir(basicPath):
        setProductPath(productPath)
        # Step 02
        if isLxDevelop_:
            modulePath = basicPath + '/source/python'
        else:
            modulePath = basicPath + '/module.pyc'
        # Step 03
        setModulePath(modulePath)
        # Step 04
        setupPipeline()


#
setup()
