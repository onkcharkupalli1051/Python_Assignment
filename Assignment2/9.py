# Read multiple lines of input from the user
lines = []
while True:
    line = input("Enter a line (or press Enter to finish): ")
    if not line:
        break
    lines.append(line)

# Convert and print the lines in uppercase
for line in lines:
    print(line.upper())
