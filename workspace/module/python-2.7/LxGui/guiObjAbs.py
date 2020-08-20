# coding:utf-8
from LxBasic import bscCfg, bscMethods


class AbsGuiIcon(object):
    def _initAbsGuiIcon(self, *args):
        self._keyStr, self._ospathStr = args

    @property
    def key(self):
        return self._keyStr

    @property
    def ospath(self):
        return self._ospathStr

    def __str__(self):
        return u'{}(key="{}", ospath="{}")'.format(
            self.__class__.__name__,
            self.key,
            self.ospath
        )

    def __repr__(self):
        return self.__str__()


class AbsGuiIconLoader(object):
    CLS_gui__icon_loader__icon_stack = None
    CLS_gui__icon_loader__icon = None
    VAR_gui__icon_loader__environ_key = None

    def _initAbsGuiIconLoader(self, *args):
        self._iconStackObj = self.CLS_gui__icon_loader__icon_stack(self)

        self._gui__icon_loader__set_build_()

    def _gui__icon_loader__get_search_path_str_lit_(self):
        return bscMethods.OsEnviron.getAsPathList(
            self.VAR_gui__icon_loader__environ_key, []
        )

    def _gui__icon_loader__set_build_(self):
        pathStrList = self._gui__icon_loader__get_search_path_str_lit_()
        for pathStr in pathStrList:

            iconPathStr = bscCfg.BscUtility.DEF_bsc__os__pathsep.join(
                [pathStr, u'icon']
            )
            self._gui__icon_loader__set_icon_obj_add_by_path_(iconPathStr)

    def _gui__icon_loader__set_icon_obj_add_by_path_(self, *args):
        iconPathStr = args[0]
        relativeFilepathStrList = bscMethods.OsDirectory.allFileRelativenames(iconPathStr, extString=['png', 'svg'])
        for relativeFilepathStr in relativeFilepathStrList:
            keyStr = relativeFilepathStr.split(bscCfg.BscUtility.DEF_bsc__os__extsep)[0].replace(
                bscCfg.BscUtility.DEF_bsc__os__pathsep, bscCfg.BscUtility.DEF_bsc__python__pathsep
            )
            if self._iconStackObj.hasObject(keyStr) is False:
                iconObj = self.CLS_gui__icon_loader__icon(
                    keyStr,
                    bscCfg.BscUtility.DEF_bsc__os__pathsep.join(
                        [iconPathStr, relativeFilepathStr]
                    )
                )
                self._iconStackObj.addObject(iconObj)

    def addIconBySourcePath(self, *args):
        sourcePathStr = args[0]
        iconPathStr = bscCfg.BscUtility.DEF_bsc__os__pathsep.join(
            [sourcePathStr, u'icon']
        )
        self._gui__icon_loader__set_icon_obj_add_by_path_(iconPathStr)

    def addIconByPath(self, *args):
        self._gui__icon_loader__set_icon_obj_add_by_path_(*args)

    def icons(self):
        return self._iconStackObj.objects()

    def icon(self, *args):
        if self._iconStackObj.hasObject(*args):
            return self._iconStackObj.object(*args)

    def existIcon(self, *args):
        return self._iconStackObj.hasObject(*args)

    def iconOspath(self, *args):
        keyStr = args[0]
        if bscMethods.OsPath.isFile(keyStr):
            return keyStr
        iconObj = self.icon(keyStr)
        if iconObj is not None:
            return iconObj.ospath
        else:
            for i in ['on', 'off', 'cur']:
                if keyStr.endswith(i):
                    iconObj = self.icon(keyStr[:-len(i)])
                    if iconObj is not None:
                        return iconObj.ospath
        return ''
