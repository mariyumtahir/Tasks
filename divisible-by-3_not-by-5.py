'''
Q47: Write a program that asks for a number and checks if it is divisible by 3 but not by 5. If 
true, print "Divisible by 3 but not by 5", else print "Not divisible by 3 or divisible by 5". 
'''
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 != 0:
    print("Divisible by 3 but not by 5")
else:
    print("Not divisible by 3 or divisible by 5")