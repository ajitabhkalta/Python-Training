match1= {"sachin":100,"virat":50,"sehwag":55}
pl_name = input("Enter player name to fetch the score:")
print(f"score done by {pl_name} is {match1[pl_name]}")
input()
#Dict with tuple as value
match2 = {"sachin":(100,2,3),"virat":(50,0,4),"sehwag":(55,0,3)}
option = input("Enter s/w/c to display values:")
score,wickets,catches=match2[pl_name] #unpack vals in to objects
if option == "s":
    print(f"score done by {pl_name} is {score}")
elif option == "c":
    print(f"catches caught by {pl_name} is {catches}")
elif option == "w":
    print(f"wickets taken by {pl_name} is {wickets}")
else:
    print("Invalid option provided\n No data found")  