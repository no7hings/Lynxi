# coding:utf-8
if __name__ == '__main__':
    from LxUsd import usdCommands

    from LxUsd import usdObjects

    from LxUsd2mtx import usd2mtxObjects

    s_ = usdCommands.loadScene(r'E:\usd_test\Kitchen_set\geo\Bottle.usd_rop1.usd')

    root = usdObjects.Node('/')

    _file = usd2mtxObjects.File(r'E:\usd_test\BottleB.mtlx')

    _look = _file.addLook('test')

    _look.addSrcGeometries(
        root.allChildren(include='Mesh', asString=True)
    )

    print _file
    # _file.save()
