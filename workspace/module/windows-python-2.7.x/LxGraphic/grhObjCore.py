# coding:utf-8
from LxBasic.bscMethods import _bscMtdRaw

from .import grhObjDef


class Abs_GrhObjSet(grhObjDef.Def_GrhObjSet):
    def _initAbsGrhObjSet(self, *args):
        self._initDefGrhObjSet(*args)

    def _initializeData_(self):
        self._objectList = []
        self._objectFilterDict = {}

        self._objectCount = 0

    def _get_object_key_string_(self, obj):
        pass

    def _get_string_(self):
        return self.VAR_grh_objectsep.join([i.toString() for i in self.objects()])


class Abs_GrhPort(grhObjDef.Def_GrhPort):
    def _initAbsGrhPort(self, *args):
        self._initDefGrhPort(*args)


class Abs_GrhNode(grhObjDef.Def_GrhNode):
    def _initAbsGrhNode(self, *args):
        self._initDefGrhNode(*args)

    @classmethod
    def _get_nodes_filter_(cls, nodeObjects, *args):
        lis = []
        if args:
            categoryString = _bscMtdRaw.String.toList(args[0])
        else:
            categoryString = None

        for i in nodeObjects:
            _categoryString = i.categoryString()
            if categoryString is not None:
                if _categoryString in categoryString:
                    lis.append(i)
            else:
                lis.append(i)
        return lis
