# Write a program to find the longest word in a list of strings.

def find_longest_word(words):
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

w = ["apple", "banana", "cherry", "blueberry", "strawberry", "asdfghjkqwerty"]
print(find_longest_word(w))

