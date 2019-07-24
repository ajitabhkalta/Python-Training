import random  

for _ in range(10):  
    x = random.randint(-5,5)  
    if x == 0: 
        print("Continuing for val 0")
        continue 
    print(1/x)