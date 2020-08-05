# coding:utf-8
import re

s = 'test_0[0].test_1[0]'

varPattern = re.compile(r'[\[](.*?)[\]]', re.S)
indexes = re.findall(varPattern, s)

print indexes

for i in indexes:
    s = s.replace('[{}]'.format(i), '')

print s

