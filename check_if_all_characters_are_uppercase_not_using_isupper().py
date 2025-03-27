# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# ask user to input a string
string = input("Enter a string in uppercase: ")

# check if all characters are uppercase
if string == string.upper():
    print("All characters are uppercase.")
else:
    print("Not all characters are uppercase.")