# coding:utf-8
from LxUsd import usdCommands, usdObjects

s_ = usdCommands.loadScene(r'E:\usd_test\Kitchen_set\geo\Bottle.usd_rop1.usd')

r = usdObjects.Node('/')

n = usdObjects.Node('/Bottle')

for p in r.allChildren(include='Mesh'):
    op = p.overrideInport('primvars:arnold:subdiv_iterations')
    if op is not None:
        print op.portraw(), "B"
    else:
        print p.pathString()
