# coding:utf-8
from LxBasic import bscObjects, bscMethods

html_method = bscMethods.Mtd_Html


def catchCostTime(fn):
    def subFnc(*args, **kwargs):

        startTime = bscObjects.ActiveTime()
        traceMessage = u'Start "{}.{}" at <{}>'.format(fn.__module__, fn.__name__, startTime.prettify)
        print
        bscMethods.PythonMessage().traceResult(traceMessage)
        #
        _connectObject = fn(*args, **kwargs)
        #
        endTime = bscObjects.ActiveTime()
        traceMessage = u'Call "{}.{}" in {}s'.format(fn.__module__, fn.__name__, (endTime.timestamp - startTime.timestamp))
        bscMethods.PythonMessage().traceResult(traceMessage)
        return _connectObject
    return subFnc


#
def catchException(fn):
    def subFnc(*args, **kw):
        # noinspection PyBroadException
        try:
            return fn(*args, **kw)
        except Exception:
            import traceback

            functionName = fn.__name__
            exceptionModule = html_method.toHtml('Python Error', 0)
            tipWin = bscMethods.If_Tip('Exception Tip', exceptionModule).ui
            tipWin.addHtml(html_method.toHtmlSpanTime())
            excStr = traceback.format_exc()
            #
            text = functionName + '(%s) is Error ' % ', '.join(fn.__code__.co_varnames) + excStr.split('fn(*args, **kw)')[-1]
            messages = text.split('\n')
            tipWin.addHtml(html_method.getHtmls(messages[0], 4))
            [tipWin.addHtml(html_method.getHtmls(i, 1)) for i in messages[1:-1]]
            tipWin.addHtml(html_method.getHtmls(u'@ %s' % bscObjects.PC().userName, 2))
            return bscMethods.PythonLog().addException(text)
    return subFnc
