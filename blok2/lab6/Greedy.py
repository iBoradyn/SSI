import math


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
