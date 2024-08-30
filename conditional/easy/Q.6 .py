# Q. Write a program to check if a given character is a vowel or a consonant.

def character():
    char = input("enter the character: ")
    vowel = "aeiou"
    for i in vowel:
        if i == char:
            print("the given character is a vowel.")
            break
    else:
        print("the given character is a consonant.")
            
character()

