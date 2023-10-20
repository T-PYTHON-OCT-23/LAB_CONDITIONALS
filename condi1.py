# Create a variable for the movie
movie = "The Mother (2023) "
print(movie)
#Create a variable of type int to hold the rating of the movie out of 5 . Give this movie 3
movie_rating = int(input("Rrating of the movie : "))
print(movie_rating)

#Create a popularity score of type float , let it be 72.65
popularity_float=72.65
print(popularity_float)

popularity = float(input("popularity : "))
print(popularity)

#Check if the movie rating is 4 or greater and the popularity is greater than 80 , print "Highly recommended"
i= float (input(" enter your rating of the movie "))

if 4 <= i < 80 :
    print("Highly recommended")

#else if the movie rating is 3 or greater and the popularity is greater than 70 , print "I recommended it . It is good"
elif 3 <= i  < 70 :
      print("I recommended it . It is good")


elif 2 <= i <= 50  :
  print("You should check it out!")
 #else the movie rating is 2 or less and the popularity is less than 50 , print "Don't watch it. It is a waste of time"   
else:
    print("Don't watch it. It is a waste of time")    

   #else if the movie rating is 2 or less and the popularity is greater than 60 , print "You should check it out!"