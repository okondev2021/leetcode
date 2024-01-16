def longest_common_prefix(strs: list):
    if len(strs) < 1:
        return ""

    strs.sort(key=lambda x: len(x))
    shortest_char = strs[0]
    index_position = 0
    stack = list()

    while index_position < len(shortest_char):

        string_stack = str()

        for char in strs:
            string_stack += char[index_position]

        if len(set(string_stack)) == 1:
            stack.append(string_stack[0])
        else:
            if len(stack) > 0:
                return "".join(stack)
            else:
                return ""
        index_position = index_position + 1
    return "".join(stack)


print(longest_common_prefix(['at']))

