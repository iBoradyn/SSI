import itertools

import numpy as np
import matplotlib.pyplot as plt


class HopfieldNeuralNetwork:
    def __init__(self, n):
        self.n = n
        self.size = n**2
        self.weights = np.zeros((self.size, self.size))

    def train(self, bitmap):
        try:
            bitmap_flat = [1 if x == 1 else -1 for x in list(itertools.chain(*bitmap))]
        except TypeError:
            bitmap_flat = bitmap.copy()

        if len(bitmap_flat) != self.size:
            raise ValueError("Bitmap size doesn't fit network size")

        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    self.weights[i][j] += (bitmap_flat[i] * bitmap_flat[j])/self.size

    def fixBitmap(self, bitmap, iters=100):
        try:
            bitmap_flat = [1 if x == 1 else -1 for x in list(itertools.chain(*bitmap))]
        except TypeError:
            bitmap_flat = bitmap.copy()

        if len(bitmap_flat) != self.size:
            raise ValueError("Bitmap size doesn't fit network size")

        for _ in range(iters):
            for i in range(self.size):
                sum_value = np.dot(self.weights[i], bitmap_flat)
                if sum_value > 0:
                    bitmap_flat[i] = 1
                elif sum_value < 0:
                    bitmap_flat[i] = -1

        return bitmap_flat


def vector_to_bitmap(bitmap_flat, n):
    return [
        [1 if x == 1 else 0 for x in bitmap_flat[i:i+n]]
        for i in range(0, len(bitmap_flat), n)
    ]


def display_bitmap(bitmap):
    for row in bitmap:
        print(*row)


bitmap_1 = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]
bitmap_2 = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1],
]
bitmap_3 = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
]
test_bitmap_1 = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]
test_bitmap_2 = [
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1],
]
test_bitmap_3 = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
]
test_bitmap_4 = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
]

neural_network = HopfieldNeuralNetwork(5)

for bitmap in [bitmap_1, bitmap_2, bitmap_3]:
    neural_network.train(bitmap)

result_1 = vector_to_bitmap(neural_network.fixBitmap(test_bitmap_1, 1), 5)
result_2 = vector_to_bitmap(neural_network.fixBitmap(test_bitmap_2, 1), 5)
result_3 = vector_to_bitmap(neural_network.fixBitmap(test_bitmap_3, 1), 5)
result_4 = vector_to_bitmap(neural_network.fixBitmap(test_bitmap_4, 1), 5)

test_bitmaps = [test_bitmap_1, test_bitmap_2, test_bitmap_3, test_bitmap_4]
results = [result_1, result_2, result_3, result_4]

fig, axs = plt.subplots(4, 2)
fig.tight_layout(pad=1.2)

for i, bitmap in enumerate(test_bitmaps):
    axs[i][0].set_title(f'Obraz {i+1} przed')

    image_before = np.array(bitmap).reshape(5, 5)
    image_before = np.expand_dims(image_before, axis=-1)
    axs[i][0].imshow(image_before, cmap=plt.get_cmap('gray'))

for i, result in enumerate(results):
    axs[i][1].set_title(f'Obraz {i+1} po')

    image_before = np.array(result).reshape(5, 5)
    image_before = np.expand_dims(image_before, axis=-1)
    axs[i][1].imshow(image_before, cmap=plt.get_cmap('gray'))

plt.show()

print('Bitmap 1 before correction:')
display_bitmap(test_bitmap_1)
print('Bitmap 1 after correction:')
display_bitmap(result_1)

print()

print('Bitmap 2 before correction:')
display_bitmap(test_bitmap_2)
print('Bitmap 2 after correction:')
display_bitmap(result_2)

print()

print('Bitmap 3 before correction:')
display_bitmap(test_bitmap_3)
print('Bitmap 3 after correction:')
display_bitmap(result_3)

print()

print('Bitmap 4 before correction:')
display_bitmap(test_bitmap_4)
print('Bitmap 4 after correction:')
display_bitmap(result_4)
