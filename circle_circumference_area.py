'''
Q42: Write a program that takes the radius of a circle as input (float), calculates and prints the 
circumference and area of the circle. Use the formulas Circumference = 2 * π * radius and Area 
= π * radius^2. 
'''
pi = 3.14
radius = float(input("Enter the radius of the circle: "))

circumference = 2 * pi * radius
area = pi * radius ** 2

print("Circumference of the circle:", round(circumference, 2))
print("Area of the circle:", round(area, 2))