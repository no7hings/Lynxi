# coding:utf-8

if __name__ == '__main__':
    from LxBasic import bscMethods

    from LxMtx import mtxMethods

    data = mtxMethods.File.objectDef(r'C:\Users\dongchangbao\htoa\htoa-4.3.0_r48c4031_houdini-17.5.360\htoa-4.3.0_r48c4031_houdini-17.5.360\scripts\materialx\arnold\nodedefs.mtlx')

    bscMethods.OsJsonFile.write('E:/mytest/nodedefs.json', data)

