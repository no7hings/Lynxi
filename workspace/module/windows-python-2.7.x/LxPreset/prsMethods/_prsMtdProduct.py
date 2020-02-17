# coding:utf-8
from LxBasic import bscMethods

from LxPreset import prsCore

from LxPreset import prsVariants


class _UtilMethod(object):
    @classmethod
    def _setStringToLabelname(cls, *args):
        string = ''
        index = 0
        for i in args:
            if isinstance(i, (str, unicode)):
                if i:
                    if i.startswith(u'_'):
                        i = i[1:]

                    if index > 0:
                        i = i.capitalize()

                    string += i

                    index += 1
        return string

    @classmethod
    def _setLabelnameCovertToName(cls, *args):
        string = ''
        for i in args:
            if isinstance(i, (str, unicode)):
                if i:
                    if not i.startswith(u'_'):
                        i = u'_{}'.format(i)

                    string += i
        return string

    @classmethod
    def _toNamespace(cls, namespaceString):
        return '' if namespaceString is None else namespaceString + ':'


class Product(
    prsCore.MtdProductBasic,
    _UtilMethod
):
    pass


class Asset(
    prsCore.MtdAssetBasic,
    _UtilMethod
):
    @classmethod
    def toName(cls, *args):
        return prsVariants.Util.Lynxi_Prefix_Product_Asset + cls._setLabelnameCovertToName(*args)

    @classmethod
    def toGroupName(cls, *args):
        return cls.toName(*args) + prsVariants.Util.basicGroupLabel

    @classmethod
    def rootName(cls, nameString, namespaceString=None):
        return cls._toNamespace(namespaceString) + cls.toGroupName(nameString, prsVariants.Util.basicUnitRootGroupLabel)
    
    @classmethod
    def toLinkSubLabelname(cls, stageString):
        if cls.isModelStageName(stageString):
            return prsVariants.Util.basicModelLinkLabel
        elif cls.isRigStageName(stageString):
            return prsVariants.Util.basicRigLinkLabel
        elif cls.isGroomStageName(stageString):
            return prsVariants.Util.basicCharacterFxLinkLabel
        elif cls.isSolverStageName(stageString):
            return prsVariants.Util.basicSolverLinkLabel
        elif cls.isLightStageName(stageString):
            return prsVariants.Util.basicLightLinkLabel
        elif cls.isAssemblyStageName(stageString):
            return prsVariants.Util.basicAssemblyLinkLabel
        return prsVariants.Util.basicModelLinkLabel
    
    @classmethod
    def toLinkMainLabelname(cls, stageString):
        if cls.isModelStageName(stageString):
            return prsVariants.Util.basicModelLinkGroupLabel
        elif cls.isRigStageName(stageString):
            return prsVariants.Util.basicRigLinkGroupLabel
        elif cls.isGroomStageName(stageString):
            return prsVariants.Util.basicCfxLinkGroupLabel
        elif cls.isSolverStageName(stageString):
            return prsVariants.Util.basicSolverLinkGroupLabel
        elif cls.isLightStageName(stageString):
            return prsVariants.Util.basicLightLinkGroupLabel
        return prsVariants.Util.basicModelLinkGroupLabel

    @classmethod
    def toLinkGroupName(cls, nameString, stageString, namespaceString=None):
        return cls._toNamespace(namespaceString) + cls.toGroupName(nameString, cls.toLinkMainLabelname(stageString))

    @classmethod
    def modelLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.modelLinkName(), namespaceString)

    @classmethod
    def rigLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.rigLinkName(), namespaceString)

    @classmethod
    def groomLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.groomLinkName(), namespaceString)

    @classmethod
    def solverLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.solverLinkName(), namespaceString)

    @classmethod
    def lightLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.lightLinkName(), namespaceString)

    @classmethod
    def serverRoot(cls):
        return prsVariants.Util.serverAssetRoot

    @classmethod
    def backupRoot(cls):
        return prsVariants.Util.localAssetRoot

    @classmethod
    def localRoot(cls):
        return prsVariants.Util.backupAssetRoot

    @classmethod
    def serverDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsVariants.Util.serverSceneRoot,
            prsVariants.Util.basicAssetFolder,
            prsVariants.Util.basicUnitFolder
        )

    @classmethod
    def backupDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsVariants.Util.backupSceneRoot,
            prsVariants.Util.basicAssetFolder,
            prsVariants.Util.basicUnitFolder
        )

    @classmethod
    def localDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsVariants.Util.localSceneRoot,
            prsVariants.Util.basicAssetFolder,
            prsVariants.Util.basicUnitFolder
        )


class Scenery(
    prsCore.MtdSceneryBasic,
    _UtilMethod
):
    @classmethod
    def toName(cls, *args):
        return prsVariants.Util.Lynxi_Prefix_Product_scenery + cls._setLabelnameCovertToName(*args)

    @classmethod
    def toGroupName(cls, *args):
        return cls.toName(*args) + prsVariants.Util.basicGroupLabel

    @classmethod
    def rootName(cls, nameString, namespaceString=None):
        return cls._toNamespace(namespaceString) + cls.toGroupName(nameString, prsVariants.Util.basicUnitRootGroupLabel)
    
    @classmethod
    def toLinkMainLabelname(cls, stageString):
        if cls.isSceneryLinkName(stageString):
            return prsVariants.Util.basicSceneryLinkLabel
        elif cls.isLayoutLinkName(stageString):
            return prsVariants.Util.basicLayoutLinkLabel
        elif cls.isAnimationLinkName(stageString):
            return prsVariants.Util.basicAnimationLinkLabel
        elif cls.isSolverLinkName(stageString):
            return prsVariants.Util.basicSolverLinkLabel
        elif cls.isSimulationLinkName(stageString):
            return prsVariants.Util.basicSimulationLinkLabel
        elif cls.isLightLinkName(stageString):
            return prsVariants.Util.basicLightLinkLabel
        return prsVariants.Util.basicSceneryLinkLabel

    @classmethod
    def toLinkGroupName(cls, nameString, stageString, namespaceString=None):
        return cls._toNamespace(namespaceString) + cls.toGroupName(nameString, cls.toLinkMainLabelname(stageString))

    @classmethod
    def sceneryLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.assemblyLinkName(), namespaceString)

    @classmethod
    def layoutLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.layoutLinkName, namespaceString)

    @classmethod
    def animationLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.animationLinkName, namespaceString)

    @classmethod
    def solverLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.solverLinkName, namespaceString)

    @classmethod
    def simulationLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.simulationLinkName, namespaceString)

    @classmethod
    def lightLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.lightLinkName, namespaceString)

    @classmethod
    def serverRoot(cls):
        return prsVariants.Util.serverSceneryRoot

    @classmethod
    def backupRoot(cls):
        return prsVariants.Util.localSceneryRoot

    @classmethod
    def localRoot(cls):
        return prsVariants.Util.backupSceneryRoot

    @classmethod
    def serverDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsVariants.Util.serverSceneRoot,
            prsVariants.Util.basicSceneryFolder,
            prsVariants.Util.basicUnitFolder
        )

    @classmethod
    def backupDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsVariants.Util.backupSceneRoot,
            prsVariants.Util.basicSceneryFolder,
            prsVariants.Util.basicUnitFolder
        )

    @classmethod
    def localDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsVariants.Util.localSceneRoot,
            prsVariants.Util.basicSceneryFolder,
            prsVariants.Util.basicUnitFolder
        )


class Scene(
    prsCore.MtdSceneBasic,
    _UtilMethod
):
    @classmethod
    def toName(cls, *args):
        return prsVariants.Util.Lynxi_Prefix_Product_scene + cls._setLabelnameCovertToName(*args)

    @classmethod
    def toGroupName(cls, *args):
        return cls.toName(*args) + prsVariants.Util.basicGroupLabel

    @classmethod
    def rootName(cls, nameString, namespaceString=None):
        return cls._toNamespace(namespaceString) + cls.toGroupName(nameString, prsVariants.Util.basicUnitRootGroupLabel)
    
    @classmethod
    def toLinkMainLabelname(cls, stageString):
        if cls.isLayoutLinkName(stageString):
            return prsVariants.Util.scLayoutLabel
        elif cls.isAnimationLinkName(stageString):
            return prsVariants.Util.scAnimationLabel
        elif cls.isSolverLinkName(stageString):
            return prsVariants.Util.scSolverLabel
        elif cls.isSimulationLinkName(stageString):
            return prsVariants.Util.scSimulationLabel
        elif cls.isLightLinkName(stageString):
            return prsVariants.Util.scLightLabel
        return prsVariants.Util.scLayoutLabel
    
    @classmethod
    def toLinkGroupName(cls, nameString, stageString, namespaceString=None):
        return cls._toNamespace(namespaceString) + cls.toGroupName(nameString, cls.toLinkMainLabelname(stageString))

    @classmethod
    def layoutLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.layoutLinkName, namespaceString)

    @classmethod
    def animationLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.animationLinkName, namespaceString)

    @classmethod
    def solverLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.solverLinkName, namespaceString)

    @classmethod
    def simulationLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.simulationLinkName, namespaceString)

    @classmethod
    def lightLinkGroupName(cls, nameString, namespaceString=None):
        return cls.toLinkGroupName(nameString, cls.lightLinkName, namespaceString)

    @classmethod
    def serverRoot(cls):
        return prsVariants.Util.serverSceneRoot

    @classmethod
    def backupRoot(cls):
        return prsVariants.Util.localSceneRoot

    @classmethod
    def localRoot(cls):
        return prsVariants.Util.backupSceneRoot

    @classmethod
    def serverDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsVariants.Util.serverSceneRoot,
            prsVariants.Util.basicSceneFolder,
            prsVariants.Util.basicUnitFolder
        )

    @classmethod
    def backupDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsVariants.Util.backupSceneRoot,
            prsVariants.Util.basicSceneFolder,
            prsVariants.Util.basicUnitFolder
        )

    @classmethod
    def localDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsVariants.Util.localSceneRoot,
            prsVariants.Util.basicSceneFolder,
            prsVariants.Util.basicUnitFolder
        )
