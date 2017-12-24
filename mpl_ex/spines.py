#!/usr/local/bin/python3.6

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot([-2, 2, 3, 4], [-10, 20, 25, 5])
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.spines['right'].set_visible(False)
ax.yaxis.set_ticks_position('left')

# "outward"
# Move the two remaining spines "out" away from the plot by 10 points
# ax.spines['bottom'].set_position(('outward', 10))
# ax.spines['left'].set_position(('outward', 10))

# "data"
# Have the spines stay intersected at (0, 0)
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# "axes"
# Have the two remaining spines placed at a fraction of the axes
#ax.spines['bottom'].set_position(('axes', 0.75))
#ax.spines['left'].set_position(('axes', 0.3))

plt.show()
