# coding:utf-8
from LxCore.method import _osMethod


#
class UiSvgMethod(_osMethod.OsFileMethod):
    LynxiOsCompPath_SvgIcon = 'icon/svg_basic'
    LynxiOsExt_Svg = '.svg'
    @classmethod
    def covertSvgSubFile(cls, osSvgFile, data):
        defFillString = '.st0{fill:#DFDFDF;}'
        onFillString = '.st0{fill:#00DFDF;}'
        offFillString = '.st0{fill:#7F7F7F;}'
        curFillString = '.st0{fill:#427FFF;}'
        if defFillString in data:
            osSvgOnFile = osSvgFile[:-len(cls.LynxiOsExt_Svg)] + 'On.svg'
            osSvgOffFile = osSvgFile[:-len(cls.LynxiOsExt_Svg)] + 'Off.svg'
            osSvgCurFile = osSvgFile[:-len(cls.LynxiOsExt_Svg)] + 'Cur.svg'
            #
            if not cls.isOsExistsFile(osSvgOnFile):
                onData = data.replace(defFillString, onFillString)
                cls.writeOsData(onData, osSvgOnFile)
            #
            if not cls.isOsExistsFile(osSvgOffFile):
                offData = data.replace(defFillString, offFillString)
                cls.writeOsData(offData, osSvgOffFile)
            #
            if not cls.isOsExistsFile(osSvgCurFile):
                curData = data.replace(defFillString, curFillString)
                cls.writeOsData(curData, osSvgCurFile)
    @classmethod
    def covertSvgSubFile__(cls, osSvgFile, data):
        defFillString = '.st0{fill:#DFDFDF;}'
        _defFillString = '.st0{fill:#BFBFBF;}'
        if defFillString in data:
            _defData = data.replace(defFillString, _defFillString)
            cls.writeOsData(_defData, osSvgFile)
    @classmethod
    def covertSvgSubFile_(cls, osSvgFile, data):
        defFillString = '.st0{fill:#BFBFBF;}'
        onFillString = '.st0{fill:#FFFFFF;}'
        offFillString = '.st0{fill:#5F5F5F;}'
        curFillString = '.st0{fill:#427FFF;}'
        if defFillString in data:
            osSvgOnFile = osSvgFile[:-len(cls.LynxiOsExt_Svg)] + 'On.svg'
            osSvgOffFile = osSvgFile[:-len(cls.LynxiOsExt_Svg)] + 'Off.svg'
            osSvgCurFile = osSvgFile[:-len(cls.LynxiOsExt_Svg)] + 'Cur.svg'
            #
            if not cls.isOsExistsFile(osSvgOnFile):
                onData = data.replace(defFillString, onFillString)
                cls.writeOsData(onData, osSvgOnFile)
            #
            if not cls.isOsExistsFile(osSvgOffFile):
                offData = data.replace(defFillString, offFillString)
                cls.writeOsData(offData, osSvgOffFile)
            #
            if not cls.isOsExistsFile(osSvgCurFile):
                curData = data.replace(defFillString, curFillString)
                cls.writeOsData(curData, osSvgCurFile)
    @classmethod
    def getOsSvgFileLis(cls):
        developPath = cls._lxDevelopRoot()
        osPath = cls._toOsPath([developPath, cls.LynxiOsCompPath_SvgIcon])
        #
        stringLis = cls.getOsFileBasenameLisByPath(osPath)
        if stringLis:
            for i in stringLis:
                if i.endswith('.svg'):
                    if not i.endswith('On.svg') and not i.endswith('Off.svg') and not i.endswith('Cur.svg'):
                        osSvgFile = cls._toOsPath([osPath, i])
                        data = cls.readOsData(osSvgFile)
                        if '<!-- Generator: Adobe Illustrator 22.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->' in data:
                            cls.covertSvgSubFile(osSvgFile, data)
                        else:
                            print 'Error File {}'.format(i)
    @classmethod
    def getOsSvgFileLis_(cls):
        developPath = cls._lxDevelopRoot()
        osPath = cls._toOsPath([developPath, cls.LynxiOsCompPath_SvgIcon])
        #
        stringLis = cls.getOsFileBasenameLisByPath(osPath)
        if stringLis:
            for i in stringLis:
                if i.endswith('.svg'):
                    if not i.endswith('On.svg') and not i.endswith('Off.svg') and not i.endswith('Cur.svg'):
                        osSvgFile = cls._toOsPath([osPath, i])
                        data = cls.readOsData(osSvgFile)
                        if '<!-- Generator: Adobe Illustrator 22.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->' in data:
                            cls.covertSvgSubFile_(osSvgFile, data)
                        else:
                            print 'Error File {}'.format(i)
    @classmethod
    def getOsSvgFileLis__(cls):
        developPath = cls._lxDevelopRoot()
        osPath = cls._toOsPath([developPath, cls.LynxiOsCompPath_SvgIcon])
        #
        stringLis = cls.getOsFileBasenameLisByPath(osPath)
        if stringLis:
            for i in stringLis:
                if i.endswith('.svg'):
                    if not i.endswith('On.svg') and not i.endswith('Off.svg') and not i.endswith('Cur.svg'):
                        osSvgFile = cls._toOsPath([osPath, i])
                        data = cls.readOsData(osSvgFile)
                        if '<!-- Generator: Adobe Illustrator 22.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->' in data:
                            cls.covertSvgSubFile__(osSvgFile, data)
                        else:
                            print 'Error File {}'.format(i)
