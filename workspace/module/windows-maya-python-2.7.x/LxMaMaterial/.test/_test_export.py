# coding:utf-8

if __name__ == '__main__':
    from LxScheme import shmOutput

    shmOutput.Resource().loadActiveModules()

    from LxMaBasic import maBscObjects

    from LxMaterial import mtlObjects

    from LxMaMaterial import maMtlObjects

    r = maBscObjects.GeometryRoot('ast_ID000229_model_grp')

    f = maMtlObjects.File('E:/mytest/2020_0316/ast_ID000229.mtlx')

    look = f.addLook('test')

    look.addDccGeometries(*[i.nodepathString() for i in r.meshes()])

    print f

    f.save()

    print mtlObjects.OBJ_grh_obj_cache.object('ast_ID000229_default_prop_base_file_3')
