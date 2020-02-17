# coding:utf-8
from LxBasic import bscMethods

from LxMaBasic import maBscCore


class AppFile(maBscCore.UtilityBasic):
    MayaAsciiType = 'mayaAscii'
    MayaBinaryType = 'mayaBinary'
    AlembicType = 'Alembic'
    #
    FileTypeDic = {
        '.ma': MayaAsciiType,
        '.mb': MayaBinaryType,
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
    MaDefFileExportKwargs = dict(
        type='mayaAscii',
        options='v=0',
        force=True,
        defaultExtensions=True,
        exportAll=True,
        preserveReferences=False,
    )
    MaDefFileImportKwargs = dict(
        options='v=0;',
        type='mayaAscii',
        i=True,
        renameAll=True,
        mergeNamespacesOnClash=True,
        namespace=':',
        preserveReferences=True
    )

    @classmethod
    def getFileType(cls, fileString):
        """
        :param fileString: str or unicode
        :return: str or unicode
        """
        ext = bscMethods.OsFile.ext(fileString)
        return cls.FileTypeDic.get(ext, cls.MayaAsciiType)

    @classmethod
    def exportCommand(cls, fileString, optionKwargs=None):
        if optionKwargs is None:
            optionKwargs = cls.MaDefFileExportKwargs.copy()
        #
        optionKwargs['type'] = cls.getFileType(fileString)
        #
        cls.MOD_maya_cmds.file(fileString, **optionKwargs)

    @classmethod
    def fileImportCommand(cls, fileString, optionKwargs=None):
        if optionKwargs is None:
            optionKwargs = cls.MaDefFileImportKwargs.copy()
        #
        optionKwargs['type'] = cls.getFileType(fileString)
        #
        cls.MOD_maya_cmds.file(
            fileString,
            **optionKwargs
        )

    @classmethod
    def setFileImport(cls, fileString, namespace=':'):
        optionKwargs = cls.MaDefFileImportKwargs.copy()
        #
        optionKwargs['type'] = cls.getFileType(fileString)
        optionKwargs['namespace'] = namespace
        #
        cls.MOD_maya_cmds.file(
            fileString,
            **optionKwargs
        )


class Texture(object):
    @classmethod
    def existFiles(cls, fileString):
        if bscMethods.OsFile.isExist(fileString):
            return [fileString.replace('\\', bscMethods.OsPath.DEF_separator_os)]
        return bscMethods.OsMultifile._getOsMultifileExistFileList(fileString, '<udim>', bscMethods.OsMultifile.VAR_padding_multifile)
