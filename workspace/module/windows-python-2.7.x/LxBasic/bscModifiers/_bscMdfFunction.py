# coding:utf-8
from LxBasic import bscObjects, bscMethods

method_html = bscMethods.HtmlText


def fncCostTimeCatch(fnc):
    def subFnc(*args, **kwargs):
        startTime = bscObjects.ActiveTime()
        traceMessage = u'Start "{}.{}" at <{}>'.format(fnc.__module__, fnc.__name__, startTime.prettify)

        bscMethods.PyMessage.traceResult(traceMessage)

        endTime = bscObjects.ActiveTime()
        traceMessage = u'Call "{}.{}" in {}s'.format(fnc.__module__, fnc.__name__, (endTime.timestamp - startTime.timestamp))
        bscMethods.PyMessage.traceResult(traceMessage)

        return fnc(*args, **kwargs)
    return subFnc


def fncExceptionCatch(fnc):
    def subFnc(*args, **kw):
        # noinspection PyBroadException
        try:
            return fnc(*args, **kw)
        except Exception:
            import traceback

            fncName = fnc.__name__
            fncModuleName = fnc.__module__
            fncFullName = '.'.join([fncModuleName, fncName])
            exceptionModule = method_html.toHtml('Python Function is Exception', 0)
            tipWin = bscObjects.If_Tip('Exception Tip', exceptionModule)
            tipWin.add(method_html.toHtmlSpanTime())

            excStr = traceback.format_exc()

            text = u'{}({}):\n {}'.format(
                fncFullName,
                ', '.join(fnc.__code__.co_varnames),
                excStr.split('fnc(*args, **kw)')[-1].lstrip().rstrip().replace('<', '&lt;').replace('>', '&gt;')
            )

            messages = text.split('\n')
            [tipWin.add(method_html.getHtmls(i, fontColor=u'yellow')) for i in messages]
            tipWin.add(method_html.getHtmls(u'@ %s' % bscObjects.System().userName, fontColor=u'orange'))

            return bscMethods.OsLog.addException(text)
    return subFnc


def fncDictSwitch(fnc):
    def subFnc(*args):
        dic = fnc(*args)
        if args:
            key = args[0]
            if key:
                return dic[key]
            else:
                return dic
        else:
            return dic
    return subFnc
