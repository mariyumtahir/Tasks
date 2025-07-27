'''
Q20: Write a program that takes a string input, checks if its length is greater than 5, and if so, 
prints the first three characters. If its length is 5 or less, print the string in lowercase. 
'''
str = input("Enter a string: ")
if len(str) > 5:
    print ( "first 3 characters :", str[:3])
else:
    print ("lowercase string :", str.lower())