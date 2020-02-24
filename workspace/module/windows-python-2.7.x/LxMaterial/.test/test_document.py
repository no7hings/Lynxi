# coding:utf-8

if __name__ == '__main__':
    from LxMaterial import mtlObjects
    document = mtlObjects.XmlDocument('e:/test_1.mtlx')

    reference = mtlObjects.Reference('e:/test_0.mtlx')
    document.addReference(reference)

    look = mtlObjects.Look('test_look')
    document.addLook(look)

    shadersetAssign0 = mtlObjects.ShadersetAssign()
    look.addAssign(shadersetAssign0)

    geometry0 = mtlObjects.Geometry('/group/geometry_0')
    geometry1 = mtlObjects.Geometry('/group/geometry_1')
    shadersetAssign0.addGeometries(geometry0, geometry1)

    material0 = mtlObjects.Material('material_0')
    shadersetAssign0.setMaterial(material0)

    surfaceShader0 = mtlObjects.Shader(u'matte', 'shader_0')
    material0.connectSurfaceFrom(surfaceShader0.output(u'out_color'))
    displacementShader0 = mtlObjects.Shader(u'matte', 'shader_1')
    material0.connectDisplacementFrom(displacementShader0.output(u'out_color'))

    node0 = mtlObjects.Node(u'matte', 'node_0')
    node1 = mtlObjects.Node(u'matte', 'node_1')
    node1.output(u'out_color').connectTo(node0.attribute(u'color'))
    node0.output(u'out_color').connectTo(surfaceShader0.attribute(u'color'))
    node1.output(u'out_transparency').connectTo(displacementShader0.attribute(u'color'))

    nodegraph = mtlObjects.NodeGraph('graph_0')
    nodegraph.addNodes(node0, node1)

    propertysetAssign0 = mtlObjects.PropertysetAssign()
    look.addAssign(propertysetAssign0)
    propertyset0 = mtlObjects.GeometryPortset('propertyset_0')
    propertysetAssign0.setPropertyset(propertyset0)
    propertysetAssign0.addGeometries(geometry0)

    propertyset0.addAttribute(geometry0.property(u'disp_autobump'))

    visibilityAssign0 = mtlObjects.VisibilityAssign()
    look.addAssign(visibilityAssign0)
    visibilityAssign0.setTypeString(u'camera')
    visibilityAssign0.addGeometries(geometry0, geometry1)

    print document
