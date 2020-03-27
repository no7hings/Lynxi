# coding:utf-8
from LxMaBasic import myaBscMtdCore


class Frame(myaBscMtdCore.Mtd_MaBasic):
    @classmethod
    def setCurrentFrame(cls, frame):
        cls.MOD_maya_cmds.currentTime(frame)

    @classmethod
    def getCurrentFrame(cls):
        return cls.MOD_maya_cmds.currentTime(query=1)

    @classmethod
    def setAnimationFrameRange(cls, startFrame, endFrame):
        cls.MOD_maya_cmds.playbackOptions(minTime=startFrame), cls.MOD_maya_cmds.playbackOptions(animationStartTime=int(startFrame) - 5)
        cls.MOD_maya_cmds.playbackOptions(maxTime=endFrame), cls.MOD_maya_cmds.playbackOptions(animationEndTime=int(endFrame) + 5)

    @classmethod
    def toFrameRange(cls, frame):
        if isinstance(frame, tuple) or isinstance(frame, list):
            startFrame, endFrame = frame
        elif isinstance(frame, int) or isinstance(float, float):
            startFrame = endFrame = frame
        else:
            startFrame = endFrame = cls.getCurrentFrame()
        return startFrame, endFrame
