# Zomato 
# 1 - 5 
# 1 2 -> low
# 3 4 -> medium
# 5 -> excellent

rating = int(input("Please rate the delivery boy"))
if(rating == 1):
    print("Too Low")
    rating = 2
elif(rating == 2):
    print("Low")
    rating = 3
elif(rating == 3):
    print("Good")
    rating = 4
elif(rating == 4):
    print("Doing Great")
    rating = 5
elif(rating == 5):
    print("Promotion")
    rating = 6
else:
    print("Error !")
