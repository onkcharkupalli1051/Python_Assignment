# Read the input sequence of comma-separated 4-digit binary numbers from the user
input_str = input("Enter a sequence of comma-separated 4-digit binary numbers: ")

# Split the input string by commas to generate a list of binary numbers
binary_numbers = input_str.split(',')

# Initialize an empty list to store binary numbers divisible by 5
divisible_by_5 = []

# Iterate through the binary numbers and check if they are divisible by 5
for binary in binary_numbers:
    decimal_value = int(binary, 2)
    if decimal_value % 5 == 0:
        divisible_by_5.append(binary)

# Print the binary numbers divisible by 5 as a comma-separated sequence
print(','.join(divisible_by_5))
