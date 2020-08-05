# coding:utf-8
from . import bscCfg, bscMethods


class Itf_BscBasic(bscCfg.BscUtility):
    pass


class Itf_BscObjStack(Itf_BscBasic):
    VAR_grh__obj_stack__objsep = u','

    def _initItfBscObjStack(self, *args):
        if args:
            self._obj = args[0]
        else:
            self._obj = 'unknown'

        self._objKeyStrList = []
        self._nodeObjList = []

        self._nodeCount = 0

    def _obj_stack__set_obj_exist_val_(self, *args):
        if args:
            _ = args[0]
            if isinstance(args[0], (str, unicode)):
                objKeyStr = _
                if not objKeyStr in self._objKeyStrList:
                    raise KeyError(
                        u'''stack "{}.{}" > object "{}.{}": key "{}" is not in "{}".'''.format(
                            self.__class__.__module__, self.__class__.__name__,
                            self._obj.__class__.__module__, self._obj.__class__.__name__,
                            objKeyStr, self._objKeyStrList
                        )
                    )
        else:
            raise KeyError(
                u'''stack "{}.{}" > object "{}.{}": key Must not be empty.'''.format(
                    self.__class__.__module__, self.__class__.__name__,
                    self._obj.__class__.__module__, self._obj.__class__.__name__
                    )
            )

    # **************************************************************************************************************** #
    def _obj_stack__set_data_int_(self):
        self._objKeyStrList = []
        self._nodeObjList = []

        self._nodeCount = 0

    def restore(self):
        self._obj_stack__set_data_int_()

    # **************************************************************************************************************** #
    def _obj_stack__get_obj_key_str_(self, obj):
        """
        replace method
        """

    def getObjectKeyString(self, *args):
        obj = args[0]
        if obj is not None:
            return self._obj_stack__get_obj_key_str_(obj)
        raise TypeError(
            u'''stack "{}.{}" > object "{}.{}": arg is "None"'''.format(
                self.__class__.__module__, self.__class__.__name__,
                self._obj.__class__.__module__, self._obj.__class__.__name__
            )
        )

    # **************************************************************************************************************** #
    def _obj_stack__get_str_(self):
        return self.VAR_grh__obj_stack__objsep.join([self.getObjectKeyString(obj) for obj in self.objects()])

    def _obj_stack__set_obj_add_(self, *args, **kwargs):
        if len(args) == 1:
            obj = args[0]
            # noinspection PyNoneFunctionAssignment
            objKeyStr = self.getObjectKeyString(obj)
        elif len(args) == 2:
            objKeyStr, obj = args
        else:
            raise TypeError()

        if objKeyStr not in self._objKeyStrList:
            indexArg = None
            if kwargs:
                if u'index' in kwargs:
                    indexArg = kwargs[u'index']

            if indexArg is not None:
                self._objKeyStrList.insert(indexArg, objKeyStr)
                self._nodeObjList.insert(indexArg, obj)
            else:
                self._objKeyStrList.append(objKeyStr)
                self._nodeObjList.append(obj)

            self._nodeCount += 1

    def addObject(self, *args, **kwargs):
        obj = args[0]
        # noinspection PyNoneFunctionAssignment
        objKeyStr = self.getObjectKeyString(obj)
        if objKeyStr not in self._objKeyStrList:
            self._obj_stack__set_obj_add_(*args, **kwargs)
        else:
            raise TypeError(
                u'''stack "{}.{}" > object "{}.{}": key "{}" is exist.'''.format(
                    self.__class__.__module__, self.__class__.__name__,
                    self._obj.__class__.__module__, self._obj.__class__.__name__,
                    objKeyStr
                )
            )

    def _obj_stack__get_objs_exist_(self, **kwargs):
        if kwargs:
            if u'filter' in kwargs:
                objKeyStr = kwargs[u'filter']
                return self.MOD_fnmatch.filter(
                    self._objKeyStrList, objKeyStr
                ) != []
        return self._objKeyStrList != []

    def hasObjects(self, **kwargs):
        """
        :return: bool
        """
        return self._obj_stack__get_objs_exist_(**kwargs)

    def _obj_stack__get_obj_list_(self, **kwargs):
        if kwargs:
            if u'filter' in kwargs:
                objKeyStr = kwargs[u'filter']
                keyStrList = self.MOD_fnmatch.filter(self._objKeyStrList, objKeyStr)
                return [self._nodeObjList[self._objKeyStrList.index(i)] for i in keyStrList]
        return self._nodeObjList

    def objects(self, **kwargs):
        """
        :return: list(object, ...)
        """
        return self._obj_stack__get_obj_list_(**kwargs)

    def _obj_stack__get_obj_exist_(self, *args):
        _ = args[0]
        if isinstance(_, (str, unicode)):
            objKeyStr = _
            return objKeyStr in self._objKeyStrList
        elif isinstance(_, int):
            index = _
            return 0 <= index <= (self._nodeCount - 1)
        elif isinstance(_, object):
            obj = _
            # noinspection PyNoneFunctionAssignment
            objKeyStr = self.getObjectKeyString(obj)
            return objKeyStr in self._objKeyStrList
        return False

    def hasObject(self, *args):
        """
        :param args: str
        :return: bool
        """
        return self._obj_stack__get_obj_exist_(*args)

    def _obj_stack__get_obj_(self, *args):
        _ = args[0]
        # key str
        if isinstance(_, (str, unicode)):
            objKeyStr = _
            if objKeyStr in self._objKeyStrList:
                index = self._objKeyStrList.index(objKeyStr)
                return self._nodeObjList[index]

            raise TypeError(
                u'''stack "{}.{}" > object "{}.{}": key "{}" is not in {}'''.format(
                    self.__class__.__module__, self.__class__.__name__,
                    self._obj.__class__.__module__, self._obj.__class__.__name__,
                    objKeyStr,
                    self._objKeyStrList
                )
            )
        # index
        elif isinstance(_, (int, float)):
            index = _
            return self._nodeObjList[int(index)]
        # object
        elif isinstance(_, object):
            obj = _
            # noinspection PyNoneFunctionAssignment
            objKeyStr = self.getObjectKeyString(obj)
            if objKeyStr in self._objKeyStrList:
                index = self._objKeyStrList.index(objKeyStr)
                return self._nodeObjList[index]
            return obj
        raise TypeError(
            u'''???'''
        )

    def object(self, *args):
        """
        :param args:
            1.args[0]
        :return: object
        """
        self._obj_stack__set_obj_exist_val_(*args)
        if args:
            _objKeyStr = args[0]
            return self._obj_stack__get_obj_(*args)

    def _obj_stack__get_obj_index_(self, *args):
        if isinstance(args[0], (str, unicode)):
            objKeyStr = args[0]
            return self._objKeyStrList.index(objKeyStr)
        elif isinstance(args[0], (int, float)):
            index = args[0]
            return int(index)
        elif isinstance(args[0], object):
            obj = args[0]
            return self._nodeObjList.index(obj)
        raise TypeError('''???''')

    def index(self, *args):
        """
        :param args:
        :return: int(0)
        """
        return self._obj_stack__get_obj_index_(*args)

    def objectsCount(self):
        """
        :return: int
        """
        return self._nodeCount

    def objectAt(self, index):
        """
        :param index: int
        :return: object
        """
        return self._obj_stack__get_obj_(index)

    def hasObjectAt(self, index):
        """
        :param index: int
        :return: object
        """
        return self._obj_stack__get_obj_exist_(index)

    # **************************************************************************************************************** #
    def _obj_stack__set_obj_rename_(self, obj, newObjKeyStr):
        index = self._nodeObjList.index(obj)
        if self._objKeyStrList[index] != newObjKeyStr:
            self._objKeyStrList[index] = newObjKeyStr

    def _obj_stack__set_obj_replace_(self, obj):
        # noinspection PyNoneFunctionAssignment
        objKeyStr = self.getObjectKeyString(obj)
        index = self._objKeyStrList.index(objKeyStr)
        self._nodeObjList[index] = obj

    # **************************************************************************************************************** #
    def keys(self):
        return self._objKeyStrList

    # **************************************************************************************************************** #
    def toString(self):
        """
        :return: str
        """
        return self._obj_stack__get_str_()

    def __str__(self):
        return u'''{}(object="{}")'''.format(
            self.__class__.__name__,
            self._obj.__class__.__name__
        )

    # **************************************************************************************************************** #
    def __len__(self):
        """
        :return: int
        """
        return self.objectsCount()


# obj **************************************************************************************************************** #
class ItfBscObjDef(Itf_BscBasic):
    def _initItfBscObjDef(self, *args, **kwargs):
        self._objTypeStr = None
        self._objPathStr = args[0]
        self._pathsepStr = kwargs[u'pathsep']
        if u'name' in args:
            self._objNameStr = kwargs[u'name']
        else:
            if self._objPathStr == self._pathsepStr:
                self._objNameStr = self._pathsepStr
            else:
                self._objNameStr = self._objPathStr.split(self._pathsepStr)[-1]

        if u'parent' in kwargs:
            self.setParent(kwargs[u'parent'])
        else:
            self._parentObj = None

        self._childObjList = []

        self._pathsepStr = None

    def setType(self, *args):
        self._objTypeStr = args[0]

    def type(self):
        return self._objTypeStr

    def path(self):
        return self._objPathStr

    def name(self):
        return self._objNameStr

    def setParent(self, *args):
        obj = args[0]
        self._parentObj = obj
        if isinstance(obj, self.__class__):
            obj.addChild(self)

    def hasParent(self):
        return self._parentObj is not None

    def parent(self):
        return self._parentObj

    def allParents(self):
        def rcsFnc_(obj_):
            _parentObj = obj_.parent()
            if _parentObj is not None:
                lis.append(_parentObj)
                rcsFnc_(_parentObj)

        lis = []
        rcsFnc_(self)
        return lis

    def addChild(self, *args):
        obj = args[0]
        if obj not in self._childObjList:
            self._childObjList.append(obj)

    def child(self, *args):
        index = args[0]
        return self._childObjList[index]

    def children(self):
        return self._childObjList

    def allChildren(self):
        def rcsFnc_(nodeObj_, lis_):
            for _i in nodeObj_.children():
                lis_.append(_i)
                rcsFnc_(_i, lis_)

        lis = []
        rcsFnc_(self, lis)
        return lis

    def childrenCount(self):
        return len(self._childObjList)

    def allChildrenCount(self):
        return len(self.allChildren())

    def childIndex(self, *args):
        if args:
            obj = args[0]
            return self._childObjList.index(obj)
        elif self.hasParent():
            return self.parent().childIndex(self)
        raise

    def isLastChild(self, *args):
        if args:
            obj = args[0]
            return self.childIndex(obj) == (self.childrenCount() - 1)
        elif self.hasParent():
            return self.parent().isLastChild(self)
        return False

    def _format_dict_(self):
        return {
            'self': self
        }

    @property
    def pathsep(self):
        return self._pathsepStr

    @pathsep.setter
    def pathsep(self, *args):
        self._pathsepStr = args[0]

    def __str__(self):
        return u'{}(path="{}")'.format(
            self.__class__.__name__,
            self.path()
        )

    def __repr__(self):
        return self.__str__()


class Itf_BscPort(ItfBscObjDef):
    def _initItfBscPort(self, *args, **kwargs):
        self._initItfBscObjDef(*args, **kwargs)

        self._raw = None

    def setRaw(self, *args):
        self._raw = args[0]

    def raw(self):
        return self._raw


class Itf_BscNode(ItfBscObjDef):
    CLS_bsc__node__port = None
    CLS_bsc__node__port_stack = None

    VAR_bsc__node__port_default_dict = {}

    def _initItfBscNode(self, *args, **kwargs):
        self._initItfBscObjDef(*args, **kwargs)

        if u'port' in kwargs:
            self._portRaw = kwargs[u'port']
        else:
            self._portRaw = {}

        self._portStackObj = self.CLS_bsc__node__port_stack(self)

        self._bsc__obj__set_ports_build_()

    def _bsc__obj__set_ports_build_(self):
        defaultRaw = self.VAR_bsc__node__port_default_dict
        for k, v in defaultRaw.items():
            if k in self._portRaw:
                value = self._portRaw[k]
            else:
                if isinstance(v, (str, unicode)):
                    value = v.format(**self._format_dict_())
                else:
                    value = v
                self._portRaw[k] = value
            #
            self.__dict__[k] = value

    def setPropertyRaw(self, *args):
        self._portRaw = args[0]
        self._bsc__obj__set_ports_build_()

    def ports(self):
        return self._portStackObj.objects()

    def port(self, *args):
        return self._portStackObj.object(*args)

    def hasPort(self, *args):
        return self._portStackObj.hasObject(*args)

    def addPort(self, *args):
        _ = args[0]
        if isinstance(_, self.CLS_bsc__node__port):
            obj = _
            self._portStackObj.addObject(obj)
        elif isinstance(_, (str, unicode)):
            obj = self.CLS_bsc__node__port(
                _
            )
            self._portStackObj.addObject(obj)


class Itf_BscDagTree(Itf_BscBasic):
    CLS_bsc__node_tree__node = None
    CLS_bsc__node_tree__node_stack = None

    DEF_bsc__node_tree__key__nodesep = u'nodesep'
    DEF_bsc__node_tree__key__portsep = u'portsep'

    DEF_bsc__node_tree__key__node = u'node'
    DEF_bsc__node_tree__key__port = u'port'

    VAR_bsc__node_tree__value__nodesep_default = u'/'
    VAR_bsc__node_tree__value__portsep_default = u'.'

    def _initItfBscDagTree(self, *args):
        if args:
            _ = args[0]
            if isinstance(_, dict):
                self._raw = _
            elif bscMethods.OsPath.isFile(_):
                self._raw = bscMethods.OsJsonFile.read(_) or {}
            else:
                raise
        else:
            self._raw = {}

        self._nodeStackObj = self.CLS_bsc__node_tree__node_stack(self)

        self._nodesepStr = self._raw.get(
            self.DEF_bsc__node_tree__key__nodesep, self.VAR_bsc__node_tree__value__nodesep_default
        )
        self._portsepStr = self._raw.get(
            self.DEF_bsc__node_tree__key__portsep, self.VAR_bsc__node_tree__value__portsep_default
        )
        #
        self._bsc__node_tree__set_build_()

    def _bsc__node_tree__set_build_(self):
        if self._raw:
            self._bsc__node_tree__set_build_by_raw_()
        # add root
        else:
            pathStr = self.nodesep
            obj = self.CLS_bsc__node_tree__node(
                pathStr,
                pathsep=self.nodesep,
                name=self.nodesep
            )
            self._nodeStackObj.addObject(obj)

    def _bsc__node_tree__set_build_by_raw_(self):
        self._bsc__node_tree__set_nodes_build_by_raw_()
        self._bsc__node_tree__set_ports_build_by_raw_()

    def _bsc__node_tree__set_nodes_build_by_raw_(self):
        def rcsFnc_(objPathStr_, objNameStr_, parentObj_):
            _nodeObj = self.CLS_bsc__node_tree__node(
                objPathStr_,
                pathsep=self.nodesep,
                name=objNameStr_,
                parent=parentObj_
            )
            self._nodeStackObj.addObject(_nodeObj)
            #
            if objPathStr_ in self._nodeRaw:
                _childNameStrList = self._nodeRaw[objPathStr_]
                for _childNameStr in _childNameStrList:
                    if objPathStr_ == self._nodesepStr:
                        _childPathStr = objPathStr_ + _childNameStr
                    else:
                        _childPathStr = self._nodesepStr.join(
                            [objPathStr_, _childNameStr]
                        )
                    rcsFnc_(_childPathStr, _childNameStr, _nodeObj)

        self._nodeRaw = self._raw.get(
            self.DEF_bsc__node_tree__key__node,
            {}
        )
        if self._nodeRaw:
            rcsFnc_(self._nodesepStr, self._nodesepStr, None)

    def _bsc__node_tree__set_ports_build_by_raw_(self):
        def lopFnc_(pathKey_, portRaw_):
            _nodeObjList = self.nodes(filter=pathKey_)
            for _nodeObj in _nodeObjList:
                _nodeObj.setPropertyRaw(portRaw_)

        self._portRaw = self._raw.get(
            self.DEF_bsc__node_tree__key__port,
            {}
        )
        if self._portRaw:
            for k, v in self._portRaw.items():
                lopFnc_(k, v)

    def restore(self):
        self._nodeStackObj.restore()

    def root(self):
        return self.node(self.nodesep)

    def _bsc__node_tree__set_node_add_by_path_str_(self, *args):
        pathStr = args[0]
        pathStrList = bscMethods.OsPath._toDagpathRemapList(pathStr, self.nodesep)
        for seq, pathStr in enumerate(pathStrList):
            if self._nodeStackObj.hasObject(pathStr) is False:
                if seq > 0:
                    parentPathStr = pathStrList[seq - 1]
                else:
                    parentPathStr = self.nodesep

                parentObj = self._nodeStackObj.object(parentPathStr)
                obj = self.CLS_bsc__node_tree__node(
                    pathStr,
                    pathsep=self.nodesep,
                    parent=parentObj
                )
                parentIndex = self.nodeIndex(parentObj)
                childIndex = parentObj.childIndex(obj)
                if childIndex > 0:
                    parentAllChildrenCount = parentObj.allChildrenCount()
                    index = parentIndex + parentAllChildrenCount
                else:
                    index = parentIndex + 1
                self._nodeStackObj.addObject(obj, index=index)

    def addNode(self, *args):
        _ = args[0]
        if isinstance(args[0], self.CLS_bsc__node_tree__node):
            obj = _
            self._nodeStackObj.addObject(obj)
        elif isinstance(args[0], (str, unicode)):
            self._bsc__node_tree__set_node_add_by_path_str_(_)
        else:
            raise

    def hasNode(self, *args):
        return self._nodeStackObj.hasObject(*args)

    def node(self, *args):
        return self._nodeStackObj.object(*args)

    def nodeIndex(self, *args):
        return self._nodeStackObj.index(*args)

    def nodes(self, **kwargs):
        return self._nodeStackObj.objects(**kwargs)

    @property
    def nodesep(self):
        """"""
        return self._nodesepStr

    @property
    def portsep(self):
        return self._portsepStr

    def _bsc__node_tree__str_(self, indent=4):
        def rscFnc_(nodeObj_, depth_):
            _indentStr = (depth_-1) * defIndentStr

            _allParentObjList = nodeObj_.allParents()

            isLastList = [i.isLastChild() for i in _allParentObjList]
            isLastList.reverse()
            _str = ''

            if depth_ == 0:
                _str = nodeObj_.name()
            else:
                _c = len(isLastList)
                for _s, i in enumerate(isLastList):
                    if _s > 0:
                        if i is True:
                            _str += ' {}'.format(' '*indent)
                        else:
                            _str += '|{}'.format(' '*indent)

                _str += '|{} '.format('_'*indent)
                _str += nodeObj_.name()

            depth_ += 1
            lis.append(_str)
            for _i in nodeObj_.children():
                rscFnc_(_i, depth_)

        defIndentStr = u' ' * indent
        lis = []
        rootObj = self.root()
        rscFnc_(rootObj, 0)
        return self.DEF_bsc__linesep.join(lis)

    def __iadd__(self, other):
        if isinstance(other, Itf_BscDagTree):
            for i in other.nodes():
                pathStr = i.path()
                if self.hasNode(pathStr) is False:
                    self.addNode(pathStr)
        return self

    def __str__(self):
        return self._bsc__node_tree__str_()
