# Read the input values X and Y from the user
X, Y = map(int, input("Enter two digits (X, Y): ").split(','))

# Initialize an empty 2-dimensional array
array_2d = []

# Generate the 2-dimensional array
for i in range(X):
    row = []
    for j in range(Y):
        row.append(i * j)
    array_2d.append(row)

# Print the generated 2-dimensional array
for row in array_2d:
    print(row)

