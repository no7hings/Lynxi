# coding=utf-8


#
class basicNodeObject(object):
    def __init__(self):
        self.__initVar()
    #
    def __initVar(self):
        self._enable = True
        #
        self._index = None
        #
        self._type = None
        self._name = None
        self._variant = None
        #
        self._inputAttributeLis = []
        self._outputAttributeLis = []


#
class basicAttributeObject(object):
    def __init__(self):
        self.__initVar()
    #
    def __initVar(self):
        self._enable = True
        #
        self._index = None
        #
        self._type = None
        self._name = None
        self._variant = None
        #
        self._isSource, self._isTarget = True, False
        #
        self._isConnected = False
        self._isMulti = False
        #
        self._childAttributeLis = []
        #
        self._inputAttributeLis = []
        self._outputAttributeLis = []


#
class basicConnectionObject(object):
    def __init__(self):
        self.__initVar()
    #
    def __initVar(self):
        self._enable = True
        #
        self._index = None
        #
        self._type = None
        self._name = None
        self._variant = None
        #
        self._inputAttributeLis = []
        self._outputAttributeLis = []
