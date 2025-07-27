'''
Q27: Write a program that checks if a number is divisible by 7 and prints "Divisible by 7" if true. 
If not, check if it’s divisible by 11 and print "Divisible by 11". If neither, print "Neither divisible by 7 
nor 11". 
'''
number = int(input("Enter a number: "))
if number % 7 == 0:
    print("Divisible by 7")
elif number % 11 == 0:
    print("Divisible by 11")
else:
    print("Neither divisible by 7 nor 11")