# coding:utf-8

if __name__ == '__main__':
    from LxScheme import shmDefinition

    p = shmDefinition.ResourceDefinition()

    schemes = p.schemes()

    for i in schemes:
        i.createServerCache()
        op = i.operateAt('0.0.0')
        if op.name == 'maya_2019_arnold':
            op.createDevelopSetupFile()

