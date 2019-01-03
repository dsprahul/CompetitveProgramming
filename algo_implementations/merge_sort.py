import random

input_list = [random.randint(1, 10000) for i in range(100)]


def mergesort(arr):

    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    a = mergesort(arr[:middle])
    b = mergesort(arr[middle:])

    return merge(a, b)


def merge(a, b):
    c = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    c += a
    c += b

    return c


assert(sorted(input_list) == mergesort(input_list))
