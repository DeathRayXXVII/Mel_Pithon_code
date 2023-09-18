import maya.cmds as cmds


def rig_color(color):
    sels = cmds.ls(sl=True)

    shape = cmds.listRelatives(sels, shapes=True)

    for selection in shape:
            cmds.setAttr(selection + '.overrideEnabled', 1)
            cmds.setAttr(selection + '.overrideColor', color)


rig_color(6)
