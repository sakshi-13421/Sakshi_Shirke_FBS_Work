def word_count(string):
    words = []
    word = ""
    counts = []

    for ch in string + " ":
        if ch != " ":
            word += ch
        else:
            if word != "":
                words.append(word)
                word = ""

    for w in words:
        c = 0
        for x in words:
            if w == x:
                c += 1
        if [w, c] not in counts:
            counts.append([w, c])

    return counts

s = input("Enter a string: ")
print("Word Occurrences:")
for w, c in word_count(s):
    print(w, ":", c)
