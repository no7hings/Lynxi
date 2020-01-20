# coding:utf-8
from LxBasic import bscCore


class OsSystem(bscCore.Basic):
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


class OsEnviron(bscCore.Basic):
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


class OsLog(bscCore.Basic):
    @classmethod
    def _setOsLogAdd(cls, text, logFileString):
        cls._setOsFileDirectoryCreate(logFileString)
        with open(logFileString, 'a') as log:
            log.writelines(u'<{}> @ {}\n'.format(cls._getActivePrettifyTime(), cls._getSystemUsername()))
            log.writelines(u'{}\n'.format(text))
            log.close()

    @classmethod
    def addException(cls, text):
        cls._setOsLogAdd(
            text,
            cls._exceptionLogFile()
        )

    @classmethod
    def addError(cls, text):
        cls._setOsLogAdd(
            text,
            cls._errorLogFile()
        )

    @classmethod
    def addResult(cls, text):
        cls._setOsLogAdd(
            text,
            cls._resultLogFile()
        )


class OsTime(bscCore.Basic):
    @classmethod
    def activeTimestamp(cls):
        return cls._getSystemActiveTimestamp()

    @classmethod
    def activeTimetag(cls):
        return cls._getActiveTimetag()

    @classmethod
    def activePrettify(cls):
        return cls._timestampToPrettify(cls._getSystemActiveTimestamp())

    @classmethod
    def activeChnPrettify(cls):
        return cls._timestampToChnPrettify(cls._getSystemActiveTimestamp())

    @classmethod
    def getCnPrettifyByTimestamp(cls, timestamp, useMode=0):
        return cls._timestampToChnPrettify(timestamp, useMode)

    @classmethod
    def getCnPrettifyByTimetag(cls, timestamp, useMode=0):
        return cls._timetagToChnPrettify(timestamp, useMode)


class Math2D(bscCore.Basic):
    @classmethod
    def getAngleByCoord(cls, x1, y1, x2, y2):
        radian = 0.0
        #
        r0 = 0.0
        r90 = cls.MOD_math.pi / 2.0
        r180 = cls.MOD_math.pi
        r270 = 3.0 * cls.MOD_math.pi / 2.0
        #
        if x1 == x2:
            if y1 < y2:
                radian = r0
            elif y1 > y2:
                radian = r180
        elif y1 == y2:
            if x1 < x2:
                radian = r90
            elif x1 > x2:
                radian = r270
        elif x1 < x2 and y1 < y2:
            radian = cls.MOD_math.atan2((-x1 + x2), (-y1 + y2))
        elif x1 < x2 and y1 > y2:
            radian = r90 + cls.MOD_math.atan2((y1 - y2), (-x1 + x2))
        elif x1 > x2 and y1 > y2:
            radian = r180 + cls.MOD_math.atan2((x1 - x2), (y1 - y2))
        elif x1 > x2 and y1 < y2:
            radian = r270 + cls.MOD_math.atan2((-y1 + y2), (x1 - x2))
        #
        return radian * 180 / cls.MOD_math.pi
    
    @classmethod
    def getLengthByCoord(cls, x1, y1, x2, y2):
        return cls.MOD_math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


class Color(bscCore.Basic):
    @classmethod
    def str2rgb(cls, string, maximum=255):
        a = int(''.join([str(ord(i)).zfill(3) for i in string]))
        b = a % 3
        i = int(a / 256) % 3
        n = int(a % 256)
        
        if a % 2:
            if i == 0:
                r, g, b = 64 + 64 * b, n, 0
            elif i == 1:
                r, g, b = 0, 64 + 64 * b, n
            else:
                r, g, b = 0, n, 64 + 64 * b
        else:
            if i == 0:
                r, g, b = 0, n, 64 + 64 * b
            elif i == 1:
                r, g, b = 64 + 64 * b, 0, n
            else:
                r, g, b = 64 + 64 * b, n, 0
        
        return r / 255.0 * maximum, g / 255.0 * maximum, b / 255.0 * maximum
    
    @classmethod
    def hsv2rgb(cls, h, s, v, maximum=255):
        h = float(h % 360.0)
        s = float(max(min(s, 1.0), 0.0))
        v = float(max(min(v, 1.0), 0.0))
        #
        c = v * s
        x = c * (1 - abs((h / 60.0) % 2 - 1))
        m = v - c
        if 0 <= h < 60:
            r_, g_, b_ = c, x, 0
        elif 60 <= h < 120:
            r_, g_, b_ = x, c, 0
        elif 120 <= h < 180:
            r_, g_, b_ = 0, c, x
        elif 180 <= h < 240:
            r_, g_, b_ = 0, x, c
        elif 240 <= h < 300:
            r_, g_, b_ = x, 0, c
        else:
            r_, g_, b_ = c, 0, x
        #
        if maximum == 255:
            r, g, b = int(round((r_ + m) * maximum)), int(round((g_ + m) * maximum)), int(round((b_ + m) * maximum))
        else:
            r, g, b = float((r_ + m)), float((g_ + m)), float((b_ + m))
        return r, g, b


class Uuid(bscCore.Basic):
    @classmethod
    def str2uuid(cls, string):
        return cls._stringToUniqueId(string)

    @classmethod
    def covertByString(cls, *args):
        return cls._stringsToUniqueId(*args)

    @classmethod
    def new(cls):
        return cls._getUuid()
