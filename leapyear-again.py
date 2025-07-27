'''
Q50: Write a program that asks for a year and checks if it's a leap year. A year is a leap year if it 
is divisible by 4, except for years that are divisible by 100, unless they are also divisible by 400. 
'''
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")