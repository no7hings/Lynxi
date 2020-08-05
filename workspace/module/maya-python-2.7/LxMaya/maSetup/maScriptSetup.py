# coding:utf-8
from LxMaya.method.basic import _maMethodBasic


#
def initHideShowCmd():
    hotkeySetName = 'Lynxi_Hotkey_Default'
    hotkeyMethod = _maMethodBasic.MaHotkeyMethodBasic
    hotkeyMethod.setHotkeySet(hotkeySetName)
    hotkeyMethod.addCommand(
        key='l',
        name='lynxiHide',
        annotation='Hide Nde_Node for Lynxi',
        pythonCommand='''from LxMaya.command import maScript;maScript.hideShowCmd(operation='hide', extend=False)''',
        ctrlModifier=True
    )
    hotkeyMethod.addCommand(
        key='l',
        name='lynxiShow',
        annotation='Show Nde_Node for Lynxi',
        pythonCommand='''from LxMaya.command import maScript;maScript.hideShowCmd(operation='show', extend=False)''',
        shiftModifier=True
    )
