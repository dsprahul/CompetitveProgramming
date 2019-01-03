from bisect import bisect_right, bisect_left

# Know scale of inputs
N, X, Y = map(int, input().split())

# Collect inputs
exams = []
for i in range(N):
    S, E = map(int, input().split())
    exams.append([S, E])

W = list(map(int, input().split()))
V = list(map(int, input().split()))

W.sort()
V.sort()

minW = min(W)
maxV = max(V)

minimum_time = 10**5 + 1

for s, e in exams:

    if s < minW or e > maxV:
        continue

    insertion_idx = bisect_right(W, s)
    if insertion_idx < 0:
        continue
    to_wormhole_time = W[insertion_idx - 1]

    insertion_idx = bisect_left(V, e)
    from_wormhole_time = V[insertion_idx]

    if from_wormhole_time - to_wormhole_time < minimum_time:
        minimum_time = from_wormhole_time - to_wormhole_time

print(minimum_time + 1)
