'''
Q44: Given a string containing a decimal number with many decimal places (e.g., 
"3.14159265359"), convert it to a float, round it to 2 decimal places, and print the result. 
'''
decimal_string = input("Enter a decimal number: ")
decimal_number = float(decimal_string)
rounded_number = round(decimal_number, 2)

print("Rounded number:", rounded_number)