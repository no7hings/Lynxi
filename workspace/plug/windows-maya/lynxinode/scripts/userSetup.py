# encoding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds


#
def register():
    # AE Template
    from lxCommand.template import aeTemplate
    cmds.evalDeferred(aeTemplate.setupAETemplate)
    # Menu
    from lxCommand.ui import menu
    cmds.evalDeferred(menu.setupMenu)


#
register()