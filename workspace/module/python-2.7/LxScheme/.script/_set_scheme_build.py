# coding:utf-8

if __name__ == '__main__':
    from LxScheme.shmObjects import _shmObjBuilder

    wb = _shmObjBuilder.WindowsResourceBuilder()
    for i in wb.schemes():
        i.createWorkspaceSourceDirectory()
        i.createServerConfigFile()
        op = i.operateAt('0.0.0')
        #
        op.createDevelopSetupJsonFile()
        op.createWorkspaceSetupJsonFile()
        op.pushWorkspaceSourceToDevelop()

    lb = _shmObjBuilder.LinuxResourceBuilder()
    for i in lb.schemes():
        i.createWorkspaceSourceDirectory()
        i.createServerConfigFile()
        op = i.operateAt('0.0.0')
        #
        op.createDevelopSetupJsonFile()
        op.createWorkspaceSetupJsonFile()
        op.pushWorkspaceSourceToDevelop()
