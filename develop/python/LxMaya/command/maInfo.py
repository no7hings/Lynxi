# coding=utf-8
import hashlib, struct


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
    md5Key = hashlib.md5(struct.pack('%s%s' % (len(packArray), getPackFormat(max(packArray))), *packArray)).hexdigest()
    return md5Key


#
def getFloatHashKey(data, roundLimit=8):
    # Debug Float Data
    strData = str([str(i)[:roundLimit] for i in data if i])
    md5Key = hashlib.md5(strData).hexdigest()
    return md5Key


#
def getIntHashKey(data):
    md5Key = hashlib.md5(struct.pack('%s%s' % (len(data), getPackFormat(max(data))), *data)).hexdigest()
    return md5Key
