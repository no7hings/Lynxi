# coding:utf-8
import threading


class PyThread(threading.Thread):
    def __init__(self, *args):
        threading.Thread.__init__(self)
        self.fn = args[0]
        self.args = args[1:]
    #
    def run(self):
        self.fn(*self.args)
