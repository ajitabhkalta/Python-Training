str1=input("Enter string:")
str2=input("Enter character to search:")
index=-1
num_times=str1.count(str2)
for _ in range(num_times):
    index=str1.find(str2,index+1)
    print(f"{str1} found at {index+1} postion")