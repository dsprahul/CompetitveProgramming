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
        self.table = defaultdict(dict)

    def set(self, s, dt):
        self.table[s].update({dt: 1})

    def get(self, s, dt):
        if self.table.get(s) is None:
            return 0

        if self.table[s].get(dt) is None:
            return 0

        return self.table[s][dt]

    def load_all_start_times(self):
        self.start_times = self.table.keys()

    def load_all_dts(self):
        self.dts = []
        for s in self.start_times:
            self.dts += self.table[s].keys()

    @property
    def get_all_start_times(self):
        try:
            type(self.start_times)
            type(self.dts)
        except AttributeError:
            self.load_all_start_times()
            self.load_all_dts()

        return self.start_times

    @property
    def get_all_dts(self):
        try:
            type(self.start_times)
            type(self.dts)
        except AttributeError:
            self.load_all_start_times()
            self.load_all_dts()

        return self.dts


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

    def in_range_starts(sorted_s, start_s, end_s):
        return [e for e in sorted_s if start_s >= e <= end_s]

    def in_range_dts(sorted_dt, max_dt):
        return [e for e in sorted_dt if e <= max_dt]

    for w, v in product_WV:
        dt = v - w

        if dt < 0:  # Such combinations are not commutable
            continue

        known_s = sorted(bt.get_all_start_times)
        known_dt = sorted(bt.get_all_dts)
        # There maybe some exams that could fit in this duration,
        # check if their start & end time lies with-in <dt>
        # Get a list of exams such that w <= s < w + dt && t <= dt
        starts = in_range_starts(known_s, start_s=w, end_s=w + dt)
        dts = in_range_dts(known_dt, max_dt=dt)
        for s, dt2 in product(starts, dts):
            if bt.get(s, dt2) == 1:
                return dt + 1


if __name__ == "__main__":
    print(minimum_time_spent(exams, W, V))
