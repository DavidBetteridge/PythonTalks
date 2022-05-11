from typing import Final
import matplotlib.pyplot as plt
import numpy as np

# Note, for now all these numbers need to be the same! If this becomes a 
# problem then we will need to add some scaling into the add cube method
NUMBER_OF_TIME_SLICES: Final = 5
NUMBER_OF_FEATURES: Final = 5
NUMBER_OF_CUSTOMERS: Final = 5

class CustomerSize:
  VerySmall = 1
  Small = 2
  Medium = 3
  Large = 4
  ExtraLarge = 5

alpha = 1

# Needs to have one entry per customer.  RBG values are between 0 and 1
# (Sky Crusie and Travel Color Palette)
colours = [
  [80/255,201/255,247/255,alpha],
  [6/255,178/255,244/255,alpha],
  [7/255,131/255,183/255,alpha],
  [15/255,85/255,119/255,alpha],
  [8/255,64/255,89/255,alpha],
]

def colour_for_customer(customer_number):
  if customer_number+1 >= len(colours):
    raise Exception("Please add more entries to the colours list.")
  return colours[customer_number]

def add_cube(usage_height,
             data, colors, t,
             customer_number,
             feature_number,
             size):
  # Each time slice is 'ExtraLarge' rows followed by a blank
  time_offset = t * (CustomerSize.ExtraLarge+1)

  # Each feature slice is 'ExtraLarge' rows followed by a blank
  feature_offset = feature_number * (CustomerSize.ExtraLarge+1)

  # Each customer is stacked on top of the previous customer for this t/feature.
  usage_offset = usage_height[t][feature_number]
  usage_height[t][feature_number] = usage_height[t][feature_number] + size

  # Each customer has their own color
  colour = colour_for_customer(customer_number)

  for t_offset in range(size):
    for f_offset in range(size):
      for u_offset in range(size):
        data[time_offset+t_offset][feature_offset+f_offset][usage_offset+u_offset] = True
        colors[time_offset+t_offset][feature_offset+f_offset][usage_offset+u_offset] = colour


# Create axis (time x feature x usage)
axes = [NUMBER_OF_TIME_SLICES * (CustomerSize.ExtraLarge + 1),
        NUMBER_OF_FEATURES * (CustomerSize.ExtraLarge + 1),
        NUMBER_OF_CUSTOMERS * (CustomerSize.ExtraLarge + 1)]

# Create Data
data = np.zeros(axes, dtype=np.bool8)

# Usage height
usage_height = np.zeros([NUMBER_OF_TIME_SLICES, NUMBER_OF_FEATURES], dtype=np.int32)


# Control colour
colors = np.empty(axes + [4], dtype=np.float32)

# One feature, low usage at t=0
add_cube(usage_height, data, colors, t=0, customer_number=0, feature_number=0, size=CustomerSize.Small)

# Two features, low usage at t=1
add_cube(usage_height, data, colors, t=1, customer_number=0, feature_number=0, size=CustomerSize.Medium)
add_cube(usage_height, data, colors, t=1, customer_number=0, feature_number=1, size=CustomerSize.Small)

# Two features, more usage at t=2
add_cube(usage_height, data, colors, t=2, customer_number=0, feature_number=0, size=CustomerSize.ExtraLarge)
add_cube(usage_height, data, colors, t=2, customer_number=0, feature_number=1, size=CustomerSize.Small)
add_cube(usage_height, data, colors, t=2, customer_number=1, feature_number=1, size=CustomerSize.Small)


# More features, more usage at t=3
add_cube(usage_height, data, colors, t=3, customer_number=0, feature_number=0, size=CustomerSize.Small)
add_cube(usage_height, data, colors, t=3, customer_number=0, feature_number=1, size=CustomerSize.Medium)
add_cube(usage_height, data, colors, t=3, customer_number=1, feature_number=1, size=CustomerSize.Small)
add_cube(usage_height, data, colors, t=3, customer_number=2, feature_number=1, size=CustomerSize.Medium)
add_cube(usage_height, data, colors, t=3, customer_number=3, feature_number=1, size=CustomerSize.Small)
add_cube(usage_height, data, colors, t=3, customer_number=0, feature_number=2, size=CustomerSize.Small)

# Plot figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.voxels(data, facecolors=colors, edgecolors=colors)
ax.set_xlabel('time')
ax.set_ylabel('features')
ax.set_zlabel('usage')
ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])
ax.axes.zaxis.set_ticks([])
plt.show()