# coding:utf-8
from LxCore import lxBasic, lxConfigure

from LxCore.definition import abstract, resource


class ResourcePreset(lxConfigure.Basic):
    def __init__(self):
        self.Def_Cls_Config_Dic = {
            self.Category_Windows_Bin: resource.Cfg_WinApplication,
            self.Category_Windows_Python_Module: resource.Cfg_WinPythonModule,
            self.Category_Windows_App_Python_Module: resource.Cfg_WinAppPythonModule,
            self.Category_Windows_Python_Package: resource.Cfg_WindowsPythonPackage,
            self.Category_Windows_App_Python_Package: resource.Cfg_WinAppPythonPackage,
            self.Category_Windows_App_Plug: resource.Cfg_WinAppPlug
        }
        self.Def_Preset_Dic = {
            # Windows Bin
            self.Category_Windows_Bin: {
                'python_0': ('python', 'share')
            },
            # Windows Python Package
            self.Category_Windows_Python_Package: {
                'yaml_0': ('yaml', '2.7.x'),
                'chardet_0': ('chardet', '2.7.x'),
                'dingtalkchatbot_0': ('dingtalkchatbot', '2.7.x'),
                'pyqt5_0': ('PyQt5', '2.7.x'),
                'materialx_0': ('MaterialX', '2.7.x')
            },
            # Windows Python Module
            self.Category_Windows_Python_Module: {
                'lxcommand_0': ('LxCommand', '2.7.x'),
                'lxcore_0': ('LxCore', '2.7.x'),
                'lxui_0': ('LxUi', '2.7.x'),
                'lxinterface_0': ('LxInterface', '2.7.x'),
                'lxdatabase_0': ('LxDatabase', '2.7.x'),
                'lxgraph_0': ('LxGraph', '2.7.x'),
                'lxmaterial_0': ('LxMaterial', '2.7.x'),
                'lxdeadline_0': ('LxDeadline', '2.7.x'),
                'lxwindows_0': ('LxWindows', '2.7.x')
            },
            self.Category_Windows_App_Python_Module: {
                'lxmaya_0': ('LxMaya', 'maya', 'share')
            },
            # Windows App Plug
            self.Category_Windows_App_Plug: {
                'lynxinode_0': ('lynxinode', 'maya', 'share'),
                'arnold_2019': ('mtoa', 'maya', '2019')
            }
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
                        self.Key_Value: u'{sourcepath}',
                        self.Key_Operate: u'='
                    },
                    'solidangle_LICENSE': {
                        self.Key_Value: u'5053@192.168.16.240',
                        self.Key_Operate: u'='
                    },
                    'PATH': {
                        self.Key_Value: u'{sourcepath}/bin',
                        self.Key_Operate: u'+'
                    },
                    'ARNOLD_PLUGIN_PATH': {
                        self.Key_Value: u'{sourcepath}/shaders',
                        self.Key_Operate: u'+'
                    },
                    'MTOA_EXTENSIONS_PATH': {
                        self.Key_Value: u'{sourcepath}/extensions',
                        self.Key_Operate: u'+'
                    },
                    'MAYA_SCRIPT_PATH': {
                        self.Key_Value: u'{sourcepath}/scripts/mtoa/mel',
                        self.Key_Operate: u'+'
                    },
                    'MAYA_CUSTOM_TEMPLATE_PATH': {
                        self.Key_Value: u'{sourcepath}/scripts/mtoa/ui/templates',
                        self.Key_Operate: u'+'
                    }
                }
        }
        self.Def_Dependent_Dic = {
            'lxcore_0': {
                self.Category_Windows_Python_Package: {
                    'yaml': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    },
                    'chardet': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    },
                    'dingtalkchatbot': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    }
                }
            },
            'lxui_0': {
                self.Category_Windows_Python_Package: {
                    'PyQt5': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    }
                },
                self.Category_Windows_Python_Module: {
                    'LxCore': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    }
                }
            },
            'lxdatabase_0': {
                self.Category_Windows_Python_Module: {
                    'LxCore': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    }
                }
            },
            'lxgraph_0': {
                self.Category_Windows_Python_Module: {
                    'LxCore': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    }
                }
            },
            'lxinterface_0': {
                self.Category_Windows_Python_Module: {
                    'LxCore': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    },
                    'LxUi': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    }
                }
            },
            'lxwindows_0': {
                self.Category_Windows_Bin: {
                    'python': {
                        self.Key_Argument: 'share'
                    }
                },
                self.Category_Windows_Python_Module: {
                    'LxCore': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    },
                    'LxUi': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    },
                    'LxInterface': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    }
                }
            },
            'lxmaya_0': {
                self.Category_Windows_Python_Module: {
                    'LxCore': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    },
                    'LxUi': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    },
                    'LxInterface': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    },
                    'LxDatabase': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    },
                    'LxDeadline': {
                        self.Key_Argument: u'2.7.x',
                        self.Key_Version: u'active'
                    }
                }
            }
        }

    def defConfigs(self):
        lis = []

        for k, v in self.Def_Preset_Dic.items():
            for ik, iv in v.items():
                cls = self.Def_Cls_Config_Dic[k]

                config = cls(*iv)
                if ik in self.Def_Version_Dic:
                    config.version().create(
                        {
                            self.Key_Record: self.Def_Version_Dic[ik][0],
                            self.Key_Active: self.Def_Version_Dic[ik][1]
                        }
                    )

                if ik in self.Def_Environ_Dic:
                    config.environ().create(
                        self.Def_Environ_Dic[ik]
                    )

                if ik in self.Def_Dependent_Dic:
                    config.dependent().create(
                        self.Def_Dependent_Dic[ik]
                    )

                lis.append(config)
                # print config

        return lis

    def createDefConfigCaches(self):
        if self.defConfigs():
            for i in self.defConfigs():
                i.createCache()

    def createDefDevelopDirectories(self):
        if self.defConfigs():
            for i in self.defConfigs():
                i.createDevelopDirectories()

