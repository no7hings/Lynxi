# coding:utf-8

if __name__ == '__main__':
    from LxMaterial import mtlObjects
    document = mtlObjects.XmlDocument('e:/test_1.mtlx')

    reference = mtlObjects.Reference('e:/test_0.mtlx')
    document.addReference(reference)

    look = mtlObjects.Look('test_look')
    document.addLook(look)

    shadersetAssign0 = mtlObjects.ShadersetAssign('shaderset_assign_0')
    look.addAssign(shadersetAssign0)

    shaderset0 = mtlObjects.Shaderset('shaderset_0')
    shadersetAssign0.setShaderset(shaderset0)
    geometry0 = mtlObjects.Geometry('/group/geometry_0')
    geometry1 = mtlObjects.Geometry('/group/geometry_1')
    shadersetAssign0.addGeometries(geometry0, geometry1)
    surfaceShader0 = mtlObjects.Shader(u'matte', 'shader_0')
    shaderset0.connectSurfaceFrom(surfaceShader0.outColor())
    displacementShader0 = mtlObjects.Shader(u'matte', 'shader_1')
    shaderset0.connectDisplacementFrom(displacementShader0.outColor())

    node0 = mtlObjects.Node(u'matte', 'node_0')
    node1 = mtlObjects.Node(u'matte', 'node_1')
    node1.output(u'out_color').connectTo(node0.input(u'color'))
    node0.output(u'out_color').connectTo(surfaceShader0.input(u'color'))
    node1.output(u'out_transparency').connectTo(displacementShader0.input(u'color'))
    # print port0

    nodegraph = mtlObjects.NodeGraph('graph_0')
    nodegraph.addNodes(node0, node1)

    propertysetAssign0 = mtlObjects.PropertysetAssign('propertyset_assign_0')
    look.addAssign(propertysetAssign0)
    propertyset0 = mtlObjects.GeometryPortset('propertyset_0')
    propertysetAssign0.setPropertyset(propertyset0)
    propertysetAssign0.addGeometries(geometry0)

    propertyset0.addPort(geometry0.input(u'disp_autobump'))

    visibilityAssign0 = mtlObjects.VisibilityAssign('visibility_0')
    visibilityAssign0.addGeometries(geometry0)

    print visibilityAssign0

    # print shadersetAssign0

    # print document
