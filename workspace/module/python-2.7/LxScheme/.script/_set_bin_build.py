# coding:utf-8

if __name__ == '__main__':
    from LxScheme.shmObjects import _shmObjBuilder

    p = _shmObjBuilder.WindowsResourceBuilder()

    for i in p.bins():
        i.createServerConfigFile()
        i.createDevelopSourceDirectories()

    p = _shmObjBuilder.LinuxResourceBuilder()

    for i in p.bins():
        i.createServerConfigFile()
        i.createDevelopSourceDirectories()
