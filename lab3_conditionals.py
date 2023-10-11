print("Wlcome to the rating Toy Story movie!")
movie_name = "Toy Story"
rating = 3
popularity_score = 72.65
print(f"The rating of the movie out of 5:{rating}")
print(f"popularity score: {popularity_score}")

if rating >= 4 and popularity_score> 80:
    print("Highly recommended")
elif rating >= 3 and popularity_score > 70:
    print("I recommended it . It is good!")
elif rating < 2 and popularity_score < 60:
    print("You should check it out!")
elif rating < 2 and popularity_score < 50:
    print("Don't watch it. It is a waste of time")

