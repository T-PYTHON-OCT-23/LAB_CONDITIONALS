print("Hello my friend, measuring the enjoyment of movies!!")


name_movie= "6-underground"
rating=5
popularity=100

print(f"{name_movie}:")
if rating >= 4 and popularity>=80:
    print("Highly recommended")
elif rating == 3 and popularity>=70:
    print ("It is good")
elif rating == 2 and popularity>=60:
    print("You should check it out!")  
elif rating<1 and popularity <50:
    print("Don't watch it. It is a waste of time")
else:
    print("Never watch movies")
    
   

