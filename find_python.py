'''
Q31: Write a program that asks for a string input and checks if the string contains the word 
"Python". If it does, print "Found Python!", otherwise print "Python not found". 
'''
text = input("Enter a string: ")
if "Python" in text:
    print("Found Python!")
else:
    print("Python not found")