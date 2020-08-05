# coding:utf-8
import copy


def restructureTo(nestedArray):
    def recursionFnc_(index_):
        if index_ < count:
            array = nestedArray[index_]
            for i in array:
                lis_[index_] = i
                recursionFnc_(index_ + 1)
        else:
            lis.append(copy.deepcopy(lis_))

    lis = []
    count = len(nestedArray)
    lis_ = [None] * count
    recursionFnc_(0)
    return lis


a = [[0, 1, 2]]

print restructureTo(a)
