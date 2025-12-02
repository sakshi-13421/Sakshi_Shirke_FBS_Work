def group_anagrams(words):
    groups = {}
    for w in words:
        key = "".join(sorted(w))   # sort करून key बनवतो
        if key in groups:
            groups[key].append(w)
        else:
            groups[key] = [w]
    return list(groups.values())

words = ["bat", "tab", "eat", "tea", "tan", "nat"]
print("Grouped anagrams:", group_anagrams(words))
