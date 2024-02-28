import matplotlib.pyplot as plt

from rw_stocks import Randomwalk

#RW1
rw = Randomwalk(500)
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)

#RW2
rw2 = Randomwalk(500)
rw2.fill_walk()
point_numbers = range(rw2.num_points)
ax.scatter(rw2.x_values, rw2.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=5)

#RW3
rw3 = Randomwalk(500)
rw3.fill_walk()
point_numbers = range(rw3.num_points)
ax.scatter(rw3.x_values, rw3.y_values, c=point_numbers, cmap=plt.cm.Greens, edgecolors='none', s=5)

#RW4
rw4 = Randomwalk(500)
rw4.fill_walk()
point_numbers = range(rw4.num_points)
ax.scatter(rw4.x_values, rw4.y_values, c=point_numbers, cmap=plt.cm.cool, edgecolors='none', s=5)

ax.get_xaxis().set_visible(True)
ax.get_yaxis().set_visible(True)

plt.show()