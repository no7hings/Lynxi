# coding=utf-8
import os
#
import hashlib
#
import struct


#
def getPackFormat(maxValue):
    outType = 'q'
    if maxValue < 128:
        outType = 'b'
    elif maxValue < 32768:
        outType = 'h'
    elif maxValue < 4294967296:
        outType = 'i'
    return outType


#
def getStrHashKey(data):
    # Debug Texture Attribute
    strData = str(data).lower()
    packArray = [ord(i) for i in strData]
    md5 = hashlib.md5(struct.pack('%s%s' % (len(packArray), getPackFormat(max(packArray))), *packArray)).hexdigest()
    return md5


#
def getFloatHashKey(data, roundLimit=8):
    # Debug Float Data
    strData = str([str(i)[:roundLimit] for i in data if i])
    md5 = hashlib.md5(strData).hexdigest()
    return md5


#
def getIntHashKey(data):
    md5 = hashlib.md5(struct.pack('%s%s' % (len(data), getPackFormat(max(data))), *data)).hexdigest()
    return md5


#
def getNumHashKey(data):
    def getBranch(subData):
        if isinstance(subData, tuple) or isinstance(subData, list):
            [getBranch(i) for i in subData]
        else:
            lis.append(subData)
    #
    lis = []
    #
    getBranch(data)
    md5 = hashlib.md5(struct.pack('%s%s' % (len(lis), getPackFormat(max(lis))), *lis)).hexdigest()
    return md5
