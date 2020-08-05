# coding:utf-8
from LxBasic import bscMethods

Lynxi_Name_Td_Lis = [
    'dongchangbao',
    'changbao.dong',
    'nothings'
]

LynxiPipelineTdPost = 'Pipeline - TD'
LynxiPipelineTdLevel = 3
pipelineTdBasicPaths = [
    'E:/myworkspace/td/lynxi'
]

# Ignore Send Message
if bscMethods.OsPlatform.username() in Lynxi_Name_Td_Lis:
    LynxiIsSendMail = False
    LynxiIsSendDingTalk = False
else:
    LynxiIsSendMail = True
    LynxiIsSendDingTalk = True

varDic = globals()


def getLxVariantValue(varName):
    if varName in varDic:
        return varDic[varName]


def setLxVariantValue(varName, value):
    varDic[varName] = value
