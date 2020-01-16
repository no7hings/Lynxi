# coding:utf-8
import threading

THREAD_MAX = threading.Semaphore(1024)


class DtbThread(threading.Thread):
    def __init__(self, *args):
        threading.Thread.__init__(self)
        self._fn = args[0]
        self._args = args[1:]
        #
        self._data = None
    #
    def setData(self, data):
        self._data = data
    #
    def data(self):
        return self._data
    #
    def run(self):
        self.setData(self._fn(*self._args))
    #
    def getData(self):
        return self._data


#
def fncThreadSemaphoreModifier(fn):
    def subMethod(*args, **kw):
        THREAD_MAX.acquire()
        method = fn(*args, **kw)
        THREAD_MAX.release()
        return method
    return subMethod
