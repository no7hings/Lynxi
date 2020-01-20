# coding:utf-8
import threading

from LxBasic import bscMethods, bscCommands

from LxCore import lxScheme

Lynxi_Ui_Family_Lis = [
    'Arial',
    'Arial Unicode MS',
    'Arial Black'
]

Lynxi_Ui_Window_Size_Default = 1920 * .85, 1080 * .85
Lynxi_Ui_Window_SubSize_Default = 1920 * .75, 1080 * .75
Lynxi_Ui_Window_Size_Dialog = 1920 * .5, 1080 * .5


class Basic(object):
    mtd_raw_position_2d = bscMethods.Position2d

    mtd_raw_ellipse2d = bscMethods.Ellipse2d

    mtd_raw_value = bscMethods.Value

    mtd_raw_color = bscMethods.Color

    @classmethod
    def _lxIconRoot(cls):
        return lxScheme.Directory().icon.server

    @staticmethod
    def _toUiDatum(data):
        string = None
        if data is not None:
            if isinstance(data, bool):
                string = unicode(data)
            elif isinstance(data, int) or isinstance(data, float):
                string = unicode(data)
            elif isinstance(data, str) or isinstance(data, unicode):
                string = data
            elif isinstance(data, tuple) or isinstance(data, list):
                data = [unicode(i) for i in data]
                string = ','.join(data)
            elif isinstance(data, dict):
                string = ','.join([':'.join(i) for i in data.items()])
        else:
            string = unicode(data)
        #
        return string

    @staticmethod
    def isRectContainPos(rect, pos):
        boolean = False
        if rect is not None:
            x, y = pos
            #
            x_, y_ = rect.x(), rect.y()
            w_, h_ = rect.width(), rect.height()
            #
            boolean = x_ <= x <= x_ + w_ and y_ <= y <= y_ + h_
        return boolean

    @staticmethod
    def getUiStrWidth(ui, string):
        linesep = '\n'
        if linesep in string:
            splitData = string.split(linesep)
            values = [ui.fontMetrics().width(i) for i in splitData]
            value = max(values)
        else:
            value = ui.fontMetrics().width(string)
        return value

    @classmethod
    def getUiStrWidthReduce(cls, ui, string, maxiWidth):
        def getIndex():
            width = 0
            for seq, i in enumerate(string):
                subWidth = cls.getUiStrWidth(ui, i)
                width = width + subWidth
                if width >= maxiWidth:
                    return seq - 3

        #
        index = getIndex()
        splitIndex = [max(getIndex(), 0), -1][index is None]
        boolean = cls.getUiStrWidth(ui, string) > maxiWidth
        return [string, string[:splitIndex] + '...'][boolean]

    @classmethod
    def _toLxOsIconFile(cls, iconKeyword, ext='.png'):
        isMayaIcon = iconKeyword.startswith('maya')
        #
        subLabel = 'table'
        #
        if iconKeyword:
            if '#' in iconKeyword:
                subLabel = iconKeyword.split('#')[0]
                iconKeyword = iconKeyword.split('#')[-1]
            if '@' in subLabel:
                ext = '.' + subLabel.split('@')[-1]
                subLabel = subLabel.split('@')[0]
        else:
            iconKeyword = ''
        #
        osFile = cls._lxIconRoot() + '/{}/{}{}'.format(subLabel, iconKeyword, ext)
        #
        if isMayaIcon:
            if bscCommands.isOsExist(osFile):
                return osFile
            else:
                return cls._lxIconRoot() + '/{}/{}{}'.format(subLabel, 'default', ext)
        else:
            return osFile

    @staticmethod
    def _toGeometryRemap(size0, size1):
        w0, h0 = size0
        w1, h1 = size1
        if h0 > 0 and h1 > 0:
            pr0 = float(w0)/float(h0)
            pr1 = float(w1)/float(h1)
            smax1 = max(w1, h1)
            smin1 = min(w1, h1)
            if pr0 > 1:
                w, h = smin1, smin1/pr0
            elif pr0 < 1:
                w, h = smin1, smin1*pr0
            else:
                w, h = smin1, smin1
            x, y = (w1 - w)/2, (h1 - h)/2
            return x, y, w, h
        else:
            return 0, 0, w0, h0

    @staticmethod
    def str2rgb(string, maximum=255):
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
        #
        return r / 255.0 * maximum, g / 255.0 * maximum, b / 255.0 * maximum

    @staticmethod
    def _lxMayaPngIconKeyword(nodeTypeString):
        return 'maya#out_{}'.format(nodeTypeString)

    @staticmethod
    def _lxMayaSvgIconKeyword(nodeTypeString):
        return 'maya@svg#{}'.format(nodeTypeString)


class UiThread(threading.Thread):
    def __init__(self, *args):
        threading.Thread.__init__(self)
        # noinspection PyUnresolvedReferences
        self._fnc = args[0]
        self._args = args[1:]
    #
    def run(self):
        self._fnc(*self._args)
