# coding=utf-8
from LxBasic import bscMethods

from LxScheme import shmOutput


#
def getMayaAppPresetVariantDic():
    def getMayaNodeIcons(osPath):
        lis = []
        osFileBasenames = bscMethods.OsDirectory.fileBasenames(osPath)
        if osFileBasenames:
            for i in osFileBasenames:
                if i.startswith('out_') and i.endswith('.png'):
                    nodeType = i[4:-4]
                    lis.append(nodeType)
        return lis
    #
    mayaIconPath = shmOutput.Directory().icon.server + '/' + 'maya'
    dic = {
        'mayaApp':
            {'maIconNodeTypes': tuple(getMayaNodeIcons(mayaIconPath))}
    }
    return dic
