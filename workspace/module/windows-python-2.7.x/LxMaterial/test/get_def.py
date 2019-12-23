# coding:utf-8

if __name__ == '__main__':
    from LxCore import lxBasic
    from LxMaterial.materialx import _util
    reload(_util)

    data = _util.loadVariant('C:/_pipe/plug/maya/2019/arnold/3.3.0.1/deploy/materialx/arnold/nodedefs.mtlx').nodeDefDic()

    lxBasic.writeOsJson(data, 'E:/mytest/attrDef.json')

