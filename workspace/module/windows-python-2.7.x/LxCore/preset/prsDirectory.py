# coding:utf-8
from LxCore import lxConfigure

from LxCore.preset import prsVariant


Database = type('Database', (object,), {})


def __convert__(variantString):
    return variantString.format(**prsVariant.Util.__dict__)


def __load__(cls, dic):
    for k, v in dic.items():
        setattr(cls, k, __convert__(v))


__load__(
    Database,
    lxConfigure.DIC_directory_database
)
