first_line = input()
N, K = map(int, first_line.split())
list_ = map(int, input().split())


# 1. Sort the list in descending order to avoid using mod operator
list_ = sorted(list_)

# 2. Starting from first element, compare along the length of the list
#    to count number of pairs satisfying |i-j| >= K

variation_count = 0
S = 1
for i in range(N):
    for j in range(S, N):
        if list_[j] - list_[i] >= K:
            variation_count += N - j
            S = j
            break

print(variation_count)
