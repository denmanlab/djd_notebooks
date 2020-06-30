import brainrender
# brainrender.SHADER_STYLE = 'cartoon'
from brainrender.scene import Scene
import pandas as pd
import numpy as np
import os,glob

scene = Scene()

scene.add_brain_regions(['VL'], alpha=.9,use_original_color=False,color=(56, 232, 25))



tracts = ['V3','V4','AQ']
for tract in tracts:
    scene.add_brain_regions([tract], alpha=.5, use_original_color=True)
    scene.actors['root']
    scene.actors['regions'][tract].flag(tract)

scene.render()


