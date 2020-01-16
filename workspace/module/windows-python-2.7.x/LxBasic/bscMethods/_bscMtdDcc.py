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
        return ''

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
        return cls._getNamespace(
            pathString,
            nodeSep=cls.separator_node,
            namespaceSep=cls.separator_namespace
        )

    @classmethod
    def getName(cls, pathString):
        return cls._getName(
            pathString,
            nodeSep=cls.separator_node,
            namespaceSep=cls.separator_namespace
        )

    @classmethod
    def getAttributeName(cls, pathString):
        return cls._getAttributeName(
            pathString,
            attributeSep=cls.separator_attribute
        )
