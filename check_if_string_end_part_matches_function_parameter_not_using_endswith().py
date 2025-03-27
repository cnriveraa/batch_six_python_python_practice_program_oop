# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# function that checks if the string end part matches the function parameter
def check_if_string_end_part_matches_function_parameter(string, end_part):
    if string[-len(end_part):] == end_part:
        print("The string end part matches the function parameter.")
        return True
    else:
        print("Not a match.")
        return False

# ask the user to input a string
# ask the user to input an end part
# call the function and print the result