# coding:utf-8
from LxUi import uiCore
#
from LxUi.qt import qtCore
#
from LxUi.qt.qtAbstracts import qtWidgetAbstract
#
from LxMaya.method.basic import _maMethodBasic


#
class IfMaNodeTreeItem(qtWidgetAbstract.Abc_QtTreeviewItem):
    ui_qt_method = uiCore.Basic
    app_node_method = _maMethodBasic.MaNodeMethodBasic
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(qtCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initItemBasic()
        #
        self.setupUi()
    @property
    def appPath(self):
        return self._appPath
    @property
    def applicationName(self):
        return self._appName
    #
    def load(self, string):
        if self.app_node_method.Ma_Separator_Attribute in string:
            self.loadComp(string)
        else:
            self.loadNode(string)
    #
    def loadNode(self, nodeString):
        self._appPath = nodeString
        self._appName = self.app_node_method._toNodeName(nodeString)
        self._appNamespace = self.app_node_method._toNamespaceByNodePath(nodeString)
        self._appNodeType = self.app_node_method.getNodeType(nodeString)
        if self._appNodeType == self.app_node_method.MaNodeType_Transform:
            shapePath = self.app_node_method.getNodeShape(self._appPath)
            if shapePath:
                self._appNodeType = self.app_node_method.getNodeType(shapePath)
        #
        self.setNameText(self._appName)
        self.setNamespace(self._appNamespace)
        self.setIcon(self.ui_qt_method._lxMayaSvgIconKeyword(self._appNodeType))
    #
    def loadComp(self, pathString):
        if self.app_node_method.isMeshFaceComp(pathString):
            compIconKeyword = 'svg_basic@svg#face'
        elif self.app_node_method.isMeshEdgeComp(pathString):
            compIconKeyword = 'svg_basic@svg#edge'
        elif self.app_node_method.isMeshVertexComp(pathString):
            compIconKeyword = 'svg_basic@svg#vertex'
        else:
            compIconKeyword = 'svg_basic@svg#attribute'
        #
        self._appPath = pathString
        self._appName = self.app_node_method._toAttrName(pathString)
        self._appNamespace = self.app_node_method._toNamespaceByNodePath(self.app_node_method._toNodeNameByAttr(pathString))
        #
        self.setNameText(self._appName)
        self.setNamespace(self._appNamespace)
        self.setIcon(compIconKeyword)



