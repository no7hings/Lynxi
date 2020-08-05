# encoding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds


#
def register():
    # AE Template
    from lxCommand.template import aeTemplate
    cmds.evalDeferred(aeTemplate.setupAETemplate)
    print 'setup lynxinode "AETemplate" complete.'
    # Menu
    from lxCommand.ui import menu
    menu.setupMenu()
    print 'setup lynxinode "Menu" complete.'


#
if __name__ == '__main__':
    register()
