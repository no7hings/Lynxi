# coding:utf-8
from LxBasic import bscCore


class OsPath(bscCore.PathBasic):
    separator_path = u'/'
    @classmethod
    def composeBy(cls, *args):
        if isinstance(args[0], (list, tuple)):
            pathStringLis = args[0]
        else:
            pathStringLis = list(args)

        string = ''
        for i in pathStringLis:
            if i not in ['', None]:
                string += u'{}{}'.format(cls.separator_path, i)
        return string

    @classmethod
    def treeViewBuildDic(cls, pathString):
        return cls._getTreeViewBuildDic(
            cls._toTreeViewPathLis(pathString, cls.separator_path),
            cls.separator_path
        )


class MayaPath(bscCore.PathBasic):
    separator_namespace = u':'
    separator_node = u'|'
    separator_attribute = u'.'

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

    @classmethod
    def namespaceTreeViewBuildDic(cls, pathString):
        return cls._getTreeViewBuildDic(
            cls._toTreeViewPathLis(pathString, cls.separator_namespace),
            cls.separator_namespace
        )

    @classmethod
    def nodeTreeViewBuildDic(cls, pathString):
        return cls._getTreeViewBuildDic(
            cls._toTreeViewPathLis(pathString, cls.separator_node),
            cls.separator_node
        )
