# coding:utf-8
from LxCore import lxCore_

from LxScheme.shmObjects import _shmResource


class ResourcePreset(lxCore_.Basic):
    def __init__(self):
        self.def_cls_resource_dic = {
            self.Category_Plf_Language: _shmResource.Rsc_PltLanguage,
            self.Category_Plf_Application: _shmResource.Rsc_PltApplication,

            self.Category_Plf_Lan_Package: _shmResource.Rsc_PltLanPackage,
            self.Category_Plf_App_Lan_Package: _shmResource.Rsc_PltAppLanPackage,
            self.Category_Plf_App_Package: _shmResource.Rsc_PltAppPackage,

            self.Category_Plf_Lan_Plug: _shmResource.Rsc_PltLanPlug,
            self.Category_Plf_App_Lan_Plug: _shmResource.Rsc_PltAppLanPlug,
            self.Category_Plf_App_Plug: _shmResource.Rsc_PltAppPlug,

            self.Category_Plf_Lan_Module: _shmResource.Rsc_PltLanModule,
            self.Category_Plf_App_Lan_Module: _shmResource.Rsc_PltAppLanModule,
            self.Category_Plf_App_Module: _shmResource.Rsc_PltAppModule,

            self.Category_Plf_Lan_Scheme: _shmResource.Rsc_PltLanScheme,
            self.Category_Plf_App_Lan_Scheme: _shmResource.Rsc_PltAppLanScheme
        }
        self.def_argument_resource_dic = {
            self.Category_Plf_Language: [
                '{system.platform.name}', '{system.platform.version}'
            ],
            self.Category_Plf_Application: [
                '{system.platform.name}', '{system.platform.version}'
            ],
            # Package
            self.Category_Plf_Lan_Package: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.Category_Plf_App_Lan_Package: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.Category_Plf_App_Package: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}'
            ],
            # Module
            self.Category_Plf_Lan_Module: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.Category_Plf_App_Lan_Module: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.Category_Plf_App_Module: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}'
            ],
            # Scheme
            self.Category_Plf_Lan_Scheme: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.Category_Plf_App_Lan_Scheme: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}',
                '{system.language.name}', '{system.language.version}'
            ]
        }

        self.Def_Resource_Dic = {
            # Bin
            'windows-python': {
                self.Key_Category: self.Category_Plf_Language,
                self.Key_Name: 'python',
                self.Key_System: [
                    'windows', 'share'
                ]
            },
            'windows-kmplayer': {
                self.Key_Category: self.Category_Plf_Application,
                self.Key_Name: 'KMPlayer',
                self.Key_System: [
                    'windows', 'share'
                ]
            },
            'windows-pdplayer64': {
                self.Key_Category: self.Category_Plf_Application,
                self.Key_Name: 'pdplayer64',
                self.Key_System: [
                    'windows', 'share'
                ]
            },
            'windows-sublime_text': {
                self.Key_Category: self.Category_Plf_Application,
                self.Key_Name: 'sublime_text',
                self.Key_System: [
                    'windows', 'share'
                ]
            },
            # Package
            'python27_yaml': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.Key_Name: 'yaml',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'python27_chardet': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.Key_Name: 'chardet',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'python27_pyqt5': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.Key_Name: 'PyQt5',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'python27_materialx': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.Key_Name: 'MaterialX',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'python27_pil': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.Key_Name: 'PIL',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'python27_dingtalkchatbot': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.Key_Name: 'dingtalkchatbot',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'python27_requests': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.Key_Name: 'requests',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'python27_certifi': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.Key_Name: 'certifi',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'python27_idna': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.Key_Name: 'idna',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'python27_urllib3': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.Key_Name: 'urllib3',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            # Platform Application Plug
            'maya_lynxinode': {
                self.Key_Category: self.Category_Plf_App_Plug,
                self.Key_Name: 'lynxinode',
                self.Key_System: [
                    'windows', 'share', 'maya', 'share'
                ]
            },
            'maya_2019_arnold': {
                self.Key_Category: self.Category_Plf_App_Plug,
                self.Key_Name: 'mtoa',
                self.Key_System: [
                    'windows', 'share', 'maya', '2019'
                ]
            },
            # Platform Language Module
            'lx_basic_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.Key_Name: 'LxBasic',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lx_scheme_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.Key_Name: 'LxScheme',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lxcore_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.Key_Name: 'LxCore',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lxui_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.Key_Name: 'LxUi',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lxinterface_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.Key_Name: 'LxInterface',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lxdatabase_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.Key_Name: 'LxDatabase',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lx_material_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.Key_Name: 'LxMaterial',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lxdeadline_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.Key_Name: 'LxDeadline',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            # Platform Application Language Module
            'lx_ma_core_0': {
                self.Key_Category: self.Category_Plf_App_Lan_Module,
                self.Key_Name: 'LxMaCore',
                self.Key_System: [
                    'windows', 'share', 'maya', 'share', 'python', '2.7.x'
                ]
            },
            'lx_ma_material_0': {
                self.Key_Category: self.Category_Plf_App_Lan_Module,
                self.Key_Name: 'LxMaMaterial',
                self.Key_System: [
                    'windows', 'share', 'maya', 'share', 'python', '2.7.x'
                ]
            },
            'lx_ma_interface_0': {
                self.Key_Category: self.Category_Plf_App_Lan_Module,
                self.Key_Name: 'LxMaInterface',
                self.Key_System: [
                    'windows', 'share', 'maya', 'share', 'python', '2.7.x'
                ]
            },
            'lx_maya_0': {
                self.Key_Category: self.Category_Plf_App_Lan_Module,
                self.Key_Name: 'LxMaya',
                self.Key_System: [
                    'windows', 'share', 'maya', 'share', 'python', '2.7.x'
                ]
            },
            # Platform Language Scheme
            'windows_scheme_0': {
                self.Key_Category: self.Category_Plf_Lan_Scheme,
                self.Key_Name: 'default',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'windows_maya_scheme_0': {
                self.Key_Category: self.Category_Plf_App_Lan_Scheme,
                self.Key_Name: 'maya_default',
                self.Key_System: [
                    'windows', 'share', 'maya', 'share', 'python', '2.7.x'
                ]
            }
        }
        self.Def_Version_Dic = {
            # Bin
            'windows-python': {
                self.Key_Record: ['2.7.13'],
                self.Key_Active: '2.7.13'
            },
            'windows-kmplayer': {
                self.Key_Record: ['4.0.8.1'],
                self.Key_Active: '4.0.8.1'
            },
            'windows-pdplayer64': {
                self.Key_Record: ['1.0.7.13'],
                self.Key_Active: '1.0.7.13'
            },
            'windows-sublime_text': {
                self.Key_Record: ['1.0.0.1'],
                self.Key_Active: '1.0.0.1'
            },
            # Package
            'python27_yaml': {
                self.Key_Record: ['3.13'],
                self.Key_Active: '3.13'
            },
            'python27_chardet': {
                self.Key_Record: ['3.0.4'],
                self.Key_Active: '3.0.4'
            },
            'python27_pyqt5': {
                self.Key_Record: ['5.3.2'],
                self.Key_Active: '5.3.2'
            },
            'python27_materialx': {
                self.Key_Record: ['1.36.5'],
                self.Key_Active: '1.36.5'
            },
            'python27_pil': {
                self.Key_Record: ['1.1.7'],
                self.Key_Active: '1.1.7'
            },
            'python27_dingtalkchatbot': {
                self.Key_Record: ['1.3.0'],
                self.Key_Active: '1.3.0'
            },
            'python27_requests': {
                self.Key_Record: ['2.22.0'],
                self.Key_Active: '2.22.0'
            },
            'python27_certifi': {
                self.Key_Record: ['2019.3.9'],
                self.Key_Active: '2019.3.9'
            },
            'python27_idna': {
                self.Key_Record: ['2.8'],
                self.Key_Active: '2.8'
            },
            'python27_urllib3': {
                self.Key_Record: ['1.25.2'],
                self.Key_Active: '1.25.2'
            },
            # Plug
            'maya_2019_arnold': {
                self.Key_Record: ['3.3.0.1'],
                self.Key_Active: '3.3.0.1'
            }
        }
        self.Def_Environ_Dic = {
            # Bin
            'windows-python': {
                'PATH': {
                    self.Key_Value: u'{self.sourcepath}/bin',
                    self.Key_Operate: u'+'
                }
            },
            'windows-kmplayer': {
                'PATH': {
                    self.Key_Value: u'{self.sourcepath}/bin',
                    self.Key_Operate: u'+'
                }
            },
            'windows-pdplayer64': {
                'PATH': {
                    self.Key_Value: u'{self.sourcepath}/bin',
                    self.Key_Operate: u'+'
                }
            },
            'windows-sublime_text': {
                'PATH': {
                    self.Key_Value: u'{self.sourcepath}/bin',
                    self.Key_Operate: u'+'
                }
            },
            # Plug
            'maya_2019_arnold': {
                'MAYA_RENDER_DESC_PATH': {
                    self.Key_Value: u'{self.sourcepath}',
                    self.Key_Operate: u'='
                },
                'solidangle_LICENSE': {
                    self.Key_Value: u'5053@192.168.16.240',
                    self.Key_Operate: u'='
                },
                'PATH': {
                    self.Key_Value: u'{self.sourcepath}/bin',
                    self.Key_Operate: u'+'
                },
                'MAYA_PLUG_IN_PATH': {
                    self.Key_Value: u'{self.sourcepath}/plug-ins',
                    self.Key_Operate: u'+'
                },
                'MAYA_SCRIPT_PATH': {
                    self.Key_Value: u'{self.sourcepath}/scripts/mtoa/mel',
                    self.Key_Operate: u'+'
                },
                'MAYA_CUSTOM_TEMPLATE_PATH': {
                    self.Key_Value: u'{self.sourcepath}/scripts/mtoa/ui/templates',
                    self.Key_Operate: u'+'
                },
                'ARNOLD_PLUGIN_PATH': {
                    self.Key_Value: u'{self.sourcepath}/shaders',
                    self.Key_Operate: u'+'
                },
                'MTOA_EXTENSIONS_PATH': {
                    self.Key_Value: u'{self.sourcepath}/extensions',
                    self.Key_Operate: u'+'
                }
            },
            'maya_lynxinode': {
                'MAYA_PLUG_IN_PATH': {
                    self.Key_Value: u'{self.sourcepath}/plug-ins',
                    self.Key_Operate: u'+'
                },
                'MAYA_SCRIPT_PATH': {
                    self.Key_Value: u'{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                },
                'PYTHONPATH': {
                    self.Key_Value: u'{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                },
                'XBMLANGPATH': {
                    self.Key_Value: u'{self.sourcepath}/icons',
                    self.Key_Operate: u'+'
                }
            },
            # Scheme
            'windows_maya_scheme_0': {
                'PYTHONPATH': {
                    self.Key_Value: u'{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                }
            }
        }
        self.Def_Dependent_Dic = {
            # Package
            'python27_dingtalkchatbot':
            {
                'requests': {
                    self.Key_Category: self.Category_Plf_Lan_Package,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'certifi': {
                    self.Key_Category: self.Category_Plf_Lan_Package,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'idna': {
                    self.Key_Category: self.Category_Plf_Lan_Package,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'urllib3': {
                    self.Key_Category: self.Category_Plf_Lan_Package,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            # Platform Language Module
            'lx_basic_0': {
                'yaml': {
                    self.Key_Category: self.Category_Plf_Lan_Package,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'chardet': {
                    self.Key_Category: self.Category_Plf_Lan_Package,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'dingtalkchatbot': {
                    self.Key_Category: self.Category_Plf_Lan_Package,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'PIL': {
                    self.Key_Category: self.Category_Plf_Lan_Package,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'lx_scheme_0': {
                'LxBasic': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'lxcore_0': {
                'LxBasic': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxScheme': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'lxui_0': {
                'PyQt5': {
                    self.Key_Category: self.Category_Plf_Lan_Package,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxCore': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'lxdatabase_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'lxgraph_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'lxinterface_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxUi': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxDatabase': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxDeadline': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'lx_material_0': {
                'MaterialX': {
                    self.Key_Category: self.Category_Plf_Lan_Package,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxCore': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            # Platform Application Language Module
            'lx_ma_core_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxDatabase': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxDeadline': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'lx_ma_material_0': {
                'LxMaterial':
                    {
                        self.Key_Category: self.Category_Plf_Lan_Module,
                        self.Key_Version: self.Keyword_Version_Active,
                        self.Key_System: self.Keyword_System_Active
                    }
            },
            'lx_ma_interface_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxInterface': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxMaCore': {
                    self.Key_Category: self.Category_Plf_App_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxMaya': {
                    self.Key_Category: self.Category_Plf_App_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'lx_maya_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxDatabase': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxDeadline': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            # Scheme
            'windows_scheme_0': {
                'python': {
                    self.Key_Category: self.Category_Plf_Language,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'KMPlayer': {
                    self.Key_Category: self.Category_Plf_Application,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'pdplayer64': {
                    self.Key_Category: self.Category_Plf_Application,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'sublime_text': {
                    self.Key_Category: self.Category_Plf_Application,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxInterface': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'windows_maya_scheme_0': {
                'KMPlayer': {
                    self.Key_Category: self.Category_Plf_Application,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'pdplayer64': {
                    self.Key_Category: self.Category_Plf_Application,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'sublime_text': {
                    self.Key_Category: self.Category_Plf_Application,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxMaInterface': {
                    self.Key_Category: self.Category_Plf_App_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'lynxinode': {
                    self.Key_Category: self.Category_Plf_App_Plug,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            }
        }

    def resources(self):
        lis = []

        for k, v in self.Def_Resource_Dic.items():
            category = v[self.Key_Category]
            name = v[self.Key_Name]
            argument = v[self.Key_System]
            cls = self.def_cls_resource_dic[category]

            resource_ = cls(name, *argument)
            if k in self.Def_Version_Dic:
                resource_.version.create(self.Def_Version_Dic[k])

            if k in self.Def_Environ_Dic:
                resource_.environ.create(self.Def_Environ_Dic[k])

            if k in self.Def_Dependent_Dic:
                resource_.dependent.create(self.Def_Dependent_Dic[k])

            lis.append(resource_)
            print resource_

        return lis

    def createDefConfigCaches(self):
        if self.resources():
            for i in self.resources():
                i.createServerCache()

    def createDefDevelopDirectories(self):
        if self.resources():
            for i in self.resources():
                i.createDevelopDirectories()

    def createDevelopSourceDirectories(self):
        if self.resources():
            for i in self.resources():
                i.createDevelopSourceDirectories()
