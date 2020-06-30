import brainrender
# brainrender.SHADER_STYLE = 'cartoon'
# brainrender.ROOT_COLOR = (70,205,235)
brainrender.ROOT_ALPHA = .1
from brainrender.scene import Scene
import pandas as pd
import numpy as np
import os,glob

scene = Scene()

scene.add_brain_regions(['VISp'], alpha=.9,use_original_color=True,wireframe=True)

areas = ['CA1', 'SUB', 'PRE','ProS', 'RSP',
         'VISa','VISrl','VISal','VISam','VISl','VISpl','VISpm']
for area in areas:
    scene.add_brain_regions([area], alpha=.1,
                            use_original_color=False, color=(237, 37, 144),
                            wireframe=True)

# tracts = ['scwm','cc','cst','lfbst']
# for tract in tracts:
#     scene.add_brain_regions([tract], alpha=.5, use_original_color=False)
#     scene.actors['root']
#     scene.actors['regions'][tract].flag(tract)

#manually add probes here
ccf_shape = np.array([1320, 800, 1140*2])
probes = [(np.array([[880,-230,-300,],[880,140,-300]]),'k',30),#stim
          (np.array([[880,-230,-320,],[880,140,-320]]),'k',30),#stim
        #   (np.array([[895,15 ,-335,],[895,290,-90 ]]),(229,191,80),100),#probe1
        #    (np.array([[895,15 ,-335,],[635,290,-335 ]]),(229,191,80),100),#probe2
        #    (np.array([[900,-60 ,-365,],[800,290,-330 ]]),(229,191,80),100),#probe3
        #    (np.array([[880,-400,-310,],[880,140,-310]]),(10,205,235),50),#stim_fiber
        #    (np.array([[880,-800,-310,],[880,-400,-310]]),(70,205,235),120),#stim_fiber
        #    (np.array([[1300,-800,-500,],[950,350,-500]]),(70,205,235),120),#fiber1
        #    (np.array([[200,-800,-500,],[535,350,-500]]),(70,205,235),120),#fiber2
        #   (np.array([[0,-250,0,],[0,134,0]]),'r'),
         ]         
for probe_points in probes:
    scene.add_probe_from_coordinates(ccf_shape + probe_points[0],color=probe_points[1],radius =probe_points[2])


# path = '/Users/danieljdenman/Academics/grants/20200602_r01BRAIN/figs/'
# filename = 'br'+len(glob.glob(os.path.join(path,'br*')))+'.png'
# scene.export_for_web(os.path.join(path,filename))

scene.render()


