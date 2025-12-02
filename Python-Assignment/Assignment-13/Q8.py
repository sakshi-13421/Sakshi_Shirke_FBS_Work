def word_frequency(s):
    words = []
    word = ""
    freq = {}

    for ch in s + " ":
        if ch != " ":
            word += ch
        else:
            if word != "":
                words.append(word)
                word = ""

    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    return freq

s = input("Enter a string: ")
print("Word frequency:", word_frequency(s))
