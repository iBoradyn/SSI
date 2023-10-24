import math
import random

from blok1.lab1.readers import SamplesReader
import matplotlib.pyplot as plt


class KMeans:
    def __init__(self, samples_filename, m, iters, groups_colors=None):
        if groups_colors is None:
            groups_colors = ['yellow', 'green', 'blue', 'cyan']

        self.samples = SamplesReader(samples_filename).samples
        self.m = m
        self.iters = iters
        self.groups_colors = groups_colors

        self.learn()

    def get_random_means(self) -> {int: (float, float)}:
        samples_list = list(zip(self.samples[0], self.samples[1]))
        result = {}

        for i in range(self.m):
            j = random.randint(0, len(samples_list)-1)
            result[i] = samples_list[j]

        return result

    def plot_samples(self, ax, V, groups):
        for x_index, X_gr in groups.items():
            if not X_gr:
                continue
            points_separated = list(zip(*X_gr))
            points_x = points_separated[0]
            points_y = points_separated[1]
            ax.plot(points_x, points_y, 'o', color=self.groups_colors[x_index])

        for v_index, v_point in V.items():
            x = v_point[0]
            y = v_point[1]
            ax.plot(x, y, 'r*')

    def learn(self):
        V = self.get_random_means()

        fig, axs = plt.subplots(2, 1)
        fig.tight_layout(pad=2.5)
        axs[0].set_xlabel('x')
        axs[0].set_ylabel('y')
        axs[0].set_title('Pierwsza interacja')
        axs[1].set_xlabel('x')
        axs[1].set_ylabel('y')
        axs[1].set_title('Po 100 iteracjach')

        for iter_i in range(self.iters):
            groups = {x: [] for x in V}
            for s_index, sample in self.samples.iterrows():
                point = (sample[0], sample[1])
                min_index = 0
                min_range = 999999999
                for v_index, v_point in V.items():
                    new_range = abs(math.dist(point, v_point))
                    if min_range > new_range:
                        min_index = v_index
                        min_range = new_range
                groups[min_index].append(point)

            if iter_i == 0:
                self.plot_samples(axs[0], V, groups)
            elif iter_i == self.iters-1:
                self.plot_samples(axs[1], V, groups)

            for x_index, X_gr in groups.items():
                if not X_gr:
                    continue

                points_separated = list(zip(*X_gr))
                points_x = points_separated[0]
                points_y = points_separated[1]
                V[x_index] = (
                        sum(points_x) / len(points_x),
                        sum(points_y) / len(points_y),
                )
        labels = [f'Grupa {i}' for i in range(1, self.m+1)] + ['Środek grupy']
        # Shrink current axis by 20%
        for ax in axs:
            box = ax.get_position()
            ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

        fig.legend(labels=labels, loc='center right')
        plt.show()


KMeans('spirala.txt', 4, 100)
