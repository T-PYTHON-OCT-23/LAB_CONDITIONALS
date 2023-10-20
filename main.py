# LAB_CONDITIONALS

movie:str  = "Cinderella " 
rate :int  = 3
popularity : float = 72.65

print("the movie is :" ,movie)
print("the rating is :", rate)
print("the popularity is :", popularity)
print("-"*19)

if rate >= 4 and popularity >= 80 :
    print("Highly recommended")
elif rate >= 3 and popularity >= 70 :
    print ("I recommended it . It is good")
elif rate <= 2 and popularity >= 60 :
    print ("You should check it out!")
elif rate <= 1 and popularity >= 50 :
    print ("Don't watch it. It is a waste of time")

