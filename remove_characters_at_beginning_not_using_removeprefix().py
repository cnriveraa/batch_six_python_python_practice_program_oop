# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

# ask user to input a string
string = input("Enter a string: ")

# ask user to input the characters to be removed
characters = input("Characters to be removed: ")

# check if the characters to be removed is at the beginning of the string
if string.startswith(characters):
    # remove the characters at the beginning of the string