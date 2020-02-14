# coding:utf-8
scheme_name = 'maya_2019_arnold'
scheme_version = 'active'

scheme_basic_path = r'L:\packages\pg\prerelease\lynxitool\0.0.2\lynxitool'
scheme_toolkit_path = r'L:\packages\pg\prerelease\lynxitool\0.0.2\lynxitool'


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
            lynxisetup.Basic.DEF_key_environ_path_product, scheme_basic_path
        )
        method.setEnviron(
            lynxisetup.Basic.DEF_key_environ_path_toolkit, scheme_toolkit_path
        )
        # Scheme
        scheme = lynxisetup.WindowsMaya2019Python27Scheme(scheme_name, scheme_version)
        #
        scheme.setup()
        # Step 04
        cls.setupPipeline()


if __name__ == '__main__':
    Setup().run()

