# coding:utf-8
from LxData.datObjects import _datObjRaw

from ..import myaBscObjAbs

from ..maBscObjects import _myaBscObjRaw, _myaBscObjQuery


class Connector(myaBscObjAbs.Abs_MyaConnector):
    def __init__(self, *args):
        self._initAbsMyaConnector(*args)


class Parm(myaBscObjAbs.Abs_MyaPort):
    CLS_grh_port_query = _myaBscObjQuery.PortQuery

    CLS_grh_type = _datObjRaw.Type
    CLS_grh_porttype = _datObjRaw.Porttype

    CLS_grh_path = _myaBscObjRaw.Attrpath
    CLS_grh_portpath = _myaBscObjRaw.Portpath

    def __init__(self, *args):
        self._initAbsMyaPort(*args)
