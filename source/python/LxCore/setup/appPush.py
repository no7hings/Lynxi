# coding:utf-8
from LxCore import lxConfigure, lxBasic

from LxCore.preset.prod import projectPr


class AppPlug(object):
    def _initPlug(self, projectName):
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
                plugVersion = v[lxConfigure.Lynxi_Key_Plug_Version]
                plug = lxConfigure.AppPlug(self._appName, self._appVersion, plugName, plugVersion)
                self._customPlugLis.append(plug)

    def _loadDefinition(self):
        pass

    def projectName(self):
        return self._projectName

    def customPlugs(self):
        return self._customPlugLis

    def definitionPlugs(self):
        return self._definitionPlugLis

    def pushEnviron(self):
        pass

    def pushSource(self):
        keyword = 'Sourc(s)'
        if self.customPlugs():
            traceMessage = u'App "{}" Update Custom Plug {}'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)
            [i.pushSource() for i in self.customPlugs()]
        else:
            traceMessage = u'App "{}" Custom Plug {} is Non - Exist'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)

        if self.definitionPlugs():
            traceMessage = u'App "{}" Update Definition Plug {}'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)
            [i.pushSource() for i in self.definitionPlugs()]
        else:
            traceMessage = u'App "{}" Definition Plug {} is Non - Exist'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)

    def push(self):
        pass


class MayaPlug(AppPlug):
    def __init__(self, projectName):
        self._initPlug(projectName)

        self._appName = lxConfigure.Lynxi_App_Maya
        self._appVersion = projectPr.getProjectMayaVersion(self._projectName)

        if self._appVersion is not None:
            self._loadCustom()
            self._loadDefinition()

    def _loadCustom(self):
        if self._customDatumDic:
            for k, v in self._customDatumDic.items():
                plugName = k
                plugVersion = v[lxConfigure.Lynxi_Key_Plug_Version]
                plug = lxConfigure.MayaPlug(self._appVersion, plugName, plugVersion)
                self._customPlugLis.append(plug)

    def _loadDefinition(self):
        self._definitionPlugLis = [
            lxConfigure.MayaPlug('2019', 'lynxinode', '1.0', True)
        ]

    def pushEnviron(self):
        keyword = 'Environ(s)'
        environFile = lxConfigure.MayaApp(self._appVersion).environFile()

        lis = []

        if self.customPlugs():
            traceMessage = u'App "{}" Update Custom Plug {}'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)
            for plug in self.customPlugs():
                environDatum = plug.appEnvironDatum()
                if environDatum is not None:
                    lis.append(environDatum)
        else:
            traceMessage = u'App "{}" Custom Plug {} is Non - Exist'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)

        if self.definitionPlugs():
            traceMessage = u'App "{}" Update Definition Plug {}'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)
            for plug in self.definitionPlugs():
                environDatum = plug.appEnvironDatum()
                if environDatum is not None:
                    lis.append(environDatum)
        else:
            traceMessage = u'App "{}" Definition Plug {} is Non - Exist'.format(self._appName, keyword)
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
            traceMessage = u'App "{}" Update Definition Plug {}'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)
            [i.pushModule() for i in self.definitionPlugs()]
        else:
            traceMessage = u'App "{}" Definition Plug {} is Non - Exist'.format(self._appName, keyword)
            lxConfigure.Message().traceResult(traceMessage)

    def push(self):
        self.pushSource()
        self.pushModule()
        self.pushEnviron()
