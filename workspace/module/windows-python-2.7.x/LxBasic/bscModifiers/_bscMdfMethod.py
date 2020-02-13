# coding:utf-8
from LxBasic import bscCore, bscMethods

method_html = bscMethods.TxtHtml


def mtdCatchException(mtd):
    def subMtd(*args, **kwargs):

        return mtd(*args, **kwargs)

    return subMtd


def mtdDictSwitch(mtd):
    def subFnc(*args):
        dic = mtd(*args)
        if args:
            key = args[1]
            if key:
                return dic[key]
            else:
                return dic
        else:
            return dic
    return subFnc
