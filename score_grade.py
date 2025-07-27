'''
Q29: Write a program that checks the score of a student and prints the grade based on the 
following conditions: 90-100 = "A", 80-89 = "B", 70-79 = "C", 60-69 = "D", below 60 = "F". 
'''
score = int(input("Enter the student's score (0–100): "))
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
elif 60 <= score <= 69:
    print("Grade: D")
elif 0 <= score < 60:
    print("Grade: F")
else:
    print("Invalid score. Please enter a numbe between 0 and 100.")