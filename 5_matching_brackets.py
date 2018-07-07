# coding=utf-8


ONE = '('
TWO = ')'

ONE = '1'
TWO = '2'


def nested_depth_and_point_of_occr(stream):

    N = len(stream)
    cur_max_len = 0
    cur_start_loc = 0

    cur_len = 0
    change_start_loc = False

    for idx in range(N):

        if stream[idx] == ONE:
            cur_len += 1

            if cur_len > cur_max_len:
                change_start_loc = True
                cur_max_len = cur_len

        if stream[idx] == TWO:
            if change_start_loc is True:
                cur_start_loc = idx

            cur_len = 0
            change_start_loc = False

    return cur_max_len, cur_start_loc


def len_of_max_sequence_and_point_of_occr(stream):

    N = len(stream)
    list_of_braces_meta = []

    longest_known = 0
    longest_known_loc = 0

    for idx in range(N):

        if stream[idx] == ONE:

            bracket_object = {
                "location": idx,
                "containing-length": 0
            }
            list_of_braces_meta.append(bracket_object)

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

    return longest_known, longest_known_loc + 1


if __name__ == "__main__":
    N = int(raw_input())
    input_stream = raw_input()
    cleaned_stream = ''.join(input_stream.split())

    depth, depth_occured_at = nested_depth_and_point_of_occr(cleaned_stream)
    longest_enclosure, enc_occured_at = len_of_max_sequence_and_point_of_occr(cleaned_stream)

    print('{} {} {} {}'.format(
        depth, depth_occured_at, longest_enclosure, enc_occured_at
    ))
