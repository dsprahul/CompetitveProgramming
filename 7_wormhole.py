from collections import defaultdict
from bisect import bisect
from itertools import product

# Know scale of inputs
N, X, Y = map(int, input().split())

# Collect inputs
exams = []
for i in range(N):
    S, E = map(int, input().split())
    exams.append([S, E])

W = list(map(int, input().split()))
V = list(map(int, input().split()))


class BinaryTable(object):

    def __init__(self):
        rows = 10**5  # Worst case length
        cols = 10**5  # Worst case length
        self.table = []
        for i in range(rows):
            self.table.append([0] * cols)

        self.S = dict()
        selt.dT = dict()
        self.s_idx = 0
        self.dt_idx = 0

    def set(self, s, dt):
        self.S[s] = self.s_idx
        self.dT[dt] = self.dt_idx

        self.table[self.s_idx, self.dt_idx] = 1

        self.s_idx += 1
        self.dt_idx += 1

    def get(self, s, dt):
        if s not in self.S:
            return 0

        if dt not in self.dT:
            return 0

        return self.data[self.S[s], self.dT[dt]]

    @property
    def get_all_start_times(self):
        return self.S.keys()

    @property
    def get_all_dts(self):
        return self.dT.keys()


def minimum_time_spent(exams, W, V):

    # exams = sorted(exams, key=lambda i_: i_[0])
    bt = BinaryTable()
    for s, e in exams:
        bt.set(s=s, dt=e-s)

    product_WV = product(W, V)
    product_WV = sorted(product_WV, key=lambda exam: exam[1] - exam[0])

    def next_smallest_exam_set(sorted_known_dts, current_dt):
        these_exams = []
        idx = bisect(sorted_known_dts, current_dt)
        for dt_key in sorted_known_dts[:idx]:
            these_exams += exams_by_duration[dt_key]

        return these_exams

    for w, v in product_WV:
        dt = v - w

        if dt < 0:  # Such combinations are not commutable
            continue

        # There maybe some exams that could fit in this duration,
        # check if their start & end time lies with-in <dt>
        # Get a list of exams such that w <= s < w + dt && t <= dt


if __name__ == "__main__":
    print(minimum_time_spent(exams, W, V))
