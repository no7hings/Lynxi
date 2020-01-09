# coding:utf-8
from LxCore import lxBasic
#
from LxCore.object import objCore
#
from LxCore.preset import personnelPr


#
class lxObjectBasic(object):
    def _initObjectBasic(self):
        self._initObjectBasicAttr()
        self._initObjectBasicVar()
    #
    def _initObjectBasicAttr(self):
        self._type = None
        self._index = None
    #
    def _initObjectBasicVar(self):
        pass
    #
    def setType(self, char):
        self._type = char
    #
    def type(self):
        return self._type
    #
    def setIndex(self, uniqueId):
        self._index = uniqueId
    #
    def index(self):
        return self._index


#
class lxUnitObjectBasic(lxObjectBasic):
    def _initUnitObjectBasic(self):
        lxObjectBasic._initObjectBasic(self)
        #
        self._initUnitObjectBasicAttr()
        self._initUnitObjectBasicVar()
    #
    def _initUnitObjectBasicAttr(self):
        self._compose = lxComposeBasic()
        self._version = lxVersionBasic()
    #
    def _initUnitObjectBasicVar(self):
        pass
    #
    def version(self):
        return self._version
    #
    def compose(self):
        return self._compose


#
class lxDatumObjectBasic(lxObjectBasic):
    def _initDatumObjectBasic(self):
        lxObjectBasic._initObjectBasic(self)
        #
        self._initDatumObjectBasicAttr()
        self._initDatumObjectBasicVar()
    #
    def _initDatumObjectBasicAttr(self):
        self._data = lxDataBasic()
    #
    def _initDatumObjectBasicVar(self):
        pass
    #
    def setData(self, data):
        self._data = data
    #
    def data(self):
        return self._data


#
class lxDatabaseObjectBasic(lxObjectBasic):
    def _initDatabaseObjectBasic(self):
        lxObjectBasic._initObjectBasic(self)
        #
        self._initDatabaseObjectBasicAttr()
        self._initDatabaseObjectBasicVar()
    #
    def _initDatabaseObjectBasicAttr(self):
        pass
    #
    def _initDatabaseObjectBasicVar(self):
        pass


#
class lxDataBasic(object):
    def _initDataBasic(self):
        self._initDataBasicAttr()
        self._initDataBasicVar()
    #
    def _initDataBasicAttr(self):
        self._data = None
        self._dataHash = None
    #
    def _initDataBasicVar(self):
        pass
    #
    def _updateDataHash(self):
        pass


#
class lxComposeBasic(lxDataBasic):
    def _initComposeBasic(self):
        lxDataBasic._initDataBasic(self)
        #
        self._initComposeBasicAttr()
        self._initComposeBasicVar()
    #
    def _initComposeBasicAttr(self):
        self._datumObjectCompose = lxObjectComposeBasic()
        self._unitObjectCompose = lxObjectComposeBasic()
    #
    def _initComposeBasicVar(self):
        pass


#
class lxObjectComposeBasic(object):
    def _initObjectComposeBasic(self):
        self._initObjectComposeBasicAttr()
        self._initObjectComposeBasicVar()
    #
    def _initObjectComposeBasicAttr(self):
        self._objectLis = []
    #
    def _initObjectComposeBasicVar(self):
        self._objectTypeLis = []
        #
        self._objectTypeDic = {}
    #
    def _updateObjectTypeLis(self, lxObjectType):
        if not lxObjectType in self._objectLis:
            self._objectTypeLis.append(lxObjectType)
    #
    def _updateObjectTypeDic(self, lxObjectType, lxObject):
        if not lxObjectType in self._objectTypeDic:
            pass
    #
    def addObject(self, model):
        if not model in self._objectLis:
            lxObjectType = model.type()
            #
            self._objectLis.append(model)
            #
            self._updateObjectTypeLis(lxObjectType)


#
class lxTagBasic(object):
    pass


#
class lxVersionBasic(object):
    def _initVersionBasic(self):
        self._initVersionBasicAttr()
        self._initVersionBasicVar()
    #
    def _initVersionBasicAttr(self):
        self._versionDic = {}
    #
    def _initVersionBasicVar(self):
        pass
    #
    def lastVersion(self):
        pass


#
class lxPathBasic(object):
    def _initPathBasic(self):
        self._initPathBasicAttr()
    #
    def _initPathBasicAttr(self):
        self._pathSep = None
        #
        self._rootPaths = []
        self._rootDirection = None
        #
        self._paths = []
        self._direction = None
    @staticmethod
    def _toDirection(paths, pathSep):
        return pathSep.join(paths)
    @staticmethod
    def _toPaths(direction, pathSep):
        return direction.split(pathSep)
    #
    def _updatePath(self):
        if self.paths():
            self._direction = self._toDirection(self.paths(), self.pathSep())
    #
    def _updatePaths(self):
        if self.direction():
            self._paths = self._toPaths(self.direction(), self.pathSep())
    #
    def _updateRootPath(self):
        if self.rootPaths():
            self._rootDirection = self._toDirection(self.rootPaths(), self.pathSep())
    #
    def _updateRootPaths(self):
        if self.rootDirection():
            self._rootPaths = self._toPaths(self.rootDirection(), self.pathSep())
    #
    def setPathSep(self, char):
        self._pathSep = char
    #
    def pathSep(self):
        return self._pathSep
    #
    def setPaths(self, paths):
        if isinstance(paths, list) or isinstance(paths, tuple):
            self._paths = paths
            #
            self._updatePath()
    #
    def paths(self):
        return self._paths
    #
    def setPath(self, char):
        if isinstance(char, str) or isinstance(char, unicode):
            self._direction = char
            #
            self._updatePaths()
    #
    def direction(self):
        return self._direction
    #
    def setRootPaths(self, paths):
        if isinstance(paths, list) or isinstance(paths, tuple):
            self._rootPaths = paths
            #
            self._updateRootPath()
    #
    def rootPaths(self):
        return self._rootPaths
    #
    def setRootPath(self, char):
        if isinstance(char, str) or isinstance(char, unicode):
            self._rootDirection = char
            #
            self._updateRootPaths()
    #
    def rootDirection(self):
        return self._rootDirection
    #
    def relDirection(self):
        if self.rootDirection() is not None:
            if self.direction() is not None:
                return self.direction()[len(self.rootDirection()) + 1:]
        else:
            return self.direction()
    #
    def isExists(self):
        pass


#
class lxInfoBasic(object):
    def _initInfoBasic(self):
        self._initInfoBasicAttr()
    #
    def _initInfoBasicAttr(self):
        self._user = None
        self._time = None
        self._hostName = None
        self._host = None
        self._describe = None
    #
    def _updateInfoByCurrent(self):
        pass
    #
    def user(self):
        return self._user
    #
    def setUser(self, string):
        self._user = string
    #
    def viewUser(self):
        if self.user() is not None:
            return personnelPr.getPersonnelUserCnName(self.user())
    #
    def time(self):
        return self._time
    #
    def setTime(self, timeStamp):
        self._time = timeStamp
    #
    def fncCatchCostTime(self):
        if self.time() is not None:
            return lxBasic.getCnViewTime(self.time())
    #
    def hostName(self):
        return self._hostName
    #
    def setHostName(self, string):
        self._hostName = string
    #
    def host(self):
        return self._host
    #
    def setHost(self, string):
        self._host = string
    #
    def setDescribe(self, string):
        self._describe = string
    #
    def describe(self):
        return self._describe
    #
    def info(self):
        return {
            objCore.DbUserKey: self._user,
            objCore.DbTimeKey: self._time,
            objCore.DbHostNameKey: self._hostName,
            objCore.DbHostKey: self._host,
            objCore.DbDescribeKey: self._describe
        }


