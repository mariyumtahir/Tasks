'''
Q49: Write a program that asks for a score and checks whether it's in the following range: 
90-100 = "Excellent" 
75-89 = "Good" 
50-74 = "Pass" 
Below 50 = "Fail" 
'''
score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("Excellent")
elif 75 <= score <= 89:
    print("Good")
elif 50 <= score <= 74:
    print("Pass")
else:
    print("Fail")