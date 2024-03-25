import random
import numpy as np

from brainrender import Scene
from brainrender.actors import Points

from rich import print
from myterial import orange
from pathlib import Path
import glob
import pickle5 as pkl

pkls = glob.glob('/Users/danieljdenman/Desktop/G17_Cells/cell*.pkl')
coordinates = []
for pk in pkls:
    print(pk)
    cells = pkl.load(open(pk,'rb'))
    for c in cells['data']:
        coords = [13000 + c[1]*10 - 2500,c[2]*-10 + 500,11400/2-c[0]*10]
        coordinates.append(coords)

print(f"[{orange}]Running example: {Path(__file__).name}")


def get_n_random_points_in_region(region, N):
    """
    Gets N random points inside (or on the surface) of a mes
    """

    region_bounds = region.mesh.bounds()
    X = np.random.randint(region_bounds[0], region_bounds[1], size=10000)
    Y = np.random.randint(region_bounds[2], region_bounds[3], size=10000)
    Z = np.random.randint(region_bounds[4], region_bounds[5], size=10000)
    pts = [[x, y, z] for x, y, z in zip(X, Y, Z)]

    ipts = region.mesh.insidePoints(pts).points()
    return np.vstack(random.choices(ipts, k=N))


scene = Scene(title="Labelled cells")

# Get a numpy array with (fake) coordinates of some labelled cells
mos = scene.add_brain_region("VISp", alpha=0.15)
coordinates2 = get_n_random_points_in_region(mos, 2000)
print(np.array(coordinates))

# Add to scene
scene.add(Points(np.array(coordinates), name="CELLS", colors="steelblue"))

# render
scene.content
print(scene.atlas.space)
scene.render()