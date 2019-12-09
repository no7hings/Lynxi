# coding:utf-8
from LxCore import lxConfigure, lxBasic

from LxCore.preset.prod import projectPr


class App(object):
    def __init__(self, appName, appVersion):
        self._initApp(appName, appVersion)

    def _initApp(self, appName, appVersion):
        self._appName = appName
        self._appVersion = appVersion

    def setup(self):
        pass


class Maya(App):
    def __init__(self, appVersion):
        self._initApp(lxConfigure.Lynxi_App_Maya, appVersion)

    def setup(self):
        pass


class _PlugBasic(object):
    PLUG_CLS = None
    def _initPlugBasic(self, projectName):
        self._appName = None
        self._appVersion = None

        self._projectName = projectName

        self._customPlugLis = []
        self._definitionPlugLis = []

        self._customDatumDic = projectPr.getMaCustomPlugPresetDic(self._projectName)

    def _loadCustom(self):
        if self._customDatumDic:
            for k, v in self._customDatumDic.items():
                plugName = k
                plugVersion = v[lxConfigure.Key_Plug_Version]
                plug = self.PLUG_CLS(self._appVersion, plugName, plugVersion)
                self._customPlugLis.append(plug)

    def _loadShare(self):
        pass

    def projectName(self):
        return self._projectName

    def customPlugs(self):
        return self._customPlugLis

    def definitionPlugs(self):
        return self._definitionPlugLis

    def pushEnviron(self):
        pass

    def localizationSource(self):
        keyword = 'Source(s)'
        if self.customPlugs():
            traceMessage = u'App "{}" Update Custom Plug {}'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)
            [i.localizationSource() for i in self.customPlugs()]
        else:
            traceMessage = u'App "{}" Custom Plug {} is Non - Exist'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)

        if self.definitionPlugs():
            traceMessage = u'App "{}" Update Share Plug {}'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)
            [i.localizationSource() for i in self.definitionPlugs()]
        else:
            traceMessage = u'App "{}" Share Plug {} is Non - Exist'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)

    def push(self):
        pass


class MayaPlug(_PlugBasic):
    PLUG_CLS = lxConfigure.MayaPlug
    def __init__(self, projectName):
        self._initPlugBasic(projectName)

        self._appName = lxConfigure.Lynxi_App_Maya
        self._appVersion = projectPr.getProjectMayaVersion(self._projectName)

        if self._appVersion is not None:
            self._loadCustom()
            self._loadShare()

    def _loadCustom(self):
        if self._customDatumDic:
            for k, v in self._customDatumDic.items():
                plugName = k
                plugVersion = v[lxConfigure.Key_Plug_Version]
                plug = self.PLUG_CLS(self._appVersion, plugName, plugVersion)
                self._customPlugLis.append(plug)

    def _loadShare(self):
        self._definitionPlugLis = [
            lxConfigure.MayaSharePlug('2019', 'lynxinode', '1.0')
        ]

    def pushEnviron(self):
        keyword = 'Environ(s)'
        environFile = lxConfigure.Maya(self._appVersion).environFile()

        lis = []

        if self.customPlugs():
            traceMessage = u'App "{}" Update Custom Plug {}'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)
            for plug in self.customPlugs():
                environDatum = plug.toAppEnvironString()
                if environDatum is not None:
                    lis.append(environDatum)
        else:
            traceMessage = u'App "{}" Custom Plug {} is Non - Exist'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)

        if self.definitionPlugs():
            traceMessage = u'App "{}" Update Share Plug {}'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)
            for plug in self.definitionPlugs():
                environDatum = plug.toAppEnvironString()
                if environDatum is not None:
                    lis.append(environDatum)
        else:
            traceMessage = u'App "{}" Share Plug {} is Non - Exist'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)

        if lis:
            traceMessage = u'App "{}" Update Environ : "{}" '.format(self._appName, environFile)
            lxConfigure.Message().traceResult(traceMessage)

            lxBasic.writeOsData('\r\n'.join(lis), environFile)

    def pushModule(self):
        keyword = 'Module(s)'
        if self.customPlugs():
            traceMessage = u'App "{}" Update Custom Plug {}'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)
            [i.pushModule() for i in self.customPlugs()]
        else:
            traceMessage = u'App "{}" Custom Plug {} is Non - Exist'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)

        if self.definitionPlugs():
            traceMessage = u'App "{}" Update Share Plug {}'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)
            [i.pushModule() for i in self.definitionPlugs()]
        else:
            traceMessage = u'App "{}" Share Plug {} is Non - Exist'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)

    def push(self):
        if lxConfigure.Lynxi_Mode_Plug_Enable_Local is True:
            self.localizationSource()
        if lxConfigure.Lynxi_Mode_Plug_Enable_Module is True:
            self.pushModule()
        if lxConfigure.Lynxi_Mode_Plug_Enable_Environ is True:
            self.pushEnviron()
