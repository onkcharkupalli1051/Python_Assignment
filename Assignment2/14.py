# Read the input sentence from the user
input_sentence = input("Enter a sentence: ")

# Initialize counters for uppercase and lowercase letters
num_uppercase = 0
num_lowercase = 0

# Iterate through each character in the input sentence
for char in input_sentence:
    if char.isupper():
        num_uppercase += 1
    elif char.islower():
        num_lowercase += 1

# Print the counts of uppercase and lowercase letters
print("UPPER CASE", num_uppercase)
print("LOWER CASE", num_lowercase)
