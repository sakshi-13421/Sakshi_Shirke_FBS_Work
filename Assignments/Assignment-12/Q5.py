def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0

    for i in range(len(string)):
        for j in range(len(vowels)):
            if string[i] == vowels[j]:
                count = count + 1
                break  

    return count

text = "Hello World"
vowel_count = count_vowels(text)

print("String:", text)
print("Number of vowels:", vowel_count)
