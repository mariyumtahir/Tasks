'''
Q26: Write a program that asks for the temperature in Celsius and checks if it's below freezing 
(below 0°C) or above boiling (above 100°C), and prints an appropriate message. 
'''
temperature = float(input("Enter temperature in Celcius: "))
if temperature < 0: 
    print ("Temperature is below freezing.")
elif temperature > 100:
    print ("Temperature is above boiling.")
else: 
    print ("Temperature is in normal range.")
    