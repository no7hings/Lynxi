# coding:utf-8

if __name__ == '__main__':
    from LxMaterial import mtlObjects

    file0 = mtlObjects.File('e:/test_0.mtlx')

    reference0 = mtlObjects.Reference('e:/test_1.mtlx')
    file0.addReference(reference0)

    file0.addLook('test_look')

    look0 = file0.look('test_look')

    geometry0 = mtlObjects.GeometryProxy('/group/geometry_0')
    geometry1 = mtlObjects.GeometryProxy('/group/geometry_1')

    geometry0.node().param(u'shadow').setPortdata(False)
    geometry0.node().param(u'camera').setPortdata(False)
    geometry1.node().param(u'shadow').setPortdata(False)

    geometry0.node().param(u'matte').setPortdata(True)
    geometry1.node().param(u'matte').setPortdata(True)

    look0.addGeometries(geometry0, geometry1)

    material0 = mtlObjects.MaterialProxy('material_0')

    shaderRef0 = mtlObjects.ShaderProxy(u'matte', 'shader_0')
    shaderRef0.node().port(u'opacity').setPortdata([1, 0, 1])
    material0.connectSurfaceFrom(shaderRef0.node().output(u'shader'))

    shaderRef1 = mtlObjects.ShaderProxy(u'matte', 'shader_1')
    shaderRef1.node().port(u'opacity').setPortdata([1, 0, 1])
    material0.connectDisplacementFrom(shaderRef1.node().output(u'shader'))

    geometry0.connectMaterial(material0)
    geometry1.connectMaterial(material0)

    node0 = mtlObjects.Node(u'utility', 'node_0')
    node1 = mtlObjects.Node(u'utility', 'node_1')
    node0.output(u'rgb').connectTo(node1.input(u'color'))
    node0.output(u'rgb.g').connectTo(node1.input(u'color.g'))

    node0.output(u'rgb').connectTo(shaderRef0.node().input(u'color'))
    node0.output(u'rgb.r').connectTo(shaderRef0.node().input(u'color.r'))
    node1.output(u'rgb.r').connectTo(shaderRef1.node().input(u'color.r'))

    print file0
