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


def minimum_time_spent(exams, W, V):

    exams = sorted(exams, key=lambda i_: i_[0])
    exams_by_duration = defaultdict(list)
    for s, e in exams:
        exams_by_duration[e - s].append([s, e])  # Appended in increasing order of s

    W.sort()
    V.sort()

    def next_smallest_exam_set(sorted_known_dts, current_dt):
        these_exams = []
        idx = bisect(sorted_known_dts, current_dt)
        for dt_key in sorted_known_dts[:idx]:
            these_exams += exams_by_duration[dt_key]

        return these_exams

    for w, v in product(W, V):
        dt = v - w

        if dt < 0:  # Such combinations are not commutable
            continue

        # There maybe some exams that could fit in this duration,
        # check if their start & end time lies with-in <dt>
        existing_dts_ascending = sorted(list(exams_by_duration.keys()))
        in_range_exams = next_smallest_exam_set(
            sorted_known_dts=existing_dts_ascending,
            current_dt=dt
        )

        # If exits without returing, try next dt combo
        for s, e in in_range_exams:
            if s + dt <= v:
                return dt + 1


if __name__ == "__main__":
    print(minimum_time_spent(exams, W, V))
