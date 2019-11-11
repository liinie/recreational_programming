# Task: to check if the opened bracket is closed
# pay attention:
# 1. the closing bracket should be after the opening bracket: '][' is not allowed
# 2. the last unclosed bracket should be closed first: '[(])' is not allowed


def is_matched(input_text):
    opening = '([{'
    closing = ')]}'
    mapping = dict(zip(opening, closing))

    matching_bracket_lst = []

    for letter in input_text:
        print(letter)
        if letter in opening:
            matching_bracket_lst.append(mapping[letter])
            print(matching_bracket_lst)

        elif letter in closing:
            if matching_bracket_lst and letter == matching_bracket_lst[-1]:
                matching_bracket_lst.remove(letter)
            else:
                return False

    return not matching_bracket_lst


if __name__ == '__main__':

    input_text_1 = '[[()]]'
    print(is_matched(input_text_1))


