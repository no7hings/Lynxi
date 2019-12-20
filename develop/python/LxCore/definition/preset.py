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

        self.Def_Preset_Dic = {
            # Windows Bin
            self.Category_Plt_Language: {
                'python_0': ('python', 'windows', 'share')
            },
            # Windows Python Package
            self.Category_Plt_Lan_Package: {
                # Python Package
                'yaml_0': ('yaml', 'windows', 'share', 'python', '2.7.x'),
                'chardet_0': ('chardet', 'windows', 'share', 'python', '2.7.x'),
                'dingtalkchatbot_0': ('dingtalkchatbot', 'windows', 'share', 'python', '2.7.x'),
                'pyqt5_0': ('PyQt5', 'windows', 'share', 'python', '2.7.x'),
                'materialx_0': ('MaterialX', 'windows', 'share', 'python', '2.7.x'),
            },
            self.Category_Plt_App_Package: {
                'lynxinode_0': ('lynxinode', 'windows', 'share', 'maya', 'share'),
                'arnold_2019': ('mtoa', 'windows', 'share', 'maya', '2019')
            },
            # Windows Python Module
            self.Category_Plt_Lan_Module: {
                'lxcommand_0': ('LxCommand', 'windows', 'share', 'python', '2.7.x'),
                'lxcore_0': ('LxCore', 'windows', 'share', 'python', '2.7.x'),
                'lxui_0': ('LxUi', 'windows', 'share', 'python', '2.7.x'),
                'lxinterface_0': ('LxInterface', 'windows', 'share', 'python', '2.7.x'),
                'lxdatabase_0': ('LxDatabase', 'windows', 'share', 'python', '2.7.x'),
                'lxgraph_0': ('LxGraph', 'windows', 'share', 'python', '2.7.x'),
                'lxmaterial_0': ('LxMaterial', 'windows', 'share', 'python', '2.7.x'),
                'lxdeadline_0': ('LxDeadline', 'windows', 'share', 'python', '2.7.x')
            },
            self.Category_Plt_App_Lan_Module: {
                'lxmaya_0': ('LxMaya', 'windows', 'share', 'maya', 'share', 'python', '2.7.x')
            },
        }
        self.Def_Version_Dic = {
            'python_0': (['2.7.13'], '2.7.13'),
            'yaml_0': (['3.13'], '3.13'),
            'chardet_0': (['3.0.4'], '3.0.4'),
            'dingtalkchatbot_0': (['1.3.0'], '1.3.0'),
            'pyqt5_0': (['5.3.2'], '5.3.2'),
            'materialx_0': (['1.36.5'], '1.36.5'),
            'arnold_2019': (['3.3.0.1'], '3.3.0.1')
        }
        self.Def_Environ_Dic = {
            'arnold_2019': {
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
            'python_0': {
                self.Key_Environ_Python_Bin_Path: {
                    self.Key_Value: u'{self.sourcepath}/python.exe',
                    self.Key_Operate: u'='
                }
            }
        }
        self.Def_Dependent_Dic = {
            'lxcore_0': {
                'yaml': {
                    self.Key_Category: self.Category_Plt_Lan_Package,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                },
                'chardet': {
                    self.Key_Category: self.Category_Plt_Lan_Package,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                },
                'dingtalkchatbot': {
                    self.Key_Category: self.Category_Plt_Lan_Package,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                }
            },
            'lxui_0': {
                'PyQt5': {
                    self.Key_Category: self.Category_Plt_Lan_Package,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                },
                'LxCore': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                }
            },
            'lxdatabase_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                }
            },
            'lxgraph_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                }
            },
            'lxinterface_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                },
                'LxUi': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                }
            },
            'lxmaterial_0': {
                'MaterialX': {
                    self.Key_Category: self.Category_Plt_Lan_Package,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                },
                'LxCore': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                }
            },
            'lxmaya_0': {
                'LxCore': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                },
                'LxUi': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                },
                'LxInterface': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                },
                'LxDatabase': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                },
                'LxDeadline': {
                    self.Key_Category: self.Category_Plt_Lan_Module,
                    self.Key_Version: u'active',
                    self.Key_Argument: [
                        '{system.platform.name}',
                        '{system.platform.version}',
                        '{system.name}',
                        '{system.version}'
                    ]
                }
            }
        }

    def resources(self):
        lis = []

        for k, v in self.Def_Preset_Dic.items():
            for ik, iv in v.items():
                cls = self.Def_Cls_Config_Dic[k]

                resource_ = cls(*iv)
                if ik in self.Def_Version_Dic:
                    resource_.version.create(
                        {
                            self.Key_Record: self.Def_Version_Dic[ik][0],
                            self.Key_Active: self.Def_Version_Dic[ik][1]
                        }
                    )

                if ik in self.Def_Environ_Dic:
                    resource_.environ.create(
                        self.Def_Environ_Dic[ik]
                    )

                if ik in self.Def_Dependent_Dic:
                    resource_.dependent.create(
                        self.Def_Dependent_Dic[ik]
                    )

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
