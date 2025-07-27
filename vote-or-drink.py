'''
Q58: Write a program that asks for the age of a person and checks if they are eligible to vote or 
drink. If they are 18 or older, print "Eligible to vote and drink", else print "Not eligible". 
'''

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote and drink")
else:
    print("Not eligible")