# coding=utf-8
from collections import defaultdict

N1, N2, N3 = map(int, raw_input().split())

id_frequencies = defaultdict(int)

for _ in range(N1 + N2 + N3):
    id_frequencies[int(raw_input())] += 1

final_list = sorted([ID for ID, freq in id_frequencies.iteritems() if freq > 1])

print(len(final_list))
for ID in final_list:
    print(ID)
