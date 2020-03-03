# coding:utf-8
if __name__ == '__main__':
    from LxScheme import shmOutput

    shmOutput.Resource().loadActiveModules()
    # noinspection PyUnresolvedReferences
    from maya import cmds

    from LxBasic import bscMethods

    from LxMaterial import mtlConfigure, mtlMethods, mtlObjects

    from LxMaBasic import maBscObjects

    dic0 = {}

    dic = mtlMethods.MayaArnoldNodedefs.raw()

    for mayaCategoryString, v in dic.items():
        categoryString = v[u'categoryString']
        mayaNodename = categoryString
        if not cmds.objExists(mayaNodename):
            cmds.createNode(mayaCategoryString, name=mayaNodename)

        node = mtlObjects.Node(categoryString, mayaNodename)
        mayaNode = maBscObjects.Node(mayaNodename)
        typeString = node.typeString()
        mayaOutputPortStrings = mayaNode.outputPortStrings()
        if not typeString in dic0:
            dic0[typeString] = mayaOutputPortStrings
            print categoryString, typeString, mayaOutputPortStrings, 'A'
        else:
            _ = dic0[typeString]
            if not _ == mayaOutputPortStrings:
                print categoryString, typeString, mayaOutputPortStrings, 'B'
        port = v[u'port']
        for mayaPortString, iv in port.items():
            portString = iv[u'portString']
            datatypeString = iv[u'datatypeString']

            attribute = node.attribute(portString)
            mayaAttribute = mayaNode.attribute(mayaPortString)
            # print mayaNodename, mayaCategoryString, mayaPortString
            # print mayaAttribute.portdata(), mayaAttribute.porttype(), attribute.value().raw(), datatypeString
            attribute.value().setRaw(mayaAttribute.portdata())
            # print attribute.value()
            # print attribute.defaultValue()

        # print node

    for k, v in dic0.items():
        print k, v

