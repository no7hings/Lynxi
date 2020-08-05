# coding:utf-8
from LxScheme import shmCfg, shmObjAbs

from LxScheme.shmObjects import _shmObjResource


class ShareResourceBuilder(shmObjAbs.Abs_ShmRscBuilder):
    def __init__(self, *args):
        self._initAbsShmRscBuilder(*args)


class WindowsResourceBuilder(shmObjAbs.Abs_ShmRscBuilder):
    def __init__(self, *args):
        self.VAR_shm__rsc__class_dict = {
            self.DEF_shm__rsc__category__plf_language: _shmObjResource.Rsc_PltLanguage,
            self.DEF_shm__rsc__category__plf_application: _shmObjResource.Rsc_PltApplication,

            self.DEF_shm__rsc__category__plf_lng_package: _shmObjResource.Rsc_PltLanPackage,
            self.DEF_shm__rsc__category__plf_app_lng_Package: _shmObjResource.Rsc_PltAppLanPackage,
            self.DEF_shm__rsc__category__plf_App_Package: _shmObjResource.Rsc_PltAppPackage,

            self.DEF_shm__rsc__category__plf_plug: _shmObjResource.Rsc_PltPlug,
            self.DEF_shm__rsc__category__plf_lng_plug: _shmObjResource.Rsc_PltLanPlug,
            self.DEF_shm__rsc__category__plf_app_lng_plug: _shmObjResource.Rsc_PltAppLanPlug,
            self.DEF_shm__rsc__category__plf_app_plug: _shmObjResource.Rsc_PltAppPlug,

            self.DEF_shm__rsc__category__plf_lng_module: _shmObjResource.Rsc_PltLanModule,
            self.DEF_shm__rsc__category__plf_app_lng_module: _shmObjResource.Rsc_PltAppLanModule,
            self.DEF_shm__rsc__category__plf_app_module: _shmObjResource.Rsc_PltAppModule,

            self.DEF_shm__rsc__category__plf_scheme: _shmObjResource.Rsc_PltScheme,
            self.DEF_shm__rsc__category__plf_lng_scheme: _shmObjResource.Rsc_PltLanScheme,
            self.DEF_shm__rsc__category__plf_app_scheme: _shmObjResource.Rsc_PltAppScheme,
            self.DEF_shm__rsc__category__plf_app_lng_scheme: _shmObjResource.Rsc_PltAppLanScheme
        }

        self.VAR_shm__rsc__system_dict = {
            # bin > windows
            'bin@windows-python_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_language,
                self.DEF_shm__key__name: 'python',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows
            },
            'bin@windows-kmplayer_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                self.DEF_shm__key__name: 'KMPlayer',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows
            },
            'bin@windows-pdplayer64_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                self.DEF_shm__key__name: 'pdplayer64',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows
            },
            'bin@windows-sublime_text_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                self.DEF_shm__key__name: 'sublime_text',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows
            },
            'bin@windows-x64-rez_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                self.DEF_shm__key__name: 'rez',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows_x64
            },
            # package > windows-python
            'package@python-2.7-yaml': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'yaml',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            'package@python-2.7-chardet': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'chardet',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            'package@windows-python-2.7-pyqt5_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'PyQt5',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__python_27
            },
            'package@windows-python-2.7-pyside_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'PySide',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__python_27
            },
            'package@windows-python-2.7-pyside2': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'PySide2',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__python_27
            },
            'package@windows-python-2.7-materialx': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'MaterialX',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__python_27
            },
            'windows-python-2.7-pil': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'PIL',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__python_27
            },
            'windows-python-2.7-dingtalkchatbot': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'dingtalkchatbot',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__python_27
            },
            'windows-python-2.7-requests': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'requests',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__python_27
            },
            'windows-python-2.7-certifi': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'certifi',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__python_27
            },
            'windows-python-2.7-idna': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'idna',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__python_27
            },
            'windows-python-2.7-urllib3': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'urllib3',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__python_27
            },
            # package > windows-application-python
            # plug > window
            'windows-usd': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_plug,
                self.DEF_shm__key__name: 'usd',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows
            },
            # plug > windows-maya
            'windows-maya-lynxinode': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_plug,
                self.DEF_shm__key__name: 'lynxinode',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__maya
            },
            'windows-maya-2019-mtoa': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_plug,
                self.DEF_shm__key__name: 'mtoa',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__maya_2019
            },
            'windows-maya-2019-usd': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_plug,
                self.DEF_shm__key__name: 'usd',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__maya_2019
            },
            # plug > windows-houdini
            'windows-houdini-18-htoa': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_plug,
                self.DEF_shm__key__name: 'htoa',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__houdini_18
            },
            # module > share__python_27
            'module@python-2.7-lx_basic_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                self.DEF_shm__key__name: 'LxBasic',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            'module@python-2.7-lx_scheme_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                self.DEF_shm__key__name: 'LxScheme',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            'module@python-2.7-lx_preset_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                self.DEF_shm__key__name: 'LxPreset',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            'module@python-2.7-lx_app_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                self.DEF_shm__key__name: 'LxApp',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            'module@python-2.7-lx_core_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                self.DEF_shm__key__name: 'LxCore',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            'module@python-2.7-lx_gui_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                self.DEF_shm__key__name: 'LxGui',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            'module@python-2.7-lx_kit_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                self.DEF_shm__key__name: 'LxKit',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            'module@python-2.7-lx_database_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                self.DEF_shm__key__name: 'LxDatabase',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            'module@python-2.7-lx_deadline_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                self.DEF_shm__key__name: 'LxDeadline',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            'module@python-2.7-lx_data_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                self.DEF_shm__key__name: 'LxData',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            'module@python-2.7-lx_graphic_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                self.DEF_shm__key__name: 'LxGraphic',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            'module@python-2.7-lx_material_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                self.DEF_shm__key__name: 'LxMtx',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            'module@python-2.7-lx_usd_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                self.DEF_shm__key__name: 'LxUsd',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            'module@python-2.7-lx_usd2mtx_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                self.DEF_shm__key__name: 'LxUsd2mtx',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__python_27
            },
            # module > share__maya__python_27
            'module@python-2.7-lx_maya_basic_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                self.DEF_shm__key__name: 'LxMaBasic',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__maya__python_27
            },
            'module@python-2.7-lx_ma_core_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                self.DEF_shm__key__name: 'LxMaCore',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__maya__python_27
            },
            'module@python-2.7-lx_ma_material_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                self.DEF_shm__key__name: 'LxMa2mtx',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__maya__python_27
            },
            'module@python-2.7-lx_ma_kit_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                self.DEF_shm__key__name: 'LxMaInterface',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__maya__python_27
            },
            'module@python-2.7-lx_maya_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                self.DEF_shm__key__name: 'LxMaya',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__maya__python_27
            },
            # module > windows-houdini-python
            'module@python-2.7-lx_houdini_basic_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                self.DEF_shm__key__name: 'LxHouBasic',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__houdini__python_27
            },
            'module@python-2.7-lx_hou2mtx_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                self.DEF_shm__key__name: 'LxHou2mtx',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__houdini__python_27
            },
            'module@python-2.7-lx_houdini_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                self.DEF_shm__key__name: 'LxHoudini',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.platform__houdini__python_27
            },
            # scheme > windows-python
            'scheme@windows-default_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_scheme,
                self.DEF_shm__key__name: 'default',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows
            },
            # scheme > windows-maya-python
            'scheme@windows-maya-maya_default_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_scheme,
                self.DEF_shm__key__name: 'maya_default',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__maya
            },
            'scheme@windows-maya-2019-maya_2019': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_scheme,
                self.DEF_shm__key__name: 'maya_2019',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__maya_2019
            },
            # scheme > windows-houdini-python
            'windows-houdini-houdini_default_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_scheme,
                self.DEF_shm__key__name: 'houdini_default',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__houdini
            },
            'windows-houdini-18-houdini_18': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_scheme,
                self.DEF_shm__key__name: 'houdini_18',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.windows__houdini_18
            }
        }
        self.VAR_shm__rsc__version_dict = {
            # Bin
            'bin@windows-python_0': {
                self.Key_Record: ['2.7.13'],
                self.Key_Active: '2.7.13'
            },
            'bin@windows-kmplayer_0': {
                self.Key_Record: ['4.0.8.1'],
                self.Key_Active: '4.0.8.1'
            },
            'bin@windows-pdplayer64_0': {
                self.Key_Record: ['1.0.7.13'],
                self.Key_Active: '1.0.7.13'
            },
            'bin@windows-sublime_text_0': {
                self.Key_Record: ['1.0.0.1'],
                self.Key_Active: '1.0.0.1'
            },
            # Package
            'package@python-2.7-yaml': {
                self.Key_Record: ['3.13'],
                self.Key_Active: '3.13'
            },
            'package@python-2.7-chardet': {
                self.Key_Record: ['3.0.4'],
                self.Key_Active: '3.0.4'
            },
            'package@windows-python-2.7-pyqt5_0': {
                self.Key_Record: ['5.3.2'],
                self.Key_Active: '5.3.2'
            },
            'package@windows-python-2.7-pyside_0': {
                self.Key_Record: ['1.2.4'],
                self.Key_Active: '1.2.4'
            },
            'package@windows-python-2.7-pyside2': {
                self.Key_Record: ['2.0.0~alpha0'],
                self.Key_Active: '2.0.0~alpha0'
            },
            'package@windows-python-2.7-materialx': {
                self.Key_Record: ['1.36.5'],
                self.Key_Active: '1.36.5'
            },
            'windows-python-2.7-pil': {
                self.Key_Record: ['1.1.7'],
                self.Key_Active: '1.1.7'
            },
            'windows-python-2.7-dingtalkchatbot': {
                self.Key_Record: ['1.3.0'],
                self.Key_Active: '1.3.0'
            },
            'windows-python-2.7-requests': {
                self.Key_Record: ['2.22.0'],
                self.Key_Active: '2.22.0'
            },
            'windows-python-2.7-certifi': {
                self.Key_Record: ['2019.3.9'],
                self.Key_Active: '2019.3.9'
            },
            'windows-python-2.7-idna': {
                self.Key_Record: ['2.8'],
                self.Key_Active: '2.8'
            },
            'windows-python-2.7-urllib3': {
                self.Key_Record: ['1.25.2'],
                self.Key_Active: '1.25.2'
            },
            # plug > windows
            'windows-usd': {
                self.Key_Record: ['19.12'],
                self.Key_Active: '19.12'
            },
            # plug > windows-maya
            'windows-maya-2019-mtoa': {
                self.Key_Record: ['3.3.0.1', '4.0.3.1'],
                self.Key_Active: '3.3.0.1'
            },
            'windows-maya-2019-usd': {
                self.Key_Record: ['2.0'],
                self.Key_Active: '2.0'
            },
            # plug > windows-houdini
            'windows-houdini-18-htoa': {
                self.Key_Record: ['5.1.1', '5.3.0'],
                self.Key_Active: '5.1.1'
            }
        }
        self.VAR_shm__rsc__environ_dict = {
            # bin
            'bin@windows-python_0': {
                u'PATH': {
                    self.Key_Value: '{self.sourcepath}/bin',
                    self.Key_Operate: u'+'
                }
            },
            'bin@windows-kmplayer_0': {
                u'PATH': {
                    self.Key_Value: '{self.sourcepath}/bin',
                    self.Key_Operate: u'+'
                }
            },
            'bin@windows-pdplayer64_0': {
                u'PATH': {
                    self.Key_Value: '{self.sourcepath}/bin',
                    self.Key_Operate: u'+'
                }
            },
            'bin@windows-sublime_text_0': {
                u'PATH': {
                    self.Key_Value: '{self.sourcepath}/bin',
                    self.Key_Operate: u'+'
                }
            },
            # package
            'package@windows-python-2.7-pyside_0': {
                u'LYNXI_PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/lib',
                    self.Key_Operate: u'+'
                },
                u'PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/lib',
                    self.Key_Operate: u'+'
                },
                u'PATH': {
                    self.Key_Value: '{self.sourcepath}/bin',
                    self.Key_Operate: u'+'
                },
            },
            # plug > windows
            'windows-usd': {
                u'LYNXI_PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/lib/python',
                    self.Key_Operate: u'+'
                },
                u'PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/lib/python',
                    self.Key_Operate: u'+'
                },
                u'PATH': {
                    self.Key_Value: ['{self.sourcepath}/bin', '{self.sourcepath}/lib'],
                    self.Key_Operate: u'+'
                },
            },
            # plug > windows-maya
            'windows-maya-lynxinode': {
                self.Environ_Key_Loadname_Plug: {
                    self.Key_Value: [
                        u'lxConvertNode',
                        u'lxProductNode'
                    ],
                    self.Key_Operate: u'+'
                },
                u'LYNXI_PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                },
                u'PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                },
                u'MAYA_PLUG_IN_PATH': {
                    self.Key_Value: '{self.sourcepath}/plug-ins',
                    self.Key_Operate: u'+'
                },
                u'MAYA_SCRIPT_PATH': {
                    self.Key_Value: '{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                },
                u'XBMLANGPATH': {
                    self.Key_Value: '{self.sourcepath}/icons',
                    self.Key_Operate: u'+'
                }
            },
            'windows-maya-2019-mtoa': {
                self.Environ_Key_Loadname_Plug: {
                    self.Key_Value: u'mtoa',
                    self.Key_Operate: u'+'
                },
                u'LYNXI_PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                },
                u'PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                },
                #
                u'PATH': {
                    self.Key_Value: '{self.sourcepath}/bin',
                    self.Key_Operate: u'+'
                },
                u'MAYA_RENDER_DESC_PATH': {
                    self.Key_Value: '{self.sourcepath}',
                    self.Key_Operate: u'='
                },
                u'MAYA_PLUG_IN_PATH': {
                    self.Key_Value: '{self.sourcepath}/plug-ins',
                    self.Key_Operate: u'+'
                },
                u'MAYA_PLUG_IN_RESOURCE_PATH': {
                    self.Key_Value: '{self.sourcepath}/resources',
                    self.Key_Operate: u'+'
                },
                u'MAYA_PRESET_PATH': {
                    self.Key_Value: '{self.sourcepath}/presets',
                    self.Key_Operate: u'+'
                },
                u'MAYA_SCRIPT_PATH': {
                    self.Key_Value: ['{self.sourcepath}/scripts', '{self.sourcepath}/scripts/mtoa/mel'],
                    self.Key_Operate: u'+'
                },
                u'MAYA_CUSTOM_TEMPLATE_PATH': {
                    self.Key_Value: '{self.sourcepath}/scripts/mtoa/ui/templates',
                    self.Key_Operate: u'+'
                },
                u'XBMLANGPATH': {
                    self.Key_Value: '{self.sourcepath}/icons',
                    self.Key_Operate: u'+'
                },
                #
                u'ARNOLD_PLUGIN_PATH': {
                    self.Key_Value: [
                        '{self.sourcepath}/shaders',
                        '{self.sourcepath}/procedurals'
                    ],
                    self.Key_Operate: u'+'
                },
                u'MTOA_PATH': {
                    self.Key_Value: '{self.sourcepath}',
                    self.Key_Operate: u'+'
                },
                u'MTOA_EXTENSIONS_PATH': {
                    self.Key_Value: '{self.sourcepath}/extensions',
                    self.Key_Operate: u'+'
                },
                u'solidangle_LICENSE': {
                    self.Key_Value: '5053@192.168.16.240',
                    self.Key_Operate: u'='
                }
            },
            'windows-maya-2019-usd': {
                u'LYNXI_PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/lib/python',
                    self.Key_Operate: u'+'
                },
                u'PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/lib/python',
                    self.Key_Operate: u'+'
                },
                u'PATH': {
                    self.Key_Value: [
                        '{self.sourcepath}/bin',
                        '{self.sourcepath}/lib',
                        '{self.sourcepath}/third_party/maya/lib'
                    ],
                    self.Key_Operate: u'+'
                },
                u'MAYA_PLUG_IN_PATH': {
                    self.Key_Value: '{self.sourcepath}/third_party/maya/plugin',
                    self.Key_Operate: u'+'
                },
                u'MAYA_SCRIPT_PATH': {
                    self.Key_Value: [
                        '{self.sourcepath}/third_party/maya/lib/usd/usdMaya/resources',
                        '{self.sourcepath}/third_party/maya/plugin/pxrUsdPreviewSurface/resources'
                    ],
                    self.Key_Operate: u'+'
                },
                u'XBMLANGPATH': {
                    self.Key_Value: '{self.sourcepath}/third_party/maya/lib/usd/usdMaya/resources',
                    self.Key_Operate: u'+'
                }
            },
            # plug > windows-houdini
            'windows-houdini-18-htoa': {
                u'PATH': {
                    self.Key_Value: '{self.sourcepath}/scripts/bin',
                    self.Key_Operate: u'+'
                },
                u'HOUDINI_PATH': {
                    self.Key_Value: '{self.sourcepath};&',
                    self.Key_Operate: u';&'
                },
                u'solidangle_LICENSE': {
                    self.Key_Value: '5053@192.168.16.240',
                    self.Key_Operate: u'='
                }
            },
            # scheme > windows
            'scheme@windows-default_0': {
                u'LYNXI_PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                },
                u'PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                }
            },
            # scheme > windows-maya
            'scheme@windows-maya-maya_default_0': {
                u'LYNXI_PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                },
                u'PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                }
            },
            'scheme@windows-maya-2019-maya_2019': {
                u'LYNXI_PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                },
                u'PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                }
            }
        }
        self.VAR_shm__rsc__dependent_dict = {
            # package > windows-python
            'windows-python-2.7-dingtalkchatbot':
            {
                'requests': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'certifi': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'idna': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'urllib3': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            # module > windows-python
            'module@python-2.7-lx_basic_0': {
                'yaml': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'chardet': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'PIL': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_scheme_0': {
                'LxBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_preset_0': {
                'LxBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_app_0': {
                'LxBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxScheme': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxPreset': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_core_0': {
                'LxBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxScheme': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxPreset': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_gui_0': {
                'PySide2': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxScheme': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_database_0': {
                'LxCore': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_kit_0': {
                'LxCore': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxApp': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxGui': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxDatabase': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxDeadline': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            #
            'module@python-2.7-lx_data_0': {
                # Module
                'LxBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_graphic_0': {
                # Module
                'LxBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxData': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_material_0': {
                # Package
                'MaterialX': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                # Module
                'LxBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxData': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxGraphic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_usd_0': {
                # module > windows-python
                u'LxBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                u'LxData': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                u'LxGraphic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_usd2mtx_0': {
                # module > windows-python
                u'LxBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                u'LxData': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                u'LxGraphic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                u'LxMtx': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            # module > windows-maya-python
            'module@python-2.7-lx_maya_basic_0': {
                'LxBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxDatabase': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxDeadline': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_ma_core_0': {
                'LxCore': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxDatabase': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxDeadline': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_ma_material_0': {
                'LxMtx':
                    {
                        self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                        self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                        self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                    }
            },
            'module@python-2.7-lx_ma_kit_0': {
                'LxCore': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxKit': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxMaBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_maya_0': {
                'LxCore': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxDatabase': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxDeadline': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxMaBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxMaInterface': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxApp': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }

            },
            # module > windows-houdini-python
            'module@python-2.7-lx_houdini_basic_0': {
                # module
                'LxBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxGraphic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxUsd': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_hou2mtx_0': {
                'LxMtx': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxHouBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'module@python-2.7-lx_houdini_0': {
                # module > windows-python
                'LxApp': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxUsd2mtx': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                # module > windows-houdini-python
                'LxHouBasic': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxHou2mtx': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            # scheme > windows
            'scheme@windows-default_0': {
                # bin > windows
                'python': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_language,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'KMPlayer': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'pdplayer64': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'sublime_text': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                # plug >  windows
                'usd': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_plug,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                # module > python
                'LxKit': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            # scheme > windows-maya
            'scheme@windows-maya-maya_default_0': {
                # bin > windows
                'KMPlayer': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'pdplayer64': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'sublime_text': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                # module > windows-maya-python
                'LxMaya': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                # plug > windows-maya-python
                'lynxinode': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_plug,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'scheme@windows-maya-2019-maya_2019': {
                # bin > windows
                'KMPlayer': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'pdplayer64': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'sublime_text': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                # module > windows-python
                'LxMtx': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: {
                        '{system.application.version}': self.DEF_shm__keyword__share
                    }
                },
                # module > windows-maya-python
                'LxMa2mtx': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: {
                        '{system.application.version}': self.DEF_shm__keyword__share
                    }
                },
                'LxMaya': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: {
                        '{system.application.version}': self.DEF_shm__keyword__share
                    }
                },
                # plug > windows-maya-python
                'lynxinode': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_plug,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: {
                        '{system.application.version}': self.DEF_shm__keyword__share
                    }
                },
                # plug > windows-maya
                'mtoa': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_plug,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'usd': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_plug,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            # module > windows-houdini
            'windows-houdini-houdini_default_0': {
                # module
                'LxApp': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxHoudini': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            'windows-houdini-18-houdini_18': {
                # bin > windows
                'sublime_text': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                # module
                'LxHoudini': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: {
                        '{system.application.version}': self.DEF_shm__keyword__share
                    }
                },
                # plug
                'htoa': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_plug,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            }
        }

        self._initAbsShmRscBuilder(*args)
        
        # bscObjects.OsJsonFile(
        #     '/data/e/myworkspace/td/lynxi/workspace/module/windows-python-2.7/LxScheme/.data/windows-resource.json'
        # ).write(self._raw)


class LinuxResourceBuilder(shmObjAbs.Abs_ShmRscBuilder):
    def __init__(self, *args):
        self.VAR_shm__rsc__class_dict = {
            self.DEF_shm__rsc__category__plf_language: _shmObjResource.Rsc_PltLanguage,
            self.DEF_shm__rsc__category__plf_application: _shmObjResource.Rsc_PltApplication,

            self.DEF_shm__rsc__category__plf_lng_package: _shmObjResource.Rsc_PltLanPackage,
            self.DEF_shm__rsc__category__plf_app_lng_Package: _shmObjResource.Rsc_PltAppLanPackage,
            self.DEF_shm__rsc__category__plf_App_Package: _shmObjResource.Rsc_PltAppPackage,

            self.DEF_shm__rsc__category__plf_plug: _shmObjResource.Rsc_PltPlug,
            self.DEF_shm__rsc__category__plf_lng_plug: _shmObjResource.Rsc_PltLanPlug,
            self.DEF_shm__rsc__category__plf_app_lng_plug: _shmObjResource.Rsc_PltAppLanPlug,
            self.DEF_shm__rsc__category__plf_app_plug: _shmObjResource.Rsc_PltAppPlug,

            self.DEF_shm__rsc__category__plf_lng_module: _shmObjResource.Rsc_PltLanModule,
            self.DEF_shm__rsc__category__plf_app_lng_module: _shmObjResource.Rsc_PltAppLanModule,
            self.DEF_shm__rsc__category__plf_app_module: _shmObjResource.Rsc_PltAppModule,

            self.DEF_shm__rsc__category__plf_scheme: _shmObjResource.Rsc_PltScheme,
            self.DEF_shm__rsc__category__plf_lng_scheme: _shmObjResource.Rsc_PltLanScheme,
            self.DEF_shm__rsc__category__plf_app_scheme: _shmObjResource.Rsc_PltAppScheme,
            self.DEF_shm__rsc__category__plf_app_lng_scheme: _shmObjResource.Rsc_PltAppLanScheme
        }
        # system
        self.VAR_shm__rsc__system_dict = {
            # bin
            'bin@linux-x64-python': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                self.DEF_shm__key__name: 'python',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.linux_x64
            },
            'bin@linux-x64-sublime_text': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                self.DEF_shm__key__name: 'sublime_text',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.linux_x64
            },
            'bin@linux-x64-rez_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                self.DEF_shm__key__name: 'rez',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.linux_x64
            },
            # package
            'package@linux-x64-python-2.7-pil_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'PIL',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.linux_x64__python_27
            },
            'package@linux-x64-python-2.7-pyside2_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'PySide2',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.linux_x64__python_27
            },
            'package@linux-x64-python-2.7-pyqt5_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'PyQt5',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.linux_x64__python_27
            },
            'package@linux-python-2.7-materialx_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_package,
                self.DEF_shm__key__name: 'MaterialX',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.linux__python_27
            },
            # plug > linux
            'plug@linux-houdini-18-htoa': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_plug,
                self.DEF_shm__key__name: 'htoa',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.linux__houdini_18
            },
            # scheme > linux-x64
            'scheme@linu-x64-default_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_scheme,
                self.DEF_shm__key__name: 'default',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.linux_x64
            },
            # scheme > linux-x64-houdini
            'scheme@linu-x64-houdini-houdini_default_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_scheme,
                self.DEF_shm__key__name: 'houdini_default',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.linux_x64__houdini
            },
            'scheme@linu-x64-houdini-18-houdini_18_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_scheme,
                self.DEF_shm__key__name: 'houdini_18',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.linux_x64__houdini_18
            },
            # scheme > linux-x64-maya
            'scheme@linu-x64-maya-maya_default_0': {
                self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_scheme,
                self.DEF_shm__key__name: 'maya_default',
                self.DEF_shm__key__system: shmCfg.ShmSystemArgument.linux_x64__maya
            }

        }
        # version
        self.VAR_shm__rsc__version_dict = {
            # bin
            'bin@linux-x64-python': {
                self.Key_Record: ['2.7.18'],
                self.Key_Active: '2.7.18'
            },
            'bin@linux-x64-sublime_text': {
                self.Key_Record: ['build.3211'],
                self.Key_Active: 'build.3211'
            },
            # package
            'package@linux-x64-python-2.7-pil_0': {
                self.Key_Record: ['1.1.7'],
                self.Key_Active: '1.1.7'
            },
            'package@linux-x64-python-2.7-pyside2_0': {
                self.Key_Record: ['5.14.2.1'],
                self.Key_Active: '5.14.2.1'
            },
            'package@linux-x64-python-2.7-pyqt5_0': {
                self.Key_Record: ['5.6', '5.7'],
                self.Key_Active: '5.7'
            },
            'package@linux-python-2.7-materialx_0': {
                self.Key_Record: ['1.37.1'],
                self.Key_Active: '1.37.1'
            },
            # plug > linux
            'plug@linux-houdini-18-htoa': {
                self.Key_Record: ['5.3.0'],
                self.Key_Active: '5.3.0'
            }
        }
        # environ
        self.VAR_shm__rsc__environ_dict = {
            # bin
            'bin@linux-x64-sublime_text': {
                u'PATH': {
                    self.Key_Value: '{self.sourcepath}/bin',
                    self.Key_Operate: u'+'
                }
            },
            'bin@linux-x64-rez_0': {
                u'PATH': {
                    self.Key_Value: '{self.sourcepath}/bin/rez',
                    self.Key_Operate: u'+'
                },
                u'LYNXI_PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/lib/python2.7/site-packages',
                    self.Key_Operate: u'+'
                }
            },
            # plug > linux-houdini-18
            'plug@linux-houdini-18-htoa': {
                u'PATH': {
                    self.Key_Value: '{self.sourcepath}/scripts/bin',
                    self.Key_Operate: u'+'
                },
                u'HOUDINI_PATH': {
                    self.Key_Value: '{self.sourcepath}:&',
                    self.Key_Operate: u';&'
                },
                u'solidangle_LICENSE': {
                    self.Key_Value: '5053@192.168.16.240',
                    self.Key_Operate: u'='
                }
            },
            # scheme > linux-x64-houdini-18
            'scheme@linu-x64-houdini-18-houdini_18_0': {
                u'HOUDINI_PATH': {
                    self.Key_Value: '{self.sourcepath}/{self.name}/lynxi/houdini:&',
                    self.Key_Operate: u';&'
                },
            },
            'scheme@linu-x64-maya-maya_default_0': {
                u'LYNXI_PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/{self.name}/lynxi/maya/scripts',
                    self.Key_Operate: u'+'
                },
                u'PYTHONPATH': {
                    self.Key_Value: '{self.sourcepath}/{self.name}/lynxi/maya/scripts',
                    self.Key_Operate: u'+'
                }
            }
        }
        # dependent
        self.VAR_shm__rsc__dependent_dict = {
            # scheme > linux-x64
            'scheme@linu-x64-default_0': {
                # bin
                'python': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_language,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'sublime_text': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_language,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                # module > python
                'LxKit': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            # scheme > linux-x64-houdini
            'scheme@linu-x64-houdini-houdini_default_0': {
                'sublime_text': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                # module
                'LxApp': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxKit': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxHoudini': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            # scheme > linux-x64-houdini-18
            'scheme@linu-x64-houdini-18-houdini_18_0': {
                # bin > windows
                'sublime_text': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxKit': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                'LxHoudini': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                # plug
                'htoa': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_plug,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            },
            # scheme > linux-64-maya
            'scheme@linu-x64-maya-maya_default_0': {
                # bin
                'sublime_text': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_application,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                # module
                'LxKit': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                # app module
                'LxMaya': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_lng_module,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                },
                # plug
                'lynxinode': {
                    self.DEF_shm__key__category: self.DEF_shm__rsc__category__plf_app_plug,
                    self.DEF_shm__key__version: self.DEF_shm_keyword__version_active,
                    self.DEF_shm__key__system: self.DEF_shm_keyword__system_active
                }
            }
        }

        self._initAbsShmRscBuilder(*args)
