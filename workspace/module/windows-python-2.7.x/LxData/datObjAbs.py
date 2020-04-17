# coding:utf-8
from . import datObjDef


class Abs_DatRaw(datObjDef.Def_DatRaw):
    def _initAbsDatRaw(self, *args):
        self._initDefDatRaw(*args)


class Abs_DatNodename(datObjDef.Def_DatNodename):
    def _initAbsDatNodename(self, *args):
        self._initDefDatFilename(*args)

    def _set_raw_to_rawobj_(self, raw):
        if self.CLS_dat_raw is not None:
            return self.CLS_dat_raw(raw)

    def _set_raw_create_(self, *args):
        if args:
            raw = args[0]
            if raw is not None:
                self._set_raw_val_(raw)

                _ = raw.split(self.VAR_dat_namesep)
                if len(_) == 1:
                    namespaceString = None
                    nameString = _[0]
                else:
                    namespaceString = self.VAR_dat_namesep.join([i for i in _[:-1] if i])
                    nameString = _[-1]

                self._namespaceObj.setRaw(namespaceString)
                self._nameObj.setRaw(nameString)

                self._rawObj = self._get_raw_()

    def _set_rawstr_create_(self, *args):
        self._set_raw_create_(*args)

    def _get_raw_(self):
        return self._set_raw_to_rawobj_(
            self._get_rawstr_()
        )

    def _get_rawstr_(self):
        return self.VAR_dat_namesep.join(
            [
                i
                for i in [self._namespaceObj.toString(), self._nameObj.toString()]
                if i
            ]
        )


class Abs_DatFilename(datObjDef.Def_DatFilename):
    def _initAbsDatFilename(self, *args):
        self._initDefDatFilename(*args)

    def _set_raw_to_rawobj_(self, raw):
        if self.CLS_dat_raw is not None:
            return self.CLS_dat_raw(raw)

    def _set_raw_create_(self, *args):
        if args:
            raw = args[0]
            if raw is not None:
                self._set_raw_val_(raw)

                _ = raw.split(self.VAR_dat_extsep)
                if len(_) == 1:
                    baseString = _[0]
                    extString = None
                else:
                    baseString = self.VAR_dat_extsep.join(_[:-1])
                    extString = _[-1]

                self._baseObj.setRaw(baseString)
                self._extObj.setRaw(extString)

                self._rawObj = self._get_raw_()

    def _set_rawstr_create_(self, *args):
        self._set_raw_create_(*args)

    def _get_raw_(self):
        return self._set_raw_to_rawobj_(
            self._get_rawstr_()
        )

    def _get_rawstr_(self):
        return self.VAR_dat_extsep.join(
            [
                i
                for i in [self._baseObj.toString(), self._extObj.toString()]
                if i
            ]
        )


class Abs_DatPath(datObjDef.Def_DatPath):
    def _initAbsDatPath(self, *args):
        self._initDefDatPath(*args)

    def _set_raw_create_(self, *args):
        if args:
            raw = args[0]
            if raw is not None:
                self._set_raw_val_(raw)

                pathsep = self.VAR_dat_pathsep

                _ = raw.split(pathsep)

                if len(_) == 1:
                    dirnameString = None
                    bscnameString = _[-1]
                else:
                    dirnameString = pathsep.join([i for i in _[:-1]])
                    bscnameString = _[-1]

                self._dirnameObj.setRaw(dirnameString)
                self._bscnameObj.setRaw(bscnameString)

                self._rawObj = self._get_raw_()

    def _set_rawstr_create_(self, *args):
        self._set_raw_create_(*args)

    def _get_raw_(self):
        return self._set_raw_to_rawobj_(
            self._get_rawstr_()
        )

    def _get_rawstr_(self):
        pathsep = self.VAR_dat_pathsep
        return pathsep.join(
           [
               i
               for i in [self._dirnameObj.toString(), self._bscnameObj.toString()]
               if i
           ]
        )


class Abs_DatAttrpath(datObjDef.Def_DatAttrpath):
    def _initAbsDatAttrpath(self, *args):
        self._initDefDatAttrpath(*args)

    def _set_raw_create_(self, *args):
        if args:
            if len(args) == 1:
                raw = args[0]
                if raw is not None:
                    self._set_raw_val_(raw)

                    pathsep = self._portpathObj.pathsep()

                    _ = raw.split(pathsep)

                    if len(_) == 1:
                        nodepathString = None
                        portpathString = _[-1]
                    else:
                        nodepathString = _[0]
                        portpathString = pathsep.join([i for i in _[1:]])

                    self._nodepathObj.setRaw(nodepathString)
                    self._portpathObj.setRaw(portpathString)

            elif len(args) == 2:
                nodepathRaw, portpathRaw = args
                if isinstance(nodepathRaw, Abs_DatPath):
                    self._nodepathObj = nodepathRaw
                elif isinstance(nodepathRaw, (str, unicode)):
                    self._nodepathObj.setRaw(nodepathRaw)

                if isinstance(portpathRaw, Abs_DatPath):
                    self._portpathObj = portpathRaw
                elif isinstance(portpathRaw, (str, unicode)):
                    self._portpathObj.setRawString(portpathRaw)

    def _set_rawstr_create_(self, *args):
        self._set_raw_create_(*args)

    def _get_raw_(self):
        return self._set_raw_to_rawobj_(
            self._get_rawstr_()
        )

    def _get_rawstr_(self):
        pathsep = self._portpathObj.pathsep()
        return pathsep.join(
           [
               i
               for i in [self._nodepathObj.toString(), self._portpathObj.toString()]
               if i
           ]
        )


# value ************************************************************************************************************** #
class Abs_DatData(datObjDef.Def_DatRaw):
    CLS_dat_data = None

    VAR_dat_compraw_strsep = None

    def _initAbsDatData(self, *args):
        self._parentObj = args[0]
        rawArgs = args[1:]

        if isinstance(args[0], Abs_DatValue):
            self._valueObj = self._parentObj

            self._rawtypePattern = self._valueObj.VAR_dat_rawtype_pattern
            self._rawtypeStrPattern = self._valueObj.VAR_dat_rawtype_str_pattern
            self._rawsizePattern = self._valueObj.VAR_dat_rawsize_pattern
        elif isinstance(args[0], Abs_DatData):
            self._multidataObj = self._parentObj

            if len(self._multidataObj._rawtypePattern) == 2:
                self._rawtypePattern = self._multidataObj._rawtypePattern[-1]
            else:
                self._rawtypePattern = self._multidataObj._rawtypePattern[1:]

            if len(self._multidataObj._rawtypeStrPattern) == 2:
                self._rawtypeStrPattern = self._multidataObj._rawtypeStrPattern[-1]
            else:
                self._rawtypeStrPattern = self._multidataObj._rawtypeStrPattern[1:]

            if len(self._multidataObj._rawsizePattern) == 2:
                self._rawsizePattern = self._multidataObj._rawsizePattern[-1]
            else:
                self._rawsizePattern = self._multidataObj._rawsizePattern[1:]
        else:
            self._rawtypePattern = None
            self._rawtypeStrPattern = None
            self._rawsizePattern = None

        self._childDataObjList = []

        self._set_create_(*rawArgs)

    @staticmethod
    def _fnc_get_list_split_(lis, splitCount):
        lis_ = []

        count = len(lis)
        cutCount = int(count / splitCount)
        for i in range(cutCount + 1):
            subLis = lis[i * splitCount:min((i + 1) * splitCount, count)]
            if subLis:
                if len(subLis) == 1:
                    lis_.append(subLis[0])
                else:
                    lis_.append(subLis)
        return lis_

    def _get_rawtypestr_(self):
        if self._rawtypeStrPattern is not None:
            if isinstance(self._rawtypeStrPattern, (tuple, list)):
                return self._rawtypeStrPattern[0]
            return self._rawtypeStrPattern

    def clear(self):
        self._childDataObjList = []

    def rawsize(self):
        """
        :return: int
        """
        if self._get_is_comp_():
            return self._rawsizePattern[0]
        return self._rawsizePattern

    # child ********************************************************************************************************** #
    def addChild(self, datumObject):
        """
        :param datumObject: object of Data
        :return: None
        """
        self._childDataObjList.append(datumObject)

    def hasChildren(self):
        """
        :return: bool
        """
        return self._childDataObjList != []

    def children(self):
        """
        :return: list(object of Data)
        """
        return self._childDataObjList

    def childrenCount(self):
        """
        :return: int
        """
        return len(self._childDataObjList)

    def childAt(self, index):
        """
        :param index: object of Data
        :return:
        """
        return self.children()[index]

    def childRawtype(self):
        """
        :return: class of raw
        """
        return self._rawtypePattern[1]

    def childRawsize(self):
        """
        :return: int
        """
        return self._rawsizePattern[1]

    def _get_is_comp_(self):
        return isinstance(self._rawtypePattern, (tuple, list))

    # raw ************************************************************************************************************ #
    def _get_raw_cls_(self):
        if self._rawtypePattern is not None:
            if isinstance(self._rawtypePattern, (tuple, list)):
                return self._rawtypePattern[0]
            return self._rawtypePattern
        return self.CLS_dat_raw

    def _set_raw_to_rawobj_(self, raw):
        cls = self._get_raw_cls_()
        if cls is not None:
            return cls(raw)

    def _set_compraw_to_rawobj_(self, *args):
        raw = args[0]
        self.clear()

        [self.addChild(self.CLS_dat_data(self, i)) for i in raw]
        cls = self._get_raw_cls_()
        if cls is not None:
            return cls([i.raw() for i in self.children()])

    def _set_raw_create_(self, *args):
        if args:
            if self._get_is_comp_():
                if isinstance(args[0], (tuple, list)):
                    if len(args) == 1:
                        compraw = args[0]
                    else:
                        if self.childRawtype() in (tuple, list):
                            if len(args[0]) == self.childRawsize():
                                compraw = args
                            else:
                                raise ValueError("value format is error")
                        else:
                            compraw = args
                else:
                    compraw = args

                if isinstance(self.rawsize(), int):
                    compraw = compraw[:self.rawsize()]

                self._rawObj = self._set_compraw_to_rawobj_(compraw)
            else:
                raw = args[0]
                if raw is not None:
                    self._set_raw_val_(raw)

                    self._rawObj = self._set_raw_to_rawobj_(raw)

    def _get_compraw_(self):
        cls = self._get_raw_cls_()
        if cls is not None:
            return cls([i._get_raw_() for i in self.children()])

    def _get_raw_(self):
        if self._get_is_comp_():
            return self._get_compraw_()
        return self._rawObj

    # rawstr ********************************************************************************************************* #
    def _set_rawstr_to_rawobj_(self, rawString):
        if self.CLS_dat_raw is not None:
            return self.CLS_dat_raw(rawString)

    def _set_comprawstr_to_rawobj_(self, *args):
        rawstr = args[0]
        self.clear()
        [self.addChild(self.CLS_dat_data(self, i)) for i in rawstr]
        cls = self._get_raw_cls_()
        if cls is not None:
            return cls([i.raw() for i in self.children()])

    def _set_rawstr_create_(self, *args):
        if args:
            rawstr = args[0]
            if rawstr is not None:
                self._set_rawstr_val_(rawstr)
                if self._get_is_comp_():
                    valueStringLis = [i.lstrip().rstrip() for i in args[0].split(self.VAR_dat_compraw_strsep)]
                    rawstr = self._fnc_get_list_split_(valueStringLis, self.childRawsize())
                    self._rawObj = self._set_comprawstr_to_rawobj_(rawstr)
                else:
                    self._rawObj = self._set_rawstr_to_rawobj_(rawstr)

    def _get_comprawstr_(self):
        return self.VAR_dat_compraw_strsep.join(
            [i._get_rawstr_() for i in self.children()]
        )

    def _get_rawstr_(self):
        if self._get_is_comp_():
            return self._get_comprawstr_()

        if self._rawObj is not None:
            return unicode(self._rawObj)
        return u''

    # create ********************************************************************************************************* #
    def _set_create_(self, *args):
        if self._get_is_comp_():
            if len(args) > 1:
                self._set_raw_create_(*args)
            else:
                if isinstance(args[0], (str, unicode)):
                    self._set_rawstr_create_(*args)
                else:
                    self._set_raw_create_(*args)
        else:
            if isinstance(args[0], (str, unicode)):
                self._set_rawstr_create_(*args)
            else:
                self._set_raw_create_(*args)

    def __len__(self):
        return self.childrenCount()


class Abs_DatValue(object):
    CLS_dat_datatype = None
    CLS_dat_data = None

    VAR_dat_rawtype_pattern = None
    VAR_dat_rawtype_str_pattern = None
    VAR_dat_rawsize_pattern = None

    def _initAbsDatValue(self, *args):
        self._set_data_build_(*args)

    def _set_data_build_(self, *args):
        self._set_datatype_(self.VAR_dat_rawtype_str_pattern)

        self._set_data_(*args)

    def _set_datatype_(self, *args):
        _ = args[0]
        if isinstance(_, (tuple, list)):
            self._datatypeObj = self.CLS_dat_datatype(_[0])
        else:
            self._datatypeObj = self.CLS_dat_datatype(_)

    def _set_data_(self, *args):
        self._dataObj = self.CLS_dat_data(
            self, *args
        )

    def datatype(self):
        """
        :return: object of Type
        """
        return self._datatypeObj

    def datatypeString(self):
        """
        :return: str
        """
        return self._datatypeObj.toString()

    def data(self):
        """
        :return: object of Data
        """
        return self._dataObj

    def dataString(self):
        return self._dataObj.toString()

    def setRaw(self, *args):
        self._dataObj._set_raw_create_(*args)

    def setRawString(self, *args):
        self._dataObj._set_rawstr_create_(*args)

    def hasRaw(self):
        """
        :return: bool
        """
        return self._dataObj.hasRaw()

    def raw(self):
        """
        :return: raw of typed
        """
        return self._dataObj.raw()

    def rawString(self):
        return self._dataObj.toString()

    def toString(self):
        """
        :return: str
        """
        return self._dataObj.toString()

    def __eq__(self, other):
        """
        :param other: object of Value
        :return: bool
        """
        return self.data() == other.data()

    def __ne__(self, other):
        """
        :param other: object of Value
        :return: bool
        """
        return self.data() != other.data()
