'''
Q59: Write a program that asks for a number and checks if it is a perfect number. A perfect 
number is a number that is equal to the sum of its divisors, excluding the number itself. (e.g., 6 
is a perfect number because 1 + 2 + 3 = 6) 
'''
num = int(input("Enter a number: "))
sum_of_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

if sum_of_divisors == num:
    print("Perfect number")
else:
    print("Not a perfect number")