def word_frequency(strings):
    words = set()
    freq = {}
    for s in strings:
        for word in s.split():
            words.add(word)
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
    return words, freq

lst = ["apple banana", "apple orange", "banana apple"]
unique, freq = word_frequency(lst)
print("Unique words:", unique)
print("Frequency:", freq)
