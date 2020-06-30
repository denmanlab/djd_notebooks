import brainrender
# brainrender.SHADER_STYLE = 'cartoon'
from brainrender.scene import Scene

scene = Scene()

scene.add_brain_regions(['VISp'], alpha=.5,use_original_color=True)
scene.add_brain_regions(['VISal'], alpha=.5,use_original_color=True)

scene.add_brain_regions(['LP'], alpha=.5, use_original_color=True)
scene.add_brain_regions(['LGd'], alpha=.5, use_original_color=True)

scene.add_brain_regions(['SCs'], alpha=.5, use_original_color=True)

scene.add_brain_regions(['scwm'], alpha=.15, use_original_color=True)

scene.render()