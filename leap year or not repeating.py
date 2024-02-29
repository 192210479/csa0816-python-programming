date = input("Enter the date to be checked: ")
c=date.split("/")
b = list(map(int,c))
input_year=(b[2])

if(input_year%4 == 0):
    if(input_year%100 == 0):
        if(input_year%400 == 0):
            print("%d is Leap Year" %input_year)
        else:
            print("%d is not the Leap Year" %input_year)
    else:
        print("%d is the Leap Year" %input_year)
else:
    print("%d is not the Leap Year" %input_year)

x=input_year%4
if x!=0:
    print("Previous year:", input_year-1)
else:
    print("Next year:",input_year+1)
