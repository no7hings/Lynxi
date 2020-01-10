# coding:utf-8
from LxBasic import bscMethods

method_html = bscMethods.HtmlText


def mtdCatchException(mtd):
    def subMtd(*args, **kwargs):

        return mtd(*args, **kwargs)

    return subMtd
