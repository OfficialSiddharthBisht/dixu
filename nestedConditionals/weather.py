raining = True
temp = 23

if(raining):
    if(temp < 25):
        print("Take umbrella and warm clothes")
    else:
        print("Take umbrella")
else:
    print("You are good to go")


# and or not 
if(raining and temp < 25):
        print("Take umbrella and warm clothes")
elif(raining):
    print("Take umbrella")
else:
    print("You are good to go")


