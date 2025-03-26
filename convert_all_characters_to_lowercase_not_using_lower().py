# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# ask user to input a string
string = input("Enter a string: ")

# convert all characters into lowercase
lowercase_string = ''.join([chr(ord(char) + 32) if 'A' <= char <= 'Z' else char for char in string])
print(lowercase_string)