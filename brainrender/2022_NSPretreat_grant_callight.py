import brainrender
# brainrender.SHADER_STYLE = 'cartoon'
from brainrender.scene import Scene
from brainrender.actors import Points
import numpy as np
import glob
import pickle5 as pkl
import pandas

pkls = glob.glob('/Users/danieljdenman/Desktop/G17_Cells/cell*.pkl')

areas = ['VISp','VISl','LGd','LP']
colors=dict(zip(areas,[(133,119,178),    #Visp color
                        (15,117,188),   #Visl color
                        (219,146,191),   #LGd color
                        (11,149,68)])) #LP color

scene = Scene()
print(scene.atlas.space)
# scene.add(Points(np.array([10000,-10000,10000]),radius=1000)s


scene.add_cells(self, coords, color='red', color_by_region=False,
    color_by_metadata=None, radius=25, res=3, alpha=1, col_names=None,
    regions=None, verbose=True):
# scene.add(Points(np.array([10000,-10000,10000]),radius=1000)s
# for pk in pkls[:1]:
#     print(pk)
#     cells = pkl.load(open(pk,'rb'))
#     for c in cells['data']:
#         print(c)
#         coordinates = np.array([c[0]*1000,c[1]*1000,c[2]*1000])
#         scene.add(Points(coordinates))

# for area in areas:  
#     scene.add_brain_region([area], alpha=.5,color=np.array(np.array(colors[area])/256.).tolist())



scene.content
scene.render()  