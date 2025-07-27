'''
Q48: Write a program that asks for a number and checks if it’s greater than 100 but less than 
500. If it is, print "Within range", else print "Out of range". 
'''
number = int(input("Enter a number: "))

if number > 100 and number < 500:
    print("Within range")
else:
    print("Out of range")