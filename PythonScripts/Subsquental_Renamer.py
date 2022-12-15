import maya.cmds as cmds

def subRenamer():
    selsInput = input()
    sels = cmds.ls(sl=True)
    count = selsInput.count('#')
    selsPartition = selsInput.partition(count * "#")
    if len(sels) <= 0:
        print("Reselect")
    else:
        for i in range(len(sels)):
            newName = selsPartition[0] + str(i+1).zfill(count) + selsPartition[2]
            cmds.rename(sels[i], newName)

subRenamer()
