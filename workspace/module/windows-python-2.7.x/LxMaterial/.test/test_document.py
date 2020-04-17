# coding:utf-8

if __name__ == '__main__':
    from LxMaterial import mtlObjects

    file0 = mtlObjects.File('e:/test_0.mtlx')

    reference0 = mtlObjects.Reference('e:/test_1.mtlx')
    file0.addReference(reference0)

    file0.addLook('test_look')

    look0 = file0.look('test_look')

    geometry0 = mtlObjects.GeometryProxy(u'mesh', '/group/geometry_0')
    geometry1 = mtlObjects.GeometryProxy(u'mesh', '/group/geometry_1')

    geometry0.node().param(u'shadow').setPortraw(False)
    geometry0.node().param(u'camera').setPortraw(False)
    geometry1.node().param(u'shadow').setPortraw(False)

    geometry0.node().param(u'matte').setPortraw(True)
    geometry1.node().param(u'matte').setPortraw(True)

    look0.addGeometries(geometry0, geometry1)

    material0 = mtlObjects.MaterialProxy(u'material', 'material_0')

    shaderRef0 = mtlObjects.ShaderProxy(u'matte', 'shader_0')
    shaderRef0.node().port(u'opacity').setPortraw([1, 0, 1])
    material0.connectSurfaceFrom(shaderRef0.node().otparm(u'shader'))

    shaderRef1 = mtlObjects.ShaderProxy(u'matte', 'shader_1')
    shaderRef1.node().port(u'opacity').setPortraw([1, 0, 1])
    material0.connectDisplacementFrom(shaderRef1.node().otparm(u'shader'))

    geometry0.connectMaterial(material0)
    geometry1.connectMaterial(material0)

    node0 = mtlObjects.Node(u'utility', 'node_0')
    node1 = mtlObjects.Node(u'utility', 'node_1')
    node0.otparm(u'rgb').connectTo(node1.inparm(u'color'))
    node0.otparm(u'rgb.g').connectTo(node1.inparm(u'color.g'))

    node0.otparm(u'rgb').connectTo(shaderRef0.node().inparm(u'color'))
    node0.otparm(u'rgb.r').connectTo(shaderRef0.node().inparm(u'color.r'))
    node1.otparm(u'rgb.r').connectTo(shaderRef1.node().inparm(u'color.r'))

    print file0
