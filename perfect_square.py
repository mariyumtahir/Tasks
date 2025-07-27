'''
Q46: Write a program that asks for a number and checks if it is a perfect square. If it is, print 
"Perfect square", otherwise print "Not a perfect square". 
'''

num = int(input("Enter a number: "))

if num >= 0 and int(num ** 0.5) ** 2 == num:
    print("Perfect square")
else:
    print("Not a perfect square")