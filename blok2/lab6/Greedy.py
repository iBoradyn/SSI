import math

import numpy as np
from matplotlib import pyplot as plt


class Greedy:
    def __init__(self, bitmaps: dict[int: list[list]] = None):
        if not bitmaps:
            self.bitmaps = {
                1: [
                    [0, 0, 0, 1],
                    [0, 0, 1, 1],
                    [0, 1, 0, 1],
                    [0, 0, 0, 1],
                    [0, 0, 0, 1],
                ],
                2: [
                    [0, 1, 1, 1],
                    [1, 0, 0, 1],
                    [0, 0, 1, 0],
                    [0, 1, 0, 0],
                    [1, 1, 1, 1],
                ],
                3: [
                    [1, 1, 1, 0],
                    [0, 0, 0, 1],
                    [1, 1, 1, 1],
                    [0, 0, 0, 1],
                    [1, 1, 1, 0],
                ],
            }
        else:
            self.bitmaps = bitmaps

    def calc_measure(self, ba, bb):
        measure = 0

        for pay in range(len(ba)):
            for pax in range(len(ba[pay])):
                if ba[pay][pax] == 1:
                    min_dist = 9999999
                    for pby in range(len(bb)):
                        for pbx in range(len(bb[pby])):
                            if bb[pby][pbx] == 1:
                                dist_now = abs(
                                    math.dist((pax, pay), (pbx, pby)),
                                )
                                min_dist = min(min_dist, dist_now)
                    measure += min_dist

        return measure

    def compare(self, bitmap: list[list]):
        max_key = None
        max_measure = -9999999

        for i, ba in self.bitmaps.items():
            measure = -(self.calc_measure(ba, bitmap) + self.calc_measure(bitmap, ba))

            if max_measure < measure:
                max_measure = measure
                max_key = i

        return max_key, max_measure


greedy_algorithm = Greedy()

bitmap_1 = [
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
]
bitmap_2 = [
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
]
bitmap_3 = [
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1],
]


bitmap_1_result = greedy_algorithm.compare(bitmap_1)
bitmap_2_result = greedy_algorithm.compare(bitmap_2)
bitmap_3_result = greedy_algorithm.compare(bitmap_3)

print(f'Bitmap 1:{bitmap_1_result}')
print(f'Bitmap 2:{bitmap_2_result}')
print(f'Bitmap 3:{bitmap_3_result}')


test_bitmaps = [bitmap_1, bitmap_2, bitmap_3]
results = [bitmap_1_result, bitmap_2_result, bitmap_3_result]
# results = [ for x, _ in results]

fig, axs = plt.subplots(3, 2)
fig.tight_layout(pad=1.2)

for i, bitmap in enumerate(test_bitmaps):
    axs[i][0].set_title(f'Obraz testowy nr. {i+1}')

    image_before = np.array(bitmap).reshape(5, 4)
    image_before = np.expand_dims(image_before, axis=-1)
    axs[i][0].imshow(image_before, cmap=plt.get_cmap('gray'))

for i, (x, result) in enumerate(results):
    axs[i][1].set_title(f'Dopasowany obraz nr. {x}')

    image_before = np.array(greedy_algorithm.bitmaps[x]).reshape(5, 4)
    image_before = np.expand_dims(image_before, axis=-1)
    axs[i][1].imshow(image_before, cmap=plt.get_cmap('gray'))

plt.show()
