# coding:utf-8
from LxBasic import bscMethods

from LxPreset import prsMtdCore

from LxPreset import prsOutputs


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
    prsMtdCore.Mtd_PrsProduct,
    _UtilMethod
):
    pass


class Asset(
    prsMtdCore.Mtd_PrsAsset,
    _UtilMethod
):
    @classmethod
    def toName(cls, *args):
        return prsOutputs.Util.Lynxi_Prefix_Product_Asset + cls._setLabelnameCovertToName(*args)

    @classmethod
    def toGroupName(cls, *args):
        return cls.toName(*args) + prsOutputs.Util.basicGroupLabel

    @classmethod
    def rootName(cls, nameString, namespaceString=None):
        return cls._toNamespace(namespaceString) + cls.toGroupName(nameString, prsOutputs.Util.basicUnitRootGroupLabel)
    
    @classmethod
    def toLinkSubLabelname(cls, stageString):
        if cls.isModelStageName(stageString):
            return prsOutputs.Util.basicModelLinkLabel
        elif cls.isRigStageName(stageString):
            return prsOutputs.Util.basicRigLinkLabel
        elif cls.isGroomStageName(stageString):
            return prsOutputs.Util.basicCharacterFxLinkLabel
        elif cls.isSolverStageName(stageString):
            return prsOutputs.Util.basicSolverLinkLabel
        elif cls.isLightStageName(stageString):
            return prsOutputs.Util.basicLightLinkLabel
        elif cls.isAssemblyStageName(stageString):
            return prsOutputs.Util.basicAssemblyLinkLabel
        return prsOutputs.Util.basicModelLinkLabel
    
    @classmethod
    def toLinkMainLabelname(cls, stageString):
        if cls.isModelStageName(stageString):
            return prsOutputs.Util.basicModelLinkGroupLabel
        elif cls.isRigStageName(stageString):
            return prsOutputs.Util.basicRigLinkGroupLabel
        elif cls.isGroomStageName(stageString):
            return prsOutputs.Util.basicCfxLinkGroupLabel
        elif cls.isSolverStageName(stageString):
            return prsOutputs.Util.basicSolverLinkGroupLabel
        elif cls.isLightStageName(stageString):
            return prsOutputs.Util.basicLightLinkGroupLabel
        return prsOutputs.Util.basicModelLinkGroupLabel

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
        return prsOutputs.Util.serverAssetRoot

    @classmethod
    def backupRoot(cls):
        return prsOutputs.Util.localAssetRoot

    @classmethod
    def localRoot(cls):
        return prsOutputs.Util.backupAssetRoot

    @classmethod
    def serverDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsOutputs.Util.serverSceneRoot,
            prsOutputs.Util.basicAssetFolder,
            prsOutputs.Util.basicUnitFolder
        )

    @classmethod
    def backupDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsOutputs.Util.backupSceneRoot,
            prsOutputs.Util.basicAssetFolder,
            prsOutputs.Util.basicUnitFolder
        )

    @classmethod
    def localDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsOutputs.Util.localSceneRoot,
            prsOutputs.Util.basicAssetFolder,
            prsOutputs.Util.basicUnitFolder
        )


class Scenery(
    prsMtdCore.Mtd_PrsScenery,
    _UtilMethod
):
    @classmethod
    def toName(cls, *args):
        return prsOutputs.Util.Lynxi_Prefix_Product_scenery + cls._setLabelnameCovertToName(*args)

    @classmethod
    def toGroupName(cls, *args):
        return cls.toName(*args) + prsOutputs.Util.basicGroupLabel

    @classmethod
    def rootName(cls, nameString, namespaceString=None):
        return cls._toNamespace(namespaceString) + cls.toGroupName(nameString, prsOutputs.Util.basicUnitRootGroupLabel)
    
    @classmethod
    def toLinkMainLabelname(cls, stageString):
        if cls.isSceneryLinkName(stageString):
            return prsOutputs.Util.basicSceneryLinkLabel
        elif cls.isLayoutLinkName(stageString):
            return prsOutputs.Util.basicLayoutLinkLabel
        elif cls.isAnimationLinkName(stageString):
            return prsOutputs.Util.basicAnimationLinkLabel
        elif cls.isSolverLinkName(stageString):
            return prsOutputs.Util.basicSolverLinkLabel
        elif cls.isSimulationLinkName(stageString):
            return prsOutputs.Util.basicSimulationLinkLabel
        elif cls.isLightLinkName(stageString):
            return prsOutputs.Util.basicLightLinkLabel
        return prsOutputs.Util.basicSceneryLinkLabel

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
        return prsOutputs.Util.serverSceneryRoot

    @classmethod
    def backupRoot(cls):
        return prsOutputs.Util.localSceneryRoot

    @classmethod
    def localRoot(cls):
        return prsOutputs.Util.backupSceneryRoot

    @classmethod
    def serverDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsOutputs.Util.serverSceneRoot,
            prsOutputs.Util.basicSceneryFolder,
            prsOutputs.Util.basicUnitFolder
        )

    @classmethod
    def backupDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsOutputs.Util.backupSceneRoot,
            prsOutputs.Util.basicSceneryFolder,
            prsOutputs.Util.basicUnitFolder
        )

    @classmethod
    def localDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsOutputs.Util.localSceneRoot,
            prsOutputs.Util.basicSceneryFolder,
            prsOutputs.Util.basicUnitFolder
        )


class Scene(
    prsMtdCore.Mtd_PrsScene,
    _UtilMethod
):
    @classmethod
    def toName(cls, *args):
        return prsOutputs.Util.Lynxi_Prefix_Product_scene + cls._setLabelnameCovertToName(*args)

    @classmethod
    def toGroupName(cls, *args):
        return cls.toName(*args) + prsOutputs.Util.basicGroupLabel

    @classmethod
    def rootName(cls, nameString, namespaceString=None):
        return cls._toNamespace(namespaceString) + cls.toGroupName(nameString, prsOutputs.Util.basicUnitRootGroupLabel)
    
    @classmethod
    def toLinkMainLabelname(cls, stageString):
        if cls.isLayoutLinkName(stageString):
            return prsOutputs.Util.scLayoutLabel
        elif cls.isAnimationLinkName(stageString):
            return prsOutputs.Util.scAnimationLabel
        elif cls.isSolverLinkName(stageString):
            return prsOutputs.Util.scSolverLabel
        elif cls.isSimulationLinkName(stageString):
            return prsOutputs.Util.scSimulationLabel
        elif cls.isLightLinkName(stageString):
            return prsOutputs.Util.scLightLabel
        return prsOutputs.Util.scLayoutLabel
    
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
        return prsOutputs.Util.serverSceneRoot

    @classmethod
    def backupRoot(cls):
        return prsOutputs.Util.localSceneRoot

    @classmethod
    def localRoot(cls):
        return prsOutputs.Util.backupSceneRoot

    @classmethod
    def serverDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsOutputs.Util.serverSceneRoot,
            prsOutputs.Util.basicSceneFolder,
            prsOutputs.Util.basicUnitFolder
        )

    @classmethod
    def backupDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsOutputs.Util.backupSceneRoot,
            prsOutputs.Util.basicSceneFolder,
            prsOutputs.Util.basicUnitFolder
        )

    @classmethod
    def localDirectory(cls):
        return bscMethods.OsPath.composeBy(
            prsOutputs.Util.localSceneRoot,
            prsOutputs.Util.basicSceneFolder,
            prsOutputs.Util.basicUnitFolder
        )
