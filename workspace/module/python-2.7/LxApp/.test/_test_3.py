# coding:utf-8
from LxApp import appObjects

apk = appObjects.AppAppkit()

for i in apk.tags():
    print i.tip

