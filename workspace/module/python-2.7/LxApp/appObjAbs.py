# coding:utf-8
from LxBasic import bscObjItf, bscMethods

from LxScheme import shmCfg

from . import appCfg


class AbsAppBasic(appCfg.AppUtility):
    @property
    def raw(self):
        return {}


class AbsAppObjStack(bscObjItf.ItfBscObjStack):
    def _initAbsAppObjStack(self, *args):
        self._initItfBscObjStack(*args)


class AbsAppObjDef(object):
    def _initAbsAppObjDef(self, *args):
        self._objNameStr, self._objVersionStr = args

    @property
    def name(self):
        return self._objNameStr

    @property
    def version(self):
        return self._objVersionStr

    def __str__(self):
        return '{}(name="{}", version="{}")'.format(
            self.__class__.__name__,
            self.name,
            self.version
        )

    def __repr__(self):
        return self.__str__()


class AbsAppPlatform(
    AbsAppBasic,
    AbsAppObjDef
):
    # noinspection PyUnusedLocal
    def _initAbsAppPlatform(self, *args):
        self._initAbsAppObjDef(
            *self._platform_cls__get_info_()
        )

    @staticmethod
    def _platform_cls__get_info_():
        nameStr, versionStr = None, None
        if bscMethods.WindowsPlatform.isActive():
            nameStr = bscMethods.WindowsPlatform.name()
            versionStr = bscMethods.WindowsPlatform.version()
        elif bscMethods.LinuxPlatform.isActive():
            nameStr = bscMethods.LinuxPlatform.name()
            versionStr = bscMethods.LinuxPlatform.version()
        return nameStr, versionStr

    def runCommand(self, *args):
        cmdStr = args[0]
        return self.MOD_commands.getoutput(
            cmdStr
        )


class AbsAppApplication(
    AbsAppBasic,
    AbsAppObjDef
):
    # noinspection PyUnusedLocal
    def _initAbsAppApplication(self, *args):
        self._initAbsAppObjDef(
            *self._application_cls__get_info_()
        )

    @staticmethod
    def _application_cls__get_info_():
        nameStr, versionStr = None, None
        if bscMethods.MayaApp.isActive():
            nameStr = bscMethods.MayaApp.name()
            versionStr = bscMethods.MayaApp.version()
        elif bscMethods.HoudiniApp.isActive():
            nameStr = bscMethods.HoudiniApp.name()
            versionStr = bscMethods.HoudiniApp.version()
        return nameStr, versionStr


class AbsAppProject(object):
    pass


class AbsAppLanguage(AbsAppBasic):
    def _initAbsAppLanguage(self, *args):
        pass


class AbsAppSystem(AbsAppBasic):
    CLS_app__system__platform = None
    CLS_app__system__application = None

    # noinspection PyUnusedLocal
    def _initAbsAppSystem(self, *args):
        self._platformObj = self.CLS_app__system__platform()
        self._applicationObj = self.CLS_app__system__application()

    @property
    def platform(self):
        if self._platformObj.name is not None:
            return self._platformObj

    @property
    def application(self):
        if self._applicationObj.name is not None:
            return self._applicationObj

    @classmethod
    def _app_system_cls__get_folder_str_(cls, *args):
        strList = [i for i in args if i != cls.DEF_app__keyword__share] or [cls.DEF_app__keyword__share]
        return u'-'.join(
            strList
        )

    def searchFolderNameStrings(self):
        lis = []
        args = [
            self.platform.name, self.platform.version
        ]
        if self.application is not None:
            args = [
                self.platform.name, self.platform.version,
                self.application.name, self.application.version
            ]

        _lis = []
        for i in args:
            if i == self.DEF_app__keyword__share:
                _lis.append([self.DEF_app__keyword__share])
            else:
                _lis.append([self.DEF_app__keyword__share, i])

        pathArgs = bscMethods.NestedArray.mapTo(_lis)
        for i in pathArgs:
            lis.append(
                self._app_system_cls__get_folder_str_(*i)
            )
        return lis

    def __str__(self):
        return u'{}(platform={}, application={})'.format(
            self.__class__.__name__,
            self.platform,
            self.application
        )


class AbsAppConfig(AbsAppBasic):
    VAR_app__config__filename = None

    def _initAbsAppConfig(self, *args):
        _ = args[0]
        if isinstance(_, (str, unicode)):
            self._filepathStr = _
            self._dirpathStr = bscMethods.OsJsonFile.dirname(self._filepathStr)
            self._raw = bscMethods.OsJsonFile.read(self._filepathStr) or {}
        elif isinstance(_, dict):
            self._filepathStr = None
            self._dirpathStr = None
            self._raw = _

    def saveConfig(self):
        pass

    @property
    def dirpath(self):
        return self._dirpathStr

    @property
    def filepath(self):
        return self._filepathStr

    def get(self, keyStr, default=None):
        return self._raw.get(keyStr, default)

    def raw(self):
        raise self._raw


class AbsAppTagObj(bscObjItf.ItfBscNode):
    def _initAbsAppTagObj(self, *args):
        self._initItfBscNode(*args)


class AbsAppTool(AbsAppBasic):
    CLS_app__tool__config = None

    def _initAbsAppTool(self, *args):
        self._toolkitObj, configArgs = args
        self._configObj = self.CLS_app__tool__config(*configArgs)

        self._pathStr = None
        self._tagpathStr = None

        # self._app__tool__set_build_()

    def _app__tool__set_build_(self):
        bscMethods.OsEnviron.add(
            shmCfg.ShmUtility.DEF_util__environ_key__paths_source,
            self.sourcepath
        )

    @property
    def path(self):
        return self._pathStr

    @path.setter
    def path(self, *args):
        self._pathStr = args[0]

    @property
    def tagpath(self):
        return self._tagpathStr

    @tagpath.setter
    def tagpath(self, *args):
        self._tagpathStr = args[0]

    @property
    def enable(self):
        return self._configObj.get(self.DEF_app__key__enable)

    @property
    def type(self):
        return self._configObj.get(self.DEF_app__key__type)

    @property
    def tag(self):
        return self._configObj.get(self.DEF_app__key__tag)

    @property
    def name(self):
        return self._configObj.get(self.DEF_app__key__name)

    @property
    def uiname(self):
        return self._configObj.get(self.DEF_app__key__uiname)

    @property
    def project(self):
        return self._configObj.get(self.DEF_app__key__project)

    @property
    def color(self):
        return self._configObj.get(
            self.DEF_app__key__color,
            [127, 127, 127, 255]
        )

    @property
    def version(self):
        return self._configObj.get(self.DEF_app__key__version)

    @property
    def icon(self):
        return self._configObj.get(self.DEF_app__key__icon).format(**self._format_dict_())

    @property
    def tip(self):
        return self._configObj.get(self.DEF_app__key__tip)

    @property
    def toolkit(self):
        return self._toolkitObj

    @property
    def root(self):
        return self._toolkitObj.root

    @property
    def sourcepath(self):
        return u'{}/{}/{}'.format(
            self._configObj.dirpath,
            self.version,
            self.DEF_app__keyword__source
        )

    @property
    def config_filepath(self):
        return self._configObj.dirpath

    @property
    def python_main_filepath(self):
        return u'{}/{}'.format(self.sourcepath, u'main.py')

    @property
    def python_main_command(self):
        filepathStr = self.python_main_filepath
        if bscMethods.OsPath.isExist(filepathStr):
            raw = bscMethods.OsFile.read(filepathStr)
            if bscMethods.MayaApp.isActive():
                return 'python(' + bscMethods.OsJsonFile.dump(raw) + ');'
            return filepathStr
        return 'print "no command to executable.\r\n"'

    @property
    def python_setup_filepath(self):
        return u'{}/{}/{}'.format(self.sourcepath, u'script', u'setup.py')

    @property
    def python_setup_command(self):
        filepathStr = self.python_setup_filepath
        if bscMethods.OsPath.isExist(filepathStr):
            raw = bscMethods.OsFile.read(filepathStr)
            if bscMethods.MayaApp.isActive():
                return 'python(' + bscMethods.OsJsonFile.dump(raw) + ');'
            return filepathStr
        return 'print "no command to executable.\r\n"'

    def _format_dict_(self):
        return {
            self.DEF_app__keyword__self: self,
        }

    def __str__(self):
        return u'{}(name="{}", version="{}")'.format(
            self.__class__.__name__,
            self.name,
            self.version
        )

    def __repr__(self):
        return self.__str__()


class AbsAppKit(AbsAppBasic):
    CLS_app__kit__system = None

    CLS_app__kit__config = None

    CLS_app__kit__tag_tree = None
    CLS_app__kit__tool_stack = None
    CLS_app__kit__tool = None

    IST_app__kit__root = None

    VAR_app__kit__folder_name = None
    VAR_app__kit__sub_folder_name = None
    VAR_app__kit__file_name = None

    VAR_app__kit__tag_config_file = None

    # noinspection PyUnusedLocal
    def _initAbsAppKit(self, *args):
        if args:
            self._projectNameStr = args[0]

        self._systemObj = self.CLS_app__kit__system()
        self._rootObj = self.IST_app__kit__root

        self._toolStackObj = self.CLS_app__kit__tool_stack(self)
        self._userToolStackObj = self.CLS_app__kit__tool_stack(self)

        self._app__kit__set_build_()

    def _app__kit__set_build_(self):
        self._app__kit__set_tag_objs_build_()
        self._app__kit__set_tool_objs_build_()

    @property
    def system(self):
        return self._systemObj

    @property
    def root(self):
        return self._rootObj

    @property
    def path(self):
        return u'{}/{}/{}'.format(
            self._rootObj.server,
            self.VAR_app__kit__folder_name,
            self.VAR_app__kit__sub_folder_name
        )

    @property
    def user_path(self):
        return u'{}/{}/{}/{}'.format(
            self._rootObj.local,
            bscMethods.OsPlatform.username(),
            self.VAR_app__kit__folder_name,
            self.VAR_app__kit__sub_folder_name
        )

    # tag ************************************************************************************************************ #
    def _app__kit__set_tag_objs_build_(self):
        self._tagTreeObj = self.CLS_app__kit__tag_tree(
            self.VAR_app__kit__tag_config_file
        )

    def tags(self):
        return self._tagTreeObj.nodes()

    def tag(self, *args):
        return self._tagTreeObj.node(*args)

    # tool *********************************************************************************************************** #
    def _app__kit__get_tool_config_filepath_str_list_(self, pathStr):
        lis = []
        for folderNameStr in self._systemObj.searchFolderNameStrings():
            dirpathStr = bscMethods.OsPath.cleanupTo(
                u'{}/{}'.format(
                    pathStr,
                    folderNameStr
                )
            )
            globStr = u'{}/*/{}'.format(dirpathStr, self.VAR_app__kit__file_name)

            configFilepathStrList = self.MOD_glob.glob(globStr)

            for configFilepathStr in configFilepathStrList:
                lis.append(
                    bscMethods.OsPath.cleanupTo(configFilepathStr)
                )
        return lis

    def _app__kit__set_tool_objs_build_(self):
        for i in self._app__kit__get_tool_config_filepath_str_list_(self.path):
            toolObj = self.CLS_app__kit__tool(self, (i, ))
            tagpathStrList = toolObj.tag
            for tagpathStr in tagpathStrList:
                toolObj.tagpath = tagpathStr
                #
                nameStr = toolObj.name
                pathStr = '/'.join([tagpathStr, nameStr])
                toolObj.path = pathStr
                self._toolStackObj.addObject(toolObj)

    def tools(self, **kwargs):
        return self._toolStackObj.objects(**kwargs)

    def hasTools(self, **kwargs):
        return self._toolStackObj.hasObjects(**kwargs)

    def tool(self, *args):
        pass

