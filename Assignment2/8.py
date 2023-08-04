# Read the input sequence of words from the user
input_str = input("Enter a comma-separated sequence of words: ")

# Split the input string by commas to generate a list of words
words = input_str.split(',')

# Sort the list of words alphabetically
sorted_words = sorted(words)

# Print the sorted words as a comma-separated sequence
print(','.join(sorted_words))
