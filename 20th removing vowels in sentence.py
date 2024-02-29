def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    without_vowels = ''.join(char for char in input_string if char not in vowels)
    return without_vowels

# Input string from the user
input_string = input("Enter a string: ")

# Remove vowels from the input string
modified_string = remove_vowels(input_string)

# Display the modified string
print("String after removing vowels:", modified_string)
 
