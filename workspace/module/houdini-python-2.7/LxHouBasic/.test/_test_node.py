# coding:utf-8
from LxHouBasic import houBscObjects

s1 = '/stage/look_0'

n1 = houBscObjects.Node(s1)

print n1

for i in n1.ports():
    print i
