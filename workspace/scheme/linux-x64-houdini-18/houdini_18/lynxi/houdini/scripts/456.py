# coding:utf-8
import lynxiutil

scheme_name = 'houdini_18'
scheme_version = 'active'

scheme_basic_root = lynxiutil.LxRoot().basic

scheme_product_root = scheme_basic_root
scheme_kit_root = scheme_basic_root


class LxSchemeSetup(object):
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
        scheme = lynxiutil.LxLinux64Houdini18Scheme(
            scheme_name, scheme_version
        )
        #
        scheme.setup()

    @classmethod
    def run(cls):
        cls.setupEnviron()


if __name__ == '__main__':
    LxSchemeSetup.run()
