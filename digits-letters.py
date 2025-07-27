'''
Q60: Write a program that takes a string as input and checks if it contains both digits and letters. 
If true, print "Contains both digits and letters", otherwise print "Doesn’t contain both".
'''
text = input("Enter a string: ")

if text.isalpha():
    print("Doesn’t contain both")
elif text.isdigit():
    print("Doesn’t contain both")
else:
    print("Contains both digits and letters")