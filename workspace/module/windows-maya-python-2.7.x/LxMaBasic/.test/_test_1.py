# coding:utf-8
a = {u'ramp': [0L, 1L]}
b = {u'outColor.outColorR': [u'outColor', u'outColorR'], u'outColor.outColorG': [u'outColor', u'outColorG'], u'outTransparency.outTransparencyB': [u'outTransparency', u'outTransparencyB'], u'outTransparency': [u'outTransparency'], u'outTransparency.outTransparencyR': [u'outTransparency', u'outTransparencyR'], u'message': [u'message'], u'ramp.ramp_Interp': [u'ramp', u'ramp_Interp'], u'isHistoricallyInteresting': [u'isHistoricallyInteresting'], u'useImplicitUvs': [u'useImplicitUvs'], u'wrapUvs': [u'wrapUvs'], u'binMembership': [u'binMembership'], u'input': [u'input'], u'type': [u'type'], u'ramp.ramp_Color': [u'ramp', u'ramp_Color'], u'nodeState': [u'nodeState'], u'uvset': [u'uvset'], u'ramp.ramp_Color.ramp_ColorR': [u'ramp', u'ramp_Color', u'ramp_ColorR'], u'ramp.ramp_Color.ramp_ColorG': [u'ramp', u'ramp_Color', u'ramp_ColorG'], u'ramp.ramp_Color.ramp_ColorB': [u'ramp', u'ramp_Color', u'ramp_ColorB'], u'aiUserOptions': [u'aiUserOptions'], u'outTransparency.outTransparencyG': [u'outTransparency', u'outTransparencyG'], u'frozen': [u'frozen'], u'ramp': [u'ramp'], u'outColor': [u'outColor'], u'ramp.ramp_Position': [u'ramp', u'ramp_Position'], u'caching': [u'caching'], u'outColor.outColorB': [u'outColor', u'outColorB']}


def fnc_(nestedArray):
    def recursionFnc_(index):
        if index < count:
            array = nestedArray[index]
            for i in array:
                c[index] = i
                recursionFnc_(index + 1)
        else:
            lis.append(c)

    lis = []
    count = len(nestedArray)
    c = [None]*count
    recursionFnc_(0)
    return lis


dic = {}

for k, v in b.items():
    s = ''
    _ = []
    for seq, i in enumerate(v):
        if i in a:
            indexes = a[i]
            if seq > 0:
                s += '.' + i + '[{{{}}}]'.format(len(_))
            else:
                s += i + '[{{{}}}]'.format(len(_))
            _.append(indexes)
        else:
            if seq > 0:
                s += '.' + i
            else:
                s += i
    if _:
        l_ = fnc_(_)
        for f in l_:
            s_ = s.format(*f)
            dic.setdefault(k, []).append(s_)
    else:
        dic[k] = s

for k, v in dic.items():
    print k, v
