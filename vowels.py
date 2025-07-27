'''
Q52: Write a program that removes all vowels from a string and prints the resulting string. For 
example, given the string "hello", it should print "hll". 
'''
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""

for char in text:
    if char not in vowels:
        result += char

print("String without vowels:", result)