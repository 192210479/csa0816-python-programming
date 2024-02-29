# Function to find the MSD of a number
def find_MSD(number):
    # Keep dividing the number by 10 until it is less than 10
    while number >= 10:
        number = number // 10
    return number

# Function to find the LSD of a number
def find_LSD(number):
    # The LSD is the remainder when the number is divided by 10
    return number % 10

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Find the MSD and LSD of the number
msd = find_MSD(num)
lsd = find_LSD(num)

# Print the results
print("Most Significant Digit:", msd)
print("Least Significant Digit:",lsd)
