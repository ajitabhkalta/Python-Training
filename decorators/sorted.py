d={"Ramesh":13,"Suresh":4,"Mahesh":18,"Puneeth":6}
print(sorted(d))
print("Default sort option")
print(dict(sorted(d.items())))
print("Custom sort func option")
print(dict(sorted(d.items(),reverse = True,key=lambda val:val[1])))