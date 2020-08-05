# coding:utf-8
from LxBasic import bscMtdCore


class OsEnviron(bscMtdCore.Mtd_BscUtility):
    @classmethod
    def get(cls, key, failobj=None):
        return cls._getOsEnvironRawWithKey(key, failobj)

    @classmethod
    def set(cls, key, value):
        cls.MOD_os.environ[key] = value

    @classmethod
    def add(cls, key, value):
        lowerKeyList = [i.lower() for i in cls.MOD_os.environ.keys()]
        if key.lower() in lowerKeyList:
            lowerValueList = [i.lower() for i in cls.MOD_os.environ[key].split(cls.MOD_os.pathsep)]
            if value.lower() not in lowerValueList:
                cls.MOD_os.environ[key] += cls.MOD_os.pathsep + value
        else:
            cls.MOD_os.environ[key.upper()] = str(value)

    @classmethod
    def getAsPath(cls, key, failobj=None):
        return cls._getOsEnvironRawAsPath(key, failobj)

    @classmethod
    def getAsList(cls, key, failobj=None):
        return cls._getOsEnvironRawAsList(key, failobj)

    @classmethod
    def getAsPathList(cls, key, failobj=None):
        return cls._getOsEnvironRawAsPathList(key, failobj)

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
    def getPythonPaths(cls):
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

        dic[u'LYNXI_PYTHONPATH'] = cls.getPythonPaths()
        #
        return dic


class WindowsPlatform(bscMtdCore.Mtd_BscPlatform):
    VAR_bsc__system__name = 'windows'


class LinuxPlatform(bscMtdCore.Mtd_BscPlatform):
    VAR_bsc__system__name = 'linux'


class MayaApp(bscMtdCore.Mtd_BscApplication):
    VAR_bsc__system__name = 'maya'

    @classmethod
    def _bsc__system_cls__get_is_active_(cls, appNameStr):
        data = OsEnviron.get('MAYA_APP_DIR')
        if data:
            return True
        return False

    @classmethod
    def _bsc__system_cls__get_full_version_str_(cls):
        if cls.isActive():
            # noinspection PyUnresolvedReferences
            import maya.cmds as cmds
            return str(cmds.about(apiVersion=1))

    @classmethod
    def _bsc__system_cls__get_version_str_(cls):
        if cls.isActive():
            # noinspection PyUnresolvedReferences
            import maya.cmds as cmds
            return str(cmds.about(apiVersion=1))[:4]

    @classmethod
    def userDocumentDirectory(cls, versionString=None):
        basicFolder = bscMtdCore.Mtd_BscUtility._toOsPathString([OsPlatform.userDocumentDirectory(), cls.VAR_bsc__system__name])
        # Custom Version
        if versionString is None or versionString == 'Unspecified':
            versionString = cls.version()
        #
        versionFolderString = versionString
        if int(versionString) < 2016:
            versionFolderString = versionString + 'x64'
        #
        return bscMtdCore.Mtd_BscUtility._toOsPathString([basicFolder, versionFolderString])

    @classmethod
    def moduleDirectory(cls, versionString=None):
        mayaDocPath = cls.userDocumentDirectory(versionString)
        return bscMtdCore.Mtd_BscUtility._toOsPathString([mayaDocPath, 'modules'])


class HoudiniApp(bscMtdCore.Mtd_BscApplication):
    VAR_bsc__system__name = 'houdini'

    @classmethod
    def _bsc__system_cls__get_is_active_(cls, appNameStr):
        data = cls.MTD_os_path.basename(cls.MOD_sys.argv[0])
        if data.lower() == '{}.exe'.format(appNameStr):
            return True
        elif data.lower() == appNameStr:
            return True
        return False

    @classmethod
    def _bsc__system_cls__get_full_version_str_(cls):
        if cls.isActive():
            # noinspection PyUnresolvedReferences
            import hou
            return str('.'.join(list(hou.applicationVersion())))

    @classmethod
    def _bsc__system_cls__get_version_str_(cls):
        if cls.isActive():
            # noinspection PyUnresolvedReferences
            import hou
            return str(hou.applicationVersion()[0])


class OsPlatform(bscMtdCore.Mtd_BscUtility):
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
    def userDirectory(cls):
        if WindowsPlatform.isActive():
            return OsEnviron.getAsPath('userprofile')
        elif LinuxPlatform.isActive():
            return OsEnviron.getAsPath('HOME')
        else:
            raise

    @classmethod
    def userDocumentDirectory(cls):
        return cls.userDirectory() + '/Documents'


class OsTimestamp(bscMtdCore.Mtd_BscUtility):
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


class OsTimetag(bscMtdCore.Mtd_BscUtility):
    @classmethod
    def toChnPrettify(cls, timetag, useMode=0):
        return cls._timetagToChnPrettify(timetag, useMode)

    @classmethod
    def active(cls):
        return cls._getActiveTimetag()
