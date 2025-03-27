# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# define a function that accepts a string and a number as parameter
def add_space_at_end_of_string(string, length):
    return string + ' ' * (length - len(string))

# ask user to input a string
string = input("Enter a string: ")

# ask user to input a number
# call the function and pass the string and number as parameter