'''
Q43: Take an input number in string format (e.g., "45.67") and cast it to both float and integer 
types. Print the results of both conversions and their sum. 
'''
number = input("Enter number: ")

float_number = float(number)
integer_number = int(number)

print ("float_number = ", float_number)
print ("integer_number = ", integer_number)
print ("sum = ", float_number + integer_number)