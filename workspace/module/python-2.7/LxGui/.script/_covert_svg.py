# coding:utf-8
from LxGui.guiMethods import _guiMtdUtility

fs = ['svg_basic/preoccurrence', 'svg_basic/nextoccurrence']

for i in fs:
    _guiMtdUtility.SvgFile(i).create()
