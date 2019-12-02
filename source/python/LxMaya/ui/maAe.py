# encoding=utf-8
import inspect
#
import os
#
import pkgutil
#
import sys
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.mel as mel
#
import LxMaya.ae


#
def setupAETemplate():
    templates = []
    #
    pathsList = LxMaya.ae.__path__
    for i in pathsList:
        sysPaths = sys.path
        if os.path.exists(i):
            if i not in sysPaths:
                sys.path.insert(0, i)
    #
    for importer, modName, isPkg in pkgutil.iter_modules(pathsList):
        if modName.endswith('Template') and modName not in templates:
            try:
                mod = __import__(modName, globals(), locals(), [], -1)
                procName = 'AE%s' % modName
                if hasattr(mod, modName):
                    templates.append(modName)
                    aeProc(modName, modName, procName)
                elif hasattr(mod, procName):
                    templates.append(modName)
                    aeProc(modName, procName, procName)
            except Exception:
                print 'Error Parsing AETemplate File %s' % str(modName)
                import traceback
                print traceback.format_exc()


#
def aeProc(modName, objName, procName):
    contents = '''global proc %(procName)s( string $nodeName ){python("import %(__name__)s;%(__name__)s.aeLoader('%(modName)s','%(objName)s','" + $nodeName + "')");}'''
    d = locals().copy()
    d['__name__'] = __name__
    mel.eval(contents % d)


#
def aeLoader(modName, objName, nodeName):
    mod = __import__(modName, globals(), locals(), [objName], -1)
    try:
        f = getattr(mod, objName)
        if inspect.isfunction(f):
            f(nodeName)
        elif inspect.isclass(f):
            inst = f(cmds.nodeType(nodeName))
            inst._doSetup(nodeName)
        else:
            print "AE Object %s has Invalid Type %s" % (f, type(f))
    except Exception:
        print "Failed to Load Python Attribute Editor Template '%s.%s'" % (modName, objName)
        import traceback
        traceback.print_exc()