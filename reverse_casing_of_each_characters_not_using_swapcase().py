# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# function to reverse the casing of each character of the string
def reverse_casing_of_each_characters(string):
    result =''
    for char in string:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result
 
# ask user to input a string
string = input("Enter a string in any casing: ")

# call the function and print the result
print(reverse_casing_of_each_characters(string))