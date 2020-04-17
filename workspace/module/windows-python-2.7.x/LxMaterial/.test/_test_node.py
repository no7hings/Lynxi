# coding:utf-8

if __name__ == '__main__':
    from LxMaterial import mtlObjects

    n0 = mtlObjects.Node('ramp_rgb', 'node_0')
    print n0

    n1 = mtlObjects.Node('rgb_to_float', 'node_1')

    # print n0.OBJ_grh_obj_cache.objects()

    n0.otparm('rgb').connectTo(n1.inparm('input'))
