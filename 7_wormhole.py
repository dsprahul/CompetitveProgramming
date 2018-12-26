from collections import defaultdict

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
        for idx, dt in enumerate(sorted_known_dts):
            if dt > current_dt:
                return exams_by_duration[sorted_known_dts[idx - 1]]

    for w, v in product(W, V):
        dt = v - w

        if dt < 0:  # Such combinations are not commutable
            continue

        if exams_by_duration.get(dt) is None:
            try:
                existing_dts_ascending = sorted(list(exams_by_duration.keys()))
                these_exams = next_smallest_exam_set(
                    sorted_known_dts=existing_dts_ascending,
                    current_dt=dt
                )
            except IndexError:
                continue
        else:
            these_exams = exams_by_duration[dt]

        # There are some exams that could fit in this duration,
        # check if the start & end time lies with-in <dt>
        for s, e in these_exams:  # If exits without returing, try next dt combo
            if s + dt <= v:
                return dt + 1


if __name__ == "__main__":
    minimum_time_spent(exams, W, V)
