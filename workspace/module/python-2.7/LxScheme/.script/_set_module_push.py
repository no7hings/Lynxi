# coding:utf-8

if __name__ == '__main__':
    import os
    from LxScheme.shmObjects import _shmObjBuilder

    p = _shmObjBuilder.WindowsResourceBuilder()

    for i in p.modules():
        op = i.operateAt('0.0.0')
        op.pushWorkspaceSourceToDevelop()
