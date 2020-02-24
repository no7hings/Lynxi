# coding:utf-8
from LxPreset import prsMtdCore

from LxPreset.prsMethods import _prsMtdUtility
#
from LxCore.preset import appPr
#
none = ''


Util = type('Util', (object,), {})


def __load__(cls, dic):
    for k, v in dic.items():
        for ik, iv in v.items():
            setattr(cls, ik, iv)


__load__(Util, prsMtdCore.Mtd_PrsUtility.getGuidePresetVariantDic(prsMtdCore.Mtd_PrsUtility.DEF_key_preset_pipeline, prsMtdCore.Mtd_PrsUtility.VAR_value_pipeline_default))

__load__(Util, _prsMtdUtility.Project.variantPresetDict())

__load__(Util, appPr.getMayaAppPresetVariantDic())
