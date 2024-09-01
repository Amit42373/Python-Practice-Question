# Write a program to count the number of vowels in a given string.

def count_of_vowel(word):
    vowel = "aeiou"
    word = word.lower()
    count = 0
    for char in  word:
        if char in vowel:
            count += 1
    return count

s = input("enter a word: ")
print(count_of_vowel(s))