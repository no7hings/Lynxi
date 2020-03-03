# coding:utf-8
if __name__ == '__main__':
    import os

    import collections

    from LxBasic import bscMethods

    from LxMaterial import mtlConfigure, mtlMethods

    dic = collections.OrderedDict()
    _ = mtlConfigure.Utility.DEF_mtl_maya_2019_def_dict
    lis = []

    nd = mtlMethods.ArnoldNodedefs.raw()

    for i in nd:
        lis.append(i)

    lis.sort()

    for categoryString in lis:
        if categoryString in _:
            v = _[categoryString]
            mayaCategoryString = v[u'categoryString']
            if mayaCategoryString is not None:
                port = nd[categoryString][u'port']
                dic[mayaCategoryString] = collections.OrderedDict()
                dic[mayaCategoryString][u'categoryString'] = categoryString
                dic[mayaCategoryString][u'port'] = collections.OrderedDict()
                for i in port:
                    portString = i[u'portString']
                    datatypeString = i[u'datatypeString']
                    mayaPortString = v[u'port'][portString][u'portString']
                    mayaDatatypeString = v[u'port'][portString][u'datatypeString'][datatypeString]
                    if isinstance(mayaPortString, (str, unicode)):
                        dic[mayaCategoryString][u'port'][mayaPortString] = collections.OrderedDict()
                        dic[mayaCategoryString][u'port'][mayaPortString][u'portString'] = portString
                        dic[mayaCategoryString][u'port'][mayaPortString][u'datatypeString'] = datatypeString
                        print mayaPortString

    bscMethods.OsJsonFile.write('E:/mytest/maya_2019_transfer.json', dic)
    print dic
