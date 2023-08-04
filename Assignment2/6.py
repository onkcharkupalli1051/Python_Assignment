import math

# Fixed values of C and H
C = 50
H = 30

# Read the input sequence of comma-separated values of D from the user
input_str = input("Enter comma-separated values of D: ")

# Split the input string by commas to generate a list of D values
D_values = input_str.split(',')

# Initialize an empty list to store the calculated Q values
Q_values = []

# Calculate Q for each D value and append to the Q_values list
for D in D_values:
    Q = math.sqrt((2 * C * int(D)) / H)
    Q_values.append(round(Q))

# Print the calculated Q values as a comma-separated sequence
print(','.join(map(str, Q_values)))
