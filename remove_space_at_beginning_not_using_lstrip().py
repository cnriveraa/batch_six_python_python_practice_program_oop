# Prog01. ltrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# ask user to input a string
string = input("Enter a string (add space at the beginning): ")

# remove space at the beginning of the string
removed_space = ' '.join(string.split())
print("Begining space removed:", removed_space)