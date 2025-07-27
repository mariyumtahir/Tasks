'''
Q41: Write a program that calculates the area and perimeter of a rectangle. Take the length and 
width as input (both float). Use the formula Area = length * width and Perimeter = 2 * (length + 
width) to calculate and print both. 
'''
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)