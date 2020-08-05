# coding:utf-8
from LxBasic import bscObjects, bscMethods

method_html = bscMethods.TxtHtml


def fncCostTimeCatch(fnc):
    def fnc_(*args, **kwargs):
        startTime = bscMethods.OsTimestamp.active()
        traceMessage = u'start function "{}.{}"'.format(fnc.__module__, fnc.__name__)
        bscMethods.PyMessage.traceResult(traceMessage)

        _fnc = fnc(*args, **kwargs)

        endTime = bscMethods.OsTimestamp.active()
        traceMessage = u'call function "{}.{}" in {}s'.format(fnc.__module__, fnc.__name__, (endTime - startTime))
        bscMethods.PyMessage.traceResult(traceMessage)

        return _fnc
    return fnc_


def fncExceptionCatch(fnc):
    def fnc_(*args, **kw):
        # noinspection PyBroadException
        try:
            return fnc(*args, **kw)
        except Exception:
            import traceback

            fncName = fnc.__name__
            fncModuleName = fnc.__module__
            fncFullName = '.'.join([fncModuleName, fncName])
            exceptionModule = method_html.toHtml('Python Function is Exception', 0)
            tipWin = bscObjects.TipWindow('Exception Tip', exceptionModule)
            tipWin.add(method_html.toHtmlSpanTime())

            excStr = traceback.format_exc()

            text = u'{}({}):\n {}'.format(
                fncFullName,
                ', '.join(fnc.__code__.co_varnames),
                excStr.split('fnc(*args, **kw)')[-1].lstrip().rstrip().replace('<', '&lt;').replace('>', '&gt;')
            )

            messages = text.split('\n')
            [tipWin.add(method_html.getHtmls(i, fontColor=u'yellow')) for i in messages]
            tipWin.add(method_html.getHtmls(u'@ %s' % bscMethods.OsPlatform.username(), fontColor=u'orange'))

            return bscMethods.OsLog.addException(text)
    return fnc_


def fncDictSwitch(fnc):
    def fnc_(*args):
        dic = fnc(*args)
        if args:
            key = args[0]
            if key:
                return dic[key]
            else:
                return dic
        else:
            return dic
    return fnc_
