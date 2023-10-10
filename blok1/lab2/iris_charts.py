import re

import matplotlib.pyplot as plt

from blok1.lab1.readers import AttributesReader
from blok1.lab1.readers import SamplesReader


sr = SamplesReader('iris.txt')
ar = AttributesReader('iris-type.txt')

fig, axs = plt.subplots(2, 2)

labels = list(map(lambda x: x[1:], re.findall(r'=[a-zA-Z]*', ar.get_attr_name(4))))
filtered_samples = [
    sr.samples.filter(like='1', axis=0),
    sr.samples.filter(like='2', axis=0),
    sr.samples.filter(like='3', axis=0),
]

list_x_0_0 = [
    filtered_samples[0][2],
    filtered_samples[1][2],
    filtered_samples[2][2],
]
list_y_0_0 = [
    filtered_samples[0][3],
    filtered_samples[1][3],
    filtered_samples[2][3],
]
axs[0, 0].plot(list_x_0_0[0], list_y_0_0[0], 'ro')
axs[0, 0].plot(list_x_0_0[1], list_y_0_0[1], 'go')
axs[0, 0].plot(list_x_0_0[2], list_y_0_0[2], 'bo')
axs[0, 0].set_xlabel(ar.get_attr_name(2))
axs[0, 0].set_ylabel(ar.get_attr_name(3))
axs[0, 0].set_title('Fig 1')


list_x_0_1 = [
    filtered_samples[0][1],
    filtered_samples[1][1],
    filtered_samples[2][1],
]
list_y_0_1 = [
    filtered_samples[0][3],
    filtered_samples[1][3],
    filtered_samples[2][3],
]
axs[0, 1].plot(list_x_0_1[0], list_y_0_1[0], 'ro')
axs[0, 1].plot(list_x_0_1[1], list_y_0_1[1], 'go')
axs[0, 1].plot(list_x_0_1[2], list_y_0_1[2], 'bo')
axs[0, 1].set_xlabel(ar.get_attr_name(1))
axs[0, 1].set_ylabel(ar.get_attr_name(3))
axs[0, 1].set_title('Fig 2')


list_x_1_0 = [
    filtered_samples[0][0],
    filtered_samples[1][0],
    filtered_samples[2][0],
]
list_y_1_0 = [
    filtered_samples[0][3],
    filtered_samples[1][3],
    filtered_samples[2][3],
]
axs[1, 0].plot(list_x_1_0[0], list_y_1_0[0], 'ro')
axs[1, 0].plot(list_x_1_0[1], list_y_1_0[1], 'go')
axs[1, 0].plot(list_x_1_0[2], list_y_1_0[2], 'bo')
axs[1, 0].set_xlabel(ar.get_attr_name(0))
axs[1, 0].set_ylabel(ar.get_attr_name(3))
axs[1, 0].set_title('Fig 3')


list_x_1_1 = [
    filtered_samples[0][1],
    filtered_samples[1][1],
    filtered_samples[2][1],
]
list_y_1_1 = [
    filtered_samples[0][2],
    filtered_samples[1][2],
    filtered_samples[2][2],
]
axs[1, 1].plot(list_x_1_1[0], list_y_1_1[0], 'ro')
axs[1, 1].plot(list_x_1_1[1], list_y_1_1[1], 'go')
axs[1, 1].plot(list_x_1_1[2], list_y_1_1[2], 'bo')
axs[1, 1].set_xlabel(ar.get_attr_name(1))
axs[1, 1].set_ylabel(ar.get_attr_name(2))
axs[1, 1].set_title('Fig 4')

fig.tight_layout(pad=2)
fig.legend(labels=labels, loc='center')

plt.show()
