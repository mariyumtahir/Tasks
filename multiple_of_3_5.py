'''
Q25: Write a program that takes a number and checks if it is a multiple of 3 and 5. If it is, print 
"Multiple of both". If it's only a multiple of 3, print "Multiple of 3", if it's only a multiple of 5, print 
"Multiple of 5", else print "Not a multiple". 
'''
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print ("Multiple of both.")
elif number % 3 == 0:
    print ("Multiple of 3.")
elif number % 5 == 0:
    print ("Multiple of 5.")
else:
    print ("Not a multiple.")