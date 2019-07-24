str1=input("Enter any string:")
num_words=0
space_found=0
for char in str1:
    if(char == " "):
        space_found=True
        
    if((space_found == True or num_words == 0) and char!=" "):#valid character
        num_words+=1
        space_found=False
        
print(f"Number of words in {str1} are {num_words}")  



