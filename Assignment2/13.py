# Read the input sentence from the user
input_sentence = input("Enter a sentence: ")

# Initialize counters for letters and digits
num_letters = 0
num_digits = 0

# Iterate through each character in the input sentence
for char in input_sentence:
    if char.isalpha():
        num_letters += 1
    elif char.isdigit():
        num_digits += 1

# Print the counts of letters and digits
print("LETTERS", num_letters)
print("DIGITS", num_digits)
