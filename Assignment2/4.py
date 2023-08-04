
######## Q4 #############

str = input("Enter comma-separated number string: ")

# Split the input string by commas to generate a list of numbers
num_list = str.split(',')

# Create a tuple from the generated list
num_tuple = tuple(num_list)

# Print the list and the tuple
print(num_list)
print(num_tuple)
