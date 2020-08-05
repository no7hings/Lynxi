# coding:utf-8

if __name__ == '__main__':
    from LxScheme.shmObjects import _shmObjBuilder

    wb = _shmObjBuilder.WindowsResourceBuilder()

    for i in wb.packages():
        i.createServerConfigFile()
        i.createDevelopSourceDirectories()
        #
        op = i.operateAt(i.version.active)

    lb = _shmObjBuilder.LinuxResourceBuilder()

    for i in lb.packages():
        i.createServerConfigFile()
        i.createDevelopSourceDirectories()
        #
        op = i.operateAt(i.version.active)
