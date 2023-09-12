import maya.cmds as cmds

def create_joint():
    """
    Creates a joint at each selection(s) transfrom.
    Returns: [joints]
    """
    selection = cmds.ls(sl=True)
    new_joints = []

    for sel in selection:
        position = cmds.xform(sel, q=True, translation=True, worldSpace=True)
        cmds.select(cl=True)

        jnt = cmds.joint()
        new_joints.append(jnt)
        cmds.xform(jnt, worldSpace=True, translation=position)

    cmds.select(new_joints, r=True)

    return new_joints

create_joint()
