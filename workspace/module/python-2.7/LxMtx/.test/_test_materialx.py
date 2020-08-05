# coding:utf-8
import MaterialX


d = MaterialX.createDocument()

MaterialX.readFromXmlFile(d, 'E:/mytest/2020_0316/test_1.mtlx')

for l in d.getLooks():
    for ma in l.getMaterialAssigns():
        print ma
