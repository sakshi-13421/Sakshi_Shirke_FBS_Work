def longest_common_prefix(strings):
    if not strings:
        return ""
    prefix = ""
    for i in range(len(strings[0])):
        char_set = set()
        for word in strings:
            if i < len(word):
                char_set.add(word[i])
            else:
                return prefix
        if len(char_set) == 1:
            prefix += strings[0][i]
        else:
            break
    return prefix

words = ["flower", "flow", "flight"]
print("Longest Common Prefix:", longest_common_prefix(words))
