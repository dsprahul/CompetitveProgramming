first_line = input()
N, K = map(int, first_line.split())
list_ = map(int, input().split())


# 1. Sort the list in descending order to avoid using mod operator
list_ = sorted(list_, reverse=True)

# 2. Starting from first element, compare along the length of the list
#    to count number of pairs satisfying |i-j| >= K

variation_count = 0
for id_, element in enumerate(list_):
    if id_ + 1 == N - 1:
        continue

    for p, element_along_len in enumerate(list_[id_ + 1:]):
        if element - element_along_len >= K:
            variation_count += (N - 1) - (id_ + p)
            break

print(variation_count)
