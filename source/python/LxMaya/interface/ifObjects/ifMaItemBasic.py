# coding:utf-8
from LxUi import uiCore
#
from LxCore.method.basic import _methodBasic
#
from LxUi.qt.uiBasic import uiWidgetBasic
#
from LxMaya.method.basic import _maMethodBasic


#
class IfMaNodeTreeItem(uiWidgetBasic._UiTreeItemBasic):
    _UiMethod = _methodBasic.LxUiMethodBasic
    _MaNodeMethod = _maMethodBasic.MaNodeMethodBasic
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(uiCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initItemBasic()
        #
        self.setupUi()
    @property
    def appPath(self):
        return self._appPath
    @property
    def appName(self):
        return self._appName
    #
    def load(self, string):
        if self._MaNodeMethod.Ma_Separator_Attribute in string:
            self.loadComp(string)
        else:
            self.loadNode(string)
    #
    def loadNode(self, nodeString):
        self._appPath = nodeString
        self._appName = self._MaNodeMethod._toNodeName(nodeString)
        self._appNamespace = self._MaNodeMethod._toNamespaceByNodePath(nodeString)
        self._appNodeType = self._MaNodeMethod.getNodeType(nodeString)
        if self._appNodeType == self._MaNodeMethod.MaNodeType_Transform:
            shapePath = self._MaNodeMethod.getNodeShape(self._appPath)
            if shapePath:
                self._appNodeType = self._MaNodeMethod.getNodeType(shapePath)
        #
        self.setNameText(self._appName)
        self.setNamespace(self._appNamespace)
        self.setIcon(self._UiMethod._lxMayaSvgIconKeyword(self._appNodeType))
    #
    def loadComp(self, pathString):
        if self._MaNodeMethod.isMeshFaceComp(pathString):
            compIconKeyword = 'svg_basic@svg#face'
        elif self._MaNodeMethod.isMeshEdgeComp(pathString):
            compIconKeyword = 'svg_basic@svg#edge'
        elif self._MaNodeMethod.isMeshVertexComp(pathString):
            compIconKeyword = 'svg_basic@svg#vertex'
        else:
            compIconKeyword = 'svg_basic@svg#attribute'
        #
        self._appPath = pathString
        self._appName = self._MaNodeMethod._toAttrName(pathString)
        self._appNamespace = self._MaNodeMethod._toNamespaceByNodePath(self._MaNodeMethod._toNodeNameByAttr(pathString))
        #
        self.setNameText(self._appName)
        self.setNamespace(self._appNamespace)
        self.setIcon(compIconKeyword)



