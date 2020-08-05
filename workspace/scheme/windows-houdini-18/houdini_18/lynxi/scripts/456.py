# coding:utf-8
scheme_name = 'houdini_18'
scheme_version = 'active'

scheme_product_root = r'L:\packages\pg\prerelease\lynxitool\0.0.3\lynxitool'
scheme_kit_root = r'L:\packages\pg\prerelease\lynxitool\0.0.3\lynxitool'


class Setup(object):
    @classmethod
    def setupPipeline(cls):
        from LxCore.setup import appSetup

        appSetup.setLynxiToolSetup()

    @classmethod
    def run(cls):
        import lynxisetup
        # Environ
        setupMethod = lynxisetup.LxSetupMethod
        setupMethod.setEnvironOverride(
            lynxisetup.LxUtilBasic.DEF_util__environ_key__path_product, scheme_product_root
        )
        setupMethod.setEnvironOverride(
            lynxisetup.LxUtilBasic.DEF_util__environ_key__path_kit, scheme_kit_root
        )
        # Scheme
        scheme = lynxisetup.LxWindowsHoudini18Scheme(
            scheme_name, scheme_version
        )
        #
        scheme.setup()
        # Step 04
        # cls.setupPipeline()


if __name__ == '__main__':
    Setup().run()
