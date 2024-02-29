def square_and_cube(number):
    square=number**2
    cube=number**3
    return square,cube
number=int(input("enter a number"))
square,cube=square_and_cube(number)
print("square of the number is:",square)
print("cube of the number is:",cube)
