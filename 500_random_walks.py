import matplotlib.pyplot as plt
from rw_stocks import Randomwalk
import random

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))

colormaps = [
    'viridis', 'plasma', 'inferno', 'magma', 'cividis', 
    'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia', 
    'hot', 'afmhot', 'gist_heat', 'copper', 'pink', 'bone', 
    'gray', 'binary', 'gist_yarg', 'gist_gray', 'gray', 
    'afmhot', 'hot', 'gist_heat', 'copper', 'binary'
]

# Plotting multiple random walks
for i in range(1, 500):
    rw = Randomwalk(500)
    rw.fill_walk()
    point_numbers = range(rw.num_points)
    colormap = random.choice(colormaps)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.get_cmap(colormap), edgecolors='none', s=5)

ax.get_xaxis().set_visible(True)
ax.get_yaxis().set_visible(True)

plt.show()