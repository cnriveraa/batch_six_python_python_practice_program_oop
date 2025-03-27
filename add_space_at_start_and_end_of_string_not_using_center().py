# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# function to add space at the beginning and end of the string
def add_space_at_start_and_end_of_string(string, length):
    # calculate the number of space characters to add at the start and end
    space = length - len(string)
    # calculate the number of space characters to add at the start
    start_space = space // 2
    # calculate the number of space characters to add at the end
    end_space = space - start_space
    # add space characters at the start and end
    return ' ' * start_space + string + ' ' * end_space

# ask the user to enter a string
string = input("Enter a string: ")

# ask the user to enter the length of the string
length = int(input("Enter a number: "))

# call the function and print the result
print(add_space_at_start_and_end_of_string(string, length))