# coding:utf-8

if __name__ == '__main__':
    from LxMaterial import mtlObjects

    look = mtlObjects.Elt_Look('test_1')
    material = mtlObjects.Elt_Shaderset('test_1')
    shader = mtlObjects.Dag_SurfaceShader('matrix_multiply_vector', 'test_2')
    material.addShader(shader)
    print material
