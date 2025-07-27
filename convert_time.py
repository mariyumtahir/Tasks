'''
Q23: Take an integer input representing the number of seconds, then convert it to hours, 
minutes, and seconds (for example, 3665 seconds = 1 hour, 1 minute, 5 seconds). 
'''

total_seconds = int(input("Enter number of seconds: "))
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print (total_seconds,  "seconds = ", hours, "hour", minutes, "minutes", seconds, "seconds")