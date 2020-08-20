# coding:utf-8
from LxScheme import shmOutput

from .. import appCfg, appObjAbs

from . import _appObjObject


class AppPlatform(appObjAbs.AbsAppPlatform):
    def __init__(self, *args):
        self._initAbsAppPlatform(*args)


class AppApplication(appObjAbs.AbsAppApplication):
    def __init__(self, *args):
        self._initAbsAppApplication(*args)


class AppAppkitSystem(appObjAbs.AbsAppSystem):
    CLS_app__system__platform = AppPlatform
    CLS_app__system__application = AppApplication

    def __init__(self, *args):
        self._initAbsAppSystem(*args)


class AppToolkitSystem(appObjAbs.AbsAppSystem):
    CLS_app__system__platform = AppPlatform
    CLS_app__system__application = AppApplication

    def __init__(self, *args):
        self._initAbsAppSystem(*args)


class AppConfig(appObjAbs.AbsAppConfig):
    def __init__(self, *args):
        self._initAbsAppConfig(*args)


class AppTool(appObjAbs.AbsAppTool):
    CLS_app__tool__config = AppConfig

    def __init__(self, *args):
        self._initAbsAppTool(*args)


class AppAppkit(appObjAbs.AbsAppKit):
    CLS_app__kit__system = AppToolkitSystem
    CLS_app__kit__config = AppConfig

    CLS_app__kit__tag_tree = _appObjObject.AppTagTree
    CLS_app__kit__tool_stack = _appObjObject.AppToolStack
    CLS_app__kit__tool = AppTool

    IST_app__kit__root = shmOutput.Root.kit

    VAR_app__kit__folder_name = appCfg.AppUtility.DEF_app__folder__kit
    VAR_app__kit__sub_folder_name = appCfg.AppUtility.DEF_app__folder__appkit
    VAR_app__kit__file_name = u'app.config.json'

    VAR_app__kit__tag_config_file = appCfg.AppUtility.DEF_app__config_file__appkit_tag

    def __init__(self, *args):
        self._initAbsAppKit(*args)


class AppToolkit(appObjAbs.AbsAppKit):
    CLS_app__kit__system = AppToolkitSystem
    CLS_app__kit__config = AppConfig

    CLS_app__kit__tag_tree = _appObjObject.AppTagTree
    CLS_app__kit__tool_stack = _appObjObject.AppToolStack
    CLS_app__kit__tool = AppTool

    IST_app__kit__root = shmOutput.Root.kit

    VAR_app__kit__folder_name = appCfg.AppUtility.DEF_app__folder__kit
    VAR_app__kit__sub_folder_name = appCfg.AppUtility.DEF_app__folder__toolkit
    VAR_app__kit__file_name = u'tool.config.json'

    VAR_app__kit__tag_config_file = appCfg.AppUtility.DEF_app__config_file__toolkit_tag

    def __init__(self, *args):
        self._initAbsAppKit(*args)
