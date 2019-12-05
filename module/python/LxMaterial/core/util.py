# coding:utf-8
import re


#
def capitalize(string):
    return string[0].upper() + string[1:] if string else string


#
def prettify(string):
    return ' '.join([capitalize(x) for x in re.findall(r'[a-zA-Z][a-z]*[0-9]*', string)])


#
def toCamelCase(string):
    return re.sub(r'_(\w)', lambda x: x.group(1).upper(), string)


#
def toUnderlineCase(string):
    return re.sub(re.compile(r'([a-z]|\d)([A-Z])'), r'\1_\2', string).lower()


#
def toNodeAttr():
    pass
