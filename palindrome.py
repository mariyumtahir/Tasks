'''
Q51: Write a program that checks if a string is a palindrome. A string is a palindrome if it reads 
the same forward and backward (e.g., "madam", "racecar"). 
'''
text = input("Enter a string: ")

if text == text[::-1]:
    print ("Palindrome")
else:
    print ("Not a palindrome")