# coding:utf-8
scheme_name = 'maya_default'
scheme_version = 'active'

scheme_basic_path = r'l:\tdAsset\lynxi'
scheme_toolkit_path = r'l:\tdAsset\lynxi'


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
            lynxisetup.Basic.environ_key_path_product, scheme_basic_path
        )
        method.setEnviron(
            lynxisetup.Basic.environ_key_path_toolkit, scheme_toolkit_path
        )
        # Scheme
        scheme = lynxisetup.WindowsMayaPython27Scheme(scheme_name, scheme_version)
        #
        scheme.setup()
        # Step 04
        cls.setupPipeline()


if __name__ == '__main__':
    Setup().run()

