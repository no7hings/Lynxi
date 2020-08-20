# coding:utf-8
from .. import kitQtWgtAbs

from ..kitQtModels import _kitQtMdlUtility


class KitQtArnoldCommandRender(kitQtWgtAbs.AbsKitQtCustomToolUnitWgt):
    CLS_kit__qt__custom_unit__model = _kitQtMdlUtility.KitQtCustomToolUnitModel

    def __init__(self):
        super(KitQtArnoldCommandRender, self).__init__()
        self._initAbsKitQtCustomToolUnitWgt()
        #
        self._kit__unit__set_build_()

    def _kit__unit__set_build_(self):
        pass
