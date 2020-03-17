# coding:utf-8

if __name__ == '__main__':
    from LxMaterial import mtlObjects
    file0 = mtlObjects.File('e:/test_0.mtlx')

    reference0 = mtlObjects.Reference('e:/test_1.mtlx')
    file0.addReference(reference0)

    file0.addLook('test_look')

    look0 = file0.look('test_look')

    geometry0 = mtlObjects.Geometry('/group/geometry_0')
    geometry1 = mtlObjects.Geometry('/group/geometry_1')

    geometry0.visibility(u'shadow').setRaw(False)
    geometry0.visibility(u'camera').setRaw(False)
    geometry1.visibility(u'shadow').setRaw(False)

    geometry0.property(u'matte').setRaw(True)
    geometry1.property(u'matte').setRaw(True)

    look0.addGeometries(geometry0, geometry1)

    material0 = mtlObjects.Material('material_0')

    surfaceShader0 = mtlObjects.Shader(u'matte', 'shader_0')
    material0.connectSurfaceFrom(surfaceShader0.output(u'out_color'))
    displacementShader0 = mtlObjects.Shader(u'matte', 'shader_1')
    material0.connectDisplacementFrom(displacementShader0.output(u'out_color'))

    geometry0.addMaterial(material0)
    geometry1.addMaterial(material0)

    node0 = mtlObjects.Node(u'matte', 'node_0')
    node1 = mtlObjects.Node(u'matte', 'node_1')
    node0.output(u'out_color').connectTo(node1.input(u'color'))
    node0.output(u'out_color.g').connectTo(node1.input(u'color.g'))

    node0.output(u'out_color').connectTo(surfaceShader0.input(u'color'))
    node0.output(u'out_color.r').connectTo(surfaceShader0.input(u'color.r'))
    node1.output(u'out_color.r').connectTo(displacementShader0.input(u'color.r'))

    material1 = mtlObjects.Material('material_0')

    # print geometry0
    look0._updateGeometries_()
    # print file0

    command = "self.valueString() if self.node().port('{portname}').isValueChanged() else '0'".format(**geometry0.property(u'matte')._conditionDict_())
    print command
    # print eval(command)

    # print mtlObjects.OBJ_mtl_obj_cache.objectNames()
