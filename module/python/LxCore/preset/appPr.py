# coding=utf-8
from LxCore import lxBasic, lxConfigure


#
def getMayaAppPresetVariantDic():
    def getMayaNodeIcons(osPath):
        lis = []
        osFileBasenames = lxBasic.getOsFileBasenameLisByPath(osPath)
        if osFileBasenames:
            for i in osFileBasenames:
                if i.startswith('out_') and i.endswith('.png'):
                    nodeType = i[4:-4]
                    lis.append(nodeType)
        return lis
    #
    mayaIconPath = lxConfigure.IconSubRoot().serverDirectory() + '/' + 'maya'
    dic = {
        'mayaApp':
            {'maIconNodeTypes': tuple(getMayaNodeIcons(mayaIconPath))}
    }
    return dic
