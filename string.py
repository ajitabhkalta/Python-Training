#1st method of converting str to upper  while taking input
str1= input("Enter any string in lower case:").upper()
#lower() converts string to lower case
print(str1)
#we can use string methods with out a variable
#by directly operating on the data
print("welcome".upper())
str1 = input("Enter any string in upper case:")
str1 = str1.lower()
print(str1)
input() # Just to wait for user input
print("10".isdigit())
print("ab10".isdigit())
print("abcZ".isalpha())
print("    ".isspace())
print("  Hi   ".isspace())
print("hello123".isalnum())