import math
import random
from typing import Callable
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import LightSource
from matplotlib.ticker import LinearLocator


class Fireflies:
    def __init__(self, N, beta0, gamma0, mu0, x_min, x_max, iters):
        self.N = N
        self.beta0 = beta0
        self.gamma0 = gamma0
        self.mu0 = mu0
        self.x_min = x_min
        self.x_max = x_max
        self.iters = iters

        self.gamma = gamma0/x_max
        self.mu = [(x_max-x_min)*mu0] * N

    def simulate(self, F: Callable, n: int):
        X = [
            [random.uniform(self.x_min, self.x_max) for _ in range(n)]
            for _ in range(self.N)
        ]

        for _ in range(self.iters):
            ratings = list(map(lambda x: F(*x), X))

            for a in random.sample(range(self.N), self.N):
                for b in random.sample(range(self.N), self.N):
                    if ratings[b] > ratings[a]:
                        beta = self.beta0 * pow(
                            math.e,
                            -self.gamma*pow(math.dist(X[a], X[b]), 2),
                        )

                        for i in range(n):
                            X[a][i] += beta * (X[b][i] - X[a][i])
                        ratings[a] = F(*X[a])

                for i in range(n):
                    X[a][i] += random.uniform(-self.mu[i], self.mu[i])
                ratings[a] = F(*X[a])

        self.plot3D(F, X)

    def plot3D(self, F: Callable, X: list):
        fig, axs = plt.subplots(3, 2, subplot_kw={"projection": "3d"})

        # Make data.
        x = np.arange(self.x_min, self.x_max, .25)
        y = np.arange(self.x_min, self.x_max, .25)
        x, y = np.meshgrid(x, y)

        z = np.array(list(map(lambda x, y: F(x, y), x, y)))

        x_flies = list(zip(*X))[0]
        y_flies = list(zip(*X))[1]
        z_flies = list(map(lambda x, y: F(x, y), x_flies, y_flies))

        # Plot the surface.
        for i in range(3):
            for j in range(2):
                axs[i][j].scatter(
                    x_flies, y_flies, z_flies, color='green', s=50,
                )
                surf = axs[i][j].plot_surface(
                    x, y, z, cmap=cm.coolwarm, linewidth=2, antialiased=False,
                )

                # fig.colorbar(surf, shrink=0.5, aspect=5)

        fig.subplots_adjust(right=0.8)
        cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
        fig.colorbar(surf, cax=cbar_ax)
        fig.legend(labels=['Fireflies'])

        axs[0][0].view_init(30, 0)
        axs[0][1].view_init(30, 60)
        axs[1][0].view_init(30, 120)
        axs[1][1].view_init(30, 180)
        axs[2][0].view_init(30, 240)
        axs[2][1].view_init(30, 300)

        plt.show()


def func(x1, x2):
    return np.sin(x1*0.05)+np.sin(x2*0.05)+0.4*np.sin(x1*0.15)*np.sin(x2*0.15)


Fireflies(4, 0.3, 0.1, 0.05, 0, 100, 30).simulate(func, 2)
