# coding:utf-8

if __name__ == '__main__':
    from LxCore import lxBasic
    from LxMaterial.materialx import _util

    data = _util.loadVariant(r'C:\Users\dongchangbao\htoa\htoa-4.3.0_r48c4031_houdini-17.5.360\htoa-4.3.0_r48c4031_houdini-17.5.360\scripts\materialx\arnold\nodedefs.mtlx').nodeDefs()

    lxBasic.writeOsJson(data, 'E:/mytest/nodedefs.json')

