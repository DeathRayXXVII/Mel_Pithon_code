import maya.cmds as cmds
#Create the butt of the spider
cmds.polySphere(name='head', radius=3, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2, ch=1)
cmds.move(0, 3, 0, relative=True, objectSpace=True, worldSpaceDistance=True)
#Create the Main body of the spider
cmds.polySphere(name='body', radius=1, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2, ch=1)
cmds.move(0, 1.6, -3.4, relative=True)
cmds.scale(1.89, 1.89, 1.89, relative=True)
#Adding legs
cmds.polyCylinder(name='leg1', r=1, h=2, sx=20, sy=1, sz=1, ax=[0, 1, 0], rcp=0, cuv=3, ch=1)
cmds.move(2, 2.3, -2.6, relative=True)
cmds.scale(0.249, 1.946, 0.249,)
cmds.rotate(4, 17.5, -29, r=True, ws=True, fo=True)
cmds.duplicate(rr=True)
cmds.rotate(-8, -0, 47, r=True, ws=True, fo=True)
cmds.move(1.507, -0.35, 0.225, relative=True)
cmds.polyUnite('leg1', 'leg2', ch=True, mergeUVSets=1, cp=True, name='rightLeg1')
cmds.select('rightLeg1', r=True)
cmds.duplicate(rr=True)
cmds.move(0, 0, -0.8, r=True)
cmds.rotate(1.65, 3.8, 0.8, r=True, ws=True, fo=True)
cmds.select('rightLeg2', r=True)
cmds.duplicate(rr=True)
cmds.move(0, 0, -0.7, r=True)
cmds.select('rightLeg3', 'rightLeg1', 'rightLeg2', r=True)
cmds.polyMirrorFace('rightLeg1', cm=1, axis=0, ad=1, mm=1, mtt=0, mt=0.001, ma=2, mps=0, sa=30, flipUVs=0, ch=1)
cmds.polyMirrorFace('rightLeg3', cm=1, axis=0, ad=1, mm=1, mtt=0, mt=0.001, ma=2, mps=0, sa=30, flipUVs=0, ch=1)
cmds.polyMirrorFace('rightLeg2', cm=1, axis=0, ad=1, mm=1, mtt=0, mt=0.001, ma=2, mps=0, sa=30, flipUVs=0, ch=1)
#Eye
cmds.polySphere(name='rightEye', r=1, sx=20, sy=20, ax=[0, 1, 0], cuv=2, ch=1)
cmds.scale(0.37, 0.37, 0.37, relative=True)
cmds.move(0.75, 2, -4.86)
cmds.duplicate(n='leftEye', rr=True)
cmds.move(-1.51, 0, 0, r=True)
#Mouth/Fangs
cmds.polyCone(n='Fang', r=1, h=2, sx=20, sy=1, sz=0, ax=[0, 1, 0], rcp=0, cuv=3, ch=1)
cmds.scale(0.465, 0.665, 0.4, r=True)
cmds.move(0.42, 1.18, -5.15, relative=True)
cmds.rotate(-90, 9.505, 0, relative=True)
cmds.polyCone(n='Fang', r=1, h=2, sx=20, sy=1, sz=0, ax=[0, 1, 0], rcp=0, cuv=3, ch=1)
cmds.scale(0.465, 0.665, 0.4, r=True)
cmds.move(-0.42, 1.18, -5.15, relative=True)
cmds.rotate(-90, -9.505, 0, relative=True)
#Hat
cmds.polyCylinder(n='topHot', r=1, h=2, sx=20, sy=2, sz=1, ax=[0, 1, 0], rcp=0, cuv=3, ch=1)
cmds.move(0, 3.7, -4, relative=True)
cmds.scale(0.6, 0.48, 0.6, relative=True)
cmds.rotate(-13, 0, 0, relative=True)
cmds.select('topHat'.f[0:19], r=True)
#clean up
cmds.select('fang1', 'leftEye', 'rightEye', 'rightLeg1', 'body', 'topHat', 'fang', 'rightLeg2', 'rightLeg3', 'head')
cmds.makeIdenity(apply=true, t=1, r=1, s=1, n=0, pn=1)
cmds.delete(constructionHistory=True)




