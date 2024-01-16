def longest_common_prefix(strs: list):

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
            index_position = index_position + 1
        else:
            if len(stack) > 0:
                return "".join(stack)
            else:
                return ""


print(longest_common_prefix(["low", "loght"]))

