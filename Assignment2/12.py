# Initialize an empty list to store the numbers
result = []

# Iterate through the range of numbers from 1000 to 3000 (both inclusive)
for num in range(1000, 3001):
    # Convert the number to a string to access each digit
    num_str = str(num)

    # Check if all digits of the number are even
    if all(int(digit) % 2 == 0 for digit in num_str):
        result.append(num)

# Print the numbers as a comma-separated sequence on a single line
print(','.join(map(str, result)))
