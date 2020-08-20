# coding:utf-8
import lynxiutil

scheme_name = 'maya_default'
scheme_version = 'active'

scheme_basic_root = lynxiutil.LxRoot().basic

scheme_product_root = scheme_basic_root
scheme_kit_root = scheme_basic_root


class Setup(object):
    @classmethod
    def setupPipeline(cls):
        from LxCore.setup import appSetup

        appSetup.setLynxiToolSetup()

    @classmethod
    def run(cls):
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
        scheme = lynxiutil.LxWindowsMayaScheme(
            scheme_name, scheme_version
        )
        #
        scheme.setup()
        # Step 04
        cls.setupPipeline()


if __name__ == '__main__':
    Setup().run()

