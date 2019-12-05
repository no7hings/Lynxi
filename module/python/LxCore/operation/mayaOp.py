# coding=utf-8
import sys
#
from subprocess import Popen, PIPE


#
def getMaPyCommandExe():
    return 'C:/Program Files/Autodesk/Maya2017/bin/mayapy.exe'


#
def runMaPyCommand(command):
    commandExe = getMaPyCommandExe()
    commandString = '''"{0}" {1}'''.format(commandExe, command)
    return Popen(commandString, shell=True, stdout=PIPE, stderr=PIPE).stdout.readlines()


#
def runMaAlone():
    command = '''import maya.standalone; maya.standalone.initialize(name='python'); sys.path.insert(0, 'D:/work/tdAsset/lynxi/setup/windows'); import mayaSetup; mayaSetup.setup('nn4_mv1')'''
    runMaPyCommand(command)


