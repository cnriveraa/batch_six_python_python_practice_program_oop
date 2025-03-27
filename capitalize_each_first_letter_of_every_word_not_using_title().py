# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# function to capitalize each first letter of every word in the string   
def capitalize_each_first_lette(string):
    words = string.split()   # split the string into words
    capitalized_words = []   # create a list to store the words
    
    # loop through each word
    for word in words:
        capitalized_words.append(word[0].upper() + word[1:].lower())  # capitalize the first letter and add to the list
    return ' '.join(capitalized_words)   # join the words and return the string

# ask user to input a string
string = input("Enter a string: ")

# call the function and print the result