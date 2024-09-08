# Write a program to count the number of vowels and consonants in a string.

str = input("enter a string: ")

vowel = "aeiou"
count_vowel = 0
count_consonant = 0

for char in str.lower():
    if char in vowel:
        count_vowel += 1
    elif char not in vowel:
        count_consonant += 1

print(f"count of vowel is {count_vowel}\ncount of consonanat is {count_consonant}")
