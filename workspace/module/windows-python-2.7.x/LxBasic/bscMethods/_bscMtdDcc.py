# coding:utf-8
from LxBasic import bscCore


class MayaPath(bscCore.Basic):
    separator_namespace = ':'
    separator_node = '|'
    separator_attribute = '.'

    @classmethod
    def _getNamespace(cls, pathString, nodeSep, namespaceSep):
        if namespaceSep in pathString:
            return namespaceSep.join(pathString.split(nodeSep)[-1].split(namespaceSep)[:-1])
        return pathString

    @classmethod
    def _getName(cls, pathString, nodeSep, namespaceSep):
        return pathString.split(nodeSep)[-1].split(namespaceSep)[-1]

    @classmethod
    def _getAttributeName(cls, attrString, attributeSep):
        return attributeSep.join(attrString.split(attributeSep)[1:])
    
    @classmethod
    def namespaceSep(cls):
        return cls.separator_namespace

    @classmethod
    def nodeSep(cls):
        return cls.separator_node

    @classmethod
    def attributeSep(cls):
        return cls.separator_attribute

    @classmethod
    def getNamespace(cls, pathString):
        return cls._getNamespace(pathString, cls.separator_node, cls.separator_namespace)

    @classmethod
    def getName(cls, pathString):
        return cls._getName(pathString, cls.separator_node, cls.separator_namespace)

    @classmethod
    def getAttributeName(cls, pathString):
        return cls._getAttributeName(pathString, cls.separator_attribute)
