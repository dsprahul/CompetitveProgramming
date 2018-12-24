import random

input_list = [random.randint(1, 10000) for i in range(1000000)]


def quick_sort(list):

    if len(list) < 2:
        return list

    pivot = random.choice(list)
    list.remove(pivot)

    left = []
    right = []
    for element in list:
        if element > pivot:
            right.append(element)
        else:
            left.append(element)

    left = quick_sort(left)
    right = quick_sort(right)
    output = left + [pivot] + right

    return output


assert sorted(input_list) == quick_sort(input_list)
