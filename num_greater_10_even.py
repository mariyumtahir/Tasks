'''
Q37: Write a program that asks for a number and checks if it is greater than 10 and even. If both 
conditions are true, print "Greater than 10 and even", else print "Not greater than 10 and even". 
'''
number = int(input("Enter a number: "))
if number > 10 and number % 2 == 0:
    print("Greater than 10 and even")
else:
    print("Not greater than 10 and even")