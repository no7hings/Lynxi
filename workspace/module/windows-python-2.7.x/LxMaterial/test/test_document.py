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

    shaderset0 = mtlObjects.Shaderset('shaderset_0')
    shadersetAssign0.setShaderset(shaderset0)
    geometry0 = mtlObjects.Geometry('/group/geometry_0')
    geometry1 = mtlObjects.Geometry('/group/geometry_1')
    shadersetAssign0.addGeometries(geometry0, geometry1)
    surfaceShader0 = mtlObjects.Shader(u'matte', 'shader_0')
    shaderset0.connectSurfaceFrom(surfaceShader0.output(u'out_color'))
    displacementShader0 = mtlObjects.Shader(u'matte', 'shader_1')
    shaderset0.connectDisplacementFrom(displacementShader0.output(u'out_color'))

    node0 = mtlObjects.Node(u'matte', 'node_0')
    node1 = mtlObjects.Node(u'matte', 'node_1')
    node1.output(u'out_color').connectTo(node0.input(u'color'))
    node0.output(u'out_color').connectTo(surfaceShader0.input(u'color'))
    node1.output(u'out_transparency').connectTo(displacementShader0.input(u'color'))
    # print port0

    nodegraph = mtlObjects.NodeGraph('graph_0')
    nodegraph.addNodes(node0, node1)

    propertysetAssign0 = mtlObjects.PropertysetAssign()
    look.addAssign(propertysetAssign0)
    propertyset0 = mtlObjects.GeometryPortset('propertyset_0')
    propertysetAssign0.setPropertyset(propertyset0)
    propertysetAssign0.addGeometries(geometry0)

    propertyset0.addPort(geometry0.property(u'disp_autobump'))

    visibilityAssign0 = mtlObjects.VisibilityAssign()
    look.addAssign(visibilityAssign0)
    visibilityAssign0.setTypeString(u'camera')
    visibilityAssign0.addGeometries(geometry0, geometry1)

    collection0 = mtlObjects.Collection('collection_0')
    collection0.addGeometries(geometry0, geometry1)

    collection1 = mtlObjects.Collection('collection_1')
    collection0.addCollection(collection1)
    visibilityAssign0.setCollection(collection0)
    propertysetAssign0.setCollection(collection0)
    # print visibilityAssign0.collection()
    # print collection0

    print document
