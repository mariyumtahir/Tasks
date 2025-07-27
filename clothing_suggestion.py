'''
Q30: Write a program that checks the temperature and prints the appropriate clothing 
suggestion: Below 0°C = "Wear a heavy jacket", 0-10°C = "Wear a coat", 10-20°C = "Wear a 
sweater", above 20°C = "Wear a t-shirt". 
'''
temperature = float(input("Enter the temperature in Celsius: "))
if temperature < 0:
    print("Wear a heavy jacket")
elif 0 <= temperature <= 10:
    print("Wear a coat")
elif 10 < temperature <= 20:
    print("Wear a sweater")
else:
    print("Wear a t-shirt")