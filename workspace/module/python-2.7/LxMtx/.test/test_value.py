# coding:utf-8

if __name__ == '__main__':
    from LxMtx.mtxObjects import _mtxObjValue

    float0 = _mtxObjValue.Val_Float(5)
    integer0 = _mtxObjValue.Val_Integer(5)

    print float0.data(), integer0.data()
    #
    # print float0 + integer0
    # print integer0 - float0
    # print float0 * integer0
    # print float0 + float0 / integer0 * integer0
    #
    # color3 = _mtlObjValue.Val_Color3(1.0, 1.0, 1.0)
    # print color3

    floatArray0 = _mtxObjValue.Val_FloatArray(1.0, 1.0, 1.0)
    print floatArray0.data()
    #
    color3Array = _mtxObjValue.Val_Color3Array([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])
    print color3Array.data()
    #
    matrix33 = _mtxObjValue.Val_Matrix33([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])
    print matrix33.data()

