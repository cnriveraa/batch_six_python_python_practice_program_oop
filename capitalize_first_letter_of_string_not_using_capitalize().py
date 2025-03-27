# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

# function to capitalize first letter of string
def capitalize_first_letter(string):
    # convert the first letter to uppercase
    first_letter = string[0].upper()
    # convert the remaining letters to lowercase
    remaining_letters = string[1:].lower()
    # return the capitalized string
    return first_letter + remaining_letters

# ask user to input a string
# call the function and print the result