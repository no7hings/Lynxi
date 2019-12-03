# coding=utf-8
import os
#
import py_compile
#
from LxCore import lxBasic, lxConfigure
#
version = '1.0.0.1'
#
lynxiPath = lxConfigure.Root()
lynxiVersion = lxConfigure.Version()

Path_Develop_Python_Source = lynxiPath.developPythonSourceRoot()
Path_Develop_Icon = lynxiPath.developIconRoot()
File_Develop_Version_File = lynxiVersion.developFile()
#
Path_Product_Python_Source = lynxiPath.productPythonSourceRoot()
Path_Product_Python_Compile = lynxiPath.productPythonCompileRoot()
Path_Product_Icon = lynxiPath.productIconRoot()
File_Product_Version_File = lynxiVersion.productFile()

Path_Backup_Product_Python = 'L:/tdAsset/lynxi/.bck'


# Get Pyc File
def getCompiles(modPath):
    # Sub Method
    def getBranch(osPath):
        fileNames = os.listdir(osPath)
        for i in fileNames:
            osFile = os.path.join(osPath, i).replace('\\', '/')
            if i.endswith('.pyc'):
                pycArray.append(osFile)
            elif os.path.isdir(osFile):
                directory = osFile
                getBranch(directory)
    # List [ <pyc> ]
    pycArray = []
    getBranch(modPath)
    return pycArray


# Get Pyc File
def getIcons(iconPath):
    # Sub Method
    def getBranch(osPath):
        fileNames = os.listdir(osPath)
        for i in fileNames:
            osFile = os.path.join(osPath, i).replace('\\', '/')
            if os.path.isfile(osFile):
                if osFile.endswith('.png'):
                    lis.append(osFile)
                elif osFile.endswith('.svg'):
                    lis.append(osFile)
            elif os.path.isdir(osFile):
                directory = osFile
                getBranch(directory)
    # List [ <pyc> ]
    lis = []
    getBranch(iconPath)
    return lis


# Get Pyc File
def getLineCount(modPath):
    # Sub Method
    def getBranch(osPath):
        fileNames = os.listdir(osPath)
        for i in fileNames:
            osFile = os.path.join(osPath, i).replace('\\', '/')
            if i.endswith('.py') and i != '__init__.py':
                pyArray.append(osFile)
                with open(osFile, 'r') as f:
                    lines = f.readlines()
                    f.close()
                    for line in lines:
                        if line:
                            if (
                                    not line.lstrip().startswith('"""') and
                                    not line.lstrip().startswith("'''") and
                                    not line.lstrip().startswith(':param') and
                                    not line.lstrip().startswith(':return') and
                                    not line.lstrip().startswith('#') and
                                    not line.lstrip().startswith(']') and
                                    not line.lstrip().startswith(')') and
                                    not line.rstrip().endswith(',') and
                                    not line.rstrip().endswith('[') and
                                    not line.rstrip().endswith('(')
                            ):
                                lineArray.append(line)
            elif os.path.isdir(osFile):
                directory = osFile
                getBranch(directory)
    # List [ <pyc> ]
    pyArray = []
    lineArray = []

    moduleName = lxBasic.getOsFileBasename(modPath)
    print moduleName
    if lxBasic.isOsExist(modPath):
        getBranch(modPath)
    return len(pyArray), len(lineArray)


# Upload Config
def setUploadConfig():
    pass


# Upload Pipeline
def setUpload():
    setUploadPyc()


#
def setBackupModule():
    print u'Backup Module ================================================================================================='
    sourcePath = Path_Product_Python_Compile
    targetPath = '{0}/{1}/{2}'.format(Path_Backup_Product_Python, lxBasic.getOsActiveTimeTag(), lxBasic.getOsFileBasename(sourcePath))
    print 'Source : ' + sourcePath
    print 'Target : ' + targetPath
    lxBasic.moveOsFolder(sourcePath, targetPath)


# Upload Pyc
def setUploadPyc():
    print u'>>>> Push Python Module Stat'
    print Path_Product_Python_Compile
    if os.path.isdir(Path_Product_Python_Compile):
        compileLis = getCompiles(Path_Develop_Python_Source)
        if compileLis:
            for pyc in compileLis:
                py = pyc[:-1]
                print 'Source : ' + py
                if os.path.isfile(py):
                    py_compile.compile(py)
                    #
                    sourcePyc = pyc
                    targetPyc = sourcePyc.replace(Path_Develop_Python_Source, Path_Product_Python_Compile)
                    print 'Target : ' + targetPyc
                    lxBasic.setOsFileCopy(sourcePyc, targetPyc)
    print u'>>>> Push Python Module Complete'


# Upload Pyc
def setUploadIcon():
    print u'>>>> Push Icon Stat'
    updateArray = []
    if os.path.isdir(Path_Product_Icon):
        icons = getIcons(Path_Develop_Icon)
        if icons:
            for icon in icons:
                if os.path.isfile(icon):
                    sourceIcon = icon
                    targetIcon = sourceIcon.replace(Path_Develop_Icon, Path_Product_Icon)
                    sourceUpdate = lxBasic.getOsFileUpdateViewTime(sourceIcon)
                    targetUpdate = lxBasic.getOsFileUpdateViewTime(targetIcon)
                    if not sourceUpdate == targetUpdate:
                        updateArray.append((sourceIcon, targetIcon))
    if updateArray:
        for sourceIcon, targetIcon in updateArray:
            print 'Source : ' + sourceIcon
            lxBasic.setOsFileCopy(sourceIcon, targetIcon)
            print 'Target : ' + targetIcon
    print u'>>>> Push Icon Complete'


def setPythonVersion(version_):
    lxConfigure.Log().addDevelop('Set Python Version: {}'.format(version_))
    lxConfigure.Version()._upload(version_)


def setPythonProductVersionInfo(version_):
    lxConfigure.Log().addDevelop('Set Python Product Version Info: {}'.format(version_))
    info = {
        lxConfigure.Lynxi_Key_Info_User: lxBasic.getOsUser(),
        lxConfigure.Lynxi_Key_Info_Timestamp: lxBasic.getOsActiveTimestamp()
    }
    lxBasic.writeOsJson(info, File_Product_Version_File)


if __name__ == '__main__':
    # print Path_Product_Python_Source
    # print Path_Product_Icon
    # setPythonVersion(version)
    # setPythonProductVersionInfo(version)
    # print u'>> Push Pipeline Start'
    # setInformation()
    # setBackupModule()
    # setUploadPyc()
    # setUploadIcon()
    # print u'>> Push Pipeline Complete'
    #
    for i in ['LxCore', 'LxUi', 'LxInterface', 'LxMaya', 'LxDatabase', 'LxDeadline', 'LxMaterial', 'LxGraph', 'LxCommand']:
        print getLineCount('{}/{}'.format(Path_Develop_Python_Source, i))



