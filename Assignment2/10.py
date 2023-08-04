# Read the input sequence of whitespace-separated words from the user
input_str = input("Enter a sequence of whitespace-separated words: ")

# Split the input string by whitespace to generate a list of words
words = input_str.split()

# Use a set to remove duplicate words while maintaining order
unique_words = list(set(words))

# Sort the list of unique words alphanumerically
sorted_unique_words = sorted(unique_words)

# Print the sorted unique words
print(' '.join(sorted_unique_words))
