def make_sandwitch(val):
    print(val)
    x={1:"Take two bread slices",
       2:"Apply green chutney on one side of each slice",
       3:"Place onion and tomato slices",
       4:"Grate the cheese",
       5:"Add extra cheese optional :)",
       6:"Yummy!!! Your sandwitch is ready"
      }
    step=0
    for _ in range(len(x)):
        step = yield
        if step != None:
            print(str(step)+")"+x[step])

sandwitch = make_sandwitch("Sandwitch_Recipie")
#next(sandwitch) #this is mandatory or send none for first time
sandwitch.send(None)
i=0
while True:
    try:
        step = input("Enter step number or press enter")
        if not step:
            i+=1
            step=str(i)
        sandwitch.send(int(step))
        
    except StopIteration:
        break
          