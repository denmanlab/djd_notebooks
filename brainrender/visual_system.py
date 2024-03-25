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
    scene.add_brain_regions([area], alpha=.5,color=np.array(np.array(colors[area])/256.).tolist())


# scene.add_brain_regions(['SCs'], alpha=.5, color=(204/256,255/256,102/256))

# scene.add_brain_regions(['LP'], alpha=.5, color=(253/256,155/256,51/255))
# scene.add_brain_regions(['VISpm'], alpha=.5, color=(253/256,155/256,51/255))
# scene.add_brain_regions(['ACAd'], alpha=.5, color=(253/256,155/256,51/255))

# scene.add_brain_regions(['VAL'], alpha=.5, color=(51/256,102/256,1))
# scene.add_brain_regions(['VM'], alpha=.5, color=(51/256,102/256,1))
# scene.add_brain_regions(['RSPd'], alpha=.5, color=(51/256,102/256,1))

# scene.add_brain_regions(['MOp'], alpha=.5, color=(204/256,51/256,0/256))
# scene.add_brain_regions(['MOs'], alpha=.5, color=(204/256,51/256,0/256))
# scene.add_brain_regions(['STRd'], alpha=.5, color=(204/256,51/256,0/256))
# scene.add_brain_regions(['scwm'], alpha=.15, use_original_color=True)

probe = scene.add_from_file("/Users/danieljdenman/Academics/grants/applications/20200800_DP2/figs/Neuropixels1.obj",
                            alpha=1)
probe.origin(probe.centerOfMass())
probe.c("green").alpha(1)
probe_com = probe.centerOfMass()
root_com = scene.root.centerOfMass()
probe.origin(probe.centerOfMass())
probe.rotateY(90).rotateX(190).rotateY(180)
probe.x(root_com[0] - probe_com[0])
probe.y(root_com[1] - probe_com[1])
probe.z(root_com[2] - probe_com[2])
probe.rotateZ(45)
probe.x(22000)
probe.z(11400)
probe.y(-13800)
# probe.z(13800)
probe.scale([650, 750, 600])

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