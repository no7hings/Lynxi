# coding:utf-8
from LxBasic import bscMethods

from LxGui import guiObjects

bscMethods.OsEnviron.add(
    'LYNXI_PATHS_SOURCE', '/data/e/myworkspace/td/lynxi'
)

bscMethods.OsEnviron.add(
    'LYNXI_PATHS_SOURCE', '/data/e/myworkspace/td/lynxi/kit/toolkit/share/arnold_cmd_render/0.0.0/source'
)

al = guiObjects.GuiIconLoader()

for i in al.icons():
    print i
