# coding:utf-8
from LxBasic import bscCore


class OsLog(bscCore.Mtd_BscBasic):
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

    @classmethod
    def addDatabaseResult(cls, text):
        cls._setOsLogAdd(
            text,
            cls._databaseLogFile()
        )

