import math
import random

from blok1.lab1.readers import SamplesReader
from blok1.lab1.readers import AttributesReader
import matplotlib.pyplot as plt


class FCM:
    def __init__(
            self,
            samples_filename,
            attributes_filename,
            m,
            iters,
            fcm_m=2,
            groups_colors=None,
            min_d_val=1e-10,
    ):
        if groups_colors is None:
            groups_colors = ['red', 'green', 'blue']
        if fcm_m <= 1:
            raise AttributeError('fcm_m must be greater than 1!')

        self.samples = SamplesReader(samples_filename).samples
        self.attributes = AttributesReader(attributes_filename).attributes
        self.m = m
        self.iters = iters
        self.fcm_m = fcm_m
        self.groups_colors = groups_colors
        self.min_d_val = min_d_val

        self.learn()

    def plot_samples(self, ax, u, v):
        for i, v_point in enumerate(v):
            x = v_point[0]
            y = v_point[1]
            ax.plot(x, y, '*', color=self.groups_colors[i])

        colors = list(zip(*u))
        colors = [[x for x in y] for y in colors]
        ax.scatter(self.samples[0], self.samples[1], c=colors)

    def calc_U(self, u, d, samples_size):
        for i in range(self.m):
            for j in range(samples_size):
                D_sum = 0
                for k in range(self.m):
                    D_sum += pow(d[k][j], 1/(1-self.fcm_m))

                u[i][j] = pow(d[i][j], 1/(1-self.fcm_m))/D_sum

        return u

    def calc_V(self, v, u, samples_size, attributes_size):
        for i in range(self.m):
            for j in range(attributes_size):
                U_x_sum = sum([
                    pow(u[i][s], self.fcm_m)*self.samples.at[s, j]
                    for s in range(samples_size)
                ])
                U_sum = sum([
                    pow(u[i][s], self.fcm_m)
                    for s in range(samples_size)
                ])
                v[i][j] = U_x_sum/U_sum

        return v

    def calc_D(self, d, v, samples_size):
        for i in range(self.m):
            for j in range(samples_size):
                d[i][j] = pow(math.dist(
                    tuple(self.samples.loc[j]),
                    tuple(v[i]),
                ), 2)

                if d[i][j] < self.min_d_val:
                    d[i][j] = self.min_d_val

        return d

    def learn(self):
        samples_size = self.samples[0].size
        attributes_size = self.attributes[0].size

        U = [[None for _ in range(samples_size)] for _ in range(self.m)]
        D = [[random.random() for _ in range(samples_size)] for _ in range(self.m)]
        V = [[None for _ in range(attributes_size)] for _ in range(self.m)]

        fig, axs = plt.subplots(2, 1)
        fig.tight_layout(pad=2.5)
        axs[0].set_xlabel('x')
        axs[0].set_ylabel('y')
        axs[0].set_title('Pierwsza interacja')
        axs[1].set_xlabel('x')
        axs[1].set_ylabel('y')
        axs[1].set_title(f'Po {self.iters} iteracjach')

        U = self.calc_U(U, D, samples_size)
        V = self.calc_V(V, U, samples_size, attributes_size)

        self.plot_samples(axs[0], U, V)

        for iter_i in range(self.iters):
            D = self.calc_D(D, V, samples_size)
            U = self.calc_U(U, D, samples_size)

            if iter_i == self.iters-1:
                self.plot_samples(axs[1], U, V)

            V = self.calc_V(V, U, samples_size, attributes_size)

        labels = [f'Grupa {i}' for i in range(1, self.m+1)]
        # Shrink current axis by 20%
        for ax in axs:
            box = ax.get_position()
            ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

        fig.legend(labels=labels, loc='center right')
        plt.show()


FCM('spirala.txt', 'spirala-type.txt', 3, 10)
