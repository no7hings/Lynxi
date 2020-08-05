# coding:utf-8
from LxBasic import bscMethods

from . import grhCfg


class _Mtd_Node(object):
    @classmethod
    def _node_cls__get_ports_exist_(cls, portStackObjList, **kwargs):
        def getArgsFnc_(kwargs_):
            _assignStr = None
            if kwargs_:
                # assign
                if grhCfg.GrhPortQuery.assign in kwargs_:
                    _assignStr = kwargs_[grhCfg.GrhPortQuery.assign]
            return _assignStr

        inportStackObj, otportStackObj, asportStackObj = portStackObjList

        assignStr = getArgsFnc_(kwargs)
        if assignStr is not None:
            if grhCfg.GrhPortAssignQuery.isInport(assignStr):
                return inportStackObj._obj_stack__get_objs_exist_(**kwargs)
            elif grhCfg.GrhPortAssignQuery.isOtport(assignStr):
                return otportStackObj._obj_stack__get_objs_exist_(**kwargs)
            elif grhCfg.GrhPortAssignQuery.isAsport(assignStr):
                return asportStackObj._obj_stack__get_objs_exist_(**kwargs)

            raise TypeError(
                u'''assign "{}" is unregistered'''.format(
                    assignStr
                )
            )
        for portStackObj in portStackObjList:
            if portStackObj._obj_stack__get_objs_exist_(**kwargs) is True:
                return True
        return False

    @classmethod
    def _node_cls__get_port_obj_list_(cls, portStackObjList, **kwargs):
        def getArgsFnc_(kwargs_):
            _assignStr = None
            if kwargs_:
                # assign
                if grhCfg.GrhPortQuery.assign in kwargs_:
                    _assignStr = kwargs_[grhCfg.GrhPortQuery.assign]
            return _assignStr

        inportStackObj, otportStackObj, asportStackObj = portStackObjList

        assignStr = getArgsFnc_(kwargs)
        if assignStr is not None:

            if grhCfg.GrhPortAssignQuery.isInport(assignStr):
                return inportStackObj._obj_stack__get_obj_list_(**kwargs)
            elif grhCfg.GrhPortAssignQuery.isOtport(assignStr):
                return otportStackObj._obj_stack__get_obj_list_(**kwargs)
            elif grhCfg.GrhPortAssignQuery.isAsport(assignStr):
                return asportStackObj._obj_stack__get_obj_list_(**kwargs)

            raise TypeError(
                u'''assign "{}" is unregistered'''.format(
                    assignStr
                )
            )

        return bscMethods.List.cleanupTo(
            inportStackObj._obj_stack__get_obj_list_(**kwargs) +
            otportStackObj._obj_stack__get_obj_list_(**kwargs) +
            asportStackObj._obj_stack__get_obj_list_(**kwargs)
        )

    @classmethod
    def _node_cls__get_port_exist_(cls, portStackObjList, *args, **kwargs):
        def getArgsFnc_(args_, kwargs_):
            _portpathStr, _assignStr = None, None
            if args_:
                if len(args_) == 1:
                    _portpathStr, _assignStr = args_[0], None
                elif len(args_) == 2:
                    _portpathStr, _assignStr = args_
            elif kwargs_:
                # portpath
                if grhCfg.GrhPortQuery.portpath in kwargs_:
                    _portpathStr = kwargs_[grhCfg.GrhPortQuery.portpath]
                # assign
                if grhCfg.GrhPortQuery.assign in kwargs_:
                    _assignStr = kwargs_[grhCfg.GrhPortQuery.assign]
            return _portpathStr, _assignStr

        inportStackObj, otportStackObj, asportStackObj = portStackObjList
        portpathStr, assignStr = getArgsFnc_(args, kwargs)
        if assignStr is not None:
            if grhCfg.GrhPortAssignQuery.isInport(assignStr):
                return inportStackObj._obj_stack__get_obj_exist_(portpathStr)
            elif grhCfg.GrhPortAssignQuery.isOtport(assignStr):
                return otportStackObj._obj_stack__get_obj_exist_(portpathStr)
            elif grhCfg.GrhPortAssignQuery.isAsport(assignStr):
                return asportStackObj._obj_stack__get_obj_exist_(portpathStr)

        for portStackObj in portStackObjList:
            if portStackObj._obj_stack__get_obj_exist_(portpathStr) is True:
                return True
        return False

    @classmethod
    def _node_cls__get_port_obj_(cls, portStackObjList, *args, **kwargs):
        def getArgsFnc_(args_, kwargs_):
            _portpathStr, _assignStr = None, None
            if args_:
                if len(args_) == 1:
                    _portpathStr, _assignStr = args_[0], None
                elif len(args_) == 2:
                    _portpathStr, _assignStr = args_
            elif kwargs_:
                if grhCfg.GrhPortQuery.portpath in kwargs_:
                    _portpathStr = kwargs_[grhCfg.GrhPortQuery.portpath]
                if grhCfg.GrhPortQuery.assign in kwargs_:
                    _assignStr = kwargs_[grhCfg.GrhPortQuery.assign]
            return _portpathStr, _assignStr

        inportStackObj, otportStackObj, asportStackObj = portStackObjList
        portpathStr, assignStr = getArgsFnc_(args, kwargs)
        if assignStr is not None:
            if grhCfg.GrhPortAssignQuery.isInport(assignStr):
                return inportStackObj._obj_stack__get_obj_(portpathStr)
            elif grhCfg.GrhPortAssignQuery.isOtport(assignStr):
                return otportStackObj._obj_stack__get_obj_(portpathStr)
            elif grhCfg.GrhPortAssignQuery.isAsport(assignStr):
                return asportStackObj._obj_stack__get_obj_(portpathStr)

        for portStackObj in portStackObjList:
            if portStackObj._obj_stack__get_obj_exist_(portpathStr):
                return portStackObj._obj_stack__get_obj_(portpathStr)

        raise TypeError(
            u'''portpath "{}" is unregistered'''.format(
                portpathStr
            )
        )
