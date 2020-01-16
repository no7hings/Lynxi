# coding:utf-8

if __name__ == '__main__':
    from LxMaterial import mtlObjects
    asset = mtlObjects.XmlDocument('e:/test_1.mtlx')
    reference = mtlObjects.ReferenceElement('e:/test_0.mtlx')
    asset.addReference(reference)
    look = mtlObjects.LookElement('test_look')
    asset.addLook(look)
    shadersetAssign0 = mtlObjects.ShadersetAssign('assign_0')
    look.addAssign(shadersetAssign0)
    shaderset0 = mtlObjects.ShadersetElement('shaderset_0')
    shadersetAssign0.addShaderset(shaderset0)
    geometry0 = mtlObjects.Geometry('/group/geometry_0')
    shadersetAssign0.addGeometry(geometry0)
    geometry1 = mtlObjects.Geometry('/group/geometry_1')
    shadersetAssign0.addGeometry(geometry1)
    surfaceShader0 = mtlObjects.Shader(u'matte', 'shader_0')
    shaderset0.addSurfaceShader(surfaceShader0)
    displacementShader0 = mtlObjects.Shader(u'matte', 'shader_1')
    shaderset0.addDisplacementShader(displacementShader0)

    nodegraph = mtlObjects.NodeGraphElement('graph_0')

    node0 = mtlObjects.Node(u'matte', 'node_0')
    nodegraph.addNode(node0)
    node1 = mtlObjects.Node(u'matte', 'node_1')
    nodegraph.addNode(node1)
    node0.port(u'color').connectTo(node1, 'out_color')

    surfaceShader0.port(u'color').connectTo(nodegraph)
    # print port0
    # print nodegraph

    # print shadersetAssign0
    # print look
    print asset
