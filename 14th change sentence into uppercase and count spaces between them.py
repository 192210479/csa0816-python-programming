def process_string(string):
    # Convert the string to uppercase
    uppercase_string = string.upper()
    
    # Count the number of spaces in the string
    space_count = string.count(" ")
    
    return uppercase_string, space_count

# Input string
input_string = "Python is the interpreted language"

# Process the string
uppercase_string, space_count = process_string(input_string)

# Output the results
print("Uppercase String:", uppercase_string)
print("Number of Spaces:", space_count)
