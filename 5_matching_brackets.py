# coding=utf-8

# 1. Nesting depth and its location
#       - Longest stream of 2s and its location
# 2. Maximum number of chars between matching pairs and their location
#       - Think

def longest_stream(string):
    """ Finds the longest stream of 2s in a given string """
    location = 0
    length = 0
    max_length = 0

    for i, digit in enumerate(string):

        if digit == '2':
            length += 1

            if length > max_length:
                max_length = length
                location = i

        else:
            length = 0

    return {"nesting-depth": max_length, "location": location-1}

if __name__ == '__main__':

    print longest_stream(raw_input().strip().split())
