# coding:utf-8
from LxBasic import bscMethods

from ..import myaBscMtdCore

from ..maBscMethods import _maBscMtdPlug


class File(myaBscMtdCore.Mtd_MaBasic):
    @classmethod
    def exportTo(cls, fileString):
        myaBscMtdCore.Mtd_MaFile._maFileExportCommand(fileString)

    @classmethod
    def exportSelectedTo(cls, fileString, nodepathString, withHistory=False):
        myaBscMtdCore.Mtd_MaFile._setMaFileExportSelected(fileString, nodepathString, withHistory)

    @classmethod
    def exportSelectedWithSetTo(cls, fileString, nodepathString, setString, withHistory=False):
        myaBscMtdCore.Mtd_MaFile._setMaFileExportSelectedWithSet(fileString, nodepathString, setString, withHistory)

    @classmethod
    def importFrom(cls, fileString, namespace=':'):
        myaBscMtdCore.Mtd_MaFile._setMaFileImport(fileString, namespace)

    @classmethod
    def importFromWithGroup(cls, fileString, groupString, namespace=':'):
        myaBscMtdCore.Mtd_MaFile._setMaFileImportWithGroup(fileString, groupString, namespace)

    @classmethod
    def importAlembicFrom(cls, fileString, namespace=':'):
        myaBscMtdCore.Mtd_MaFile._setMaAlembicImport(fileString, namespace)

    @classmethod
    def referenceFrom(cls, fileString, namespace=':'):
        myaBscMtdCore.Mtd_MaFile._setMaFileReference(fileString, namespace)

    @classmethod
    def referenceCacheFrom(cls, fileString, namespace=':'):
        myaBscMtdCore.Mtd_MaFile._setMaCacheReference(fileString, namespace)

    @classmethod
    def openFrom(cls, fileString):
        myaBscMtdCore.Mtd_MaFile._setMaFileOpen(fileString)

    @classmethod
    def openAsTemporary(cls, fileString):
        myaBscMtdCore.Mtd_MaFile._setMaFileOpenAsTemporary(fileString)

    @classmethod
    def openAsBackup(cls, fileString, backupString, timetag=None):
        myaBscMtdCore.Mtd_MaFile._setMaFileOpenAsBackup(fileString, backupString, timetag)

    @classmethod
    def saveToServer(cls, fileString):
        myaBscMtdCore.Mtd_MaFile._setMaFileSaveToServer(fileString)

    @classmethod
    def saveToLocal(cls, fileString, timetag=None):
        myaBscMtdCore.Mtd_MaFile._setMaFileSaveToLocal(fileString, timetag)

    @classmethod
    def updateTo(cls, fileString):
        myaBscMtdCore.Mtd_MaFile._setMaFileUpdate(fileString)

    @classmethod
    def new(cls):
        myaBscMtdCore.Mtd_MaFile._setMaFileNew()


class AlembicCache(myaBscMtdCore.Mtd_MaBasic):
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

    @classmethod
    def getAbcCacheNodeLis(cls):
        pass

    @classmethod
    def abcCacheExportCommand(cls, exportArgString):
        """
        :param exportArgString: str
        :return: None
        """
        _maBscMtdPlug.Plug.load(cls.MaPlugName_AlembicExport)
        #
        cls.MOD_maya_cmds.AbcExport(j=exportArgString)

    @classmethod
    def abcCacheImport(cls, fileString, namespace=None):

        _maBscMtdPlug.Plug.load(cls.MaPlugName_AlembicExport)
        #
        if bscMethods.OsFile.isExist(fileString):
            File.importFrom(fileString, namespace)


class Texture(object):
    @classmethod
    def existFiles(cls, fileString):
        if bscMethods.OsFile.isExist(fileString):
            return [fileString.replace('\\', bscMethods.OsPath.DEF_separator_os)]
        return bscMethods.OsMultifile._getOsMultifileExistFileList(fileString, '<udim>', bscMethods.OsMultifile.VAR_padding_multifile)
