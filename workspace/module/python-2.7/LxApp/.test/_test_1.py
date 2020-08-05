# coding:utf-8
from LxBasic import bscObjects

ot = bscObjects.DagTree()

ot.addNode('/asset/test1')
ot.addNode('/shot/test0')
ot.addNode('/asset/test2')
ot.addNode('/asset/test2/test0')
ot.addNode('/set/test2/test0')
ot.addNode('/shot/test0/test0')

print ot.nodes()

print ot

