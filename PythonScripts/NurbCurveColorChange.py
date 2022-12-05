import maya.cmds as cmds


def rig_color(color):
    sels = cmds.ls(sl=True)

    for sel in sels:
        cmds.setAttr(sels + '.overrideEnabled', 1)
        cmds.setAttr(sels + '.overrideColor', color)


rig_color("17")
