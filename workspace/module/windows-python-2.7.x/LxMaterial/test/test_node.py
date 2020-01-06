# coding:utf-8

if __name__ == '__main__':
    from LxMaterial import mtlObjects

    look = mtlObjects.Elt_Look('test_look')
    material_assign = mtlObjects.Asn_Shaderset('test_assign')
    look.addAssign(material_assign)
    material = mtlObjects.Elt_Material('test_1')
    material_assign.addMaterial(material)
    geometry0 = mtlObjects.Dag_Geometry('test_group/test_geometry_0')
    material_assign.addGeometry(geometry0)
    geometry1 = mtlObjects.Dag_Geometry('test_group/test_geometry_1')
    material_assign.addGeometry(geometry1)
    shader = mtlObjects.Dag_SurfaceShader('layer_shader', 'test_2')
    material.addShader(shader)

    print look
