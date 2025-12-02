def count_words_characters(string):
    # Count characters
    char_count = 0
    for ch in string:
        if ch != "":  
            char_count += 1
    
    # Count words manually
    word_count = 1 if len(string) > 0 else 0 
    for i in range(len(string)):
        if string[i] == " ":
            word_count += 1

    return word_count, char_count

text = "Hello World Python"
words, chars = count_words_characters(text)
print("String:", text)
print("Number of words:", words)
print("Number of characters:", chars)
