# coding:utf-8
from LxBasic import bscMtdCore

a = bscMtdCore.Mtd_BscPath._toDagpathRemapList('A/B/C', '/')


print bscMtdCore.Mtd_BscPath._getDagpathRemapDict(a, '/')
