'''
Q19: Write a program that asks for a number input. If the number is greater than 10, check if it's 
even or odd. If it’s even, print "Even number greater than 10", else print "Odd number greater 
than 10". If the number is less than or equal to 10, print "Number is 10 or less". 
'''
number = int(input("Enter a number: "))
if number > 10:
    if number % 2 == 0:
        print ("Even number greater than 10")
    else:
        print("Odd number greater than 10")
else:
    print("Number is 10 or less")
