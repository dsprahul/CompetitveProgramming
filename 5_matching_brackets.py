# coding=utf-8


ONE = '('
TWO = ')'

ONE = '1'
TWO = '2'


def logic(stream):

    N = len(stream)
    list_of_braces_meta = []

    deepest_loc = 0
    deepest_known = 0
    longest_known = 0
    longest_known_loc = 0

    for idx in range(N):

        if stream[idx] == ONE:

            bracket_object = {
                "location": idx,
                "containing-length": 0
            }
            list_of_braces_meta.append(bracket_object)

        if len(list_of_braces_meta) > deepest_known:
            # At any point, longest list of open bracket_objects will give
            # right depth, and their location of occurance is obvious
            deepest_known = len(list_of_braces_meta)
            deepest_loc = list_of_braces_meta[-1]["location"]

        if stream[idx] == TWO:
            # This made a pair, pop this open brace from queue
            # Check if the length of popped item > longest_known
            # add 2 to content length of last open brace item after popping
            most_recent_bracket_pair = list_of_braces_meta.pop()

            most_recent_bracket_pair["containing-length"] += 2

            if most_recent_bracket_pair["containing-length"] > longest_known:
                longest_known = most_recent_bracket_pair["containing-length"]
                longest_known_loc = most_recent_bracket_pair["location"]

            if len(list_of_braces_meta) >= 1:
                list_of_braces_meta[-1]["containing-length"] += most_recent_bracket_pair["containing-length"]

    return deepest_known, deepest_loc + 1, longest_known, longest_known_loc + 1


if __name__ == "__main__":
    N = int(raw_input())
    input_stream = raw_input()
    cleaned_stream = ''.join(input_stream.split())

    # depth, depth_occured_at = part_1(cleaned_stream)
    depth, depth_occured_at, longest_enclosure, enc_occured_at = logic(
        cleaned_stream
    )

    print('{} {} {} {}'.format(
        depth, depth_occured_at, longest_enclosure, enc_occured_at
    ))
