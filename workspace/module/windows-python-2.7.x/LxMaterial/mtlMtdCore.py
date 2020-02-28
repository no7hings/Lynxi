# coding:utf-8
import functools

import collections

import MaterialX

from LxBasic import bscMethods

from LxMaterial import mtlConfigure


class Mtd_MtlBasic(mtlConfigure.Utility):
    MOD_materialx = MaterialX
    MOD_functools = functools
    CLS_ordered_dict = collections.OrderedDict


class Mtd_MtlFile(Mtd_MtlBasic):
    @classmethod
    def _getNodeDefDict(cls, fileString):
        dic = cls.CLS_ordered_dict()
        doc = cls.MOD_materialx.createDocument()
        # noinspection PyArgumentList
        cls.MOD_materialx.readFromXmlFile(doc, fileString)
        #
        for i in doc.getNodeDefs():
            nodeCategory = i.getNodeString()
            nodeType = i.getType()

            nodeDic = collections.OrderedDict()
            nodeDic[cls.DEF_mtl_key_type] = nodeType
            nodeAttrLis = []
            for input_ in i.getInputs():
                portname = input_.getName()
                valueTypeString = input_.getType()
                valueString = input_.getValueString()
                attrDic = collections.OrderedDict()
                attrDic[cls.DEF_mtl_key_port_string] = portname
                attrDic[cls.DEF_mtl_key_type] = valueTypeString
                attrDic[cls.DEF_mtl_key_value] = valueString
                nodeAttrLis.append(attrDic)

            nodeDic[cls.DEF_mtl_key_port] = nodeAttrLis
            dic[nodeCategory] = nodeDic
        return dic


class Mtd_MtlUtility(Mtd_MtlBasic):
    @classmethod
    def _setMethodAdd(cls, fnc):
        # noinspection PyUnusedLocal
        @cls.MOD_functools.wraps(fnc)
        def dummy(self, *args, **kwargs):
            fnc(*args, **kwargs)

        setattr(cls, fnc.func_name, dummy)

    @classmethod
    def _toJsonStringMethod(cls, raw, indent=4):
        def addNoneFnc_(lString, rString):
            lis.append(u'{}null{}'.format(lString, rString))

        def addStringFnc_(raw_, lString, rString):
            lis.append(u'{}"{}"{}'.format(lString, raw_, rString))

        def addUnicodeFnc_(raw_, lString, rString):
            lis.append(u'{}"{}"{}'.format(lString, raw_, rString))

        def addNumberFnc_(raw_, lString, rString):
            lis.append(u'{}{}{}'.format(lString, raw_, rString))

        def addBooleanFnc_(raw_, lString, rString):
            lis.append(u'{}{}{}'.format(lString, str(raw_).lower(), rString))

        def addMemberFnc_(raw_, lString, rString):
            if isinstance(raw_, bool):
                addBooleanFnc_(raw_, lString, rString)

            elif isinstance(raw_, int) or isinstance(raw_, float):
                addNumberFnc_(raw_, lString, rString)

            elif isinstance(raw_, str):
                addStringFnc_(raw_, lString, rString)

            elif isinstance(raw_, unicode):
                addUnicodeFnc_(raw_, lString, rString)

        def addValueFnc_(raw_, lString, rString, rawType=None):
            if raw_ is None:
                addNoneFnc_(lString=lString, rString='\r\n')

            elif isinstance(raw_, list) or isinstance(raw_, tuple):
                lString += defIndentString
                addListFnc_(raw_, lString=lString, rString=rString)

            elif isinstance(raw_, dict):
                lString += defIndentString
                addDictionaryFnc_(raw_, lString=lString, rString=rString)

            else:
                if rawType == dict:
                    addMemberFnc_(raw_, lString='', rString=rString)
                else:
                    addMemberFnc_(raw_, lString=lString+defIndentString, rString=rString)

        def addListFnc_(raw_, lString, rString):
            if raw_:
                lis.append(u'{lString}[{rString}'.format(lString='', rString='\r\n'))

                c = len(raw_)
                for seq, i in enumerate(raw_):
                    if seq < c - 1:
                        addValueFnc_(i, lString=lString, rString=',\r\n', rawType=list)
                    else:
                        addValueFnc_(i, lString=lString, rString='\r\n', rawType=list)

                lis.append(u'{lString}]{rString}'.format(lString=lString, rString=rString))

            else:
                lis.append(u'{lString}[]{rString}\r\n'.format(lString=lString, rString=rString))

        def addDictionaryFnc_(raw_, lString, rString):
            if raw_:
                lis.append(u'{lString}{{{rString}'.format(lString='', rString='\r\n'))

                c = len(raw_)
                for seq, (k, v) in enumerate(raw_.items()):
                    addMemberFnc_(k, lString=lString + defIndentString, rString=': ')

                    if seq < c - 1:
                        addValueFnc_(v, lString=lString, rString=',\r\n', rawType=dict)
                    else:
                        addValueFnc_(v, lString=lString, rString='\r\n', rawType=dict)

                lis.append(u'{lString}}}{rString}'.format(lString=lString, rString=rString))

            else:
                lis.append(u'{lString}{{}}{rString}'.format(lString='', rString=rString))

        def addRawFnc_(raw_):
            if raw_ is None:
                addNoneFnc_(lString='', rString='\r\n')

            elif isinstance(raw_, list) or isinstance(raw_, tuple):
                addListFnc_(raw_, lString='', rString='\r\n')

            elif isinstance(raw_, dict):
                addDictionaryFnc_(raw_, lString='', rString='\r\n')

        defIndentString = ' ' * indent

        lis = [
            u'{} = '.format(cls.__name__)
        ]

        addRawFnc_(raw)

        return ''.join(lis)


class Mtd_MtlRaw(Mtd_MtlBasic):

    @classmethod
    def _setMayaAttributeCovert(cls, string):
        return bscMethods.StrCamelcase.toUnderline(string[2:])

