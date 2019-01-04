from collections import defaultdict
import heapq

N, M = map(int, input().split())

multiset = defaultdict(int)
for item in list(map(int, input().split())):
    multiset[item] += 1

Q = []
for _ in range(M):
    Q.append(int(input()))


def logn_max(arr):
    '''
    This sucks!
    '''
    length = len(arr)
    mid = length // 2

    if length <= 2:
        return max(arr)

    left = logn_max(arr[:mid])
    right = logn_max(arr[mid:])

    if left > right:
        return left
    else:
        return right


history = dict()
max_steps = max(Q)
for step in range(1, max_steps + 1):
    cur_max = heapq._heapify_max(multiset.keys())
    history[step] = cur_max
    if multiset[cur_max] == 1:
        del multiset[cur_max]
    else:
        multiset[cur_max] -= 1

    cur_max = cur_max // 2
    if cur_max > 0:
        multiset[cur_max] += 1

for q in Q:
    print(history[q])
