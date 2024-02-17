import maya.cmds as cmds


def rig_color(color):
    sels = cmds.ls(sl=True)

    shape = cmds.listRelatives(sels, shapes=True)

    for selection in shape:
        cmds.setAttr(selection + '.overrideEnabled', 1)
        cmds.setAttr(selection + '.overrideColor', color)


def create_ui():
    if cmds.window("myWindow", exists=True):
        cmds.deleteUI("myWindow", window=True)

    my_window = cmds.window("myWindow", title="Color Change UI", widthHeight=(200, 100))
    cmds.columnLayout(adjustableColumn=True)

    color_field = cmds.textField(text='Color Index')

    def change_color(*args):
        color_index = cmds.textField(color_field, query=True, text=True)
        rig_color(int(color_index))

    cmds.button(label="Change Color", command=change_color)
    cmds.showWindow(my_window)


create_ui()
