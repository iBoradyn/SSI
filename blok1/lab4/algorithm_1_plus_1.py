import math
from typing import Callable
import random
import matplotlib.pyplot as plt
import numpy as np


class OnePlusOne:
    def __init__(self, init_scatter, growth_factor, iters):
        self.init_scatter = init_scatter
        self.growth_factor = growth_factor
        self.iters = iters

    def find_extremum(self, function: Callable, func_range: tuple[float, float]):
        x = random.uniform(func_range[0], func_range[1])
        y = function(x)
        scatter = self.init_scatter
        min_point = min(func_range)
        max_point = max(func_range)

        fig, ax = plt.subplots()

        for i in range(self.iters):
            x_pot = x + random.uniform(-scatter, scatter)
            if x_pot > max_point:
                x_pot = max_point
            elif x_pot < min_point:
                x_pot = min_point

            y_pot = function(x_pot)

            if y_pot >= y:
                x = x_pot
                y = y_pot
                scatter *= self.growth_factor
            else:
                scatter /= self.growth_factor

            print(f'{i}: {x}, {y} - {scatter}')

        x_points = np.linspace(min_point, max_point, int(max_point-min_point))
        y_points = list(map(function, x_points))
        ax.plot(x_points, y_points, 'b-')
        ax.plot(x, y, 'ro')

        labels = ['Funkcja', 'Ekstremum']

        fig.legend(labels=labels, loc='upper right')
        plt.show()

        return x, y


def func(x):
    return math.sin(x/10) * math.sin(x/200)

alg = OnePlusOne(10, 1.1, 100)
alg.find_extremum(func, (0, 100))
