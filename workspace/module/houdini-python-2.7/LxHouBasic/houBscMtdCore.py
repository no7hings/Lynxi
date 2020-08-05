# coding:utf-8
from . import houBscCfg


class Mtd_HoBasic(houBscCfg.HouBscUtility):
    pass


class Mtd_HouGrh(Mtd_HoBasic):
    # **************************************************************************************************************** #
    @classmethod
    def _dcc_getNodCategoryObj(cls, typepathString):
        c = cls.MOD_hou.nodeType(typepathString)
        if c is not None:
            return c
        raise Exception(
            u'category "{}" is non-exist'.format(typepathString)
        )

    @classmethod
    def _dcc_getNodAttrpathString(cls, *args):
        if len(args) > 1:
            return cls.DEF_hou__node_port_pathsep.join(list(args))
        return args[0]

    @classmethod
    def _dcc_getNodFullpathNodepathStr(cls, nodepathString):
        n = cls.MOD_hou.node(nodepathString)
        if n:
            n.path()
        return nodepathString

    # **************************************************************************************************************** #
    @classmethod
    def _dcc_getNodExist(cls, nodepathString):
        if nodepathString is not None:
            return cls.MOD_hou.node(nodepathString) is not None
        return False

    # **************************************************************************************************************** #
    @classmethod
    def _dcc_getNodNodetypeStr(cls, nodepathString):
        return cls.MOD_hou.node(nodepathString).type().category().name()

    @classmethod
    def _dcc_getNodCategoryStr(cls, nodepathString):
        return cls.MOD_hou.node(nodepathString).type().nameWithCategory()

    @classmethod
    def _dcc_getNodPortIndexes(cls, nodepathString, portpathString):
        n = cls.MOD_hou.node(nodepathString)
        pt = n.parmTuple(portpathString)
        if pt is not None:
            if pt.isMultiParmInstance() is True:
                return list(pt.multiParmInstanceIndices())
            return []
        return []

    @classmethod
    def _dcc_getNodPortpathStrList_(cls, nodepathString):
        n = cls.MOD_hou.node(nodepathString)
        ps = n.allParms()
        for i in ps:
            print i.name()

    @classmethod
    def _dcc_getNodPortraw(cls, nodepathString, portpathString, **kwargs):
        if kwargs:
            pass

        n = cls.MOD_hou.node(nodepathString)
        p = n.parm(portpathString)
        if p is not None:
            return p.eval()
        else:
            raise Exception(
                u'nodepath "{}" portpath "{}" is non-exist'.format(nodepathString, portpathString)
            )

    # **************************************************************************************************************** #
    @classmethod
    def _grh_getNodRampPortraw(cls, nodepathString, portpathString, **kwargs):
        pass

    @classmethod
    def _grh_getNodRampChannelRaw(cls, nodepathString, channelPortpathString, parentPortpathString):
        n = cls.MOD_hou.node(nodepathString)
        if n is not None:
            pt = n.parmTuple(parentPortpathString)
            r = pt.eval()[0]
            if channelPortpathString.endswith(u'_position'):
                return list(r.keys())
            # [v0, v1, v2, ...]
            elif channelPortpathString.endswith(u'_value'):
                return list(r.values())
            # [r0, g0, b0, r1, b1, g1, ...]
            elif channelPortpathString.endswith(u'_color'):
                return [j for i in r.values() for j in i]
            elif channelPortpathString.endswith(u'_interpolation'):
                return [cls.DEF_hou__port_ramp_interpolation_dict[i.name()] for i in r.basis()]


class Mtd_HoUsd(Mtd_HoBasic):
    @classmethod
    def _usd__get_root_prim_(cls, stageObj, asString=False):
        if asString is True:
            return stageObj.GetPseudoRoot().GetPath().pathString
        return stageObj.GetPseudoRoot()

    @classmethod
    def _usd_stage__get_prims_(cls, stageObj, filterCategory=None, filterPath=None, asString=False):
        def addFnc_(lis_, primObj_):
            # filter
            if getCategoryFilterFnc_(primObj_) is True and getPathFilterFnc_(primObj_) is True:
                if asString is True:
                    lis_.append(primObj_.GetPath().pathString)
                else:
                    lis_.append(primObj_)

        def getCategoryFilterFnc_(primObj_):
            if filterCategoryStrList is not None:
                _typepathStr = primObj_.GetTypeName()
                return _typepathStr in filterCategoryStrList
            return True

        def getPathFilterFnc_(primObj_):
            if filterPath is not None:
                _varPattern = filterPath.replace(u'*', u'')
                if not filterPath.startswith(u'*'):
                    _varPattern = r'^' + _varPattern
                if not filterPath.endswith(u'*'):
                    _varPattern += r'$'

                _pathStr = primObj_.GetPath().pathString
                return cls.MOD_re.findall(_varPattern, _pathStr) != []
            return True

        def rcsFnc_(lis_, primObj_):
            _childPrimObjs = primObj_.GetChildren()
            if _childPrimObjs:
                if _childPrimObjs:
                    for _primObj in _childPrimObjs:
                        addFnc_(lis_, _primObj)
                        rcsFnc_(lis_, _primObj)

        lis = []

        if filterCategory is not None:
            if isinstance(filterCategory, (str, unicode)):
                filterCategoryStrList = [filterCategory]
            elif isinstance(filterCategory, (tuple, list)):
                filterCategoryStrList = filterCategory
            else:
                raise
        else:
            filterCategoryStrList = None
        #
        if filterPath is not None:
            if u'*' in filterPath:
                if filterPath.startswith(u'*'):
                    primObj = stageObj.GetPseudoRoot()
                else:
                    primObjPathStr = filterPath.replace(u'*', u'')
                    primObj = stageObj.GetPrimAtPath(primObjPathStr)
            else:
                primObj = stageObj.GetPrimAtPath(filterPath)
        else:
            primObj = stageObj.GetPseudoRoot()

        if primObj.IsValid():
            # add root
            addFnc_(lis, primObj)
            # add sub
            rcsFnc_(lis, primObj)
        return lis
