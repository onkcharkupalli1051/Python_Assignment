# Read the input sequence of comma-separated numbers from the user
input_str = input("Enter a sequence of comma-separated numbers: ")

# Split the input string by commas to generate a list of numbers
numbers = input_str.split(',')

# Use a list comprehension to square each odd number and store in a new list
squared_odds = [str(int(num)**2) for num in numbers if int(num) % 2 != 0]

# Print the squared odd numbers as a comma-separated sequence
print(','.join(squared_odds))
