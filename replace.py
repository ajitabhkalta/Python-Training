str1="$"
#str2 = ("h","i","j")
str2="hello" #h$e$l$l$o
#alternate way not recommended because of complexity
print(str2[0]+str1+str2[1]+str1+str2[2]+str1+str2[3]+str1+str2[4])

print(str1.join(str2))
print("-".join(str2))
input()
str3 = input("Enter any string:")
old = input("Enter the old string:")
new = input("enter new string:")
print(str3.replace(old,new))
# # # #only one occurence will be replaced
print(str3.replace(old,new,2))
input()
print(min("Ajitabh"))
print(max("Hello","Hi"))
input()
str1 = " I want to learn I want to explore I want to Implement I want to get a job I want to have experience"
print(str1.count("I"))
print(str1.count("I",5,48))