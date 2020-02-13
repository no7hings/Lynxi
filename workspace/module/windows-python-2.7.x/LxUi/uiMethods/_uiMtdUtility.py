# coding:utf-8
from LxBasic import bscMethods

from LxCore import lxScheme


class SvgFile(object):
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
            
            if not bscMethods.OsPath.isExist(osSvgOnFile):
                onData = data.replace(defFillString, onFillString)
                bscMethods.OsFile.write(osSvgOnFile, onData)
            #
            if not bscMethods.OsPath.isExist(osSvgOffFile):
                offData = data.replace(defFillString, offFillString)
                bscMethods.OsFile.write(osSvgOffFile, offData)
            #
            if not bscMethods.OsPath.isExist(osSvgCurFile):
                curData = data.replace(defFillString, curFillString)
                bscMethods.OsFile.write(osSvgCurFile, curData)
    @classmethod
    def covertSvgSubFile__(cls, osSvgFile, data):
        defFillString = '.st0{fill:#DFDFDF;}'
        _defFillString = '.st0{fill:#BFBFBF;}'
        if defFillString in data:
            _defData = data.replace(defFillString, _defFillString)
            bscMethods.OsFile.write(osSvgFile, _defData)
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
            if not bscMethods.OsPath.isExist(osSvgOnFile):
                onData = data.replace(defFillString, onFillString)
                bscMethods.OsFile.write(osSvgOnFile, onData)
            #
            if not bscMethods.OsPath.isExist(osSvgOffFile):
                offData = data.replace(defFillString, offFillString)
                bscMethods.OsFile.write(osSvgOffFile, offData)
            #
            if not bscMethods.OsPath.isExist(osSvgCurFile):
                curData = data.replace(defFillString, curFillString)
                bscMethods.OsFile.write(osSvgCurFile, curData)
    @classmethod
    def getOsSvgFileLis(cls):
        developPath = lxScheme.Root().basic.develop
        
        osPath = bscMethods.OsPath.composeBy([developPath, cls.LynxiOsCompPath_SvgIcon])
        #
        stringLis = bscMethods.OsDirectory.fileBasenames(osPath)
        if stringLis:
            for i in stringLis:
                if i.endswith('.svg'):
                    if not i.endswith('On.svg') and not i.endswith('Off.svg') and not i.endswith('Cur.svg'):
                        osSvgFile = bscMethods.OsPath.composeBy([osPath, i])
                        data = bscMethods.OsFile.read(osSvgFile)
                        if '<!-- Generator: Adobe Illustrator 22.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->' in data:
                            cls.covertSvgSubFile(osSvgFile, data)
                        else:
                            print 'Error File {}'.format(i)
    @classmethod
    def getOsSvgFileLis_(cls):
        developPath = lxScheme.Root().basic.develop
        osPath = bscMethods.OsPath.composeBy([developPath, cls.LynxiOsCompPath_SvgIcon])
        #
        stringLis = bscMethods.OsDirectory.fileBasenames(osPath)
        if stringLis:
            for i in stringLis:
                if i.endswith('.svg'):
                    if not i.endswith('On.svg') and not i.endswith('Off.svg') and not i.endswith('Cur.svg'):
                        osSvgFile = bscMethods.OsPath.composeBy([osPath, i])
                        data = bscMethods.OsFile.read(osSvgFile)
                        if '<!-- Generator: Adobe Illustrator 22.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->' in data:
                            cls.covertSvgSubFile_(osSvgFile, data)
                        else:
                            print 'Error File {}'.format(i)
    @classmethod
    def getOsSvgFileLis__(cls):
        developPath = lxScheme.Root().basic.develop
        osPath = bscMethods.OsPath.composeBy([developPath, cls.LynxiOsCompPath_SvgIcon])
        #

        stringLis = bscMethods.OsDirectory.fileBasenames(osPath)
        if stringLis:
            for i in stringLis:
                if i.endswith('.svg'):
                    if not i.endswith('On.svg') and not i.endswith('Off.svg') and not i.endswith('Cur.svg'):
                        osSvgFile = bscMethods.OsPath.composeBy([osPath, i])
                        data = bscMethods.OsFile.read(osSvgFile)
                        if '<!-- Generator: Adobe Illustrator 22.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->' in data:
                            cls.covertSvgSubFile__(osSvgFile, data)
                        else:
                            print 'Error File {}'.format(i)
