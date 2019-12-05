# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
none = ''


# Get Coord Range
def getObjectRange(maObj):
    _x, _y, _z, x, y, z = cmds.exactWorldBoundingBox(maObj)
    xRange = _x, x
    yRange = _y, y
    zRange = _z, z
    return xRange, yRange, zRange


# Get Object In Range
def getInRange(rangeObject, objects=none):
    # List [ <Object> ]
    lis = []
    if not objects:
        objects = cmds.ls(selection=True)
    #
    rangeSet = getObjectRange(rangeObject)
    xRangeSet, yRangeSet, zRangeSet = rangeSet
    for maObj in objects:
        data = getObjectRange(maObj)
        x, y, z = data
        if xRangeSet[0] < x[0] < xRangeSet[1] or xRangeSet[0] < x[1] < xRangeSet[1]:
            if yRangeSet[0] < y[0] < yRangeSet[1] or yRangeSet[0] < y[1] < yRangeSet[1]:
                if zRangeSet[0] < z[0] < zRangeSet[1] or zRangeSet[0] < z[1] < zRangeSet[1]:
                    lis.append(maObj)
    for maObj in objects:
        if maObj in lis:
            cmds.setAttr(maObj + '.visibility', 1)
        else:
            cmds.setAttr(maObj + '.visibility', 0)
    return lis


# Set Object Range Filter
def setRangeFilter(rangeObject, objects=none):
    # List [ <Object> ]
    lis = []
    if not objects:
        objects = cmds.ls(selection=True)
    rangeSet = getObjectRange(rangeObject)
    xRangeSet, yRangeSet, zRangeSet = rangeSet
    # Get Filter
    for maObj in objects:
        data = getObjectRange(maObj)
        x, y, z = data
        #
        if xRangeSet[0] < x[0] < xRangeSet[1] or xRangeSet[0] < x[1] < xRangeSet[1]:
            if yRangeSet[0] < y[0] < yRangeSet[1] or yRangeSet[0] < y[1] < yRangeSet[1]:
                if zRangeSet[0] < z[0] < zRangeSet[1] or zRangeSet[0] < z[1] < zRangeSet[1]:
                    lis.append(maObj)
        #
        if x[0] < xRangeSet[0] < x[1] and x[0] < xRangeSet[1] < x[1]:
            if y[0] < yRangeSet[0] < y[1] and y[0] < yRangeSet[1] < y[1]:
                if z[0] < zRangeSet[0] < z[1] and z[0] < zRangeSet[1] < z[1]:
                    lis.append(maObj)
        #
        if xRangeSet[0] < x[0] < xRangeSet[1] or xRangeSet[0] < x[1] < xRangeSet[1]:
            if y[0] < yRangeSet[0] < y[1] and y[0] < yRangeSet[1] < y[1]:
                if z[0] < zRangeSet[0] < z[1] and z[0] < zRangeSet[1] < z[1]:
                    lis.append(maObj)
        if x[0] < xRangeSet[0] < x[1] and x[0] < xRangeSet[1] < x[1]:
            if yRangeSet[0] < y[0] < yRangeSet[1] or yRangeSet[0] < y[1] < yRangeSet[1]:
                if z[0] < zRangeSet[0] < z[1] and z[0] < zRangeSet[1] < z[1]:
                    lis.append(maObj)
        if x[0] < xRangeSet[0] < x[1] and x[0] < xRangeSet[1] < x[1]:
            if y[0] < yRangeSet[0] < y[1] and y[0] < yRangeSet[1] < y[1]:
                if zRangeSet[0] < z[0] < zRangeSet[1] or zRangeSet[0] < z[1] < zRangeSet[1]:
                    lis.append(maObj)
        #
        if xRangeSet[0] < x[0] < xRangeSet[1] or xRangeSet[0] < x[1] < xRangeSet[1]:
            if yRangeSet[0] < y[0] < yRangeSet[1] or yRangeSet[0] < y[1] < yRangeSet[1]:
                if z[0] < zRangeSet[0] < z[1] and z[0] < zRangeSet[1] < z[1]:
                    lis.append(maObj)
        if x[0] < xRangeSet[0] < x[1] and x[0] < xRangeSet[1] < x[1]:
            if yRangeSet[0] < y[0] < yRangeSet[1] or yRangeSet[0] < y[1] < yRangeSet[1]:
                if zRangeSet[0] < z[0] < zRangeSet[1] or zRangeSet[0] < z[1] < zRangeSet[1]:
                    lis.append(maObj)
        if xRangeSet[0] < x[0] < xRangeSet[1] or xRangeSet[0] < x[1] < xRangeSet[1]:
            if y[0] < yRangeSet[0] < y[1] and y[0] < yRangeSet[1] < y[1]:
                if zRangeSet[0] < z[0] < zRangeSet[1] or zRangeSet[0] < z[1] < zRangeSet[1]:
                    lis.append(maObj)
    # Set Filter
    for maObj in objects:
        if maObj in lis:
            cmds.setAttr(maObj + '.visibility', 1)
        elif not maObj in lis:
            cmds.setAttr(maObj + '.visibility', 0)
    return lis
