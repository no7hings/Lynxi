# coding:utf-8

if __name__ == '__main__':
    from LxScheme import shmBuilder

    p = shmBuilder.Resource()

    modules = p.modules()

    # for i in modules:
    #     i.createServerConfigFile()

    schemes = p.schemes()

    for i in schemes:
        i.createServerConfigFile()
        op = i.operateAt('0.0.0')
        if op.name == 'maya_2019_arnold':
            op.createDevelopSetupFile()

