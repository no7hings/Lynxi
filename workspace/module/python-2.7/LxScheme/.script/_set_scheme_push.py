# coding:utf-8

if __name__ == '__main__':
    from LxScheme.shmObjects import _shmObjBuilder

    p = _shmObjBuilder.WindowsResourceBuilder()
    for i in p.schemes():
        op = i.operateAt('0.0.0')
        op.pushWorkspaceSourceToDevelop()

    p = _shmObjBuilder.LinuxResourceBuilder()
    for i in p.schemes():
        op = i.operateAt('0.0.0')
        op.pushWorkspaceSourceToDevelop()
