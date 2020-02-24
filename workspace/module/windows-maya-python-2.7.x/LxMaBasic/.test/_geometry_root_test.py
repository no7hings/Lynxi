# coding:utf-8
# test in maya
if __name__ == '__main__':
    from LxScheme import shmOutput

    shmOutput.Resource().loadActiveModules()

    from LxMaBasic import maBscObjects

    gr = maBscObjects.GeometryRoot('group2')

    print gr.root()

    for g in gr.meshes():
        print g
        for m in g.materials():
            print m
            for s in m.shaders():
                print s
                for a in s.attributes():
                    print a
                    print a.raw()
