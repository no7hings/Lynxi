# coding:utf-8

if __name__ == '__main__':
    from LxGraph.grhModel import grhValue

    float0 = grhValue.ValFloat(5.0)
    integer0 = grhValue.ValInteger(5)

    print float0 + integer0
    print integer0 - float0
    print float0 * integer0
    print float0 + float0 / integer0 * integer0

    color3 = grhValue.ValColor3(1.0, 1.0, 1.0)
    print color3

    color3Array = grhValue.ValColor3Array([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])
    print color3Array

    matrix33 = grhValue.ValMatrix33([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])
    print matrix33

