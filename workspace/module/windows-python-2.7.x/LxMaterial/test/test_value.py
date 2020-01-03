# coding:utf-8

if __name__ == '__main__':
    from LxMaterial.mtlObjects import _mtlValue

    float0 = _mtlValue.Val_Float(5.0)
    integer0 = _mtlValue.Val_Integer(5)

    print float0, integer0

    print float0 + integer0
    print integer0 - float0
    print float0 * integer0
    print float0 + float0 / integer0 * integer0

    color3 = _mtlValue.Val_Color3(1.0, 1.0, 1.0)
    print color3

    color3Array = _mtlValue.Val_Color3Array([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])
    print color3Array

    matrix33 = _mtlValue.Val_Matrix33([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])
    print matrix33
