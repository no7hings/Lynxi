# coding:utf-8

if __name__ == '__main__':
    from LxBasic import bscMethods

    ls = bscMethods.OsFile.readlines(r'E:\mytest\port_type_raw.txt')
    lis = []
    for i in ls:
        i = i.rstrip()
        if not i.endswith(')'):
            i = i.split(' ')[-1]
        else:
            i = i.split('(')[-2].rstrip().split(' ')[-1]

        if not '"' in i:
            i = "'{}'".format(i)
        if not i in lis:
            lis.append(i)

    for i in lis:
        print i + ','
        # print i + ': ' + i + ','
