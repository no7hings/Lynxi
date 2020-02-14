# coding:utf-8
from LxPreset.prsMethods import _prsMtdUtility

from LxCore import lxConfigure
#
from LxCore.preset import appPr, basicPr
#
none = ''


Util = type('Util', (object,), {})


def __load__(cls, dic):
    for k, v in dic.items():
        for ik, iv in v.items():
            setattr(cls, ik, iv)


__load__(
    Util,
    basicPr.getGuidePresetVariantDic(
        lxConfigure.Lynxi_Key_Pipeline,
        lxConfigure.Lynxi_Def_Value_Pipeline
    )
)

__load__(
    Util,
    _prsMtdUtility.Project.variantPresetDict(_prsMtdUtility.Project.appActiveName())
)

__load__(
    Util,
    appPr.getMayaAppPresetVariantDic()
)


