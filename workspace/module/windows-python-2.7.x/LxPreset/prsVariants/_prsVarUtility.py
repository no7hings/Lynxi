# coding:utf-8
from LxCore import lxConfigure
#
from LxCore.preset import appPr, basicPr
#
from LxCore.preset.prod import projectPr
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
    projectPr.getProjectPresetVariantDic(
        projectPr.getAppProjectName()
    )
)

__load__(
    Util,
    appPr.getMayaAppPresetVariantDic()
)


