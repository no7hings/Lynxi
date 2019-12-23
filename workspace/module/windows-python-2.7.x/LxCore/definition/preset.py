# coding:utf-8
from LxCore import lxConfigure

from LxCore.definition import resource


class ResourcePreset(lxConfigure.Basic):
    def __init__(self):
        self.Def_Cls_Config_Dic = {
            self.Category_Plt_Language: resource.Rsc_PltLanguage,
            self.Category_Plt_Application: resource.Rsc_PltApplication,

            self.Category_Plt_Lan_Package: resource.Rsc_PltLanPackage,
            self.Category_Plt_App_Lan_Package: resource.Rsc_PltAppLanPackage,

            self.Category_Plt_App_Package: resource.Rsc_PltAppPackage,

            self.Category_Plt_Lan_Module: resource.Rsc_PltLanModule,
            self.Category_Plt_App_Lan_Module: resource.Rsc_PltAppLanModule,

            self.Category_Plt_App_Module: resource.Rsc_PltAppModule,

            self.Category_Plt_Lan_Scheme: resource.Rsc_PltLanScheme,
            self.Category_Plt_App_Lan_Scheme: resource.Rsc_PltAppLanScheme
        }

        self.Def_Resource_Dic = {
            # Bin
            'python_27': {
                self.Key_Category: self.Category_Plt_Language,
                self.Key_Name: 'python',
                self.Key_Argument: [
                    'windows', 'share'
                ]
            },
            # Package
            'python27_yaml': {
                self.Key_Category: self.Category_Plt_Lan_Package,
                self.Key_Name: 'yaml',
                self.Key_Argument: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'python27_chardet': {
                self.Key_Category: self.Category_Plt_Lan_Package,
                self.Key_Name: 'chardet',
                self.Key_Argument: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'python27_dingtalkchatbot': {
                self.Key_Category: self.Category_Plt_Lan_Package,
                self.Key_Name: 'dingtalkchatbot',
                self.Key_Argument: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'python27_pyqt5': {
                self.Key_Category: self.Category_Plt_Lan_Package,
                self.Key_Name: 'PyQt5',
                self.Key_Argument: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'python27_materialx': {
                self.Key_Category: self.Category_Plt_Lan_Package,
                self.Key_Name: 'MaterialX',
                self.Key_Argument: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'python27_lynxinode': {
                self.Key_Category: self.Category_Plt_App_Package,
                self.Key_Name: 'lynxinode',
                self.Key_Argument: [
                    'windows', 'share', 'maya', 'share'
                ]
            },
            'python27_arnold': {
                self.Key_Category: self.Category_Plt_App_Package,
                self.Key_Name: 'mtoa',
                self.Key_Argument: [
                    'windows', 'share', 'maya', '2019'
                ]
            },
            # Module
            'lxcommand_0': {
                self.Key_Category: self.Category_Plt_Lan_Module,
                self.Key_Name: 'LxCommand',
                self.Key_Argument: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lxcore_0': {
                self.Key_Category: self.Category_Plt_Lan_Module,
                self.Key_Name: 'LxCore',
                self.Key_Argument: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lxui_0': {
                self.Key_Category: self.Category_Plt_Lan_Module,
                self.Key_Name: 'LxUi',
                self.Key_Argument: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lxinterface_0': {
                self.Key_Category: self.Category_Plt_Lan_Module,
                self.Key_Name: 'LxInterface',
                self.Key_Argument: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lxdatabase_0': {
                self.Key_Category: self.Category_Plt_Lan_Module,
                self.Key_Name: 'LxDatabase',
                self.Key_Argument: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lxgraph_0': {
                self.Key_Category: self.Category_Plt_Lan_Module,
                self.Key_Name: 'LxGraph',
                self.Key_Argument: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lxmaterial_0': {
                self.Key_Category: self.Category_Plt_Lan_Module,
                self.Key_Name: 'LxMaterial',
                self.Key_Argument: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lxdeadline_0': {
                self.Key_Category: self.Category_Plt_Lan_Module,
                self.Key_Name: 'LxDeadline',
                self.Key_Argument: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'lxmaya_0': {
                self.Key_Category: self.Category_Plt_App_Lan_Module,
                self.Key_Name: 'LxMaya',
                self.Key_Argument: [
                    'windows', 'share', 'maya', 'share', 'python', '2.7.x'
                ]
            },
            # Scheme
            'windows_scheme_0': {
                self.Key_Category: self.Category_Plt_Lan_Scheme,
                self.Key_Name: 'default',
                self.Key_Argument: [
                    'windows', 'share', 'python', '2.7.x'
                ]
            },
            'windows_maya_scheme_0': {
                self.Key_Category: self.Category_Plt_App_Lan_Scheme,
                self.Key_Name: 'maya_default',
                self.Key_Argument: [
                    'windows', 'share', 'maya', 'share', 'python', '2.7.x'
                ]
            }
        }
        self.Def_Version_Dic = {
            'python_27': {
                self.Key_Record: ['2.7.13'],
                self.Key_Active: '2.7.13'
            },
            'python27_yaml': {
                self.Key_Record: ['3.13'],
                self.Key_Active: '3.13'
            },
            'python27_chardet': {
                self.Key_Record: ['3.0.4'],
                self.Key_Active: '3.0.4'
            },
            'python27_dingtalkchatbot': {
                self.Key_Record: ['1.3.0'],
                self.Key_Active: '1.3.0'
            },
            'python27_pyqt5': {
                self.Key_Record: ['5.3.2'],
                self.Key_Active: '5.3.2'
            },
            'python27_materialx': {
                self.Key_Record: ['1.36.5'],
                self.Key_Active: '1.36.5'
            },
            'python27_arnold': {
                self.Key_Record: ['3.3.0.1'],
                self.Key_Active: '3.3.0.1'
            }
        }
        self.Def_Environ_Dic = {
            'python27_arnold': {
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
                    'ARNOLD_PLUGIN_PATH': {
                        self.Key_Value: u'{self.sourcepath}/shaders',
                        self.Key_Operate: u'+'
                    },
                    'MTOA_EXTENSIONS_PATH': {
                        self.Key_Value: u'{self.sourcepath}/extensions',
                        self.Key_Operate: u'+'
                    },
                    'MAYA_SCRIPT_PATH': {
                        self.Key_Value: u'{self.sourcepath}/scripts/mtoa/mel',
                        self.Key_Operate: u'+'
                    },
                    'MAYA_CUSTOM_TEMPLATE_PATH': {
                        self.Key_Value: u'{self.sourcepath}/scripts/mtoa/ui/templates',
                        self.Key_Operate: u'+'
                    }
                },
            'python_27': {
                self.Key_Environ_Python_Bin_Path: {
                    self.Key_Value: u'{self.sourcepath}/python.exe',
                    self.Key_Operate: u'='
                }
            }
        }
        self.Def_Dependent_Dic = {
            # Module
            'lxcore_0': {
                'yaml': {
                    self.Key_Category: self.Category_Plt_Lan_Package,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                },
                'chardet': {
                    self.Key_Category: self.Category_Plt_Lan_Package,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                },
                'dingtalkchatbot': {
                    self.Key_Category: self.Category_Plt_Lan_Package,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                }
            },
            'lxui_0': {
                'PyQt5': {
                    self.Key_Category: self.Category_Plt_Lan_Package,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                },
                'LxCore': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                }
            },
            'lxdatabase_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                }
            },
            'lxgraph_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                }
            },
            'lxinterface_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                },
                'LxUi': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                },
                'LxDatabase': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                },
                'LxDeadline': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                }
            },
            'lxmaterial_0': {
                'MaterialX': {
                    self.Key_Category: self.Category_Plt_Lan_Package,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                },
                'LxCore': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                }
            },
            'lxmaya_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                },
                'LxInterface': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                },
                'LxDatabase': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                },
                'LxDeadline': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                }
            },
            # Scheme
            'windows_scheme_0': {
                'LxInterface': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.name}', '{system.version}'
                    ]
                }
            },
            'windows_maya_scheme_0': {
                'LxMaya': {
                    self.Key_Category: self.Category_Plt_App_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}', '{system.platform.version}',
                        '{system.application.name}', '{system.application.version}',
                        '{system.name}', '{system.version}'
                    ]
                }
            }
        }

    def resources(self):
        lis = []

        for k, v in self.Def_Resource_Dic.items():
            category = v[self.Key_Category]
            name = v[self.Key_Name]
            argument = v[self.Key_Argument]
            cls = self.Def_Cls_Config_Dic[category]

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
