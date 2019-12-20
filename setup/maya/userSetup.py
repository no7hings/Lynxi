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


class Setup(object):
    Pth_ModuleDirectory = 'l:/packages/pg/prerelease/lynxitool/0.0.1/lynxitool'
    ToolkitPath = 'l:/packages/pg/prerelease/lynxitool/0.0.1/lynxitool'

    ProductModulePathDic = {
        'LxCore': ''
    }

    @staticmethod
    def getOsActiveViewTime():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    @classmethod
    def traceMessage(cls, text):
        print u'# Lynxi {}'.format(cls.getOsActiveViewTime())
        print u'    {}'.format(text)

    @classmethod
    def traceResult(cls, text):
        cls.traceMessage(
            u'''# Result {}'''.format(text)
        )

    @classmethod
    def traceWarning(cls, text):
        cls.traceMessage(
            u'''# Warning {}'''.format(text)
        )

    @classmethod
    def traceError(cls, text):
        cls.traceMessage(
            u'''# Error {}'''.format(text)
        )

    @staticmethod
    def isLxDevelop():
        boolean = False
        key = 'LYNXI_DEVELOP'
        envDatum = os.environ.get(key)
        if envDatum:
            if envDatum.lower() == 'true':
                boolean = True
        return boolean

    @staticmethod
    def getLxDevelopPath():
        key = 'LYNXI_DEVELOP_PATH'
        envDatum = os.environ.get(key)
        if envDatum:
            if envDatum:
                return envDatum

    @classmethod
    def setEnviron(cls, key, osPath):
        envDatum = os.environ.get(key)
        if envDatum:
            message = 'Exists Environ "{}" : {}'.format(key, osPath)
            cls.traceResult(message)
        else:
            os.environ[key] = osPath
            message = 'Set Environ "{}" : {}'.format(key, osPath)
            cls.traceResult(message)

    @classmethod
    def addPath(cls, osPath):
        # System Path
        sysData = sys.path
        if os.path.exists(osPath):
            if not osPath in sysData:
                sys.path.insert(0, osPath)
                message = 'Add Path: {}'.format(osPath)
                cls.traceResult(message)
            else:
                message = 'Exists Path: {}'.format(osPath)
                cls.traceResult(message)
        else:
            message = 'Non - Exists Path: {}'.format(osPath)
            cls.traceWarning(message)

    @staticmethod
    def setupPipeline():
        from LxCore.setup import appSetup

        appSetup.setLynxiSetup()

    def run(self):

        isLxDevelop = self.isLxDevelop()
        # Step 01
        if isLxDevelop is True:
            moduleDirectory = self.getLxDevelopPath()
        else:
            moduleDirectory = self.Pth_ModuleDirectory

        if os.path.isdir(moduleDirectory):
            self.setEnviron('LYNXI_PRODUCT_PATH', self.Pth_ModuleDirectory)
            self.setEnviron('LYNXI_TOOLKIT_PATH', self.ToolkitPath)
            # Step 02
            if isLxDevelop:
                modulePath = moduleDirectory + '/develop/python'
            else:
                modulePath = moduleDirectory + '/product/python/compile'
            # Step 03
            self.addPath(modulePath)
            # Step 04
            self.setupPipeline()


Setup().run()

