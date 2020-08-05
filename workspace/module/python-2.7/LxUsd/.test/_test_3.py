# coding:utf-8
from LxBasic import bscModifiers

from pxr import Usd


@bscModifiers.fncCostTimeCatch
def loadS(f):
    return Usd.Stage.Open(f)


s = loadS(r'E:\mytest\usd\geo\test.usd_rop1.usda')

n = s.GetPrimAtPath('/asset/geo/geo_0')

print n.GetInherits().GetAllDirectInherits()

