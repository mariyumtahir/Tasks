'''
Q40: Write a program that takes a string input. If the string contains more than 5 characters, 
slice and print the first 3 characters. If it contains 5 or fewer characters, print the string in 
reverse. 
'''
text = input("Enter a string: ")
if len(text) > 5:
    print("First 3 characters:", text[:3])
else:
    print("Reversed string:", text[::-1])