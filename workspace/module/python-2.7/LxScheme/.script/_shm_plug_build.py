# coding:utf-8

if __name__ == '__main__':
    from LxScheme.shmObjects import _shmObjBuilder

    wb = _shmObjBuilder.WindowsResourceBuilder()
    for i in wb.plugs():
        i.createServerConfigFile()
        i.createDevelopSourceDirectories()
        op = i.operateAt('0.0.0')

    lb = _shmObjBuilder.LinuxResourceBuilder()
    for i in lb.plugs():
        i.createServerConfigFile()
        i.createDevelopSourceDirectories()
