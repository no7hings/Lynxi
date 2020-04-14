# coding:utf-8
from LxUi import guiCore
#
from LxUi.qt import qtCore
#
from LxUi.qt.qtObjects import qtObjWidget
#
from LxMaya.method.basic import _maMethodBasic


#
class IfMaNodeTreeItem(qtObjWidget.QtAbcObj_Treeitem):
    ui_qt_method = guiCore.UiMtdBasic
    mtd_app_node = _maMethodBasic.MaNodeMethodBasic
    def __init__(self, *args, **kwargs):
        self._clsSuper = super(qtCore.QWidget, self)
        self._clsSuper.__init__(*args, **kwargs)

        self._initAbcObjTreeitem()
    @property
    def appPath(self):
        return self._appPath
    @property
    def applicationName(self):
        return self._appName
    #
    def load(self, string):
        if self.mtd_app_node.DEF_mya_port_pathsep in string:
            self.loadComp(string)
        else:
            self.loadNode(string)
    #
    def loadNode(self, nodepathString):
        self._appPath = nodepathString
        self._appName = self.mtd_app_node._nodeString2nodename_(nodepathString)
        self._appNamespace = self.mtd_app_node._toNamespaceByNodePath(nodepathString)
        self._appNodeType = self.mtd_app_node._getNodeCategoryString(nodepathString)
        if self._appNodeType == self.mtd_app_node.DEF_mya_type_transform:
            shapePath = self.mtd_app_node._getNodeShapeNodeString(self._appPath)
            if shapePath:
                self._appNodeType = self.mtd_app_node._getNodeCategoryString(shapePath)
        #
        self.setNameText(self._appName)
        self.setNamespace(self._appNamespace)
        self.setIcon(self.ui_qt_method._lxMayaSvgIconKeyword(self._appNodeType))
    #
    def loadComp(self, pathString):
        if self.mtd_app_node.isMeshFaceComp(pathString):
            compIconKeyword = 'svg_basic@svg#face'
        elif self.mtd_app_node.isMeshEdgeComp(pathString):
            compIconKeyword = 'svg_basic@svg#edge'
        elif self.mtd_app_node.isMeshVertexComp(pathString):
            compIconKeyword = 'svg_basic@svg#vertex'
        else:
            compIconKeyword = 'svg_basic@svg#attribute'
        #
        self._appPath = pathString
        self._appName = self.mtd_app_node._toAttrName(pathString)
        self._appNamespace = self.mtd_app_node._toNamespaceByNodePath(self.mtd_app_node._toNodeNameByAttr(pathString))
        #
        self.setNameText(self._appName)
        self.setNamespace(self._appNamespace)
        self.setIcon(compIconKeyword)



