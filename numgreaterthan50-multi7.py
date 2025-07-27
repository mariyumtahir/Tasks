'''
Q57: Write a program that checks if a number is greater than 50 and also a multiple of 7. If both 
conditions are true, print "Condition met", else print "Condition not met". 
'''

number = int(input("Enter a number: "))

if number > 50 and number % 7 == 0:
    print("Condition met")
else:
    print("Condition not met")