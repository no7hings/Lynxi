# coding:utf-8

if __name__ == '__main__':
    import collections

    from LxScheme import shmOutput

    shmOutput.Resource().loadActiveModules()

    from LxBasic import bscMethods

    from LxMaterial import mtlMethods, mtlObjects

    from LxMaBasic import maBscObjects

    dic = collections.OrderedDict()

    categories = mtlMethods.ArnoldNodedefs.categoryRaw()
    # noinspection PyUnresolvedReferences
    mayaNodeCategories = cmds.allNodeTypes()
    for category in categories:
        mayaCategory = bscMethods.StrUnderline.toCamelcase('ai_' + category)
        dic[category] = collections.OrderedDict()
        dic[category][u'categoryString'] = None
        dic[category][u'port'] = collections.OrderedDict()
        nodeDef = mtlObjects.MtlNodeDef(category)
        inputRaw = nodeDef.inputRaw()
        if mayaCategory in mayaNodeCategories:
            dic[category][u'categoryString'] = mayaCategory
            nodeName = '{}1'.format(mayaCategory)
            mayaNode = maBscObjects.Node(nodeName)
            for i in inputRaw:
                portString = i[u'portString']
                datatypeString = i[u'datatypeString']
                dic[category][u'port'][portString] = collections.OrderedDict()
                dic[category][u'port'][portString][u'portString'] = None
                dic[category][u'port'][portString][u'datatypeString'] = collections.OrderedDict()
                dic[category][u'port'][portString][u'datatypeString'][datatypeString] = None
                mayaPortString = bscMethods.StrUnderline.toCamelcase(portString)
                if mayaNode.hasAttribute(mayaPortString):
                    dic[category][u'port'][portString][u'portString'] = mayaPortString
                    mayaPorttypeString = mayaNode.attribute(mayaPortString).porttype()
                    dic[category][u'port'][portString][u'datatypeString'][datatypeString] = mayaPorttypeString
        else:
            for i in inputRaw:
                portString = i[u'portString']
                datatypeString = i[u'datatypeString']
                dic[category][u'port'][portString] = collections.OrderedDict()
                dic[category][u'port'][portString][u'portString'] = None
                dic[category][u'port'][portString][u'datatypeString'] = collections.OrderedDict()
                dic[category][u'port'][portString][u'datatypeString'][datatypeString] = None

    bscMethods.OsJsonFile.write('E:/mytest/maya_transfer.json', dic)
    print dic
