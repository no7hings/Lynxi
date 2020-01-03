# coding:utf-8
scheme_name = 'maya_default'
scheme_version = 'active'

scheme_basic_path = 'l:/packages/pg/prerelease/lynxitool/0.0.1/lynxitool'
scheme_toolkit_path = 'l:/packages/pg/prerelease/lynxitool/0.0.1/lynxitool'


class Setup(object):
    @classmethod
    def setupPipeline(cls):
        from LxCore.setup import appSetup

        appSetup.setLynxiToolSetup()

    @classmethod
    def run(cls):
        import lynxisetup
        # Environ
        method = lynxisetup.Method
        method.setEnviron(
            'LYNXI_PATH', scheme_basic_path
        )
        method.setEnviron(
            'LYNXI_TOOLKIT_PATH', scheme_toolkit_path
        )
        # Scheme
        scheme = lynxisetup.WindowsMayaPython27Scheme(scheme_name, scheme_version)
        #
        scheme.setup()
        # Step 04
        cls.setupPipeline()


if __name__ == '__main__':
    Setup().run()

