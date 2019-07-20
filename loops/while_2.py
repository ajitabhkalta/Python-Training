import time
temp=int(input("Enter temperature:"))
while temp>0:
    while temp>22:
        print("INFO:AC is turned on")
        time.sleep(2) #sleep for one second
        temp-=2
    else:
        print(f"INFO:Temperature is under control:{temp}")
        time.sleep(4) #sleep for 1 sec
        temp-=2
else:
    print("Warning: Oops Need a heater now")
