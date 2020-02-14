# coding:utf-8
from LxBasic import bscCore


class OsEnviron(bscCore.Mtd_BscBasic):
    @classmethod
    def get(cls, key, failobj=None):
        return cls._getOsEnvironRawWithKey(key, failobj)

    @classmethod
    def set(cls, key, value):
        cls.MOD_os.environ[key] = value

    @classmethod
    def getAsPath(cls, key, failobj=None):
        return cls._getOsEnvironRawAsPath(key, failobj)

    @classmethod
    def getAsList(cls, key, failobj=None):
        return cls._getOsEnvironRawAsList(key, failobj)

    @classmethod
    def isSystemPathExist(cls, pathString):
        pathLowerLis = [i.replace('\\', '/').lower() for i in cls.MOD_sys.path]
        if pathString.lower() in pathLowerLis:
            return True
        return False

    @classmethod
    def addSystemPath(cls, pathString):
        if cls.isSystemPathExist(pathString) is False:
            cls.MOD_sys.path.insert(0, pathString)

    @classmethod
    def getSystemPaths(cls):
        return cls.MOD_sys.path

    @classmethod
    def getEnvironDict(cls):
        def branchFnc_(key_):
            lis = cls.getAsList(key_)
            lis.sort()
            dic[key_] = lis

        dic = cls.CLS_dic_order()
        keyLis = cls.MOD_copy.deepcopy(cls.MOD_os.environ.keys())
        if keyLis:
            keyLis.sort()
            [branchFnc_(i) for i in keyLis]

        dic['SYSTEM_PATH'] = cls.getSystemPaths()
        #
        return dic


class OsSystem(bscCore.Mtd_BscBasic):
    @classmethod
    def username(cls):
        return cls._getSystemUsername()

    @classmethod
    def hostname(cls):
        return cls._getSystemHostname()

    @classmethod
    def host(cls):
        return cls._getSystemHost()

    @classmethod
    def activeTimestamp(cls):
        return cls._getSystemActiveTimestamp()

    @classmethod
    def language(cls):
        return cls.MOD_locale.getdefaultlocale()

    @classmethod
    def runCommand(cls, command):
        cls.MOD_subprocess.Popen(
            command,
            shell=True,
            stdout=cls.MOD_subprocess.PIPE,
            stderr=cls.MOD_subprocess.PIPE
        )

    @classmethod
    def documentDirectory(cls):
        return OsEnviron.getAsPath('userprofile') + '/Documents'


class MayaApp(bscCore.Mtd_BscApplicationBasic):
    DEF_name_application = 'maya'

    @classmethod
    def isActive(cls):
        return cls._isActiveApplication(cls.DEF_name_application)

    @classmethod
    def fullVersion(cls):
        if cls.isActive():
            # noinspection PyUnresolvedReferences
            import maya.cmds as cmds
            return str(cmds.about(apiVersion=1))

        return ''

    @classmethod
    def version(cls):
        if cls.isActive():
            # noinspection PyUnresolvedReferences
            import maya.cmds as cmds
            return str(cmds.about(apiVersion=1))[:4]

        return ''

    @classmethod
    def documentDirectory(cls, versionString=None):
        basicFolder = cls._toOsPathString([OsSystem.documentDirectory(), cls.DEF_name_application])
        # Custom Version
        if versionString is None or versionString == 'Unspecified':
            versionString = cls.version()
        #
        versionFolderString = versionString
        if int(versionString) < 2016:
            versionFolderString = versionString + 'x64'
        #
        return cls._toOsPathString([basicFolder, versionFolderString])

    @classmethod
    def moduleDirectory(cls, versionString=None):
        mayaDocPath = cls.documentDirectory(versionString)
        return cls._toOsPathString([mayaDocPath, 'modules'])


class OsTimestamp(bscCore.Mtd_BscBasic):
    @classmethod
    def active(cls):
        return cls._getSystemActiveTimestamp()

    @classmethod
    def activePrettify(cls):
        return cls._timestampToPrettify(cls._getSystemActiveTimestamp())

    @classmethod
    def toPrettify(cls, timestamp):
        return cls._timestampToPrettify(timestamp)

    @classmethod
    def activeChnPrettify(cls):
        return cls._timestampToChnPrettify(cls._getSystemActiveTimestamp())

    @classmethod
    def toChnPrettify(cls, timestamp, useMode=0):
        return cls._timestampToChnPrettify(timestamp, useMode)


class OsTimetag(bscCore.Mtd_BscBasic):
    @classmethod
    def toChnPrettify(cls, timetag, useMode=0):
        return cls._timetagToChnPrettify(timetag, useMode)

    @classmethod
    def active(cls):
        return cls._getActiveTimetag()