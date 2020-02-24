# coding:utf-8
from LxScheme import shmConfigure

from LxScheme.shmObjects import _shmObjResource


class Resource(shmConfigure.Utility):
    def __init__(self):
        self.def_cls_resource_dic = {
            self.Category_Plf_Language: _shmObjResource.Rsc_PltLanguage,
            self.Category_Plf_Application: _shmObjResource.Rsc_PltApplication,

            self.Category_Plf_Lan_Package: _shmObjResource.Rsc_PltLanPackage,
            self.Category_Plf_App_Lan_Package: _shmObjResource.Rsc_PltAppLanPackage,
            self.Category_Plf_App_Package: _shmObjResource.Rsc_PltAppPackage,

            self.Category_Plf_Lan_Plug: _shmObjResource.Rsc_PltLanPlug,
            self.Category_Plf_App_Lan_Plug: _shmObjResource.Rsc_PltAppLanPlug,
            self.Category_Plf_App_Plug: _shmObjResource.Rsc_PltAppPlug,

            self.Category_Plf_Lan_Module: _shmObjResource.Rsc_PltLanModule,
            self.Category_Plf_App_Lan_Module: _shmObjResource.Rsc_PltAppLanModule,
            self.Category_Plf_App_Module: _shmObjResource.Rsc_PltAppModule,

            self.Category_Plf_Lan_Scheme: _shmObjResource.Rsc_PltLanScheme,
            self.Category_Plf_App_Lan_Scheme: _shmObjResource.Rsc_PltAppLanScheme
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

        self.def_resource_dic = {
            # Bin
            'windows-python': {
                self.Key_Category: self.Category_Plf_Language,
                self.DEF_key_name: 'python',
                self.Key_System: [
                    'windows', 'share'
                ]
            },
            'windows-kmplayer': {
                self.Key_Category: self.Category_Plf_Application,
                self.DEF_key_name: 'KMPlayer',
                self.Key_System: [
                    'windows', 'share'
                ]
            },
            'windows-pdplayer64': {
                self.Key_Category: self.Category_Plf_Application,
                self.DEF_key_name: 'pdplayer64',
                self.Key_System: [
                    'windows', 'share'
                ]
            },
            'windows-sublime_text': {
                self.Key_Category: self.Category_Plf_Application,
                self.DEF_key_name: 'sublime_text',
                self.Key_System: [
                    'windows', 'share'
                ]
            },
            # Package
            'py-2.7-yaml': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.DEF_key_name: 'yaml',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'py-2.7-chardet': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.DEF_key_name: 'chardet',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'py-27-pyqt5': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.DEF_key_name: 'PyQt5',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'py-27-pyside2': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.DEF_key_name: 'PySide2',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'py-2.7-materialx': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.DEF_key_name: 'MaterialX',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'py-2.7-pil': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.DEF_key_name: 'PIL',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'py-2.7-dingtalkchatbot': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.DEF_key_name: 'dingtalkchatbot',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'py-2.7-requests': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.DEF_key_name: 'requests',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'py-2.7-certifi': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.DEF_key_name: 'certifi',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'py-2.7-idna': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.DEF_key_name: 'idna',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'py-2.7-urllib3': {
                self.Key_Category: self.Category_Plf_Lan_Package,
                self.DEF_key_name: 'urllib3',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            # Platform Application Plug
            'maya-lynxinode': {
                self.Key_Category: self.Category_Plf_App_Plug,
                self.DEF_key_name: 'lynxinode',
                self.Key_System: [
                    'windows', 'share', 'maya', 'share'
                ]
            },
            'windows-ma-2019-arnold': {
                self.Key_Category: self.Category_Plf_App_Plug,
                self.DEF_key_name: 'mtoa',
                self.Key_System: [
                    'windows', 'share', 'maya', '2019'
                ]
            },
            # Platform Language Module
            'lx-basic_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.DEF_key_name: 'LxBasic',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lx-scheme_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.DEF_key_name: 'LxScheme',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lx-preset_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.DEF_key_name: 'LxPreset',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lx-app_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.DEF_key_name: 'LxApp',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lx-core_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.DEF_key_name: 'LxCore',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lx-ui_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.DEF_key_name: 'LxUi',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lx-interface_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.DEF_key_name: 'LxInterface',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lx-database_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.DEF_key_name: 'LxDatabase',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lx-material_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.DEF_key_name: 'LxMaterial',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lx-deadline_0': {
                self.Key_Category: self.Category_Plf_Lan_Module,
                self.DEF_key_name: 'LxDeadline',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            # Platform Application Language Module
            'lx-maya-basic_0': {
                self.Key_Category: self.Category_Plf_App_Lan_Module,
                self.DEF_key_name: 'LxMaBasic',
                self.Key_System: [
                    'windows', 'share', 'maya', 'share', 'python', '2.7.x'
                ]
            },
            'lx-ma_core_0': {
                self.Key_Category: self.Category_Plf_App_Lan_Module,
                self.DEF_key_name: 'LxMaCore',
                self.Key_System: [
                    'windows', 'share', 'maya', 'share', 'python', '2.7.x'
                ]
            },
            'lx-ma-material_0': {
                self.Key_Category: self.Category_Plf_App_Lan_Module,
                self.DEF_key_name: 'LxMaMaterial',
                self.Key_System: [
                    'windows', 'share', 'maya', 'share', 'python', '2.7.x'
                ]
            },
            'lx-ma-interface_0': {
                self.Key_Category: self.Category_Plf_App_Lan_Module,
                self.DEF_key_name: 'LxMaInterface',
                self.Key_System: [
                    'windows', 'share', 'maya', 'share', 'python', '2.7.x'
                ]
            },
            'lx-maya_0': {
                self.Key_Category: self.Category_Plf_App_Lan_Module,
                self.DEF_key_name: 'LxMaya',
                self.Key_System: [
                    'windows', 'share', 'maya', 'share', 'python', '2.7.x'
                ]
            },
            # Platform Language Scheme
            'windows-scheme_0': {
                self.Key_Category: self.Category_Plf_Lan_Scheme,
                self.DEF_key_name: 'default',
                self.Key_System: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'windows-maya-scheme_0': {
                self.Key_Category: self.Category_Plf_App_Lan_Scheme,
                self.DEF_key_name: 'maya_default',
                self.Key_System: [
                    'windows', 'share', 'maya', 'share', 'python', '2.7.x'
                ]
            },
            'windows-maya-2019-scheme_0': {
                self.Key_Category: self.Category_Plf_App_Lan_Scheme,
                self.DEF_key_name: 'maya_2019_arnold',
                self.Key_System: [
                    'windows', 'share', 'maya', '2019', 'python', '2.7.x'
                ]
            }
        }
        self.def_version_dic = {
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
            'py-2.7-yaml': {
                self.Key_Record: ['3.13'],
                self.Key_Active: '3.13'
            },
            'py-2.7-chardet': {
                self.Key_Record: ['3.0.4'],
                self.Key_Active: '3.0.4'
            },
            'py-27-pyqt5': {
                self.Key_Record: ['5.3.2'],
                self.Key_Active: '5.3.2'
            },
            'py-27-pyside2': {
                self.Key_Record: ['2.0.0~alpha0'],
                self.Key_Active: '2.0.0~alpha0'
            },
            'py-2.7-materialx': {
                self.Key_Record: ['1.36.5'],
                self.Key_Active: '1.36.5'
            },
            'py-2.7-pil': {
                self.Key_Record: ['1.1.7'],
                self.Key_Active: '1.1.7'
            },
            'py-2.7-dingtalkchatbot': {
                self.Key_Record: ['1.3.0'],
                self.Key_Active: '1.3.0'
            },
            'py-2.7-requests': {
                self.Key_Record: ['2.22.0'],
                self.Key_Active: '2.22.0'
            },
            'py-2.7-certifi': {
                self.Key_Record: ['2019.3.9'],
                self.Key_Active: '2019.3.9'
            },
            'py-2.7-idna': {
                self.Key_Record: ['2.8'],
                self.Key_Active: '2.8'
            },
            'py-2.7-urllib3': {
                self.Key_Record: ['1.25.2'],
                self.Key_Active: '1.25.2'
            },
            # Plug
            'windows-ma-2019-arnold': {
                self.Key_Record: ['3.3.0.1'],
                self.Key_Active: '3.3.0.1'
            }
        }
        self.def_environ_dic = {
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
            'windows-ma-2019-arnold': {
                self.Environ_Key_Loadname_Plug: {
                    self.Key_Value: u'mtoa',
                    self.Key_Operate: u'+'
                },
                'MAYA_RENDER_DESC_PATH': {
                    self.Key_Value: u'{self.sourcepath}',
                    self.Key_Operate: u'='
                },
                'PATH': {
                    self.Key_Value: u'{self.sourcepath}/bin',
                    self.Key_Operate: u'+'
                },
                'SYSTEM_PATH': {
                    self.Key_Value: u'{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                },
                'MAYA_PLUG_IN_PATH': {
                    self.Key_Value: u'{self.sourcepath}/plug-ins',
                    self.Key_Operate: u'+'
                },
                'MAYA_PLUG_IN_RESOURCE_PATH': {
                    self.Key_Value: u'{self.sourcepath}/resources',
                    self.Key_Operate: u'+'
                },
                'MAYA_PRESET_PATH': {
                    self.Key_Value: u'{self.sourcepath}/presets',
                    self.Key_Operate: u'+'
                },
                'MAYA_SCRIPT_PATH': {
                    self.Key_Value: u'{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                },
                'XBMLANGPATH': {
                    self.Key_Value: u'{self.sourcepath}/icons',
                    self.Key_Operate: u'+'
                },
                'ARNOLD_PLUGIN_PATH': {
                    self.Key_Value: [
                        u'{self.sourcepath}/shaders',
                        u'{self.sourcepath}/procedurals'
                    ],
                    self.Key_Operate: u'+'
                },
                'MTOA_PATH': {
                    self.Key_Value: u'{self.sourcepath}',
                    self.Key_Operate: u'+'
                },
                'MTOA_EXTENSIONS_PATH': {
                    self.Key_Value: u'{self.sourcepath}/extensions',
                    self.Key_Operate: u'+'
                },
                'solidangle_LICENSE': {
                    self.Key_Value: u'5053@192.168.16.240',
                    self.Key_Operate: u'='
                }
            },
            'maya-lynxinode': {
                self.Environ_Key_Loadname_Plug: {
                    self.Key_Value: [
                        u'lxConvertNode',
                        u'lxProductNode'
                    ],
                    self.Key_Operate: u'+'
                },
                'MAYA_PLUG_IN_PATH': {
                    self.Key_Value: u'{self.sourcepath}/plug-ins',
                    self.Key_Operate: u'+'
                },
                'MAYA_SCRIPT_PATH': {
                    self.Key_Value: u'{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                },
                'SYSTEM_PATH': {
                    self.Key_Value: u'{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                },
                'XBMLANGPATH': {
                    self.Key_Value: u'{self.sourcepath}/icons',
                    self.Key_Operate: u'+'
                }
            },
            # Scheme
            'windows-scheme_0': {
                'SYSTEM_PATH': {
                    self.Key_Value: u'{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                }
            },
            'windows-maya-scheme_0': {
                'SYSTEM_PATH': {
                    self.Key_Value: u'{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                }
            },
            'windows-maya-2019-scheme_0': {
                'SYSTEM_PATH': {
                    self.Key_Value: u'{self.sourcepath}/scripts',
                    self.Key_Operate: u'+'
                }
            }
        }
        self.def_dependent_dic = {
            # Package
            'py-2.7-dingtalkchatbot':
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
            'lx-basic_0': {
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
            'lx-scheme_0': {
                'LxBasic': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'lx-preset_0': {
                'LxBasic': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'lx-app_0': {
                'LxBasic': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxScheme': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxPreset': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'lx-core_0': {
                'LxBasic': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxScheme': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxPreset': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'lx-ui_0': {
                'PyQt5': {
                    self.Key_Category: self.Category_Plf_Lan_Package,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxCore': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxApp': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'lx-database_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxApp': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            'lx-interface_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxApp': {
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
            'lx-material_0': {
                'MaterialX': {
                    self.Key_Category: self.Category_Plf_Lan_Package,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxBasic': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            # Platform Application Language Module
            'lx-maya-basic_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxBasic': {
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
            'lx-ma_core_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                },
                'LxBasic': {
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
            'lx-ma-material_0': {
                'LxMaterial':
                    {
                        self.Key_Category: self.Category_Plf_Lan_Module,
                        self.Key_Version: self.Keyword_Version_Active,
                        self.Key_System: self.Keyword_System_Active
                    }
            },
            'lx-ma-interface_0': {
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
                'LxMaBasic': {
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
            'lx-maya_0': {
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
                },
                'LxMaBasic': {
                    self.Key_Category: self.Category_Plf_App_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            },
            # Scheme
            'windows-scheme_0': {
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
            'windows-maya-scheme_0': {
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
            },
            'windows-maya-2019-scheme_0': {
                # Bin
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
                # Module
                'LxMaterial': {
                    self.Key_Category: self.Category_Plf_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: {
                        '{system.application.version}': self.Keyword_Share
                    }
                },
                # Application Module
                'LxMaInterface': {
                    self.Key_Category: self.Category_Plf_App_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: {
                        '{system.application.version}': self.Keyword_Share
                    }
                },
                'LxMaMaterial': {
                    self.Key_Category: self.Category_Plf_App_Lan_Module,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: {
                        '{system.application.version}': self.Keyword_Share
                    }
                },
                'lynxinode': {
                    self.Key_Category: self.Category_Plf_App_Plug,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: {
                        '{system.application.version}': self.Keyword_Share
                    }
                },
                # Plug
                'mtoa': {
                    self.Key_Category: self.Category_Plf_App_Plug,
                    self.Key_Version: self.Keyword_Version_Active,
                    self.Key_System: self.Keyword_System_Active
                }
            }
        }

    def resources(self):
        lis = []

        for k, v in self.def_resource_dic.items():
            category = v[self.Key_Category]
            name = v[self.DEF_key_name]
            argument = v[self.Key_System]
            cls = self.def_cls_resource_dic[category]

            resource_ = cls(name, *argument)
            if k in self.def_version_dic:
                resource_.version.create(self.def_version_dic[k])

            if k in self.def_environ_dic:
                resource_.environ.create(self.def_environ_dic[k])

            if k in self.def_dependent_dic:
                resource_.dependent.create(self.def_dependent_dic[k])

            lis.append(resource_)

        return lis

    def schemes(self):
        lis = []
        for i in self.resources():
            if i.isScheme:
                lis.append(i)
        return lis

    def modules(self):
        lis = []
        for i in self.resources():
            if i.isModule:
                lis.append(i)
        return lis

    def packages(self):
        lis = []
        for i in self.resources():
            if i.isPackage:
                lis.append(i)
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
