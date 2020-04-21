# coding:utf-8
from LxData.datObjects import _datObjString

from ..import myaBscObjAbs

from ..maBscObjects import _myaBscObjRaw, _myaBscObjQuery


class Connector(myaBscObjAbs.Abs_MyaConnector):
    def __init__(self, *args):
        self._initAbsMyaConnector(*args)


class Parm(myaBscObjAbs.Abs_MyaPort):
    CLS_grh_port_query = _myaBscObjQuery.PortQuery

    CLS_grh_type = _datObjString.Type
    CLS_grh_porttype = _datObjString.Porttype

    CLS_grh_attrpath = _myaBscObjRaw.Attrpath
    CLS_grh_portpath = _myaBscObjRaw.Portpath

    def __init__(self, *args):
        self._initAbsMyaPort(*args)
