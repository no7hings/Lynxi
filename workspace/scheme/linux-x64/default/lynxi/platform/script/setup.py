# coding:utf-8
import sys

import lynxiutil

scheme_name = 'default'
scheme_version = 'active'

scheme_basic_root = lynxiutil.LxRoot().basic

scheme_product_root = scheme_basic_root
scheme_kit_root = scheme_basic_root


class LxSchemeSetup(object):
    @staticmethod
    def setupKit():
        from PySide2 import QtWidgets
        #
        from LxKit.qt.kitQtWidgets import _kitQtWgtUtilityWindow
        #
        app = QtWidgets.QApplication(sys.argv)
        w = _kitQtWgtUtilityWindow.LynxiMainWindow()
        #
        w.windowShow()
        sys.exit(app.exec_())

    @classmethod
    def setupEnviron(cls):
        # Environ
        setupMethod = lynxiutil.LxSetupMethod

        setupMethod.setEnvironOverride(
            lynxiutil.LxUtilBasic.DEF_util__environ_key__path_product, scheme_product_root
        )
        setupMethod.setEnvironAppend(
            lynxiutil.LxUtilBasic.DEF_util__environ_key__paths_source, scheme_basic_root
        )

        setupMethod.setEnvironOverride(
            lynxiutil.LxUtilBasic.DEF_util__environ_key__path_kit, scheme_kit_root
        )
        # Scheme
        shmObj = lynxiutil.LxLinux64Scheme(scheme_name, scheme_version)
        shmObj.setup()

    @classmethod
    def run(cls):
        cls.setupEnviron()
        cls.setupKit()


if __name__ == '__main__':
    LxSchemeSetup.run()

