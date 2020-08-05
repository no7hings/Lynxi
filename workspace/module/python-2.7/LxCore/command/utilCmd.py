# coding:utf-8
import collections

from LxBasic import bscMethods


class helpDocument(object):
    NAME = 'NAME'
    FILE = 'FILE'
    DESCRIPTION = 'DESCRIPTION'
    CLASSES = 'CLASSES'
    FUNCTIONS = 'FUNCTIONS'
    DATA = 'DATA'
    def __init__(self, sourceFileString, targetFileString):
        self._sourceFile = sourceFileString
        self._targetFile = targetFileString

        self.cls_lineLis = []

        self._nameLineLis = []
        self._fileLineLis = []
        self._descriptionLineLis = []
        self._classLineLis = []
        self._functionLineLis = []
        self._dataLis = []

        self._classTocLineLis = []

        self._subClassLineDic = collections.OrderedDict()
        self._subExtendFuncDic = collections.OrderedDict()

        self._sourceLineLis = bscMethods.OsFile.readlines(self._sourceFile)
        if self._sourceLineLis:
            self._collMember()
            bscMethods.OsFile.write(self._targetFile, self.cls_lineLis)

    @staticmethod
    def _comTrans(raw):
        raw = raw.lstrip().rstrip()
        if raw.startswith('#') or raw.startswith('|'):
            raw = raw[1:].lstrip()
        if raw.startswith('*'):
            return '> **' + raw[1:].lstrip().replace('_', '\\_') + '**\r\n'
        else:
            return '> *' + raw.replace('_', '\\_') + '*\r\n'

    @staticmethod
    def _docTrans(raw):
        raw = raw.lstrip().rstrip()
        if raw.startswith('#') or raw.startswith('|'):
            raw = raw[1:].lstrip()
        return '> ' + raw + '\r\n'

    @staticmethod
    def _tocTrans(raw):
        textLis = raw.rstrip().split('    ')
        return '    '.join(textLis[:-1]) + '- ' + textLis[-1].replace('_', '\\_') + '\r\n'

    @staticmethod
    def _clsTrans(raw):
        raw = raw.lstrip().rstrip()
        _clsName = raw.split('(')[0].replace('_', '\\_')[6:]
        _ihtName = raw.split('(')[-1].replace(')', '').replace('_', '\\_')

        return '## ' + '<span style="color:#ff003f;">{}</span>'.format(_clsName) + '<span style="color:#7f7f7f;">({})</span>'.format(_ihtName) + '\r\n'

    @staticmethod
    def _title3Trans(raw):
        raw = raw.lstrip().rstrip()
        if raw.startswith('|'):
            raw = raw[1:].lstrip()
        return '### *' + '<span style="color:#7f7f7f;">{}</span>'.format(raw) + '*\r\n'

    @staticmethod
    def _classMethodTrans(raw):
        raw = raw.lstrip().rstrip().replace('_', '\\_')
        if raw.startswith('|'):
            raw = raw[1:].lstrip()
        return '#### ' + '<span style="color:#ffbf7f;">{}</span>'.format(raw) + '\r\n'

    @staticmethod
    def _classMethodTrans_(raw):
        raw = raw.lstrip().rstrip().replace('_', '\\_')
        if raw.startswith('|'):
            raw = raw[1:].lstrip()
        return '#### ' + raw.split(' = ')[0] + '(...)\r\n*= ' + raw.split(' = ')[-1] + '*\r\n'
    
    @staticmethod
    def _listTrans(raw):
        raw = raw.lstrip().rstrip().replace('_', '\\_')
        if raw.startswith('|'):
            raw = raw[1:].lstrip()
        return '- ' + raw + '\r\n'

    @staticmethod
    def _paramTrans(raw):
        raw = raw.lstrip().rstrip().replace('_', '\\_')
        if raw.startswith('|'):
            raw = raw[1:].lstrip()
        return '- *' + raw.split(':param')[-1].lstrip() + '*\r\n'

    @staticmethod
    def _returnTrans(raw):
        raw = raw.lstrip().rstrip().replace('_', '\\_')
        if raw.startswith('|'):
            raw = raw[1:].lstrip()

        return '- return: ' + '<span style="color:#7f5fff;">{}</span>'.format(raw.split(':return')[-1].lstrip()[1:].lstrip()) + '\r\n'

    @staticmethod
    def _returnTrans_(raw):
        raw = raw.lstrip().rstrip().replace('_', '\\_')
        if raw.startswith('|'):
            raw = raw[1:].lstrip()
        return '*' + raw.split(' -> ')[0] + '*\r\n' + '- return: ' + '<span style="color:#7f5fff;">{}</span>'.format(raw.split(' -> ')[-1].lstrip()) + '\r\n'

    @staticmethod
    def _orderListTrans(seq, raw):
        raw = raw.lstrip().rstrip()
        if raw.startswith('|'):
            raw = raw[1:].lstrip()
        return '{}. '.format(seq) + raw.replace('_', '\\_') + '\r\n'

    @staticmethod
    def _quoteTrans(raw):
        raw = raw.lstrip().rstrip()
        if raw.startswith('|'):
            raw = raw[1:].lstrip()
        return '#### ' + raw.replace('_', '\\_') + '\r\n'

    def _collMember(self):
        a = 'NAME'
        b = 'FILE'
        c = 'DESCRIPTION'
        d = 'CLASSES'
        e = 'FUNCTIONS'
        f = 'DATA'

        isName, isFile, isDescription, isClass, isFunction, isData = [False]*6
        for seq, i in enumerate(self._sourceLineLis):
            if (
                    not i.lstrip() == '' and
                    not i.lstrip().rstrip() == '[' and
                    not i.lstrip().rstrip() == ']' and
                    not i.lstrip().rstrip() == '|'
            ):
                for subSeq, j in enumerate([a, b, c, d, e, f]):
                    if i.rstrip().endswith(j):
                        booleanLis = [False] * 6
                        booleanLis[subSeq] = True
                        isName, isFile, isDescription, isClass, isFunction, isData = booleanLis

                if isName is True:
                    self._nameLineLis.append(i)
                if isFile is True:
                    self._fileLineLis.append(i)
                if isClass is True:
                    self._classLineLis.append(i)
                if isDescription is True:
                    self._descriptionLineLis.append(i)
                if isFunction is True:
                    self._functionLineLis.append(i)
                if isData is True:
                    self._dataLis.append(i)

        self.cls_lineLis.append('# Information\r\n')

        if self._nameLineLis:
            self.cls_lineLis.append('- **Name:**\r\n')
            for i in self._nameLineLis[1:]:
                self.cls_lineLis.append(self._comTrans(i))

        if self._fileLineLis:
            self.cls_lineLis.append('- **File:**\r\n')
            for i in self._fileLineLis[1:]:
                self.cls_lineLis.append(self._comTrans(i))

        if self._descriptionLineLis:
            self.cls_lineLis.append('- **Description:**\r\n')
            for i in self._descriptionLineLis[1:]:
                self.cls_lineLis.append(self._comTrans(i))

        if self._classLineLis:
            self._collClass()

        if self._functionLineLis:
            self.cls_lineLis.append('# Function\r\n')
            self._collFunction(self._functionLineLis[1:])

        if self._dataLis:
            self.cls_lineLis.append('# Data\r\n')
            for i in self._dataLis[1:]:
                self.cls_lineLis.append(self._listTrans(i))

    def _collClass(self):
        isClassToc, isSubClass = True, False

        subClassIndex = 0
        self.cls_lineLis.append('# Classes\r\n')
        for i in self._classLineLis[1:]:
            if i.lstrip().startswith('class'):
                isClassToc, isSubClass = False, True
                subClassIndex += 1

            if isClassToc is True:
                self._classTocLineLis.append(i)
            if isSubClass is True:
                self._subClassLineDic.setdefault(subClassIndex, []).append(i)

        if self._classTocLineLis:
            for i in self._classTocLineLis:
                self.cls_lineLis.append(self._tocTrans(i))

        if self._subClassLineDic:
            for k, v in self._subClassLineDic.items():
                self.cls_lineLis.append(self._clsTrans(v[0]))
                self._collClassBranch(v)

    def _collClassBranch(self, lines):
        functionDic = {}
        docstringLis = []
        resolutionLis = []
        categoryName = lines[0].rstrip()
        if categoryName.endswith('(__builtin__.object)'):
            isDocstring, isFunction = True, False
            subIndex = 0
            for i in lines[1:]:
                if (
                        i.lstrip().startswith('|  Methods defined here:') or
                        i.lstrip().startswith('|  Static methods defined here:') or
                        i.lstrip().startswith('|  Data and other attributes defined here:')
                ):
                    isDocstring, isFunction = False, True
                elif i.lstrip().rstrip() == '|  ----------------------------------------------------------------------':
                    subIndex += 1

                if isDocstring is True:
                    docstringLis.append(i)

                if isFunction is True:
                    functionDic.setdefault(subIndex, []).append(i)
        else:
            isDocstring, isResolution, isFunction = True, False, False
            subIndex = 0
            for i in lines[1:]:
                if i.lstrip().startswith('|  Method resolution order:'):
                    isDocstring, isResolution, isFunction = False, True, False
                elif i.lstrip().startswith('|      __builtin__.object'):
                    isDocstring, isResolution, isFunction = False, False, True
                elif i.lstrip().rstrip() == '|  ----------------------------------------------------------------------':
                    subIndex += 1

                if isDocstring is True:
                    docstringLis.append(i)

                if isResolution is True:
                    resolutionLis.append(i)

                if isFunction is True:
                    functionDic.setdefault(subIndex, []).append(i)

        if docstringLis:
            self.cls_lineLis.append(self._title3Trans('Method description:'))
            for i in docstringLis:
                self.cls_lineLis.append(self._comTrans(i))

        if resolutionLis:
            self.cls_lineLis.append(self._title3Trans('Method resolution order:'))
            orderIndex = 0
            for i in resolutionLis[1:]:
                orderIndex += 1
                self.cls_lineLis.append(self._orderListTrans(orderIndex, i))
            orderIndex += 1
            self.cls_lineLis.append(self._orderListTrans(orderIndex, '__builtin__.object'))

        if functionDic:
            for k, v in functionDic.items():
                if (
                        not v[0].lstrip().rstrip() == '|  ----------------------------------------------------------------------' and
                        not v[0].lstrip().rstrip() == '|      __builtin__.object'
                ):
                    v.insert(0, None)

                self.cls_lineLis.append(self._title3Trans(v[1]))
                self._collClassMethod(v[2:])

    def _collClassMethod(self, lines):
        for i in lines:
            if not i.lstrip().startswith('|      '):
                if ' = ' in i:
                    if i.rstrip().endswith(')'):
                        self.cls_lineLis.append(self._classMethodTrans_(i))
                    else:
                        self.cls_lineLis.append(self._listTrans(i))
                elif i.rstrip().endswith(')'):
                    self.cls_lineLis.append(self._classMethodTrans(i))
                elif i.lstrip()[1:].lstrip().startswith('__') and i.rstrip().endswith('__'):
                    self.cls_lineLis.append(self._classMethodTrans(i))
                else:
                    self.cls_lineLis.append(self._comTrans(i))
            else:
                if ':param' in i:
                    self.cls_lineLis.append(self._paramTrans(i))
                elif ':return' in i:
                    self.cls_lineLis.append(self._returnTrans(i))
                elif ' -> ' in i:
                    self.cls_lineLis.append(self._returnTrans_(i))
                else:
                    self.cls_lineLis.append(self._comTrans(i))

    def _collFunction(self, lines):
        for i in lines:
            if not i.startswith('        '):
                if ' = ' in i:
                    if i.rstrip().endswith(')'):
                        self.cls_lineLis.append(self._classMethodTrans_(i))
                    else:
                        self.cls_lineLis.append(self._listTrans(i))
                elif i.rstrip().endswith(')'):
                    self.cls_lineLis.append(self._classMethodTrans(i))
                elif i.lstrip()[1:].startswith('__') and i.rstrip().endswith('__'):
                    self.cls_lineLis.append(self._classMethodTrans(i))
                else:
                    self.cls_lineLis.append(self._comTrans(i))
            else:
                if ':param' in i:
                    self.cls_lineLis.append(self._paramTrans(i))
                elif ':return' in i:
                    self.cls_lineLis.append(self._returnTrans(i))
                elif ' -> ' in i:
                    self.cls_lineLis.append(self._returnTrans_(i))
                else:
                    self.cls_lineLis.append(self._comTrans(i))


if __name__ == '__main__':
    helpDocument(
        'E:/myworkspace/td/lynxi/doc/pxr/python/pxr.UsdShade',
        'E:/myworkspace/td/lynxi/doc/pxr/python/pxr.UsdShade.md'
    )
