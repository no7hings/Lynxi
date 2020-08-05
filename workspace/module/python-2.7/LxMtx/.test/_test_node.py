# coding:utf-8

if __name__ == '__main__':
    from LxMtx import mtxObjects

    n0 = mtxObjects.Node('ramp_rgb', 'node_0')
    print n0

    n1 = mtxObjects.Node('rgb_to_float', 'node_1')

    n0.otport('rgb').connectTo(n1.inport('input'))
