# coding:utf-8
from LxGraph import grhAbstract


class NodeSet(grhAbstract.AbcObjectSet):
    def __init__(self):
        self._initAbcObjectSet()


class AttributeSet(grhAbstract.AbcObjectSet):
    def __init__(self):
        self._initAbcObjectSet()
