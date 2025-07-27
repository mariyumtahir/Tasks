'''
Q45: Write a program that checks if a given number is a prime number. A prime number is 
greater than 1 and divisible only by 1 and itself. Print "Prime" if it is prime and "Not Prime" 
otherwise. 
'''
num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")