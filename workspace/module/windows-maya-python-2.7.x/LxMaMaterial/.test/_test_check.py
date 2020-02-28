# coding:utf-8
if __name__ == '__main__':
    from LxScheme import shmOutput

    shmOutput.Resource().loadActiveModules()

    from LxBasic import bscMethods

    from LxMaterial import mtlObjects

    from LxMaBasic import maBscObjects

    def_ = mtlObjects.MtlDef()

    maya_category_list = def_.nodeCategories()
    # noinspection PyUnresolvedReferences
    maya_category_list_ = cmds.allNodeTypes()

    dic = {}
    for nodeCategory in maya_category_list:
        mayaNodeCategory = bscMethods.StrUnderline.toCamelcase('ai_' + nodeCategory)
        if mayaNodeCategory in maya_category_list_:
            nodeDef = mtlObjects.MtlNodeDef(nodeCategory)
            attributeRaw = nodeDef.attributeRaw()
            name = '{}1'.format(mayaNodeCategory)
            n = maBscObjects.Node(name)
            dic[nodeCategory] = {}
            for i in attributeRaw:
                portString = i['name']
                mayaPortString = bscMethods.StrUnderline.toCamelcase(portString)
                if not n.hasAttribute(mayaPortString):
                    print name, nodeCategory, portString, mayaNodeCategory, mayaPortString
                    dic[nodeCategory][portString] = None
