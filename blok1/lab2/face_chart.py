import math

import matplotlib.pyplot as plt
import numpy as np

circle = plt.Circle((0, 0), 2, color='r', fill=False)

fig, ax = plt.subplots()

ax.add_patch(circle)
circle_legend = ax.plot(0, 0, color='r', label='lamane')
eye1 = ax.plot(-1, 1, 'bD', label='punkty')
eye2 = ax.plot(1, 1, 'bD')
nose = ax.plot(0, 0, 'bD')

x = np.linspace(-1, 1)
y = -np.sqrt(1 - x ** 2)
mouth = plt.plot(x, y, 'y', label='sinus')

ax.set_xticks([-2, -1, 0, 1, 2])
ax.set_yticks([-3, -2, -1, 0, 1, 2, 3])
ax.tick_params(axis='both', which='major', pad=15)
ax.grid()

# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1))

plt.show()
