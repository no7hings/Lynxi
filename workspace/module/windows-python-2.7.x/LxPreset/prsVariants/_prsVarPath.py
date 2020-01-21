# coding:utf-8
from LxPreset import prsConfigure

from LxPreset.prsVariants import _prsVarUtility

Database = type('Database', (object,), {})


class Asset(object):
    def __init__(self):
        pass

    @property
    def name(self):
        return None

    @property
    def variant(self):
        return None


def __convert__(variantString):
    return variantString.format(**_prsVarUtility.Util.__dict__)


def __load__(cls, dic):
    for k, v in dic.items():
        setattr(cls, k, __convert__(v))


__load__(
    Database,
    prsConfigure.DIC_path_database
)
