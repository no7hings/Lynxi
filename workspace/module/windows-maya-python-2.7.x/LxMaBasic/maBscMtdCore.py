# coding:utf-8
import re

import collections
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMaya, OpenMayaUI

from LxBasic import bscMethods

from LxMaBasic import maBscConfigure


class Mtd_MaBasic(maBscConfigure.Utility):
    MOD_re = re
    MOD_maya_cmds = cmds
    CLS_ordered_dict = collections.OrderedDict


class Mtd_MaUtility(Mtd_MaBasic):

    @classmethod
    def _getNodeFullpathNameString(cls, nodeString):
        if not nodeString.startswith(cls.DEF_mya_node_separator):
            return cls.MOD_maya_cmds.ls(nodeString, long=1)[0]
        else:
            return nodeString

    @classmethod
    def _toAppExistStringList(cls, nodeString, fullPath=True):
        lis = []
        if isinstance(nodeString, (str, unicode)):
            if cls._isAppExist(nodeString):
                if fullPath is True:
                    lis = [cls._getNodeFullpathNameString(nodeString)]
                else:
                    lis = [bscMethods.MaNodeString.nodenameWithNamespace(nodeString)]
        elif isinstance(nodeString, (tuple, list)):
            for i in nodeString:
                if cls._isAppExist(i):
                    if fullPath is True:
                        lis.append(cls._getNodeFullpathNameString(i))
                    else:
                        lis.append(bscMethods.MaNodeString.nodenameWithNamespace(i))
        return lis

    @staticmethod
    def _setListCleanup(lis):
        lis_ = list(set(lis))
        lis_.sort(key=lis.index)
        return lis_

    @classmethod
    def _isAppExist(cls, nodeString):
        if nodeString is not None:
            return cls.MOD_maya_cmds.objExists(nodeString)
        return False


class Mtd_MaAttribute(Mtd_MaBasic):
    @classmethod
    def _getAttributeQueryNameString(cls, attributeString):
        _ = attributeString.split(cls.DEF_mya_port_separator)[-1]
        if _.endswith(u']'):
            return _.split(u'[')[0]
        return _

    @classmethod
    def _toAttributePortsepSplit(cls, attributeString):
        _ = attributeString.split(cls.DEF_mya_port_separator)
        return _[0], cls.DEF_mya_port_separator.join(_[1:])

    @classmethod
    def _getAttributePorttype(cls, attributeString):
        if isinstance(attributeString, (tuple, list)):
            nodeString, portString = attributeString
        else:
            nodeString, portString = cls._toAttributePortsepSplit(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            attributeType=1
        )

    @classmethod
    def _getAttributeIsAppExist(cls, attributeString):
        if isinstance(attributeString, (tuple, list)):
            attributeString = cls.DEF_mya_port_separator.join(list(attributeString))
        return cls.MOD_maya_cmds.objExists(attributeString)

    @classmethod
    def _getAttributeIsNodeExist(cls, attributeString):
        if isinstance(attributeString, (tuple, list)):
            nodeString, portString = attributeString
        else:
            nodeString, portString = cls._toAttributePortsepSplit(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            exists=1
        )

    @classmethod
    def _getAttributeIsCompound(cls, attributeString):
        if isinstance(attributeString, (tuple, list)):
            nodeString, portString = attributeString
        else:
            nodeString, portString = cls._toAttributePortsepSplit(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            usesMultiBuilder=1
        )

    @classmethod
    def _getAttributeIsMultichannel(cls, attributeString):
        if isinstance(attributeString, (tuple, list)):
            nodeString, portString = attributeString
        else:
            nodeString, portString = cls._toAttributePortsepSplit(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            multi=1
        )

    @classmethod
    def _getAttributeIndexes(cls, attributeString):
        """
        :param attributeString: etc. aiRampFloat1.ramp
        :return:
        """
        if isinstance(attributeString, (tuple, list)):
            attributeString = cls.DEF_mya_port_separator.join(list(attributeString))
        return cls.MOD_maya_cmds.getAttr(attributeString, multiIndices=1) or []

    @classmethod
    def _getAttributeIsMessage(cls, attributeString):
        if isinstance(attributeString, (tuple, list)):
            nodeString, portString = attributeString
        else:
            nodeString, portString = cls._toAttributePortsepSplit(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            message=1
        )

    @classmethod
    def _getAttributeIsColor(cls, attributeString):
        if isinstance(attributeString, (tuple, list)):
            nodeString, portString = attributeString
        else:
            nodeString, portString = cls._toAttributePortsepSplit(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            usedAsColor=1
        )

    @classmethod
    def _getAttributeIsFilename(cls, attributeString):
        if isinstance(attributeString, (tuple, list)):
            nodeString, portString = attributeString
        else:
            nodeString, portString = cls._toAttributePortsepSplit(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            usedAsFilename=1
        )

    @classmethod
    def _getAttributeHasParent(cls, attributeString):
        if isinstance(attributeString, (tuple, list)):
            nodeString, portString = attributeString
        else:
            nodeString, portString = cls._toAttributePortsepSplit(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            listParent=1
        ) is not None

    @classmethod
    def _getAttributeParentPortname(cls, attributeString):
        if isinstance(attributeString, (tuple, list)):
            nodeString, portString = attributeString
        else:
            nodeString, portString = cls._toAttributePortsepSplit(attributeString)
        _ = cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            listParent=1
        )
        if _:
            return _[0]

    @classmethod
    def _getAttributeHasChild(cls, attributeString):
        if isinstance(attributeString, (tuple, list)):
            nodeString, portString = attributeString
        else:
            nodeString, portString = cls._toAttributePortsepSplit(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            numberOfChildren=1
        ) > 0

    @classmethod
    def _getAttributeChildPortnameList(cls, attributeString):
        if isinstance(attributeString, (tuple, list)):
            nodeString, portString = attributeString
        else:
            nodeString, portString = cls._toAttributePortsepSplit(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            listChildren=1
        ) or []

    @classmethod
    def _getAttributeRaw(cls, attributeString):
        exclude_datatype_list = [
            'mesh', 'attributeAlias'
        ]
        if isinstance(attributeString, (tuple, list)):
            attributeString = cls.DEF_mya_port_separator.join(list(attributeString))
        if (
                cls._getAttributeIsMultichannel(attributeString) is False
                and cls._getAttributeIsMessage(attributeString) is False
        ):
            datatype = cls._getAttributeDatatype(attributeString)
            if datatype == 'enum':
                return cls.MOD_maya_cmds.getAttr(attributeString, asString=1)
            elif datatype not in exclude_datatype_list:
                return cls.MOD_maya_cmds.getAttr(attributeString)

    @classmethod
    def _getAttributeDefaultData(cls, attributeString):
        pass

    @classmethod
    def _getAttributeDatatype(cls, attributeString):
        if isinstance(attributeString, (tuple, list)):
            attributeString = cls.DEF_mya_port_separator.join(list(attributeString))
        return cls.MOD_maya_cmds.getAttr(attributeString, type=1)

    @classmethod
    def _getAttributeHasSource(cls, attributeString):
        return cls.MOD_maya_cmds.connectionInfo(attributeString, isExactDestination=1)

    @classmethod
    def _getAttributeIsSource(cls, attributeString):
        return cls.MOD_maya_cmds.connectionInfo(attributeString, isExactSource=1)

    @classmethod
    def _getAttributeSource(cls, attributeString):
        _ = cls.MOD_maya_cmds.listConnections(attributeString, destination=0, source=1, connections=1, plugs=1)
        if _:
            return _[1]

    @classmethod
    def _getAttributeHasTarget(cls, attributeString):
        return cls.MOD_maya_cmds.connectionInfo(attributeString, isExactSource=1)

    @classmethod
    def _getAttributeIsTarget(cls, attributeString):
        return cls.MOD_maya_cmds.connectionInfo(attributeString, isExactDestination=1)

    @classmethod
    def _getAttributeTarget(cls, attributeString):
        _ = cls.MOD_maya_cmds.listConnections(attributeString, destination=1, source=0, connections=1, plugs=1)
        if _:
            return _[1]

    @classmethod
    def _getAttributeNodeString(cls, attributeString):
        return bscMethods.MaAttributeString.nodeString(attributeString)

    @classmethod
    def _getAttributeFullpathPortname(cls, attributeString):
        return bscMethods.MaAttributeString.fullpathPortname(attributeString)

    @classmethod
    def _getAttributePortname(cls, attributeString):
        return bscMethods.MaAttributeString.name(attributeString)


class Mtd_MaFile(Mtd_MaBasic):
    DEF_mya_type_maya_ascii = 'mayaAscii'
    DEF_mya_type_maya_binary = 'mayaBinary'
    AlembicType = 'Alembic'
    #
    FileTypeDic = {
        '.ma': DEF_mya_type_maya_ascii,
        '.mb': DEF_mya_type_maya_binary,
        '.abc': AlembicType
    }
    #
    MaFileExportAllOption = 'exportAll'
    MaFileExportSelectedOption = 'exportSelected'
    #
    MaFileConstructionHistoryOption = 'constructionHistory'
    MaFileShaderOption = 'shader'
    #
    MaFileExportSelectedOptions = [
        MaFileConstructionHistoryOption,
        MaFileShaderOption
    ]
    VAR_file_export_kwarg_dic = dict(
        type='mayaAscii',
        options='v=0',
        force=True,
        defaultExtensions=True,
        exportAll=True,
        preserveReferences=False,
    )
    VAR_file_import_kwarg_dic = dict(
        options='v=0;',
        type='mayaAscii',
        i=True,
        renameAll=True,
        mergeNamespacesOnClash=True,
        namespace=':',
        preserveReferences=True
    )

    @classmethod
    def _getMaFileType(cls, fileString):
        ext = bscMethods.OsFile.ext(fileString)
        return cls.FileTypeDic.get(ext, cls.DEF_mya_type_maya_ascii)

    @classmethod
    def _maFileExportCommand(cls, fileString, optionKwargs=None):
        if optionKwargs is None:
            optionKwargs = cls.VAR_file_export_kwarg_dic.copy()
        #
        optionKwargs['type'] = cls._getMaFileType(fileString)
        #
        cls.MOD_maya_cmds.file(fileString, **optionKwargs)

    @classmethod
    def _maFileImportCommand(cls, fileString, optionKwargs=None):
        if optionKwargs is None:
            optionKwargs = cls.VAR_file_import_kwarg_dic.copy()
        #
        optionKwargs['type'] = cls._getMaFileType(fileString)
        #
        cls.MOD_maya_cmds.file(
            fileString,
            **optionKwargs
        )

    @classmethod
    def _setMaFileImport(cls, fileString, namespace=':'):
        optionKwargs = cls.VAR_file_import_kwarg_dic.copy()
        #
        optionKwargs['type'] = cls._getMaFileType(fileString)
        optionKwargs['namespace'] = namespace
        #
        cls.MOD_maya_cmds.file(
            fileString,
            **optionKwargs
        )
    
    @classmethod
    def _setMaFileImportWithGroup(cls, fileString, groupString, namespace=':'):
        cls.MOD_maya_cmds.file(
            fileString,
            i=1,
            options='v=0;',
            type=cls._getMaFileType(fileString),
            ra=1,
            mergeNamespacesOnClash=1,
            namespace=namespace,
            preserveReferences=1,
            groupReference=True,
            groupString=groupString
        )
        
    @classmethod
    def _setMaAlembicImport(cls, fileString, namespace=':'):
        cls.MOD_maya_cmds.loadPlugin('AbcImport', quiet=1)

        cls.MOD_maya_cmds.file(
            fileString,
            i=1,
            options='v=0;',
            type='Alembic',
            ra=1,
            mergeNamespacesOnClash=1,
            namespace=namespace,
            preserveReferences=1
        )
        #
        if namespace:
            alembicNodeString = namespace + ':' + bscMethods.OsFile.name(fileString) + '_AlembicNode'
        else:
            alembicNodeString = bscMethods.OsFile.name(fileString) + '_AlembicNode'

        if cls.MOD_maya_cmds.objExists(alembicNodeString):
            pass
        else:
            cls.MOD_maya_cmds.createNode(cls.DEF_mya_type_alembic, name=alembicNodeString)
            cls.MOD_maya_cmds.setAttr(alembicNodeString + '.abc_File', fileString, type='string')

    @classmethod
    def _setMaMaterialExport(cls, fileString, shadingEngines, aiAovs):
        cls.MOD_maya_cmds.select(clear=1)
        if shadingEngines:
            cls.MOD_maya_cmds.select(shadingEngines, noExpand=1)
            if aiAovs:
                cls.MOD_maya_cmds.select(aiAovs, add=1)
            cls.MOD_maya_cmds.file(rename=fileString)
            cls.MOD_maya_cmds.file(
                force=1,
                options='v=0',
                type=cls._getMaFileType(fileString),
                preserveReferences=0,
                exportSelected=1
            )
            cls.MOD_maya_cmds.select(clear=1)
        
    @classmethod
    def _setMaFileExportSelected(cls, fileString, objectString, withHistory=False):
        temporaryFile = bscMethods.OsFile.temporaryName(fileString)
        cls.MOD_maya_cmds.select(objectString)
        cls.MOD_maya_cmds.file(
            temporaryFile,
            force=1,
            options='v=0',
            type=cls._getMaFileType(fileString),
            preserveReferences=0,
            exportSelected=1,
            constructionHistory=withHistory
        )
        cls.MOD_maya_cmds.select(clear=1)
        bscMethods.OsFile.copyTo(temporaryFile, fileString)
        
    @classmethod
    def _setMaFileExportSelectedWithSet(cls, fileString, objectString, setString, withHistory=False):
        cls.MOD_maya_cmds.select(clear=1)
        cls.MOD_maya_cmds.select(objectString)

        if isinstance(setString, str):
            if cls.MOD_maya_cmds.objExists(setString):
                cls.MOD_maya_cmds.select(setString, add=1, noExpand=1)
        elif isinstance(setString, list):
            for i in setString:
                if cls.MOD_maya_cmds.objExists(i):
                    cls.MOD_maya_cmds.select(i, add=1, noExpand=1)
        #
        temporaryFile = bscMethods.OsFile.temporaryName(fileString)
        cls.MOD_maya_cmds.file(
            temporaryFile,
            force=1,
            options='v=0',
            type=cls._getMaFileType(fileString),
            preserveReferences=0,
            exportSelected=1,
            constructionHistory=withHistory
        )
        cls.MOD_maya_cmds.select(clear=1)
        bscMethods.OsFile.copyTo(temporaryFile, fileString)

    @classmethod
    def _setMaFileReference(cls, fileString, namespace=':'):
        cls.MOD_maya_cmds.file(
            fileString,
            ignoreVersion=1,
            reference=1,
            mergeNamespacesOnClash=0,
            namespace=namespace,
            options='v=0;p=17;f=0',
            type=cls._getMaFileType(fileString)
        )
    
    @classmethod
    def _setMaCacheReference(cls, fileString, namespace=':'):
        cls.MOD_maya_cmds.file(
            fileString,
            reference=1,
            mergeNamespacesOnClash=1,
            namespace=namespace
        )

    @classmethod
    def _setMaFileOpen(cls, fileString):
        cls.MOD_maya_cmds.file(
            fileString,
            open=1,
            options='v=0',
            force=1,
            type=cls._getMaFileType(fileString)
        )
        
    @classmethod
    def _setMaFileSaveToServer(cls, fileString):
        temporaryFile = bscMethods.OsFile.temporaryName(fileString)
        cls.MOD_maya_cmds.file(rename=temporaryFile)
        cls.MOD_maya_cmds.file(save=1, type=cls._getMaFileType(fileString))
        bscMethods.OsFile.copyTo(temporaryFile, fileString)
        
    @classmethod
    def _setMaFileSaveToLocal(cls, fileString, timetag=None):
        if timetag is None:
            timetag = bscMethods.OsTimetag.active()
        #
        bscMethods.OsFile.createDirectory(fileString)
        fileString = bscMethods.OsFile.toJoinTimetag(fileString, timetag)
        # Main
        cls.MOD_maya_cmds.file(rename=fileString)
        cls.MOD_maya_cmds.file(
            save=1,
            options='v=0;',
            force=1,
            type=cls._getMaFileType(fileString)
        )
    
    @classmethod
    def _setMaFileUpdate(cls, fileString):
        origString = cls.MOD_maya_cmds.file(query=1, sceneName=1)
        cls._setMaFileSaveToServer(fileString)
        cls.MOD_maya_cmds.file(rename=origString)
    
    @classmethod
    def _setMaFileOpenAsTemporary(cls, fileString):
        if bscMethods.OsFile.isExist(fileString):
            temporaryFile = bscMethods.OsFile.temporaryName(fileString)
            bscMethods.OsFile.createDirectory(temporaryFile)

            bscMethods.OsFile.copyTo(fileString, temporaryFile)
            cls._setMaFileOpen(temporaryFile)
        
    @classmethod
    def _setMaFileOpenAsBackup(cls, fileString, backupString, timetag=None):
        if bscMethods.OsFile.isExist(fileString):
            if timetag is None:
                timetag = bscMethods.OsTimetag.active()
            bscMethods.OsFile.createDirectory(backupString)
            localFileJoinUpdateTag = bscMethods.OsFile.toJoinTimetag(backupString, timetag)
            
            bscMethods.OsFile.copyTo(fileString, localFileJoinUpdateTag)
            cls._setMaFileOpen(localFileJoinUpdateTag)
    
    @classmethod
    def _setMaFileNew(cls):
        cls.MOD_maya_cmds.file(new=1, force=1)


class Mtd_MaNode(Mtd_MaUtility):

    @classmethod
    def _getNodeIsGroup(cls, nodeString):
        boolean = False
        # category is "transform" and has no "shape(s)"
        if cls.MOD_maya_cmds.nodeType(nodeString) == cls.DEF_mya_type_transform:
            _ = cls.MOD_maya_cmds.listRelatives(nodeString, children=1, shapes=1, noIntermediate=0, fullPath=1)
            if _ is None:
                boolean = True
        return boolean

    @classmethod
    def _getNodeIsTransform(cls, nodeString):
        boolean = False
        # category is "transform" and has "shape(s)"
        if cls.MOD_maya_cmds.nodeType(nodeString) == cls.DEF_mya_type_transform:
            _ = cls.MOD_maya_cmds.listRelatives(nodeString, children=1, shapes=1, noIntermediate=0, fullPath=1)
            if _ is not None:
                boolean = True
        return boolean

    @classmethod
    def _getNodeIsShape(cls, nodeString):
        boolean = False
        # parent is "transform" and has no "shape(s)"
        if cls.MOD_maya_cmds.nodeType(nodeString) != cls.DEF_mya_type_transform:
            transformPath = cls._getNodeTransformNodeString(nodeString)
            _ = cls._getNodeShapeNodeStringList(nodeString)
            if transformPath and not _:
                boolean = True
        return boolean

    @classmethod
    def _isNodeDag(cls, nodeString):
        return cls.DEF_mya_node_separator in cls._getNodeFullpathNameString(nodeString)

    @classmethod
    def _getNodeUniqueIdString(cls, nodeString):
        if cls._isAppExist(nodeString):
            stringLis = cls.MOD_maya_cmds.ls(nodeString, uuid=1)
            if stringLis:
                return stringLis[0]

    @classmethod
    def _getNodeCategoryString(cls, nodeString):
        return cls.MOD_maya_cmds.nodeType(nodeString)

    @classmethod
    def _getNodeShapeCategoryString(cls, nodeString):
        string = cls._getNodeCategoryString(nodeString)
        if string == cls.DEF_mya_type_transform:
            shapePathString = cls._getNodeShapeNodeString(nodeString)
            if shapePathString:
                string = cls._getNodeCategoryString(shapePathString)
        return string

    @classmethod
    def _getNodeTransformNodeString(cls, nodeString, fullpath=True):
        if cls._isAppExist(nodeString):
            if cls._getNodeCategoryString(nodeString) == cls.DEF_mya_type_transform:
                if fullpath:
                    return cls._getNodeFullpathNameString(nodeString)
                else:
                    return bscMethods.MaNodeString.nodenameWithNamespace(nodeString)
            else:
                stringLis = cls.MOD_maya_cmds.listRelatives(nodeString, parent=1, fullPath=fullpath)
                if stringLis:
                    return stringLis[0]

    @classmethod
    def _getNodeShapeNodeString(cls, nodeString, fullpath=True):
        string = None
        if cls._getNodeCategoryString(nodeString) == cls.DEF_mya_type_transform:
            stringLis = cls.MOD_maya_cmds.listRelatives(nodeString, children=1, shapes=1, noIntermediate=1, fullPath=fullpath)
            if stringLis:
                string = stringLis[0]
        else:
            if fullpath:
                string = cls._getNodeFullpathNameString(nodeString)
            else:
                string = bscMethods.MaNodeString.nodenameWithNamespace(nodeString)
        return string

    @classmethod
    def _getNodeShapeNodeStringList(cls, nodeString, fullpath=True):
        return cls.MOD_maya_cmds.listRelatives(nodeString, children=1, shapes=1, noIntermediate=0, fullPath=fullpath) or []

    @classmethod
    def _getNodeTargetNodeStringList(cls, nodeString, includeCategoryString=None):
        if includeCategoryString is not None:
            return cls.MOD_maya_cmds.listConnections(nodeString, destination=1, source=0, type=includeCategoryString) or []
        return cls.MOD_maya_cmds.listConnections(nodeString, destination=1, source=0) or []

    @classmethod
    def _getNodeSourceNodeStringList(cls, nodeString, includeCategoryString=None):
        if includeCategoryString is not None:
            return cls.MOD_maya_cmds.listConnections(nodeString, destination=0, source=1, type=includeCategoryString) or []
        return cls.MOD_maya_cmds.listConnections(nodeString, destination=0, source=1) or []

    @classmethod
    def _getNodeShadingEngineNodeStringList(cls, nodeString, excludeNodeString=None):
        def branchFnc_(subObjectString):
            shapePathString = cls._getNodeShapeNodeString(subObjectString)
            if not shapePathString:
                shapePathString = subObjectString
            #
            _ = cls._getNodeTargetNodeStringList(shapePathString, cls.DEF_mya_type_shading_engine)
            if _:
                if excludeNodeString is not None:
                    [lis.append(j) for j in _ if not j in lis and not j in excludeNodeString]
                else:
                    [lis.append(j) for j in _ if not j in lis]
        #
        lis = []
        #
        stringLis = cls._toAppExistStringList(nodeString)

        if excludeNodeString is not None:
            excludeNodeString = bscMethods.String.toList(excludeNodeString)

        [branchFnc_(i) for i in stringLis]
        return lis

    @classmethod
    def _getShadingEngineObjectSetDatumList(cls, nodeString):
        """
        :param nodeString: str
        :return: list
        """
        lis = []
        #
        objSetLis = cls.MOD_maya_cmds.sets(nodeString, query=1)
        if objSetLis:
            shaderObjectPathLis = [i for i in cls.MOD_maya_cmds.ls(objSetLis, leaf=1, noIntermediate=1, long=1)]
            for shaderObjectPath in shaderObjectPathLis:
                # Object Group
                showType = cls.MOD_maya_cmds.ls(shaderObjectPath, showType=1)[1]
                if showType == 'float3':
                    shaderObjectPath_ = shaderObjectPath.split('.')[0]
                    shaderObjectUuid = cls._getNodeUniqueIdString(shaderObjectPath_)
                    objSetData = shaderObjectPath, shaderObjectUuid
                    if not objSetData in lis:
                        lis.append(objSetData)
                else:
                    shaderObjectUuid = cls._getNodeUniqueIdString(shaderObjectPath)
                    objSetData = shaderObjectPath, shaderObjectUuid
                    if not objSetData in lis:
                        lis.append(objSetData)
        return lis

    @classmethod
    def _getNodeAllTargetNodeStringList(cls, nodeString, includeCategoryString=None, excludeCategoryString=None, useShapeCategory=False, extend=False):
        def recursionFnc_(nodeString_):
            if extend is True:
                searchNodes = [cls._getNodeTransformNodeString(nodeString_), cls._getNodeShapeNodeString(nodeString_)]
                set(searchNodes)
            else:
                searchNodes = [nodeString_]

            for subNode in searchNodes:
                nodeStrings = cls.MOD_maya_cmds.listConnections(subNode, destination=1, source=0, shapes=1)
                if nodeStrings:
                    for i in nodeStrings:
                        if useShapeCategory is True:
                            nodeTypeString = cls._getNodeShapeCategoryString(i)
                        else:
                            nodeTypeString = cls._getNodeCategoryString(i)

                        if includeCategoryString is not None:
                            if nodeTypeString in includeCategoryString:
                                if not i in lis:
                                    lis.append(i)
                        elif excludeCategoryString is not None:
                            if nodeTypeString not in excludeCategoryString:
                                if not i in lis:
                                    lis.append(i)
                        else:
                            if not i in lis:
                                lis.append(i)
                        #
                        if not i in lis:
                            searchLis.append(i)
                            recursionFnc_(i)

        #
        searchLis = []
        #
        lis = []
        #
        if includeCategoryString is not None:
            includeCategoryString = bscMethods.String.toList(includeCategoryString)
        elif excludeCategoryString is not None:
            excludeCategoryString = bscMethods.String.toList(excludeCategoryString)
        #
        recursionFnc_(nodeString)
        #
        return lis

    @classmethod
    def _getNodeAllSourceNodeStringList(cls, nodeString, includeCategoryString=None, excludeCategoryString=None, useShapeCategory=False, extend=False):
        def addFnc_(nodeString_):
            if not nodeString_ in lis:
                lis.append(nodeString_)

        def recursionFnc_(nodeString_):
            if extend is True:
                searchNodes = [cls._getNodeTransformNodeString(nodeString_), cls._getNodeShapeNodeString(nodeString_)]
                set(searchNodes)
            else:
                searchNodes = [nodeString_]

            for subNode in searchNodes:
                nodeStrings = cls.MOD_maya_cmds.listConnections(subNode, destination=0, source=1, shapes=1)
                if nodeStrings:
                    for i in nodeStrings:
                        if useShapeCategory is True:
                            nodeTypeString = cls._getNodeShapeCategoryString(i)
                        else:
                            nodeTypeString = cls._getNodeCategoryString(i)

                        if includeCategoryString is not None:
                            if nodeTypeString in includeCategoryString:
                                addFnc_(i)
                        elif excludeCategoryString is not None:
                            if nodeTypeString not in excludeCategoryString:
                                addFnc_(i)
                        else:
                            addFnc_(i)
                        #
                        if not i in searchLis:
                            searchLis.append(i)
                            recursionFnc_(i)
        #
        searchLis = []
        #
        lis = []
        #
        if includeCategoryString is not None:
            includeCategoryString = bscMethods.String.toList(includeCategoryString)
        elif excludeCategoryString is not None:
            excludeCategoryString = bscMethods.String.toList(excludeCategoryString)
        #
        recursionFnc_(nodeString)
        #
        return lis

    @classmethod
    def _getNodeAttributeFullpathPortnameList(cls, nodeString):
        return cls.MOD_maya_cmds.listAttr(nodeString, multi=1) or []

    @classmethod
    def _getNodeInputFullpathPortnameList(cls, nodeString):
        _ = cls.MOD_maya_cmds.listAttr(nodeString, read=1, write=1, multi=1)
        if _:
            return [i for i in _ if cls._isAppExist(cls.DEF_mya_port_separator.join([cls._getNodeFullpathNameString(nodeString), i]))]
        return []

    @classmethod
    def _getNodeAttributePortDict(cls, nodeString):
        def recursionFnc_(portString_):
            if Mtd_MaAttribute._getAttributeIsAppExist((nodeString, portString_)):
                indexes_ = Mtd_MaAttribute._getAttributeIndexes((nodeString, portString_))
                children_ = Mtd_MaAttribute._getAttributeChildPortnameList((nodeString, portString_))
                if indexes_ and children_:
                    for index_ in indexes_:
                        for childPortString_ in children_:
                            portString__ = u'{}[{}].{}'.format(portString_, index_, childPortString_)
                            dic.setdefault(portString_, []).append(portString__)
                            recursionFnc_(portString__)
                elif indexes_ or children_:
                    if indexes_:
                        for index_ in indexes_:
                            portString__ = u'{}[{}]'.format(portString_, index_)
                            dic.setdefault(portString_, []).append(portString__)
                            recursionFnc_(portString__)
                    else:
                        for childPortString_ in children_:
                            portString__ = u'{}.{}'.format(portString_, childPortString_)
                            dic.setdefault(portString_, []).append(portString__)
                            recursionFnc_(portString__)
                else:
                    dic[portString_] = portString_

        dic = cls.CLS_ordered_dict()
        _ = cls.MOD_maya_cmds.attributeInfo(nodeString, allAttributes=1)
        if _:
            for k in _:
                hasParent = Mtd_MaAttribute._getAttributeHasParent((nodeString, k))
                if not hasParent:
                    recursionFnc_(k)
        return dic

    @classmethod
    def _getNodeAttributePortDict_(cls, nodeString):
        indexDict = cls._getNodeAttributePortIndexesDict(nodeString)
        pathDict = cls._getNodeAttributePortPathDict(nodeString)
        childDict = cls._getNodeAttributeChildDict(nodeString)

        dic = cls.CLS_ordered_dict()
        for k, v in pathDict.items():
            if k not in childDict:
                portString = ''
                lis = []
                for seq, i in enumerate(v):
                    if i in indexDict:
                        indexes = indexDict[i]
                        if seq > 0:
                            portString += '.' + i + '[{{{}}}]'.format(len(lis))
                        else:
                            portString += i + '[{{{}}}]'.format(len(lis))
                        lis.append(indexes)
                    else:
                        if seq > 0:
                            portString += '.' + i
                        else:
                            portString += i
                if lis:
                    l_ = bscMethods.NestedArray.restructureTo(lis)
                    for f in l_:
                        portString_ = portString.format(*f)
                        if Mtd_MaAttribute._getAttributeIsAppExist((nodeString, portString_)):
                            dic.setdefault(k, []).append(portString_)
                else:
                    if Mtd_MaAttribute._getAttributeIsAppExist((nodeString, portString)):
                        dic[k] = portString
            else:
                dic[k] = childDict[k]
        return dic

    @classmethod
    def _getNodeAttributePortIndexesDict(cls, nodeString):
        def getKeyFnc_(portString_):
            varPattern = re.compile(r'[\[](.*?)[\]]', re.S)
            indexes = re.findall(varPattern, portString_)
            for i in indexes:
                portString_ = portString_.replace(u'[{}]'.format(i), u'')
            return portString_

        def recursionFnc_(portString_):
            if Mtd_MaAttribute._getAttributeIsAppExist((nodeString, portString_)):
                key = getKeyFnc_(portString_)
                indexes_ = Mtd_MaAttribute._getAttributeIndexes((nodeString, portString_))
                children_ = Mtd_MaAttribute._getAttributeChildPortnameList((nodeString, portString_))
                if indexes_:
                    dic[key] = indexes_
                if indexes_ and children_:
                    for index_ in indexes_:
                        for childPortString_ in children_:
                            portString__ = u'{}[{}].{}'.format(portString_, index_, childPortString_)
                            recursionFnc_(portString__)
                elif indexes_ or children_:
                    if indexes_:
                        for index_ in indexes_:
                            for childPortString_ in children_:
                                portString__ = u'{}[{}].{}'.format(portString_, index_, childPortString_)
                                recursionFnc_(portString__)
                        for index_ in indexes_:
                            portString__ = u'{}[{}]'.format(portString_, index_)
                            recursionFnc_(portString__)
                    else:
                        for childPortString_ in children_:
                            portString__ = u'{}.{}'.format(portString_, childPortString_)
                            recursionFnc_(portString__)

        dic = cls.CLS_ordered_dict()
        _ = cls.MOD_maya_cmds.attributeInfo(nodeString, allAttributes=1)
        if _:
            for k in _:
                hasParent = Mtd_MaAttribute._getAttributeHasParent((nodeString, k))
                if not hasParent:
                    recursionFnc_(k)
        return dic

    @classmethod
    def _getNodeAttributePortPathDict(cls, nodeString):
        def getKeyFnc_(portString_):
            varPattern = re.compile(r'[\[](.*?)[\]]', re.S)
            indexes = re.findall(varPattern, portString_)
            for i in indexes:
                portString_ = portString_.replace(u'[{}]'.format(i), u'')
            return portString_

        def recursionFnc_(portString_):
            key = getKeyFnc_(portString_)
            children_ = Mtd_MaAttribute._getAttributeChildPortnameList((nodeString, portString_))
            dic[key] = portString_.split(cls.DEF_mya_port_separator)
            if children_:
                for childPortString_ in children_:
                    portString__ = u'{}.{}'.format(portString_, childPortString_)
                    recursionFnc_(portString__)

        dic = cls.CLS_ordered_dict()
        _ = cls.MOD_maya_cmds.attributeInfo(nodeString, allAttributes=1)
        if _:
            for k in _:
                hasParent = Mtd_MaAttribute._getAttributeHasParent((nodeString, k))
                if not hasParent:
                    recursionFnc_(k)
        return dic

    @classmethod
    def _getNodeAttributeChildDict(cls, nodeString):
        def recursionFnc_(portString_):
            children_ = Mtd_MaAttribute._getAttributeChildPortnameList((nodeString, portString_))
            if children_:
                for childPortString_ in children_:
                    portString__ = u'{}.{}'.format(portString_, childPortString_)
                    dic.setdefault(portString_, []).append(portString__)
                    recursionFnc_(portString__)

        dic = cls.CLS_ordered_dict()
        _ = cls.MOD_maya_cmds.attributeInfo(nodeString, allAttributes=1)
        if _:
            for k in _:
                hasParent = Mtd_MaAttribute._getAttributeHasParent((nodeString, k))
                if not hasParent:
                    recursionFnc_(k)
        return dic

    @classmethod
    def _getNodeOutputFullpathPortnameList(cls, nodeString):
        _ = cls.MOD_maya_cmds.listAttr(nodeString, readOnly=1, multi=1)
        if _:
            return [i for i in _ if cls._isAppExist(cls.DEF_mya_port_separator.join([cls._getNodeFullpathNameString(nodeString), i]))]
        return []


class Mtd_MaNodeGraph(Mtd_MaUtility):
    @classmethod
    def _getNodeGraphNodeStringList(cls, nodeString, includeCategoryString=None, excludeCategoryString=None, useShapeCategory=False, extend=False):
        return Mtd_MaNode._getNodeAllSourceNodeStringList(
            nodeString,
            includeCategoryString,
            excludeCategoryString,
            useShapeCategory,
            extend
        )

    @classmethod
    def _getNodeGraphConnectionDatumList(cls):
        pass


class Mtd_MaDag(Mtd_MaUtility):
    @classmethod
    def _getDagParentString(cls, dagString, fullpath=True):
        _ = cls.MOD_maya_cmds.listRelatives(dagString, parent=1, fullPath=fullpath)
        if _:
            return _[0]

    @classmethod
    def _getDagChildStringList(cls, dagString, fullpath=True):
        return cls.MOD_maya_cmds.listRelatives(dagString, children=1, type=cls.DEF_mya_type_transform, fullPath=fullpath) or []


class Mtd_MaShadingEngine(Mtd_MaUtility):
    pass


class Mtd_MaNodeGroup(Mtd_MaUtility):
    @classmethod
    def _getGroupChildNodeStringList(cls, groupString, includeCategoryString=None, excludeCategoryString=None, useShapeCategory=False, withShape=True):
        def addFnc_(nodeString_):
            if not nodeString_ in lis:
                if withShape is True:
                    lis.append(nodeString_)
                else:
                    if Mtd_MaNode._getNodeIsShape(nodeString_) is False:
                        lis.append(nodeString_)

        def recursionFnc_(nodeString_):
            nodeStrings = cls.MOD_maya_cmds.listRelatives(nodeString_, children=1, fullPath=1)
            if nodeStrings:
                for i in nodeStrings:
                    if useShapeCategory is True:
                        nodeTypeString = Mtd_MaNode._getNodeShapeCategoryString(i)
                    else:
                        nodeTypeString = Mtd_MaNode._getNodeCategoryString(i)

                    if includeCategoryString is not None:
                        if nodeTypeString in includeCategoryString:
                            addFnc_(i)
                    elif excludeCategoryString is not None:
                        if nodeTypeString not in excludeCategoryString:
                            addFnc_(i)
                    else:
                        addFnc_(i)
                    #
                    if not i in searchLis:
                        searchLis.append(i)
                        recursionFnc_(i)
        #
        searchLis = []
        #
        lis = []
        #
        if includeCategoryString is not None:
            includeCategoryString = bscMethods.String.toList(includeCategoryString)
        elif excludeCategoryString is not None:
            excludeCategoryString = bscMethods.String.toList(excludeCategoryString)
        #
        recursionFnc_(groupString)
        #
        return lis


class Mtd_MaPlug(Mtd_MaBasic):
    pass
