import math
import random
from typing import Callable
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


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
        x = np.arange(self.x_min, self.x_max, .25)
        y = np.arange(self.x_min, self.x_max, .25)
        x, y = np.meshgrid(x, y)

        z = np.array(list(map(lambda x, y: F(x, y), x, y)))

        x_flies = list(zip(*X))[0]
        y_flies = list(zip(*X))[1]

        fig, ax = plt.subplots()
        CS = ax.contour(x, y, z)
        ax.clabel(CS, inline=True, fontsize=10)
        ax.autoscale(False)
        ax.scatter(
            x_flies, y_flies, color='red', zorder=1,
        )

        fig.legend(labels=['Fireflies'])

        plt.show()


def func(x1, x2):
    return np.sin(x1*0.05)+np.sin(x2*0.05)+0.4*np.sin(x1*0.15)*np.sin(x2*0.15)


Fireflies(4, 0.3, 0.1, 0.05, 0, 100, 30).simulate(func, 2)
