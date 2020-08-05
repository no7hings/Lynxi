# coding:utf-8
from LxBasic import bscModifiers

from pxr import Usd


@bscModifiers.fncCostTimeCatch
def loadS(f):
    return Usd.Stage.Open(f)


s = loadS(r'E:\mytest\2020_0521\geo\test.usd_rop1.usd')

p = s.GetDefaultPrim()

vs = p.GetVariantSets()

v = vs.GetVariantSet('shader')

v.SetVariantSelection('look_0')

# print v.GetVariantNames()
# print v.GetVariantSelection()
ec = v.GetVariantEditContext()
et = v.GetVariantEditTarget()

ps = et.GetPrimSpecForScenePath('/asset/geo')

# print ps.GetVariantNames()

p__ = s.GetPrimAtPath('/asset/geo')
print p__.GetPath().GetPrimOrPrimVariantSelectionPath()

# s.Flatten()

print p__.GetProperties()


