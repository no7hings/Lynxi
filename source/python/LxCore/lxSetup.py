# coding:utf-8
from LxCore import lxConfigure


class Environ(lxConfigure.Basic):
    def __init__(self):
        self._path = lxConfigure.Root()
