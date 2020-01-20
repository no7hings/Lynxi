# coding:utf-8
from LxPreset import prsConfigure

from LxCore.config import appConfig
#
from LxCore.method import _osMethod


#
class LxPresetMethod(_osMethod.OsFileMethod, appConfig.LxDbProductUnitConfig):
    @classmethod
    def isDbProductUnitExists(cls, dbUnitId):
        osFile = cls.dbProductUnitSetFile(dbUnitId)
        return cls.isOsExistsFile(osFile)
    @classmethod
    def getDbProductUnitIndexDatumLis(cls, productModule):
        osFile = cls.dbProductUnitIndexFile(productModule)
        return cls.readOsJson(osFile)
    @classmethod
    def getDbProductUnitIndexLis(cls, productModule):
        data = cls.getDbProductUnitIndexDatumLis(productModule)
        if data:
            return zip(*data)[0]
        else:
            return []
    @classmethod
    def getDbProductUnitCount(cls, productModule):
        data = cls.getDbProductUnitIndexDatumLis(productModule)
        if data:
            return len(data)
        else:
            return 0
    @classmethod
    def getDbProductUnitSetDatum(cls, dbUnitId):
        osFile = cls.dbProductUnitSetFile(dbUnitId)
        return cls.readOsJson(osFile)
    @classmethod
    def getDbProductUnitSetUiDatum(cls, projectName, productModule, dbUnitId, number=0, overrideNumber=False):
        def getDefaultDatum():
            return prsConfigure.Product.lxDbProductUnitDefaultSetConfig(projectName, productModule, number)
        #
        def getCustomDatum():
            osFile = cls.dbProductUnitSetFile(dbUnitId)
            return cls.readOsJson(osFile)
        #
        def getDatum(defaultLis, customDic):
            lis = []
            if defaultLis:
                for i in defaultLis:
                    key, uiValue = i
                    #
                    uiKey = None
                    if isinstance(key, str) or isinstance(key, unicode):
                        uiKey = cls.str_camelcase2prettify(key)
                    if isinstance(key, tuple):
                        key, uiKey = key
                    #
                    defValue = uiValue
                    value = uiValue
                    if isinstance(uiValue, list):
                        defValue = uiValue[0]
                        value = uiValue[0]
                    elif isinstance(uiValue, dict):
                        defValue = uiValue.values()[0][0]
                        value = uiValue.values()[0][0]
                    #
                    if customDic:
                        if key in customDic:
                            value = customDic[key]
                        else:
                            if key == 'name':

                                value = prsConfigure.Product._toProductUnitName(number)
                        #
                        if overrideNumber is True:
                            if key == 'name':
                                value = prsConfigure.Product._toProductUnitName(number)
                    lis.append(
                        (key, uiKey, value, defValue, uiValue)
                    )
            return lis
        #
        return getDatum(getDefaultDatum(), getCustomDatum())
    @classmethod
    def setDbProductUnitUpdate(cls, productModule, dbUnitId, unitIndexDatum, unitSetDatum):
        cls.setDbProductUnitIndexUpdate(productModule, unitIndexDatum)
        cls.setDbProductUnitSetUpdate(dbUnitId, unitSetDatum)
    @classmethod
    def setDbProductUnitIndexUpdate(cls, productModule, unitIndexDatum):
        indexFile = cls.dbProductUnitIndexFile(productModule)
        if cls.isOsExistsFile(indexFile):
            data = cls.readOsJson(indexFile)
            unitIndexLis = zip(*data)[0]
            dbUnitId = unitIndexDatum[0]
            if not dbUnitId in unitIndexLis:
                data += [unitIndexDatum]
                cls.setOsFileBackup(indexFile)
                cls.writeOsJson(data, indexFile)
            else:
                index = unitIndexLis.index(dbUnitId)
                serverUnitIndexDatum = data[index]
                if not unitIndexDatum == serverUnitIndexDatum:
                    data[index] = unitIndexDatum
                    cls.setOsFileBackup(indexFile)
                    cls.writeOsJson(data, indexFile)
        else:
            cls.writeOsJson([unitIndexDatum], indexFile)
    @classmethod
    def setDbProductUnitSetUpdate(cls, dbUnitId, unitSetDatum):
        setFile = cls.dbProductUnitSetFile(dbUnitId)
        if cls.isOsExistsFile(setFile):
            data = cls.readOsJson(setFile)
            if not data == unitSetDatum:
                cls.setOsFileBackup(setFile)
                cls.writeOsJson(unitSetDatum, setFile)
        else:
            cls.writeOsJson(unitSetDatum, setFile)
    @classmethod
    def getDbProductUnitViewInfo(cls):
        pass
