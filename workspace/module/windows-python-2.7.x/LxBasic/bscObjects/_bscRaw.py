# coding:utf-8
import re


class Str_Prettify(object):
    def __init__(self, string):
        self._string = string
        self._stringLis = [i.lstrip().rstrip() for i in self._string.split(' ')]

    def toCamelcase(self):
        return re.sub(r' (\w)', lambda x: x.group(1).upper(), self._string)

    def toUnderline(self):
        return '_'.join(self._stringLis).lower()


class Str_Camelcase(object):
    def __init__(self, string):
        self._string = string

    def toPrettify(self):
        return ' '.join([i.capitalize() for i in re.findall(r'[a-zA-Z][a-z]*[0-9]*', self._string)])

    def toUnderline(self):
        return re.sub(re.compile(r'([a-z]|\d)([A-Z])'), r'\1_\2', self._string).lower()


class Str_Underline(object):
    def __init__(self, string):
        self._string = string
        self._stringLis = [i.lstrip().rstrip() for i in self._string.split('_')]

    def toPrettify(self):
        return ' '.join([i.capitalize() for i in self._string.split('_')])

    def toCamelcase(self):
        return re.sub(r'_(\w)', lambda x: x.group(1).upper(), self._string)


class Int_Frame(object):
    def __init__(self, integer, fps=24):
        self._integer = integer
        self._fps = fps

    def toTime(self):
        second = int(self._integer) / self._fps
        h = second / 3600
        m = second / 60 - 60 * h
        s = second - 3600 * h - 60 * m
        return h, m, s

    def toTimeString(self):
        h, m, s = self.toTime()
        return '%s:%s:%s' % (str(h).zfill(2), str(m).zfill(2), str(s).zfill(2))


class Lis_Frame(object):
    def __init__(self, lis):
        self._lis = lis

    def toRange(self):
        lis_ = self._lis

        lis = []
        #
        maximum, minimum = max(lis_), min(lis_)
        #
        start, end = None, None
        count = len(lis_)
        index = 0
        #
        lis_.sort()
        for seq in lis_:
            if index > 0:
                pre = lis_[index - 1]
            else:
                pre = None
            #
            if index < (count - 1):
                nex = lis_[index + 1]
            else:
                nex = None
            #
            if pre is None and nex is not None:
                start = minimum
                if seq - nex != -1:
                    lis.append(start)
            elif pre is not None and nex is None:
                end = maximum
                if seq - pre == 1:
                    lis.append((start, end))
                else:
                    lis.append(end)
            elif pre is not None and nex is not None:
                if seq - pre != 1 and seq - nex != -1:
                    lis.append(seq)
                elif seq - pre == 1 and seq - nex != -1:
                    end = seq
                    lis.append((start, end))
                elif seq - pre != 1 and seq - nex == -1:
                    start = seq
            #
            index += 1
        #
        return lis
