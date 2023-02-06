#String slicing
# Syntax =
# string [start : end : step]

my_string = "This is my string!"

print(my_string[0:4]) # The default for the step is always 1 + Always add 1 to the last number
print(my_string[0:4:2]) # Step:2 means it will skip every 2 steps
print(my_string[:]) # Prints everything
print(my_string[4:]) # cuts out the first 4 letter.
print(my_string[:10]) # starts from the beginning and ends on the 10th number 
