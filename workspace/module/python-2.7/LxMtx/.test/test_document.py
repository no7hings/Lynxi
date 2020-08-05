# coding:utf-8

if __name__ == '__main__':
    from LxMtx import mtxObjects

    file0 = mtxObjects.File('e:/test_0.mtlx')

    reference0 = mtxObjects.Reference('e:/test_1.mtlx')
    file0.addReference(reference0)

    file0.addLook('test_look')

    look0 = file0.look('test_look')

    geometry_proxy_0 = mtxObjects.GeometryProxy(mtxObjects.Node(u'mesh', '/group/geometry_0'))
    geometry_proxy_1 = mtxObjects.GeometryProxy(mtxObjects.Node(u'mesh', '/group/geometry_1'))
    geometry_proxy_2 = mtxObjects.GeometryProxy(mtxObjects.Node(u'mesh', '/group/geometry_2'))

    geometry_proxy_0.bindPort(u'shadow').setPortraw(False)
    geometry_proxy_0.bindPort(u'camera').setPortraw(False)
    geometry_proxy_1.bindPort(u'shadow').setPortraw(False)

    geometry_proxy_0.bindPort(u'matte').setPortraw(True)
    geometry_proxy_1.bindPort(u'matte').setPortraw(True)

    look0.addGeometries(geometry_proxy_0, geometry_proxy_1, geometry_proxy_2)

    material0 = mtxObjects.MaterialProxy(mtxObjects.Node(u'material', 'material_0'))

    geometry_proxy_0.connectNodeProxyFrom(material0)
    geometry_proxy_1.connectNodeProxyFrom(material0)
    geometry_proxy_2.connectNodeProxyFrom(material0)

    shader_proxy_0 = mtxObjects.ShaderProxy(mtxObjects.Node(u'matte', 'shader_0'))
    shader_proxy_0.bindInport(u'opacity').setPortraw([1, 0, 1])
    material0.connectSurfaceShaderFrom(shader_proxy_0)

    shader_proxy_1 = mtxObjects.ShaderProxy(mtxObjects.Node(u'matte', 'shader_1'))
    shader_proxy_1.bindInport(u'opacity').setPortraw([1, 0, 1])
    material0.connectDisplacementShaderFrom(shader_proxy_1.bindOtport(u'shader'))

    node0 = mtxObjects.Node(u'utility', 'node_0')
    node1 = mtxObjects.Node(u'utility', 'node_1')
    node0.otport(u'rgb').connectTo(node1.inport(u'color'))
    node0.otport(u'rgb.g').connectTo(node1.inport(u'color.g'))

    node0.otport(u'rgb').connectTo(shader_proxy_0.bindInport(u'color'))
    node0.otport(u'rgb.r').connectTo(shader_proxy_0.bindInport(u'color.r'))
    node1.otport(u'rgb.r').connectTo(shader_proxy_1.bindInport(u'color.r'))

    # print file0
    print geometry_proxy_0.bindObject().asport('materialassign')
