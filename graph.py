# Import libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

alpha = 1


def colour_for_customer(customer_number):
  # Each customer has their own color
  if customer_number == 0:
    return [1, 0, 0, alpha]
  elif customer_number == 1:
    return [0, 1, 0, alpha]
  elif customer_number == 2:
    return [0, 0, 1, alpha]
  else:
    return [1, 1, 1, alpha]

def add_cube(data, colors, t,
             customer_number,
             feature_number):
  # Each time slice is 2 rows followed by a blank
  time_offset = t * 3

  # Each feature slice is 2 rows followed by a blank
  feature_offset = feature_number * 3

  # Each usage slice is the 2 row without a blank.
  # (We assume a customer never stops using a feature!)
  usage_offset = customer_number * 2

  # Each customer has their own color
  colour = colour_for_customer(customer_number)

  for t_offset in range(2):
    for f_offset in range(2):
      for u_offset in range(2):
        data[time_offset+t_offset][feature_offset+f_offset][usage_offset+u_offset] = True
        colors[time_offset+t_offset][feature_offset+f_offset][usage_offset+u_offset] = colour


# Create axis (time x feature x usage)
axes = [20, 20, 20]

# Create Data
data = np.zeros(axes, dtype=np.bool)


# Control colour
colors = np.empty(axes + [4], dtype=np.float32)

# One feature, low usage at t=0
add_cube(data, colors, t=0, customer_number=0, feature_number=0)

# Two features, low usage at t=1
add_cube(data, colors, t=1, customer_number=0, feature_number=0)
add_cube(data, colors, t=1, customer_number=0, feature_number=1)

# Two features, more usage at t=2
add_cube(data, colors, t=2, customer_number=0, feature_number=0)
add_cube(data, colors, t=2, customer_number=0, feature_number=1)
add_cube(data, colors, t=2, customer_number=1, feature_number=1)


# Two features, more usage at t=3
add_cube(data, colors, t=3, customer_number=0, feature_number=0)
add_cube(data, colors, t=3, customer_number=0, feature_number=1)
add_cube(data, colors, t=3, customer_number=1, feature_number=1)
add_cube(data, colors, t=3, customer_number=2, feature_number=1)
add_cube(data, colors, t=3, customer_number=3, feature_number=1)
add_cube(data, colors, t=3, customer_number=0, feature_number=2)

# Plot figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Voxels is used to customizations of
# the sizes, positions and colors.
ax.voxels(data, facecolors=colors, edgecolors=colors)
ax.set_xlabel('time')
ax.set_ylabel('features')
ax.set_zlabel('usage')
ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])
ax.axes.zaxis.set_ticks([])
plt.show()