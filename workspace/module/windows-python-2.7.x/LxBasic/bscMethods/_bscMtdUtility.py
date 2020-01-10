# coding:utf-8
from LxBasic import bscCore

from LxBasic.bscMethods import _bscMtdPython


class OsSystem(bscCore.Basic):
    @classmethod
    def username(cls):
        return cls._getSystemUsername()

    @classmethod
    def activeTimestamp(cls):
        return cls._getActiveTimestamp()

    @classmethod
    def language(cls):
        return cls.module_locale.getdefaultlocale()


class OsEnviron(bscCore.Basic):
    @classmethod
    def get(cls, key, failobj=None):
        return cls._getOsEnvironValue(key, failobj)

    @classmethod
    def set(cls, key, value):
        cls.module_os.environ[key] = value

    @classmethod
    def getAsPath(cls, key, failobj=None):
        return cls._getOsEnvironValueAsPath(key, failobj)

    @classmethod
    def getAsList(cls, key, failobj=None):
        return cls._getOsEnvironValueAsList(key, failobj)

    @classmethod
    def isSystemPathExist(cls, pathString):
        pathLowerLis = [i.replace('\\', '/').lower() for i in cls.module_sys.path]
        if pathString.lower() in pathLowerLis:
            return True
        return False

    @classmethod
    def addSystemPath(cls, pathString):
        if cls.isSystemPathExist(pathString) is False:
            cls.module_sys.path.insert(0, pathString)

    @classmethod
    def getSystemPaths(cls):
        return cls.module_sys.path

    @classmethod
    def getEnvironDict(cls):
        def branchFnc_(key_):
            lis = cls.getAsList(key_)
            lis.sort()
            dic[key_] = lis

        dic = cls.cls_dic_order()
        keyLis = cls.module_copy.deepcopy(cls.module_os.environ.keys())
        if keyLis:
            keyLis.sort()
            [branchFnc_(i) for i in keyLis]

        dic['SYSTEM_PATH'] = cls.getSystemPaths()
        #
        return dic


class OsDirectory(bscCore.Basic):
    @classmethod
    def getAllChildren(cls, directoryString):
        """
        :param directoryString: str
        :return: list([str, ...])
        """
        return cls._getOsPathNamesByDirectory(
            directoryString,
            extString=None,
            isFile=False,
            isFullpath=True
        )

    @classmethod
    def isExist(cls, directoryString):
        """
        :param directoryString: str
        :return: bool
        """
        return cls.mtd_os_path.exists(directoryString)

    @classmethod
    def setDirectoryCreate(cls, directoryString):
        """
        :param directoryString: str
        :return: None
        """
        cls._setOsDirectoryCreate(directoryString)

    @classmethod
    def getAllChildFileRelativeNames(cls, directoryString, extString):
        return cls._getOsPathNamesByDirectory(
            rootString=directoryString,
            extString=extString,
            isFile=True,
            isFullpath=False
        )

    @classmethod
    def remove(cls, directoryString):
        """
        :param directoryString: str
        :return: None
        """
        children = cls.getAllChildren(directoryString)
        if children:
            children.reverse()
            for i in children:
                _bscMtdPython.PyMessage.traceResult(u'Os Remove: {}'.format(i.decode(u'gbk')))
                cls._setOsPathRemove(i)

        cls._setOsPathRemove(directoryString)

    @classmethod
    def open(cls, directoryString):
        cls._setOsDirectoryOpen(directoryString)


class OsFile(bscCore.Basic):
    @classmethod
    def isExist(cls, fileString):
        return cls._isOsFileExist(fileString)

    @classmethod
    def setFileDirectoryCreate(cls, fileString):
        cls._setOsFileDirectoryCreate(fileString)

    @classmethod
    def write(cls, fileString, raw):
        if raw is not None:
            cls._setOsFileDirectoryCreate(fileString)
            with open(fileString, u'w') as f:
                if isinstance(raw, str) or isinstance(raw, unicode):
                    f.write(raw)
                elif isinstance(raw, tuple) or isinstance(raw, list):
                    f.writelines(raw)

                f.close()

    @classmethod
    def read(cls, fileString):
        if cls._isOsFileExist(fileString):
            with open(fileString, u'r') as f:
                raw = f.read()
                f.close()
                return raw

    @classmethod
    def readlines(cls, fileString):
        if cls._isOsFileExist(fileString):
            with open(fileString, u'r') as f:
                raw = f.readlines()
                f.close()
                return raw
    
    @classmethod
    def isSame(cls, sourceFileString, targetFileString):
        return cls._isOsSameFile(sourceFileString, targetFileString)

    @classmethod
    def copyTo(cls, sourceFileString, targetFileString, force=True):
        cls._setOsFileCopy(sourceFileString, targetFileString, force)

    @classmethod
    def backupTo(cls, fileString, backupFileString, timetag=None):
        cls._setOsFileBackup(fileString, backupFileString, timetag)

    @classmethod
    def renameTo(cls, fileString, newFileName):
        cls._setOsFileRename(fileString, newFileName)

    @classmethod
    def renameTo_(cls, fileString, newFileString):
        cls._setOsFileRename_(fileString, newFileString)

    @classmethod
    def remove(cls, fileString):
        cls._setOsPathRemove(fileString)

    @classmethod
    def open(cls, fileString):
        cls._setOsFileOpen(fileString)

    @classmethod
    def openDirectory(cls, fileString):
        if cls._isOsFileExist(fileString):
            directoryString = cls._getOsFileDirectory(fileString)
            cls._setOsDirectoryOpen(directoryString)

    @classmethod
    def openAsTemporary(cls, fileString, temporaryFileString):
        if cls._isOsFileExist(fileString):

            timestamp = str(cls._getOsFileMtimestamp(fileString))
            if cls._isOsFileExist(temporaryFileString):
                tempTimestamp = str(cls._getOsFileMtimestamp(temporaryFileString))
            else:
                tempTimestamp = None

            if not timestamp == tempTimestamp:
                cls._setOsFileCopy(fileString, temporaryFileString)
            #
            cls._setOsFileOpen(temporaryFileString)

    @classmethod
    def isFileTimeChanged(cls, sourceFileString, targetFileString):
        return cls._isOsFileTimeChanged(sourceFileString, targetFileString)


class OsGzFile(bscCore.Basic):
    @classmethod
    def isExist(cls, fileString):
        return cls._isOsFileExist(fileString)


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
    def_time_month_lis = [
        (u'一月', 'January'),
        (u'二月', 'February'),
        (u'三月', 'March'),
        (u'四月', 'April'),
        (u'五月', 'May'),
        (u'六月', 'June'),
        (u'七月', 'July'),
        (u'八月', 'August'),
        (u'九月', 'September'),
        (u'十月', 'October'),
        (u'十一月', 'November'),
        (u'十二月', 'December')
    ]
    def_time_day_lis = [
        (u'一日', '1st'),
        (u'二日', '2nd'),
        (u'三日', '3rd'),
        (u'四日', '4th'),
        (u'五日', '5th'),
        (u'六日', '6th'),
        (u'七日', '7th'),
        (u'八日', '8th'),
        (u'九日', '9th'),
        (u'十日', '10th'),
    ]
    def_time_week_lis = [
        (u'周一', 'Monday'),
        (u'周二', 'Tuesday'),
        (u'周三', 'Wednesday'),
        (u'周四', 'Thursday'),
        (u'周五', 'Friday'),
        (u'周六', 'Saturday'),
        (u'周天', 'Sunday'),
    ]

    @classmethod
    def _timetagToChnPrettify(cls, timetag, useMode=0):
        if timetag:
            if cls.module_re.findall(r'[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]', timetag):
                year = int(timetag[:4])
                month = int(timetag[5:7])
                date = int(timetag[7:9])
                hour = int(timetag[10:12])
                minute = int(timetag[12:14])
                if year > 0:
                    timetuple = cls.module_datetime.datetime(year=year, month=month, day=date, hour=hour, minute=minute).timetuple()
                    string = cls._timetupleToChnPrettify(timetuple, useMode)
                else:
                    string = u'{0}{0}年{0}月{0}日{0}点分'.format('??')
            else:
                string = u'无记录'
        else:
            string = u'无记录'
        return string

    @classmethod
    def _timestampToChnPrettify(cls, timestamp, useMode=0):
        if isinstance(timestamp, float):
            return cls._timetupleToChnPrettify(cls.module_time.localtime(timestamp), useMode)
        else:
            return u'无记录'

    @classmethod
    def _timetupleToChnPrettify(cls, timetuple, useMode=0):
        year, month, date, hour, minute, second, week, dayCount, isDst = timetuple
        if useMode == 0:
            timetuple_ = cls.module_time.localtime(cls.module_time.time())
            year_, month_, date_, hour_, minute_, second_, week_, dayCount_, isDst_ = timetuple_
            #
            monday = date - week
            monday_ = date_ - week_
            if timetuple_[:1] == timetuple[:1]:
                dateString = u'{}月{}日'.format(str(month).zfill(2), str(date).zfill(2))
                weekString = u''
                subString = u''
                if timetuple_[:2] == timetuple[:2]:
                    if monday_ == monday:
                        dateString = ''
                        weekString = u'{0}'.format(cls.def_time_week_lis[int(week)][0])
                        if date_ == date:
                            subString = u'（今天）'
                        elif date_ == date + 1:
                            subString = u'（昨天）'
                #
                timeString = u'{}点{}分'.format(str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2))
                #
                string = u'{}{}{} {}'.format(dateString, weekString, subString, timeString)
                return string
            else:
                return u'{}年{}月{}日'.format(str(year).zfill(4), str(month).zfill(2), str(date).zfill(2))
        else:
            dateString = u'{}年{}月{}日'.format(str(year).zfill(4), str(month).zfill(2), str(date).zfill(2))
            timeString = u'{}点{}分{}秒'.format(str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2))
            return u'{} {}'.format(dateString, timeString)

    @classmethod
    def activeTimestamp(cls):
        return cls._getActiveTimestamp()

    @classmethod
    def activeChnPrettify(cls):
        return cls._timestampToChnPrettify(cls._getActiveTimestamp())

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
        r90 = cls.module_math.pi / 2.0
        r180 = cls.module_math.pi
        r270 = 3.0 * cls.module_math.pi / 2.0
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
            radian = cls.module_math.atan2((-x1 + x2), (-y1 + y2))
        elif x1 < x2 and y1 > y2:
            radian = r90 + cls.module_math.atan2((y1 - y2), (-x1 + x2))
        elif x1 > x2 and y1 > y2:
            radian = r180 + cls.module_math.atan2((x1 - x2), (y1 - y2))
        elif x1 > x2 and y1 < y2:
            radian = r270 + cls.module_math.atan2((-y1 + y2), (x1 - x2))
        #
        return radian * 180 / cls.module_math.pi
    
    @classmethod
    def getLengthByCoord(cls, x1, y1, x2, y2):
        return cls.module_math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


class Color(bscCore.Basic):
    @classmethod
    def getRgbByString(cls, string, maximum=255):
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
    def hsvToRgb(cls, h, s, v, maximum=255):
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
