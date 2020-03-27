# coding:utf-8
from LxBasic import bscObjCore


class Type(bscObjCore.Abs_BscName):
    VAR_bsc_rawtype = str, unicode

    def __init__(self, *args):
        self._initAbsBscName(*args)


class Category(bscObjCore.Abs_BscName):
    VAR_bsc_rawtype = str, unicode

    def __init__(self, *args):
        self._initAbsBscName(*args)


class Name(bscObjCore.Abs_BscName):
    VAR_bsc_rawtype = str, unicode

    def __init__(self, *args):
        self._initAbsBscName(*args)


class Porttype(bscObjCore.Abs_BscName):
    VAR_bsc_rawtype = str, unicode

    def __init__(self, *args):
        self._initAbsBscName(*args)


class Portpath(bscObjCore.Abs_BscObjpath):
    CLS_bsc_raw = Name

    VAR_bsc_pathsep = u'.'

    def __init__(self, *args):
        self._initAbsBscObjpath(*args)


class Nodename(bscObjCore.Abs_BscNodename):
    CLS_bsc_raw = Name

    VAR_bsc_namesep = u':'

    def __init__(self, *args):
        self._initAbsBscNodename(*args)


class Nodepath(bscObjCore.Abs_BscObjpath):
    CLS_bsc_raw = Nodename

    VAR_bsc_pathsep = u'/'

    def __init__(self, *args):
        self._initAbsBscObjpath(*args)
