# coding:utf-8
from LxUsd import usdCommands, usdObjects

s_ = usdCommands.loadScene(r'E:\mytest\2020_0521\geo\test.usd_rop1.usd')

n = usdObjects.Node('/asset/materials/material_0/standard_surface1')

for p in n.ports():
    print p.portraw()
