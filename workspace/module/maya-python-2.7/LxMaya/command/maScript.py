# coding:utf-8
from LxMaya.method.basic import _maMethodBasic


#
def hideShowCmd(operation, extend):
    operationDic = {
        'hide': u'''dict(title=u"隐藏操作", message=u"确认要隐藏吗？", button=["Yes", "No"], defaultButton="No", cancelButton="No", dismissString="No")''',
        'show': u'''dict(title=u"显示操作", message=u"确认要显示吗？", button=["Yes", "No"], defaultButton="No", cancelButton="No", dismissString="No")'''
    }
    if operation in operationDic:
        uiMethod = _maMethodBasic.Mtd_MaUiBasic
        nodeMethod = _maMethodBasic.MaNodeMethodBasic
        hasSel = nodeMethod.getSelectedNodeLis() != []
        if hasSel is True:
            result = uiMethod.getResultByDialog(
                **eval(operationDic[operation])
            )
            if result == 'Yes':
                nodeMethod.lxHideShow(operation, extend)
        else:
            nodeMethod.traceWaning('Nothing is Selected')
