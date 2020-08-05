# coding:utf-8
import sys


class __Autonomy__(object):
    def __init__(self):
        self._buff = ""

    def write(self, out_stream):
        self._buff += out_stream


current = sys.stdout
a = __Autonomy__()
sys.stdout = a
sys.stdout = current
