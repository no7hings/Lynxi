# coding:utf-8
from LxBasic import bscMethods


fileList = bscMethods.OsDirectory.allFileFullpathnames('/data/e/myworkspace/td/lynxi/icon/svg_basic')

for i in fileList:
    dn = '/'.join(i.split('/')[:-1])
    fn = i.split('/')[-1]
    print dn, fn

    nn = '{}/{}'.format(dn, fn.lower())
    print nn

    bscMethods.OsFile.renameTo(i, nn)

