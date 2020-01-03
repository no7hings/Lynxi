# coding:utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxCore.method import _osMethod
#
from LxMaya.method.config import _maConfig
#
from LxMaya.method.basic import _maMethodBasic
#
from LxMaya.method import _maMethod


#
class Mtd_MaAbcCache(_maMethodBasic.Mtd_MaPlug):
    FileKey = '-file'
    FrameRangeKey = '-frameRange'
    StepKey = '-step'
    RootKey = '-root'
    AttributeKey = '-attr'
    #
    DataFormatKey = '-dataFormat'
    #
    NoNormalsOption = '-noNormals'
    RenderableOnlyOption = '-ro'
    StripNamespacesOption = '-stripNamespaces'
    UvWriteOption = '-uvWrite'
    WriteFaceSetsOption = '-writeFaceSets'
    WholeFrameGeo = '-wholeFrameGeo'
    WorldSpaceOption = '-worldSpace'
    WriteVisibilityOption = '-writeVisibility'
    EulerFilterOption = '-eulerFilter'
    WriteCreasesOption = '-writeCreases'
    WriteUVSetsOption = '-writeUVSets'
    #
    OptionDic = {
        '-noNormals': False,
        '-ro': False,
        '-stripNamespaces': False,
        '-uvWrite': True,
        '-writeFaceSets': False,
        '-wholeFrameGeo': False,
        '-worldSpace': True,
        '-writeVisibility': True,
        '-eulerFilter': False,
        '-writeCreases': False,
        '-writeUVSets': True,
    }
    #
    OgawaDataFormat = 'ogawa'
    HDF5DataFormat = 'hdf'
    #
    DataFormats = [
        OgawaDataFormat,
        HDF5DataFormat
    ]

    file_method = _maMethod.MaFileMethod

    @classmethod
    def getAbcCacheNodeLis(cls):
        pass
    @classmethod
    def abcCacheExportCommand(cls, exportArgString):
        """
        :param exportArgString: str
        :return: None
        """
        cls.loadAppPlug(cls.MaPlugName_AlembicExport)
        #
        cmds.AbcExport(j=exportArgString)
    @classmethod
    def abcCacheImport(cls, fileString, namespace=None):
        cls.loadAppPlug(cls.MaPlugName_AlembicExport)
        #
        if cls.isOsExistsFile(fileString):
            cls.file_method.setFileImport(fileString, namespace)


#
class MaGpuCacheMethod(_maMethodBasic.Mtd_MaPlug):
    MaDefGpuCacheExportKwargs = dict(
        startTime=0,
        endTime=0,
        dataFormat='ogawa',
        optimizationThreshold=40000,
        optimize=True,
        writeMaterials=True,
    )

    file_method = _osMethod.OsFileMethod
    @classmethod
    def gpuCacheExportCommand(cls, fileString, groupString=None, optionKwargs=None):
        cls.loadAppPlug(cls.MaPlugName_GpuCache)
        #
        if optionKwargs is None:
            optionKwargs = cls.MaDefGpuCacheExportKwargs.copy()
        #
        directory, fileName = cls.file_method.getOsFileDirname(fileString), cls.file_method.getOsFileName(fileString)
        #
        if groupString is None:
            optionKwargs['allDagObjects'] = True
            cmds.gpuCache(
                directory=directory,
                fileName=fileName,
                **optionKwargs
            )
        else:
            cmds.gpuCache(
                groupString,
                directory=directory,
                fileName=fileName,
                **optionKwargs
            )
    @classmethod
    def gpuCacheImport(cls, fileString, namespace=None):
        cls.loadAppPlug(cls.MaPlugName_GpuCache)
        #
        if cls.isOsExist(fileString):
            transformName = cls.file_method.getOsFileName(fileString)
            if namespace is not None:
                pass
            shapeName = transformName + 'Shape'
            cmds.createNode('transform', name=transformName)
            cmds.createNode('gpuCache', name=shapeName, parent=transformName)
            cmds.setAttr(shapeName + '.cacheFileName', fileString, type='string')
            return transformName


#
class MaProxyCacheMethod(_maMethodBasic.Mtd_MaPlug):
    app_method = _maMethodBasic.Mtd_AppMaya
    MaDefArnoldProxyExportKwargs = dict(
        type='ASS Export',
        options='-mask 255;-lightLinks 1;-shadowLinks 1;',
        force=True,
        defaultExtensions=True,
        constructionHistory=True,
        preserveReferences=False,
        exportAll=True
    )

    file_method = _osMethod.OsFileMethod

    @classmethod
    def arnoldProxyExportCommand(cls, fileString, groupString=None, optionKwargs=None):
        cls.loadAppPlug(cls.MaPlugName_Arnold)
        #
        if optionKwargs is None:
            optionKwargs = cls.MaDefArnoldProxyExportKwargs.copy()
        #
        if groupString is not None:
            optionKwargs.pop('exportAll')
            optionKwargs['exportSelected'] = True
            #
            cls.setNodeSelect(groupString)
        #
        cmds.file(
            fileString,
            **optionKwargs
        )
        #
        cls.setSelectClear()


#
class MaYetiObjectMethod(_maMethod.MaHairNodeGraphMethod, _maMethodBasic.Mtd_MaPlug, _maConfig.MaPlugConfig, _maConfig.MaYetiPlugConfig):
    file_method = _osMethod.OsMultFileMethod
    @staticmethod
    def getYetiTextureNodeLis(yetiShape):
        return cmds.pgYetiGraph(yetiShape, listNodes=1, type='texture')
    @staticmethod
    def getYetiTextureParam(yetiShape, yetiTextureNode):
        return cmds.pgYetiGraph(yetiShape, node=yetiTextureNode, param='file_name', getParamValue=1)
    @staticmethod
    def setYetiTextureParam(yetiShape, yetiTextureNode, osImageFile):
        cmds.pgYetiGraph(yetiShape, node=yetiTextureNode, param='file_name', setParamValueString=osImageFile)
    @classmethod
    def getYetiImportNodeLis(cls, yetiShape, importType=None):
        lis = []
        stringLis = cmds.pgYetiGraph(yetiShape, listNodes=1, type='import') or []
        if importType is None:
            lis = stringLis
        else:
            if stringLis:
                for importNode in stringLis:
                    if importType == cls.getYetiImportType(yetiShape, importNode):
                        lis.append(importNode)
        return lis
    @staticmethod
    def getYetiImportShape(yetiShape, importNode):
        return cmds.pgYetiGraph(yetiShape, node=importNode, param='geometry', getParamValue=1)
    @classmethod
    def getYetiImportType(cls, yetiShape, importNode):
        index = cmds.pgYetiGraph(yetiShape, node=importNode, param='type', getParamValue=1)
        return cls.MaYetiImportTypeLis[index]
    @staticmethod
    def setYetiImportParam(yetiShape, importNode, objectShape):
        cmds.pgYetiGraph(yetiShape, node=importNode, param='geometry', setParamValueString=objectShape)
    @classmethod
    def getYetiShapeLis(cls, groupString=None):
        if groupString is None:
            return cls.getNodeLisByType(cls.MaNodeType_Plug_Yeti)
        else:
            return cls.getNodeLisByGroup(groupString, cls.MaNodeType_Plug_Yeti)
    @classmethod
    def getYetiObjectLis(cls, groupString=None):
        if groupString is None:
            return cls.getObjectLisByType(cls.MaNodeType_Plug_Yeti)
        else:
            return cls.getObjectLisByGroup(groupString, cls.MaNodeType_Plug_Yeti)
    @classmethod
    def getYetiGraphData(cls, yetiObject):
        lis = []
        #
        yetiShape = cls.getNodeShape(yetiObject)
        graphNodeLis = cmds.pgYetiGraph(yetiShape, listNodes=1)
        #
        if graphNodeLis:
            for graphNode in graphNodeLis:
                paramDataLis = []
                graphNodeType = cmds.pgYetiGraph(yetiShape, node=graphNode, nodeType=1)
                nodeParams = cmds.pgYetiGraph(yetiShape, node=graphNode, listParams=1)
                for nodeParam in nodeParams:
                    paramType = cmds.pgYetiGraph(yetiShape, node=graphNode, param=nodeParam, paramType=1)
                    paramValue = cmds.pgYetiGraph(yetiShape, node=graphNode, param=nodeParam, getParamValue=1)
                    isParamConstant = cmds.pgYetiGraph(yetiShape, node=graphNode, param=nodeParam, isParamConstant=1)
                    #
                    paramDataLis.append((nodeParam, paramValue, paramType, isParamConstant))
                #
                lis.append((graphNode, graphNodeType, paramDataLis))
        return lis
    @staticmethod
    def getYetiRootNode(yetiObject):
        return cmds.pgYetiGraph(yetiObject, getRootNode=1)
    @staticmethod
    def setYetiRootNode(yetiObject, graphNodeString):
        cmds.pgYetiGraph(yetiObject, setRootNode=graphNodeString)
    @classmethod
    def yetiFurCacheExportCommand(cls, fileString, groupString=None, optionKwargs=None):
        pass


#
class MaYetiGraphObjectMethod(MaYetiObjectMethod):
    set_method = _maMethodBasic.MaSetMethodBasic
    @classmethod
    def getYetiShapeLisByImportShape(cls, importType, importParam):
        if importType == cls.MaYetiImportType_Geometry:
            return cls.getOutputNodeLisFilter(importParam, target='inputGeometry')
        elif importType == cls.MaYetiImportType_Groom:
            return cls.getOutputNodeLisFilter(importParam, target='inputStrandData')
        elif importType == cls.MaYetiImportType_Guide:
            return cls.getOutputNodeLisFilter(importParam, target='guideSets')
    @classmethod
    def getYetiImportParamDic(cls):
        dic = {}
        #
        yetiShapeLis = cls.getYetiShapeLis()
        for yetiShape in yetiShapeLis:
            yetiShapeUniqueId = cls.getNodeUniqueId(yetiShape)
            importNodes = cmds.pgYetiGraph(yetiShape, listNodes=1, type='import')
            for importNode in importNodes:
                importParam = cls.getYetiImportShape(yetiShape, importNode)
                importParamUniqueId = cls.getNodeUniqueId(importParam)
                dic.setdefault(importParamUniqueId, []).append((yetiShapeUniqueId, importNode))
        return dic
    @classmethod
    def getYetiImportDatumLis(cls, yetiObject):
        lis = []
        yetiShape = cls.getNodeShape(yetiObject)
        yetiImportNodeLis = cls.getYetiImportNodeLis(yetiShape)
        if yetiImportNodeLis:
            for importNode in yetiImportNodeLis:
                importParam = cls.getYetiImportShape(yetiShape, importNode)
                importType = cls.getYetiImportType(yetiObject, importNode)
                if importParam != '*':
                    if cls.isAppExist(importParam):
                        lis.append((yetiShape, importNode, importType, importParam))
        return lis
    @classmethod
    def setYetiHairGraphRename(cls, importType, importGuideUniqueId, nameSet):
        if importType == cls.MaYetiImportType_Guide:
            importGuide = cls.getNodeByUniqueId(importGuideUniqueId)
            hairOutputCurveObjectLis = cls.set_method.getNodeLisBySet(importGuide)
            if hairOutputCurveObjectLis:
                for subSeq, hairOutputCurveObject in enumerate(hairOutputCurveObjectLis):
                    newHairOutputCurveObjectName = cls._toLynxiHairOutputCurveObjectName(nameSet, subSeq)
                    newHairLocalCurveObjectName = cls._toLynxiHairLocalCurveObjectName(nameSet, subSeq)
                    cls.setHairCurveRename(hairOutputCurveObject, [newHairOutputCurveObjectName, newHairLocalCurveObjectName])
    @classmethod
    def setYetiHairGraphCollection(cls, yetiObjectUniqueId, importType, importGuideUniqueId, rootGroupPath):
        if importType == cls.MaYetiImportType_Guide:
            yetiObjectPath = cls.getNodeByUniqueId(yetiObjectUniqueId)
            yetiObjectName = cls._toNodeName(yetiObjectPath)
            importGuide = cls.getNodeByUniqueId(importGuideUniqueId)
            #
            hairOutputCurveObjectLis = cls.set_method.getNodeLisBySet(importGuide)
            #
            if hairOutputCurveObjectLis:
                subGuideGroupName = cls.lxGroupName(yetiObjectName)
                compGuideGroupName = cls.lxGroupName(importGuide)
                #
                objectCompGroupPath = cls.Ma_Separator_Node.join(
                    [subGuideGroupName, compGuideGroupName]
                )
                for hairOutputCurveObject in hairOutputCurveObjectLis:
                    cls.setHairCurveCollection(hairOutputCurveObject, rootGroupPath, objectCompGroupPath)
    @classmethod
    def setYetiGraphRename(cls, nameLabel=None, yetiObject=None):
        def setBranch(mainSeq, yetiObjectPath):
            def setImportParmRefresh(importParamUniqueId, importParam):
                if importParamUniqueId in yetiImportParamDic:
                    paramLis = yetiImportParamDic[importParamUniqueId]
                    for yetiShapeUniqueId, importNode in paramLis:
                        yetiShape = cls.getNodeByUniqueId(yetiShapeUniqueId)
                        cls.setYetiImportParam(yetiShape, importNode, importParam)
            #
            def setImportSubBranch(subObjectLis, nameSet):
                if subObjectLis:
                    for subSeq, (yetiShape, importNode, importType, importParam) in enumerate(subObjectLis):
                        countKey = (yetiShape, importType)
                        importCountDic.setdefault(countKey, []).append(subSeq)
                        #
                        objSeq = len(importCountDic[countKey]) - 1
                        if importType in [cls.MaYetiImportType_Geometry, cls.MaYetiImportType_Groom]:
                            importShapeUniqueId = cls.getNodeUniqueId(importParam)
                            importObjectPath = cls.getNodeTransform(importParam)
                            importObjectUniqueId = cls.getNodeUniqueId(importObjectPath)
                            newImportObjectName = cls.lxNodeName(nameSet, importType, objSeq)
                            cls.setObjectRenameByUniqueId(importObjectUniqueId, newImportObjectName)
                            cls.setObjectShapeRenameByUniqueId(importObjectUniqueId)
                            #
                            cls.setNodeOutlinerRgbByUniqueId(importObjectUniqueId, r, g, b, isColorEnable)
                            #
                            importParamUniqueId = importShapeUniqueId
                            newImportParam = cls.getObjectShapeByUniqueId(importObjectUniqueId, fullPath=False)
                            setImportParmRefresh(importParamUniqueId, newImportParam)
                            #
                            cls.setObjectTextureReferenceRenameByUniqueId(importObjectUniqueId)
                        elif importType == cls.MaYetiImportType_Guide:
                            importGuide = importParam
                            importGuideUniqueId = cls.getNodeUniqueId(importGuide)
                            #
                            newImportSetName = cls.lxNodeSetName(nameSet, importType, objSeq)
                            cls.setObjectRenameByUniqueId(importGuideUniqueId, newImportSetName)
                            #
                            importParamUniqueId = importGuideUniqueId
                            newImportParam = newImportSetName
                            setImportParmRefresh(importParamUniqueId, newImportParam)
                            #
                            subNameSet = '_'.join([nameSet, importType, str(objSeq)])
                            cls.setYetiHairGraphRename(importType, importGuideUniqueId, subNameSet)
            #
            nameLabel_ = None
            yetiObjectName = cls._toNodeName(yetiObjectPath)
            if yetiObjectName.startswith(cls.LynxiKeyword_Rename):
                nameLabel_ = yetiObjectName[len(cls.LynxiKeyword_Rename) + 1:]
            else:
                if nameLabel is not None:
                    nameLabel_ = nameLabel + '_' + str(mainSeq + 1)
            #
            if nameLabel_ is not None:
                yetiObjectUniqueId = cls.getNodeUniqueId(yetiObjectPath)
                #
                isColorEnable = cls.lynxi_isNodeColorEnable(yetiObjectPath)
                r, g, b = cls.lynxi_getNodeColor(yetiObjectPath)
                #
                cls.setAttrStringDatumForce_(yetiObjectPath, cls.LynxiAttrName_NodeNameLabel, nameLabel_)
                #
                importDatumLis = cls.getYetiImportDatumLis(yetiObjectPath)
                setImportSubBranch(importDatumLis, nameLabel_)
                #
                newYetiObjectName = cls.lxNodeName(nameLabel_, 'yetiObject')
                cls.setObjectRenameByUniqueId(yetiObjectUniqueId, newYetiObjectName)
                cls.setObjectShapeRenameByUniqueId(yetiObjectUniqueId)
                cls.setNodeOutlinerRgbByUniqueId(yetiObjectUniqueId, r, g, b, isColorEnable)
                #
                newYetiShapePath = cls.getObjectShapeByUniqueId(yetiObjectUniqueId)
                cls.setNodeColorAttr(newYetiShapePath, 'color', r, g, b)
            #
            cls.updateProgress()
        #
        if yetiObject is not None:
            yetiObjectPathLis = cls._toNodeLis(yetiObject)
        else:
            yetiObjectPathLis = cls.getYetiObjectLis()
        #
        if yetiObjectPathLis:
            importCountDic = {}
            yetiImportParamDic = cls.getYetiImportParamDic()
            cls.viewProgress('Rename Yeti Graph', maxValue=len(yetiObjectPathLis))
            [setBranch(s, i) for s, i in enumerate(yetiObjectPathLis)]
    @classmethod
    def setYetiGraphCollection(cls, rootGroupPath, yetiObject=None):
        # noinspection PyUnusedLocal
        def setBranch(mainSeq, yetiObjectPath):
            def setImportSubBranch(subObjectLis):
                if subObjectLis:
                    for subSeq, (yetiShape, importNode, importType, importParam) in enumerate(subObjectLis):
                        if importType in [cls.MaYetiImportType_Geometry, cls.MaYetiImportType_Groom]:
                            importObject = cls.getNodeTransform(importParam)
                            importObjectUniqueId = cls.getNodeUniqueId(importObject)
                            importGroupName = cls.lxGroupName(importType)
                            #
                            importGroupPath = cls.Ma_Separator_Node.join([yetiFurGroupPath, importGroupName])
                            cls.setAppPathCreate(importGroupPath)
                            cls.setObjectParentByUniqueId(importObjectUniqueId, importGroupPath)
                            #
                            refObject = cls.getObjectTextureReferenceByUniqueId(importObjectUniqueId)
                            if refObject:
                                refObjectGroupName = cls.lxGroupName(importType + '_reference')
                                cls.setAppPathCreate(cls.Ma_Separator_Node.join([yetiFurGroupPath, refObjectGroupName]))
                                cls.setObjectParent(refObject, refObjectGroupName)
                        elif importType == cls.MaYetiImportType_Guide:
                            importGuide = importParam
                            importGuideUniqueId = cls.getNodeUniqueId(importGuide)
                            yetiObjectName = cls._toNodeName(yetiObjectPath)
                            #
                            importGuideName = cls.lxSetName(importType)
                            subImportGuideName = cls.lxSetName(yetiObjectName)
                            cls.set_method.setSetPathCreate(cls.Ma_Separator_Set.join([yetiFurSetName, importGuideName, subImportGuideName, importGuide]))
                            #
                            cls.setYetiHairGraphCollection(yetiObjectUniqueId, importType, importGuideUniqueId, rootGroupPath)
            #
            yetiObjectGroupName = cls.lxGroupName('yetiObject')
            yetiObjectUniqueId = cls.getNodeUniqueId(yetiObjectPath)
            #
            yetiObjectGroupPath = cls.Ma_Separator_Node.join([yetiFurGroupPath, yetiObjectGroupName])
            cls.setAppPathCreate(yetiObjectGroupPath)
            #
            importDatumLis = cls.getYetiImportDatumLis(yetiObjectPath)
            setImportSubBranch(importDatumLis)
            #
            cls.lynxi_setNodeAttr(yetiObjectPath)
            cls.setObjectParentByUniqueId(yetiObjectUniqueId, yetiObjectGroupName)
            #
            cls.updateProgress()
        #
        if yetiObject is not None:
            yetiObjectPathLis = cls._toNodeLis(yetiObject)
        else:
            yetiObjectPathLis = cls.getYetiObjectLis()
        #
        if yetiObjectPathLis:
            cls.viewProgress('Collection Yeti Graph', maxValue=len(yetiObjectPathLis))
            #
            furYetiGroupName = cls.lxGroupName(cls.LynxiNameLabel_FurYeti)
            yetiFurGroupPath = cls.Ma_Separator_Node.join([rootGroupPath, furYetiGroupName])
            #
            yetiFurSetName = cls.lxSetName(cls.LynxiNameLabel_FurYeti)
            #
            cls.setAppPathCreate(rootGroupPath)
            [setBranch(s, i) for s, i in enumerate(yetiObjectPathLis)]
            #
            cls.setEmptyGroupClear(rootGroupPath)
    @classmethod
    def setYetiGraphRenameByUniqueId(cls, nameLabel=None, uniqueId=None):
        objectLis = None
        if uniqueId is not None:
            uniqueIdLis = cls._toUniqueIdLis(uniqueId)
            if uniqueIdLis:
                objectLis = cls.getObjectLisByUniqueId(uniqueIdLis)
        #
        cls.setYetiGraphRename(nameLabel, yetiObject=objectLis)
    @classmethod
    def setYetiGraphCollectionByUniqueId(cls, rootGroupPath, uniqueId=None):
        objectLis = None
        if uniqueId is not None:
            uniqueIdLis = cls._toUniqueIdLis(uniqueId)
            if uniqueIdLis:
                objectLis = cls.getObjectLisByUniqueId(uniqueIdLis)
        #
        cls.setYetiGraphCollection(rootGroupPath, yetiObject=objectLis)


#
class MaYetiTextureFileMethod(MaYetiObjectMethod):
    @classmethod
    def getYetiTextureLisByYetiObjectForCollection(cls, yetiObject=None):
        def getBranch(yetiObjectPath):
            yetiShape = cls.getNodeShape(yetiObjectPath)
            mapNodeLis = cls.getYetiTextureNodeLis(yetiShape)
            if mapNodeLis:
                for yetiTextureNode in mapNodeLis:
                    osImageFile = cls.getYetiTextureParam(yetiShape, yetiTextureNode)
                    subMapFileLis = cls.file_method.getOsUdimFileSubFileLis(osImageFile)
                    if subMapFileLis:
                        for subMapFile in subMapFileLis:
                            if not subMapFile in lis:
                                lis.append(subMapFile)
        #
        lis = []
        if yetiObject:
            yetiObjectPathLis = cls._toNodeLis(yetiObject)
        else:
            yetiObjectPathLis = cls.getYetiObjectLis()
        #
        if yetiObjectPathLis:
            [getBranch(i) for i in yetiObjectPathLis]
        return lis
    @classmethod
    def getYetiTextureDatumLis(cls, yetiObject=None):
        """
        :param yetiObject: str or list
        :return: None
        """
        def getBranch(yetiObjectPath):
            yetiShape = cls.getNodeShape(yetiObjectPath)
            furMapNodeLis = cls.getYetiTextureNodeLis(yetiShape)
            if furMapNodeLis:
                for yetiTextureNode in furMapNodeLis:
                    osImageFile = cls.getYetiTextureParam(yetiShape, yetiTextureNode)
                    if osImageFile:
                        lis.append((yetiShape, yetiTextureNode, osImageFile))
        #
        lis = []
        #
        if yetiObject:
            yetiObjectPathLis = cls._toNodeLis(yetiObject)
        else:
            yetiObjectPathLis = cls.getYetiObjectLis()
        #
        if yetiObjectPathLis:
            [getBranch(i) for i in yetiObjectPathLis]
        return lis
    @classmethod
    def setYetiTextureCollection(cls, targetOsPath, yetiObject=None, ignoreMtimeChanged=False, ignoreExists=False, backupExists=False):
        def setBranch(sourceOsFile, targetOsFile):
            cls.updateProgress()
            #
            cls.file_method.setOsFileCopy(sourceOsFile, targetOsFile)
            cls.traceMessage(u'//Result : Copy {} > {}//'.format(sourceOsFile, targetOsFile))
        #
        osFileLis = cls.getYetiTextureLisByYetiObjectForCollection(yetiObject)
        #
        if backupExists is True:
            pass
        #
        osFileCollectionDatumLis = cls.file_method.getOsFileCollectionDatumLis(osFileLis, targetOsPath, ignoreMtimeChanged, ignoreExists)
        if osFileCollectionDatumLis:
            cls.viewProgress(u'Collection Yeti Texture', maxValue=len(osFileCollectionDatumLis))
            [setBranch(i, j) for i, j in osFileCollectionDatumLis]
            cls.traceMessage(u'//Result : Complete Collection//'.format(targetOsPath))
        else:
            cls.traceMessage(u'//Warning : Nothing to Collection//'.format(targetOsPath))
    @classmethod
    def setYetiTextureRepath(cls, targetOsPath, yetiObject=None, ignoreExists=False):
        def getMain(yetiFurMapRepathLis):
            def getBranch(yetiShape, yetiTextureNode, osImageFile):
                cls.updateProgress()
                #
                targetOsImageFile = cls.file_method.getOsTargetFile(osImageFile, targetOsPath)
                #
                enable = False
                if ignoreExists is True:
                    enable = True
                else:
                    if cls.file_method.isOsExistsMultiFile(targetOsImageFile):
                        enable = True
                #
                if enable is True:
                    if not cls.file_method.isOsSameFile(osImageFile, targetOsImageFile):
                        lis.append((yetiShape, yetiTextureNode, targetOsImageFile))
            #
            lis = []
            if yetiFurMapRepathLis:
                cls.viewProgress(u'Repath Yeti Texture', maxValue=len(yetiFurMapRepathLis))
                for i, j, k in yetiFurMapRepathLis:
                    getBranch(i, j, k)
            return lis
        #
        def setMain(yetiFurMapRepathLis):
            def setBranch(yetiShape, yetiTextureNode, targetOsImageFile):
                cls.setYetiTextureParam(yetiShape, yetiTextureNode, targetOsImageFile)
                cls.traceMessage(u'//Result : Repath {} > {}'.format(cls._toNodeName(yetiShape), targetOsImageFile))
            #
            if yetiFurMapRepathLis:
                [setBranch(i, j, k) for i, j, k in yetiFurMapRepathLis]
                #
                cls.traceMessage(u'//Result : Complete Repath//'.format(targetOsPath))
            else:
                cls.traceMessage(u'//Warning : Nothing to Repath//'.format(targetOsPath))
        #
        setMain(getMain(cls.getYetiTextureDatumLis(yetiObject)))
