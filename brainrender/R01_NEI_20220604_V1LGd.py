from telnetlib import WONT
import brainrender
# brainrender.SHADER_STYLE = 'cartoon'
from brainrender.scene import Scene
import numpy as np

areas = ['VISp','VISl','LGd','LP']
colors=dict(zip(areas,[(133,119,178),    #Visp color
                        (15,117,188),   #Visl color
                        (219,146,191),   #LGd color
                        (11,149,68)])) #LP color

scene = Scene()
for area in areas:  
    scene.add_brain_regions([area], alpha=.8,color=np.array(np.array(colors[area])/256.).tolist())


do_probe1 = True
do_probe2 = True
do_probe3 = True
#probe A: V1 - LGd
if do_probe1:
    probe = scene.add_from_file("/Users/danieljdenman/Academics/grants/applications/20200800_DP2/figs/Neuropixels1.obj",
                                alpha=1)
    probe.origin(probe.centerOfMass())
    probe.c("green").alpha(1)
    probe_com = probe.centerOfMass()
    root_com = scene.root.centerOfMass()
    probe.origin(probe.centerOfMass())
    probe.rotateY(0).rotateX(180).rotateY(180)
    probe.x(root_com[0] - probe_com[0])
    probe.y(root_com[1] - probe_com[1])
    probe.z(root_com[2] - probe_com[2])
    probe.rotateZ(15)
    probe.x(13500)# rostrocaudal
    probe.z(8250)# mediolateral
    probe.y(-18000)# dorsoventral
    probe.scale([650, 750, 600])

#probe B: V1 - LP
if do_probe2:
    probe2 = scene.add_from_file("/Users/danieljdenman/Academics/grants/applications/20200800_DP2/figs/Neuropixels1.obj",
                                alpha=1)
    probe2.origin(probe2.centerOfMass())
    probe2.c("green").alpha(1)
    probe_com = probe2.centerOfMass()
    root_com = scene.root.centerOfMass()
    probe2.rotateY(0).rotateX(208).rotateY(180)
    probe2.x(root_com[0] - probe_com[0])
    probe2.y(root_com[1] - probe_com[1])
    probe2.z(root_com[2] - probe_com[2])
    probe2.rotateZ(35)
    probe2.x(18700)# rostrocaudal
    probe2.z(17900)# mediolateral
    probe2.y(-13400)# dorsoventral
    probe2.scale([650, 750, 600])

#probeC: V1 - LGd steep
if do_probe3:
    probe3 = scene.add_from_file("/Users/danieljdenman/Academics/grants/applications/20200800_DP2/figs/Neuropixels1.obj",
                                alpha=1)
    probe3.origin(probe3.centerOfMass())
    probe3.c("green").alpha(1)
    probe_com = probe3.centerOfMass()
    root_com = scene.root.centerOfMass()
    probe3.rotateY(180).rotateX(190).rotateY(180)
    probe3.x(root_com[0] - probe_com[0])
    probe3.y(root_com[1] - probe_com[1])
    probe3.z(root_com[2] - probe_com[2])
    probe3.rotateZ(40)
    probe3.x(21800)# rostrocaudal
    probe3.z(11900)# mediolateral
    probe3.y(-13800)# dorsoventral
    probe3.scale([650, 750, 600])


# skull = scene.add_from_file("/Users/danieljdenman/github/BrainRender/Examples/example_files/skull.stl")
# skull.c("ivory").alpha(1)

# # Align skull and brain (scene.root)
# skull_com = skull.centerOfMass()
# root_com = scene.root.centerOfMass()

# skull.origin(skull.centerOfMass())
# skull.rotateY(90).rotateX(180)
# skull.x(root_com[0] - skull_com[0])
# skull.y(root_com[1] - skull_com[1])
# skull.z(root_com[2] - skull_com[2])
# skull.x(3500)
# skull.rotateZ(-25)
# skull.y(7800)
# skull.scale([1300, 1500, 1200])


# Cut skull actor to show brain inside
# scene.cut_actors_with_plane("sagittal", actors=skull)

# Improve looks
# scene.add_silhouette(scene.root, lw=3)
# scene.add_silhouette(skull, lw=3)
scene.render()  