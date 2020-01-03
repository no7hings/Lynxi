# coding:utf-8
scheme_name = 'default'
scheme_version = 'active'

scheme_path = 'l:/packages/pg/prerelease/lynxitool/0.0.1/lynxitool'
scheme_toolkit_path = 'l:/packages/pg/prerelease/lynxitool/0.0.1/lynxitool'


class Setup(object):
    @staticmethod
    def setupUi():
        import sys
        #
        from PyQt5 import QtWidgets
        #
        from LxInterface.qt.ifWidgets import ifProductWindow
        #
        app = QtWidgets.QApplication(sys.argv)
        w = ifProductWindow.If_QtToolkitWindow()
        w.windowShow()
        sys.exit(app.exec_())

    @classmethod
    def getSetupMethod(cls):
        import sys
        pyFile = sys.argv[0].replace('\\', '/')
        methodPath = '/'.join(pyFile.split('/')[:-3])
        sys.path.insert(0, methodPath)

    @classmethod
    def run(cls):
        cls.getSetupMethod()

        import lynxisetup
        # Environ
        method = lynxisetup.Method
        #
        method.setEnviron(
            'LYNXI_PATH', scheme_path
        )
        method.setEnviron(
            'LYNXI_TOOLKIT_PATH', scheme_toolkit_path
        )
        # Scheme
        scheme = lynxisetup.WindowsPython27Scheme(scheme_name, scheme_version)
        scheme.setup()
        #
        cls.setupUi()


if __name__ == '__main__':
    Setup().run()
