import brainrender
# brainrender.SHADER_STYLE = 'cartoon'
from brainrender.scene import Scene
import pandas as pd
import numpy as np
import os,glob

scene = Scene()

scene.add_brain_regions(['STN'], alpha=.9,use_original_color=False,wireframe=True,color=(76, 175, 149))

# areas = ['CA3', 'PA', 'STRd','MEA', 'VENT',
#          'LM','PH','LHA','PST','ZI','SNr','SNc']
# for area in areas:
#     scene.add_brain_regions([area], alpha=.1,
#                             use_original_color=False, color=(237, 37, 144),
#                             wireframe=True)

tracts = ['opt','cst','epsc','mfb']
for tract in tracts:
    scene.add_brain_regions([tract], alpha=.5, use_original_color=False)
    scene.actors['root']
    scene.actors['regions'][tract].flag(tract)

#manually add probes here
ccf_shape = np.array([1320, 800, 1140*2])
probes = [(np.array([[880,-230,-300,],[880,140,-300]]),'k',30),#stim
          (np.array([[880,-230,-320,],[880,140,-320]]),'k',30),#stim
          (np.array([[895,15 ,-335,],[895,290,-90 ]]),(229,191,80),100),#probe1
           (np.array([[895,15 ,-335,],[635,290,-335 ]]),(229,191,80),100),#probe2
           (np.array([[950,-60 ,-305,],[850,290,-330 ]]),(229,191,80),100),#probe3
        #   (np.array([[0,-250,0,],[0,134,0]]),'r'),
         ]
center_point_adjust  = np.array([-160,340,-80])


for probe_points in probes:
    scene.add_probe_from_coordinates(ccf_shape + probe_points[0]+center_point_adjust,color=probe_points[1],radius =probe_points[2])

# path = '/Users/danieljdenman/Academics/grants/20200602_r01BRAIN/figs/'
# filename = 'br'+len(glob.glob(os.path.join(path,'br*')))+'.png'
# scene.export_for_web(os.path.join(path,filename))

scene.render()


